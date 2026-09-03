# =============================================================================
#  biotechnology.core.validation
# -----------------------------------------------------------------------------
#  The integrity suite. It answers one question:
#
#      IS THIS DATASET INTERNALLY CONSISTENT, AND DOES IT MEET THE EDITORIAL
#      MINIMUMS IT CLAIMS TO MEET?
#
#  It cannot tell you whether a fact is true. Nothing mechanical can. What it
#  can do is guarantee that no cross-reference dangles, no key is duplicated,
#  no metric lacks a unit, and no record quietly falls below the minimums
#  STYLE_GUIDE.md sets out. Those are the failures that accumulate silently in
#  a growing corpus, and they are exactly the ones a human reviewer stops
#  noticing after the twentieth record.
#
#  TWO SEVERITIES, AND THE DISTINCTION IS LOAD-BEARING
#
#      ERROR    the dataset is wrong. A dangling reference, a duplicate key,
#               a metric with no unit. These fail the build.
#      WARNING  the dataset is incomplete in a way that is currently expected.
#               A reference into a branch that has not been written yet is the
#               main case, and there are hundreds of them.
#
#  Collapsing those two would make `validate` useless in either direction. If
#  pending-branch references were errors, validation could never pass until the
#  taxonomy was finished, so nobody would run it. If duplicate keys were
#  warnings, the build would go green on a broken dataset.
#
#  `--strict` promotes warnings to errors. That is the mode the release
#  workflow should use once the tenth branch lands, and the mode CI should not
#  use before then.
#
#  WHY THE REGISTRY CHECKS ARE CONDITIONAL
#  Organism, technique, glossary and citation keys are checked against their
#  registries only when those registries are populated. An empty registry means
#  "not written yet", not "every key is wrong", and reporting two thousand
#  failures for an unwritten module would drown the findings that matter.
#  `registry_coverage()` reports the gap honestly instead.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Callable, Dict, Iterable, List, Optional, Sequence, Set, Tuple

from .errors import ValidationError
from .models import Branch, Subtype
from .registry import branches, subtypes

__all__ = [
    "Finding",
    "validate",
    "check",
    "registry_coverage",
    "MIN_APPLICATIONS",
    "MIN_CHALLENGES",
    "MIN_MILESTONES",
    "MIN_RELATED",
    "MAX_RELATED",
    "MAX_SUMMARY_LENGTH",
]


# =============================================================================
#  EDITORIAL MINIMUMS
#
#  These are the numbers STYLE_GUIDE.md states, lifted into code so that the
#  document and the enforcement cannot drift apart. Changing one of these is a
#  change to the editorial contract and belongs in the same commit as the
#  document edit.
# =============================================================================

MIN_APPLICATIONS = 4  # rule 6
MIN_CHALLENGES = 4  # rule 7
MIN_MILESTONES = 3  # rule 8
MIN_RELATED = 4  # rule 13
MAX_RELATED = 8  # rule 13
MAX_SUMMARY_LENGTH = 200  # rule 4

#: The five narrative fields every record must carry, non-empty.
_NARRATIVE_FIELDS = (
    "summary",
    "description",
    "plain_language",
    "analogy",
    "why_it_matters",
)


# =============================================================================
#  A FINDING
#
#  A plain frozen record rather than a formatted string, so that a caller can
#  filter, group and count. The CLI formats; this module reports.
# =============================================================================


class Finding:
    """One validation result.

    Attributes
    ----------
    severity:
        Either "error" or "warning". See the module header for why the
        distinction matters.
    where:
        The record path, or the check name for a whole-dataset finding.
    rule:
        A short slug naming what was violated, for grouping.
    message:
        A sentence a human can act on. It names the offending value.
    """

    __slots__ = ("severity", "where", "rule", "message")

    def __init__(self, severity: str, where: str, rule: str, message: str) -> None:
        self.severity = severity
        self.where = where
        self.rule = rule
        self.message = message

    @property
    def is_error(self) -> bool:
        return self.severity == "error"

    def __str__(self) -> str:
        return "{0:7} {1:34} {2:22} {3}".format(
            self.severity.upper(), self.where, self.rule, self.message
        )

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return "Finding({0!r}, {1!r}, {2!r}, {3!r})".format(
            self.severity, self.where, self.rule, self.message
        )


def _error(where: str, rule: str, message: str) -> Finding:
    return Finding("error", where, rule, message)


def _warning(where: str, rule: str, message: str) -> Finding:
    return Finding("warning", where, rule, message)


# =============================================================================
#  INDIVIDUAL CHECKS
#
#  Each returns a list of findings and takes no arguments beyond the data it
#  needs. Kept separate rather than folded into one pass so that a failing
#  check can be run alone while it is being fixed.
# =============================================================================


