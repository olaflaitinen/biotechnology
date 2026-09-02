# =============================================================================
#  biotechnology.core.enums
# -----------------------------------------------------------------------------
#  Controlled vocabularies used across the whole taxonomy.
#
#  WHY ENUMS AND NOT PLAIN STRINGS?
#  Every subtype in this library carries a maturity level, a risk tier, an
#  operating scale and an evidence grade. If those were free-text strings,
#  eighty-five separate module authors would spell them eighty-five different
#  ways ("pilot", "Pilot scale", "pilot-scale", ...) and no filter would ever
#  work. An enumeration makes the vocabulary finite, self-documenting and
#  machine-checkable: a typo becomes an ImportError at package load time
#  instead of a silently empty query result three months later.
#
#  READING THIS FILE WITHOUT A BIOLOGY BACKGROUND
#  Each member below carries three things:
#    * a machine value  -> the short lowercase string stored and exported
#    * .label           -> a human title, safe to print in a report
#    * .explain()       -> a plain-language sentence with no jargon
#  So `Maturity.PILOT.explain()` tells a non-specialist what "pilot" means
#  without them having to know anything about process engineering.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional, Tuple

__all__ = [
    "DescribedEnum",
    "Maturity",
    "RiskTier",
    "Scale",
    "EvidenceLevel",
    "Domain",
    "RegulatoryStatus",
    "vocabularies",
]


# =============================================================================
#  Shared base class
# =============================================================================
class DescribedEnum(Enum):
    """Base class for every controlled vocabulary in this package.

    A plain :class:`enum.Enum` member carries only a value. Members of this
    class carry three fields instead, supplied as a tuple at declaration time:

    ``(value, label, explanation)``

    ``value``
        The short, stable, lowercase token. This is what gets written to JSON,
        CSV and the database. Never change one of these without a major
        version bump - downstream filters depend on them.
    ``label``
        A capitalised human-readable title, suitable for a table header or a
        slide.
    ``explanation``
        One sentence of plain language aimed at a reader with no training in
        the field. This is what makes the library usable by policy staff,
        journalists and students, not only by scientists.
    """

    # -------------------------------------------------------------------------
    #  __new__ is used (rather than __init__) because Enum resolves the member
    #  value during __new__. We hand Enum only the first element of the tuple
    #  as the canonical value, then attach the two descriptive fields.
    # -------------------------------------------------------------------------
    def __new__(cls, value: str, label: str, explanation: str) -> "DescribedEnum":
        obj = object.__new__(cls)
        obj._value_ = value
        obj._label = label
        obj._explanation = explanation
        return obj

    # -- descriptive accessors ------------------------------------------------
    @property
    def label(self) -> str:
        """Capitalised human-readable title, e.g. ``"Pilot scale"``."""
        return self._label

    @property
    def explanation(self) -> str:
        """One plain-language sentence describing the member."""
        return self._explanation

    def explain(self) -> str:
        """Return ``"Label - explanation"``, ready to print."""
        return f"{self.label} - {self.explanation}"

    # -- lookup helpers -------------------------------------------------------
    @classmethod
    def parse(cls, raw: str) -> "DescribedEnum":
        """Resolve a member from its value or its label, case-insensitively.

        This is deliberately forgiving because the same vocabulary is typed by
        hand in data modules, passed on the command line and read back out of
        JSON files.

        Raises
        ------
        ValueError
            If ``raw`` matches no member. The message lists every valid token,
            so the caller never has to open this file to find out.
        """
        needle = str(raw).strip().lower().replace(" ", "_").replace("-", "_")
        for member in cls:
            if needle in (member.value, member.label.lower().replace(" ", "_")):
                return member
        valid = ", ".join(m.value for m in cls)
        raise ValueError(f"unknown {cls.__name__} {raw!r}; valid values: {valid}")

    @classmethod
    def values(cls) -> Tuple[str, ...]:
        """Every machine value, in declaration order."""
        return tuple(m.value for m in cls)

    @classmethod
    def table(cls) -> List[Dict[str, str]]:
        """The whole vocabulary as a list of dicts, for docs and exports."""
        return [
            {"value": m.value, "label": m.label, "explanation": m.explanation}
            for m in cls
        ]

    # -- ordering -------------------------------------------------------------
    #  Declaration order is meaningful for every vocabulary here (research ->
    #  commercial, low risk -> high risk, bench -> industrial), so we expose it
    #  as a sortable rank rather than relying on alphabetical string order.
    @property
    def rank(self) -> int:
        """Zero-based position in declaration order; higher means further along."""
        return list(type(self)).index(self)

    def __lt__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            return self.rank < other.rank
        return NotImplemented

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return self.value


