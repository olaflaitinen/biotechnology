# =============================================================================
#  biotechnology.core.search
# -----------------------------------------------------------------------------
#  Ranked free-text search across the taxonomy.
#
#  WHAT THIS IS NOT
#  It is not an index, not an inverted file, and not a relevance model. It is a
#  linear scan with a scoring function, and that is a deliberate choice rather
#  than a first draft:
#
#      THE CORPUS IS EIGHTY-FIVE RECORDS. A FULL SCAN COSTS UNDER A
#      MILLISECOND, AND AN INDEX WOULD COST A CACHE THAT CAN GO STALE.
#
#  Building an inverted index over a few hundred kilobytes of frozen literals
#  would add a second copy of the data, a build step, an invalidation problem
#  and a dependency argument, in exchange for a saving nobody can perceive.
#  When the taxonomy reaches a size where that trade changes, this module is
#  the one file that has to change.
#
#  THE SCORING MODEL, AND WHY IT IS SHAPED THIS WAY
#  A user searching this library is almost always looking for a RECORD they
#  half-remember rather than for every mention of a word. So the score is
#  dominated by where the match occurs rather than by how often:
#
#      exact key or path match        the user typed an address; nothing else
#                                     can outrank it
#      exact alias match              they typed a name the field actually uses
#      name contains the query        they typed most of a title
#      summary contains the query     the one-line description matches
#      body contains the query        it is mentioned somewhere
#
#  Frequency is used only to break ties inside the last band, and it is capped.
#  Without a cap, a long record beats a short one for no better reason than
#  length, which is exactly the wrong answer when the short record is the one
#  actually about the subject.
#
#  MATCHING IS SUBSTRING, NOT TOKEN
#  "ferment" finds `food_fermentation`, `precision_fermentation` and
#  `microbial_fermentation`. Token matching would find none of them, because
#  the corpus is full of compound keys and Latin binomials where the useful
#  prefix is not a word. Substring matching costs precision on short queries,
#  which is why queries under two characters are rejected rather than answered
#  badly.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Iterable, List, Optional, Sequence, Tuple

from .enums import Domain, Maturity, RiskTier, Scale
from .models import Branch, Node, Subtype
from .registry import branches, subtypes

__all__ = ["search", "search_scored", "MIN_QUERY_LENGTH"]


# =============================================================================
#  TUNING CONSTANTS
#
#  Named rather than inlined so that the ranking can be reasoned about and
#  changed in one place. The absolute values do not matter; the ORDER of
#  magnitude between bands does, because that is what guarantees a key match
#  always outranks a body match no matter how many times the body mentions it.
# =============================================================================

#: Below this, a substring query matches too much to be useful. Two characters
#: against this corpus returns most of it, which is not an answer.
MIN_QUERY_LENGTH = 2

_SCORE_EXACT_PATH = 1000
_SCORE_EXACT_KEY = 900
_SCORE_EXACT_ALIAS = 800
_SCORE_KEY_PREFIX = 400
_SCORE_NAME_EXACT = 350
_SCORE_NAME_CONTAINS = 200
_SCORE_ALIAS_CONTAINS = 150
_SCORE_SUMMARY_CONTAINS = 100
_SCORE_BODY_CONTAINS = 20

#: Ceiling on the frequency bonus. Three occurrences and thirty occurrences
#: mean much the same thing, and without a cap a long record wins on length.
_MAX_FREQUENCY_BONUS = 15


# =============================================================================
#  SCORING ONE RECORD
# =============================================================================


def _score(node: Node, query: str) -> int:
    """Score one record against a lower-cased query. Zero means no match."""
    key = node.key.lower()
    name = node.name.lower()
    aliases = tuple(a.lower() for a in node.aliases)

    path = node.path.lower() if isinstance(node, Subtype) else key

    # -- addressed directly ---------------------------------------------------
    if query == path:
        return _SCORE_EXACT_PATH
    if query == key:
        return _SCORE_EXACT_KEY
    if query in aliases:
        return _SCORE_EXACT_ALIAS

    score = 0

    # -- partially addressed --------------------------------------------------
    if key.startswith(query):
        score += _SCORE_KEY_PREFIX
    elif query in key:
        score += _SCORE_KEY_PREFIX // 2

    # -- named ----------------------------------------------------------------
    if name == query:
        score += _SCORE_NAME_EXACT
    elif query in name:
        score += _SCORE_NAME_CONTAINS

    if any(query in alias for alias in aliases):
        score += _SCORE_ALIAS_CONTAINS

    # -- described ------------------------------------------------------------
    if query in node.summary.lower():
        score += _SCORE_SUMMARY_CONTAINS

    # -- mentioned ------------------------------------------------------------
    #  `haystack` is a property on Subtype and a method on Branch. Rather than
    #  special-case the two record types here, or change a public API on the
    #  models to suit one caller, the value is normalised at the point of use.
    haystack = node.haystack
    if callable(haystack):
        haystack = haystack()
    occurrences = haystack.count(query)
    if occurrences:
        score += _SCORE_BODY_CONTAINS
        score += min(occurrences, _MAX_FREQUENCY_BONUS)

    return score


