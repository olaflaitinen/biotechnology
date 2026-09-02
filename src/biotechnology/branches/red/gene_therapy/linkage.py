# =============================================================================
#  biotechnology.branches.red.gene_therapy.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE -  every edge this record has to the rest of the
#                             taxonomy and to the outside world.
# -----------------------------------------------------------------------------
#
#  THE TAXONOMY IS A GRAPH, NOT A TREE
#  The ten colour branches look like a tree, and for navigation they are one.
#  But biotechnology does not divide cleanly: the nuclease used to edit a
#  human embryo cell is the same nuclease used to edit a wheat genome, and the
#  ethical machinery applied to both is the same machinery. Those relationships
#  are the interesting part of the subject, and they live in this file.
#
#  FOUR KINDS OF EDGE
#      SDGS         which UN Sustainable Development Goals this work serves
#      GLOSSARY     terms a reader must know, resolved in biotechnology.glossary
#      REFERENCES   citation keys, resolved in biotechnology.refs
#      RELATED      other subtypes, by dotted path
#
#  EVERY EDGE IS CHECKED
#  `tests/test_integrity.py` resolves all four tuples on every commit. A
#  reference to a glossary term that has not been written yet, or to a subtype
#  that has been renamed, fails the build rather than silently producing a
#  dead link in the generated documentation. This is the single most valuable
#  test in the suite, because cross-references are exactly what rots first in
#  a hand-curated dataset.
#
#  HOW TO CHOOSE `RELATED`
#  Between four and eight entries. Prefer edges that cross a branch boundary,
#  because those are the ones a reader would not have found on their own. An
#  edge to a sibling in the same branch is only worth including when the two
#  are genuinely often confused - as gene therapy and cell therapy are.
#
#  RECIPROCITY IS NOT REQUIRED
#  If A relates to B, B need not relate to A. Gene therapy points at
#  bioethics because a reader of gene therapy needs the ethics; a reader of
#  bioethics needs a much broader set of examples than gene therapy alone.
#  The validation suite reports asymmetries as information, not as errors.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS - United Nations Sustainable Development Goals
#  Only goals with a defensible, direct connection. Padding this tuple to make
#  a field look socially useful is the most common failure mode in impact
#  reporting, and the review rule here is that each number must survive the
#  question "what would a sceptical auditor say?"
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Good health and well-being - direct: treats otherwise untreatable disease
    9,  # Industry, innovation and infrastructure - the manufacturing platform
    10,  # Reduced inequalities - included because the ACCESS problem is central,
    #     not because the technology reduces inequality by itself. It currently
    #     does the opposite, and the record says so in narrative.WHY_IT_MATTERS.
)


# =============================================================================
#  GLOSSARY
#  Terms a reader must understand to follow the technical description. Each
#  key resolves in `biotechnology.glossary`, where it carries a definition in
#  both registers.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- delivery vocabulary -------------------------------------------------
    "vector",
    "transduction",
    "episome",
    "capsid",
    "tropism",
    # ---- genetics vocabulary -------------------------------------------------
    "germline",
    "somatic_cell",
    "allele",
    # ---- editing vocabulary --------------------------------------------------
    "crispr",
    "off_target_effect",
    "base_editing",
    # ---- regulatory vocabulary -----------------------------------------------
    "advanced_therapy_medicinal_product",
    "orphan_designation",
)


# =============================================================================
#  REFERENCES
#  Citation keys resolved in `biotechnology.refs`. The selection is deliberate
#  rather than exhaustive: one founding paper, one authoritative review, one
#  paper for the enabling tool, one clinical landmark and one regulatory
#  document. A reader who follows all five understands the field.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "friedmann1972",  # the founding proposal
    "naldini2015",  # authoritative review of the modern field
    "doudna2014",  # the enabling editing tool
    "high2019",  # clinical state of the art
    "ema_atmp_guideline",  # the regulatory frame
)


# =============================================================================
#  RELATED
#  Ordered from nearest to furthest. The first two are siblings inside the red
#  branch that are routinely confused with this one; the remainder cross
#  branch boundaries and are the edges a reader is unlikely to find alone.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- siblings that are genuinely confused with this one -------------------
    "red.cell_therapy",  # CAR-T is both; the boundary is where the edit happens
    "red.pharmaceutical_biotechnology",  # shares the manufacturing discipline
    # ---- the same molecular toolkit, applied to plants and livestock ---------
    "green.agricultural_genome_editing",
    # ---- the computational layer that designs the payload ---------------------
    "gold.computational_drug_discovery",
    "gold.nanobiotechnology",  # lipid nanoparticle delivery
    # ---- the normative layer that decides whether any of it is permissible ---
    "purple.bioethics",
    "purple.regulatory_affairs",
    "purple.genetic_data_privacy",
)
