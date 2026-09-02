# =============================================================================
#  biotechnology.branches.green.plant_genetic_engineering
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  GREEN BIOTECHNOLOGY  ->  PLANT GENETIC ENGINEERING
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Taking a useful gene from one organism and adding it to a crop, so that the
#  crop gains a trait, such as resistance to an insect or extra vitamin, that
#  its own species never had.
#
#  A DELIBERATELY NEUTRAL RECORD
#  Few topics in this taxonomy attract more heat. This record reports what the
#  technology does, what is deployed, what the measured outcomes have been, and
#  what the open disputes are. It argues for nothing, and it refuses to resolve
#  the disputes into a verdict, because resolving them would be advocacy.
#
#  Several things are true simultaneously and are usually presented as
#  alternatives: insecticide applications fell, seed supply concentrated,
#  herbicide-resistant weeds emerged, and European public trust never recovered
#  from how the first products were introduced. `narrative.WHY_IT_MATTERS`
#  states all four and stops there.
#
#  THE FACT THAT EXPLAINS THE MOST AND IS DISCUSSED THE LEAST
#  The binding constraint is regulatory cost per event, not biology. A dossier
#  runs into tens of millions of euro, which only commodity-scale crops repay.
#  That is why the deployed trait set has barely changed in three decades, why
#  no public-sector programme has brought a transgenic crop to market at scale,
#  and why cassava, sorghum, cowpea and banana, the crops eaten by the most
#  food-insecure people, have benefited least from a technology frequently
#  justified by their needs.
#
#  THE NUMBER MOST OFTEN MISREAD
#  A Bt or virus-resistance trait does not raise genetic yield potential. It
#  PROTECTS existing yield by removing a loss. The observed difference against
#  an isogenic line is therefore a property of the pest pressure in the field
#  where it was measured, not of the technology. Advocates and critics both
#  quote it as though it were the latter, in opposite directions.
#  `metrics.py` says so before the list rather than after it.
#
#  THE COMPARISON WORTH MAKING
#  Read this record beside `green.agricultural_genome_editing`. Same laboratory,
#  same people, same crops, and a completely different regulatory position in
#  most of the world. It shows how much of what is attributed to the technology
#  is attributable to the law.
#
#  PACKAGE LAYOUT
#      narrative.py    the card-deck analogy, which corrects the commonest
#                      misconception without arguing
#      practice.py     applications grouped by who benefits
#      metrics.py      eight metrics, with the yield correction stated first
#      history.py      1977 to 2021, including two failures of trust
#      governance.py   process versus product regulation, and why cost is policy
#      linkage.py      the prerequisite, the successor, and the medical twin
#
#  The full facet contract is documented in
#  `branches/red/gene_therapy/__init__.py` and is identical for all eighty-five
#  subtype packages in this library.
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
# =============================================================================
KEY = "plant_genetic_engineering"

NAME = "Plant Genetic Engineering"

# "gmo crops" and "gm crops" are what most people search for. "biotech crops"
# is the industry's preferred term and "transgenic plants" the scientific one.
# All resolve here, deliberately, so that a reader arriving with any of them
# lands on the same neutral record.
ALIASES = (
    "gm crops",
    "gmo crops",
    "transgenic plants",
    "biotech crops",
    "genetically modified crops",
)


# =============================================================================
#  ASSEMBLY
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
