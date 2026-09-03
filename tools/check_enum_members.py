#!/usr/bin/env python3
# =============================================================================
#  tools/check_enum_members.py
# -----------------------------------------------------------------------------
#  Assert that every controlled-vocabulary reference in the branch records names
#  a member that actually exists.
#
#  WHY THIS IS A SCRIPT AND NOT A CONVENTION
#  The six controlled vocabularies in `core/enums.py` are the spine of this
#  library. Every one of the eighty-five subtype records places itself in all
#  six, and those placements are what make the data comparable at all: a filter
#  for RiskTier.REGULATED is only meaningful if no record has quietly invented
#  its own tier.
#
#  The failure this script catches is specific and easy to commit. A
#  contributor writing a new record reaches for the value that the subject
#  matter suggests rather than the value the vocabulary defines. They write
#  `RiskTier.MODERATE` because moderate is the honest description, or
#  `Domain.AGRICULTURE` because the record is about farming. Neither member
#  exists. RiskTier measures GOVERNANCE INTENSITY and its members are ROUTINE,
#  CONTROLLED, REGULATED and RESTRICTED; Domain groups by WHO PAYS and offers
#  FOOD rather than AGRICULTURE.
#
#  WHY PYTHON DOES NOT CATCH IT FOR YOU
#  It does, eventually, with an AttributeError - but only when the module is
#  imported. A subtype package that is written before its branch package exists
#  is not importable yet, and so the error sits in the tree unnoticed until the
#  branch is completed, by which point several records may carry it. This
#  script works on the ABSTRACT SYNTAX TREE instead, so it validates a record
#  the moment the file is saved, with no import and no working package.
#
#  That property is the whole point. It is the only check in this repository
#  that gives a useful answer while the library is half written.
#
#  WHAT IT CHECKS
#    1. Every `<EnumClass>.<MEMBER>` reference under src/biotechnology/branches
#       names a member defined on that class in core/enums.py.
#    2. Nothing else. It does not judge whether the chosen value is CORRECT for
#       the subject, which is a matter for review by a domain expert and is
#       governed by STYLE_GUIDE.md rule 9.
#
#  WHAT IT DELIBERATELY DOES NOT DO
#  It does not import anything. Importing the package would defeat the purpose
#  described above, and it would also mean executing repository code inside a
#  pre-commit hook, which SECURITY.md section 4.1 argues against for the
#  checking scripts specifically.
#
#  USAGE
#      python tools/check_enum_members.py
#
#  EXIT CODES
#      0  every vocabulary reference resolves
#      1  at least one reference names a member that does not exist
#      2  the vocabulary source could not be read at all
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import ast
import sys
from pathlib import Path
from typing import Dict, List, NamedTuple, Set

# -----------------------------------------------------------------------------
#  Paths are derived from this file's own location rather than from the current
#  working directory, so the script behaves identically whether it is invoked
#  from the repository root, from a hook, or from tox.
# -----------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
ENUMS = ROOT / "src" / "biotechnology" / "core" / "enums.py"
BRANCHES = ROOT / "src" / "biotechnology" / "branches"

# -----------------------------------------------------------------------------
#  The base class is excluded from the check. `DescribedEnum` defines machinery
#  rather than vocabulary, and nothing in the records should reference it.
# -----------------------------------------------------------------------------
NOT_A_VOCABULARY = frozenset({"DescribedEnum"})


class Violation(NamedTuple):
    """One reference to a vocabulary member that does not exist."""

    where: str  # path and line, in the form that editors make clickable
    reference: str  # what was written, for example "RiskTier.MODERATE"
    available: str  # what could have been written instead


