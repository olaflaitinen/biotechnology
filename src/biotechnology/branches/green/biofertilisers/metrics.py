# =============================================================================
#  biotechnology.branches.green.biofertilisers.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  One distinction runs through this whole set and is routinely collapsed on
#  product labels, in the field's own literature and in policy documents.
#
#  A VIABLE CELL COUNT IS NOT AN EFFECT. Colony forming units per gram measure
#  how many living organisms are in the bag. They say nothing about whether
#  those organisms will survive sowing, colonise a root, outcompete the native
#  population, or fix any nitrogen at all. A product can meet its label
#  specification perfectly and do nothing in a field.
#
#  The metrics below are therefore ordered from what is easy to measure and
#  weakly informative, through what is harder to measure and more informative,
#  to what actually matters and is hardest of all. Reading them in that order
#  is the fastest way to understand why this field's evidence base is
#  contested.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # -------------------------------------------------------------------------
    #  Easy to measure, weakly informative. The label number.
    # -------------------------------------------------------------------------
    Metric(
        name="Viable cell count",
        symbol="CFU/g",
        unit="colony forming units per gram or millilitre of product",
        typical="1e8 - 1e9 CFU/g at manufacture",
        formula="colony_forming_units",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The number on the label, and the only one most regulators check. "
            "Most national standards set a minimum at the point of sale rather "
            "than at manufacture, which matters because the count falls "
            "throughout storage. It measures what is in the bag, not what will "
            "happen in the field."
        ),
    ),
    # -------------------------------------------------------------------------
    #  How fast the label number stops being true.
    # -------------------------------------------------------------------------
    Metric(
        name="Shelf-life viability half-life",
        symbol="t_half_cfu",
        unit="months to lose half the viable count",
        typical="3 - 12 months, far shorter above 30 degC",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Strongly temperature-dependent, which is why a product warehoused "
            "in a hot climate can be dead on arrival while complying with its "
            "specification at dispatch. This is the single most common cause of "
            "field failure and is almost never measured by the purchaser."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Harder to measure, more informative. Did it establish?
    # -------------------------------------------------------------------------
    Metric(
        name="Nodule number and mass",
        symbol="N_nod",
        unit="nodules per plant, and dry mass per plant",
        typical="10 - 100 nodules per plant in a well-nodulated legume",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Counting is straightforward; attribution is not. Nodules formed by "
            "the native population look identical to those formed by the "
            "inoculant, so a good count proves the plant is nodulated and not "
            "that the product did anything. Strain-specific markers are needed "
            "to tell them apart."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Colonisation, the mycorrhizal equivalent.
    # -------------------------------------------------------------------------
    Metric(
        name="Mycorrhizal root colonisation",
        symbol="M%",
        unit="per cent of root length colonised",
        typical="20 - 80 %",
        formula="root_colonisation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Assessed by staining and gridline intersection. Colonisation "
            "percentage correlates only loosely with benefit: a heavily "
            "colonised root in a phosphorus-rich soil may be paying "
            "photosynthate for a service it does not need, and the net effect "
            "can be negative."
        ),
    ),
    # -------------------------------------------------------------------------
    #  What actually matters, and is hardest to measure.
    # -------------------------------------------------------------------------
    Metric(
        name="Biological nitrogen fixation",
        symbol="BNF",
        unit="kilograms of nitrogen per hectare per year",
        typical="30 - 300 kg N/ha/year in legumes; under 20 in associative "
        "systems",
        formula="nitrogen_fixation_rate",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The quantity the whole field exists to deliver, and the hardest to "
            "measure. Isotope dilution and natural abundance methods each carry "
            "large uncertainties, and the acetylene reduction assay measures "
            "nitrogenase activity at an instant rather than nitrogen "
            "accumulated over a season. Published ranges are wide for real "
            "reasons."
        ),
    ),
    # -------------------------------------------------------------------------
    #  How much of the plant's nitrogen came from air rather than soil.
    # -------------------------------------------------------------------------
    Metric(
        name="Proportion of nitrogen derived from the atmosphere",
        symbol="Ndfa",
        unit="per cent of plant nitrogen",
        typical="40 - 90 % in a well-nodulated legume",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Falls sharply when soil mineral nitrogen is high, because the "
            "plant stops paying for a service it can get free. Applying "
            "nitrogen fertiliser to an inoculated legume therefore substitutes "
            "for fixation rather than adding to it."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The competition question, which is what establishment really means.
    # -------------------------------------------------------------------------
    Metric(
        name="Inoculant occupancy of nodules",
        symbol="O_inoc",
        unit="per cent of nodules formed by the applied strain",
        typical="10 - 80 %, and low wherever a native population is present",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The number that separates a product that worked from a crop that "
            "would have nodulated anyway. It requires strain-specific markers "
            "and is rarely measured outside research, which is why the field's "
            "efficacy evidence is weaker than its publication volume suggests."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The agronomic outcome the farmer is buying.
    # -------------------------------------------------------------------------
    Metric(
        name="Nitrogen use efficiency",
        symbol="NUE",
        unit="kilograms of yield per kilogram of nitrogen applied",
        typical="20 - 60 kg/kg",
        formula="nutrient_use_efficiency",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The system-level measure, and the one that connects this record to "
            "eutrophication. Roughly half of applied synthetic nitrogen is not "
            "taken up by the crop, and what is not taken up goes somewhere."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  serial_dilution is included because every colony count in this record comes
#  from one, and a dilution error propagates directly into the label claim.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "colony_forming_units",
    "nitrogen_fixation_rate",
    "nutrient_use_efficiency",
    "root_colonisation",
    "serial_dilution",
    "exponential_growth",
    "specific_growth_rate",
)
