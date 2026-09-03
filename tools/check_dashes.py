#!/usr/bin/env python3
# =============================================================================
#  tools/check_dashes.py
# -----------------------------------------------------------------------------
#  Forbid em dashes, en dashes and other typographic punctuation that does not
#  survive a round trip through the systems this project's output passes
#  through.
#
#  WHY THIS RULE EXISTS
#  This library's text is not read only on a modern web page. It goes into:
#
#    * a terminal, sometimes with a legacy code page on Windows;
#    * a CSV file opened in a spreadsheet that guessed the encoding wrong;
#    * a LaTeX document, where some of these characters need escaping;
#    * a plain-text export read by somebody offline;
#    * a diff, where a character that looks like a hyphen but is not makes a
#      reviewer waste time working out why a search did not match.
#
#  An ASCII hyphen survives all of that. An em dash does not. The rule is
#  recorded in STYLE_GUIDE.md section 3 and this script is what enforces it.
#
#  WHAT IS ALLOWED
#  Deliberately, this is a NARROW check. It forbids a specific list of
#  characters rather than all non-ASCII, because three categories of non-ASCII
#  are correct and must not be broken:
#
#    * accented author names in BIBLIOGRAPHY.md, which are spellings, not
#      decoration;
#    * box-drawing characters in the architecture diagrams, which are the
#      diagram;
#    * the Greek letters in the NOTATION.md reference table, whose whole
#      purpose is to show the Unicode form beside the ASCII one.
#
#  THE LICENCE IS EXEMPT
#  LICENCE reproduces the official EUPL v1.2 text verbatim. Modifying the
#  reproduced text of a licence is both wrong and arguably a breach of the
#  terms under which it may be redistributed. It is never touched.
#
#  USAGE
#      python tools/check_dashes.py
#      python tools/check_dashes.py --fix
#
#  EXIT CODES
#      0  clean
#      1  forbidden characters found
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import argparse
import sys
import unicodedata
from pathlib import Path
from typing import Dict, List, NamedTuple, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------------
#  Directories never scanned.
# -----------------------------------------------------------------------------
SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "venv",
    "build",
    "dist",
    "site",
    "htmlcov",
    ".benchmarks",
}

# -----------------------------------------------------------------------------
#  Files never scanned. The licence is verbatim third-party text.
# -----------------------------------------------------------------------------
SKIP_FILES = {"LICENCE", "LICENSE"}

# -----------------------------------------------------------------------------
#  Exact paths never scanned, each for a stated reason.
#
#  `docs/project/licence.md` is the generated mirror of the root LICENCE, which
#  `tools/generate_docs.py` copies into the documentation tree because mkdocs
#  can only serve what is inside `docs_dir`. It carries the EUPL text verbatim,
#  typographic quotation marks and dashes included.
#
#  Excluding it follows the same principle as excluding the root LICENCE and
#  not a different one: the text is a published legal instrument, and running
#  `--fix` over it would alter the licence. The exclusion is by exact path
#  rather than by filename so that a future document called `licence.md`
#  somewhere else is still checked.
# -----------------------------------------------------------------------------
SKIP_PATHS = {Path("docs") / "project" / "licence.md"}

# -----------------------------------------------------------------------------
#  Extensions scanned. Anything not listed is treated as binary or irrelevant.
# -----------------------------------------------------------------------------
TEXT_SUFFIXES = {
    ".py",
    ".pyi",
    ".md",
    ".rst",
    ".txt",
    ".toml",
    ".cfg",
    ".ini",
    ".yml",
    ".yaml",
    ".cff",
    ".json",
    ".csv",
    ".html",
    ".css",
    ".js",
}

#: Extensionless files that are still text and still scanned.
TEXT_NAMES = {"Makefile", "CODEOWNERS", ".gitignore", ".gitattributes", ".editorconfig"}

