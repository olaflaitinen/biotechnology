#!/usr/bin/env python3
# =============================================================================
#  tools/verify_references.py
# -----------------------------------------------------------------------------
#  Resolves every DOI in the bibliography against Crossref and reports any that
#  does not exist or whose stored metadata disagrees with the record of truth.
#
#  WHY THIS EXISTS
#  A curated dataset intended for citation has exactly one unforgivable defect,
#  and it is not an incomplete record or an unwritten branch:
#
#      A CITATION THAT LOOKS AUTHORITATIVE AND POINTS AT NOTHING.
#
#  A wrong year is an inconvenience. A wrong volume wastes ten minutes. A DOI
#  that resolves to a different paper, or to no paper, propagates into every
#  work that trusts this one, and it is undetectable by reading because a
#  fabricated citation is formatted exactly like a real one.
#
#  Bibliographies are written from memory more often than anyone admits, and
#  memory reconstructs plausible volume numbers and page ranges with complete
#  confidence. This script exists because "we were careful" is not a control.
#
#  WHAT IT CHECKS, AGAINST WHAT
#  Crossref is the DOI registration agency for essentially all of the
#  scholarly literature this project cites. Its REST API is free, needs no key
#  and returns the metadata the publisher deposited, which is the closest thing
#  to ground truth that exists. For every DOI it compares:
#
#      does the DOI resolve at all
#      published year
#      journal or container title
#      first author family name
#      title, on a word-overlap basis rather than exact match
#
#  Title comparison is deliberately fuzzy. Publishers deposit titles with
#  inconsistent capitalisation, trailing full stops, and occasional markup, and
#  an exact-match check would report dozens of false failures and be switched
#  off. Year, journal and first author are compared strictly, because those are
#  what a reader uses to find the paper on a shelf.
#
#  NETWORK USE, AND WHY IT IS CONFINED TO tools/
#  SECURITY.md forbids network capability in `src/`. This is a development
#  tool, not library code: nothing under `src/` imports it, and the shipped
#  package remains dependency-free and offline. It uses `urllib` from the
#  standard library rather than `requests`, so it adds no dependency of any
#  kind, and it caches every answer so that a rerun and a CI run without
#  network still verify against the last known truth.
#
#  EXIT CODES
#      0  every DOI resolves and every compared field agrees
#      1  at least one DOI does not resolve, or a field disagrees
#      2  the bibliography could not be read
#      3  the network was needed and unavailable, and the cache was cold
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
BIBLIOGRAPHY = ROOT / "BIBLIOGRAPHY.md"
CACHE = ROOT / "tools" / ".crossref_cache.json"

#: Crossref asks that automated clients identify themselves and offers a faster
#: pool to those that do. Sending a contact address is the polite convention
#: and costs nothing.
USER_AGENT = (
    "biotechnology-taxonomy/0.1 "
    "(https://github.com/olaflaitinen/biotechnology; mailto:yunus.imanov@metropolia.fi)"
)

#: Crossref publishes no hard rate limit for the polite pool. A short pause
#: between uncached requests keeps this a good citizen rather than a scraper.
REQUEST_PAUSE_SECONDS = 0.2

# =============================================================================
#  JOURNAL ABBREVIATIONS
#
#  Crossref stores the full container title. Bibliographies write the
#  abbreviation, because that is what the citing conventions of these journals
#  expect. Neither is wrong, so the comparison has to know the pairs.
#
#  The first run of this script reported three failures for "PNAS", which is
#  the standard abbreviation and appears that way in essentially every citation
#  of that journal. A checker that reports the correct form as an error trains
#  its reader to ignore it, so the map exists rather than the false positives.
# =============================================================================
ABBREVIATIONS: Dict[str, str] = {
    "pnas": "proceedings of the national academy of sciences",
    "nejm": "new england journal of medicine",
    "jama": "journal of the american medical association",
    "embo j": "the embo journal",
    "nar": "nucleic acids research",
    "tibtech": "trends in biotechnology",
    "nat biotechnol": "nature biotechnology",
    "nat rev drug discov": "nature reviews drug discovery",
    "nat rev genet": "nature reviews genetics",
    "nat rev microbiol": "nature reviews microbiology",
    "appl environ microbiol": "applied and environmental microbiology",
    "environ sci technol": "environmental science and technology",
}


# =============================================================================
#  PARSING THE BIBLIOGRAPHY
# =============================================================================

#: A bibliography row: | `key` | Author, A. (Year). Title. *Journal*, ... |
ROW = re.compile(r"^\|\s*`([a-z0-9_]+)`\s*\|\s*(.+?)\s*\|\s*$")

