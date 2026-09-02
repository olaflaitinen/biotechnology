# =============================================================================
#  biotechnology.core.registry
# -----------------------------------------------------------------------------
#  The single source of truth for "what exists and where is it".
#
#  This module builds three flat indexes over the ten branch packages once, at
#  import time, and then answers every lookup from them in constant time:
#
#      _BRANCH_INDEX   key or alias      -> Branch
#      _SUBTYPE_INDEX  "branch.subtype"  -> Subtype
#      _ALIAS_INDEX    subtype alias     -> Subtype
#
#  WHY BUILD EAGERLY?
#  The whole taxonomy is a few hundred kilobytes of literals. Building the
#  indexes costs a few milliseconds and buys three things: alias collisions
#  are detected the moment the package is imported rather than at the moment
#  an unlucky user hits one; every lookup afterwards is a dict hit; and the
#  objects are immutable, so the indexes can never drift out of date.
#
#  ALIAS PRECEDENCE
#  A canonical key always beats an alias. If a future branch were to declare
#  the alias "gold" while a branch already owns the key "gold", the canonical
#  owner keeps it and the alias is dropped rather than silently shadowing.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple, Union

from .enums import Domain, Maturity, RiskTier, Scale
from .errors import UnknownBranchError, UnknownNodeError, UnknownSubtypeError
from .models import Branch, Milestone, Node, Subtype
from .paths import parse_path

__all__ = [
    "branches",
    "branch_keys",
    "get_branch",
    "get_subtype",
    "get",
    "resolve",
    "subtypes",
    "subtype_paths",
    "exists",
    "related_to",
    "by_sdg",
    "by_domain",
    "by_maturity",
    "by_risk_tier",
    "by_scale",
    "timeline",
    "counts",
    "iter_nodes",
]


# =============================================================================
#  Index construction
# =============================================================================
def _load_branches() -> Tuple[Branch, ...]:
    """Import the branch packages and return them in colour-wheel order.

    Imported inside a function rather than at module scope to keep the import
    graph acyclic: ``core.models`` needs ``core.registry.get_branch`` for its
    ``Subtype.branch`` property, and the branch packages need ``core.models``.
    """
    from ..branches import ALL_BRANCHES

    return ALL_BRANCHES


_BRANCHES: Tuple[Branch, ...] = _load_branches()

# -- key/alias -> Branch ------------------------------------------------------
_BRANCH_INDEX: Dict[str, Branch] = {}
for _b in _BRANCHES:
    _BRANCH_INDEX[_b.key] = _b
for _b in _BRANCHES:  # second pass so canonical keys always win
    for _alias in _b.aliases:
        _BRANCH_INDEX.setdefault(_alias, _b)

# -- "branch.subtype" -> Subtype ---------------------------------------------
_SUBTYPE_INDEX: Dict[str, Subtype] = {
    s.path: s for _b in _BRANCHES for s in _b.subtypes
}

# -- subtype alias -> Subtype -------------------------------------------------
#  Aliases are convenience only. A collision between two branches' aliases is
#  resolved first-come, and the validation suite reports it as a warning.
_ALIAS_INDEX: Dict[str, Subtype] = {}
for _b in _BRANCHES:
    for _s in _b.subtypes:
        for _alias in _s.aliases:
            _ALIAS_INDEX.setdefault(_alias.strip().lower(), _s)

del _b, _s, _alias  # keep the module namespace clean


# =============================================================================
#  Listing
# =============================================================================
def branches() -> Tuple[Branch, ...]:
    """Every branch, in the conventional colour-wheel order.

    >>> [b.key for b in branches()][:3]
    ['red', 'green', 'white']
    """
    return _BRANCHES


def branch_keys() -> Tuple[str, ...]:
    """Canonical keys of every branch, in order."""
    return tuple(b.key for b in _BRANCHES)


def subtypes(branch_key: Optional[str] = None) -> Tuple[Subtype, ...]:
    """Every subtype, or only those belonging to ``branch_key``.

    >>> len(subtypes("red"))
    8
    """
    if branch_key is None:
        return tuple(s for b in _BRANCHES for s in b.subtypes)
    return get_branch(branch_key).subtypes


