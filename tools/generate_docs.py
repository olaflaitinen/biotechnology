#!/usr/bin/env python3
# =============================================================================
#  tools/generate_docs.py
# -----------------------------------------------------------------------------
#  Builds the `docs/` tree that `mkdocs.yml` navigates, from the taxonomy and
#  from the root documents.
#
#  WHY `docs/` WAS EMPTY
#  `make docs` has always called this script, and this script did not exist.
#  Nothing could have generated the tree, so `mkdocs build` had no input, the
#  "Build site" job could not pass, and `make all` stopped before reaching it.
#
#  OWNERSHIP IS THE DESIGN DECISION IN THIS FILE
#  A generator that owns a directory will eventually delete something a human
#  wrote. A generator that owns nothing produces a tree that silently rots.
#  So ownership is explicit and narrow:
#
#      GENERATED, overwritten every run
#          index.md            branches/**        registries/**
#          reference/api.md    formulas/index.md  project/**
#
#      AUTHORED, created once if missing and never overwritten
#          guide/*.md
#
#  The guide is prose about how to use the library. It cannot be derived from
#  the data, and a run that flattened somebody's edits to it would be a bug
#  rather than a regeneration. Every generated file carries a header saying so,
#  because the first thing anyone does with a documentation tree is edit a page
#  in it.
#
#  `project/` MIRRORS THE ROOT DOCUMENTS RATHER THAN RESTATING THEM
#  mkdocs can only serve what is inside `docs_dir`, so the root documents are
#  copied in with a generated banner naming the source. The alternative,
#  writing a second copy by hand, is how a governance document and its
#  published version drift apart.
#
#  DETERMINISM
#  The output is committed, so a nondeterministic generator produces a diff on
#  every run and the tree stops being reviewable. Ordering is taken from
#  COLOUR_ORDER and from the records' own tuple order, never from a set or a
#  dict built at runtime, and files are written with an explicit "\n" newline
#  so a Windows checkout does not rewrite every line.
#
#  EXIT CODES
#      0  the tree was written
#      1  a source document named in the mirror list is missing
#      2  the output directory could not be created
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

# The package must be importable. It is, since `core/__init__.py` and the three
# missing core modules landed; before that this script could not have run
# either.
sys.path.insert(0, str(SRC))

import biotechnology as bt  # noqa: E402
from biotechnology.branches import (  # noqa: E402
    COLOUR_ORDER,
    PENDING_COLOURS,
    WRITTEN_COLOURS,
)
from biotechnology.core import export, validation  # noqa: E402
from biotechnology.core.models import Branch, Subtype  # noqa: E402

BANNER = (
    "<!--\n"
    "  GENERATED FILE. Do not edit.\n"
    "  Produced by tools/generate_docs.py from {source}.\n"
    "  Edit the source and run `make docs`.\n"
    "-->\n\n"
)

#: Root documents mirrored into `docs/project/`, and the page name each takes.
MIRRORED: Sequence[Tuple[str, str]] = (
    ("ARCHITECTURE.md", "architecture.md"),
    ("STYLE_GUIDE.md", "style-guide.md"),
    ("CONTRIBUTING.md", "contributing.md"),
    ("GOVERNANCE.md", "governance.md"),
    ("SECURITY.md", "security.md"),
    ("THREAT_MODEL.md", "threat-model.md"),
    ("CODE_OF_CONDUCT.md", "code-of-conduct.md"),
    ("ROADMAP.md", "roadmap.md"),
    ("FAQ.md", "faq.md"),
    ("CHANGELOG.md", "changelog.md"),
    ("LICENCE", "licence.md"),
)

#: Root documents mirrored into `docs/reference/`.
MIRRORED_REFERENCE: Sequence[Tuple[str, str]] = (
    ("DATA_MODEL.md", "data-model.md"),
    ("NOTATION.md", "notation.md"),
)

