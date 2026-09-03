# =============================================================================
#  tests/test_packaging.py
# -----------------------------------------------------------------------------
#  The distribution, and the public surface it is supposed to carry.
#
#  WHY THIS FILE EXISTS
#  Because the defect it guards against had already shipped and no test could
#  have caught it. `src/biotechnology/core/` had no `__init__.py`, so setuptools
#  discovery omitted the entire machinery layer from the wheel, and
#  `import biotechnology` raised ModuleNotFoundError for every installed copy
#  while working perfectly in the repository:
#
#      A SOURCE CHECKOUT AND AN EDITABLE INSTALL BOTH FALL BACK TO IMPLICIT
#      NAMESPACE PACKAGES. THE PEOPLE MOST LIKELY TO RUN THE TESTS WERE THE
#      PEOPLE LEAST LIKELY TO SEE THE FAILURE.
#
#  So the tests here deliberately do not import the thing they are checking.
#  They ask setuptools what it would package, and they read `pyproject.toml`,
#  which is the only way to see a packaging fault from inside the checkout that
#  hides it.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from pathlib import Path
from typing import Set

import pytest

import biotechnology as bt

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"


def discoverable() -> Set[str]:
    from setuptools import find_packages

    return set(find_packages(where=str(SRC)))


# =============================================================================
#  DISCOVERY
# =============================================================================


def test_every_module_directory_is_packaged() -> None:
    """A directory holding modules and no `__init__.py` ships nothing.

    Empty directories are excluded: the unwritten branches and the empty
    registries ship nothing either way, so they cannot break an install.
    """
    found = discoverable()
    missing = []
    for path in SRC.rglob("*.py"):
        if "__pycache__" in path.parts or "egg-info" in str(path):
            continue
        package = ".".join(path.parent.relative_to(SRC).parts)
        if package and package not in found:
            missing.append(package)
    assert not missing, "would be omitted from the wheel: {0}".format(sorted(set(missing)))


def test_core_is_packaged() -> None:
    """Named explicitly because this is the one that actually broke."""
    assert "biotechnology.core" in discoverable()


def test_every_written_branch_is_packaged() -> None:
    found = discoverable()
    for branch in bt.branches():
        assert "biotechnology.branches.{0}".format(branch.key) in found
        for subtype in branch.subtypes:
            assert (
                "biotechnology.branches.{0}.{1}".format(branch.key, subtype.key) in found
            )


def test_py_typed_marker_is_present() -> None:
    """PEP 561: without this file, type checkers ignore the package entirely."""
    assert (SRC / "biotechnology" / "py.typed").exists()


# =============================================================================
#  ENTRY POINT
# =============================================================================


def test_console_script_target_exists() -> None:
    """`pyproject.toml` declares `biotechnology = biotechnology.cli:main`.

    It previously pointed at a module that imported a package that did not
    exist, so the script installed and then failed on first use.
    """
    from biotechnology import cli

    assert callable(cli.main)


def test_module_entry_point_shares_the_same_main() -> None:
    """`python -m biotechnology` and the console script must not diverge."""
    import biotechnology.__main__ as dunder_main
    from biotechnology import cli

    assert dunder_main.main is cli.main


# =============================================================================
#  THE PUBLIC SURFACE
# =============================================================================


def test_dunder_all_is_importable() -> None:
    """Every name in `__all__` must actually exist.

    A name listed and not defined is an ImportError for anyone using
    `from biotechnology import *`, and it is invisible to every other test.
    """
    for name in bt.__all__:
        assert hasattr(bt, name), name


def test_core_dunder_all_is_importable() -> None:
    from biotechnology import core

    for name in core.__all__:
        assert hasattr(core, name), name


def test_metadata_is_present() -> None:
    for attribute in ("__version__", "__author__", "__license__", "__url__"):
        assert getattr(bt, attribute)


def test_licence_is_declared_consistently() -> None:
    """The SPDX identifier in the package must match the licence file present."""
    assert bt.__license__ == "EUPL-1.2"
    assert (ROOT / "LICENCE").exists()


# =============================================================================
#  DEPENDENCIES
#
#  Zero runtime dependencies is a hard constraint in GOVERNANCE.md 3.3, not a
#  preference. `tools/check_no_dependencies.py` enforces it against the source;
#  this asserts it against the declared metadata, which is the half a reader of
#  `pyproject.toml` sees.
# =============================================================================


def test_no_runtime_dependencies_are_declared() -> None:
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    in_project = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("["):
            in_project = stripped == "[project]"
            continue
        if in_project and stripped.startswith("dependencies"):
            assert stripped.replace(" ", "") in {
                "dependencies=[]",
                "dependencies=[]  #none,bydesign",
            } or stripped.endswith("[]"), stripped
