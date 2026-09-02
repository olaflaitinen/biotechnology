# =============================================================================
#  biotechnology.branches.red.pharmaceutical_biotechnology.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract, and the rules for choosing RELATED entries: see
#  `red/gene_therapy/linkage.py`. In short: four to eight entries, prefer
#  edges that cross a branch boundary, reciprocity is not required, and every
#  key in all four tuples is resolved by the integrity test on every commit.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has the most consequential cross-branch edge in the whole
#  library: `white.microbial_fermentation` and `yellow.precision_fermentation`
#  are the same engineering discipline pointed at different products. A reader
#  who understands a monoclonal antibody plant understands ninety per cent of
#  an industrial enzyme plant and of an animal-free dairy protein plant. That
#  is the single most useful thing this taxonomy can show someone, and it is
#  only visible through these edges.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Two only. The temptation to add 10 (reduced inequalities) was resisted:
#  biologics have, on net, widened rather than narrowed treatment inequality,
#  and claiming otherwise would fail the sceptical-auditor test that governs
#  this field.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Good health and well-being
    9,  # Industry, innovation and infrastructure
)


# =============================================================================
#  GLOSSARY
#  Grouped by the part of the process each term belongs to, so that a reader
#  working through the DESCRIPTION can pick up vocabulary in order.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- what the product is -------------------------------------------------
    "biologic",
    "biosimilar",
    "monoclonal_antibody",
    "recombinant_protein",
    # ---- how it is made ------------------------------------------------------
    "expression_vector",
    "cell_bank",
    "bioreactor",
    "fed_batch",
    "titre",
    # ---- what makes it complicated -------------------------------------------
    "glycosylation",
    "post_translational_modification",
    "host_cell_protein",
    "aggregation",
    # ---- how it is controlled ------------------------------------------------
    "good_manufacturing_practice",
    "critical_quality_attribute",
    "comparability",
)


# =============================================================================
#  REFERENCES
#  One founding experiment, one industry survey updated regularly, one quality
#  framework and one regulatory guideline.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "cohen1973",  # the founding recombinant DNA experiment
    "walsh2018",  # the standard periodic survey of approved biopharmaceuticals
    "ich_q8",  # the quality-by-design framework
    "ema_biosimilar_guideline",  # the regulatory frame for copies
    "berlec2013",  # expression host comparison
)


# =============================================================================
#  RELATED
#  The first three edges are the important ones: they show that this subtype's
#  engineering is shared, unchanged, with two other colour branches.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the same engineering, different product ----------------------------
    "white.microbial_fermentation",
    "white.bioprocess_engineering",
    "yellow.precision_fermentation",
    # ---- what is made in the plant ------------------------------------------
    "red.antibody_engineering",
    "red.gene_therapy",
    "red.vaccine_development",
    # ---- the rules that govern it -------------------------------------------
    "purple.regulatory_affairs",
    "purple.biotechnology_patents",
)