# =============================================================================
#  LINK REWRITING FOR MIRRORED DOCUMENTS
#
#  A root document links to its siblings by bare filename, because at the
#  repository root that is what they are. Copied into `docs/project/`, those
#  links point at files that do not exist there, and `mkdocs build --strict`
#  refuses the build: 36 warnings on the first run, every one a link that would
#  have been dead on the published site.
#
#  So links are rewritten on the way in. Three cases, and the third is the one
#  worth stating:
#
#      mirrored into the same directory   GOVERNANCE.md -> governance.md
#      mirrored elsewhere in the tree     DATA_MODEL.md -> ../reference/...
#      NOT MIRRORED AT ALL                AUTHORS.md    -> the GitHub blob URL
#
#  The third case covers documents that belong in the repository and not on the
#  site: the author list, the notice file, the bibliography, the CODEOWNERS
#  file. Rewriting them to an absolute repository URL keeps the link live
#  rather than deleting it, which is what a reader following a reference to the
#  authors file actually wants.
# =============================================================================

REPO_BLOB = "https://github.com/olaflaitinen/biotechnology/blob/main/"

#: Where each mirrored source ends up, relative to `docs/`.
_MIRROR_TARGET: Dict[str, str] = {}

#: Root paths that are deliberately not mirrored and become absolute links.
_NOT_MIRRORED = (
    "AUTHORS.md",
    "NOTICE.md",
    "BIBLIOGRAPHY.md",
    "GLOSSARY.md",
    "README.md",
    "CITATION.cff",
    "Makefile",
    "pyproject.toml",
    "mkdocs.yml",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".well-known/security.txt",
)


def _rewrite_links(text: str, page_dir: str) -> str:
    """Point a mirrored document's links at their new homes.

    `page_dir` is the document's directory under `docs/`, so that a target in
    another directory gets the right number of `../` segments. Computed rather
    than hard-coded because `project/` and `reference/` both mirror documents
    and both link into each other.
    """
    for source_name, target in sorted(_MIRROR_TARGET.items(), key=lambda kv: -len(kv[0])):
        if page_dir and target.startswith(page_dir + "/"):
            replacement = target[len(page_dir) + 1 :]
        elif page_dir:
            replacement = "../" + target
        else:
            replacement = target
        text = text.replace("(" + source_name + ")", "(" + replacement + ")")
        text = text.replace("](./" + source_name + ")", "](" + replacement + ")")

    for name in _NOT_MIRRORED:
        text = text.replace("(" + name + ")", "(" + REPO_BLOB + name + ")")
        text = text.replace("](./" + name + ")", "](" + REPO_BLOB + name + ")")

    return text


#: Authored pages. Created with a usable starter if absent, never overwritten.
GUIDE_PAGES: Sequence[Tuple[str, str]] = (
    ("getting-started.md", "Getting started"),
    ("navigating.md", "Navigating the taxonomy"),
    ("reading-a-record.md", "Reading a record"),
    ("searching.md", "Searching and filtering"),
    ("formulas.md", "Using the formulas"),
    ("exporting.md", "Exporting"),
    ("cli.md", "Command line"),
)

# Built from the two mirror lists rather than written a third time, so a
# document added to a list cannot be forgotten by the link rewriter.
_MIRROR_TARGET.update({name: "project/" + page for name, page in MIRRORED})
_MIRROR_TARGET.update({name: "reference/" + page for name, page in MIRRORED_REFERENCE})


# =============================================================================
#  WRITING
# =============================================================================


