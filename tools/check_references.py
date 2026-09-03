#!/usr/bin/env python3
# =============================================================================
#  tools/check_references.py
# -----------------------------------------------------------------------------
#  Checks every key the taxonomy points at, and reports what does not resolve.
#
#  SIX KINDS OF REFERENCE LEAVE A RECORD
#
#      related      -> another subtype, by dotted path
#      organisms    -> biotechnology.organisms
#      techniques   -> biotechnology.techniques
#      glossary     -> biotechnology.glossary
#      references   -> biotechnology.refs
#      formulas     -> biotechnology.formulas
#      sdgs         -> biotechnology.sdg
#
#  A dangling key is the characteristic failure of a cross-referenced dataset.
#  It is invisible to a reader, invisible to Python, and it accumulates: every
#  new record adds a few dozen keys and nobody checks them by hand past the
#  tenth record.
#
#  THE HARD PART IS NOT DETECTION, IT IS SEVERITY
#  Five of the six registries are empty. A naive checker would report 2,028
#  failures and be switched off within a day, which is worse than no checker.
#  So a key is judged against the state of the registry it points into:
#
#      registry is populated      an unresolved key is an ERROR. Somebody
#                                 wrote a key the registry does not have, and
#                                 that is a typo nothing else will catch.
#      registry is empty          keys are COUNTED and reported, not failed.
#                                 An empty registry means "not written yet",
#                                 not "every key is wrong".
#
#  The same logic applies to `related`: a path into a written branch that names
#  no record is an error, and a path into a branch that does not exist yet is a
#  forward reference, which is a deliberate and documented pattern in this
#  repository.
#
#  --strict removes the distinction. That is the mode for the release that
#  claims the taxonomy is complete, and it must not be the mode for CI before
#  then, or the build can never go green.
#
#  IT PARSES RATHER THAN IMPORTS
#  So that it runs while the package is incomplete and can attribute a key to
#  the file that contains it, which an assembled record cannot do.
#
#  EXIT CODES
#      0  every reference that can be checked resolves
#      1  at least one does not
#      2  the branches directory could not be read
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "biotechnology"
BRANCHES = SRC / "branches"

#: Facet field -> the registry package it points into.
FIELD_TO_REGISTRY: Dict[str, str] = {
    "ORGANISMS": "organisms",
    "TECHNIQUES": "techniques",
    "GLOSSARY": "glossary",
    "REFERENCES": "refs",
    "FORMULAS": "formulas",
}


# =============================================================================
#  READING WHAT THE TAXONOMY POINTS AT
# =============================================================================


def collect_references() -> Tuple[Dict[str, Dict[str, Set[str]]], Set[str], Set[int]]:
    """Return (references by registry and key to the files using it,
    every subtype path that exists, every SDG number cited)."""
    by_registry: Dict[str, Dict[str, Set[str]]] = {
        name: {} for name in FIELD_TO_REGISTRY.values()
    }
    by_registry["related"] = {}
    existing_paths: Set[str] = set()
    sdgs: Set[int] = set()

    for facet in sorted(BRANCHES.glob("*/*/*.py")):
        branch = facet.parent.parent.name
        subtype = facet.parent.name
        existing_paths.add("{0}.{1}".format(branch, subtype))
        label = str(facet.relative_to(ROOT))

        tree = ast.parse(facet.read_text(encoding="utf-8"), filename=str(facet))
        for node in tree.body:
            name, value = _assignment(node)
            if name is None or not isinstance(value, ast.Tuple):
                continue

            if name == "SDGS":
                for element in value.elts:
                    if isinstance(element, ast.Constant) and isinstance(element.value, int):
                        sdgs.add(element.value)
                continue

            registry = FIELD_TO_REGISTRY.get(name)
            if name == "RELATED":
                registry = "related"
            if registry is None:
                continue

            for element in value.elts:
                if isinstance(element, ast.Constant) and isinstance(element.value, str):
                    by_registry[registry].setdefault(element.value, set()).add(label)

    return by_registry, existing_paths, sdgs


def _assignment(node: ast.stmt) -> Tuple[object, object]:
    """Normalise `X = ...` and `X: T = ...` into (name, value)."""
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return node.target.id, node.value
    if isinstance(node, ast.Assign) and len(node.targets) == 1:
        target = node.targets[0]
        if isinstance(target, ast.Name):
            return target.id, node.value
    return None, None


