# =============================================================================
#  biotechnology.branches.yellow.food_safety_biotechnology.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `red.molecular_diagnostics` holds the methods, and the division is worth
#  stating because a reader could reasonably ask why this record exists.
#
#      red.molecular_diagnostics    the method, and a clinical sample. One
#                                   patient, a sample that is mostly the target
#                                   organism's environment, and a result that
#                                   informs a treatment decision.
#      yellow.food_safety_...       the same method against food. A few hundred
#                                   grams from a consignment of tonnes, a
#                                   matrix that actively inhibits the assay, and
#                                   a result that creates a LEGAL DUTY to
#                                   withdraw product.
#
#  What is specific here is the sampling statistics, the matrix and the
#  consequence, none of which the clinical record faces.
#
#  `yellow.food_biopreservation` is the reciprocal of a control loop. That
#  record exists to keep Listeria from growing in ready-to-eat food; this one
#  measures whether it did. Neither is meaningful without the other, and the
#  end-of-shelf-life criterion is the specification they share.
#
#  `dark.biosurveillance` is the closest structural parallel in the library.
#  Both are detection systems for rare events with severe consequences, both
#  have discovered that detection capacity now exceeds response capacity, and
#  both face the same interpretive problem of what a genomic cluster means. The
#  arguments transfer.
#
#  `purple.genetic_data_privacy` is included for a specific and unresolved
#  reason: cross-border outbreak investigation shares sequences derived from
#  identified patients, which is a genuine tension between surveillance and
#  data protection rather than a formality.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and Goal 3 is the primary claim with unusually direct evidence.
#
#  Good health is claimed on prevented illness rather than on capability.
#  Foodborne disease affects a very large number of people annually and kills a
#  substantial number, and detection before release prevents cases rather than
#  documenting them. Genomic surveillance has located contaminated sites that
#  would otherwise have continued producing.
#
#  Goal 12 is claimed with a qualification that cuts both ways. Better
#  detection prevents contaminated product reaching consumers, and it also
#  causes precautionary destruction of product that was probably safe, because
#  molecular methods detect nucleic acid rather than viable organisms. The net
#  effect on waste is genuinely unclear and is recorded as such.
#
#  GOAL 2 IS DELIBERATELY NOT CLAIMED. Zero hunger would be a reachable claim
#  for a food record and this one does not increase supply. What it does is
#  make supply safer, which is Goal 3.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on foodborne illness prevented, the primary claim
    12,  # Responsible production, with the waste qualification stated
    17,  # Partnerships, on the cross-border sequence sharing that makes
    #      outbreak detection work at all
)


# =============================================================================
#  GLOSSARY
#  Grouped: what is looked for, how, what the numbers mean, and the legal
#  vocabulary a result triggers.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- what is looked for ----------------------------------------------------
    "foodborne_pathogen",
    "mycotoxin",
    "marine_biotoxin",
    "food_allergen",
    "food_fraud",
    "adulteration",
    "food_authenticity",
    # -- how ------------------------------------------------------------------
    "enrichment_culture",
    "polymerase_chain_reaction",
    "isothermal_amplification",
    "immunoassay",
    "whole_genome_sequencing",
    "metagenomics",
    "stable_isotope_analysis",
    # -- what the numbers mean -------------------------------------------------
    "limit_of_detection",
    "sensitivity_specificity",
    "sampling_plan",
    "measurement_uncertainty",
    "viable_but_nonculturable",
    "genomic_cluster",
    "core_genome_mlst",
    # -- what a result triggers ------------------------------------------------
    "microbiological_criteria",
    "critical_control_point",
    "product_withdrawal",
    "traceability",
    "method_validation",
    "accreditation",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "who_foodborne_disease_burden",
    "eu_microbiological_criteria_regulation",
    "whole_genome_sequencing_outbreak_surveillance",
    "melamine_adulteration_review",
    "horsemeat_incident_report",
    "iso_16140_method_validation",
    "codex_sampling_plans",
    "aflatoxin_discovery_history",
    "food_allergen_detection_review",
    "seafood_species_substitution_survey",
)


# =============================================================================
#  RELATED
#  Six edges. The first is the method, the second is the control loop.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same methods against a cooperative sample -------------------------
    "red.molecular_diagnostics",
    # -- the control this record verifies --------------------------------------
    "yellow.food_biopreservation",
    # -- the same detection-versus-response problem ----------------------------
    "dark.biosurveillance",
    # -- the acid barrier whose failure this record detects --------------------
    "yellow.food_fermentation",
    # -- pathogen control before the food is food ------------------------------
    "green.veterinary_vaccines",
    # -- sequences from identified patients, shared across borders -------------
    "purple.genetic_data_privacy",
)
