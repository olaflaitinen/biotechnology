# =============================================================================
#  biotechnology.branches.yellow.precision_fermentation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  PRECISION FERMENTATION
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Making the actual proteins found in milk and eggs using microbes in a tank,
#  so the molecule is the real thing rather than an imitation of it.
#
#  WHAT THIS RECORD IS NOT, STATED FIRST BECAUSE IT MATTERS
#
#      PRECISION FERMENTATION IS NOT A NEW TECHNOLOGY.
#
#  Making a specific protein in an engineered microorganism has been routine
#  since recombinant insulin in 1982 and since chymosin entered cheesemaking in
#  1988. The great majority of cheese produced in several countries has been
#  made with a fermentation-derived enzyme for over thirty years, with almost
#  no controversy and very little public awareness.
#
#  WHAT ACTUALLY CHANGED IS THE PRICE THE PRODUCT MUST MEET
#      a pharmaceutical protein   grams per patient, competing on efficacy
#                                 against a patented alternative. Hundreds of
#                                 euro per gram is unremarkable.
#      a dairy protein            millions of tonnes, competing on price
#                                 against an agricultural commodity produced at
#                                 enormous scale and frequently subsidised.
#
#  The engineering problem is therefore not making the protein, which is
#  solved, but making it for what a food ingredient can bear. That is why
#  `metrics.py` opens with a PRICE rather than with titre: opening with the
#  fermentation would describe an interesting problem that is not the binding
#  one.
#
#  THE THING THE FIELD COMMUNICATES WORST
#  The protein is identical to the animal one. That is the entire selling
#  proposition, and it means it is AN ALLERGEN IN EXACTLY THE SAME WAY. Whey
#  protein made by a fungus will still affect someone allergic to milk. The
#  product is animal-free and is not allergy-free, and the two are routinely
#  conflated.
#
#  `narrative.ANALOGY` is printing a document rather than describing it, and
#  its stated limit is precisely this: an identical copy inherits everything,
#  including the parts nobody wanted.
#
#  THE GOVERNANCE COMPARISON, WHICH IS THE SHARPEST IN THE BRANCH
#      yellow.food_fermentation        UNREGULATED
#      yellow.precision_fermentation   AUTHORISED
#
#  Same underlying biology. The variable is not hazard, risk or evidence. It is
#  CONSUMPTION HISTORY. A food eaten for centuries is exempt from the novel
#  food regime; a molecule identical to one eaten for millennia, made a
#  different way, is not.
#
#  That is defensible, since a population's diet is not a place for
#  uncontrolled experiment. The consequence should still be stated: the regime
#  measures FAMILIARITY, and its practical effect is a barrier to entry
#  favouring companies able to fund parallel dossiers in several jurisdictions.
#
#  THE PAIR OF HISTORICAL ENTRIES WORTH READING TOGETHER
#      1988   fermentation chymosin approved. Purified away from the organism,
#             replaced an enzyme from slaughtered calves, gave the consumer
#             something. Almost no opposition.
#      1994   recombinant bovine somatotropin approved in the United States and
#             rejected in Europe. Scientifically defensible, administered to
#             animals, raised welfare questions, gave the consumer nothing they
#             had asked for. Among the most successfully opposed agricultural
#             biotechnologies in Europe.
#
#  The difference was not the science and not the risk. A product in this
#  record that cannot say what the EATER gains starts from the second position.
#
#  THE SETBACK OF 2023
#  Cost projections assumed rapid declines with scale, by analogy with
#  technologies whose costs are dominated by manufacturing learning. Here they
#  are dominated by feedstock and downstream processing, and neither falls that
#  way. Companies reduced scope or failed, and the sector moved towards
#  high-value proteins where the price target is reachable. The technical work
#  was sound and the economic reasoning was not, which is the same shape
#  `white.biobased_chemicals` records for succinic acid.
#
#  THE PRODUCT MOST PEOPLE HAVE EATEN WITHOUT KNOWING
#  Yeast-produced heme protein, which gives plant-based meat its colour and
#  flavour. It is the most widely consumed product in this record and is almost
#  never described by this record's name.
#
#  PACKAGE LAYOUT
#      narrative.py    why it is not new, what changed, and the allergen point
#      practice.py     applications by TIME ON THE MARKET, oldest first, so
#                      that the maturity of the technique is visible
#      metrics.py      thirteen metrics opening with a price, and separating
#                      identity from functionality
#      history.py      1982 to 2024, with the chymosin and somatotropin pair
#      governance.py   the UNREGULATED against AUTHORISED comparison
#      linkage.py      why SDG 2 and SDG 13 are deliberately not claimed
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
KEY = "precision_fermentation"

NAME = "Precision Fermentation"

# "animal-free dairy" and "fermentation-derived protein" are what the products
# are marketed as. "recombinant food protein" is the accurate technical term
# and the one a regulator would use, so all three resolve here.
ALIASES = (
    "animal free dairy",
    "fermentation derived protein",
    "recombinant food protein",
    "animal free protein",
    "cellular agriculture",
    "molecular farming",
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