def subtype_paths(branch_key: Optional[str] = None) -> Tuple[str, ...]:
    """Dotted paths of every subtype, optionally restricted to one branch."""
    return tuple(s.path for s in subtypes(branch_key))


def iter_nodes() -> Iterator[Node]:
    """Yield every branch followed by its subtypes, depth-first."""
    for b in _BRANCHES:
        yield b
        for s in b.subtypes:
            yield s


# =============================================================================
#  Lookup
# =============================================================================
def get_branch(key: str) -> Branch:
    """Resolve a branch by canonical key or alias.

    >>> get_branch("industrial").key
    'white'
    >>> get_branch("GRAY").key
    'grey'
    """
    token = str(key).strip().lower().replace("-", "_").replace(" ", "_")
    try:
        return _BRANCH_INDEX[token]
    except KeyError:
        raise UnknownBranchError(key, branch_keys()) from None


def get_subtype(path: str) -> Subtype:
    """Resolve a subtype from a full dotted path, or from a bare alias.

    >>> get_subtype("red.gene_therapy").name
    'Gene Therapy'
    """
    token = str(path).strip().lower()
    if "." not in token and token in _ALIAS_INDEX:
        return _ALIAS_INDEX[token]

    parsed = parse_path(path)
    if parsed.is_branch:
        raise UnknownSubtypeError(
            parsed.branch,
            _ALIAS_INDEX and sorted(_ALIAS_INDEX) or [],
            message=(
                f"{parsed.normalised!r} names a branch, not a subtype; "
                f"use get() if either is acceptable"
            ),
        )

    branch_obj = get_branch(parsed.branch)
    return branch_obj[parsed.subtype]  # raises UnknownSubtypeError with candidates


def get(path: str) -> Node:
    """Resolve a dotted path to a :class:`Branch` or a :class:`Subtype`.

    This is the workhorse of the public API. It accepts:

    * a branch key             ``"red"``
    * a branch alias           ``"medical"``
    * a full subtype path      ``"red.gene_therapy"``
    * an aliased branch head   ``"medical.gene_therapy"``

    >>> get("white").key
    'white'
    >>> get("medical.gene_therapy").path
    'red.gene_therapy'
    """
    parsed = parse_path(path)
    branch_obj = get_branch(parsed.branch)
    if parsed.is_branch:
        return branch_obj
    subtype = branch_obj.get(parsed.subtype)
    if subtype is None:
        raise UnknownSubtypeError(
            parsed.subtype, branch_obj.keys(), branch_key=branch_obj.key
        )
    return subtype


def resolve(path: str, default: object = None) -> object:
    """Non-raising :func:`get`.

    Returns ``default`` for anything that does not resolve, including
    malformed input, which makes it safe to call on untrusted strings.

    >>> resolve("nope") is None
    True
    >>> resolve("!!!", default="fallback")
    'fallback'
    """
    try:
        return get(path)
    except Exception:  # noqa: BLE001 - deliberately total
        return default


def exists(path: str) -> bool:
    """True when ``path`` resolves to anything at all."""
    return resolve(path) is not None


# =============================================================================
#  Graph traversal
# =============================================================================
def related_to(path: str, *, depth: int = 1) -> List[Subtype]:
    """Subtypes reachable from ``path`` through ``related`` cross-references.

    Parameters
    ----------
    path:
        A branch or subtype address. For a branch, the union of its subtypes'
        outward references is returned, excluding the branch's own subtypes.
    depth:
        How many hops to follow. ``depth=1`` gives direct neighbours;
        ``depth=2`` also gives their neighbours, and so on. The starting node
        is never included in the result.

    >>> [s.key for s in related_to("red.gene_therapy")]
    ['bioethics', 'computational_drug_discovery']
    """
    if depth < 1:
        return []

    node = get(path)
    frontier: List[Subtype]
    origin_paths = set()

    if isinstance(node, Branch):
        frontier = list(node.subtypes)
        origin_paths = set(node.paths())
    else:
        frontier = [node]
        origin_paths = {node.path}

    collected: Dict[str, Subtype] = {}
    for _ in range(depth):
        nxt: List[Subtype] = []
        for current in frontier:
            for ref in current.related:
                target = _SUBTYPE_INDEX.get(ref)
                if target is None or target.path in origin_paths:
                    continue
                if target.path not in collected:
                    collected[target.path] = target
                    nxt.append(target)
        frontier = nxt
        if not frontier:
            break
    return list(collected.values())