# =============================================================================
#  Maturity - how far from the laboratory bench a subtype has travelled
# =============================================================================
class Maturity(DescribedEnum):
    """Technology readiness, expressed in five steps instead of nine.

    The European Commission and NASA both use a nine-point Technology
    Readiness Level (TRL) scale. Nine steps is more resolution than a field
    survey can honestly support, so this library collapses them into five
    bands and records the approximate TRL span in :meth:`trl_range`.
    """

    RESEARCH = (
        "research",
        "Research",
        "Still being studied in laboratories; no product exists yet.",
    )
    EMERGING = (
        "emerging",
        "Emerging",
        "Works in the laboratory and the first companies are trying to scale it.",
    )
    PILOT = (
        "pilot",
        "Pilot",
        "Being run at demonstration size to see whether it survives real conditions.",
    )
    COMMERCIAL = (
        "commercial",
        "Commercial",
        "Sold as a product or service today, though not yet everywhere.",
    )
    ESTABLISHED = (
        "established",
        "Established",
        "Routine, widely deployed and often decades old.",
    )

    def trl_range(self) -> Tuple[int, int]:
        """Approximate Technology Readiness Level span for this band."""
        return {
            "research": (1, 3),
            "emerging": (3, 5),
            "pilot": (5, 7),
            "commercial": (7, 9),
            "established": (9, 9),
        }[self.value]


# =============================================================================
#  RiskTier - how much oversight the work attracts
# =============================================================================
class RiskTier(DescribedEnum):
    """Governance intensity, not danger to an individual worker.

    A tier says how much review, licensing and documentation an activity
    typically attracts. It is not a laboratory biosafety level: a BSL-2
    organism handled under a clinical trial protocol sits in ``REGULATED``
    here because the paperwork, not the pathogen, dominates.
    """

    ROUTINE = (
        "routine",
        "Routine",
        "Ordinary laboratory or factory work with standard safety rules.",
    )
    CONTROLLED = (
        "controlled",
        "Controlled",
        "Needs a permit, a licence or an institutional committee sign-off.",
    )
    REGULATED = (
        "regulated",
        "Regulated",
        "Overseen by a national agency before it may be sold or released.",
    )
    RESTRICTED = (
        "restricted",
        "Restricted",
        "Access to materials or methods is deliberately limited by law.",
    )

    def requires_committee(self) -> bool:
        """True when an institutional review body is normally involved."""
        return self.rank >= RiskTier.CONTROLLED.rank


# =============================================================================
#  Scale - the physical size at which the work is normally done
# =============================================================================
class Scale(DescribedEnum):
    """Working volume or land area, in five bands."""

    BENCH = (
        "bench",
        "Bench scale",
        "Fits on a laboratory bench; millilitres to a few litres.",
    )
    PILOT = (
        "pilot",
        "Pilot scale",
        "A small demonstration plant; tens to thousands of litres.",
    )
    INDUSTRIAL = (
        "industrial",
        "Industrial scale",
        "A full production plant; cubic metres and upward.",
    )
    FIELD = (
        "field",
        "Field scale",
        "Open land, water or an animal herd rather than a vessel.",
    )
    POPULATION = (
        "population",
        "Population scale",
        "Whole communities, countries or ecosystems.",
    )