def _check_unique_keys() -> List[Finding]:
    """No two records may claim the same address, and no alias may shadow one.

    A duplicate here does not raise at import time in every case, and a
    silently shadowed record is unfindable rather than visibly broken, which
    is worse.
    """
    findings: List[Finding] = []

    seen_paths: Dict[str, str] = {}
    for subtype in subtypes():
        if subtype.path in seen_paths:
            findings.append(
                _error(
                    subtype.path,
                    "duplicate-path",
                    "path is already used by another record",
                )
            )
        seen_paths[subtype.path] = subtype.path

    branch_keys = {b.key for b in branches()}
    seen_alias: Dict[str, str] = {}
    for subtype in subtypes():
        for alias in subtype.aliases:
            token = alias.strip().lower()
            if token in branch_keys:
                findings.append(
                    _error(
                        subtype.path,
                        "alias-shadows-branch",
                        "alias {0!r} collides with a branch key".format(alias),
                    )
                )
            if token in seen_alias and seen_alias[token] != subtype.path:
                findings.append(
                    _warning(
                        subtype.path,
                        "alias-collision",
                        "alias {0!r} is also claimed by {1}".format(
                            alias, seen_alias[token]
                        ),
                    )
                )
            seen_alias[token] = subtype.path

    return findings


def _check_cross_references() -> List[Finding]:
    """Every `related` entry must name a record that exists.

    An edge into a branch that has not been written is a WARNING, because the
    forward-reference pattern is deliberate and there are hundreds of them. An
    edge into a written branch that names no such record is an ERROR, because
    that is a typo nothing else will catch.
    """
    from ..branches import PENDING_COLOURS

    findings: List[Finding] = []
    known = {s.path for s in subtypes()}

    for subtype in subtypes():
        for target in subtype.related:
            if target in known:
                continue
            colour = target.split(".", 1)[0]
            if colour in PENDING_COLOURS:
                findings.append(
                    _warning(
                        subtype.path,
                        "forward-reference",
                        "related {0!r} is in a branch not yet written".format(target),
                    )
                )
            else:
                findings.append(
                    _error(
                        subtype.path,
                        "broken-reference",
                        "related {0!r} names no record".format(target),
                    )
                )
    return findings


def _check_narrative() -> List[Finding]:
    """Rule 4: all five narrative fields present, summary bounded."""
    findings: List[Finding] = []
    for subtype in subtypes():
        for field in _NARRATIVE_FIELDS:
            if not getattr(subtype, field, "").strip():
                findings.append(
                    _error(subtype.path, "empty-narrative", "{0} is empty".format(field))
                )
        if len(subtype.summary) > MAX_SUMMARY_LENGTH:
            findings.append(
                _error(
                    subtype.path,
                    "summary-too-long",
                    "summary is {0} characters, the limit is {1}".format(
                        len(subtype.summary), MAX_SUMMARY_LENGTH
                    ),
                )
            )
    return findings


def _check_minimums() -> List[Finding]:
    """Rules 6, 7, 8 and 13: the countable editorial minimums."""
    findings: List[Finding] = []
    for subtype in subtypes():
        if len(subtype.applications) < MIN_APPLICATIONS:
            findings.append(
                _error(
                    subtype.path,
                    "too-few-applications",
                    "{0} applications, minimum {1}".format(
                        len(subtype.applications), MIN_APPLICATIONS
                    ),
                )
            )
        if len(subtype.challenges) < MIN_CHALLENGES:
            findings.append(
                _error(
                    subtype.path,
                    "too-few-challenges",
                    "{0} challenges, minimum {1}".format(
                        len(subtype.challenges), MIN_CHALLENGES
                    ),
                )
            )
        if len(subtype.milestones) < MIN_MILESTONES:
            findings.append(
                _error(
                    subtype.path,
                    "too-few-milestones",
                    "{0} milestones, minimum {1}".format(
                        len(subtype.milestones), MIN_MILESTONES
                    ),
                )
            )
        if not MIN_RELATED <= len(subtype.related) <= MAX_RELATED:
            findings.append(
                _error(
                    subtype.path,
                    "related-out-of-range",
                    "{0} related entries, permitted range {1} to {2}".format(
                        len(subtype.related), MIN_RELATED, MAX_RELATED
                    ),
                )
            )
    return findings


