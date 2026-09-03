# =============================================================================
#  biotechnology.branches.yellow.food_fermentation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  FOOD FERMENTATION
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Letting helpful microbes change food on purpose, which is the oldest thing
#  in this library and still one of the largest.
#
#  THE OLDEST RECORD HERE, BY THOUSANDS OF YEARS
#  Fermented beverages are evidenced from roughly nine thousand years ago. That
#  is older than writing and probably older than settled agriculture in some
#  regions. Bread, cheese, beer, wine, soy sauce, kimchi, vinegar and yoghurt
#  were all made for millennia before anyone knew a microorganism existed.
#
#  WHAT THE SCIENCE ACTUALLY CONTRIBUTED, WHICH IS NOT WHAT IT SOUNDS LIKE
#  When Pasteur showed in 1857 that fermentation is caused by living organisms,
#  he was explaining a technology already in daily use worldwide. The science
#  did not enable the practice.
#
#      IT ENABLED DOING THE PRACTICE THE SAME WAY TWICE.
#
#  A bakery that cannot afford to lose a batch, a dairy shipping a million
#  yoghurts a week, a brewery that must taste the same in March and September:
#  all need something a village practice never needed. That is a
#  smaller-sounding achievement than inventing fermentation and a much larger
#  one than it appears.
#
#  FOUR THINGS AT ONCE, AND THEY ARE WORTH SEPARATING
#      preserve       acid and alcohol exclude what would spoil or poison.
#                     No refrigeration required, which still matters to a great
#                     many people.
#      digest         microbial enzymes break down lactose, phytate and
#                     antinutritional factors that human enzymes cannot.
#      make safe      controlled acidification is a reliable pathogen barrier.
#      make good      hundreds of volatile compounds that no ingredient
#                     supplies. Not a trivial function: almost nothing on the
#                     list would have survived without it.
#
#  DEFINED CULTURES AGAINST COMMUNITIES, WHICH RUNS THROUGH EVERYTHING
#  A defined starter is known organisms, added deliberately, giving control. A
#  spontaneous or backslopped fermentation is a COMMUNITY, dozens of species
#  arriving in succession, and much of the world's fermented food is made that
#  way. Several such products CANNOT be reproduced from a defined starter,
#  because the succession is part of what makes them.
#
#  So the science has explained a great deal and has not replaced the craft.
#  `narrative.ANALOGY` is gardening rather than manufacturing, and its stated
#  limit is exactly this: a gardener can say what is growing, and the
#  traditional fermenter often cannot.
#
#  WHY `metrics.py` OPENS WITH pH
#  Everywhere else in this library a pH figure describes conditions. HERE THE
#  ACID IS THE SAFETY BARRIER. A fermentation that acidifies too slowly has not
#  made a poor product, it has made an unsafe one, which is why acidification
#  rate sits immediately below it and why both come before anything about
#  flavour or yield. Below pH 4.6 the organism responsible for botulism cannot
#  grow, and that threshold is a regulatory landmark rather than a preference.
#
#  THE VOCABULARY VALUE THAT IS UNIQUE IN THE LIBRARY
#  `REGULATORY_STATUS = UNREGULATED`, and it needs care. It does not mean
#  unsupervised: hygiene law applies in full, establishments are approved,
#  hazard analysis is mandatory. It means THE PRODUCT NEEDS NO PRIOR
#  AUTHORISATION, because a history of consumption exempts it from the novel
#  food regime.
#
#  Read against `yellow.precision_fermentation`, which is AUTHORISED for the
#  same underlying biology, it is the sharpest illustration in this branch that
#  much of food regulation turns on FAMILIARITY rather than on hazard. A
#  traditional product from one region may be freely sold there and be a novel
#  food in another.
#
#  TWO SETBACKS OF KINDS THAT APPEAR NOWHERE ELSE
#  In 1935 bacteriophage was identified as the cause of failed dairy
#  fermentations. Ninety years later it has never been eliminated: phage builds
#  in any plant using one strain repeatedly, and the answer is rotation and
#  resistance breeding rather than a cure. A problem managed permanently rather
#  than solved.
#
#  And from about 1990, industrial starters displaced regional fermentation
#  communities. Consistency, safety and shelf life were real gains; the cost was
#  the microbial diversity of foods that had been regionally distinct, and the
#  strains lost were also the reservoir from which future starters would have
#  been selected. A setback caused by successfully solving a different problem.
#
#  A QUESTION THIS RECORD RAISES AND DOES NOT SETTLE
#  Traditional fermented foods belong to communities and places. Characterising
#  one, isolating its organisms and selling a defined culture back is lawful in
#  most places and is not obviously fair. `governance.py` records the
#  geographical indication law that partially addresses it, and notes that a
#  rule protecting a PLACE cannot easily say whether the ORGANISMS are part of
#  what it protects.
#
#  PACKAGE LAYOUT
#      narrative.py    the four functions, and gardening rather than
#                      manufacturing
#      practice.py     applications by WHAT THE FERMENTATION IS FOR, and
#                      deliberately not confined to European products
#      metrics.py      twelve metrics opening with the safety barrier, and
#                      declining to invent a number for flavour
#      history.py      mostly prehistory, attributable to nobody, which is the
#                      finding rather than a gap
#      governance.py   process control rather than product approval
#      linkage.py      the precision fermentation comparison, which shows how
#                      much regulation turns on familiarity
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
KEY = "food_fermentation"

NAME = "Food Fermentation"

# "fermented foods" is what a reader will search for. "starter cultures" names
# the commercial core, and "brewing" and "cheesemaking" are included because
# they are the two applications most people can name and both belong here.
ALIASES = (
    "fermented foods",
    "starter cultures",
    "food microbiology",
    "brewing",
    "cheesemaking",
    "traditional fermentation",
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
