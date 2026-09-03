# =============================================================================
#  tests/test_taxonomy.py
# -----------------------------------------------------------------------------
#  The registry API: lookup, resolution, filtering and traversal.
#
#  WHERE THIS DIFFERS FROM test_integrity.py
#  That file asserts properties of the DATA. This one asserts the behaviour of
#  the CODE that reads it, including the behaviour on bad input, which is the
#  half most likely to rot. A lookup that returns the right record for a valid
#  path is easy; one that raises a useful error for an invalid one is where the
#  work is, and it is what a user meets first.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

import pytest

import biotechnology as bt
from biotechnology.core.errors import (
    BiotechnologyError,
    UnknownBranchError,
    UnknownSubtypeError,
)
from biotechnology.core.models import Branch, Subtype


# =============================================================================
#  LOOKUP
# =============================================================================


def test_get_branch_by_key() -> None:
    branch = bt.get_branch("grey")
    assert isinstance(branch, Branch)
    assert branch.key == "grey"


def test_get_branch_is_case_insensitive() -> None:
    assert bt.get_branch("GREY") is bt.get_branch("grey")


def test_get_branch_by_alias() -> None:
    """Aliases exist so a reader can arrive with the word their field uses."""
    assert bt.get_branch("environmental").key == "grey"


def test_get_subtype_by_path() -> None:
    subtype = bt.get_subtype("grey.biomining")
    assert isinstance(subtype, Subtype)
    assert subtype.key == "biomining"
    assert subtype.branch_key == "grey"


def test_get_accepts_both_levels() -> None:
    assert bt.get("grey").key == "grey"
    assert bt.get("grey.biomining").key == "biomining"


def test_us_spelling_alias_is_the_same_object() -> None:
    """GRAY is documented as an alias, not a copy.

    Asserted with `is` rather than `==` because a copy would compare equal and
    quietly double the memory and the confusion.
    """
    assert bt.GRAY is bt.GREY


# =============================================================================
#  FAILING LOOKUP
#
#  The half that decides whether this library is pleasant to use. Every error
#  must name the token that failed and offer the valid alternatives, because
#  the commonest cause is a typo and the second commonest is not knowing the
#  vocabulary.
# =============================================================================


def test_unknown_branch_names_the_token_and_the_alternatives() -> None:
    with pytest.raises(UnknownBranchError) as caught:
        bt.get_branch("purpel")
    message = str(caught.value)
    assert "purpel" in message
    assert "grey" in message


def test_unknown_subtype_names_the_token() -> None:
    with pytest.raises(UnknownSubtypeError) as caught:
        bt.get_subtype("grey.biominning")
    assert "biominning" in str(caught.value)


def test_every_library_error_is_catchable_as_one_type() -> None:
    """The whole point of the hierarchy: one except clause covers the library.

    An ordinary Python error must still propagate, which is why this asserts
    the base class rather than a bare `Exception`.
    """
    for bad in ("nosuchbranch", "grey.nosuchrecord", "a.b.c.d"):
        with pytest.raises(BiotechnologyError):
            bt.get(bad)


def test_pending_branch_lookup_fails_rather_than_returning_none() -> None:
    """A branch that is not written must raise, not resolve to nothing.

    `bt.BROWN` is None by design, which is a stated value. `get_branch("brown")`
    is a lookup that cannot be satisfied, and returning None there would push
    the failure to the caller's next attribute access.
    """
    if "brown" not in bt.PENDING_COLOURS:  # pragma: no cover - future state
        pytest.skip("brown has been written")
    with pytest.raises(UnknownBranchError):
        bt.get_branch("brown")


# =============================================================================
#  FILTERING
# =============================================================================


def test_by_sdg_returns_only_records_citing_it(all_subtypes: Tuple[Subtype, ...]) -> None:
    matches = bt.by_sdg(6)
    assert matches
    for subtype in matches:
        assert 6 in subtype.sdgs
    expected = {s.path for s in all_subtypes if 6 in s.sdgs}
    assert {s.path for s in matches} == expected


def test_by_maturity_partitions_the_taxonomy(all_subtypes: Tuple[Subtype, ...]) -> None:
    """Every record has exactly one maturity, so the filters must partition.

    A record appearing in two buckets, or in none, means an enum comparison is
    wrong somewhere.
    """
    total = 0
    for value in bt.Maturity:
        total += len(bt.by_maturity(value))
    assert total == len(all_subtypes)