def _check_metrics() -> List[Finding]:
    """Rule 9: every metric carries a unit, an evidence grade and a string typical."""
    findings: List[Finding] = []
    for subtype in subtypes():
        for metric in subtype.metrics:
            if not metric.unit.strip():
                findings.append(
                    _error(
                        subtype.path,
                        "metric-no-unit",
                        "metric {0!r} has no unit".format(metric.name),
                    )
                )
            if not isinstance(metric.typical, str):
                findings.append(
                    _error(
                        subtype.path,
                        "metric-typical-not-string",
                        "metric {0!r} typical is {1}, not a string".format(
                            metric.name, type(metric.typical).__name__
                        ),
                    )
                )
            if metric.evidence is None:
                findings.append(
                    _error(
                        subtype.path,
                        "metric-no-evidence",
                        "metric {0!r} has no evidence grade".format(metric.name),
                    )
                )
    return findings


def _check_ascii() -> List[Finding]:
    """No non-ASCII character may appear in any field of any record.

    Checked against the assembled objects rather than against the source
    files, so it catches a character that arrives through a computed value as
    well as one typed into a literal. `tools/check_dashes.py` covers the source
    files; this covers the data.
    """
    findings: List[Finding] = []
    for subtype in subtypes():
        haystack = subtype.haystack
        if callable(haystack):  # Branch exposes this as a method, Subtype as a property
            haystack = haystack()
        offenders = sorted({c for c in haystack if ord(c) > 127})
        if offenders:
            findings.append(
                _error(
                    subtype.path,
                    "non-ascii",
                    "contains non-ASCII: {0}".format(
                        ", ".join("U+{0:04X}".format(ord(c)) for c in offenders)
                    ),
                )
            )
    return findings


def _check_sdgs() -> List[Finding]:
    """SDG numbers must be in range. There are seventeen goals."""
    findings: List[Finding] = []
    for subtype in subtypes():
        for goal in subtype.sdgs:
            if not 1 <= goal <= 17:
                findings.append(
                    _error(
                        subtype.path,
                        "sdg-out-of-range",
                        "SDG {0} does not exist; the goals are 1 to 17".format(goal),
                    )
                )
        if len(set(subtype.sdgs)) != len(subtype.sdgs):
            findings.append(
                _error(subtype.path, "sdg-duplicate", "an SDG is listed twice")
            )
    return findings


#: Plausible range for a milestone year.
#:
#: The lower bound is NEGATIVE and that is not an oversight. Years before the
#: common era are stored as negative integers, and this corpus genuinely
#: reaches back that far: `yellow.food_fermentation` records -7000 for the
#: earliest evidence of deliberate fermentation and
#: `green.molecular_plant_breeding` records -9000 for the domestication of
#: wheat. A naive `year > 0` check flagged eight legitimate records across four
#: branches as implausible, which is how this bound came to be written down.
_EARLIEST_YEAR = -12000
_LATEST_YEAR = 2100


def _check_milestone_order() -> List[Finding]:
    """A milestone year must be plausible.

    Chronological order is deliberately NOT enforced. The history facets group
    thematically and the convention is established across every merged branch,
    so a strictly ascending check would fail two thirds of the corpus for
    following its own house style.

    Nor is year zero rejected. There is no year zero in the proleptic Gregorian
    calendar, but no record uses one, and a check for a value nothing produces
    is a check that only ever fires on a false positive.
    """
    findings: List[Finding] = []
    for subtype in subtypes():
        for milestone in subtype.milestones:
            if not _EARLIEST_YEAR <= milestone.year <= _LATEST_YEAR:
                findings.append(
                    _error(
                        subtype.path,
                        "milestone-year",
                        "milestone year {0} is outside the plausible range "
                        "{1} to {2}".format(
                            milestone.year, _EARLIEST_YEAR, _LATEST_YEAR
                        ),
                    )
                )
            if not milestone.event.strip():
                findings.append(
                    _error(
                        subtype.path,
                        "milestone-empty",
                        "a milestone has no event text",
                    )
                )
    return findings


def _check_branch_consistency() -> List[Finding]:
    """A subtype must agree with the branch that contains it."""
    findings: List[Finding] = []
    for branch in branches():
        if not branch.subtypes:
            findings.append(
                _error(branch.key, "empty-branch", "branch declares no subtypes")
            )
        for subtype in branch.subtypes:
            if subtype.branch_key != branch.key:
                findings.append(
                    _error(
                        subtype.path,
                        "branch-mismatch",
                        "record sits in {0} and declares branch_key {1!r}".format(
                            branch.key, subtype.branch_key
                        ),
                    )
                )
        if not branch.colour.startswith("#") or len(branch.colour) != 7:
            findings.append(
                _error(
                    branch.key,
                    "branch-colour",
                    "colour {0!r} is not a seven-character hex triplet".format(
                        branch.colour
                    ),
                )
            )
    return findings


