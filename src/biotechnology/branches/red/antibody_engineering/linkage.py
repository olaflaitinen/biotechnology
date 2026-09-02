# =============================================================================
#  biotechnology.branches.red.antibody_engineering.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record supplies a component to more of the taxonomy than almost any
#  other, and the edges below are chosen to show that rather than to be
#  exhaustive.
#
#  The binding domain designed here is the recognition half of a chimeric
#  antigen receptor in `red.cell_therapy`. It is the capture reagent in the
#  immunoassays underlying `red.molecular_diagnostics` and
#  `yellow.food_safety_biotechnology`. It is the targeting element of the
#  nanoparticles in `gold.nanobiotechnology`. In each case the same molecule is
#  doing the same job, meaning finding one thing among millions, and only the
#  thing attached to it changes.
#
#  That is the most transferable idea in the red branch, and a reader who
#  follows these edges will find the same design problem four times in four
#  different vocabularies.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Two. Goal 10 was considered and rejected: antibody therapeutics are among
#  the most expensive medicines in existence and their availability tracks
#  national wealth closely, so a claim to reduce inequality would fail the
#  sceptical-auditor test in the direction of overstatement.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Good health and well-being
    9,  # Industry, innovation and infrastructure
)


# =============================================================================
#  GLOSSARY
#  Grouped by the modular idea the record is built around: the part that binds,
#  the part that acts, how binding is measured, and how the molecule is made
#  acceptable to a human immune system.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- the part that binds -------------------------------------------------
    "antibody",
    "epitope",
    "paratope",
    "complementarity_determining_region",
    "single_domain_antibody",
    # ---- the part that acts ---------------------------------------------------
    "fc_region",
    "effector_function",
    "neonatal_fc_receptor",
    # ---- how binding is measured -----------------------------------------------
    "affinity",
    "avidity",
    "dissociation_constant",
    "residence_time",
    # ---- making it acceptable to a human ----------------------------------------
    "humanisation",
    "immunogenicity",
    "anti_drug_antibody",
    # ---- formats beyond the natural molecule -------------------------------------
    "bispecific",
    "antibody_drug_conjugate",
    "developability",
)


# =============================================================================
#  REFERENCES
#  The founding technique, the technique that replaced immunisation, the
#  discovery that opened the single-domain format, and the standard modern
#  review.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "kohler1975",  # hybridoma monoclonal antibodies
    "mccafferty1990",  # phage display
    "hamers1993",  # camelid heavy-chain-only antibodies
    "carter2018",  # the standard modern review of next-generation formats
)


# =============================================================================
#  RELATED
#  Ordered by how directly this record supplies a component to the target.
#  Six of the eight cross a branch boundary.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- where the designed molecule is manufactured --------------------------
    "red.pharmaceutical_biotechnology",
    # ---- where the binding domain becomes part of a living cell ---------------
    "red.cell_therapy",
    # ---- the alternative way to supply protection against a pathogen ----------
    "red.vaccine_development",
    # ---- where the same binder becomes a capture reagent ----------------------
    "red.molecular_diagnostics",
    "yellow.food_safety_biotechnology",
    # ---- where the same binder becomes a targeting element --------------------
    "gold.nanobiotechnology",
    # ---- the computational layer that now designs and screens it --------------
    "gold.structural_bioinformatics",
    "gold.machine_learning_in_biology",
)
