#!/usr/bin/env python3
# =============================================================================
#  tools/check_facets.py
# -----------------------------------------------------------------------------
#  Asserts that every subtype package satisfies the seven-file facet contract.
#
#  THE CONTRACT
#  A subtype is a directory of exactly seven modules, and each one exports a
#  fixed set of names and nothing else:
#
#      __init__.py     KEY, NAME, ALIASES, SUBTYPE
#      narrative.py    SUMMARY, DESCRIPTION, PLAIN_LANGUAGE, ANALOGY,
#                      WHY_IT_MATTERS
#      practice.py     APPLICATIONS, TECHNOLOGIES, ORGANISMS, TECHNIQUES,
#                      CHALLENGES
#      metrics.py      METRICS, FORMULAS
#      history.py      MILESTONES
#      governance.py   MATURITY, RISK_TIER, SCALE, DOMAINS,
#                      REGULATORY_STATUS, REGULATIONS, STANDARDS
#      linkage.py      SDGS, GLOSSARY, REFERENCES, RELATED
#
#  WHY A SEPARATE CHECKER RATHER THAN A TEST
#  `core.validation` checks the ASSEMBLED objects, which is the right place for
#  editorial minimums and dangling references. It cannot see the file layout,
#  because by the time a Subtype exists the seven files have already been
#  collapsed into one object. Two failures are therefore invisible to it: a
#  facet that exports a name the contract does not include, and a package
#  where a required file is missing but the field happens to be supplied from
#  somewhere else.
#
#  Both matter for the same reason. The seven-file split exists so that a
#  domain expert can review one facet without reading the other six, and a
#  package that quietly drifts from the layout defeats that without breaking
#  anything a user would notice.
#
#  IT WORKS BY PARSING, NOT IMPORTING
#  Deliberate. The check must run while the package is incomplete, and it must
#  attribute a problem to a FILE rather than to an assembled record. Parsing
#  also lets it see the `__all__` a module declares, which is the contract as
#  written rather than as executed.
#
#  EXIT CODES
#      0  every package satisfies the contract
#      1  at least one does not
#      2  the branches directory could not be read
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import ast
import sys
from pathlib import Path
from typing import Dict, List, Set

ROOT = Path(__file__).resolve().parent.parent
BRANCHES = ROOT / "src" / "biotechnology" / "branches"

# =============================================================================
#  THE CONTRACT, AS DATA
#
#  Stated once here rather than inferred from an existing package, so that a
#  drift introduced into one record cannot become the standard the others are
#  measured against.
# =============================================================================
CONTRACT: Dict[str, Set[str]] = {
    "__init__.py": {"KEY", "NAME", "ALIASES", "SUBTYPE"},
    "narrative.py": {
        "SUMMARY",
        "DESCRIPTION",
        "PLAIN_LANGUAGE",
        "ANALOGY",
        "WHY_IT_MATTERS",
    },
    "practice.py": {
        "APPLICATIONS",
        "TECHNOLOGIES",
        "ORGANISMS",
        "TECHNIQUES",
        "CHALLENGES",
    },
    "metrics.py": {"METRICS", "FORMULAS"},
    "history.py": {"MILESTONES"},
    "governance.py": {
        "MATURITY",
        "RISK_TIER",
        "SCALE",
        "DOMAINS",
        "REGULATORY_STATUS",
        "REGULATIONS",
        "STANDARDS",
    },
    "linkage.py": {"SDGS", "GLOSSARY", "REFERENCES", "RELATED"},
}

#: `__init__.py` is the assembly file. It defines KEY, NAME and ALIASES and
#: exports only SUBTYPE, which is why its `__all__` is checked against a
#: narrower set than its definitions.
INIT_EXPORTS: Set[str] = {"SUBTYPE"}


