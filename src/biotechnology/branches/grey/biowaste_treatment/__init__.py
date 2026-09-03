# =============================================================================
#  biotechnology.branches.grey.biowaste_treatment
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BIOWASTE TREATMENT
#
#  WHAT THIS PACKAGE DOES
#  It imports the six facet modules beside it and assembles them into a single
#  frozen `Subtype`. Assembly only; the content is in the facets.
#
#      narrative.py    what it is, in two registers
#      practice.py     what is done, grouped by feedstock and by process stage
#      metrics.py      what is measured, warning indicators before yields
#      history.py      how it arrived, on tax policy rather than on science
#      governance.py   the vocabularies, and four regimes meeting on one plant
#      linkage.py      goals, terms, sources, and neighbouring records
#
#  WHY THIS RECORD IS DIFFERENT FROM THE REST OF THE BRANCH
#  Everywhere else in grey biotechnology, treatment is a cost imposed by
#  regulation. Here the material has value: methane that can be burned or put
#  into the gas grid, and a digestate that returns nitrogen and phosphorus to
#  soil.
#
#      BUT THE ECONOMICS TURN ON AVOIDED DISPOSAL COST RATHER THAN ON WHAT THE
#      GAS IS WORTH, WHICH IS WHY THE SAME PLANT IS VIABLE UNDER A LANDFILL TAX
#      AND UNVIABLE WITHOUT ONE.
#
#  TWO THINGS THIS RECORD INSISTS ON. The climate case is a comparison with
#  landfill, not with doing nothing: the methane is produced either way, and
#  the benefit is that it is produced inside a vessel with a pipe on it. And
#  the operational failures are about plastic and glass in the feedstock, which
#  makes plant performance a function of collection policy rather than of
#  process engineering.
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
#  The key is referenced from `grey.bioremediation` and from
#  `grey.wastewater_treatment`, so it is fixed and must not be renamed.
#
#  The aliases carry both routes and the product names, because a reader will
#  more often have met "anaerobic digestion" or "biogas" than the umbrella
#  term used here.
# -----------------------------------------------------------------------------
KEY = "biowaste_treatment"
NAME = "Biowaste Treatment"
ALIASES = (
    "anaerobic digestion",
    "biogas production",
    "composting",
    "organic waste treatment",
    "food waste treatment",
    "biomethane production",
    "biological waste recovery",
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
