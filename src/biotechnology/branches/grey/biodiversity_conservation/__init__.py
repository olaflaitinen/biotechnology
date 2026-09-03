# =============================================================================
#  biotechnology.branches.grey.biodiversity_conservation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BIODIVERSITY CONSERVATION
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. Assembly only; the content is in the facets.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, grouped by how much is being changed
#      metrics.py      what is measured, starting with what is breeding rather
#                      than what is alive
#      history.py      how it arrived, and one question answered twice
#      governance.py   the vocabularies, and treaty law that predates the tools
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  THE STATEMENT THIS RECORD LEADS WITH AND DOES NOT WALK BACK
#
#      SPECIES ARE LOST BECAUSE HABITAT IS DESTROYED.
#      NO BIOTECHNOLOGY ADDRESSES HABITAT DESTRUCTION.
#
#  Everything here manages consequences. That is not a dismissal: genetic
#  rescue has documented recoveries behind it, genomic analysis has redirected
#  conservation effort by showing that protected units were defined wrongly,
#  and biobanking is the one intervention in this library that cannot be
#  performed later. But a record presenting these as an answer to biodiversity
#  loss would be describing a different problem from the one that exists.
#
#  DE-EXTINCTION IS KEPT IN PROPORTION. No extinct species has been restored.
#  The serious objection is not technical: a credible promise of reversal
#  weakens the case for prevention, and conservation biologists have made that
#  argument about their own field.
#
#  THIS IS THE LAST OF THE NINE GREY RECORDS, AND THE ONE LEAST LIKE THE
#  OTHERS. Its methods come from `green.animal_biotechnology` and its binding
#  constraint comes from `purple.access_benefit_sharing`, which is why most of
#  its edges point out of the branch.
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
#  The key is referenced from `grey.biomining` and
#  `grey.environmental_biomonitoring`, so it is fixed and must not be renamed.
#
#  The aliases carry the named subfields, because a reader will more often have
#  met "conservation genetics" or "genetic rescue" than the umbrella term.
# -----------------------------------------------------------------------------
KEY = "biodiversity_conservation"
NAME = "Biodiversity Conservation"
ALIASES = (
    "conservation biotechnology",
    "conservation genetics",
    "conservation genomics",
    "genetic rescue",
    "biobanking",
    "assisted reproduction for wildlife",
    "wildlife forensics",
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
