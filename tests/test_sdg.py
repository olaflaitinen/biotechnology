# =============================================================================
#  tests/test_sdg.py
# -----------------------------------------------------------------------------
#  The Sustainable Development Goal registry.
#
#  WHY THIS ONE GETS ITS OWN FILE
#  It is the only registry that can be complete rather than merely started,
#  because its contents are a fixed, published, seventeen-item list. That makes
#  it the one place where "every referenced key resolves" is a property the
#  suite can actually assert today, and asserting it here is what proves the
#  registry contract works before the five open-ended registries adopt it.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

import pytest

import biotechnology as bt
from biotechnology import sdg
from biotechnology.core.errors import BiotechnologyError
from biotechnology.core.models import Subtype


# =============================================================================
#  COMPLETENESS
# =============================================================================


def test_there_are_seventeen_goals() -> None:
    assert len(sdg.goals()) == 17


def test_numbering_has_no_gaps() -> None:
    assert sdg.KEYS == tuple(range(1, 18))


def test_every_goal_has_a_title_and_a_short_label() -> None:
    for goal in sdg.goals():
        assert goal.title.strip()
        assert goal.short.strip()
        assert goal.theme in sdg.themes()


def test_titles_are_ascii() -> None:
    """The resolution uses typographic characters; this registry does not.

    Titles get cited, so they are transliterated once here rather than by each
    consumer, and the project's ASCII rule applies to them like everything
    else.
    """
    for goal in sdg.goals():
        assert goal.title.isascii(), goal.number
        assert goal.short.isascii(), goal.number


def test_titles_are_distinct() -> None:
    titles = [goal.title for goal in sdg.goals()]
    assert len(set(titles)) == len(titles)


# =============================================================================
#  LOOKUP
# =============================================================================


def test_get_resolves_by_number() -> None:
    assert sdg.get(6).short == "Clean water"
    assert sdg.title_of(13).startswith("Take urgent action")
    assert sdg.short_of(15) == "Life on land"


def test_get_accepts_a_numeric_string() -> None:
    """Records store integers, but a CLI hands over a string.

    Coercing here rather than at every call site is deliberate, and worth a
    test because the coercion is what makes `exists("six")` non-obvious.
    """
    assert sdg.get("6").number == 6


def test_unknown_goal_raises_a_library_error() -> None:
    for bad in (0, 18, -1, "six", None):
        with pytest.raises(BiotechnologyError):
            sdg.get(bad)


def test_the_error_names_the_valid_range() -> None:
    with pytest.raises(sdg.UnknownGoalError) as caught:
        sdg.get(18)
    assert "1 to 17" in str(caught.value)


def test_exists_never_raises() -> None:
    assert sdg.exists(17) is True
    assert sdg.exists(18) is False
    assert sdg.exists("six") is False
    assert sdg.exists(None) is False


# =============================================================================
#  THEMES
# =============================================================================


def test_themes_partition_the_goals() -> None:
    covered = []
    for theme in sdg.themes():
        covered.extend(sdg.by_theme(theme))
    assert len(covered) == 17
    assert {g.number for g in covered} == set(sdg.KEYS)


def test_unknown_theme_lists_the_valid_ones() -> None:
    with pytest.raises(sdg.UnknownGoalError) as caught:
        sdg.by_theme("prosperity and joy")
    assert "planet" in str(caught.value)


# =============================================================================
#  THE INTEGRATION THAT WAS BROKEN
# =============================================================================


def test_sdg_titles_on_a_record_now_resolves(all_subtypes: Tuple[Subtype, ...]) -> None:
    """`Subtype.sdg_titles` raised ImportError until this registry existed.

    Asserted across every record rather than one, because the property is
    computed per goal and a single bad number would only surface on the record
    that cites it.
    """
    for subtype in all_subtypes:
        titles = subtype.sdg_titles
        assert len(titles) == len(subtype.sdgs)
        for title in titles:
            assert title.strip()


def test_every_cited_goal_resolves(all_subtypes: Tuple[Subtype, ...]) -> None:
    """The one registry where full coverage is assertable today."""
    cited = {goal for subtype in all_subtypes for goal in subtype.sdgs}
    assert cited
    for goal in cited:
        assert sdg.exists(goal), goal