def _check_coverage() -> List[Finding]:
    """Report unwritten branches as warnings, never as errors.

    An unwritten branch is a known, stated, deliberate gap. It belongs in the
    report so that nobody reads a green validation as "the taxonomy is
    complete", and it must not fail the build, because it would fail every
    build until the last branch lands.
    """
    from ..branches import COLOUR_ORDER, PENDING_COLOURS

    if not PENDING_COLOURS:
        return []
    return [
        _warning(
            "taxonomy",
            "branch-pending",
            "{0} of {1} branches written; pending: {2}".format(
                len(COLOUR_ORDER) - len(PENDING_COLOURS),
                len(COLOUR_ORDER),
                ", ".join(PENDING_COLOURS),
            ),
        )
    ]


#: Every check, in the order they are run and reported. Structural problems
#: come before editorial ones so that a broken dataset reports the breakage
#: first rather than burying it under style findings.
_CHECKS: Sequence[Tuple[str, Callable[[], List[Finding]]]] = (
    ("unique-keys", _check_unique_keys),
    ("branch-consistency", _check_branch_consistency),
    ("cross-references", _check_cross_references),
    ("narrative", _check_narrative),
    ("minimums", _check_minimums),
    ("metrics", _check_metrics),
    ("sdgs", _check_sdgs),
    ("milestones", _check_milestone_order),
    ("ascii", _check_ascii),
    ("coverage", _check_coverage),
)


# =============================================================================
#  REGISTRY COVERAGE
#
#  Reported rather than enforced while the registries are unwritten. See the
#  module header for why an empty registry must not produce two thousand
#  failures.
# =============================================================================


def registry_coverage() -> Dict[str, Dict[str, int]]:
    """How many referenced keys each registry actually resolves.

    Returns a mapping of registry name to `{"referenced": n, "resolved": m}`.
    A registry that is not importable reports `resolved` as 0, which is the
    honest answer rather than an exception.
    """
    referenced: Dict[str, Set[str]] = {
        "organisms": set(),
        "techniques": set(),
        "glossary": set(),
        "refs": set(),
        "formulas": set(),
    }
    for subtype in subtypes():
        referenced["organisms"].update(subtype.organisms)
        referenced["techniques"].update(subtype.techniques)
        referenced["glossary"].update(subtype.glossary)
        referenced["refs"].update(subtype.references)
        referenced["formulas"].update(subtype.formulas)

    out: Dict[str, Dict[str, int]] = {}
    for name, keys in referenced.items():
        out[name] = {
            "referenced": len(keys),
            "resolved": len(_resolvable(name, keys)),
        }
    return out


def _resolvable(registry: str, keys: Iterable[str]) -> Set[str]:
    """Keys the named registry can resolve. Empty if it is not written yet."""
    try:
        module = __import__(
            "biotechnology.{0}".format(registry), fromlist=["keys"]
        )
    except Exception:
        return set()
    known = getattr(module, "KEYS", None)
    if known is None:
        getter = getattr(module, "keys", None)
        known = set(getter()) if callable(getter) else set()
    return {k for k in keys if k in set(known)}


# =============================================================================
#  THE PUBLIC ENTRY POINTS
# =============================================================================


def check(*, strict: bool = False) -> List[Finding]:
    """Run every check and return the findings, worst first.

    Does not raise. Use this when you want to inspect, group or format the
    results yourself.
    """
    findings: List[Finding] = []
    for _name, fn in _CHECKS:
        findings.extend(fn())

    if strict:
        findings = [
            Finding("error", f.where, f.rule, f.message) if not f.is_error else f
            for f in findings
        ]

    findings.sort(key=lambda f: (0 if f.is_error else 1, f.where, f.rule))
    return findings


def validate(*, strict: bool = False, raise_on_error: bool = True) -> List[Finding]:
    """Validate the dataset.

    Parameters
    ----------
    strict:
        Promote warnings to errors. Intended for the release workflow once the
        taxonomy is complete, and not before: with four branches unwritten,
        strict mode fails on hundreds of deliberate forward references.
    raise_on_error:
        Raise `ValidationError` when anything failed. Set False to collect the
        findings without an exception, which is what the CLI does so it can
        print all of them rather than the first.

    Returns
    -------
    The findings, worst first. Empty means the dataset is consistent.

    Raises
    ------
    ValidationError
        When `raise_on_error` is True and at least one error was found. The
        message names the counts; the findings carry the detail.
    """
    findings = check(strict=strict)
    errors = [f for f in findings if f.is_error]

    if errors and raise_on_error:
        raise ValidationError(
            "{0} error(s) and {1} warning(s) in {2} record(s)".format(
                len(errors), len(findings) - len(errors), len(subtypes())
            )
        )
    return findings
