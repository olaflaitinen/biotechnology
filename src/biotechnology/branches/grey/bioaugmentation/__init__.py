# =============================================================================
#  biotechnology.branches.grey.bioaugmentation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BIOAUGMENTATION
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. Assembly only; the content is in the facets.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, grouped by strength of evidence
#      metrics.py      what is measured, and what measurement settles it
#      history.py      how it arrived, and how it found its own boundary
#      governance.py   the vocabularies, and the safety-without-efficacy gap
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  WHY THIS RECORD IS UNUSUAL
#  It is the only record in the library whose subject usually fails. That is
#  the field's own repeated finding rather than an outside judgement, and the
#  record is built around it:
#
#      IF THE CAPABILITY IS PRESENT, FEED IT.
#      IF IT IS GENUINELY ABSENT, ADD IT.
#      ALMOST ALL THE FAILURES ARE THE FIRST CASE TREATED AS THE SECOND.
#
#  The record is referenced by `grey.bioremediation`, `green.biofertilisers`
#  and `yellow.probiotics_and_prebiotics`, which reached the same conclusion in
#  three separate literatures. It exists so those records can defer to one
#  place rather than each restating the evidence.
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
#  The key is referenced from other branches and must not be renamed.
#
#  The aliases include the commercial vocabulary as well as the technical one,
#  because a reader arriving from a product datasheet will have met "microbial
#  inoculant" or "bioadditive" rather than the word bioaugmentation.
# -----------------------------------------------------------------------------
KEY = "bioaugmentation"
NAME = "Bioaugmentation"
ALIASES = (
    "microbial augmentation",
    "microbial inoculation",
    "microbial inoculant",
    "bioadditive",
    "seeding",
    "culture addition",
    "microbial consortium addition",
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