def timeline(
    path: Optional[str] = None, *, since: Optional[int] = None
) -> List[Tuple[int, str, str]]:
    """A chronological list of ``(year, event, source_path)`` triples.

    With no argument, the whole taxonomy's history is merged into one
    timeline - which is, on its own, a readable one-page history of applied
    biology.
    """
    rows: List[Tuple[int, str, str]] = []

    def _collect(subtype: Subtype) -> None:
        for m in subtype.milestones:
            rows.append((m.year, m.event, subtype.path))

    if path is None:
        for b in _BRANCHES:
            for m in b.milestones:
                rows.append((m.year, m.event, b.key))
            for s in b.subtypes:
                _collect(s)
    else:
        node = get(path)
        if isinstance(node, Branch):
            for m in node.milestones:
                rows.append((m.year, m.event, node.key))
            for s in node.subtypes:
                _collect(s)
        else:
            _collect(node)

    if since is not None:
        rows = [r for r in rows if r[0] >= since]
    return sorted(rows)


# =============================================================================
#  Filters
# =============================================================================
def by_sdg(goal: int) -> List[Subtype]:
    """Subtypes tagged with a UN Sustainable Development Goal number (1-17)."""
    if not isinstance(goal, int) or not 1 <= goal <= 17:
        raise ValueError(f"SDG number must be an integer 1-17, got {goal!r}")
    return [s for s in subtypes() if goal in s.sdgs]


def by_domain(domain: Union[Domain, str]) -> List[Subtype]:
    """Subtypes serving a given cross-cutting sector."""
    want = domain if isinstance(domain, Domain) else Domain.parse(domain)
    return [s for s in subtypes() if want in s.domains]


def by_maturity(maturity: Union[Maturity, str]) -> List[Subtype]:
    """Subtypes at a given technology-readiness band."""
    want = maturity if isinstance(maturity, Maturity) else Maturity.parse(maturity)
    return [s for s in subtypes() if s.maturity is want]


def by_risk_tier(tier: Union[RiskTier, str]) -> List[Subtype]:
    """Subtypes attracting a given level of governance."""
    want = tier if isinstance(tier, RiskTier) else RiskTier.parse(tier)
    return [s for s in subtypes() if s.risk_tier is want]


def by_scale(scale: Union[Scale, str]) -> List[Subtype]:
    """Subtypes normally practised at a given physical scale."""
    want = scale if isinstance(scale, Scale) else Scale.parse(scale)
    return [s for s in subtypes() if s.scale is want]


# =============================================================================
#  Summary statistics
# =============================================================================
def counts() -> Dict[str, object]:
    """Headline numbers about the taxonomy, used by the CLI and the README."""
    all_subtypes = subtypes()
    return {
        "branches": len(_BRANCHES),
        "subtypes": len(all_subtypes),
        "per_branch": {b.key: len(b) for b in _BRANCHES},
        "metrics": sum(len(s.metrics) for s in all_subtypes),
        "milestones": sum(len(s.milestones) for s in all_subtypes)
        + sum(len(b.milestones) for b in _BRANCHES),
        "applications": sum(len(s.applications) for s in all_subtypes),
        "technologies": sum(len(s.technologies) for s in all_subtypes),
        "cross_references": sum(len(s.related) for s in all_subtypes),
        "distinct_sdgs": sorted({g for s in all_subtypes for g in s.sdgs}),
    }