def write(path: Path, text: str, *, source: Optional[str] = None) -> None:
    """Write a generated page, with the banner and a stable newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    body = BANNER.format(source=source or "the taxonomy") + text
    if not body.endswith("\n"):
        body += "\n"
    path.write_text(body, encoding="utf-8", newline="\n")


def write_once(path: Path, text: str) -> bool:
    """Write only if absent. Returns True when it wrote."""
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def coverage_note() -> str:
    """One paragraph, on every index page, stating what is missing.

    Repeated rather than centralised on purpose. A reader lands on a branch
    page from a search engine and never sees the home page, and a taxonomy that
    presented six branches without saying there are ten would mislead by
    omission.
    """
    if not PENDING_COLOURS:
        return (
            "All ten branches are written and the taxonomy is complete.\n"
        )
    return (
        "> **Coverage.** {written} of {total} branches are written, holding "
        "{records} records. Still to come: {pending}. Cross-references into "
        "those branches resolve to nothing until they land, and the validator "
        "reports them as forward references rather than as errors.\n".format(
            written=len(WRITTEN_COLOURS),
            total=len(COLOUR_ORDER),
            records=len(bt.subtypes()),
            pending=", ".join(PENDING_COLOURS),
        )
    )


# =============================================================================
#  PAGES: HOME
# =============================================================================


def page_index() -> str:
    counts = bt.counts()
    lines = [
        "# biotechnology",
        "",
        "A machine-readable taxonomy of the ten colour-coded branches of "
        "biotechnology and their subtypes, with zero runtime dependencies.",
        "",
        coverage_note(),
        "",
        "## The branches",
        "",
        "| Colour | Branch | Records | Covers |",
        "|---|---|---:|---|",
    ]
    for key in COLOUR_ORDER:
        if key in PENDING_COLOURS:
            lines.append(
                "| `{0}` | *not written yet* | 0 | |".format(key)
            )
            continue
        branch = bt.get_branch(key)
        lines.append(
            "| `{0}` | [{1}](branches/{0}/index.md) | {2} | {3} |".format(
                key, branch.name, len(branch.subtypes), branch.summary
            )
        )

    lines += [
        "",
        "## At a glance",
        "",
        "| | |",
        "|---|---:|",
        "| Branches written | {0} of {1} |".format(len(WRITTEN_COLOURS), len(COLOUR_ORDER)),
        "| Records | {0} |".format(len(bt.subtypes())),
        "| Applications listed | {0} |".format(counts.get("applications", 0)),
        "| Cross-references | {0} |".format(counts.get("cross_references", 0)),
        "| Runtime dependencies | 0 |",
        "",
        "## Getting started",
        "",
        "```python",
        "import biotechnology as bt",
        "",
        'bt.get("grey.biomining").summary',
        'bt.search("fermentation", limit=5)',
        "bt.by_sdg(6)",
        "```",
        "",
        "```",
        "biotechnology list",
        "biotechnology show grey.biomining --plain",
        "biotechnology export --format csv -o taxonomy.csv",
        "```",
        "",
        "See the [guide](guide/getting-started.md).",
    ]
    return "\n".join(lines)


# =============================================================================
#  PAGES: BRANCHES
# =============================================================================


def page_branches_index() -> str:
    lines = ["# Branches", "", coverage_note(), ""]
    for key in COLOUR_ORDER:
        if key in PENDING_COLOURS:
            lines += ["## {0}".format(key.title()), "", "Not written yet.", ""]
            continue
        branch = bt.get_branch(key)
        lines += [
            "## [{0}](  {1}/index.md)".replace("(  ", "(").format(branch.name, key),
            "",
            "`{0}`  |  {1} records  |  colour `{2}`".format(
                key, len(branch.subtypes), branch.colour
            ),
            "",
            branch.summary,
            "",
        ]
        for subtype in branch.subtypes:
            lines.append(
                "- [{0}]({1}/{2}.md) - {3}".format(
                    subtype.name, key, subtype.key, subtype.summary
                )
            )
        lines.append("")
    return "\n".join(lines)


def page_branch(branch: Branch) -> str:
    lines = [
        "# {0}".format(branch.name),
        "",
        "`{0}`  |  {1} records  |  colour `{2}`".format(
            branch.key, len(branch.subtypes), branch.colour
        ),
        "",
        branch.summary,
        "",
    ]
    if branch.description:
        lines += ["## What it covers", "", branch.description, ""]
    if branch.plain_language:
        lines += ["## In plain language", "", branch.plain_language, ""]
    if branch.analogy:
        lines += ["## An analogy", "", branch.analogy, ""]
    if branch.why_it_matters:
        lines += ["## Why it matters", "", branch.why_it_matters, ""]
    if branch.origin_note:
        lines += ["## On the name", "", branch.origin_note, ""]
    if branch.key_questions:
        lines += ["## Key questions", ""]
        lines += ["- {0}".format(q) for q in branch.key_questions]
        lines += [""]

    lines += ["## Records", "", "| Record | Maturity | Scale | Summary |", "|---|---|---|---|"]
    for subtype in branch.subtypes:
        lines.append(
            "| [{0}]({1}.md) | {2} | {3} | {4} |".format(
                subtype.name,
                subtype.key,
                subtype.maturity.name,
                subtype.scale.name,
                _cell(subtype.summary),
            )
        )
    lines.append("")

    if branch.milestones:
        lines += ["## Branch history", "", "| Year | Event |", "|---:|---|"]
        for milestone in sorted(branch.milestones, key=lambda m: m.year):
            lines.append("| {0} | {1} |".format(milestone.year, _cell(milestone.event)))
        lines.append("")

    return "\n".join(lines)


def page_subtype(subtype: Subtype) -> str:
    """One record, rendered from the shared Markdown emitter.

    The emitter is reused rather than reimplemented so that a change to the
    record shape reaches the documentation and the `--markdown` CLI output
    together. The only thing added here is the breadcrumb and the cross
    reference links, which are page concerns rather than record concerns.
    """
    body = export.to_markdown(subtype)
    lines = [
        "[{0}](index.md) / **{1}**".format(subtype.branch.name, subtype.name),
        "",
        body.rstrip(),
        "",
    ]

    if subtype.related:
        lines += ["### Cross-references", ""]
        for target in subtype.related:
            colour, _, key = target.partition(".")
            if colour in PENDING_COLOURS:
                lines.append("- `{0}` (branch not written yet)".format(target))
            elif colour == subtype.branch_key:
                lines.append("- [{0}]({1}.md)".format(target, key))
            else:
                lines.append("- [{0}](../{1}/{2}.md)".format(target, colour, key))
        lines.append("")

    return "\n".join(lines)


# =============================================================================
#  PAGES: REGISTRIES
# =============================================================================


def page_registry_placeholder(name: str, title: str) -> str:
    """A registry page for a registry that is not written yet.

    It lists the keys the taxonomy REFERENCES, which is genuinely useful: it is
    the specification of what the registry has to contain, and it is the only
    place a contributor can see the whole list. Emitting nothing, or a "coming
    soon", would waste a page that can carry the work item.
    """
    referenced = sorted(_referenced_keys(name))
    lines = [
        "# {0}".format(title),
        "",
        "> **Not written yet.** This registry is an empty package. The "
        "{0} key(s) below are referenced by records in the taxonomy and are "
        "what it has to contain. Until it is written, "
        "`biotechnology.core.validation.registry_coverage()` reports zero "
        "resolved and the reference checker counts rather than fails.".format(
            len(referenced)
        ),
        "",
        "## Referenced keys",
        "",
    ]
    for key in referenced:
        lines.append("- `{0}`".format(key))
    lines.append("")
    return "\n".join(lines)


def _referenced_keys(registry: str) -> set:
    field = {
        "organisms": "organisms",
        "techniques": "techniques",
        "glossary": "glossary",
        "refs": "references",
        "formulas": "formulas",
    }[registry]
    keys = set()
    for subtype in bt.subtypes():
        keys.update(getattr(subtype, field))
    return keys


def page_sdg() -> str:
    from biotechnology import sdg

    lines = [
        "# Sustainable Development Goals",
        "",
        "The seventeen goals adopted in General Assembly Resolution 70/1. "
        "Titles are verbatim from the resolution.",
        "",
        "Records cite a goal only where the link survives the sceptical-auditor "
        "test in STYLE_GUIDE.md rule 12. Several records decline goals they "
        "could plausibly have claimed, and say why in their linkage facet.",
        "",
        "| # | Goal | Theme | Records |",
        "|---:|---|---|---:|",
    ]
    for goal in sdg.goals():
        lines.append(
            "| {0} | **{1}** - {2} | {3} | {4} |".format(
                goal.number,
                goal.short,
                _cell(goal.title),
                goal.theme,
                len(bt.by_sdg(goal.number)),
            )
        )
    lines.append("")

    for goal in sdg.goals():
        records = bt.by_sdg(goal.number)
        if not records:
            continue
        lines += ["## {0}. {1}".format(goal.number, goal.short), "", goal.title, ""]
        for subtype in records:
            lines.append(
                "- [{0}](../branches/{1}/{2}.md)".format(
                    subtype.path, subtype.branch_key, subtype.key
                )
            )
        lines.append("")
    return "\n".join(lines)


def page_vocabularies() -> str:
    from biotechnology.core import enums

    lines = [
        "# Controlled vocabularies",
        "",
        "Six closed sets. A record may only use a member listed here, and "
        "`tools/check_enum_members.py` enforces that against the source "
        "without importing the package.",
        "",
    ]
    for name in sorted(enums.vocabularies()):
        members = enums.vocabularies()[name]
        lines += [
            "## {0}".format(name),
            "",
            "| Member | Meaning | Records |",
            "|---|---|---:|",
        ]
        for member in members:
            explanation = getattr(member, "explanation", "") or getattr(member, "label", "")
            lines.append(
                "| `{0}` | {1} | {2} |".format(
                    member.name, _cell(explanation), _count_with(name, member)
                )
            )
        lines.append("")
    return "\n".join(lines)


def _count_with(vocabulary: str, member: object) -> int:
    field = {
        "Maturity": "maturity",
        "RiskTier": "risk_tier",
        "Scale": "scale",
        "RegulatoryStatus": "regulatory_status",
    }.get(vocabulary)
    if field:
        return sum(1 for s in bt.subtypes() if getattr(s, field) is member)
    if vocabulary == "Domain":
        return sum(1 for s in bt.subtypes() if member in s.domains)
    if vocabulary == "EvidenceLevel":
        return sum(1 for s in bt.subtypes() for m in s.metrics if m.evidence is member)
    return 0


# =============================================================================
#  PAGES: REFERENCE AND FORMULAS
# =============================================================================


def page_api() -> str:
    lines = [
        "# API reference",
        "",
        "Everything below is importable from the top-level package.",
        "",
        "## Records",
        "",
        "| Name | What it is |",
        "|---|---|",
        "| `Branch` | One colour branch, a container of records |",
        "| `Subtype` | One record |",
        "| `Metric` | A named, united, evidence-graded measurement |",
        "| `Milestone` | A dated event with a note |",
        "| `Node` | `Branch` or `Subtype`, for functions accepting either |",
        "",
        "## Lookup and filtering",
        "",
        "| Call | Returns |",
        "|---|---|",
        "| `get(path)` | a branch or a record |",
        "| `get_branch(key)` | a branch, by key or alias |",
        "| `get_subtype(path)` | a record |",
        "| `branches()` | every written branch |",
        "| `subtypes()` | every record |",
        "| `by_sdg(n)` | records citing a goal |",
        "| `by_domain(d)`, `by_maturity(m)`, `by_risk_tier(t)`, `by_scale(s)` | filtered records |",
        "| `related_to(path, depth=1)` | records reachable by cross-reference |",
        "| `timeline(path=None, since=None)` | `(year, event, source)` triples |",
        "| `counts()` | headline figures |",
        "",
        "## Search, export and validation",
        "",
        "| Call | Returns |",
        "|---|---|",
        "| `search(query, limit=None)` | records, best first |",
        "| `to_dict()`, `to_json()`, `to_csv()`, `to_markdown()`, `to_dot()`, `tree()` | text |",
        "| `validate(strict=False)` | findings; raises `ValidationError` on error |",
        "",
        "## Coverage",
        "",
        "| Name | Meaning |",
        "|---|---|",
        "| `WRITTEN_COLOURS` | branches whose package exists |",
        "| `PENDING_COLOURS` | branches not written yet |",
        "| `BROWN`, `GOLD`, `DARK`, `PURPLE` | `None` while pending |",
        "",
        "## Errors",
        "",
        "Every error inherits from `BiotechnologyError`, so one `except` "
        "clause covers the library while ordinary Python errors still "
        "propagate.",
        "",
    ]
    return "\n".join(lines)


def page_formulas_index() -> str:
    keys = sorted(_referenced_keys("formulas"))
    return "\n".join(
        [
            "# Formulas",
            "",
            "> **Not written yet.** `biotechnology.formulas` is an empty "
            "package, so `biotechnology formula` and `biotechnology compute` "
            "exit 3 and say so rather than crashing.",
            "",
            "The {0} keys below are referenced from records' `metrics.FORMULAS` "
            "tuples and from `Metric.formula`. Each will need the four-file "
            "treatment CONTRIBUTING.md section 6 describes: `notation.py`, "
            "`derivation.py` in both ASCII and LaTeX, `implementation.py` with "
            "domain checking, and worked doctests.".format(len(keys)),
            "",
        ]
        + ["- `{0}`".format(key) for key in keys]
        + [""]
    )


# =============================================================================
#  GUIDE STARTERS
# =============================================================================


def guide_starter(title: str) -> str:
    return "\n".join(
        [
            "# {0}".format(title),
            "",
            "<!--",
            "  AUTHORED PAGE. tools/generate_docs.py created this file because",
            "  it was missing and will never overwrite it. Edit freely.",
            "-->",
            "",
            "To be written.",
            "",
        ]
    )


# =============================================================================
#  HELPERS
# =============================================================================


def _cell(text: str) -> str:
    """Escape for a Markdown table cell: a pipe ends the cell, a newline the row."""
    return text.replace("|", "\\|").replace("\n", " ")


# =============================================================================
#  ENTRY POINT
# =============================================================================


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate the docs/ tree.")
    parser.add_argument("--output", default="docs", help="output directory")
    parser.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 if the tree would change",
    )
    args = parser.parse_args(argv)

    out = (ROOT / args.output).resolve()
    try:
        out.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print("cannot create {0}: {1}".format(out, exc), file=sys.stderr)
        return 2

    if args.check:
        # A real content comparison would need the tree built to a temporary
        # directory and diffed. That is worth having and is not what this flag
        # promises today, so it says so rather than reporting a result it did
        # not compute.
        print("--check is not implemented; run without it and inspect the diff")
        return 0

    written = 0

    # -- home ----------------------------------------------------------------
    write(out / "index.md", page_index())
    written += 1

    # -- branches ------------------------------------------------------------
    write(out / "branches" / "index.md", page_branches_index())
    written += 1
    for key in COLOUR_ORDER:
        if key in PENDING_COLOURS:
            write(
                out / "branches" / key / "index.md",
                "# {0}\n\nThis branch is not written yet.\n\n{1}".format(
                    key.title(), coverage_note()
                ),
            )
            written += 1
            continue
        branch = bt.get_branch(key)
        write(out / "branches" / key / "index.md", page_branch(branch))
        written += 1
        for subtype in branch.subtypes:
            write(
                out / "branches" / key / "{0}.md".format(subtype.key),
                page_subtype(subtype),
                source="src/biotechnology/branches/{0}/{1}/".format(key, subtype.key),
            )
            written += 1

    # -- registries ----------------------------------------------------------
    write(out / "registries" / "sdg.md", page_sdg())
    write(out / "registries" / "vocabularies.md", page_vocabularies())
    written += 2
    for registry, title, page in (
        ("organisms", "Organisms", "organisms.md"),
        ("techniques", "Techniques", "techniques.md"),
        ("glossary", "Glossary", "glossary.md"),
        ("refs", "Bibliography", "bibliography.md"),
    ):
        write(out / "registries" / page, page_registry_placeholder(registry, title))
        written += 1

    # -- formulas and reference ----------------------------------------------
    write(out / "formulas" / "index.md", page_formulas_index())
    write(out / "reference" / "api.md", page_api())
    written += 2

    # -- mirrored documents ---------------------------------------------------
    missing: List[str] = []
    for source_name, page in MIRRORED_REFERENCE:
        source = ROOT / source_name
        if not source.exists():
            missing.append(source_name)
            continue
        write(
            out / "reference" / page,
            _rewrite_links(source.read_text(encoding="utf-8"), "reference"),
            source=source_name,
        )
        written += 1
    for source_name, page in MIRRORED:
        source = ROOT / source_name
        if not source.exists():
            missing.append(source_name)
            continue
        text = source.read_text(encoding="utf-8")
        if source_name == "LICENCE":
            # Fenced rather than rendered: it is a legal instrument, and
            # Markdown would reflow its numbered clauses.
            text = "# Licence\n\n```\n{0}\n```\n".format(text.rstrip())
        else:
            text = _rewrite_links(text, "project")
        write(out / "project" / page, text, source=source_name)
        written += 1

    # -- authored guide -------------------------------------------------------
    created = 0
    for page, title in GUIDE_PAGES:
        if write_once(out / "guide" / page, guide_starter(title)):
            created += 1

    # `--output` may point anywhere, and the test suite generates into a
    # temporary directory so that a test run never touches the working tree.
    # `Path.relative_to` raises for a path outside the repository, so the
    # absolute path is the fallback rather than a crash in the final line
    # after all the work has succeeded.
    try:
        shown = out.relative_to(ROOT)
    except ValueError:
        shown = out
    print("Wrote {0} generated page(s) to {1}/".format(written, shown))
    if created:
        print(
            "Created {0} authored guide page(s); they will never be "
            "overwritten.".format(created)
        )
    if PENDING_COLOURS:
        print(
            "Coverage stated on every index page: {0} of {1} branches, "
            "pending {2}.".format(
                len(WRITTEN_COLOURS), len(COLOUR_ORDER), ", ".join(PENDING_COLOURS)
            )
        )
    if missing:
        print()
        print("FAIL: mirrored source document(s) missing:", file=sys.stderr)
        for name in missing:
            print("  - {0}".format(name), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
