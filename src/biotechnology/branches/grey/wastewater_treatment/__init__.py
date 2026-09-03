# =============================================================================
#  biotechnology.branches.grey.wastewater_treatment
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WASTEWATER TREATMENT
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. Assembly only; the content is in the facets.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, grouped by pollutant and by biomass form
#      metrics.py      what is measured, including the oldest metric in the
#                      library
#      history.py      how it arrived, and an objective defined too narrowly
#      governance.py   the vocabularies, and a law that specifies only results
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  WHY THIS RECORD MATTERS MORE THAN ITS PROFILE SUGGESTS
#  It is the largest deliberate use of microorganisms on Earth. The volumes
#  exceed all the fermentation in `white` and all the food processing in
#  `yellow` combined, it has run continuously since 1914, and almost nobody
#  describes it as biotechnology.
#
#      THE ENGINEERING IS NOT IN THE ORGANISMS. IT IS IN THE SELECTION.
#
#  Nothing is inoculated. The organisms arrive in the sewage, and retention
#  times, aeration and zone sequencing decide which of them can persist. That
#  is the exact inverse of the sterile defined-strain model in
#  `white.microbial_fermentation`, and it operates at the larger scale.
#
#  AND THE HALF OF THE SUBJECT THAT IS USUALLY OMITTED: treating water converts
#  dissolved pollution into a wet solid, and handling that solid is about half
#  the cost of running a works.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ....core.models import Subtype

from . import governance, history, linkage, metrics, narrative, practice

__all__ = ["SUBTYPE"]


# -----------------------------------------------------------------------------
#  IDENTITY
#  The key is referenced from `grey.bioremediation`, `grey.bioaugmentation` and
#  `grey.phytoremediation`, so it is fixed and must not be renamed.
#
#  The aliases carry the named unit process as well as the general term,
#  because a reader arriving from an engineering context will have met
#  "activated sludge" rather than the umbrella phrase.
# -----------------------------------------------------------------------------
KEY = "wastewater_treatment"
NAME = "Wastewater Treatment"
ALIASES = (
    "sewage treatment",
    "activated sludge",
    "biological wastewater treatment",
    "effluent treatment",
    "water reclamation",
    "sanitation",
    "secondary treatment",
)


SUBTYPE = Subtype(
    key=KEY,
    name=NAME,
    aliases=ALIASES,
    # -- narrative ------------------------------------------------------------
    summary=narrative.SUMMARY,
    description=narrative.DESCRIPTION,
    plain_language=narrative.PLAIN_LANGUAGE,
    analogy=narrative.ANALOGY,
    why_it_matters=narrative.WHY_IT_MATTERS,
    # -- practice -------------------------------------------------------------
    applications=practice.APPLICATIONS,
    technologies=practice.TECHNOLOGIES,
    organisms=practice.ORGANISMS,
    techniques=practice.TECHNIQUES,
    challenges=practice.CHALLENGES,
    # -- metrics --------------------------------------------------------------
    metrics=metrics.METRICS,
    formulas=metrics.FORMULAS,
    # -- history --------------------------------------------------------------
    milestones=history.MILESTONES,
    # -- governance -----------------------------------------------------------
    maturity=governance.MATURITY,
    risk_tier=governance.RISK_TIER,
    scale=governance.SCALE,
    domains=governance.DOMAINS,
    regulatory_status=governance.REGULATORY_STATUS,
    regulations=governance.REGULATIONS,
    standards=governance.STANDARDS,
    # -- linkage --------------------------------------------------------------
    sdgs=linkage.SDGS,
    glossary=linkage.GLOSSARY,
    references=linkage.REFERENCES,
    related=linkage.RELATED,
)
