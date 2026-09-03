# =============================================================================
#  biotechnology.branches.grey.phytoremediation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  PHYTOREMEDIATION
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. Assembly only; the content is in the facets.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, grouped by mechanism
#      metrics.py      what is measured, and why the headline number misleads
#      history.py      how it arrived, including the chelate episode
#      governance.py   the vocabularies, and three bodies of law colliding
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  WHY THIS RECORD IS SEPARATE FROM `grey.bioremediation`
#  Because plants can do one thing microbes cannot:
#
#      A PLANT CAN PULL A METAL OUT OF THE SOIL, CONCENTRATE IT IN TISSUE
#      ABOVE GROUND, AND BE CUT DOWN AND CARRIED AWAY.
#
#  That is extraction, not destruction. The metal still exists and the harvest
#  is hazardous waste, so a project that has not planned its disposal has not
#  finished. And most deployed phytoremediation extracts nothing at all: the
#  common applications are hydraulic control and stabilisation, which are
#  containment.
#
#  TWO CONSTRAINTS DEFINE THE SCOPE. Roots reach a few metres, so deeper
#  contamination is out of the method rather than slow within it. And plants
#  grow seasonally, so extraction is measured in years to decades.
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
#
#  The aliases carry the individual mechanisms as well as the umbrella term,
#  because a reader arriving from a site report will have met "phytoextraction"
#  or "hydraulic control" rather than the general word, and because those
#  mechanisms have genuinely different endpoints.
# -----------------------------------------------------------------------------
KEY = "phytoremediation"
NAME = "Phytoremediation"
ALIASES = (
    "plant-based remediation",
    "phytotechnology",
    "phytoextraction",
    "phytostabilisation",
    "rhizodegradation",
    "phytomining",
    "hydraulic control",
    "green remediation",
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
