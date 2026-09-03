#!/usr/bin/env python3
# =============================================================================
#  tools/check_defensive.py
# -----------------------------------------------------------------------------
#  Enforces the dual-use content policy in SECURITY.md section 2.
#
#  THE POLICY, IN ONE LINE
#
#      NOTHING IN THIS REPOSITORY MAY READ AS OPERATIONAL INSTRUCTIONS FOR
#      CAUSING HARM.
#
#  It applies everywhere, and it applies with particular force to the `dark`
#  branch, which documents biosafety, biosecurity governance, dual-use research
#  oversight, gene synthesis screening, biosurveillance, medical
#  countermeasures, microbial forensics and biological arms control. That
#  branch exists to describe the PROTECTIVE side of a subject whose other side
#  must not be described at all.
#
#  WHAT A CHECKER CAN AND CANNOT DO HERE
#  It cannot judge intent, and it must not pretend to. A keyword scanner
#  applied to a biosecurity corpus will match on the very words the protective
#  literature uses, and a naive one would flag every sentence about what a
#  control exists to prevent. That failure mode is worse than no check: it
#  trains a reviewer to dismiss the output.
#
#  So this script looks for two narrow, mechanical things, and leaves judgement
#  to the human review that SECURITY.md already requires:
#
#      1. IMPERATIVE PROCEDURE. Text shaped like a protocol rather than like a
#         description: numbered steps with quantities, "add X to Y", "incubate
#         at", "the procedure is as follows". A record describes what a field
#         does; it never tells a reader how to do it. This shape is detectable
#         and it is the thing the policy is actually about.
#
#      2. ENHANCEMENT AND ACQUISITION FRAMING. A small, explicit list of
#         phrases that describe increasing harm or obtaining a controlled
#         agent, as opposed to detecting, governing or defending against one.
#
#  Every match is reported for a human to read, and the exit code is what makes
#  it enforceable. There is no attempt at a severity model, because a
#  false-negative here is a policy breach and a false-positive is thirty
#  seconds of a reviewer's time.
#
#  WHY IT PASSES TODAY WITH NOTHING TO CHECK
#  The dark branch is not written. This script therefore reports zero findings
#  and says plainly that the branch is pending, rather than exiting 0 as though
#  it had verified something. When the branch lands, the check is already in
#  `make validate`, in CI and in pre-commit, which is the only ordering that
#  makes a content policy real: the control exists before the content does.
#
#  EXIT CODES
#      0  no finding
#      1  at least one passage needs human review before it can be merged
#      2  the source tree could not be read
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent.parent
BRANCHES = ROOT / "src" / "biotechnology" / "branches"

#: The branch the policy names explicitly. Checked with the others, and
#: reported separately, because its absence should be visible rather than
#: silently indistinguishable from a clean pass.
SENSITIVE_BRANCH = "dark"


# =============================================================================
#  PATTERN 1: TEXT SHAPED LIKE A PROTOCOL
#
#  These match STRUCTURE rather than subject. A sentence describing what a
#  technique achieves does not match; a sentence telling a reader to perform it
#  does. That is the distinction the policy turns on, and it is the only part
#  of it a machine can see.
# =============================================================================
PROCEDURAL_PATTERNS: Tuple[Tuple[str, str], ...] = (
    (r"\bthe (?:procedure|protocol|method) is as follows\b", "introduces a protocol"),
    (r"\bstep\s*\d+\s*[:.)]", "numbered procedural step"),
    (r"\bincubate\s+(?:at|for)\b", "imperative laboratory instruction"),
    (r"\b(?:add|mix|dissolve|inoculate|transfect|transform)\s+\d+\s*(?:g|mg|ug|ml|ul|l)\b",
     "imperative instruction with a quantity"),
    (r"\bcentrifuge\s+at\s+\d+", "imperative instruction with a setting"),
    (r"\bto (?:produce|synthesise|synthesize|construct|obtain) (?:the|a) \w+, (?:first|begin|start)\b",
     "opens a construction procedure"),
)

# =============================================================================
#  PATTERN 2: ENHANCEMENT AND ACQUISITION FRAMING
#
#  Deliberately short and explicit. Every entry describes increasing harm or
#  obtaining a controlled agent. Words that merely NAME a hazard are absent,
#  because the protective literature is made of them and matching on them would
#  make this script useless.
# =============================================================================
HARM_PATTERNS: Tuple[Tuple[str, str], ...] = (
    (r"\bincreas\w+ (?:the )?(?:transmissibility|virulence|lethality|pathogenicity)\b",
     "describes enhancing harm rather than detecting or preventing it"),
    (r"\benhanc\w+ (?:the )?(?:transmissibility|virulence|lethality)\b",
     "describes enhancing harm"),
    (r"\bhow to (?:acquire|obtain|synthesise|synthesize|weaponise|weaponize)\b",
     "acquisition or weaponisation framing"),
    (r"\bevade (?:detection|screening|surveillance)\b",
     "detection evasion framing"),
    (r"\bcircumvent\w* (?:the )?(?:screening|detection|controls?)\b",
     "control circumvention framing"),
    (r"\bconfer\w* resistance to (?:every|all) (?:known )?(?:treatment|therapy|antibiotic)",
     "describes defeating countermeasures"),
)


def string_constants(path: Path) -> List[Tuple[int, str]]:
    """Every string literal in a module, with its line number.

    Only literals are scanned. Comments and identifiers are excluded on
    purpose: the policy is about what the DATA says to a reader, and a comment
    explaining why a record declines to describe something would otherwise
    match its own explanation.
    """
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError:
        return []

    found: List[Tuple[int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            found.append((getattr(node, "lineno", 0), node.value))
    return found


def scan(path: Path) -> List[str]:
    """Return one line per finding in this file."""
    findings: List[str] = []
    relative = path.relative_to(ROOT)

    for line_number, text in string_constants(path):
        lowered = text.lower()
        for pattern, reason in PROCEDURAL_PATTERNS + HARM_PATTERNS:
            match = re.search(pattern, lowered)
            if not match:
                continue
            excerpt = text[max(0, match.start() - 30) : match.end() + 40].strip()
            findings.append(
                "{0}:{1}  {2}\n        ...{3}...".format(
                    relative, line_number, reason, " ".join(excerpt.split())
                )
            )
    return findings


def main() -> int:
    if not BRANCHES.is_dir():
        print("cannot read {0}".format(BRANCHES), file=sys.stderr)
        return 2

    findings: List[str] = []
    scanned = 0
    sensitive_written = False

    for facet in sorted(BRANCHES.glob("*/*/*.py")):
        if facet.parent.parent.name == SENSITIVE_BRANCH:
            sensitive_written = True
        scanned += 1
        findings.extend(scan(facet))

    if findings:
        print("REVIEW REQUIRED: {0} passage(s) match the dual-use policy.".format(len(findings)))
        print("See SECURITY.md section 2. A match is not proof of a breach; it is")
        print("a passage a human must read before it is merged.")
        print()
        for finding in findings:
            print("  - {0}".format(finding))
        return 1

    print(
        "OK: {0} facet file(s) scanned, no passage reads as operational "
        "instructions.".format(scanned)
    )
    if not sensitive_written:
        print(
            "     Note: the {0!r} branch is not written yet. This check is in "
            "place before the content is, which is the point.".format(
                SENSITIVE_BRANCH
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