# =============================================================================
#  THE PUBLIC ENTRY POINTS
# =============================================================================


def search_scored(
    query: str,
    *,
    limit: Optional[int] = None,
    include_branches: bool = True,
    maturity: Optional[Maturity] = None,
    risk_tier: Optional[RiskTier] = None,
    scale: Optional[Scale] = None,
    domain: Optional[Domain] = None,
    branch: Optional[str] = None,
) -> List[Tuple[Node, int]]:
    """Search and return `(record, score)` pairs, best first.

    Parameters
    ----------
    query:
        Free text. Case-insensitive, matched as a substring. A query shorter
        than `MIN_QUERY_LENGTH` returns nothing rather than returning most of
        the corpus.
    limit:
        Truncate the result. None returns everything that matched.
    include_branches:
        Whether branch records may appear alongside subtypes. Default True,
        because a user searching "marine" plausibly wants the blue branch.
    maturity, risk_tier, scale, domain, branch:
        Optional filters, applied to subtypes only. A branch has no maturity,
        so passing one of these with `include_branches=True` filters the
        subtypes and leaves the branches, which is the useful behaviour rather
        than the consistent one.

    Notes
    -----
    Ties are broken by path, so the ordering is total and the output is
    reproducible. Without that, two records with identical scores could swap
    places between runs and produce a diff in generated documentation.
    """
    text = query.strip().lower()
    if len(text) < MIN_QUERY_LENGTH:
        return []

    candidates: List[Node] = []
    if include_branches:
        candidates.extend(branches())
    candidates.extend(_filtered_subtypes(maturity, risk_tier, scale, domain, branch))

    scored: List[Tuple[Node, int]] = []
    for node in candidates:
        value = _score(node, text)
        if value > 0:
            scored.append((node, value))

    scored.sort(key=lambda pair: (-pair[1], _sort_key(pair[0])))

    return scored[:limit] if limit is not None else scored


def search(
    query: str,
    *,
    limit: Optional[int] = None,
    include_branches: bool = True,
    maturity: Optional[Maturity] = None,
    risk_tier: Optional[RiskTier] = None,
    scale: Optional[Scale] = None,
    domain: Optional[Domain] = None,
    branch: Optional[str] = None,
) -> List[Node]:
    """Search and return records, best first.

    The scoreless form, which is what almost every caller wants. Use
    `search_scored` when you need to show relevance or set a threshold.
    """
    return [
        node
        for node, _ in search_scored(
            query,
            limit=limit,
            include_branches=include_branches,
            maturity=maturity,
            risk_tier=risk_tier,
            scale=scale,
            domain=domain,
            branch=branch,
        )
    ]


# =============================================================================
#  FILTERING AND ORDERING HELPERS
# =============================================================================


def _filtered_subtypes(
    maturity: Optional[Maturity],
    risk_tier: Optional[RiskTier],
    scale: Optional[Scale],
    domain: Optional[Domain],
    branch: Optional[str],
) -> List[Subtype]:
    rows: Iterable[Subtype] = subtypes()
    if branch is not None:
        wanted = branch.strip().lower()
        rows = [s for s in rows if s.branch_key == wanted]
    if maturity is not None:
        rows = [s for s in rows if s.maturity is maturity]
    if risk_tier is not None:
        rows = [s for s in rows if s.risk_tier is risk_tier]
    if scale is not None:
        rows = [s for s in rows if s.scale is scale]
    if domain is not None:
        rows = [s for s in rows if domain in s.domains]
    return list(rows)


def _sort_key(node: Node) -> str:
    """Stable tie-breaker.

    Branches sort under their own key and subtypes under their dotted path, so
    a branch and its first subtype never compare equal.
    """
    return node.path if isinstance(node, Subtype) else node.key
