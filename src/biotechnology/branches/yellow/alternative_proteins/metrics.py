# =============================================================================
#  biotechnology.branches.yellow.alternative_proteins.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS REPEAT PURCHASE RATE, AND IT IS NOT A MARKETING FIGURE
#  IN THIS RECORD. IT IS THE ONE THAT DECIDED THE SECTOR.
#
#  Between roughly 2019 and 2023 plant-based meat achieved wide trial and then
#  contracted. Awareness was high, distribution was wide, and people did not
#  buy the products a second time. Every technical metric below was improving
#  through that period. A facet that opened with protein content or texture
#  would describe a field that was succeeding, which is not what happened.
#
#  A WARNING ABOUT PROTEIN CONTENT. It is the number on the front of the pack
#  and the least informative one here. Protein quantity is easy and cheap;
#  quality, meaning the amino acid profile and digestibility, is what
#  nutritional equivalence turns on, and the DIAAS metric below is the honest
#  version. A product can be high in protein and nutritionally inferior to the
#  thing it replaces.
#
#  A NOTE ON THE ENVIRONMENTAL METRICS. They are the strongest quantitative
#  case this record has and they must be read against a NAMED comparator.
#  Against beef the advantage is large and not seriously disputed. Against
#  chicken it is much smaller, and against pulses eaten directly it usually
#  disappears, since the processing is what the product is.
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
    #  THE NUMBER THAT DECIDED THE SECTOR
    # =========================================================================
    Metric(
        name="Repeat purchase rate",
        symbol="R_rep",
        unit="per cent of first-time buyers who buy again",
        typical="the decisive commercial metric, and low enough in plant-based "
        "meat to contract the category despite high trial",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Recorded first because it is what actually happened. Trial rates "
            "were high and awareness was wide while the category contracted, "
            "which means the failure was in the product rather than in the "
            "marketing. Graded REPORTED because the figures are commercial and "
            "not systematically published."
        ),
    ),
    Metric(
        name="Retail price ratio to the animal product",
        symbol="P_ratio",
        unit="dimensionless, product price divided by conventional equivalent",
        typical="above 1 for most plant-based meat, and the second half of the "
        "repeat purchase problem",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Parity is the stated goal of most of the sector and has not been "
            "reached for most products. The comparison is against a commodity "
            "that is inexpensive partly because it is supported, so parity is a "
            "moving target set by agricultural policy rather than by processing "
            "cost."
        ),
    ),
    # =========================================================================
    #  IS IT ACTUALLY THE SAME NUTRITIONALLY
    # =========================================================================
    Metric(
        name="Digestible indispensable amino acid score",
        symbol="DIAAS",
        unit="ratio, dimensionless",
        typical="above 1.0 for animal proteins; commonly 0.6 - 0.9 for single "
        "plant sources and higher for blends",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The honest measure of protein quality and the reason protein "
            "content on a label means little. It accounts for the limiting "
            "amino acid and for digestibility at the end of the small "
            "intestine, and it is why protein blending appears in "
            "`practice.TECHNOLOGIES`: two sources with complementary limiting "
            "amino acids score better together than either alone."
        ),
    ),
    Metric(
        name="Protein content",
        symbol="f_prot",
        unit="per cent by weight",
        typical="matched to the product being replaced",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The number on the front of the pack and the least informative one "
            "here. Quantity is easy and cheap; the entry above is what "
            "nutritional equivalence turns on. A product can be high in protein "
            "and nutritionally inferior to what it replaces."
        ),
    ),
    Metric(
        name="Iron and zinc bioavailability",
        symbol="B_min",
        unit="per cent absorbed relative to the animal-derived form",
        typical="lower from plant matrices, and reduced further by phytate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The reason fortification is not sufficient by itself. Adding iron "
            "raises the declared content and the plant matrix restricts how "
            "much is absorbed, which connects this record to the phytate work "
            "in `yellow.food_fermentation` and to `yellow.biofortification`."
        ),
    ),
    Metric(
        name="Sodium content",
        symbol="c_Na",
        unit="milligrams per hundred grams",
        typical="frequently higher than the product being replaced",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Included because it undermines the health positioning and is a "
            "consequence of the sensory work rather than an oversight: salt is "
            "part of how a plant protein is made to taste like meat. It is a "
            "genuine tension between the two things the products are sold on."
        ),
    ),
    # =========================================================================
    #  DOES IT BEHAVE LIKE THE THING IT REPLACES
    # =========================================================================
    Metric(
        name="Degree of texturisation",
        symbol="DoT",
        unit="ratio of longitudinal to transverse tensile strength",
        typical="above 1 indicates anisotropy; higher values approach muscle",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The quantitative handle on fibrousness and the core output of "
            "extrusion. Meat is anisotropic because it is made of aligned "
            "fibres, and a value near 1 describes a homogeneous paste however "
            "good its composition. It is the one place where the materials "
            "engineering in this record becomes measurable."
        ),
    ),
    Metric(
        name="Cooking loss",
        symbol="L_cook",
        unit="per cent mass lost during a standard cooking procedure",
        typical="benchmarked against the meat product being replaced",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Determines whether a product shrinks, dries or falls apart in a "
            "pan, which is what a consumer experiences directly. It depends "
            "heavily on how the fat phase is structured, which is why fat "
            "structuring has its own technology group."
        ),
    ),
    Metric(
        name="Water holding capacity",
        symbol="WHC",
        unit="grams of water retained per gram of protein",
        typical="matched to the reference product",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Underlies juiciness, which is among the first attributes a "
            "consumer comments on and among the hardest to specify. It "
            "interacts with cooking loss: a product that holds water well "
            "before cooking and releases it under heat is worse than one that "
            "holds less throughout."
        ),
    ),
    # =========================================================================
    #  WHAT IT SAVES, AGAINST A NAMED COMPARATOR
    # =========================================================================
    Metric(
        name="Greenhouse gas intensity",
        symbol="GWP",
        unit="kilograms of carbon dioxide equivalent per kilogram of protein",
        formula="carbon_intensity",
        typical="much lower than beef, moderately lower than chicken, and "
        "similar to or higher than the pulses the protein came from",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The strongest quantitative case in this record and it must be read "
            "against a NAMED comparator. Against beef the advantage is large "
            "and not seriously disputed. Against chicken it narrows "
            "considerably. Against pulses eaten directly it usually disappears, "
            "because the processing is what the product is."
        ),
    ),
    Metric(
        name="Land use per kilogram of protein",
        symbol="A_land",
        unit="square metres per kilogram",
        typical="substantially lower than ruminant meat; near zero for "
        "gas-fermented protein",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The clearest argument in the record, since livestock occupies most "
            "agricultural land for a minority of calories. Gas-fermented "
            "protein is the extreme case and requires no farmland at all, which "
            "is why it appears in `practice.APPLICATIONS` despite being "
            "commercially marginal."
        ),
    ),
    Metric(
        name="Feed conversion ratio",
        symbol="FCR",
        unit="kilograms of feed per kilogram of edible product",
        formula="feed_conversion_ratio",
        typical="far more favourable for insects and fungi than for livestock",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Applies to the insect and single-cell routes and is where their "
            "case rests. It should be read with the same caution "
            "`blue.aquaculture_biotechnology` records: wet weight comparisons "
            "flatter, and the edible fraction differs greatly between an insect "
            "and a bullock."
        ),
    ),
    # =========================================================================
    #  THE CLASSIFICATION THAT BECAME A LIABILITY
    # =========================================================================
    Metric(
        name="Degree of processing classification",
        symbol="C_proc",
        unit="NOVA or equivalent classification category",
        typical="most formulated analogues classify as ultra-processed",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Recorded as a metric because it became a commercial fact rather "
            "than an academic one. The classification is a fair description of "
            "how the texture is achieved, and it placed these products in a "
            "category consumers were being advised to avoid. Graded REPORTED "
            "because the classification itself is contested as a guide to "
            "healthfulness."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Nutrition and conversion first, then the environmental assessment.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "protein_digestibility_score",
    "feed_conversion_ratio",
    "carbon_intensity",
    "life_cycle_impact",
    "mass_balance",
    "water_activity",
)
