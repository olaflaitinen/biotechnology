# =============================================================================
#  biotechnology.branches.red.molecular_diagnostics.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has the widest cross-branch reach of any in the taxonomy, and
#  for a reason worth stating: the same three techniques, meaning amplification,
#  sequencing and hybridisation, are used to answer completely different
#  questions in at least six of the ten branches.
#
#  A laboratory that can detect a respiratory virus in a nasal swab can, with
#  no new equipment and largely the same protocol, detect Salmonella in a
#  chicken carcass, a fish species in a fillet sold as something else, a
#  pathogen circulating in a river, an invasive species from a bucket of
#  seawater, or a deliberately released agent. The edges below are that fact
#  made navigable, and following them is the fastest way to understand how
#  little of biotechnology is actually separate.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Two only. The temptation to add 10 was resisted: diagnostic capacity is
#  distributed far more unevenly than treatment capacity, so the honest claim
#  is that this field currently widens rather than narrows health inequality,
#  and a record cannot claim a goal it works against.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Good health and well-being
    9,  # Industry, innovation and infrastructure
)


# =============================================================================
#  GLOSSARY
#  Grouped in the order the DESCRIPTION uses them: how the signal is made, how
#  it is read, and how the result is judged.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- making the signal ---------------------------------------------------
    "amplification",
    "primer",
    "probe",
    "melting_temperature",
    "isothermal_amplification",
    # ---- reading it ------------------------------------------------------------
    "quantification_cycle",
    "standard_curve",
    "multiplexing",
    # ---- judging it -------------------------------------------------------------
    "sensitivity",
    "specificity",
    "prevalence",
    "positive_predictive_value",
    "limit_of_detection",
    "analytical_validity",
    "clinical_validity",
    "variant_of_uncertain_significance",
)


# =============================================================================
#  REFERENCES
#  The founding method, the reporting standard that made results comparable,
#  the sequencing survey, and the newest detection chemistry.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "mullis1986",  # the founding method
    "bustin2009",  # MIQE, the reporting standard
    "goodwin2016",  # the sequencing technology survey
    "kaminski2021",  # CRISPR-based detection
)


# =============================================================================
#  RELATED
#  Eight edges, seven of them crossing a branch boundary. See the header note:
#  the same three techniques answer different questions in six branches.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the sibling that turns a result into a prescribing decision ----------
    "red.pharmacogenomics",
    # ---- the computational layer that interprets everything above -------------
    "gold.genomics_data_analysis",
    "gold.multi_omics_integration",
    # ---- the same techniques, different question: is this food safe? ----------
    "yellow.food_safety_biotechnology",
    # ---- the same techniques, different question: is this river polluted? -----
    "grey.environmental_biomonitoring",
    # ---- the same techniques, different question: what lives in this sea? -----
    "blue.marine_genomics",
    # ---- the same techniques, different question: is an outbreak deliberate? --
    "dark.biosurveillance",
    # ---- who may hold the result, and what may be done with it ----------------
    "purple.genetic_data_privacy",
)
