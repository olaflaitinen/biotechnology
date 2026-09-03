# =============================================================================
#  biotechnology.branches.yellow.food_biopreservation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS A LOG REDUCTION MEASURED IN THE ACTUAL FOOD, AND THE
#  QUALIFICATION IS THE POINT.
#
#  Almost every published figure for a biopreservative is generated in broth,
#  where a peptide meets its target unimpeded. In a food it meets fat, protein,
#  a solid matrix and a resident flora, and the reduction achieved is
#  frequently far smaller. A record reporting broth activity as though it were
#  performance would repeat the field's most common overstatement.
#
#  THE SECOND METRIC IS WHY THE FIRST IS RARELY ENOUGH. Listeria
#  monocytogenes grows at refrigeration temperature, so a reduction that is not
#  sustained is a delay rather than a control. Preventing growth over the whole
#  shelf life is a different requirement from killing organisms once, and it is
#  the requirement regulation actually imposes on ready-to-eat food.
#
#  A NOTE ON UNITS. Bacteriocin activity is quoted in international units
#  rather than in mass, because preparations vary in purity and because the
#  unit is defined by an inhibition assay. Two products with the same declared
#  mass of nisin may differ in activity, which is why the unit exists.
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
    #  DOES IT WORK IN THE FOOD, NOT IN A TUBE
    # =========================================================================
    Metric(
        name="Log reduction in the food matrix",
        symbol="dlog_N",
        unit="log10 reduction in target organism count",
        typical="1 - 3 log10 in a real food, and frequently higher in broth",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The qualification carries the whole entry. Broth figures overstate "
            "food performance because fat and protein bind antimicrobial "
            "peptides and a solid matrix restricts diffusion. A biopreservative "
            "reported at five logs in vitro may deliver one in a sausage, and "
            "the difference is not a failure of the agent but a property of "
            "food."
        ),
    ),
    Metric(
        name="Growth inhibition over shelf life",
        symbol="dN_shelf",
        unit="log10 increase in target organism permitted over the stated "
        "shelf life",
        typical="regulatory expectation for ready-to-eat foods is that "
        "Listeria does not exceed a defined limit at the end of shelf life",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The requirement that matters more than the entry above. Listeria "
            "grows at refrigeration temperature, so killing organisms once is a "
            "delay and preventing growth throughout is control. This is what "
            "regulation actually imposes on ready-to-eat food, and it is why a "
            "single log reduction figure is an incomplete answer."
        ),
    ),
    Metric(
        name="Shelf life extension",
        symbol="dt_shelf",
        unit="days added before spoilage or the microbiological limit is "
        "reached",
        typical="days to weeks depending on product and hurdle set",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The commercial metric and the one that justifies the cost. It is "
            "also the food waste argument in `linkage.py` made quantitative, "
            "since a few extra days on a chilled product changes how much is "
            "thrown away at retail and at home."
        ),
    ),
    # =========================================================================
    #  HOW MUCH AGENT, AND HOW ACTIVE
    # =========================================================================
    Metric(
        name="Bacteriocin activity",
        symbol="A_bac",
        unit="international units per gram of food",
        typical="permitted nisin levels are set by food category in the "
        "additive legislation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Quoted in activity units rather than in mass because preparations "
            "differ in purity and because the unit is defined by an inhibition "
            "assay against a reference organism. Two products declaring the "
            "same mass of nisin can differ in delivered activity, which is why "
            "the unit exists and why a mass figure alone is not a "
            "specification."
        ),
    ),
    Metric(
        name="Minimum inhibitory concentration",
        symbol="MIC",
        unit="micrograms per millilitre or international units per millilitre",
        typical="determined against the specific target strain",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Strain-specific and determined in a defined medium, so it "
            "establishes the agent's intrinsic potency and not the dose needed "
            "in a product. The gap between MIC and the effective in-food dose "
            "is the matrix effect, and it is frequently an order of magnitude "
            "or more."
        ),
    ),
    Metric(
        name="Protective culture inoculum level",
        symbol="N_prot",
        unit="colony forming units per gram at application",
        typical="10^6 - 10^7 CFU/g",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A live culture must be present in sufficient number to compete, "
            "and as `yellow.probiotics_and_prebiotics` insists in its own "
            "context, a count is not an effect. What is being bought here is "
            "competition for nutrients and surfaces, so the relevant question "
            "is whether the culture outnumbers and outgrows the contaminant at "
            "the storage temperature."
        ),
    ),
    # =========================================================================
    #  THE PHAGE-SPECIFIC MEASURES
    # =========================================================================
    Metric(
        name="Phage application titre",
        symbol="T_phage",
        unit="plaque forming units per square centimetre or per gram",
        typical="10^7 - 10^9 PFU applied to a surface",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "High titres are required because phage and host must physically "
            "meet, and in a solid food neither diffuses. This is why phage "
            "products are applied to surfaces rather than mixed through a "
            "product, and why they suit processing environments as well as "
            "foods."
        ),
    ),
    Metric(
        name="Host range",
        symbol="R_host",
        unit="per cent of target strains susceptible to the preparation",
        typical="broadened by using a cocktail of several phages",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The double-edged property of phage biocontrol. Specificity means "
            "the resident and starter flora are untouched, which is a real "
            "advantage, and it also means a preparation may miss the particular "
            "strain contaminating a particular batch. Cocktails widen the range "
            "and delay resistance at once."
        ),
    ),
    Metric(
        name="Resistance emergence frequency",
        symbol="f_res",
        unit="proportion of the target population resistant after exposure",
        typical="measurable for both bacteriocins and phages, and the reason "
        "cocktails and hurdle combinations are used",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Recorded explicitly because the field has been slower than "
            "clinical microbiology to say plainly that these are antimicrobials "
            "under the same evolutionary pressure as any other. Nisin "
            "resistance in Listeria is documented, and phage resistance arises "
            "readily against a single phage."
        ),
    ),
    # =========================================================================
    #  DID THE FOOD STAY THE SAME
    # =========================================================================
    Metric(
        name="Sensory change from the untreated control",
        symbol="dS_sens",
        unit="difference score in a trained panel discrimination test",
        typical="the requirement is no detectable difference",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The performance requirement that distinguishes this record from "
            "`yellow.food_fermentation`. A protective culture that acidifies "
            "the product perceptibly has failed even if the food is safe, "
            "because the whole proposition is that nothing changes except the "
            "shelf life."
        ),
    ),
    # =========================================================================
    #  WHETHER THE BARRIER ACTUALLY HOLDS
    # =========================================================================
    Metric(
        name="Challenge test outcome",
        symbol="C_chal",
        unit="qualitative, whether the deliberately inoculated pathogen is "
        "controlled through shelf life including abuse conditions",
        typical="the only acceptable evidence for a safety claim",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Deliberate inoculation of the actual product, stored under the "
            "intended conditions and under reasonable temperature abuse. No "
            "combination of the metrics above substitutes for it, because "
            "hurdle interactions are not additive and cannot be predicted from "
            "the components."
        ),
    ),
    Metric(
        name="Water activity and pH of the hurdle set",
        symbol="a_w_pH",
        unit="dimensionless pair",
        formula="water_activity",
        typical="recorded together, since the biological agent is one barrier "
        "among several",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Included because a biopreservation figure quoted without the rest "
            "of the hurdle set is uninterpretable. The same nisin "
            "concentration performs differently at pH 5.5 and pH 6.5, and the "
            "hurdles interact rather than add."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  The inhibition and growth relationships, then the barrier measures.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "dose_response",
    "specific_growth_rate",
    "thermal_death_kinetics",
    "water_activity",
    "arrhenius_equation",
    "serial_dilution",
)
