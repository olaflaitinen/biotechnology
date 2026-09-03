# =============================================================================
#  biotechnology.branches.grey.air_biotreatment
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  AIR BIOTREATMENT
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. Assembly only; the content is in the facets.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, grouped by what is being complained about
#      metrics.py      what is measured, starting with a property of the
#                      compound rather than of the plant
#      history.py      how it arrived, from a soil bed with a pipe under it
#      governance.py   the vocabularies, and a standard enforced by a human
#                      sense
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  THE ONE IDEA THAT EXPLAINS THE WHOLE RECORD
#
#      THE ORGANISMS LIVE IN A FILM OF WATER, NOT IN THE AIR. A CONTAMINANT
#      MUST DISSOLVE BEFORE IT CAN BE DEGRADED.
#
#  So the limit is solubility rather than biodegradability. Hydrogen sulphide,
#  ammonia and alcohols are treated well; methane and chlorinated solvents pass
#  through a perfectly healthy bed. That boundary is chemical, and no
#  improvement in the biology moves it.
#
#  TWO CONSEQUENCES. Biology beats thermal oxidation for large volumes of
#  weakly contaminated air, because heating mostly nitrogen is expensive and
#  running a fan is not. And most of what is installed is odour control, which
#  means the acceptance criterion is a trained human panel and the driver is a
#  neighbour rather than a measured exposure.
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
#  The key is referenced from `grey.biowaste_treatment`, so it is fixed.
#
#  The aliases lead with the configuration names and with "odour control",
#  because that is what a reader will have met on a drawing or in a planning
#  condition rather than the umbrella term used here.
# -----------------------------------------------------------------------------
KEY = "air_biotreatment"
NAME = "Air Biotreatment"
ALIASES = (
    "biofiltration",
    "biofilter",
    "biotrickling filter",
    "bioscrubber",
    "odour control",
    "waste gas biotreatment",
    "biological air purification",
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
