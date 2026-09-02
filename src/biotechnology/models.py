"""Core data model for the biotechnology taxonomy.

The taxonomy has two levels:

``Branch``
    One of the ten colour-coded fields of biotechnology (red, green, white,
    blue, yellow, grey, brown, gold, dark, purple).

``Subtype``
    A named sub-discipline that belongs to exactly one branch, addressed by a
    dotted path such as ``"red.gene_therapy"``.

Both objects are frozen dataclasses, so they are hashable and safe to share.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterator, List, Optional, Sequence, Tuple

__all__ = ["Subtype", "Branch"]


def _tuple(value: Optional[Sequence[str]]) -> Tuple[str, ...]:
    return tuple(value) if value else ()


@dataclass(frozen=True)
class Subtype:
    """A sub-discipline inside a colour branch of biotechnology."""

    key: str
    name: str
    description: str
    applications: Tuple[str, ...] = ()
    technologies: Tuple[str, ...] = ()
    sdgs: Tuple[int, ...] = ()
    related: Tuple[str, ...] = ()
    branch_key: str = ""

    # -- identity -----------------------------------------------------------
    @property
    def path(self) -> str:
        """Dotted address of the subtype, e.g. ``"red.gene_therapy"``."""
        return f"{self.branch_key}.{self.key}" if self.branch_key else self.key

    @property
    def branch(self) -> "Branch":
        """The :class:`Branch` this subtype belongs to."""
        from .registry import branch as _branch

        return _branch(self.branch_key)

    # -- search -------------------------------------------------------------
    def haystack(self) -> str:
        """Lower-cased blob of every searchable field."""
        parts = [self.key, self.name, self.description, self.branch_key]
        parts.extend(self.applications)
        parts.extend(self.technologies)
        return " ".join(parts).lower()

    # -- export -------------------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "key": self.key,
            "name": self.name,
            "branch": self.branch_key,
            "description": self.description,
            "applications": list(self.applications),
            "technologies": list(self.technologies),
            "sdgs": list(self.sdgs),
            "related": list(self.related),
        }

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return self.name

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Subtype({self.path!r})"


@dataclass(frozen=True)
class Branch:
    """One of the ten colour-coded branches of biotechnology."""

    key: str
    name: str
    colour: str
    summary: str
    description: str
    subtypes: Tuple[Subtype, ...] = ()
    aliases: Tuple[str, ...] = ()
    sdgs: Tuple[int, ...] = ()
    _index: Dict[str, Subtype] = field(
        default_factory=dict, repr=False, compare=False
    )

    # -- construction -------------------------------------------------------
    @classmethod
    def build(
        cls,
        key: str,
        name: str,
        colour: str,
        summary: str,
        description: str,
        subtypes: Sequence[Subtype],
        aliases: Sequence[str] = (),
        sdgs: Sequence[int] = (),
    ) -> "Branch":
        """Create a branch, stamping ``branch_key`` onto each subtype."""
        bound = tuple(
            Subtype(
                key=s.key,
                name=s.name,
                description=s.description,
                applications=_tuple(s.applications),
                technologies=_tuple(s.technologies),
                sdgs=tuple(s.sdgs),
                related=_tuple(s.related),
                branch_key=key,
            )
            for s in subtypes
        )
        seen = [s.key for s in bound]
        duplicates = {k for k in seen if seen.count(k) > 1}
        if duplicates:
            raise ValueError(
                f"duplicate subtype keys in branch {key!r}: {sorted(duplicates)}"
            )
        return cls(
            key=key,
            name=name,
            colour=colour,
            summary=summary,
            description=description,
            subtypes=bound,
            aliases=tuple(aliases),
            sdgs=tuple(sdgs),
            _index={s.key: s for s in bound},
        )

    # -- alias of the British spelling --------------------------------------
    @property
    def color(self) -> str:
        """US spelling alias for :attr:`colour`."""
        return self.colour

    # -- container protocol -------------------------------------------------
    def __iter__(self) -> Iterator[Subtype]:
        return iter(self.subtypes)

    def __len__(self) -> int:
        return len(self.subtypes)

    def __contains__(self, key: object) -> bool:
        if isinstance(key, Subtype):
            return key.branch_key == self.key and key.key in self._index
        return isinstance(key, str) and key.lower() in self._index

    def __getitem__(self, key: str) -> Subtype:
        try:
            return self._index[key.lower()]
        except KeyError:
            raise KeyError(
                f"{self.key!r} has no subtype {key!r}; "
                f"available: {', '.join(self.keys())}"
            ) from None

    def get(self, key: str, default: Optional[Subtype] = None) -> Optional[Subtype]:
        """Return a subtype by key, or ``default`` when it does not exist."""
        return self._index.get(key.lower(), default)

    def keys(self) -> Tuple[str, ...]:
        """Keys of every subtype in declaration order."""
        return tuple(s.key for s in self.subtypes)

    def names(self) -> Tuple[str, ...]:
        """Human-readable names of every subtype."""
        return tuple(s.name for s in self.subtypes)

    # -- search -------------------------------------------------------------
    def search(self, query: str) -> List[Subtype]:
        """Subtypes of this branch whose text matches ``query``."""
        needle = query.strip().lower()
        if not needle:
            return []
        return [s for s in self.subtypes if needle in s.haystack()]

    def haystack(self) -> str:
        """Lower-cased blob of every searchable field."""
        return " ".join(
            [self.key, self.name, self.summary, self.description, *self.aliases]
        ).lower()

    # -- export -------------------------------------------------------------
    def to_dict(self, *, include_subtypes: bool = True) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            "key": self.key,
            "name": self.name,
            "colour": self.colour,
            "summary": self.summary,
            "description": self.description,
            "aliases": list(self.aliases),
            "sdgs": list(self.sdgs),
        }
        if include_subtypes:
            data["subtypes"] = [s.to_dict() for s in self.subtypes]
        return data

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return self.name

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Branch({self.key!r}, subtypes={len(self.subtypes)})"
