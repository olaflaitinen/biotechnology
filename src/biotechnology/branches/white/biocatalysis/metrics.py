# =============================================================================
#  biotechnology.branches.white.biocatalysis.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `white.industrial_enzymes` measures the CATALYST. This record measures the
#  PROCESS, and the two sets barely overlap. A reader who wants k_cat and K_M
#  should be in the other record; a reader who wants to know whether a route is
#  worth running is in the right one.
#
#  THE ORDER IS THE ARGUMENT. The first three metrics are the ones that kill
#  routes, in the order a project meets them: how much substrate can be put in
#  the vessel, how many times the cofactor turns over, and how much catalyst
#  each kilogram of product consumes. A route that fails any of these is dead
#  regardless of how elegant the enzymology is.
#
#  A WARNING ABOUT ENANTIOMERIC EXCESS. It is quoted more often than any other
#  number in this field and it flatters. Ninety-nine per cent ee sounds like
#  near-perfection and means one part in two hundred is the wrong enantiomer,
#  which for a medicine can be a specification failure. Worse, ee alone says
#  nothing about how much product there is: a kinetic resolution can report
#  excellent ee at low conversion precisely BECAUSE it has barely run. The
#  metric below carries that caution rather than leaving the reader to it.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # =========================================================================
    #  THE THREE THAT KILL ROUTES
    # =========================================================================
    Metric(
        name="Substrate loading",
        symbol="S_0",
        unit="grams of substrate per litre of reaction",
        typical="50 - 300 g/L for a viable process, often under 10 g/L at "
        "first attempt",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The first number a process chemist asks for and the one that most "
            "often ends a project. Enzymes work in water and most organic "
            "substrates do not dissolve in it, so an academically successful "
            "reaction at 2 grams per litre may be two orders of magnitude away "
            "from a manufacturable one. Everything in `practice.TECHNOLOGIES` "
            "about reaction media exists to raise this number."
        ),
    ),
    Metric(
        name="Cofactor total turnover number",
        symbol="TTN_cof",
        unit="moles of product per mole of cofactor, dimensionless",
        typical="10^3 - 10^6 with in situ regeneration",
        formula="total_turnover_number",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Usually the governing economic figure for any oxidoreductase or "
            "transaminase route, and more important than the enzyme's own "
            "turnover. A nicotinamide cofactor used once costs far more than "
            "the product; recycled ten thousand times it costs almost nothing. "
            "This single ratio is why coupled dehydrogenase regeneration is "
            "present in essentially every redox process."
        ),
    ),
    Metric(
        name="Biocatalyst yield",
        symbol="Y_cat",
        unit="kilograms of product per kilogram of enzyme preparation",
        typical="10 - 10^4 kg/kg",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The industrial form of total turnover number, expressed in the "
            "units a purchasing department uses. It is the figure that decides "
            "whether immobilisation is worth its development cost, because "
            "recovering and reusing the catalyst multiplies this number by the "
            "number of reuses."
        ),
    ),
    # =========================================================================
    #  HOW HARD THE PLANT IS WORKING
    # =========================================================================
    Metric(
        name="Space-time yield",
        symbol="STY",
        unit="grams of product per litre of reactor per hour",
        typical="1 - 100 g/L/h in batch, higher in packed-bed flow",
        formula="space_time_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Sets how much capital equipment a given output needs, and the "
            "metric on which biocatalysis most often loses to chemistry, "
            "because a dilute aqueous reaction occupies a large vessel for a "
            "small mass of product. Continuous flow over an immobilised bed is "
            "the standard answer."
        ),
    ),
    Metric(
        name="Conversion",
        symbol="X",
        unit="per cent of substrate consumed",
        typical="above 95 % required to avoid a separation problem",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Incomplete conversion leaves unreacted substrate that is usually "
            "chemically similar to the product and therefore expensive to "
            "remove. It must be read together with enantiomeric excess: a "
            "classical kinetic resolution is capped at fifty per cent "
            "conversion by definition, which is why dynamic kinetic resolution "
            "and deracemisation exist."
        ),
    ),
    # =========================================================================
    #  THE PROPERTY THE ROUTE WAS CHOSEN FOR
    # =========================================================================
    Metric(
        name="Enantiomeric excess",
        symbol="ee",
        unit="per cent",
        typical="above 99.5 % for a pharmaceutical intermediate",
        formula="enantiomeric_excess",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The most quoted and most flattering number in the field. Ninety "
            "nine per cent reads as near-perfect and means one part in two "
            "hundred is the wrong hand, which can still fail a specification. "
            "It also says nothing about quantity: a resolution can post an "
            "excellent ee at low conversion precisely because it has barely "
            "run. Always read it beside conversion and isolated yield."
        ),
    ),
    Metric(
        name="Diastereomeric ratio",
        symbol="dr",
        unit="ratio, dimensionless",
        typical="above 95:5 for a useful step",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The relevant selectivity measure once a molecule has more than "
            "one stereocentre, which is the common case in modern drug "
            "substances. Enzymes that set two centres in a single step, such "
            "as aldolases, are valued specifically for controlling this."
        ),
    ),
    # =========================================================================
    #  WHAT THE ROUTE COSTS THE ENVIRONMENT
    # =========================================================================
    Metric(
        name="Process mass intensity",
        symbol="PMI",
        unit="kilograms of total material input per kilogram of product",
        typical="under 50 is good for a pharmaceutical, several hundred is "
        "common",
        formula="process_mass_intensity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The metric the pharmaceutical industry adopted in preference to E "
            "factor because it counts everything that goes in, including water "
            "and including the mass used in workup, rather than only what "
            "comes out as waste. It is the standard basis on which a "
            "biocatalytic route redesign is justified."
        ),
    ),
    Metric(
        name="Environmental factor",
        symbol="E_factor",
        unit="kilograms of waste per kilogram of product",
        typical="25 - 100 for pharmaceuticals, under 5 for bulk chemicals",
        formula="e_factor",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The older green chemistry measure, kept because most of the "
            "literature this record draws on reports it. Pharmaceutical "
            "manufacture has the worst figure of any chemical sector by a wide "
            "margin, and solvent is the overwhelming majority of it."
        ),
    ),
    Metric(
        name="Atom economy",
        symbol="AE",
        unit="per cent of reactant mass appearing in the product",
        typical="higher for enzymatic routes that avoid protecting groups",
        formula="atom_economy",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A property of the route on paper rather than of the plant, since "
            "it ignores solvent and yield. Its usefulness here is that it "
            "captures the largest structural advantage of enzymatic synthesis: "
            "selectivity removes the protecting groups that conventional "
            "routes install and then discard."
        ),
    ),
    # =========================================================================
    #  WHETHER THE CATALYST SURVIVES THE PROCESS
    # =========================================================================
    Metric(
        name="Operational stability under process conditions",
        symbol="t_half_op",
        unit="hours of retained activity in the actual reaction medium",
        typical="24 - 2000 h",
        formula="enzyme_half_life",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Measured in the reaction as run, with its cosolvent, its "
            "substrate concentration and its shear, not in buffer. The gap "
            "between a buffer figure and a process figure is the most common "
            "unpleasant surprise in scale-up, and it is why solvent tolerance "
            "is engineered rather than assumed."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Ordered as the metrics are: the process-limiting quantities, then the
#  selectivity measures, then the green chemistry set.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "total_turnover_number",
    "space_time_yield",
    "enzyme_half_life",
    "enantiomeric_excess",
    "process_mass_intensity",
    "e_factor",
    "atom_economy",
    "partition_coefficient",
    "arrhenius_equation",
)
