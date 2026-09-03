# =============================================================================
#  biotechnology.branches.grey.biomining
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BIOMINING
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. Assembly only; the content is in the facets.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, split by whether the metal dissolves
#      metrics.py      what is measured, including the figure that outlives
#                      the operation
#      history.py      how it arrived, culprit before tool
#      governance.py   the vocabularies, and a liability outlasting its
#                      institutions
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  THE FACT THIS RECORD REFUSES TO SOFTEN
#
#      BIOMINING AND ACID MINE DRAINAGE ARE THE SAME CHEMISTRY. THE TECHNOLOGY
#      IS THE POLLUTION, CONTAINED AND POINTED SOMEWHERE.
#
#  Same organisms, same minerals, same acid, same dissolved metals. The
#  engineering that separates a copper operation from a century of orange water
#  running out of a hillside is a liner and a collection pipe.
#
#  AND THE MECHANISM THAT IS ROUTINELY MISDESCRIBED. The organisms do not eat
#  metal and do not accumulate it. They oxidise iron and sulphur for energy,
#  and the ferric iron and acid that result dissolve the mineral chemically.
#  The bacteria regenerate a reagent; the leaching is chemistry. That is why
#  the process cannot be accelerated by adding more organisms, and why its real
#  limits are oxygen transport, heap temperature and mineral surface
#  passivation.
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
#  The key is referenced from `grey.bioremediation` and `grey.phytoremediation`,
#  so it is fixed and must not be renamed.
#
#  The aliases carry both processes separately, because `practice.py` insists
#  they are not the same operation and a reader searching for either should
#  arrive here.
# -----------------------------------------------------------------------------
KEY = "biomining"
NAME = "Biomining"
ALIASES = (
    "bioleaching",
    "biooxidation",
    "biohydrometallurgy",
    "microbial leaching",
    "bacterial leaching",
    "heap leaching",
    "biological metal recovery",
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
