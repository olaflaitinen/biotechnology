"""Lookup, search and export functions over the branch registry."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from .data import ALL_BRANCHES
from .models import Branch, Subtype

__all__ = [
    "branches",
    "branch",
    "subtypes",
    "get",
    "resolve",
    "search",
    "by_sdg",
    "related",
    "keys",
    "tree",
    "to_dict",
    "to_json",
]

Node = Union[Branch, Subtype]

_BY_KEY: Dict[str, Branch] = {}
for _b in ALL_BRANCHES:
    _BY_KEY[_b.key] = _b
    for _alias in _b.aliases:
        _BY_KEY.setdefault(_alias, _b)
del _b

_BY_PATH: Dict[str, Subtype] = {
    s.path: s for b in ALL_BRANCHES for s in b.subtypes
}


class UnknownNodeError(KeyError):
    """Raised when a branch or subtype cannot be resolved."""


# ---------------------------------------------------------------------------
# listing
# ---------------------------------------------------------------------------
def branches() -> Tuple[Branch, ...]:
    """Every branch, in colour-wheel order."""
    return ALL_BRANCHES


def keys() -> Tuple[str, ...]:
    """Canonical keys of every branch."""
    return tuple(b.key for b in ALL_BRANCHES)


def subtypes(branch_key: Optional[str] = None) -> Tuple[Subtype, ...]:
    """Every subtype, or only those of ``branch_key`` when given."""
    if branch_key is None:
        return tuple(s for b in ALL_BRANCHES for s in b.subtypes)
    return branch(branch_key).subtypes


# ---------------------------------------------------------------------------
# lookup
# ---------------------------------------------------------------------------
def branch(key: str) -> Branch:
    """Resolve a branch by key or alias, e.g. ``"red"`` or ``"industrial"``."""
    try:
        return _BY_KEY[key.strip().lower()]
    except KeyError:
        raise UnknownNodeError(
            f"unknown branch {key!r}; known branches: {', '.join(keys())}"
        ) from None


def get(path: str) -> Node:
    """Resolve a dotted path to a :class:`Branch` or :class:`Subtype`.

    ``get("red")`` returns a branch, ``get("red.gene_therapy")`` a subtype.
    Branch aliases work in both positions, so ``get("medical.gene_therapy")``
    resolves too.
    """
    cleaned = path.strip().lower()
    if not cleaned:
        raise UnknownNodeError("empty path")
    head, _, tail = cleaned.partition(".")
    node = branch(head)
    if not tail:
        return node
    if tail in node:
        return node[tail]
    raise UnknownNodeError(
        f"unknown subtype {tail!r} in branch {node.key!r}; "
        f"available: {', '.join(node.keys())}"
    )


def resolve(path: str, default: Any = None) -> Any:
    """Like :func:`get`, but returns ``default`` instead of raising."""
    try:
        return get(path)
    except UnknownNodeError:
        return default


def related(path: str) -> List[Subtype]:
    """Subtypes cross-referenced from the node at ``path``."""
    node = get(path)
    if isinstance(node, Branch):
        seen: Dict[str, Subtype] = {}
        for sub in node.subtypes:
            for ref in sub.related:
                target = _BY_PATH.get(ref)
                if target is not None and target.branch_key != node.key:
                    seen[target.path] = target
        return list(seen.values())
    return [_BY_PATH[ref] for ref in node.related if ref in _BY_PATH]


# ---------------------------------------------------------------------------
# search
# ---------------------------------------------------------------------------
def _score(needle: str, node: Node) -> int:
    """Higher is a better match; ``0`` means no match."""
    name = node.name.lower()
    key = node.key.lower()
    if needle == key or needle == name:
        return 100
    if needle in key:
        return 80
    if needle in name:
        return 70
    if isinstance(node, Subtype):
        if any(needle in item.lower() for item in node.technologies):
            return 50
        if any(needle in item.lower() for item in node.applications):
            return 45
    return 30 if needle in node.haystack() else 0


def search(
    query: str,
    *,
    branch_key: Optional[str] = None,
    include_branches: bool = False,
    limit: Optional[int] = None,
) -> List[Node]:
    """Free-text search over the taxonomy, best matches first.

    Every text field is searched: names, keys, descriptions, applications and
    technologies. Pass ``branch_key`` to restrict the search to one branch and
    ``include_branches=True`` to let branches themselves appear in the results.
    """
    needle = query.strip().lower()
    if not needle:
        return []

    pool: List[Node] = []
    if include_branches:
        pool.extend(
            [branch(branch_key)] if branch_key else list(ALL_BRANCHES)
        )
    pool.extend(subtypes(branch_key))

    hits = [(node, _score(needle, node)) for node in pool]
    hits = [(node, score) for node, score in hits if score]
    hits.sort(key=lambda pair: (-pair[1], pair[0].name))
    results = [node for node, _ in hits]
    return results[:limit] if limit else results


def by_sdg(goal: int) -> List[Subtype]:
    """Subtypes tagged with a UN Sustainable Development Goal number."""
    return [s for s in subtypes() if goal in s.sdgs]


# ---------------------------------------------------------------------------
# rendering and export
# ---------------------------------------------------------------------------
def tree(branch_keys: Optional[Sequence[str]] = None) -> str:
    """An indented text tree of the taxonomy, ready to print."""
    selected = (
        [branch(k) for k in branch_keys] if branch_keys else list(ALL_BRANCHES)
    )
    lines: List[str] = []
    for b in selected:
        lines.append(f"{b.name}  [{b.key}]  {b.colour}")
        for i, sub in enumerate(b.subtypes):
            connector = "`--" if i == len(b.subtypes) - 1 else "|--"
            lines.append(f"  {connector} {sub.key} -  {sub.name}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def to_dict(*, include_subtypes: bool = True) -> Dict[str, Any]:
    """The whole taxonomy as plain Python data."""
    return {
        "branches": [
            b.to_dict(include_subtypes=include_subtypes) for b in ALL_BRANCHES
        ],
        "branch_count": len(ALL_BRANCHES),
        "subtype_count": len(subtypes()),
    }


def to_json(*, indent: int = 2, include_subtypes: bool = True) -> str:
    """The whole taxonomy as a JSON string."""
    return json.dumps(
        to_dict(include_subtypes=include_subtypes),
        indent=indent,
        ensure_ascii=False,
    )
