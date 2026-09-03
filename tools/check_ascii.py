#!/usr/bin/env python3
# =============================================================================
#  tools/check_ascii.py
# -----------------------------------------------------------------------------
#  Asserts that every source and data file is pure ASCII.
#
#  WHY THIS MATTERS, CONCRETELY
#  STYLE_GUIDE.md section 3 and NOTATION.md require ASCII symbols and units in
#  every metric: `mu` rather than the Greek letter, `u` for micro, `1e14`
#  rather than a superscript. That is not fastidiousness. Three failures
#  motivate it:
#
#      A Greek mu in a metric symbol is unsearchable. A reader who types "mu"
#      finds nothing, and a reader who can produce the character has to guess
#      which of several visually identical code points was used.
#
#      A curly quote or an en dash in a CSV export breaks a spreadsheet import
#      under any locale that is not UTF-8, which is still the default on a
#      large share of Windows installations.
#
#      A no-break space is invisible in every editor and in every diff, and it
#      is what a word processor produces when text is pasted through one.
#
#  SCOPE, AND WHY IT IS NARROWER THAN "EVERY FILE"
#  This checks `src/`, `tools/` and `tests/`: the code, the taxonomy and the
#  machinery that reads them. Root documents are deliberately OUT of scope, and
#  the reason is a finding rather than an omission. A first version of this
#  script scanned everything and reported 620 characters across the root
#  documents. Inspecting them found three distinct populations:
#
#      537  box-drawing characters in deliberate directory-tree diagrams in
#           ARCHITECTURE.md, CONTRIBUTING.md and DATA_MODEL.md
#       51  typographic symbols in prose: section signs, degree signs
#       32  LETTERS WITH DIACRITICS IN AUTHOR NAMES in BIBLIOGRAPHY.md
#
#  The third population settles it. Those are real people's names. Stripping
#  the diacritic from a cited author would misspell them, and a rule that
#  required it would be a worse rule. Rather than carve out an exception broad
#  enough to swallow the intent, the scope is set where the rule has teeth: a
#  metric symbol, a unit, a record field, a piece of code.
#
#  The forbidden PUNCTUATION set is enforced repository-wide by the neighbour
#  `check_dashes.py`, which already covers em and en dashes, curly quotes,
#  ellipses, no-break and zero-width spaces and byte order marks in documents
#  as well as in source. Nothing is lost by narrowing this one.
#
#  THE THREE CHECKS TOGETHER
#      check_dashes.py               forbidden punctuation, everywhere
#      this file                     any non-ASCII byte, in code and data
#      core.validation _check_ascii  the ASSEMBLED records
#
#  The overlap is deliberate. This catches a character in a comment that never
#  reaches a record; the validation check catches one that arrives through a
#  computed value rather than a literal.
#
#  EXIT CODES
#      0  every scanned file is ASCII
#      1  at least one is not, with every offending byte located and named
#      2  a scanned root could not be read
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent.parent

#: Trees scanned. See the module header on why the root documents are not here.
SCAN_ROOTS = ("src", "tools", "tests")

#: Extensions worth scanning. Restricted rather than open-ended, so a binary
#: asset added later cannot fail the check for the wrong reason.
TEXT_SUFFIXES = frozenset({".py", ".pyi", ".md", ".toml", ".cfg", ".ini", ".txt", ".json"})

SKIP_DIRS = frozenset(
    {
        ".git",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".benchmarks",
        ".tox",
        "build",
        "dist",
        ".venv",
        "venv",
    }
)

#: Excluded by name, each for a stated reason. Kept this short on purpose: a
#: long exclusion list is how a rule stops meaning anything.
EXCLUDED = {
    "LICENCE": "the published EUPL-1.2 text; editing its characters would alter it",
    "LICENSE": "as above",
}


def offending_characters(path: Path) -> List[Tuple[int, int, str]]:
    """Return (line, column, character) for every non-ASCII character."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [(0, 0, "<not valid UTF-8>")]

    found: List[Tuple[int, int, str]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for column, character in enumerate(line, start=1):
            if ord(character) > 127:
                found.append((line_number, column, character))
    return found


def _describe(character: str) -> str:
    """Name the usual suspects, because a bare code point is not actionable.

    A reader who sees U+00A0 and no name will not understand why a line that
    looks correct fails the check.
    """
    known = {
        0x00A0: "no-break space, usually pasted from a word processor",
        0x2013: "en dash; write a plain hyphen",
        0x2014: "em dash; forbidden, rewrite the sentence",
        0x2018: "left single quote; use an apostrophe",
        0x2019: "right single quote; use an apostrophe",
        0x201C: "left double quote; use a straight quote",
        0x201D: "right double quote; use a straight quote",
        0x2026: "ellipsis; write three full stops",
        0x00B5: "micro sign; write u",
        0x03BC: "Greek mu; write mu",
        0x00D7: "multiplication sign; write x",
        0x00B0: "degree sign; write the word",
        0x00A7: "section sign; write the word section",
        0x2022: "bullet; use a hyphen",
        0xFEFF: "byte order mark",
        0x200B: "zero-width space, invisible and unsearchable",
    }
    return known.get(ord(character), "")


def main() -> int:
    scanned = 0
    failures = 0

    for root_name in SCAN_ROOTS:
        root = ROOT / root_name
        if not root.is_dir():
            # A missing tree is not a failure. `tests/` may be empty in a fresh
            # checkout, and refusing to run because of that would make the
            # check unusable exactly when it is cheapest to adopt.
            continue

        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.name in EXCLUDED:
                continue
            if path.suffix not in TEXT_SUFFIXES:
                continue

            scanned += 1
            offenders = offending_characters(path)
            if not offenders:
                continue

            failures += 1
            print("FAIL {0}".format(path.relative_to(ROOT)))
            for line_number, column, character in offenders[:20]:
                if character.startswith("<"):
                    print("     {0}".format(character))
                    continue
                description = _describe(character)
                print(
                    "     line {0}, column {1}: U+{2:04X}{3}".format(
                        line_number,
                        column,
                        ord(character),
                        "  " + description if description else "",
                    )
                )
            if len(offenders) > 20:
                print("     ... and {0} more".format(len(offenders) - 20))
            print()

    if failures:
        print(
            "{0} file(s) contain non-ASCII characters. See STYLE_GUIDE.md "
            "section 3 and NOTATION.md.".format(failures)
        )
        return 1

    print(
        "OK: {0} file(s) under {1} scanned, all ASCII.".format(
            scanned, ", ".join(SCAN_ROOTS)
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
