# =============================================================================
#  biotechnology.branches.yellow.alternative_proteins.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Three edges are comparisons rather than pointers and each clarifies what
#  this record is.
#
#  `yellow.precision_fermentation` makes a COPY of an animal molecule; this
#  record makes a DESCRIPTION of an animal product. They compete for the same
#  shelf and solve different problems, and a reader treating them as one
#  category will misread both. The two also cooperate: the heme protein that
#  gives plant-based meat its character is a precision fermentation product.
#
#  `yellow.cultivated_meat` is the third answer to the same question, and the
#  three form a spectrum by how much of the animal is retained: none here, one
#  molecule there, the actual cells in the third. Cost and regulatory burden
#  rise in the same order, and so does the strength of the claim to be the
#  thing rather than a version of it.
#
#  `green.animal_biotechnology` is the incumbent this record competes with, and
#  the edge is deliberate. That record documents efficiency gains in livestock
#  that are real and continuing, which means the comparator is improving rather
#  than static, and an environmental claim measured against 1990s livestock
#  performance overstates the advantage.
#
#  `white.biopolymers` is included for a specific technical reason: extrusion
#  and the anisotropy it produces are the same materials engineering, and a
#  reader interested in how a globular protein is made fibrous will find the
#  polymer processing vocabulary there.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and one of them is claimed with an explicit reservation.
#
#  Goal 15, life on land, is the strongest claim this record has and is rarely
#  the one made for it. Livestock occupies most agricultural land for a
#  minority of calories, so displacing part of that reduces pressure on land
#  directly, and the deforestation link through soy cuts both ways and is
#  addressed in `governance.py` through the supply chain condition.
#
#  Goal 13 is claimed against ruminant meat specifically, which is the
#  comparison `metrics.py` says is not seriously disputed, and NOT as a general
#  climate benefit, since against chicken the advantage narrows and against
#  pulses eaten directly it disappears.
#
#  GOAL 3 IS DELIBERATELY NOT CLAIMED, although displacing red meat has health
#  benefits. This record's own metrics show sodium frequently higher than the
#  product replaced and mineral bioavailability lower, and the ultra-processed
#  classification is a fair description rather than a misunderstanding. The
#  health case is genuinely two-sided and claiming the goal would report one
#  side of it.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on protein supplied at lower resource cost
    12,  # Responsible production, on feed conversion and side-stream use
    13,  # Climate action, against ruminant meat specifically
    15,  # Life on land, on agricultural land pressure, the strongest claim
)


# =============================================================================
#  GLOSSARY
#  Grouped: the sources, the structure problem, the nutrition vocabulary, and
#  what the market measures.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the sources -----------------------------------------------------------
    "plant_protein",
    "mycoprotein",
    "single_cell_protein",
    "insect_protein",
    "protein_isolate",
    "protein_concentrate",
    # -- the structure problem, which is the engineering -----------------------
    "extrusion",
    "high_moisture_extrusion",
    "texturisation",
    "anisotropy",
    "shear_cell_processing",
    "mycelium",
    "oleogel",
    "fat_structuring",
    # -- flavour ---------------------------------------------------------------
    "maillard_reaction",
    "heme_protein",
    "off_flavour",
    "sensory_analysis",
    # -- the nutrition vocabulary ----------------------------------------------
    "amino_acid_profile",
    "limiting_amino_acid",
    "protein_digestibility",
    "bioavailability",
    "antinutritional_factor",
    "fortification",
    # -- what the market measures ----------------------------------------------
    "repeat_purchase",
    "price_parity",
    "ultra_processed_food",
    "feed_conversion_ratio",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "alternative_protein_sector_review",
    "high_moisture_extrusion_review",
    "mycoprotein_safety_and_history",
    "plant_based_meat_market_contraction",
    "diaas_protein_quality_methodology",
    "protein_environmental_footprint_comparison",
    "insect_protein_feed_authorisation",
    "ultra_processed_food_classification_debate",
    "novel_food_regulation_eu",
    "dairy_denomination_ruling",
)


# =============================================================================
#  RELATED
#  Seven edges. The first three are the spectrum of answers to one question.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- a copy of the molecule, against a description of the product ----------
    "yellow.precision_fermentation",
    # -- the third answer, retaining the animal's cells ------------------------
    "yellow.cultivated_meat",
    # -- the incumbent, which is itself improving ------------------------------
    "green.animal_biotechnology",
    # -- fungal biomass production, the fermentation half of this record -------
    "white.microbial_fermentation",
    # -- extrusion and anisotropy as materials engineering ---------------------
    "white.biopolymers",
    # -- where insect meal actually goes, and the fishmeal it displaces --------
    "blue.aquaculture_biotechnology",
    # -- the crops the protein is extracted from -------------------------------
    "green.molecular_plant_breeding",
)