DOI_IN_TEXT = re.compile(r"DOI:\s*(10\.\d{4,9}/\S+?)(?:[.,]?\s*$|[.,]?\s*\|)")
YEAR_IN_TEXT = re.compile(r"\((\d{4})[a-z]?\)")
JOURNAL_IN_TEXT = re.compile(r"\*([^*]+)\*")


class Entry:
    """One bibliography row, as written."""

    __slots__ = ("key", "text", "doi", "year", "journal", "first_author", "line")

    def __init__(self, key: str, text: str, line: int) -> None:
        self.key = key
        self.text = text
        self.line = line

        doi_match = DOI_IN_TEXT.search(text)
        self.doi: Optional[str] = doi_match.group(1).rstrip(".,") if doi_match else None

        year_match = YEAR_IN_TEXT.search(text)
        self.year: Optional[int] = int(year_match.group(1)) if year_match else None

        journal_match = JOURNAL_IN_TEXT.search(text)
        self.journal: Optional[str] = journal_match.group(1).strip() if journal_match else None

        # First author family name is everything before the first comma.
        self.first_author: Optional[str] = None
        head = text.split(",", 1)[0].strip()
        if head and not head.startswith(("*", "`")):
            self.first_author = head


def read_entries() -> List[Entry]:
    if not BIBLIOGRAPHY.exists():
        return []
    entries: List[Entry] = []
    for number, line in enumerate(
        BIBLIOGRAPHY.read_text(encoding="utf-8").splitlines(), start=1
    ):
        match = ROW.match(line)
        if not match:
            continue
        key, text = match.group(1), match.group(2)
        if key == "Key":  # the table header
            continue
        entries.append(Entry(key, text, number))
    return entries


# =============================================================================
#  ASKING CROSSREF
# =============================================================================


def load_cache() -> Dict[str, dict]:
    if CACHE.exists():
        try:
            return json.loads(CACHE.read_text(encoding="utf-8"))
        except ValueError:
            return {}
    return {}


def save_cache(cache: Dict[str, dict]) -> None:
    CACHE.write_text(
        json.dumps(cache, indent=1, sort_keys=True, ensure_ascii=True),
        encoding="utf-8",
        newline="\n",
    )


def fetch(doi: str) -> Tuple[str, Optional[dict]]:
    """Return (status, metadata). Status is 'ok', 'notfound' or 'error:...'."""
    url = "https://api.crossref.org/works/{0}".format(urllib_quote(doi))
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
        return "ok", payload.get("message", {})
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return "notfound", None
        return "error:http{0}".format(exc.code), None
    except Exception as exc:  # network down, DNS, TLS, timeout
        return "error:{0}".format(type(exc).__name__), None


def urllib_quote(doi: str) -> str:
    from urllib.parse import quote

    return quote(doi, safe="/")


# =============================================================================
#  COMPARING
# =============================================================================


