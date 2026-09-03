# =============================================================================
#  biotechnology.branches.blue.aquaculture_biotechnology
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BLUE BIOTECHNOLOGY  ->  AQUACULTURE BIOTECHNOLOGY
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Breeding, feeding and keeping healthy the fish and shellfish that people
#  eat, now that most seafood is farmed rather than caught.
#
#  AN ETHICAL NOTE THAT BELONGS IN THE DATA
#  This is the second record in the library whose subject can suffer, after
#  `green.animal_biotechnology`. Welfare is recorded in `metrics.py` and
#  `practice.CHALLENGES` rather than appended as a caveat, and the honest
#  position is that the evidence on fish sentience has strengthened
#  considerably while the regulation covering it has not kept pace.
#
#  THE REVERSAL MOST READERS HAVE NOT REGISTERED
#  Aquaculture overtook capture fisheries in 2014 and now supplies about half
#  the fish people eat. Farming, not fishing, is how most seafood reaches a
#  plate, and that changes what questions about seafood are actually about.
#
#  DOMESTICATION HERE IS FIFTY YEARS OLD, NOT TEN THOUSAND
#  Systematic salmon breeding began in 1971. These animals are a few
#  generations from wild, which is why gains of ten to fifteen per cent per
#  generation are achievable, far above terrestrial livestock: the variation is
#  still there to be taken. It is also why effective population size is a
#  live concern, since the populations were founded from small numbers of
#  individuals.
#
#  THE FEED QUESTION, STATED PRECISELY
#  Farmed carnivorous fish were fed on wild fish, so an industry meant to
#  relieve wild stocks was drawing on them. That was a fair criticism in 1997.
#  Reformulation towards plant proteins, trimmings and algal oils has since cut
#  the wild fish requirement per kilogram of salmon by a large factor.
#
#  It is not zero, the substitutes carry land, water and fertiliser costs, and
#  the fish-in fish-out ratio is calculated differently by advocates on each
#  side. `metrics.py` grades it REPORTED and explains the convention problem
#  rather than picking a number.
#
#  THE FACT THAT GOVERNS EVERYTHING ELSE
#
#      A FISH FARM IS OPEN TO THE SEA.
#
#  A net pen exchanges water, parasites, pathogens, waste and occasionally
#  animals with the environment around it. Sea lice move to wild salmon.
#  Escapees interbreed and dilute local adaptation, irreversibly. Treatments
#  enter the water. `narrative.ANALOGY` is a barn with the windows permanently
#  open, and its stated limit is the recirculating trade: windows can be
#  fitted, at great cost, and somebody pays for the air handling afterwards.
#
#  This is why `SCALE = POPULATION` rather than FIELD. Sea lice thresholds
#  exist to protect wild fish migrating past. Fallowing is synchronised across
#  every farm in an area because a parasite does not respect a licence
#  boundary. The unit of both the risk and its management is a population,
#  farmed and wild together.
#
#  THE PAIR OF ENTRIES WORTH READING TOGETHER
#      1988   vaccines against furunculosis and vibriosis take salmon farming
#             from heavy antibiotic use to almost none, while production grows.
#      2010   sea lice resistance to successive chemicals becomes widespread,
#             and the industry moves to thermal and mechanical delousing, which
#             works and injures fish.
#
#  Where a vaccine existed, the problem was solved. Where one did not, thirty
#  years of chemistry produced resistance and a welfare cost. It is the
#  strongest evidence in this library for the argument
#  `green.veterinary_vaccines` makes at length.
#
#  THE THIRD SETBACK IS REGULATORY
#  A fast-growing modified salmon was approved in 2015 for work completed in
#  the early 1990s. Whatever one concludes about the product, a twenty-year
#  review is a statement about the system, and it deterred investment in the
#  area for a generation. Genome editing for disease resistance is now
#  demonstrated and held up by classification rather than by technique.
#
#  WHERE THE TONNAGE ACTUALLY IS
#  Salmon dominates the literature and most of this record's documented
#  successes, and it is a small fraction of world aquaculture by weight. Carp,
#  tilapia and molluscs are far larger and far less written about. A reader
#  should not mistake the visibility of salmon for its share.
#
#  PACKAGE LAYOUT
#      narrative.py    the reversal, the feed question, and the open system
#      practice.py     applications in the order a fish passes through them:
#                      bred, fed, kept healthy, contained
#      metrics.py      twelve metrics, correcting the two that are routinely
#                      quoted misleadingly, and including harm as well as output
#      history.py      ancient practice, recent science, three setbacks
#      governance.py   four legal systems meeting on one farm
#      linkage.py      why SDG 14 is claimed only on a specific mechanism
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
KEY = "aquaculture_biotechnology"

NAME = "Aquaculture Biotechnology"

# "fish farming" is what most readers will search for. "mariculture" is the
# marine subset and "aquaculture genetics" names the part of this record where
# the largest gains have been made.
ALIASES = (
    "fish farming",
    "mariculture",
    "aquaculture genetics",
    "fish breeding",
    "shellfish aquaculture",
    "aquatic animal health",
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
