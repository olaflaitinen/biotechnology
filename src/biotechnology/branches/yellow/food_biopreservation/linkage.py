# =============================================================================
#  biotechnology.branches.yellow.food_biopreservation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `yellow.food_fermentation` is the reciprocal edge and the distinction is
#  intent rather than mechanism. There the microbes TRANSFORM the food and
#  preservation is one of four things happening; here they PROTECT it and are
#  meant to change nothing else. The same acid, produced by the same organisms,
#  is a defining feature in one record and a failure in the other.
#
#  `green.biopesticides` is the cross-branch edge that carries the most, and it
#  is close enough that the arguments transfer almost intact. Both records
#  deploy biological agents against a target organism, both are narrow in
#  spectrum by design, both work as one component of an integrated set of
#  measures rather than alone, both face resistance, and both are marketed on a
#  natural framing that their regulatory status does not always support. A
#  reader who has understood integrated pest management has understood hurdle
#  technology.
#
#  `red.pharmaceutical_biotechnology` holds phage therapy, and the edge exists
#  because the two applications share a technology and diverge on evidence
#  requirements entirely. A phage preparation on a food surface and a phage
#  administered to a patient are the same biology under regimes that could not
#  be further apart.
#
#  `dark.biosurveillance` is included because the resistance monitoring this
#  record admits it lacks is the same activity that record is built around, and
#  the 1999 nisin finding is an argument for it.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and Goal 12 is the strongest and least obvious.
#
#  Responsible production is claimed on food waste, which is the largest
#  quantitative effect in this record. Roughly a third of food produced is lost
#  or wasted, spoilage is a substantial part of that, and shelf life extension
#  reduces it without requiring anyone to change their behaviour. Very few
#  interventions in this library have that property.
#
#  Goal 3 is claimed on Listeria specifically rather than on food safety
#  generally. The organism grows at refrigeration temperature, contaminates
#  after cooking, and has a high case fatality rate, and this record's central
#  purpose is controlling it in the finished product.
#
#  Goal 2 is claimed narrowly on the lactoperoxidase system for raw milk where
#  no cold chain exists, which is a specific and documented application rather
#  than a general food security argument.
#
#  GOAL 13 IS DELIBERATELY NOT CLAIMED. Reduced food waste has a climate
#  benefit and the connection runs through enough steps that it would not
#  survive the sceptical-auditor test. Goal 12 covers the waste directly and
#  honestly.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, narrowly, on milk preservation without a cold chain
    3,  # Health, on Listeria control in ready-to-eat food
    12,  # Responsible production, on food waste, the strongest claim here
)


# =============================================================================
#  GLOSSARY
#  Grouped: the agents, the framework, the targets, and how efficacy is proved.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the agents ------------------------------------------------------------
    "biopreservation",
    "bacteriocin",
    "nisin",
    "protective_culture",
    "bacteriophage",
    "lysozyme",
    "lactoperoxidase_system",
    "antimicrobial_peptide",
    # -- the framework ---------------------------------------------------------
    "hurdle_technology",
    "water_activity",
    "competitive_exclusion",
    "shelf_life",
    "minimum_inhibitory_concentration",
    "log_reduction",
    # -- the targets -----------------------------------------------------------
    "listeria_monocytogenes",
    "clostridium_botulinum",
    "spoilage_organism",
    "gram_positive",
    "gram_negative",
    "antimicrobial_resistance",
    # -- how it is proved and classified ---------------------------------------
    "challenge_testing",
    "predictive_microbiology",
    "food_additive",
    "processing_aid",
    "clean_label",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "nisin_food_preservation_review",
    "hurdle_technology_leistner",
    "listeria_ready_to_eat_criteria",
    "protective_cultures_review",
    "bacteriophage_biocontrol_food",
    "nisin_resistance_listeria",
    "bacteriocin_matrix_effects",
    "challenge_testing_guidance",
    "nitrite_reduction_cured_meat",
    "food_waste_and_shelf_life",
)


# =============================================================================
#  RELATED
#  Six edges. The second is the parallel whose arguments transfer intact.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same organisms, the opposite intent -------------------------------
    "yellow.food_fermentation",
    # -- the same arguments in agriculture: narrow agents, integrated sets -----
    "green.biopesticides",
    # -- the same phages, under an entirely different evidence regime ----------
    "red.pharmaceutical_biotechnology",
    # -- detecting the pathogens this record is meant to control ---------------
    "yellow.food_safety_biotechnology",
    # -- the enzymes used as antimicrobials ------------------------------------
    "white.industrial_enzymes",
    # -- the resistance monitoring this record admits it lacks -----------------
    "dark.biosurveillance",
)