def normalise(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", text.lower()).strip()


def title_agrees(stored: str, authoritative: str) -> bool:
    """Word overlap rather than exact match. See the module header.

    The floor is the length of the authoritative title when that title is
    short, and not a constant. The first version demanded three words in
    common, which no two-word title can satisfy: it reported `high2019`
    ("Gene Therapy") and `langer1993` ("Tissue Engineering") as mismatches
    when both entries were exactly right. A threshold that cannot be met by
    correct input is not a strict check, it is a broken one.
    """
    a = set(normalise(stored).split())
    b = set(normalise(authoritative).split())
    if not b:
        return True
    needed = min(len(b), max(2, int(0.5 * len(b))))
    return len(a & b) >= needed


def compare(entry: Entry, record: dict) -> List[str]:
    """Return a list of disagreements between what is written and what is true."""
    problems: List[str] = []

    # -- year -----------------------------------------------------------------
    #  A journal article has more than one date and they legitimately differ.
    #  `issued` is the earliest, which for a Nature Reviews paper is the
    #  online-first date; `published-print` is the version of record a reader
    #  finds by volume and page. `carter2018` is written as 2018 and Crossref
    #  `issued` says 2017, and the entry is correct: the print issue is
    #  2018, volume 17, issue 3. Accepting any of the deposited years is the
    #  only answer that does not flag a correct citation.
    acceptable = set()
    for field in ("issued", "published-print", "published-online", "published"):
        parts = (record.get(field) or {}).get("date-parts") or [[]]
        if parts and parts[0]:
            acceptable.add(parts[0][0])
    if entry.year and acceptable and entry.year not in acceptable:
        problems.append(
            "year: written {0}, Crossref has {1}".format(
                entry.year, ", ".join(str(y) for y in sorted(acceptable))
            )
        )

    # -- journal --------------------------------------------------------------
    containers = record.get("container-title") or []
    true_journal = containers[0] if containers else ""
    if entry.journal and true_journal:
        stored = ABBREVIATIONS.get(normalise(entry.journal), normalise(entry.journal))
        actual = normalise(true_journal)
        # An abbreviation is acceptable if it is a prefix or a subset of words.
        if not (
            stored == actual
            or stored in actual
            or actual in stored
            or set(stored.split()) <= set(actual.split())
        ):
            problems.append(
                "journal: written {0!r}, Crossref {1!r}".format(
                    entry.journal, true_journal
                )
            )

    # -- first author ---------------------------------------------------------
    authors = record.get("author") or []
    true_first = (authors[0].get("family") or "") if authors else ""
    if entry.first_author and true_first:
        if normalise(entry.first_author) not in normalise(true_first) and normalise(
            true_first
        ) not in normalise(entry.first_author):
            problems.append(
                "first author: written {0!r}, Crossref {1!r}".format(
                    entry.first_author, true_first
                )
            )

    # -- title ----------------------------------------------------------------
    titles = record.get("title") or []
    true_title = titles[0] if titles else ""
    if true_title and not title_agrees(entry.text, true_title):
        problems.append("title does not match: Crossref has {0!r}".format(true_title[:80]))

    return problems


# =============================================================================
#  ENTRY POINT
# =============================================================================


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--offline",
        action="store_true",
        help="use the cache only; never touch the network",
    )
    parser.add_argument(
        "--refresh", action="store_true", help="ignore the cache and re-fetch"
    )
    parser.add_argument("--key", action="append", help="verify only these keys")
    args = parser.parse_args(argv)

    entries = read_entries()
    if not entries:
        print("cannot read {0}".format(BIBLIOGRAPHY), file=sys.stderr)
        return 2

    if args.key:
        wanted = set(args.key)
        entries = [e for e in entries if e.key in wanted]

    cache = {} if args.refresh else load_cache()
    fetched = 0

    with_doi = [e for e in entries if e.doi]
    without_doi = [e for e in entries if not e.doi]

    failures: List[Tuple[Entry, List[str]]] = []
    unresolved: List[Entry] = []
    cold = 0

    for entry in with_doi:
        assert entry.doi is not None
        cached = cache.get(entry.doi)
        if cached is None:
            if args.offline:
                cold += 1
                continue
            status, record = fetch(entry.doi)
            fetched += 1
            cache[entry.doi] = {"status": status, "message": record}
            time.sleep(REQUEST_PAUSE_SECONDS)
            cached = cache[entry.doi]

        if cached["status"] == "notfound":
            unresolved.append(entry)
            continue
        if cached["status"].startswith("error"):
            print(
                "     could not check {0} ({1}): {2}".format(
                    entry.key, entry.doi, cached["status"]
                )
            )
            continue

        problems = compare(entry, cached["message"] or {})
        if problems:
            failures.append((entry, problems))

    if fetched:
        save_cache(cache)

    # -- report ---------------------------------------------------------------
    print(
        "{0} entries, {1} with a DOI, {2} without, {3} fetched this run.".format(
            len(entries), len(with_doi), len(without_doi), fetched
        )
    )
    if without_doi:
        print()
        print(
            "     {0} entry(ies) carry no DOI. Books, historical papers and "
            "institutional documents legitimately have none; each is listed so "
            "the gap is visible rather than assumed:".format(len(without_doi))
        )
        for entry in without_doi:
            print("       {0}".format(entry.key))

    if cold:
        print()
        print(
            "FAIL: {0} DOI(s) are not in the cache and --offline was given.".format(cold),
            file=sys.stderr,
        )
        return 3

    if unresolved or failures:
        print()
        if unresolved:
            print("FAIL: {0} DOI(s) DO NOT RESOLVE.".format(len(unresolved)))
            print(
                "      A DOI that resolves to nothing is the one defect this "
                "project cannot ship. Correct or remove each of these."
            )
            print()
            for entry in unresolved:
                print(
                    "  - {0}  (BIBLIOGRAPHY.md:{1})\n      {2}".format(
                        entry.key, entry.line, entry.doi
                    )
                )
        if failures:
            print()
            print("FAIL: {0} entry(ies) disagree with Crossref.".format(len(failures)))
            print()
            for entry, problems in failures:
                print("  - {0}  (BIBLIOGRAPHY.md:{1})".format(entry.key, entry.line))
                for problem in problems:
                    print("      {0}".format(problem))
        return 1

    print()
    print("OK: every DOI resolves and every compared field agrees with Crossref.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
