# =============================================================================
#  biotechnology.branches.yellow.food_fermentation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The edge to `yellow.precision_fermentation` is the one that carries the most
#  information in this branch, and it should be read as a comparison.
#
#  Both records use microorganisms to make food. The biology is continuous
#  between them and the governance is not:
#
#      food_fermentation        transforms a food that already existed. History
#                               of consumption exempts it, so the product needs
#                               no authorisation.
#                               REGULATORY_STATUS = UNREGULATED
#      precision_fermentation   makes a specific molecule that the organism was
#                               engineered to produce. No consumption history,
#                               so novel food authorisation applies in full.
#                               REGULATORY_STATUS = AUTHORISED
#
#  A reader following that edge learns that a great deal of food regulation
#  turns on FAMILIARITY rather than on hazard, which is a fact about the
#  regulatory system worth knowing before judging either record.
#
#  `white.microbial_fermentation` is the same unit operation with a different
#  objective. There the product is recovered from the broth and the broth is
#  discarded; here the broth IS the product. That single difference removes the
#  entire downstream separation problem that governs the white record's
#  economics, and it is why a dairy is not a bioprocess plant.
#
#  `blue.seaweed_cultivation` is included for a specific reason: agar reached
#  microbiology from a fermented-food tradition, and both records document a
#  craft that a science later explained.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and two of them rest on mechanisms that are easy to overlook.
#
#  Goal 2 is claimed on preservation without a cold chain and on cassava
#  detoxification, not on production volume. Fermentation keeps food edible
#  where refrigeration does not exist, and it makes a staple crop safe for
#  hundreds of millions of people. Both are food security in the literal sense.
#
#  Goal 3 is claimed on phytate reduction improving iron and zinc absorption,
#  which addresses the same deficiencies `yellow.biofortification` attacks from
#  the crop end, and it does so with no new variety and no supplement.
#
#  GOAL 13 IS DELIBERATELY NOT CLAIMED. Fermentation reduces food waste, which
#  has a climate benefit, and the connection runs through enough steps that it
#  would not survive the sceptical-auditor test in rule 12. Goal 12 covers the
#  waste reduction directly and honestly.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on preservation without a cold chain and detoxification
    3,  # Health, on mineral bioavailability and on digestibility
    11,  # Sustainable communities, on food traditions as cultural heritage
    12,  # Responsible production, on food preserved rather than wasted
)


# =============================================================================
#  GLOSSARY
#  Grouped: the process, the organisms, the safety barrier, and the products.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the process -----------------------------------------------------------
    "fermentation",
    "starter_culture",
    "backslopping",
    "spontaneous_fermentation",
    "microbial_succession",
    "adjunct_culture",
    "koji",
    "ripening",
    # -- the organisms ---------------------------------------------------------
    "lactic_acid_bacteria",
    "yeast",
    "acetic_acid_bacteria",
    "filamentous_fungus",
    "bacteriophage",
    "qualified_presumption_of_safety",
    # -- the safety barrier ----------------------------------------------------
    "acidification",
    "water_activity",
    "hurdle_technology",
    "critical_control_point",
    "biogenic_amine",
    "mycotoxin",
    # -- what changes in the food ----------------------------------------------
    "proteolysis",
    "lipolysis",
    "phytate",
    "cyanogenic_glycoside",
    "volatile_compound",
    "probiotic",
    # -- who owns the name -----------------------------------------------------
    "protected_designation_of_origin",
    "traditional_food",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "fermented_foods_review",
    "jiahu_fermented_beverage_residues",
    "pasteur_fermentation_1857",
    "dairy_starter_bacteriophage_review",
    "cassava_fermentation_detoxification",
    "phytate_reduction_fermentation",
    "traditional_fermented_food_microbiomes",
    "codex_fermented_milks_standard",
    "qps_microorganisms_list",
    "protected_designation_origin_regulation",
)


# =============================================================================
#  RELATED
#  Six edges. The first is a comparison rather than a cross-reference.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same biology, the opposite regulatory position --------------------
    "yellow.precision_fermentation",
    # -- the same unit operation, with the broth discarded rather than eaten ---
    "white.microbial_fermentation",
    # -- the enzymes that make koji, cheese and baking work --------------------
    "white.industrial_enzymes",
    # -- the acid barrier extended deliberately into a preservation technology -
    "yellow.food_biopreservation",
    # -- what the organisms do after they are eaten ----------------------------
    "yellow.probiotics_and_prebiotics",
    # -- the same deficiencies attacked from the crop end ----------------------
    "yellow.biofortification",
)
