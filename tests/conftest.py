# =============================================================================
#  tests/conftest.py
# -----------------------------------------------------------------------------
#  Shared fixtures.
#
#  A NOTE ON SCOPE THAT IS NOT AN OPTIMISATION
#  Every fixture here is session-scoped. That is not for speed, although it is
#  faster. The records are FROZEN dataclasses and the registry is built once at
#  import time, so a function-scoped fixture would hand every test the same
#  objects while implying they were fresh. Session scope states the truth:
#  there is exactly one taxonomy in the process and no test can mutate it for
#  another.
#
#  If a test ever needs to modify a record, it must build its own, and the
#  frozen dataclasses will make that difficulty obvious rather than letting a
#  mutation leak sideways.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import List, Tuple

import pytest

import biotechnology as bt
from biotechnology.branches import COLOUR_ORDER, PENDING_COLOURS, WRITTEN_COLOURS
from biotechnology.core.models import Branch, Subtype


@pytest.fixture(scope="session")
def all_branches() -> Tuple[Branch, ...]:
    """Every branch whose package is written."""
    return tuple(bt.branches())


@pytest.fixture(scope="session")
def all_subtypes() -> Tuple[Subtype, ...]:
    """Every subtype in every written branch."""
    return tuple(bt.subtypes())


@pytest.fixture(scope="session")
def colour_order() -> Tuple[str, ...]:
    return COLOUR_ORDER


@pytest.fixture(scope="session")
def written_colours() -> Tuple[str, ...]:
    return WRITTEN_COLOURS


@pytest.fixture(scope="session")
def pending_colours() -> Tuple[str, ...]:
    """Branches not written yet.

    Exposed as a fixture rather than imported in each test so that the day it
    becomes empty, every test that skips on it starts running instead of
    quietly continuing to skip.
    """
    return PENDING_COLOURS


@pytest.fixture(scope="session")
def known_paths(all_subtypes: Tuple[Subtype, ...]) -> frozenset:
    """The set of dotted paths that resolve, for cross-reference checks."""
    return frozenset(s.path for s in all_subtypes)


def pytest_collection_modifyitems(items: List[pytest.Item]) -> None:
    """Mark whole-taxonomy tests as slow automatically.

    `make test-fast` excludes `slow`, and the tests that walk all 51 records
    are the ones worth excluding. Marking by module rather than by hand keeps
    the marker from drifting as tests are added, which is what happens to a
    convention that has to be remembered.
    """
    for item in items:
        if item.module.__name__.endswith(("test_integrity", "test_taxonomy")):
            item.add_marker(pytest.mark.slow)
