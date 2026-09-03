# =============================================================================
#  biotechnology.branches.yellow.biofortification
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  BIOFORTIFICATION
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Breeding vitamins and minerals into staple crops, so the nutrient arrives
#  with the harvest instead of through a shop or a clinic.
#
#  THE PROBLEM MOST READERS OF THIS LIBRARY HAVE NEVER HAD
#
#      HIDDEN HUNGER IS NOT HUNGER.
#
#  A person eating enough calories every day can be severely deficient in iron,
#  zinc or vitamin A, because a diet built on one staple cereal supplies energy
#  and very little else. It affects billions of people, it is invisible to any
#  measure based on calories, and its effects in childhood are permanent:
#  blindness, impaired cognitive development, increased mortality from ordinary
#  infections.
#
#  THE ARGUMENT IS ABOUT DELIVERY, NOT NUTRITION
#  Supplementation works. Industrial fortification of flour, salt and oil works
#  and is among the most cost-effective public health measures there is. Both
#  require a person to reach a clinic or buy centrally processed food.
#
#  The populations with the highest deficiency rates are frequently subsistence
#  farmers who eat what they grow and do neither. A nutrient bred into the seed
#  reaches them because it travels with the crop, needs no continuing
#  programme, no purchase and no behaviour change.
#
#  `narrative.ANALOGY` is fluoride in a water supply rather than tablets, and
#  its stated limit is the record's own boundary: it reaches only the people
#  connected to that supply.
#
#  THE CHAIN, AND EVERY LINK CAN BREAK
#  `metrics.py` is ordered as this chain because a content figure is the first
#  link and is routinely reported as though it were the last:
#
#      content in the grain
#        -> retained through processing and cooking
#          -> absorbed rather than bound by phytate
#            -> eaten in sufficient quantity, often enough
#              -> a measurable change in nutritional status
#
#  The breeding target is derived by working BACKWARDS along that chain from a
#  required change in status, which is what distinguishes this field from
#  raising a number for its own sake.
#
#  BUT THE FARMER DECIDES BEFORE THE NUTRITIONIST DOES
#  So the facet opens with the yield penalty. A variety with excellent
#  micronutrient content and a small yield penalty will not be planted, because
#  the benefit is invisible, delayed, and accrues to the household rather than
#  to the harvest. It cannot be traded against yield.
#
#  TWO ROUTES, AND THEIR RECORDS DIFFER SHARPLY
#      conventional breeding   uses variation that already exists. Released
#                              across many countries since 2007 and reaching
#                              tens of millions of households. Orange-fleshed
#                              sweet potato, iron beans and pearl millet, zinc
#                              wheat.
#      genetic engineering     required where the pathway is absent from the
#                              crop entirely, as for provitamin A in rice
#                              endosperm. Enormous scientific attention, and
#                              almost no deployed food.
#
#  THE RICE STORY IS TOLD BADLY BY EVERYONE
#  The 1999 construct produced too little provitamin A to matter nutritionally,
#  which its advocates did not always state clearly. A second construct in 2005
#  raised content by a large factor and made the argument real. Food approvals
#  followed from 2018 in countries that do not grow it. The Philippines
#  approved cultivation in 2021, the first anywhere. In 2024 an appellate court
#  there revoked the permits, subject to further process.
#
#      Twenty-five years from publication, and farmers are still not growing it
#      at scale. Advocates blaming opposition alone omit the first fact.
#      Opponents citing the 1999 weakness omit that it was superseded in 2005.
#
#  Meanwhile the conventionally bred crops were released and eaten. That
#  comparison is what this record exists to make, and `governance.py` declines
#  to adjudicate it: precaution about novel traits is defensible, and so is the
#  observation that the process cost decades against a deficiency that blinds
#  and kills children.
#
#  THE COMPLEMENT NOBODY EXPECTS
#  `linkage.py` points at `yellow.food_fermentation`, and the reason is
#  specific. This record raises the iron and zinc CONTENT of a grain; that one
#  degrades the PHYTATE that stops it being absorbed. Same deficiency, opposite
#  ends, and fermentation needs no new variety, no seed system, no approval and
#  no donor. A household already fermenting its porridge is doing half of what
#  this record is trying to achieve.
#
#  WHY `SCALE = POPULATION` FOR A CROP RECORD
#  `green.molecular_plant_breeding` is FIELD, because its unit is a crop in a
#  field. Here the unit is a deficiency prevalence in a population: the
#  breeding target is derived from it, the trials measure it, and a variety is
#  judged by whether it changes nutritional status rather than by what it
#  yields.
#
#  PACKAGE LAYOUT
#      narrative.py    hidden hunger, the delivery argument, and the water
#                      supply analogy with its boundary
#      practice.py     applications BY NUTRIENT, and within each by DEPLOYMENT
#                      rather than by scientific interest
#      metrics.py      twelve metrics ordered as the chain, opening with the
#                      yield penalty because the farmer decides first
#      history.py      1990 to 2024, with the longest setback in the library
#      governance.py   the same outcome, three regulatory regimes, no verdict
#      linkage.py      fermentation as the unexpected complement
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
KEY = "biofortification"

NAME = "Biofortification"

# "hidden hunger" is the term for the problem rather than the solution, and a
# reader arriving with it should land here. "golden rice" is included because
# it is what most people associate with the field, even though the
# conventionally bred crops have delivered almost all of its actual nutrition.
ALIASES = (
    "hidden hunger",
    "micronutrient deficiency",
    "nutrient enriched crops",
    "golden rice",
    "harvestplus",
    "crop nutritional quality",
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
