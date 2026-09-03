# =============================================================================
#  tests/test_integrity.py
# -----------------------------------------------------------------------------
#  The integrity suite. `make validate` runs this file by name, so it is the
#  one test module that is part of the release gate rather than of the
#  development loop.
#
#  WHAT IT IS FOR
#  Everything here asserts a property of the DATASET rather than of the code.
#  A failure means a record is wrong, not that a function is broken. That
#  distinction decides how the assertions are written: each one names the
#  offending record and the offending value, because the person reading the
#  failure is going to open a facet file and fix a fact.
#
#  A NOTE ON WHAT IS NOT ASSERTED
#  Nothing here checks whether a claim is TRUE. No test can. The suite
#  guarantees internal consistency and the editorial minimums, and the truth of
#  a regulation citation or a milestone date is settled by review against a
#  source, which is what the pull request template's Section 3 exists for.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

import pytest

import biotechnology as bt
from biotechnology.core import validation
from biotechnology.core.models import Branch, Subtype

pytestmark = pytest.mark.integrity


# =============================================================================
#  THE VALIDATOR ITSELF
#
#  One test that runs the whole suite, so that a new check added to
#  `core.validation` is enforced here without anyone remembering to add a test
#  for it.
# =============================================================================


def test_validator_reports_no_errors() -> None:
    findings = validation.validate(raise_on_error=False)
    errors = [f for f in findings if f.is_error]
    assert not errors, "\n".join(str(f) for f in errors)


def test_warnings_are_only_the_expected_kinds(pending_colours: Tuple[str, ...]) -> None:
    """Warnings must be explainable, or they are errors nobody looked at.

    Three kinds are expected while the taxonomy is incomplete. Anything else
    is a finding that has been allowed to become background noise, which is
    how a warning stops meaning anything.
    """
    expected = {"forward-reference", "alias-collision", "branch-pending"}
    findings = validation.validate(raise_on_error=False)
    unexpected = {f.rule for f in findings if not f.is_error} - expected
    assert not unexpected, "unexplained warning kinds: {0}".format(sorted(unexpected))

    if not pending_colours:
        # When the last branch lands, forward references must be gone. This
        # assertion is the reminder, and it is written so that it starts
        # failing the moment it becomes relevant rather than being remembered.
        forward = [f for f in findings if f.rule == "forward-reference"]
        assert not forward, "taxonomy is complete but forward references remain"


# =============================================================================
#  ADDRESSING
# =============================================================================


def test_every_path_is_unique(all_subtypes: Tuple[Subtype, ...]) -> None:
    paths = [s.path for s in all_subtypes]
    duplicates = {p for p in paths if paths.count(p) > 1}
    assert not duplicates, "duplicate paths: {0}".format(sorted(duplicates))


