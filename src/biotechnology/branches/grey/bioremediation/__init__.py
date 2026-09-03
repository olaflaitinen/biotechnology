# =============================================================================
#  biotechnology.branches.grey.bioremediation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BIOREMEDIATION
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. No content is written here; this file is assembly only,
#  which is the convention every subtype package in this library follows.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, what it is done with, what goes wrong
#      metrics.py      what is measured, and the formulas behind it
#      history.py      how it arrived, including where it went wrong
#      governance.py   where it sits in the vocabularies, and the law
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  THE TWO THINGS THIS RECORD EXISTS TO CORRECT
#
#      1. Organisms destroy organic contaminants. They do not destroy metals.
#         Metal work relocates, concentrates or immobilises, and every one of
#         those leaves the metal somewhere.
#
#      2. Bioavailability, not biodegradability, is usually the limit. Most
#         contamination that has persisted for decades is degradable in a
#         flask and unreachable in the ground.
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
#  The key is referenced from `green.biofertilisers`, `grey.bioaugmentation`
#  and elsewhere, so it is fixed and must not be renamed.
#
#  The aliases carry the regulatory vocabulary as well as the scientific one,
#  because a reader arriving from a site report will have met "natural
#  attenuation" or "in situ treatment" rather than the word bioremediation.
# -----------------------------------------------------------------------------
KEY = "bioremediation"
NAME = "Bioremediation"
ALIASES = (
    "biological remediation",
    "microbial remediation",
    "in situ bioremediation",
    "natural attenuation",
    "biostimulation",
    "soil and groundwater remediation",
    "contaminated land treatment",
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
