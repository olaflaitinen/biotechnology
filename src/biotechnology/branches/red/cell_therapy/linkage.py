# =============================================================================
#  biotechnology.branches.red.cell_therapy.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The first edge below is the most important cross-reference in the red
#  branch, and it points both ways. A CAR-T product is simultaneously a cell
#  therapy and a gene therapy; the European Union classifies it as the latter
#  and the clinical community treats it as the former. A reader who follows
#  only one of the two records will misunderstand the field. This is precisely
#  the situation the graph structure of this taxonomy exists to handle: no
#  single tree position is correct, so the record sits in one place and points
#  clearly at the other.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Goal 10 is included here, as it is for gene therapy, because access
#  inequality is a defining rather than an incidental feature of the field.
#  The claim being made is that the subject engages the goal, not that it
#  advances it.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Good health and well-being
    10,  # Reduced inequalities - engaged, and currently on the wrong side of it
)


# =============================================================================
#  GLOSSARY
#  Grouped so that a reader meets the vocabulary in the order the DESCRIPTION
#  uses it: sourcing first, then engineering, then delivery and safety.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- sourcing ------------------------------------------------------------
    "autologous",
    "allogeneic",
    "apheresis",
    "histocompatibility",
    # ---- engineering ---------------------------------------------------------
    "chimeric_antigen_receptor",
    "costimulatory_domain",
    "vector",
    # ---- what happens in the patient -----------------------------------------
    "engraftment",
    "persistence",
    "graft_versus_host_disease",
    "cytokine_release_syndrome",
    # ---- release and regulation ----------------------------------------------
    "potency_assay",
    "advanced_therapy_medicinal_product",
    "chain_of_identity",
)


# =============================================================================
#  REFERENCES
#  One founding clinical report, one construct paper, one modern review, one
#  regulatory guideline.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "thomas1957",  # the founding, and failing, transplant series
    "gross1989",  # the first chimeric antigen receptor
    "june2018",  # the standard modern review
    "ema_atmp_guideline",  # the regulatory frame
    "porter2011",  # the clinical result that redirected the field
)


# =============================================================================
#  RELATED
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the record every reader of this one also needs ----------------------
    "red.gene_therapy",
    # ---- adjacent modalities in the same branch ------------------------------
    "red.regenerative_medicine",
    "red.antibody_engineering",  # the binding domain of every CAR comes from here
    # ---- the manufacturing discipline ----------------------------------------
    "red.pharmaceutical_biotechnology",
    # ---- the governance layer -------------------------------------------------
    "purple.clinical_trial_ethics",
    "purple.regulatory_affairs",
    "purple.bioethics",
)
