# =============================================================================
#  biotechnology.branches.white.biofuels
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  BIOFUELS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Making transport fuel from plants and waste instead of from oil wells, and
#  arguing, correctly, about whether that is worth doing.
#
#  THE EDITORIAL POSITION, STATED FIRST
#  This is the most contested record in the white branch, and it takes the same
#  stance as `green.plant_genetic_engineering`: report the disagreement
#  accurately, say what is actually settled, and decline to adjudicate what is
#  not.
#
#      SETTLED      sugarcane ethanol returns far more energy than it consumes;
#                   maize ethanol returns much less and the exact figure is
#                   genuinely disputed; indirect land use change is real and
#                   its magnitude is uncertain; cellulosic ethanol did not
#                   arrive at the scale mandated for it.
#
#      NOT SETTLED  how to allocate emissions to co-products, how to price land
#                   use change, and whether crop-based fuel was a transitional
#                   necessity or a costly detour.
#
#  THE ONE HARD NUMBER IN A RECORD FULL OF CONTESTED ONES
#  Fermenting glucose to ethanol cannot exceed 0.511 grams per gram. Each
#  glucose gives two ethanol and two carbon dioxide, so roughly HALF THE
#  FEEDSTOCK MASS LEAVES AS CARBON DIOXIDE by stoichiometry, before any
#  inefficiency is counted. Industrial plants already reach ninety per cent or
#  more of what remains, so there is almost nothing left to win in that step.
#  Improvement has to come from feedstock, pretreatment or energy integration.
#
#  THE CONCEPT A READER MOST NEEDS
#  Energy return on investment. `narrative.ANALOGY` puts it as a job whose wage
#  is consumed by the commute: the number on the contract tells you little. For
#  sugarcane the commute is short. For maize it is long enough that careful
#  people still disagree about whether the job pays. Treating biofuels as one
#  category is the commonest error in discussing them, and the EROI spread
#  between feedstocks is nearly an order of magnitude.
#
#  WHY THE SECOND GENERATION WAS SUPPOSED TO END THE ARGUMENT, AND DID NOT
#  Straw and residues compete with nobody's dinner. But plant cell walls
#  evolved specifically to resist microbial attack, and every step of defeating
#  that resistance creates the next step's problem:
#
#      pretreatment  disrupts lignin, and generates furans and acids that
#                    poison the fermentation two steps later
#      hydrolysis    needs enzyme loadings whose cost per litre has never come
#                    down enough
#      fermentation  must use xylose, which the standard ethanol yeast ignores
#      recovery      faces 4 to 6 per cent titre against 12 to 16 for starch,
#                    and distillation energy rises steeply as titre falls
#
#  THREE SETBACKS, WHICH IS MORE THAN ANY OTHER RECORD HERE
#  That is not an editorial choice; it is what the field looks like.
#
#      2008  indirect land use change was quantified, and a sector that had
#            expanded for years discovered its central assumption had never
#            been tested. Under some estimates crop-based fuel offered no
#            benefit at all.
#      2009  algal fuel was funded far ahead of its evidence. Laboratory
#            productivity did not survive open cultivation, harvesting a dilute
#            suspension was expensive, and most programmes redirected to
#            higher value products.
#      2014  commercial cellulosic ethanol plants opened against mandated
#            volumes and were mostly idled within a few years. Mandates were
#            written down by orders of magnitude. It is the clearest case in
#            this library of policy requiring an outcome the science could not
#            supply on the assumed schedule.
#
#  A PATTERN WORTH NAMING
#  Biofuel expansion has repeatedly been driven by ENERGY SECURITY and had
#  climate arguments attached afterwards: Brazil in 1975, the United States in
#  2005, and again after 2022. That ordering explains why volumes were mandated
#  before feasibility was established, and why the fuels were then judged
#  against a criterion they had not been designed for.
#
#  THE GOVERNANCE FEATURE FOUND NOWHERE ELSE IN THIS LIBRARY
#  Elsewhere regulation permits or restricts. HERE REGULATION CREATES THE
#  MARKET. A biofuel competes with a cheaper fossil equivalent; what makes it
#  saleable is a mandate, a target or a tradable certificate that exists only
#  because a legislature made it. And because a litre of ethanol carries no
#  evidence of how its crop was grown, compliance is demonstrated by AUDIT
#  rather than by analysis. A contested scientific estimate becomes an
#  administrative determination.
#
#  WHERE THE FIELD ACTUALLY WENT
#  Road transport is electrifying, which removes the market the first
#  generation was built for. What remains, and what genuinely needs a liquid
#  fuel, is aviation, shipping and heavy freight, so the centre of gravity has
#  moved to drop-in fuels from waste oils and residues. Gas fermentation of
#  steel mill off-gas sidesteps the land argument entirely rather than
#  answering it, which after three setbacks is a reasonable strategy.
#
#  PACKAGE LAYOUT
#      narrative.py    what is settled, what is not, and the commute analogy
#      practice.py     applications by generation, each with its commercial
#                      state stated rather than implied
#      metrics.py      eleven metrics, assessment before fermentation, because
#                      a process can be excellent and still not worth running
#      history.py      1900 to 2022, with three setbacks of three kinds
#      governance.py   regulation as market creation, and audit as mechanism
#      linkage.py      the three problems this record cannot solve alone, and
#                      why SDG 2 is deliberately not claimed
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
KEY = "biofuels"

NAME = "Biofuels and Bioenergy"

# "bioenergy" is broader than biofuels and is included because a reader
# searching for it should arrive here. "advanced biofuels" is the policy term
# for everything after the first generation, and "sustainable aviation fuel" is
# where the demand now is, so both must resolve to this record.
ALIASES = (
    "bioenergy",
    "bioethanol",
    "biodiesel",
    "advanced biofuels",
    "sustainable aviation fuel",
    "renewable fuels",
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
