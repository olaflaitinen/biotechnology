# =============================================================================
#  biotechnology.branches.green.biopesticides.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two edges here are more than cross-references; each explains something this
#  record cannot explain on its own.
#
#  `green.plant_genetic_engineering` uses the SAME PROTEIN. The Bt cry genes
#  sprayed as a product since 1938 are the genes moved into maize and cotton in
#  1987. That has a consequence recorded in both records: deploying one protein
#  as a spray and as a transgene across the same landscape doubles the
#  selection pressure on the same resistance allele, and field-evolved Bt
#  resistance followed exactly where that happened without enforced refuges.
#  Neither record is complete without the other.
#
#  `green.biofertilisers` is separated from this record by a line drawn on a
#  label rather than in biology. The same Bacillus strain is a fertilising
#  product sold for root growth and a plant protection product sold for
#  pathogen suppression, at one to two orders of magnitude more dossier cost.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, which is more than most records in this library claim, and each is
#  supported by a distinct mechanism rather than by the same one restated.
#  Goal 3 is included on occupational exposure specifically: much of the
#  world's insecticide is applied by hand without protective equipment, and
#  acute pesticide poisoning is a substantial occupational health burden.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on crop loss avoided where resistance has defeated chemistry
    3,  # Good health and well-being, on occupational exposure and on residues
    12,  # Responsible consumption and production, on displaced synthetic load
    15,  # Life on land, on pollinators and natural enemies spared
)


# =============================================================================
#  GLOSSARY
#  Grouped as the DESCRIPTION uses them: the agents, how they act, how they are
#  deployed, and how their use is judged.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- the agents ----------------------------------------------------------
    "biopesticide",
    "entomopathogen",
    "baculovirus",
    "parasitoid",
    "natural_enemy",
    # ---- how they act ---------------------------------------------------------
    "cry_protein",
    "midgut_activation",
    "cuticle_penetration",
    "rna_interference",
    "pheromone",
    "mating_disruption",
    "competitive_exclusion",
    "induced_resistance",
    # ---- how they are deployed --------------------------------------------------
    "augmentative_release",
    "classical_biological_control",
    "sterile_insect_technique",
    # ---- how their use is judged -------------------------------------------------
    "integrated_pest_management",
    "economic_threshold",
    "non_target_organism",
    "pre_harvest_interval",
    "refuge",
)


# =============================================================================
#  REFERENCES
#  The isolation, the mechanism that explains the selectivity, the standard
#  modern review, and the efficacy evaluation standard.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "ishiwata1901",  # isolation of the organism, from a silkworm epidemic
    "bravo2011",  # the Bt mechanism, and why it is selective
    "lacey2015",  # the standard modern review of insect pathogens as agents
    "eppo_efficacy",  # the efficacy evaluation standards
)


# =============================================================================
#  RELATED
#  Seven edges. The first two are the ones explained in the header note.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the same protein, delivered by the plant instead of a sprayer -------
    "green.plant_genetic_engineering",
    # ---- separated from this record by a label claim, not by biology ---------
    "green.biofertilisers",
    # ---- where sequence-based selectivity comes from -------------------------
    "green.agricultural_genome_editing",
    # ---- how the agents are produced at scale --------------------------------
    "white.microbial_fermentation",
    # ---- monitoring pest populations and detecting resistance alleles --------
    "grey.environmental_biomonitoring",
    "yellow.food_safety_biotechnology",
    # ---- the ecosystem the whole proposition is about protecting -------------
    "grey.biodiversity_conservation",
)
