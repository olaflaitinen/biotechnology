# =============================================================================
#  biotechnology.branches.yellow.cultivated_meat.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST TWO METRICS ARE A COST AND ITS DOMINANT COMPONENT, and putting
#  them there is the whole argument of this record.
#
#  The biology works. Cells grow, differentiate and taste like meat. What has
#  not been achieved is a price, and the reason is specific rather than
#  general: the dominant cost is a CONSUMABLE INPUT rather than a fixed cost
#  that volume spreads. Medium cost per litre falls when the formulation
#  changes and not when the factory gets bigger.
#
#  That distinction matters because most cost projections in this field were
#  borrowed from technologies where learning curves apply. It is the same error
#  `yellow.precision_fermentation` records for 2023 and the same shape
#  `white.biobased_chemicals` records for succinic acid, and this facet is
#  ordered so a reader sees it before anything about cell density or
#  differentiation.
#
#  A NOTE ON THE ENVIRONMENTAL METRICS. They are graded REPORTED and the
#  uncertainty is genuine rather than a hedge. Published assessments disagree on
#  whether cultivated meat beats conventional beef, and they disagree because
#  the answer depends on the energy source and on how medium inputs are made,
#  neither of which is settled. Presenting a single figure would be false
#  precision.
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
    #  THE COST, AND WHY IT DOES NOT FALL THE WAY PROJECTIONS ASSUMED
    # =========================================================================
    Metric(
        name="Production cost per kilogram",
        symbol="C_kg",
        unit="euro per kilogram of product",
        typical="far above commodity meat; the 2013 demonstration cost was in "
        "the hundreds of thousands of euro per kilogram and current figures "
        "are much lower and not competitive",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The number the field is judged by and the one companies publish "
            "least. The decline since 2013 is real and large; the remaining gap "
            "to commodity meat is also real and large. Graded REPORTED because "
            "published figures are company estimates at assumed scale rather "
            "than audited production costs."
        ),
    ),
    Metric(
        name="Medium cost per litre",
        symbol="C_med",
        unit="euro per litre of growth medium",
        typical="the dominant component of cost of goods, and the target of "
        "most of the field's technical work",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The reason the scale-up curve does not behave like the ones the "
            "projections were borrowed from. This is a CONSUMABLE, so its price "
            "falls when the formulation changes, when pharmaceutical-grade "
            "components are replaced with food-grade ones, and when medium is "
            "recycled. It does not fall because the factory is larger."
        ),
    ),
    Metric(
        name="Medium consumption per kilogram of product",
        symbol="V_med",
        unit="litres of medium per kilogram of biomass",
        typical="high, and reduced by perfusion and recycling rather than by "
        "cell biology",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The other half of the medium cost, and the half that process "
            "engineering can address. Recovering and recycling unconsumed "
            "components attacks this figure directly, which is why perfusion "
            "appears in `practice.TECHNOLOGIES` as an economic measure rather "
            "than a biological one."
        ),
    ),
    # =========================================================================
    #  WHAT THE CULTURE ACHIEVES
    # =========================================================================
    Metric(
        name="Maximum cell density",
        symbol="X_max",
        unit="cells per millilitre",
        typical="10^7 - 10^8 cells/mL in high-density perfusion systems",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Determines how much product a given reactor volume yields and "
            "therefore the capital requirement. It is capped not by nutrient "
            "supply but by oxygen transfer and by lactate and ammonia "
            "accumulation, which is why raising it is a bioreactor problem "
            "rather than a medium problem."
        ),
    ),
    Metric(
        name="Population doubling time",
        symbol="t_d",
        unit="hours",
        typical="18 - 30 h for animal cells, against under an hour for "
        "bacteria",
        formula="specific_growth_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The structural disadvantage against every fermentation record in "
            "this library. An animal cell doubles roughly once a day; a "
            "bacterium doubles in under an hour. Reactor time is therefore "
            "measured in weeks rather than days, which multiplies both capital "
            "requirement and contamination risk."
        ),
    ),
    Metric(
        name="Population doublings before senescence",
        symbol="N_pd",
        unit="doublings",
        typical="limited in primary cells; unlimited in immortalised lines",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The reason immortalised cell lines matter commercially. A primary "
            "line that senesces requires a fresh biopsy periodically, which "
            "reintroduces the animal the process exists to remove. "
            "Immortalisation solves it and raises the regulatory and consumer "
            "question recorded in `practice.CHALLENGES`."
        ),
    ),
    Metric(
        name="Differentiation efficiency",
        symbol="f_diff",
        unit="per cent of cells forming myotubes or adipocytes",
        typical="varies widely and is a principal determinant of product "
        "quality",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Undifferentiated cells are biomass rather than meat. This is the "
            "step that separates a cell culture from a food, and it is "
            "typically induced by withdrawing growth factors, which means the "
            "process must switch from expansion to differentiation rather than "
            "doing both at once."
        ),
    ),
    Metric(
        name="Oxygen transfer coefficient",
        symbol="kLa",
        unit="per hour",
        formula="oxygen_transfer_rate",
        typical="constrained by shear tolerance far below what microbial "
        "culture permits",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The same quantity `white.bioprocess_engineering` records, under a "
            "constraint that record does not face. Agitation supplies oxygen "
            "and damages animal cells, so the two requirements are in direct "
            "opposition and the achievable density follows from where the "
            "compromise is struck."
        ),
    ),
    # =========================================================================
    #  IS IT MEAT
    # =========================================================================
    Metric(
        name="Protein and fat composition",
        symbol="C_comp",
        unit="per cent by weight",
        typical="matched to the conventional product it represents",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Compositional equivalence is achievable and is not the same as "
            "sensory equivalence. A formed product from loose cells can match "
            "on composition and differ entirely in texture, which is why the "
            "structural work in `practice.TECHNOLOGIES` is a separate problem "
            "from the culture."
        ),
    ),
    Metric(
        name="Construct thickness achievable",
        symbol="d_max",
        unit="micrometres without perfusion",
        typical="roughly 100 - 200 um, the same oxygen diffusion limit that "
        "governs tissue engineering",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The reason whole cuts remain unachieved. It is precisely the limit "
            "`red.regenerative_medicine` is organised around, and it is a "
            "property of oxygen diffusion in tissue rather than of any "
            "technique. Anything thicker requires a vascular supply or "
            "engineered perfusion, and neither has been demonstrated at food "
            "scale."
        ),
    ),
    # =========================================================================
    #  WHAT IT COSTS THE WORLD, WHICH IS GENUINELY UNCERTAIN
    # =========================================================================
    Metric(
        name="Greenhouse gas intensity",
        symbol="GWP",
        unit="kilograms of carbon dioxide equivalent per kilogram of product",
        formula="carbon_intensity",
        typical="published assessments disagree on whether it beats "
        "conventional beef",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The uncertainty here is genuine rather than a hedge. The result "
            "depends chiefly on the energy source powering the process and on "
            "how medium inputs are manufactured, and assessments differ on both "
            "because neither is settled. A single figure would be false "
            "precision, and the field's promotional material frequently "
            "supplies one."
        ),
    ),
    Metric(
        name="Energy use per kilogram",
        symbol="E_kg",
        unit="megajoules per kilogram of product",
        typical="high, since the process replaces an animal's metabolism with "
        "heating, mixing and sterile manufacture",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The honest core of the environmental question. A cow does its own "
            "thermoregulation, mixing and immune defence at no energy cost to "
            "the producer, and a bioreactor does not. Whether the substitution "
            "is favourable depends on how that energy is generated, which is "
            "why the assessments disagree."
        ),
    ),
    Metric(
        name="Land use per kilogram of protein",
        symbol="A_land",
        unit="square metres per kilogram",
        typical="much lower than ruminant meat, and not zero because medium "
        "inputs are agricultural",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The strongest environmental claim in the record and the one least "
            "sensitive to the energy assumption. Sugars, amino acids and plant "
            "hydrolysates in the medium are grown, so land use is greatly "
            "reduced rather than eliminated, on the same terms "
            "`yellow.precision_fermentation` records."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Growth and transfer first, then the assessment relationships.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "specific_growth_rate",
    "monod_equation",
    "oxygen_transfer_rate",
    "space_time_yield",
    "carbon_intensity",
    "life_cycle_impact",
    "mass_balance",
)
