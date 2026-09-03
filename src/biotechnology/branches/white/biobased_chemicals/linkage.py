# =============================================================================
#  biotechnology.branches.white.biobased_chemicals.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The most useful edge here is the one to `white.biofuels`, and it should be
#  read as a comparison rather than as a cross-reference.
#
#  The two records share their feedstocks, their organisms, their vessels and
#  much of their engineering. They differ in the target molecule, and that
#  single difference decides almost everything:
#
#      biofuels             the target is a hydrocarbon, so oxygen must be
#                           stripped out of an oxygen-rich feedstock, wasting
#                           carbon. Low value per tonne, enormous volume, and
#                           a market that exists because a legislature created
#                           it.
#      biobased_chemicals   the target is usually oxygen-rich, so the feedstock
#                           starts most of the way there. Higher value per
#                           tonne, smaller volume, and a market that already
#                           exists and simply has to be won on price.
#
#  A reader who follows this edge should come away understanding why the same
#  science reads as disappointment in one record and as modest steady progress
#  in the other.
#
#  `white.biopolymers` is downstream: lactic acid becomes polylactic acid, the
#  diols become polyesters, and the boundary is drawn at polymerisation.
#
#  `purple.biotechnology_patents` is included because it genuinely binds here.
#  A designed pathway to a known commodity molecule is protected by process and
#  strain patents rather than by composition of matter, since the molecule
#  itself is old and unpatentable. That makes the intellectual property
#  position of a biobased commodity producer structurally weaker than that of a
#  novel-molecule producer, and it is part of why the platform chemical
#  business proved hard.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three. Goal 12 is the primary claim and the one this record can actually
#  support: the carbon in a material is displaced permanently rather than
#  burned, so the substitution is durable in a way that fuel substitution is
#  not.
#
#  Goal 13 is claimed with the qualification recorded in `metrics.py`, that a
#  biobased route is not automatically lower in greenhouse gas intensity and
#  must be measured against a named benchmark.
# =============================================================================
SDGS: Tuple[int, ...] = (
    9,  # Industry and innovation, on feedstock substitution in manufacturing
    12,  # Responsible production, the primary and best-supported claim
    13,  # Climate action, subject to a benchmarked life cycle assessment
)


# =============================================================================
#  GLOSSARY
#  Grouped: the strategic vocabulary, the molecules themselves, the recovery
#  problem, then the vocabulary of proving the claim.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- how the field thinks about itself -------------------------------------
    "biobased_chemical",
    "platform_chemical",
    "drop_in_chemical",
    "biorefinery",
    "bioeconomy",
    "feedstock",
    "value_pyramid",
    # -- the property that predicts success ------------------------------------
    "oxygen_to_carbon_ratio",
    "degree_of_reduction",
    "carbon_yield",
    # -- the molecules ---------------------------------------------------------
    "lactic_acid",
    "succinic_acid",
    "propanediol",
    "butanediol",
    "furandicarboxylic_acid",
    "levulinic_acid",
    "itaconic_acid",
    "glycerol",
    "lignin",
    # -- getting it out of the water -------------------------------------------
    "product_recovery",
    "reactive_extraction",
    "electrodialysis",
    "crystallisation",
    "in_situ_product_removal",
    # -- proving the claim -----------------------------------------------------
    "biobased_carbon_content",
    "radiocarbon_dating",
    "life_cycle_assessment",
    "techno_economic_analysis",
    "minimum_selling_price",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "doe_top_value_added_chemicals",
    "top_chemicals_revisited_review",
    "biobased_succinic_acid_market_analysis",
    "propanediol_commercial_process",
    "butanediol_designed_pathway",
    "organic_acid_recovery_review",
    "astm_d6866_biobased_carbon",
    "biorefinery_technoeconomic_review",
    "lignin_valorisation_review",
    "oecd_bioeconomy_2030",
)


# =============================================================================
#  RELATED
#  Seven edges. The first is a comparison, not a cross-reference.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same science with a different target molecule ---------------------
    "white.biofuels",
    # -- who builds the pathway ------------------------------------------------
    "white.metabolic_engineering",
    # -- the enzymatic rather than fermentative route --------------------------
    "white.biocatalysis",
    # -- the vessel and the separation train -----------------------------------
    "white.bioprocess_engineering",
    # -- where these molecules go next -----------------------------------------
    "white.biopolymers",
    # -- feedstock design and its land constraint ------------------------------
    "green.plant_genetic_engineering",
    # -- why protecting a commodity molecule is structurally hard --------------
    "purple.biotechnology_patents",
)