def module_level_names(path: Path) -> Set[str]:
    """Upper-case module-level assignments, which is what a facet exports.

    Lower-case names are helpers and are not part of the contract. Restricting
    to upper case is what lets a facet keep a private constant without the
    checker treating it as an undeclared export.
    """
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names: Set[str] = set()
    for node in tree.body:
        targets = []
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            targets = [node.target]
        elif isinstance(node, ast.Assign):
            targets = [t for t in node.targets if isinstance(t, ast.Name)]
        for target in targets:
            if target.id.isupper() and not target.id.startswith("_"):
                names.add(target.id)
    return names


def declared_all(path: Path) -> Set[str]:
    """The module's `__all__`, or an empty set if it declares none."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        return {
                            e.value
                            for e in node.value.elts
                            if isinstance(e, ast.Constant) and isinstance(e.value, str)
                        }
    return set()


def check_package(package: Path) -> List[str]:
    """Return the problems found in one subtype package."""
    problems: List[str] = []
    label = "{0}.{1}".format(package.parent.name, package.name)

    for filename, required in CONTRACT.items():
        path = package / filename
        if not path.exists():
            problems.append("{0}: missing {1}".format(label, filename))
            continue

        defined = module_level_names(path)
        missing = required - defined
        if missing:
            problems.append(
                "{0}/{1}: does not define {2}".format(
                    label, filename, ", ".join(sorted(missing))
                )
            )

        expected_exports = INIT_EXPORTS if filename == "__init__.py" else required
        exported = declared_all(path)
        if not exported:
            problems.append("{0}/{1}: declares no __all__".format(label, filename))
        else:
            extra = exported - expected_exports
            absent = expected_exports - exported
            if extra:
                problems.append(
                    "{0}/{1}: __all__ exports {2}, which the contract does not "
                    "include".format(label, filename, ", ".join(sorted(extra)))
                )
            if absent:
                problems.append(
                    "{0}/{1}: __all__ omits {2}".format(
                        label, filename, ", ".join(sorted(absent))
                    )
                )

    # -- files the contract does not mention ----------------------------------
    #  A stray module in a subtype package is a real finding. The seven-file
    #  split is what makes a facet independently reviewable, and an eighth file
    #  is content nobody is looking for.
    for path in sorted(package.glob("*.py")):
        if path.name not in CONTRACT:
            problems.append(
                "{0}: unexpected file {1}; the contract is seven files".format(
                    label, path.name
                )
            )

    # -- the key must match the directory -------------------------------------
    init = package / "__init__.py"
    if init.exists():
        tree = ast.parse(init.read_text(encoding="utf-8"), filename=str(init))
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if (
                        isinstance(target, ast.Name)
                        and target.id == "KEY"
                        and isinstance(node.value, ast.Constant)
                        and node.value.value != package.name
                    ):
                        problems.append(
                            "{0}: KEY is {1!r} but the directory is {2!r}".format(
                                label, node.value.value, package.name
                            )
                        )
    return problems


def main() -> int:
    if not BRANCHES.is_dir():
        print("cannot read {0}".format(BRANCHES), file=sys.stderr)
        return 2

    problems: List[str] = []
    packages = 0
    pending: List[str] = []

    for branch_dir in sorted(p for p in BRANCHES.iterdir() if p.is_dir()):
        if branch_dir.name.startswith("__"):
            continue
        subtype_dirs = sorted(
            p for p in branch_dir.iterdir() if p.is_dir() and not p.name.startswith("__")
        )
        if not subtype_dirs:
            # An unwritten branch. Reported once, as information, never as a
            # failure: it is a stated gap and failing on it would make this
            # check unusable until the taxonomy is finished.
            pending.append(branch_dir.name)
            continue
        for package in subtype_dirs:
            packages += 1
            problems.extend(check_package(package))

    if problems:
        print("FAIL: {0} facet contract violation(s).".format(len(problems)))
        print()
        for problem in problems:
            print("  - {0}".format(problem))
        return 1

    print(
        "OK: {0} subtype package(s) satisfy the seven-file facet contract.".format(
            packages
        )
    )
    if pending:
        print("     {0} branch(es) not written yet: {1}".format(len(pending), ", ".join(pending)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
