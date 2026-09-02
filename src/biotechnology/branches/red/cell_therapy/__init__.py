# =============================================================================
#  biotechnology.branches.red.cell_therapy
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  RED BIOTECHNOLOGY  ->  CELL THERAPY
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Instead of giving a patient a chemical, cell therapy gives them living
#  cells - often their own, taken out, reprogrammed and put back - and those
#  cells do the treating.
#
#  THE BOUNDARY WITH GENE THERAPY
#  These two subtypes overlap more than any other pair in the library. A CAR-T
#  product is a cell therapy whose cells have been gene-modified, and the
#  European Union therefore regulates it as a gene therapy medicinal product
#  while every clinician calls it a cell therapy. The division used here:
#
#      red.gene_therapy   concerns the genetic payload and its delivery
#      red.cell_therapy   concerns the cells themselves - where they come
#                         from, how they are expanded, how potency is proven,
#                         and how they are returned to a patient
#
#  Neither record is complete without the other, and `linkage.py` says so.
#
#  PACKAGE LAYOUT
#      narrative.py    prose, technical and public registers
#      practice.py     applications, technologies, organisms, techniques,
#                      challenges - note that most challenges are logistical
#      metrics.py      six release specifications, every one of them gating
#      history.py      1956 to the present, including the 1957 total failure
#      governance.py   two overlapping legal regimes, and why that matters
#      linkage.py      SDGs, glossary, citations, cross-references
#
#  The full facet contract is documented in
#  `branches/red/gene_therapy/__init__.py` and is identical for all
#  eighty-five subtype packages in this library.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ....core.models import Subtype

from . import governance, history, linkage, metrics, narrative, practice

__all__ = ["SUBTYPE"]


# =============================================================================
#  IDENTITY
# =============================================================================
KEY = "cell_therapy"

NAME = "Cell Therapy"

# "car-t" is included because it is overwhelmingly the term the public and the
# press use, even though it names one product class rather than the field.
ALIASES = (
    "cellular therapy",
    "car-t",
    "adoptive cell transfer",
    "stem cell therapy",
    "cell based medicine",
)


# =============================================================================
#  ASSEMBLY
# =============================================================================
SUBTYPE = Subtype(
    # -- identity --------------------------------------------------------------
    key=KEY,
    name=NAME,
    aliases=ALIASES,
    # -- narrative.py ----------------------------------------------------------
    summary=narrative.SUMMARY,
    description=narrative.DESCRIPTION,
    plain_language=narrative.PLAIN_LANGUAGE,
    analogy=narrative.ANALOGY,
    why_it_matters=narrative.WHY_IT_MATTERS,
    # -- practice.py -----------------------------------------------------------
    applications=practice.APPLICATIONS,
    technologies=practice.TECHNOLOGIES,
    organisms=practice.ORGANISMS,
    techniques=practice.TECHNIQUES,
    challenges=practice.CHALLENGES,
    # -- metrics.py ------------------------------------------------------------
    metrics=metrics.METRICS,
    formulas=metrics.FORMULAS,
    # -- history.py ------------------------------------------------------------
    milestones=history.MILESTONES,
    # -- governance.py ---------------------------------------------------------
    maturity=governance.MATURITY,
    risk_tier=governance.RISK_TIER,
    scale=governance.SCALE,
    domains=governance.DOMAINS,
    regulatory_status=governance.REGULATORY_STATUS,
    regulations=governance.REGULATIONS,
    standards=governance.STANDARDS,
    # -- linkage.py ------------------------------------------------------------
    sdgs=linkage.SDGS,
    glossary=linkage.GLOSSARY,
    references=linkage.REFERENCES,
    related=linkage.RELATED,
)
