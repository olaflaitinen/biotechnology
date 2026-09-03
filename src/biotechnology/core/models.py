# =============================================================================
#  biotechnology.core.models
# -----------------------------------------------------------------------------
#  The record types that make up the taxonomy.
#
#  THE SHAPE OF THE DATA
#  ---------------------
#      Branch                      one of the ten colours
#        +-- Subtype               a sub-discipline inside that colour
#              +-- Metric          a measurable quantity used in that field
#              +-- Milestone       a dated event in its history
#
#  Everything is a frozen dataclass. Frozen means immutable, which in turn
#  means hashable, thread-safe and impossible to corrupt by accident: a user
#  who writes `bt.RED.name = "..."` gets an exception rather than a silently
#  broken global. The whole taxonomy is built once at import time and then
#  never changes.
#
#  TWO AUDIENCES, ONE RECORD
#  -------------------------
#  Every Subtype carries both a technical `description` and a
#  `plain_language` field written for a reader with no scientific training,
#  plus an everyday `analogy`. A single record therefore serves a researcher
#  writing a grant proposal and a journalist writing a news story, without
#  either having to read the other's version.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from dataclasses import dataclass, field
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from .enums import Domain, EvidenceLevel, Maturity, RegulatoryStatus, RiskTier, Scale
from .errors import SchemaError, UnknownSubtypeError

__all__ = [
    "Metric",
    "Milestone",
    "Subtype",
    "Branch",
    "Node",
]


