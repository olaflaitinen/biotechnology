# =============================================================================
#  biotechnology.branches.red.pharmaceutical_biotechnology
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  RED BIOTECHNOLOGY  ->  PHARMACEUTICAL BIOTECHNOLOGY
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Most classical medicines are small molecules built by chemists. This field
#  makes medicines that are too large and too intricate to build chemically,
#  by getting living cells to manufacture them instead.
#
#  WHY THIS SUBTYPE IS THE ANCHOR OF THE WHOLE COLOUR SCHEME
#  Roughly half of the best-selling medicines in the world are now biologics
#  made this way. More importantly for a reader navigating this library, the
#  bioprocess engineering involved is shared almost unchanged with
#  `white.microbial_fermentation` (industrial enzymes and chemicals) and with
#  `yellow.precision_fermentation` (animal-free food proteins). Three colour
#  branches, one discipline. Follow the RELATED edges in `linkage.py` to see it.
#
#  PACKAGE LAYOUT
#  Six facet files, each independently reviewable by a different specialist:
#
#      narrative.py    prose in a technical and a public register
#      practice.py     applications, technologies, organisms, techniques,
#                      and what does not work yet
#      metrics.py      titre, productivity, yield and purity specifications
#      history.py      1922 to the present, including the 1985 setback
#      governance.py   the densest regulatory apparatus in the taxonomy
#      linkage.py      SDGs, glossary, citations, cross-references
#
#  The full rationale for the six-facet split, and the complete facet
#  contract, is documented in `branches/red/gene_therapy/__init__.py`. Every
#  subtype package in this library follows exactly the same shape, so once you
#  have read one you can navigate all eighty-five.
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
#  KEY must equal the directory name; the parent branch asserts this at import.
# =============================================================================
KEY = "pharmaceutical_biotechnology"

NAME = "Pharmaceutical Biotechnology"

# The aliases matter more here than for most subtypes, because the industry
# itself uses four different names for the same thing depending on whether the
# speaker is a scientist, an investor or a regulator.
ALIASES = (
    "biologics",
    "biopharmaceuticals",
    "biopharma",
    "recombinant therapeutics",
    "large molecule drugs",
)


# =============================================================================
#  ASSEMBLY
#  Arguments are grouped and ordered to match the facet files, so that the
#  mapping from file to field is obvious without cross-referencing.
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
