# =============================================================================
#  biotechnology.branches.red.regenerative_medicine.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The two cross-branch edges that matter most here are the materials ones, and
#  they are easy to miss because they point away from medicine entirely.
#
#  `white.biopolymers` and `blue.marine_biomaterials` are where the scaffolds
#  come from. Alginate is extracted from seaweed; chitosan from crustacean
#  shells, largely a seafood processing by-product; collagen and gelatin from
#  bovine and marine sources; polylactic acid from fermented sugar. A reader
#  who studies this record without following those edges will treat the
#  scaffold as a given rather than as a manufactured material with its own
#  supply chain, its own variability and its own sustainability question.
#
#  That is also why this is the only record in the red branch carrying the
#  MATERIALS domain.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Two. Goal 10 was considered and rejected: these are among the most expensive
#  and least portable treatments in existence, delivered at a handful of
#  specialist centres, and the unregulated market described in
#  practice.CHALLENGES actively exploits patients who cannot access the
#  legitimate version. A claim to reduce inequality would fail the
#  sceptical-auditor test badly.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Good health and well-being
    9,  # Industry, innovation and infrastructure
)


# =============================================================================
#  GLOSSARY
#  Grouped along the three-component framework, then the physical constraint,
#  then the regulatory boundary that decides what the product legally is.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- the cells -----------------------------------------------------------
    "stem_cell",
    "pluripotency",
    "differentiation",
    "organoid",
    # ---- the scaffold ---------------------------------------------------------
    "scaffold",
    "extracellular_matrix",
    "decellularisation",
    "porosity",
    "biocompatibility",
    "biodegradation",
    # ---- the signals ----------------------------------------------------------
    "growth_factor",
    "mechanotransduction",
    # ---- the physical constraint -----------------------------------------------
    "vascularisation",
    "angiogenesis",
    "necrosis",
    # ---- what it legally is ----------------------------------------------------
    "minimal_manipulation",
    "advanced_therapy_medicinal_product",
)


# =============================================================================
#  REFERENCES
#  The framework paper, the reprogramming discovery, the organoid result that
#  redirected the field, and the standard review of bioprinting.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "langer1993",  # cells, scaffolds and signals
    "takahashi2006",  # reprogramming to pluripotency
    "sato2009",  # intestinal organoids
    "murphy2014",  # three-dimensional bioprinting
)


# =============================================================================
#  RELATED
#  Seven edges. The first two are red-branch siblings that share cell sourcing
#  and manufacturing; the two materials edges are the ones the header note
#  explains and are easy to overlook.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- shares cell sourcing, expansion and release testing ------------------
    "red.cell_therapy",
    # ---- how a construct is given a corrected or added gene -------------------
    "red.gene_therapy",
    # ---- where the scaffold materials actually come from ----------------------
    "white.biopolymers",
    "blue.marine_biomaterials",
    # ---- the fabrication and characterisation toolkit -------------------------
    "gold.nanobiotechnology",
    # ---- the ethics of embryonic sources, and of selling hope -----------------
    "purple.bioethics",
    # ---- the classification question that decides what the product is ---------
    "purple.regulatory_affairs",
)