# =============================================================================
#  Small value objects
# =============================================================================
@dataclass(frozen=True)
class Metric:
    """A quantity that practitioners in a subtype actually measure.

    Metrics are what connect the descriptive half of this library to the
    computational half. A metric names a symbol (``mu``), a unit (``1/h``) and
    a typical range, and may point at the formula module that computes it, so
    that ``bt.get("white.microbial_fermentation").metrics`` leads directly to
    ``bt.formulas.get("specific_growth_rate")``.

    Attributes
    ----------
    name:
        Full human name, e.g. ``"Specific growth rate"``.
    symbol:
        The symbol used in the literature, written in ASCII so that it renders
        in a terminal, a CSV file and a LaTeX document alike (``"mu"`` rather
        than the Greek letter).
    unit:
        SI or field-conventional unit as a plain string, ``"-"`` when the
        quantity is dimensionless.
    typical:
        A representative range as free text, because real ranges are
        organism- and process-dependent and a single number would mislead.
    formula:
        Optional key into :mod:`biotechnology.formulas`.
    evidence:
        How solid the typical range is; see :class:`~.enums.EvidenceLevel`.
    note:
        Optional caveat, e.g. what changes the value.
    """

    name: str
    symbol: str
    unit: str
    typical: str = ""
    formula: Optional[str] = None
    evidence: EvidenceLevel = EvidenceLevel.REVIEWED
    note: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Plain-data form, used by every exporter."""
        return {
            "name": self.name,
            "symbol": self.symbol,
            "unit": self.unit,
            "typical": self.typical,
            "formula": self.formula,
            "evidence": self.evidence.value,
            "note": self.note,
        }

    def render(self) -> str:
        """One-line human rendering, e.g. ``"mu [1/h] 0.1-1.2 - Specific growth rate"``."""
        span = f" {self.typical}" if self.typical else ""
        return f"{self.symbol} [{self.unit}]{span} - {self.name}"

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return self.render()


@dataclass(frozen=True)
class Milestone:
    """A dated event in the history of a subtype.

    History matters for a non-technical reader more than any other field: it
    is the difference between "this is science fiction" and "this has been in
    hospitals since 1982".

    Attributes
    ----------
    year:
        Four-digit year. Approximate years are fine; use ``circa`` in the note.
    event:
        What happened, in one clause.
    note:
        Optional detail, such as who did it or why it mattered.
    """

    year: int
    event: str
    note: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {"year": self.year, "event": self.event, "note": self.note}

    def render(self) -> str:
        """``"1982  First recombinant insulin approved"``."""
        return f"{self.year}  {self.event}"

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return self.render()


# =============================================================================
#  Subtype
# =============================================================================
@dataclass(frozen=True)
class Subtype:
    """A sub-discipline inside one colour branch of biotechnology.

    This is the fundamental unit of the taxonomy. There are eighty-five of
    them, each defined in its own module under
    ``src/biotechnology/branches/<colour>/<key>.py`` so that a contributor who
    wants to correct one field never has to open a thousand-line file.

    The fields fall into five groups.

    **Identity**
        ``key``, ``name``, ``aliases``, ``branch_key`` (stamped on by the
        branch during assembly), and the derived ``path``.

    **Explanation, two registers**
        ``summary`` and ``description`` for a technical reader;
        ``plain_language``, ``analogy`` and ``why_it_matters`` for everybody
        else. All five are mandatory in practice - the validation suite
        rejects a subtype that leaves the plain-language fields empty,
        because a half-explained record is worse than none.

    **Practice**
        ``applications``, ``technologies``, ``organisms``, ``techniques``,
        ``challenges``.

    **Quantitative hooks**
        ``metrics`` and ``formulas`` connect this record to the calculation
        modules.

    **Context**
        ``maturity``, ``risk_tier``, ``scale``, ``domains``,
        ``regulatory_status``, ``regulations``, ``standards``, ``milestones``,
        ``sdgs``, ``glossary``, ``references``, ``related``.
    """

    # -- identity -------------------------------------------------------------
    key: str
    name: str

    # -- explanation ----------------------------------------------------------
    summary: str = ""
    description: str = ""
    plain_language: str = ""
    analogy: str = ""
    why_it_matters: str = ""

    # -- practice -------------------------------------------------------------
    applications: Tuple[str, ...] = ()
    technologies: Tuple[str, ...] = ()
    organisms: Tuple[str, ...] = ()
    techniques: Tuple[str, ...] = ()
    challenges: Tuple[str, ...] = ()

    # -- quantitative hooks ---------------------------------------------------
    metrics: Tuple[Metric, ...] = ()
    formulas: Tuple[str, ...] = ()

    # -- context --------------------------------------------------------------
    maturity: Maturity = Maturity.EMERGING
    risk_tier: RiskTier = RiskTier.ROUTINE
    scale: Scale = Scale.BENCH
    domains: Tuple[Domain, ...] = ()
    regulatory_status: RegulatoryStatus = RegulatoryStatus.VARIES
    regulations: Tuple[str, ...] = ()
    standards: Tuple[str, ...] = ()
    milestones: Tuple[Milestone, ...] = ()
    sdgs: Tuple[int, ...] = ()
    glossary: Tuple[str, ...] = ()
    references: Tuple[str, ...] = ()
    related: Tuple[str, ...] = ()
    aliases: Tuple[str, ...] = ()

    # -- assigned by Branch.build --------------------------------------------
    branch_key: str = ""

    # -------------------------------------------------------------------------
    #  Identity
    # -------------------------------------------------------------------------
    @property
    def path(self) -> str:
        """Dotted address, e.g. ``"red.gene_therapy"``.

        Before a subtype is attached to a branch, ``branch_key`` is empty and
        the path degrades to the bare key. Data modules therefore never rely
        on ``path`` at definition time.
        """
        return f"{self.branch_key}.{self.key}" if self.branch_key else self.key

    @property
    def branch(self) -> "Branch":
        """The :class:`Branch` this subtype belongs to.

        Resolved lazily through the registry rather than stored as an object
        reference, which would create a reference cycle between two frozen
        dataclasses and break ``dataclasses.replace``.
        """
        from .registry import get_branch

        return get_branch(self.branch_key)

    # -------------------------------------------------------------------------
    #  Derived views
    # -------------------------------------------------------------------------
    @property
    def sdg_titles(self) -> Tuple[str, ...]:
        """Official titles of the Sustainable Development Goals cited here."""
        from ..sdg import title_of

        return tuple(title_of(g) for g in self.sdgs)

    @property
    def timeline(self) -> Tuple[Milestone, ...]:
        """Milestones sorted oldest first."""
        return tuple(sorted(self.milestones, key=lambda m: m.year))

    @property
    def first_year(self) -> Optional[int]:
        """Year of the earliest recorded milestone, or ``None`` when unknown."""
        return self.timeline[0].year if self.milestones else None

    def metric(self, symbol_or_name: str) -> Metric:
        """Look up one metric by symbol or by name, case-insensitively."""
        needle = symbol_or_name.strip().lower()
        for m in self.metrics:
            if needle in (m.symbol.lower(), m.name.lower()):
                return m
        raise UnknownSubtypeError(
            symbol_or_name,
            [m.symbol for m in self.metrics],
            branch_key=self.path,
        )

    # -------------------------------------------------------------------------
    #  Search support
    # -------------------------------------------------------------------------
    def haystack(self) -> str:
        """Every searchable field flattened into one lower-cased string.

        Computed on demand rather than cached: the taxonomy is small enough
        that a full scan costs well under a millisecond, and caching on a
        frozen dataclass would need ``object.__setattr__`` gymnastics.
        """
        parts: List[str] = [
            self.key,
            self.name,
            self.branch_key,
            self.summary,
            self.description,
            self.plain_language,
            self.analogy,
            self.why_it_matters,
        ]
        parts.extend(self.aliases)
        parts.extend(self.applications)
        parts.extend(self.technologies)
        parts.extend(self.organisms)
        parts.extend(self.techniques)
        parts.extend(self.challenges)
        parts.extend(self.regulations)
        parts.extend(self.standards)
        parts.extend(self.glossary)
        parts.extend(m.name for m in self.metrics)
        parts.extend(m.symbol for m in self.metrics)
        parts.extend(m.event for m in self.milestones)
        return " ".join(p for p in parts if p).lower()

    # -------------------------------------------------------------------------
    #  Export
    # -------------------------------------------------------------------------
    def to_dict(self, *, verbose: bool = True) -> Dict[str, Any]:
        """Plain-data form.

        Parameters
        ----------
        verbose:
            When ``False``, only identity and the two summaries are emitted.
            Used for index pages and search results, where dumping every
            field would produce megabytes of noise.
        """
        compact: Dict[str, Any] = {
            "path": self.path,
            "key": self.key,
            "name": self.name,
            "branch": self.branch_key,
            "summary": self.summary,
            "plain_language": self.plain_language,
        }
        if not verbose:
            return compact
        compact.update(
            {
                "analogy": self.analogy,
                "description": self.description,
                "why_it_matters": self.why_it_matters,
                "applications": list(self.applications),
                "technologies": list(self.technologies),
                "organisms": list(self.organisms),
                "techniques": list(self.techniques),
                "challenges": list(self.challenges),
                "metrics": [m.to_dict() for m in self.metrics],
                "formulas": list(self.formulas),
                "maturity": self.maturity.value,
                "risk_tier": self.risk_tier.value,
                "scale": self.scale.value,
                "domains": [d.value for d in self.domains],
                "regulatory_status": self.regulatory_status.value,
                "regulations": list(self.regulations),
                "standards": list(self.standards),
                "milestones": [m.to_dict() for m in self.timeline],
                "sdgs": list(self.sdgs),
                "glossary": list(self.glossary),
                "references": list(self.references),
                "related": list(self.related),
                "aliases": list(self.aliases),
            }
        )
        return compact

    # -------------------------------------------------------------------------
    #  Dunder
    # -------------------------------------------------------------------------
    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return self.name

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Subtype({self.path!r})"


# =============================================================================
#  Branch
# =============================================================================
@dataclass(frozen=True)
class Branch:
    """One of the ten colour-coded branches of biotechnology.

    A branch behaves like a read-only mapping of its subtypes, so all of the
    following work:

        len(branch)          number of subtypes
        for s in branch      iterate in declaration order
        "key" in branch      membership by key or by Subtype
        branch["key"]        indexed access, raising UnknownSubtypeError
        branch.get("key")    non-raising access

    Instances are never constructed directly. Use :meth:`build`, which stamps
    each subtype with its ``branch_key`` and builds the lookup index.
    """

    key: str
    name: str
    colour: str
    summary: str
    description: str
    plain_language: str = ""
    analogy: str = ""
    why_it_matters: str = ""
    origin_note: str = ""
    subtypes: Tuple[Subtype, ...] = ()
    aliases: Tuple[str, ...] = ()
    domains: Tuple[Domain, ...] = ()
    sdgs: Tuple[int, ...] = ()
    milestones: Tuple[Milestone, ...] = ()
    key_questions: Tuple[str, ...] = ()
    references: Tuple[str, ...] = ()

    # Private lookup index. `compare=False` keeps it out of __eq__, and
    # `repr=False` keeps it out of the printed representation; without both,
    # a Branch would print thousands of lines.
    _index: Dict[str, Subtype] = field(default_factory=dict, repr=False, compare=False)

    # -------------------------------------------------------------------------
    #  Construction
    # -------------------------------------------------------------------------
    @classmethod
    def build(
        cls,
        *,
        key: str,
        name: str,
        colour: str,
        summary: str,
        description: str,
        subtypes: Sequence[Subtype],
        plain_language: str = "",
        analogy: str = "",
        why_it_matters: str = "",
        origin_note: str = "",
        aliases: Sequence[str] = (),
        domains: Sequence[Domain] = (),
        sdgs: Sequence[int] = (),
        milestones: Sequence[Milestone] = (),
        key_questions: Sequence[str] = (),
        references: Sequence[str] = (),
    ) -> "Branch":
        """Assemble a branch from loose subtypes.

        Two things happen here that cannot happen in a data module:

        1. Each subtype is rebound with ``branch_key`` set, so that ``path``
           works. Because ``Subtype`` is frozen, this means constructing a
           copy via :func:`dataclasses.replace` rather than mutating.
        2. Duplicate keys are detected immediately, at import time, with a
           message naming the branch. Finding a duplicate three weeks later
           through a mysteriously missing search hit is far more expensive.
        """
        from dataclasses import replace

        bound = tuple(replace(s, branch_key=key) for s in subtypes)

        seen: Dict[str, int] = {}
        for s in bound:
            seen[s.key] = seen.get(s.key, 0) + 1
        duplicates = sorted(k for k, n in seen.items() if n > 1)
        if duplicates:
            raise SchemaError(
                field="subtypes",
                expected="unique keys",
                got=duplicates,
                location=f"branch {key!r}",
            )

        return cls(
            key=key,
            name=name,
            colour=colour,
            summary=summary,
            description=description,
            plain_language=plain_language,
            analogy=analogy,
            why_it_matters=why_it_matters,
            origin_note=origin_note,
            subtypes=bound,
            aliases=tuple(aliases),
            domains=tuple(domains),
            sdgs=tuple(sdgs),
            milestones=tuple(milestones),
            key_questions=tuple(key_questions),
            references=tuple(references),
            _index={s.key: s for s in bound},
        )

    # -------------------------------------------------------------------------
    #  Colour helpers
    # -------------------------------------------------------------------------
    @property
    def color(self) -> str:
        """US-spelling alias of :attr:`colour`, for American callers."""
        return self.colour

    @property
    def rgb(self) -> Tuple[int, int, int]:
        """The branch colour as an ``(r, g, b)`` triple of 0-255 integers."""
        h = self.colour.lstrip("#")
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

    @property
    def is_light(self) -> bool:
        """True when black text is more readable than white on this colour.

        Uses the ITU-R BT.601 luma coefficients, the same weighting used for
        broadcast grayscale conversion::

            Y = 0.299 R + 0.587 G + 0.114 B

        Two branches return ``True``: white at a luma of about 238, and
        yellow at about 177. White is the reason the check exists, since its
        swatch would otherwise be rendered with invisible white-on-white
        labels, and yellow needs the same treatment for the same reason in
        weaker form.

        One caution for anyone changing a branch colour. Gold sits at a luma
        of roughly 160, which is within half a unit of the threshold, so a
        small adjustment to that swatch would flip its label colour. The
        threshold is a convention rather than a perceptual constant, and a
        renderer needing guaranteed contrast should compute a contrast ratio
        against its actual text colour rather than relying on this property.
        """
        r, g, b = self.rgb
        return (0.299 * r + 0.587 * g + 0.114 * b) > 160

    # -------------------------------------------------------------------------
    #  Mapping protocol
    # -------------------------------------------------------------------------
    def __iter__(self) -> Iterator[Subtype]:
        return iter(self.subtypes)

    def __len__(self) -> int:
        return len(self.subtypes)

    def __contains__(self, item: object) -> bool:
        if isinstance(item, Subtype):
            return item.branch_key == self.key and item.key in self._index
        return isinstance(item, str) and item.strip().lower() in self._index

    def __getitem__(self, key: str) -> Subtype:
        try:
            return self._index[key.strip().lower()]
        except KeyError:
            raise UnknownSubtypeError(key, self.keys(), branch_key=self.key) from None

    def get(self, key: str, default: Optional[Subtype] = None) -> Optional[Subtype]:
        """Return a subtype by key, or ``default`` when absent."""
        return self._index.get(key.strip().lower(), default)

    def keys(self) -> Tuple[str, ...]:
        """Subtype keys in declaration order."""
        return tuple(s.key for s in self.subtypes)

    def names(self) -> Tuple[str, ...]:
        """Subtype display names in declaration order."""
        return tuple(s.name for s in self.subtypes)

    def paths(self) -> Tuple[str, ...]:
        """Fully qualified subtype paths in declaration order."""
        return tuple(s.path for s in self.subtypes)

    # -------------------------------------------------------------------------
    #  Derived views
    # -------------------------------------------------------------------------
    @property
    def timeline(self) -> Tuple[Milestone, ...]:
        """Branch milestones plus every subtype milestone, oldest first."""
        pooled: List[Milestone] = list(self.milestones)
        for s in self.subtypes:
            pooled.extend(s.milestones)
        return tuple(sorted(pooled, key=lambda m: m.year))

    @property
    def all_sdgs(self) -> Tuple[int, ...]:
        """Every SDG cited by the branch or any of its subtypes, sorted."""
        pooled = set(self.sdgs)
        for s in self.subtypes:
            pooled.update(s.sdgs)
        return tuple(sorted(pooled))

    @property
    def all_formulas(self) -> Tuple[str, ...]:
        """Every formula key referenced by any subtype, de-duplicated."""
        seen: Dict[str, None] = {}
        for s in self.subtypes:
            for f in s.formulas:
                seen.setdefault(f, None)
        return tuple(seen)

    def by_maturity(self, maturity: Union[Maturity, str]) -> Tuple[Subtype, ...]:
        """Subtypes at a given readiness band."""
        want = maturity if isinstance(maturity, Maturity) else Maturity.parse(maturity)
        return tuple(s for s in self.subtypes if s.maturity is want)

    def search(self, query: str) -> List[Subtype]:
        """Substring search restricted to this branch."""
        needle = query.strip().lower()
        if not needle:
            return []
        return [s for s in self.subtypes if needle in s.haystack()]

    def haystack(self) -> str:
        """Every searchable branch-level field, flattened and lower-cased."""
        parts = [
            self.key,
            self.name,
            self.summary,
            self.description,
            self.plain_language,
            self.analogy,
            self.why_it_matters,
            *self.aliases,
            *self.key_questions,
        ]
        return " ".join(p for p in parts if p).lower()

    # -------------------------------------------------------------------------
    #  Export
    # -------------------------------------------------------------------------
    def to_dict(
        self, *, include_subtypes: bool = True, verbose: bool = True
    ) -> Dict[str, Any]:
        """Plain-data form of the branch and, optionally, its subtypes."""
        data: Dict[str, Any] = {
            "key": self.key,
            "name": self.name,
            "colour": self.colour,
            "rgb": list(self.rgb),
            "summary": self.summary,
            "plain_language": self.plain_language,
            "analogy": self.analogy,
            "description": self.description,
            "why_it_matters": self.why_it_matters,
            "origin_note": self.origin_note,
            "aliases": list(self.aliases),
            "domains": [d.value for d in self.domains],
            "sdgs": list(self.sdgs),
            "key_questions": list(self.key_questions),
            "milestones": [m.to_dict() for m in self.milestones],
            "references": list(self.references),
            "subtype_count": len(self.subtypes),
        }
        if include_subtypes:
            data["subtypes"] = [s.to_dict(verbose=verbose) for s in self.subtypes]
        return data

    # -------------------------------------------------------------------------
    #  Dunder
    # -------------------------------------------------------------------------
    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return self.name

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Branch({self.key!r}, subtypes={len(self.subtypes)})"


#: Anything addressable by a dotted path.
Node = Union[Branch, Subtype]
