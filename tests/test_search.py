# =============================================================================
#  tests/test_search.py
# -----------------------------------------------------------------------------
#  The ranking function.
#
#  WHAT IS WORTH ASSERTING ABOUT A RANKER
#  Not the absolute scores. Those are tuning constants and changing them is
#  allowed; a test that pinned them would fail on every improvement and teach
#  the next person to delete it.
#
#  What must hold is the ORDERING GUARANTEE the module claims: an address beats
#  a name, a name beats a mention, and no amount of repetition in a body lets a
#  passing mention outrank a title. Those are the properties a user notices,
#  and they are the ones a refactor can silently break.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

import pytest

import biotechnology as bt
from biotechnology.core import search as search_module
from biotechnology.core.models import Branch, Subtype


def paths(results) -> list:
    return [getattr(node, "path", node.key) for node in results]


# =============================================================================
#  THE ORDERING GUARANTEE
# =============================================================================


def test_exact_path_wins() -> None:
    assert paths(bt.search("grey.biomining"))[0] == "grey.biomining"


def test_exact_key_wins() -> None:
    assert paths(bt.search("biomining"))[0] == "grey.biomining"


def test_alias_finds_the_record_it_names() -> None:
    """Aliases exist so a reader can arrive with their field's word.

    "bioleaching" is what a hydrometallurgist would type; `biomining` is the
    key. If the alias does not win, the alias is decorative.
    """
    assert paths(bt.search("bioleaching"))[0] == "grey.biomining"


def test_a_title_outranks_a_passing_mention() -> None:
    """The property the frequency cap exists to protect.

    Many records mention wastewater. One is named for it, and it must come
    first however often the others say the word.
    """
    assert paths(bt.search("wastewater treatment"))[0] == "grey.wastewater_treatment"


def test_body_mentions_still_match() -> None:
    """A term appearing only in prose must be findable.

    Otherwise search is a key lookup wearing a different name.
    """
    results = paths(bt.search("colonisation resistance"))
    assert "grey.bioaugmentation" in results


# =============================================================================
#  SUBSTRING MATCHING
# =============================================================================


def test_substring_finds_compound_keys() -> None:
    """Token matching would find none of these.

    The corpus is full of compound keys where the useful prefix is not a word,
    which is why matching is substring rather than token.
    """
    results = paths(bt.search("ferment"))
    for expected in (
        "white.microbial_fermentation",
        "yellow.food_fermentation",
        "yellow.precision_fermentation",
    ):
        assert expected in results


def test_search_is_case_insensitive() -> None:
    assert paths(bt.search("BIOMINING")) == paths(bt.search("biomining"))


def test_very_short_queries_return_nothing() -> None:
    """One character matches most of the corpus, which is not an answer."""
    assert bt.search("a") == []
    assert bt.search("") == []
    assert len(bt.search("bi")) > 0


# =============================================================================
#  DETERMINISM
# =============================================================================


def test_results_are_reproducible() -> None:
    """Ties are broken by path so the ordering is total.

    Without that, equal-scoring records could swap between runs and produce a
    diff in generated documentation.
    """
    assert paths(bt.search("bio")) == paths(bt.search("bio"))


def test_scores_are_monotonically_non_increasing() -> None:
    scores = [score for _, score in search_module.search_scored("bio")]
    assert scores == sorted(scores, reverse=True)


# =============================================================================
#  FILTERS
# =============================================================================


def test_branch_filter_restricts_subtypes_only() -> None:
    """A branch has no maturity, so filters apply to subtypes.

    Branches are left in rather than excluded whenever any filter is set,
    which is the useful behaviour rather than the consistent one, and it is
    documented as such.
    """
    results = search_module.search("bio", branch="grey", include_branches=False)
    assert results
    for node in results:
        assert node.branch_key == "grey"


def test_maturity_filter_applies() -> None:
    results = search_module.search(
        "bio", maturity=bt.Maturity.ESTABLISHED, include_branches=False
    )
    for node in results:
        assert node.maturity is bt.Maturity.ESTABLISHED


def test_domain_filter_applies() -> None:
    results = search_module.search(
        "bio", domain=bt.Domain.ENVIRONMENT, include_branches=False
    )
    for node in results:
        assert bt.Domain.ENVIRONMENT in node.domains


def test_include_branches_toggles_branch_records() -> None:
    with_branches = bt.search("marine")
    without = search_module.search("marine", include_branches=False)
    assert any(isinstance(n, Branch) for n in with_branches)
    assert all(isinstance(n, Subtype) for n in without)


def test_limit_truncates() -> None:
    assert len(bt.search("bio", limit=3)) == 3
