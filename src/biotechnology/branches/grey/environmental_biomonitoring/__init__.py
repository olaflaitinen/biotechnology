# =============================================================================
#  biotechnology.branches.grey.environmental_biomonitoring
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  ENVIRONMENTAL BIOMONITORING
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. Assembly only; the content is in the facets.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, grouped by the question being asked
#      metrics.py      what is measured, starting with the expectation that
#                      everything else is compared against
#      history.py      how it arrived, and a baseline that had been moving
#      governance.py   the vocabularies, and a record that is the instrument
#                      rather than the subject
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  WHY THIS RECORD IS THE BRANCH'S INSTRUMENT
#  Every other grey record changes something. This one finds out whether
#  anything changed, and without it the rest of the branch is a set of claims
#  about invisible processes.
#
#      A CHEMICAL SAMPLE RECORDS A CONCENTRATION AT AN INSTANT.
#      A COMMUNITY RECORDS AN EXPOSURE OVER TIME.
#
#  A discharge at three in the morning is invisible in a sample taken at noon
#  and visible in the invertebrates for months. That difference is the whole
#  argument for measuring organisms rather than substances, and it is why both
#  are needed.
#
#  TWO LIMITS THE RECORD INSISTS ON. Environmental DNA detects MATERIAL that
#  was present, not an organism that is there now, gives no reliable abundance,
#  and is blind to any species missing from a reference database. And every
#  assessment is a comparison against a reference condition chosen from the
#  least disturbed sites available, which means the standard itself has been
#  moving for as long as anyone has been measuring.
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
#  The key is referenced from every other record in this branch, so it is fixed
#  and must not be renamed.
#
#  The aliases lead with the method names a reader will actually have met,
#  since "environmental DNA" and "bioindicator" are far more current than the
#  umbrella term used here.
# -----------------------------------------------------------------------------
KEY = "environmental_biomonitoring"
NAME = "Environmental Biomonitoring"
ALIASES = (
    "biomonitoring",
    "bioindicators",
    "environmental DNA",
    "eDNA monitoring",
    "ecological assessment",
    "biological water quality assessment",
    "wastewater surveillance",
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