def test_by_domain_matches_membership(all_subtypes: Tuple[Subtype, ...]) -> None:
    matches = bt.by_domain(bt.Domain.ENVIRONMENT)
    expected = {s.path for s in all_subtypes if bt.Domain.ENVIRONMENT in s.domains}
    assert {s.path for s in matches} == expected


# =============================================================================
#  TRAVERSAL
# =============================================================================


def test_related_to_resolves_paths_into_records() -> None:
    """`related` holds paths; `related_to` resolves them into records.

    It takes a path rather than a record, which is worth asserting because the
    signature invites the other reading.

    Records pointing into unwritten branches are dropped rather than raising,
    because a forward reference is a documented pattern and a traversal that
    exploded on one would be unusable until the taxonomy is complete. So the
    result is bounded above by the number of declared edges, not equal to it.
    """
    subtype = bt.get_subtype("grey.biomining")
    resolved = bt.related_to(subtype.path)
    for item in resolved:
        assert isinstance(item, Subtype)
    assert 0 < len(resolved) <= len(subtype.related)
    assert subtype.path not in {s.path for s in resolved}


def test_related_to_depth_widens_the_neighbourhood() -> None:
    near = bt.related_to("grey.biomining", depth=1)
    far = bt.related_to("grey.biomining", depth=2)
    assert {s.path for s in near} <= {s.path for s in far}


def test_timeline_returns_sorted_triples(
    known_paths: frozenset, written_colours: Tuple[str, ...]
) -> None:
    """`timeline` yields (year, event, source), not Milestone objects.

    Asserted because the name suggests otherwise, and the difference is the
    kind that surfaces as an AttributeError in a caller rather than here.

    The third element is a BRANCH KEY for a branch-level milestone and a
    SUBTYPE PATH for a record-level one. Both are present in the merged
    timeline, which is correct: branches carry their own history. An earlier
    version of this test assumed every source contained a dot and failed on
    the first branch milestone it met.
    """
    rows = bt.timeline()
    assert rows
    for year, event, source in rows:
        assert isinstance(year, int)
        assert isinstance(event, str) and event
        assert source in known_paths or source in written_colours, source

    years = [row[0] for row in rows]
    assert years == sorted(years)
    assert len(years) > 100


def test_timeline_since_filters() -> None:
    recent = bt.timeline(since=2000)
    assert recent
    assert all(row[0] >= 2000 for row in recent)


def test_counts_reports_the_written_taxonomy(all_subtypes: Tuple[Subtype, ...]) -> None:
    counts = bt.counts()
    assert counts["subtypes"] == len(all_subtypes)


# =============================================================================
#  BRANCH CONTAINER PROTOCOL
#
#  Branch implements __iter__, __len__, __contains__ and __getitem__. Those
#  make `for subtype in branch` and `branch["biomining"]` work, and a container
#  protocol that is half implemented is worse than none because it invites the
#  syntax and then fails on it.
# =============================================================================


def test_branch_is_a_container() -> None:
    branch = bt.get_branch("grey")
    assert len(branch) == len(branch.subtypes)
    assert list(branch) == list(branch.subtypes)
    assert "biomining" in branch
    assert branch["biomining"].key == "biomining"


def test_branch_is_light_matches_luma() -> None:
    """The property that decides label colour on a swatch.

    White and yellow are the two light branches; grey is not. Asserted because
    a docstring in `core/models.py` previously claimed white was the only one,
    which was wrong and was found by importing rather than by reading.
    """
    assert bt.WHITE.is_light is True
    assert bt.YELLOW.is_light is True
    assert bt.GREY.is_light is False
    assert bt.RED.is_light is False


# =============================================================================
#  COVERAGE REPORTING
# =============================================================================


def test_pending_and_written_partition_the_colours(
    colour_order: Tuple[str, ...],
    written_colours: Tuple[str, ...],
    pending_colours: Tuple[str, ...],
) -> None:
    assert set(written_colours) | set(pending_colours) == set(colour_order)
    assert not set(written_colours) & set(pending_colours)


def test_pending_branch_constants_are_none() -> None:
    """The four constants are None while pending, and a Branch once written.

    This is the assertion that fires when a branch lands and its constant is
    not switched over, which is otherwise easy to forget.
    """
    for key in ("BROWN", "GOLD", "DARK", "PURPLE"):
        value = getattr(bt, key)
        expected_pending = key.lower() in bt.PENDING_COLOURS
        if expected_pending:
            assert value is None, "{0} should be None while pending".format(key)
        else:  # pragma: no cover - future state
            assert isinstance(value, Branch), key