def test_every_path_resolves(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        assert bt.get(subtype.path) is subtype, subtype.path


def test_key_matches_path(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        assert subtype.path == "{0}.{1}".format(subtype.branch_key, subtype.key)


def test_branch_membership_is_consistent(all_branches: Tuple[Branch, ...]) -> None:
    for branch in all_branches:
        for subtype in branch.subtypes:
            assert subtype.branch_key == branch.key, subtype.path


# =============================================================================
#  CROSS-REFERENCES
# =============================================================================


def test_related_targets_exist_or_are_pending(
    all_subtypes: Tuple[Subtype, ...],
    known_paths: frozenset,
    pending_colours: Tuple[str, ...],
) -> None:
    """A related entry names a record, or a branch that does not exist yet.

    Anything else is a typo, and a typo here is invisible: it produces no
    error, no warning and no broken link a reader would notice.
    """
    for subtype in all_subtypes:
        for target in subtype.related:
            if target in known_paths:
                continue
            colour = target.split(".", 1)[0]
            assert colour in pending_colours, "{0} -> {1} resolves to nothing".format(
                subtype.path, target
            )


def test_no_record_relates_to_itself(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        assert subtype.path not in subtype.related, subtype.path


def test_related_entries_are_unique(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        assert len(set(subtype.related)) == len(subtype.related), subtype.path


# =============================================================================
#  EDITORIAL MINIMUMS
#
#  Asserted here as well as in the validator, on purpose. The validator can be
#  called with `raise_on_error=False` and its result ignored; a test cannot.
# =============================================================================


def test_narrative_fields_are_present(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        for field in (
            "summary",
            "description",
            "plain_language",
            "analogy",
            "why_it_matters",
        ):
            assert getattr(subtype, field).strip(), "{0}: {1} is empty".format(
                subtype.path, field
            )


def test_summary_is_bounded(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        assert len(subtype.summary) <= validation.MAX_SUMMARY_LENGTH, "{0}: {1} chars".format(
            subtype.path, len(subtype.summary)
        )


def test_countable_minimums(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        assert len(subtype.applications) >= validation.MIN_APPLICATIONS, subtype.path
        assert len(subtype.challenges) >= validation.MIN_CHALLENGES, subtype.path
        assert len(subtype.milestones) >= validation.MIN_MILESTONES, subtype.path
        assert (
            validation.MIN_RELATED <= len(subtype.related) <= validation.MAX_RELATED
        ), "{0}: {1} related".format(subtype.path, len(subtype.related))


def test_every_metric_is_complete(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        for metric in subtype.metrics:
            assert metric.name.strip(), subtype.path
            assert metric.unit.strip(), "{0}: {1} has no unit".format(
                subtype.path, metric.name
            )
            assert isinstance(metric.typical, str), "{0}: {1}".format(
                subtype.path, metric.name
            )
            assert metric.evidence is not None, "{0}: {1}".format(
                subtype.path, metric.name
            )


def test_sdgs_are_in_range_and_unique(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        for goal in subtype.sdgs:
            assert 1 <= goal <= 17, "{0}: SDG {1}".format(subtype.path, goal)
        assert len(set(subtype.sdgs)) == len(subtype.sdgs), subtype.path


# =============================================================================
#  NOTATION
# =============================================================================


def test_no_non_ascii_anywhere_in_the_data(all_subtypes: Tuple[Subtype, ...]) -> None:
    """The rule that stops a Greek mu reaching a metric symbol.

    Checked against assembled data rather than source text, so it also catches
    a character that arrives through a computed value.
    """
    for subtype in all_subtypes:
        haystack = subtype.haystack
        if callable(haystack):
            haystack = haystack()
        offenders = sorted({c for c in haystack if ord(c) > 127})
        assert not offenders, "{0}: {1}".format(
            subtype.path, ["U+{0:04X}".format(ord(c)) for c in offenders]
        )


def test_metric_symbols_are_ascii(all_subtypes: Tuple[Subtype, ...]) -> None:
    for subtype in all_subtypes:
        for metric in subtype.metrics:
            assert metric.symbol.isascii(), "{0}: {1}".format(subtype.path, metric.symbol)


# =============================================================================
#  HISTORY
# =============================================================================


def test_milestone_years_are_plausible(all_subtypes: Tuple[Subtype, ...]) -> None:
    """Negative years are legitimate and mean BCE.

    Asserted explicitly because the obvious `year > 0` bound is wrong here and
    has already been written once: this corpus records -9000 for the
    domestication of wheat and -7000 for the earliest deliberate fermentation.
    """
    for subtype in all_subtypes:
        for milestone in subtype.milestones:
            assert -12000 <= milestone.year <= 2100, "{0}: {1}".format(
                subtype.path, milestone.year
            )
            assert milestone.event.strip(), subtype.path


def test_timeline_is_sorted(all_subtypes: Tuple[Subtype, ...]) -> None:
    """`Subtype.timeline` sorts; `milestones` does not have to.

    History facets group thematically by house style, so the raw tuple is
    frequently out of order and that is correct. The property that sorts it is
    what callers use, and it must actually sort.
    """
    for subtype in all_subtypes:
        years = [m.year for m in subtype.timeline]
        assert years == sorted(years), subtype.path


# =============================================================================
#  BRANCH-LEVEL
# =============================================================================


def test_branch_colours_are_hex(all_branches: Tuple[Branch, ...]) -> None:
    for branch in all_branches:
        assert branch.colour.startswith("#"), branch.key
        assert len(branch.colour) == 7, branch.key
        int(branch.colour[1:], 16)


def test_branch_order_matches_colour_order(
    all_branches: Tuple[Branch, ...], written_colours: Tuple[str, ...]
) -> None:
    assert tuple(b.key for b in all_branches) == written_colours


def test_every_branch_has_subtypes(all_branches: Tuple[Branch, ...]) -> None:
    for branch in all_branches:
        assert branch.subtypes, branch.key
