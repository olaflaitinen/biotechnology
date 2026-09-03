# =============================================================================
#  biotechnology.branches.white.microbial_fermentation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has more inbound dependencies than any other in the white
#  branch. Three completed records already point here because their products
#  are physically made in a fermenter, and the edges below are therefore
#  written as a division of labour rather than as a reading list.
#
#      metabolic_engineering   builds the strain and measures it
#      microbial_fermentation  grows the strain and measures the cultivation
#      bioprocess_engineering  designs the vessel and takes the product out
#
#  The boundary with the third is the one most easily blurred. Oxygen transfer
#  appears in both records and means different things: here it is a demand the
#  culture makes, there it is a capability the vessel supplies. kLa is a
#  property of the equipment; the oxygen uptake rate is a property of the
#  organism; a process works when the first exceeds the second. Splitting them
#  across two records is deliberate, because in practice they are the
#  responsibility of two different engineers.
#
#  `yellow.precision_fermentation` is a genuinely new edge rather than a
#  restatement. The operation is the same, and what differs is that the product
#  is a food protein and the governing questions become novel food
#  authorisation, allergen labelling and consumer acceptance.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and Goal 6 is the one that is easy to miss in the wrong direction.
#  Fermentation is water-intensive and produces a large organic effluent, so
#  Goal 6 is claimed on the treatment and reuse practice the industry has been
#  obliged to develop, not on the process being inherently clean. Recording it
#  this way is the honest version.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on feed amino acids and animal-free protein
    3,  # Health, on antibiotics and recombinant medicines
    6,  # Clean water, on effluent treatment and water reuse obligations
    9,  # Industry and innovation, as the manufacturing base of the branch
)


# =============================================================================
#  GLOSSARY
#  Grouped: the modes of operation, the sterility vocabulary, the transfer and
#  kinetics vocabulary, then the terms specific to running a plant.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- how it is run ---------------------------------------------------------
    "fermentation",
    "batch_culture",
    "fed_batch_culture",
    "continuous_culture",
    "chemostat",
    "solid_state_fermentation",
    "inoculum",
    "seed_train",
    # -- keeping everything else out -------------------------------------------
    "sterilisation",
    "aseptic_technique",
    "contamination",
    "bacteriophage",
    "sterility_assurance_level",
    "cell_bank",
    # -- transfer and kinetics -------------------------------------------------
    "oxygen_transfer_coefficient",
    "dissolved_oxygen",
    "respiratory_quotient",
    "specific_growth_rate",
    "monod_kinetics",
    "maintenance_energy",
    "overflow_metabolism",
    "crabtree_effect",
    # -- running the plant -----------------------------------------------------
    "bioreactor",
    "impeller",
    "sparger",
    "antifoam",
    "off_gas_analysis",
    "process_analytical_technology",
    "turnaround_time",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "bioprocess_engineering_principles",
    "penicillin_deep_tank_history",
    "monod_growth_kinetics",
    "chemostat_theory_paper",
    "overflow_metabolism_review",
    "single_cell_protein_pruteen_review",
    "oxygen_transfer_scale_up_review",
    "sterilisation_kinetics_reference",
    "single_use_bioreactor_assessment",
    "gas_fermentation_commercial_review",
)


# =============================================================================
#  RELATED
#  Seven edges. The first two are the division of labour described above.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- what is grown here, and who built it ----------------------------------
    "white.metabolic_engineering",
    # -- the vessel that supplies what the culture demands ---------------------
    "white.bioprocess_engineering",
    # -- the largest single class of product made this way ---------------------
    "white.industrial_enzymes",
    # -- medicines made in a fermenter -----------------------------------------
    "red.pharmaceutical_biotechnology",
    # -- the bulk chemical and fuel products -----------------------------------
    "white.biobased_chemicals",
    "white.biofuels",
    # -- the same operation with a food product and a food regulator -----------
    "yellow.precision_fermentation",
)