# =============================================================================
#  READING THE VOCABULARIES
# =============================================================================
def load_vocabularies() -> Dict[str, Set[str]]:
    """Return {class name: {member names}} parsed from core/enums.py.

    A member is any assignment to an ALL_CAPS name directly in a class body.
    That is exactly how the six vocabularies are written, and it deliberately
    ignores methods, docstrings and the `rank` machinery on the base class.
    """
    tree = ast.parse(ENUMS.read_text(encoding="utf-8"), filename=str(ENUMS))

    vocabularies: Dict[str, Set[str]] = {}
    for node in tree.body:
        if not isinstance(node, ast.ClassDef) or node.name in NOT_A_VOCABULARY:
            continue

        names: Set[str] = set()
        for statement in node.body:
            # An enum member is a plain assignment: NAME = (...)
            if isinstance(statement, ast.Assign):
                for target in statement.targets:
                    if isinstance(target, ast.Name) and target.id.isupper():
                        names.add(target.id)

        # A class with no ALL_CAPS assignments is not a vocabulary. Recording it
        # anyway would cause every reference to it to be reported as invalid.
        if names:
            vocabularies[node.name] = names

    return vocabularies


# =============================================================================
#  CHECKING THE RECORDS
# =============================================================================
def check_file(path: Path, vocabularies: Dict[str, Set[str]]) -> List[Violation]:
    """Report every vocabulary reference in one file that does not resolve."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        # A syntax error is a real problem, but it is not THIS script's problem.
        # check_facets.py and the test suite both catch it, and reporting it
        # here as well would produce two failures for one cause.
        print(f"  skipped (syntax error): {path}: {exc}", file=sys.stderr)
        return []

    violations: List[Violation] = []

    for node in ast.walk(tree):
        # We are looking for the shape `Name.ATTRIBUTE`, which is how every
        # vocabulary value is written throughout the records.
        if not isinstance(node, ast.Attribute):
            continue
        if not isinstance(node.value, ast.Name):
            continue

        class_name = node.value.id
        member_name = node.attr

        if class_name not in vocabularies:
            continue  # not one of ours, for example `narrative.SUMMARY`
        if not member_name.isupper():
            continue  # a method call such as `.requires_committee()`
        if member_name in vocabularies[class_name]:
            continue  # resolves correctly

        relative = path.relative_to(ROOT).as_posix()
        violations.append(
            Violation(
                where=f"{relative}:{node.lineno}",
                reference=f"{class_name}.{member_name}",
                available=", ".join(sorted(vocabularies[class_name])),
            )
        )

    return violations


# =============================================================================
#  ENTRY POINT
# =============================================================================
def main() -> int:
    if not ENUMS.is_file():
        print(f"cannot read the vocabularies: {ENUMS} does not exist", file=sys.stderr)
        return 2

    vocabularies = load_vocabularies()
    if not vocabularies:
        print(f"no vocabularies found in {ENUMS}", file=sys.stderr)
        return 2

    if not BRANCHES.is_dir():
        print(f"nothing to check: {BRANCHES} does not exist", file=sys.stderr)
        return 0

    files = sorted(BRANCHES.rglob("*.py"))
    violations: List[Violation] = []
    for path in files:
        violations.extend(check_file(path, vocabularies))

    if not violations:
        print(
            f"OK: {len(files)} record file(s) checked against "
            f"{len(vocabularies)} controlled vocabular(ies); "
            "every reference resolves."
        )
        return 0

    print(f"{len(violations)} invalid vocabulary reference(s):\n", file=sys.stderr)
    for violation in violations:
        print(f"  {violation.where}", file=sys.stderr)
        print(f"    wrote:     {violation.reference}", file=sys.stderr)
        print(f"    available: {violation.available}\n", file=sys.stderr)
    print(
        "The controlled vocabularies are closed sets. If none of the available "
        "members fits the record, the correct response is to propose a change "
        "to core/enums.py under GOVERNANCE.md section 4, not to invent a value "
        "in the record. Read the class docstring first: RiskTier measures "
        "governance intensity rather than danger, and Domain groups by who "
        "pays rather than by subject matter.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
