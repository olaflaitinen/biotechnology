# =============================================================================
#  biotechnology.branches.yellow.biofortification.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS FACET IS ORDERED AS A CHAIN, AND EVERY LINK CAN BREAK.
#
#      content in the grain
#        -> retained after processing and cooking
#          -> absorbed rather than bound by phytate
#            -> eaten in sufficient quantity, often enough
#              -> a measurable change in nutritional status
#
#  A content figure is the first link and is routinely reported as though it
#  were the last. The breeding target exists precisely because somebody worked
#  backwards along this chain from a required change in status, and a record
#  that opened with content and stopped there would repeat the field's most
#  common overstatement.
#
#  YIELD PENALTY IS PLACED HIGH BECAUSE THE FARMER DECIDES BEFORE THE
#  NUTRITIONIST DOES. A variety with excellent micronutrient content and five
#  per cent less yield will not be planted, and the nutritional metrics below
#  it are then irrelevant.
#
#  A NOTE ON UNITS. Content is given per gram of dry weight, because moisture
#  varies with storage and a fresh weight figure is not comparable between
#  studies. This is the same basis problem `blue.seaweed_cultivation` records
#  and it produces the same confusion in the literature.
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
    #  THE FARMER'S DECISION, WHICH COMES FIRST
    # =========================================================================
    Metric(
        name="Yield penalty relative to the check variety",
        symbol="dY",
        unit="per cent difference in grain or root yield",
        typical="parity is the requirement; any measurable penalty is a "
        "barrier to adoption",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Placed first because a farmer decides before a nutritionist does. "
            "A variety with excellent micronutrient content and a small yield "
            "penalty will not be planted, and every nutritional metric below "
            "then describes something nobody grows. The benefit is invisible, "
            "delayed and accrues to the household rather than to the harvest, "
            "so it cannot be traded against yield."
        ),
    ),
    Metric(
        name="Adoption rate",
        symbol="f_adopt",
        unit="per cent of target farmers planting the biofortified variety",
        typical="varies enormously with seed system access and with whether "
        "the trait is visible",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The bridge between a released variety and a delivered nutrient. "
            "Orange-fleshed sweet potato achieved substantial adoption through "
            "vine distribution and demand creation; other biofortified "
            "varieties have been released and scarcely planted. A release is "
            "not an outcome."
        ),
    ),
    # =========================================================================
    #  LINK ONE: WHAT IS IN THE GRAIN
    # =========================================================================
    Metric(
        name="Micronutrient concentration",
        symbol="c_nutrient",
        unit="micrograms per gram of dry weight",
        typical="breeding targets are set as an increment above the baseline "
        "variety rather than as an absolute figure",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The first link in the chain and the one routinely reported as "
            "though it were the last. Given on a dry weight basis because "
            "moisture varies with storage and fresh weight figures are not "
            "comparable between studies, which is the same problem "
            "`blue.seaweed_cultivation` records for its own yields."
        ),
    ),
    Metric(
        name="Breeding target increment",
        symbol="dC_target",
        unit="micrograms per gram above the baseline, set per crop and per "
        "population",
        typical="derived by working backwards from a required change in "
        "nutritional status",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The metric that shows the chain being taken seriously. A target is "
            "calculated from the deficiency prevalence, the amount of the crop "
            "actually eaten, the retention through cooking and the "
            "bioavailability, and then set as the content the breeder must "
            "reach. It is the reverse of reporting whatever content a variety "
            "happens to have."
        ),
    ),
    # =========================================================================
    #  LINK TWO: DOES IT SURVIVE THE KITCHEN
    # =========================================================================
    Metric(
        name="Retention through processing and cooking",
        symbol="R_ret",
        unit="per cent of the nutrient remaining after local preparation",
        typical="substantial losses for carotenoids; minerals are not "
        "destroyed but can be lost with discarded fractions",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Must be measured through the ACTUAL local preparation rather than "
            "a standard laboratory procedure, because the losses depend on "
            "whether the food is boiled, fried, sun-dried or fermented. "
            "Carotenoids degrade with heat, light and storage; iron and zinc "
            "are elements and cannot be destroyed, but leave with milling "
            "fractions and cooking water."
        ),
    ),
    # =========================================================================
    #  LINK THREE: IS IT ABSORBED
    # =========================================================================
    Metric(
        name="Bioavailability",
        symbol="B_avail",
        unit="per cent of the ingested nutrient absorbed",
        typical="low for iron and zinc from cereal diets, and higher for "
        "provitamin A from processed orange-fleshed roots",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The link that most often breaks, and the reason a content figure "
            "alone means little. Iron absorption from a high-phytate cereal "
            "diet is a small fraction of what is ingested, so a large increase "
            "in content produces a much smaller increase in absorbed dose."
        ),
    ),
    Metric(
        name="Phytate to mineral molar ratio",
        symbol="PA_Zn",
        unit="molar ratio, dimensionless",
        typical="ratios above roughly 15 for phytate to zinc indicate poor "
        "absorption",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The specific measure of the inhibition above, and the reason "
            "low-phytate breeding is a complement rather than an alternative to "
            "raising content. It also connects this record directly to "
            "`yellow.food_fermentation`, where fermentation degrades phytate "
            "and improves absorption from the same grain without changing the "
            "variety at all."
        ),
    ),
    # =========================================================================
    #  LINK FOUR: IS ENOUGH OF IT EATEN
    # =========================================================================
    Metric(
        name="Contribution to estimated average requirement",
        symbol="f_EAR",
        unit="per cent of the daily requirement supplied by usual consumption",
        typical="the figure biofortification programmes actually target",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Combines content, retention, bioavailability and how much of the "
            "crop a person actually eats. It is the honest summary of the first "
            "four links and the number a programme should be judged on, and it "
            "requires dietary intake data that is frequently the weakest input "
            "in the calculation."
        ),
    ),
    # =========================================================================
    #  LINK FIVE: DID ANYONE GET BETTER
    # =========================================================================
    Metric(
        name="Change in biomarker of nutritional status",
        symbol="dStatus",
        unit="change in serum retinol, ferritin, zinc or haemoglobin",
        typical="the endpoint of an efficacy trial, and the only evidence the "
        "chain held end to end",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The last link and the only one that matters, and it is measured in "
            "very few programmes because a trial in the target population is "
            "far slower and more expensive than the breeding. Where it has been "
            "done, notably for orange-fleshed sweet potato, it is the field's "
            "strongest evidence."
        ),
    ),
    Metric(
        name="Deficiency prevalence in the target population",
        symbol="P_def",
        unit="per cent of the population below the deficiency threshold",
        typical="the figure that justifies a programme and defines its target "
        "population",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Determines where an intervention is worth running at all, since "
            "biofortification reaches people who grow and eat the staple. It is "
            "also how the breeding target in the second group is derived, which "
            "makes it both the starting point and the justification."
        ),
    ),
    # =========================================================================
    #  IS IT WORTH DOING THIS WAY
    # =========================================================================
    Metric(
        name="Cost per disability-adjusted life year averted",
        symbol="C_DALY",
        unit="euro per DALY averted",
        typical="favourable for established biofortified crops, and compared "
        "against supplementation and industrial fortification rather than "
        "against nothing",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The metric that decides between interventions rather than "
            "justifying one. Supplementation and industrial fortification are "
            "both highly cost-effective, so the comparison is not against doing "
            "nothing but against the alternatives, and biofortification's "
            "advantage is reaching populations those alternatives do not."
        ),
    ),
    Metric(
        name="Time from programme start to released variety",
        symbol="t_release",
        unit="years",
        typical="commonly a decade or more for conventional breeding, and "
        "considerably longer where a regulatory approval is required",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Recorded because it shapes how the field is funded. A decade of "
            "donor support before any variety reaches a farmer is a long "
            "commitment for crops and populations that no commercial seed "
            "market serves, and the transgenic route in `history.py` shows what "
            "happens when the interval extends past two decades."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Breeding, then the nutritional chain, then the economic comparison.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "breeders_equation",
    "heritability",
    "bioavailability_ratio",
    "estimated_average_requirement",
    "cost_effectiveness_ratio",
    "mass_balance",
)