# =============================================================================
#  EvidenceLevel - how solid the claims in a record are
# =============================================================================
class EvidenceLevel(DescribedEnum):
    """Confidence grade attached to metrics and statements.

    Data modules in this package mix textbook consensus with figures taken
    from a single recent paper. Recording which is which keeps the library
    honest and lets cautious users filter to the settled material only.
    """

    CONSENSUS = (
        "consensus",
        "Consensus",
        "Textbook material that the field agrees on.",
    )
    REVIEWED = (
        "reviewed",
        "Reviewed",
        "Supported by peer-reviewed literature or an official report.",
    )
    REPORTED = (
        "reported",
        "Reported",
        "Stated in one credible source but not yet widely replicated.",
    )
    INDICATIVE = (
        "indicative",
        "Indicative",
        "A rough order-of-magnitude figure, useful for orientation only.",
    )


# =============================================================================
#  Domain - the broad sector a subtype serves
# =============================================================================
class Domain(DescribedEnum):
    """Cross-cutting sector labels, orthogonal to the colour branches.

    Colours group by tradition; domains group by who pays. A single colour
    can span several domains, and one domain appears in several colours, so
    these labels give a second axis for filtering.
    """

    HEALTH = ("health", "Health", "Human medicine, diagnosis and care.")
    FOOD = ("food", "Food", "Growing, processing and preserving what we eat.")
    ENERGY = ("energy", "Energy", "Fuels, electricity and heat from biological sources.")
    MATERIALS = ("materials", "Materials", "Plastics, fibres, chemicals and construction stock.")
    ENVIRONMENT = ("environment", "Environment", "Pollution, waste, water and ecosystems.")
    INFORMATION = ("information", "Information", "Data, software, models and databases.")
    GOVERNANCE = ("governance", "Governance", "Law, ethics, standards and oversight.")
    SECURITY = ("security", "Security", "Protection against accidental or deliberate harm.")


# =============================================================================
#  RegulatoryStatus - where a class of product sits with the authorities
# =============================================================================
class RegulatoryStatus(DescribedEnum):
    """How a product class is treated by regulators, in broad terms.

    These labels are jurisdiction-neutral on purpose. A genome-edited plant
    is ``VARIES`` because the European Union, the United States and Japan
    reach three different answers about the same organism.
    """

    UNREGULATED = (
        "unregulated",
        "Unregulated",
        "No product-specific approval is normally required.",
    )
    NOTIFIED = (
        "notified",
        "Notified",
        "The authorities must be told, but no full approval is needed.",
    )
    AUTHORISED = (
        "authorised",
        "Authorised",
        "A formal licence must be granted before sale or release.",
    )
    VARIES = (
        "varies",
        "Varies by jurisdiction",
        "Different countries reach materially different decisions.",
    )
    PROHIBITED = (
        "prohibited",
        "Prohibited",
        "Banned outright in most or all jurisdictions.",
    )


# =============================================================================
#  Registry of every vocabulary, for documentation generation
# =============================================================================
_VOCABULARIES: Dict[str, type] = {
    "maturity": Maturity,
    "risk_tier": RiskTier,
    "scale": Scale,
    "evidence_level": EvidenceLevel,
    "domain": Domain,
    "regulatory_status": RegulatoryStatus,
}


def vocabularies(name: Optional[str] = None):
    """Return the controlled vocabularies, or one of them by name.

    Used by ``tools/generate_docs.py`` to render the vocabulary reference
    pages, and by the CLI's ``vocab`` command.

    >>> sorted(vocabularies())          # doctest: +ELLIPSIS
    ['domain', 'evidence_level', ...]
    >>> vocabularies("maturity") is Maturity
    True
    """
    if name is None:
        return dict(_VOCABULARIES)
    try:
        return _VOCABULARIES[name.strip().lower()]
    except KeyError:
        valid = ", ".join(sorted(_VOCABULARIES))
        raise ValueError(f"unknown vocabulary {name!r}; valid: {valid}") from None
