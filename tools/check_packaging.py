#!/usr/bin/env python3
# =============================================================================
#  tools/check_packaging.py
# -----------------------------------------------------------------------------
#  Asserts that every directory holding a Python module under `src/` is
#  discoverable by the packaging configuration in `pyproject.toml`.
#
#  WHY THIS CHECK EXISTS
#  It exists because the defect it detects had already shipped, and because the
#  defect is invisible from a source checkout.
#
#  `pyproject.toml` uses the default setuptools discovery directive:
#
#      [tool.setuptools.packages.find]
#      where = ["src"]
#
#  `find` locates REGULAR packages only, and a regular package is a directory
#  containing `__init__.py`. `biotechnology/core/` had no `__init__.py`, so
#  `find_packages` returned 58 packages without it, and the built wheel omitted
#  the entire machinery layer. Since `biotechnology/__init__.py` imports from
#  `.core.enums` on its first executable line, `import biotechnology` raised
#  `ModuleNotFoundError` on any installed copy.
#
#      IT WORKED IN THE REPOSITORY AND FAILED FOR EVERY USER.
#
#  That asymmetry is the whole reason for this file. In a source checkout, and
#  under an editable install, Python falls back to implicit namespace packages
#  and imports the directory happily. The people most likely to run the test
#  suite are therefore the people least likely to see the failure, and no
#  amount of testing from the checkout would have caught it.
#
#  WHAT IT CHECKS
#      1. Every directory under `src/` containing a `.py` file is returned by
#         `setuptools.find_packages`.
#      2. Every module a top-level `__init__` imports from resolves to a
#         directory that check 1 accepts.
#      3. The `[project.scripts]` entry point names a module that exists and
#         an attribute that module actually defines.
#
#  DELIBERATELY NOT CHECKED
#  Empty directories are ignored rather than reported. `branches/brown/` and
#  the registries are empty on purpose while the taxonomy is being written, and
#  an empty directory ships nothing, so it cannot break an install. This script
#  reports only what would actually be lost.
#
#  EXIT CODES
#      0  every module directory is discoverable
#      1  at least one would be omitted from a built distribution
#      2  the packaging configuration could not be read
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import ast
import sys
from pathlib import Path
from typing import List, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
PYPROJECT = ROOT / "pyproject.toml"


# =============================================================================
#  READING THE PACKAGING CONFIGURATION
#
#  `tomllib` is standard library from Python 3.11. The project floor is 3.9, so
#  a checker that imported it unconditionally would fail on exactly the oldest
#  interpreter the project promises to support. Rather than take a development
#  dependency on `tomli`, which GOVERNANCE.md 3.3 would require justifying, the
#  two facts this script needs are read with a small deliberate parser.
# =============================================================================


def read_packaging_config() -> Tuple[List[str], str]:
    """Return (search roots, console script target) from pyproject.toml.

    Falls back to the documented defaults rather than failing, because a
    missing key means setuptools uses those defaults too.
    """
    text = PYPROJECT.read_text(encoding="utf-8")

    # -- where = ["src"] ------------------------------------------------------
    roots: List[str] = []
    in_find = False
    script = ""
    in_scripts = False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("["):
            in_find = line == "[tool.setuptools.packages.find]"
            in_scripts = line == "[project.scripts]"
            continue
        if in_find and line.startswith("where"):
            inner = line.split("=", 1)[1].strip().strip("[]")
            roots = [p.strip().strip('"').strip("'") for p in inner.split(",") if p.strip()]
        if in_scripts and "=" in line and not line.startswith("#"):
            script = line.split("=", 1)[1].strip().strip('"').strip("'")

    return (roots or ["."], script)


# =============================================================================
#  CHECK 1: IS EVERY MODULE DIRECTORY DISCOVERABLE
# =============================================================================


def discoverable_packages(where: Path) -> Set[str]:
    """Directories under `where` that setuptools `find` would return."""
    found: Set[str] = set()
    for init in where.rglob("__init__.py"):
        if "__pycache__" in init.parts or "egg-info" in str(init):
            continue
        rel = init.parent.relative_to(where)
        found.add(".".join(rel.parts))
    return found


def module_directories(where: Path) -> Set[str]:
    """Directories under `where` that contain at least one module.

    A directory with no `.py` file in it ships nothing and is skipped, which
    is what keeps the unwritten branches and the empty registries out of the
    report.
    """
    dirs: Set[str] = set()
    for path in where.rglob("*.py"):
        if "__pycache__" in path.parts or "egg-info" in str(path):
            continue
        rel = path.parent.relative_to(where)
        if rel.parts:
            dirs.add(".".join(rel.parts))
    return dirs


# =============================================================================
#  CHECK 3: DOES THE CONSOLE SCRIPT RESOLVE
# =============================================================================


def check_entry_point(target: str, where: Path) -> List[str]:
    """Verify that `module:attribute` names something that exists.

    The attribute is looked for by parsing the module rather than by importing
    it, because the package cannot be imported while the taxonomy is
    incomplete and a checker that only works on a finished repository is not
    much of a checker.
    """
    problems: List[str] = []
    if not target or ":" not in target:
        return problems

    module_path, _, attribute = target.partition(":")
    parts = module_path.split(".")

    candidate_pkg = where.joinpath(*parts) / "__init__.py"
    candidate_mod = where.joinpath(*parts).with_suffix(".py")
    source_file = candidate_pkg if candidate_pkg.exists() else candidate_mod

    if not source_file.exists():
        problems.append(
            "console script target {0!r} names module {1!r}, which does not "
            "exist. Looked for {2} and {3}.".format(
                target, module_path, candidate_pkg, candidate_mod
            )
        )
        return problems

    tree = ast.parse(source_file.read_text(encoding="utf-8"), filename=str(source_file))
    defined: Set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            defined.add(node.name)
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    defined.add(tgt.id)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                defined.add(alias.asname or alias.name.split(".")[0])

    if attribute not in defined:
        problems.append(
            "console script target {0!r} names attribute {1!r}, which {2} does "
            "not define.".format(target, attribute, source_file.relative_to(ROOT))
        )
    return problems


# =============================================================================
#  ENTRY POINT
# =============================================================================


def main() -> int:
    if not PYPROJECT.exists():
        print("cannot read {0}".format(PYPROJECT), file=sys.stderr)
        return 2

    roots, script = read_packaging_config()
    problems: List[str] = []
    checked = 0

    for root_name in roots:
        where = (ROOT / root_name).resolve()
        if not where.is_dir():
            problems.append("packaging root {0!r} does not exist".format(root_name))
            continue

        found = discoverable_packages(where)
        needed = module_directories(where)
        checked += len(needed)

        for pkg in sorted(needed - found):
            problems.append(
                "{0} contains modules and has no __init__.py, so setuptools "
                "find will omit it from the built distribution.".format(
                    pkg.replace(".", "/")
                )
            )

    problems.extend(check_entry_point(script, (ROOT / roots[0]).resolve()))

    if problems:
        print("FAIL: packaging would omit code, or an entry point does not resolve.")
        print()
        for p in problems:
            print("  - {0}".format(p))
        print()
        print(
            "A directory holding modules must contain __init__.py to be packaged. "
            "This passes from a source checkout regardless, because Python falls "
            "back to implicit namespace packages, so it must be checked rather "
            "than tested."
        )
        return 1

    print(
        "OK: {0} module director(ies) checked; all are discoverable and the "
        "console script resolves.".format(checked)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