# -----------------------------------------------------------------------------
#  The forbidden set, and what each one should become.
#
#  Each entry is (character, replacement, why it is forbidden). The replacement
#  is what --fix writes; where a character has no safe automatic replacement
#  the replacement is None and --fix reports it for a human instead.
# -----------------------------------------------------------------------------
FORBIDDEN: Dict[str, Tuple[str, str]] = {
    # Keys are built with chr() from a code point rather than written as a
    # literal character or as a backslash escape. Both of those forms have a
    # way of being silently normalised by an editor, a copy-paste, or a
    # well-meaning formatter, and either would make this file fail its own
    # check. Exempting the checker from its own rule is exactly the sort of
    # quiet exception that makes a rule stop meaning anything, so the code
    # point is written as a number that nothing will rewrite.
    chr(0x2014): ("-", "em dash, does not survive a legacy code page"),
    chr(0x2013): ("-", "en dash, visually confusable with a hyphen in a diff"),
    chr(0x2012): ("-", "figure dash"),
    chr(0x2015): ("-", "horizontal bar"),
    chr(0x2212): ("-", "minus sign, confusable with a hyphen"),
    chr(0x2018): ("'", "left single quotation mark"),
    chr(0x2019): ("'", "right single quotation mark, breaks apostrophe search"),
    chr(0x201C): ('"', "left double quotation mark"),
    chr(0x201D): ('"', "right double quotation mark"),
    chr(0x2026): ("...", "horizontal ellipsis, three dots are searchable"),
    chr(0x00A0): (" ", "non-breaking space, invisible and breaks word matching"),
    chr(0x200B): ("", "zero-width space, invisible and unsearchable"),
    chr(0x200E): ("", "left-to-right mark, invisible"),
    chr(0x200F): ("", "right-to-left mark, invisible"),
    chr(0xFEFF): ("", "byte order mark inside a file, breaks shebangs and parsers"),
}


class Finding(NamedTuple):
    """One forbidden character occurrence."""

    path: Path
    line_no: int
    column: int
    char: str
    reason: str
    line: str


def iter_text_files() -> List[Path]:
    """Every text file in the repository that this rule applies to."""
    out: List[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(REPO_ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel.name in SKIP_FILES:
            continue
        if rel in SKIP_PATHS:
            continue
        if rel.suffix in TEXT_SUFFIXES or rel.name in TEXT_NAMES:
            out.append(path)
    return sorted(out)


def scan(path: Path) -> List[Finding]:
    """Find every forbidden character in one file."""
    findings: List[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return findings

    for line_no, line in enumerate(text.splitlines(), start=1):
        for column, ch in enumerate(line, start=1):
            if ch in FORBIDDEN:
                findings.append(
                    Finding(
                        path=path,
                        line_no=line_no,
                        column=column,
                        char=ch,
                        reason=FORBIDDEN[ch][1],
                        line=line,
                    )
                )
    return findings


def fix(path: Path) -> int:
    """Rewrite one file with the forbidden characters replaced.

    Returns the number of substitutions made.

    Note that this is a character-for-character substitution and deliberately
    does NOT try to be clever about surrounding whitespace. An earlier version
    of this tooling collapsed runs of spaces around a replaced dash and, in
    doing so, destroyed the leading indentation of YAML list items across the
    repository. The lesson was expensive and is recorded here so that nobody
    reintroduces it: never combine a character substitution with a whitespace
    normalisation in the same pass.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return 0

    original = text
    count = 0
    for ch, (replacement, _) in FORBIDDEN.items():
        occurrences = text.count(ch)
        if occurrences:
            text = text.replace(ch, replacement)
            count += occurrences

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
    return count


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Forbid em dashes and other punctuation that does not survive a round trip.",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Rewrite the offending files instead of only reporting them.",
    )
    args = parser.parse_args(argv)

    files = iter_text_files()

    if args.fix:
        total = 0
        touched = 0
        for path in files:
            n = fix(path)
            if n:
                total += n
                touched += 1
                print(f"fixed {n:4} in {path.relative_to(REPO_ROOT)}")
        print(f"\n{total} substitution(s) across {touched} file(s).")
        print("Review the diff before committing. See STYLE_GUIDE.md section 3.")
        return 0

    findings: List[Finding] = []
    for path in files:
        findings.extend(scan(path))

    if not findings:
        print(f"OK: {len(files)} text file(s) scanned, no forbidden punctuation.")
        return 0

    print(f"{len(findings)} forbidden character(s) found:\n", file=sys.stderr)
    for f in findings[:200]:
        name = unicodedata.name(f.char, "UNKNOWN")
        rel = f.path.relative_to(REPO_ROOT)
        print(f"  {rel}:{f.line_no}:{f.column}", file=sys.stderr)
        print(f"    U+{ord(f.char):04X} {name}: {f.reason}", file=sys.stderr)
        print(f"    {f.line.strip()[:100]}\n", file=sys.stderr)
    if len(findings) > 200:
        print(f"  ... and {len(findings) - 200} more.\n", file=sys.stderr)

    print("Run `python tools/check_dashes.py --fix` to correct them.", file=sys.stderr)
    print("The rule is in STYLE_GUIDE.md section 3.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