# =============================================================================
#  READING WHAT THE REGISTRIES CONTAIN
# =============================================================================


def registry_keys(name: str) -> Set[str]:
    """Keys a registry package declares, or an empty set if it is unwritten.

    Read by parsing rather than importing, for the same reason as everything
    else here. A registry is recognised by a module-level `KEYS` collection or
    by the keys of a module-level mapping named `ENTRIES`, which is the shape
    the registries will take.
    """
    package = SRC / name
    if not package.is_dir():
        return set()

    keys: Set[str] = set()
    for module in sorted(package.rglob("*.py")):
        try:
            tree = ast.parse(module.read_text(encoding="utf-8"), filename=str(module))
        except SyntaxError:
            continue
        for node in tree.body:
            field, value = _assignment(node)
            if field == "KEYS" and isinstance(value, (ast.Tuple, ast.List, ast.Set)):
                keys.update(
                    e.value
                    for e in value.elts
                    if isinstance(e, ast.Constant) and isinstance(e.value, str)
                )
            elif field == "ENTRIES" and isinstance(value, ast.Dict):
                keys.update(
                    k.value
                    for k in value.keys
                    if isinstance(k, ast.Constant) and isinstance(k.value, str)
                )
    return keys


def pending_colours() -> Set[str]:
    """Branch directories that hold no subtype package."""
    pending: Set[str] = set()
    for branch_dir in BRANCHES.iterdir():
        if not branch_dir.is_dir() or branch_dir.name.startswith("__"):
            continue
        if not any(p.is_dir() and not p.name.startswith("__") for p in branch_dir.iterdir()):
            pending.add(branch_dir.name)
    return pending


# =============================================================================
#  ENTRY POINT
# =============================================================================


def main(argv: List[str] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat unwritten registries and forward references as errors",
    )
    args = parser.parse_args(argv)

    if not BRANCHES.is_dir():
        print("cannot read {0}".format(BRANCHES), file=sys.stderr)
        return 2

    by_registry, existing_paths, sdgs = collect_references()
    pending = pending_colours()

    errors: List[str] = []
    notes: List[str] = []

    # -- related paths --------------------------------------------------------
    forward = 0
    for path, files in sorted(by_registry["related"].items()):
        if path in existing_paths:
            continue
        colour = path.split(".", 1)[0]
        if colour in pending and not args.strict:
            forward += 1
            continue
        errors.append(
            "related {0!r} names no record  (in {1})".format(
                path, ", ".join(sorted(files)[:2])
            )
        )
    if forward:
        notes.append(
            "{0} forward reference(s) into branches not yet written: {1}".format(
                forward, ", ".join(sorted(pending))
            )
        )

    # -- registry keys --------------------------------------------------------
    for registry in sorted(FIELD_TO_REGISTRY.values()):
        referenced = by_registry[registry]
        known = registry_keys(registry)

        if not known:
            notes.append(
                "{0:11} {1:5} key(s) referenced, registry not written yet".format(
                    registry, len(referenced)
                )
            )
            if args.strict:
                errors.append(
                    "registry {0!r} is empty but {1} key(s) point into it".format(
                        registry, len(referenced)
                    )
                )
            continue

        unresolved = sorted(k for k in referenced if k not in known)
        for key in unresolved:
            errors.append(
                "{0} key {1!r} does not resolve  (in {2})".format(
                    registry, key, ", ".join(sorted(referenced[key])[:2])
                )
            )
        notes.append(
            "{0:11} {1:5} of {2:5} referenced key(s) resolve".format(
                registry, len(referenced) - len(unresolved), len(referenced)
            )
        )

    # -- sdgs -----------------------------------------------------------------
    out_of_range = sorted(g for g in sdgs if not 1 <= g <= 17)
    for goal in out_of_range:
        errors.append("SDG {0} does not exist; the goals are numbered 1 to 17".format(goal))

    # -- report ---------------------------------------------------------------
    for note in notes:
        print("     {0}".format(note))
    print()

    if errors:
        print("FAIL: {0} unresolved reference(s).".format(len(errors)))
        print()
        for error in errors[:60]:
            print("  - {0}".format(error))
        if len(errors) > 60:
            print("  ... and {0} more".format(len(errors) - 60))
        return 1

    print("OK: every reference that can be checked resolves.")
    if not args.strict and notes:
        print(
            "     Re-run with --strict once every registry is written; it will "
            "then fail on the counts above."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
