# =============================================================================
#  biotechnology.branches.blue.marine_biofouling_control
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BLUE BIOTECHNOLOGY  ->  MARINE BIOFOULING CONTROL
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Stopping barnacles, weed and slime from growing on everything humans put in
#  the sea, which turns out to matter a great deal for fuel.
#
#  THIS RECORD CLOSES THE BLUE BRANCH BY INVERTING IT
#  Every other record here treats marine life as a resource. This one treats it
#  as the adversary. Anything submerged is colonised within hours, and
#  preventing that is a large industry in its own right.
#
#  WHY IT MATTERS MORE THAN IT SOUNDS
#  A fouled hull increases drag substantially, and most world trade moves by
#  sea. Hull coatings are therefore among the most consequential surface
#  treatments in the world for fuel consumption and emissions.
#
#      THIS IS A CLIMATE TECHNOLOGY FILED UNDER MARINE PAINT.
#
#  THE SEQUENCE, AND WHY THE FIRST STAGE IS THE ONE TO ATTACK
#      minutes   a conditioning film of dissolved organic molecules adsorbs
#      hours     bacteria attach and form a biofilm
#      days      diatoms and protozoa follow
#      weeks     barnacle, mussel and tubeworm larvae settle on what is there
#
#  Each stage prepares the surface for the next, and many larvae settle in
#  response to a bacterial biofilm cue rather than onto bare substrate. Prevent
#  the film and much of what follows never arrives, which is why quorum sensing
#  and enzymatic approaches are the current frontier.
#
#  THE CENTRAL LESSON IS REGULATORY, AND IT IS THE CLEAREST IN THE LIBRARY
#  Tributyltin was an outstandingly effective antifouling agent. By any measure
#  of its stated purpose it was the best ever deployed. It also caused imposex
#  in molluscs, females developing male characteristics and becoming unable to
#  reproduce, at concentrations of NANOGRAMS PER LITRE.
#
#      1960s   introduced, outstandingly effective
#      1970s   oyster farms near marinas report deformation and failure
#      1981    imposex described and attributed
#      2008    global prohibition takes effect
#
#  Roughly three decades from strong evidence of harm to the global ban. The
#  effect occurred orders of magnitude below anything the original assessment
#  had thought worth testing.
#
#  Two conclusions belong in the data. A TECHNOLOGY CAN BE EXCELLENT AT ITS
#  PURPOSE AND UNACCEPTABLE IN ITS CONSEQUENCES, and the two judgements are
#  independent. And an assessment that tests only where an effect is expected
#  will not find one that occurs below.
#
#  `metrics.py` is built around this: efficacy and predicted environmental
#  concentration are placed adjacent and deliberately, because reporting the
#  first without the second is the error that took decades to correct.
#
#  AND THE PATTERN IS REPEATING, MORE WEAKLY
#  Copper replaced tributyltin and is now restricted in enclosed waters, since
#  it accumulates in marina sediment and is toxic to non-target organisms.
#  `practice.CHALLENGES` therefore records that an effective biocide should be
#  assumed to have a REGULATORY LIFETIME rather than a permanent one.
#
#  THE ALTERNATIVES, AND WHAT EACH CANNOT DO
#      foul-release    very low surface energy, so organisms attach weakly and
#                      the vessel's own motion removes them. Needs the vessel
#                      to MOVE: a ship at anchor fouls regardless.
#      microtexture    copies shark skin, deters settlement mechanically.
#                      Performs in a laboratory, hard to maintain on a hull
#                      for years.
#      natural product the chemistry sessile organisms use to stay clean, and
#                      the supply constraint of the whole branch with it.
#      quorum sensing  attacks the biofilm before anything visible settles.
#                      Most promising, least commercially established.
#
#  `narrative.ANALOGY` is a non-stick pan rather than a strong detergent, and
#  its stated limit is the honest one: a pan left on the side still gets dirty.
#
#  TWO OBJECTIVES THAT ARE NOT THE SAME
#  Fuel efficiency wants a smooth open hull. Biosecurity depends on niche areas
#  such as sea chests and thrusters, which foul heavily, are rarely inspected,
#  and are where invasive species are actually transported. The two usually
#  align and do not always, which is why `metrics.py` carries a separate
#  species transfer metric.
#
#  A CROSS-BRANCH PARALLEL WORTH FOLLOWING
#  `green.biopesticides` describes a field that used broad-spectrum toxicity,
#  found the non-target consequences, has a signature banned compound, and
#  moved towards interfering with a behaviour rather than killing. The
#  arguments transfer almost entirely, which suggests the pattern belongs to
#  using poisons in an open system rather than to either field.
#
#  PACKAGE LAYOUT
#      narrative.py    the sequence, the cost, and the non-stick pan
#      practice.py     applications by WHAT IS PROTECTED; technologies by
#                      mechanism, in the order the field moved through them
#      metrics.py      twelve metrics opening with drag, and placing efficacy
#                      beside environmental concentration deliberately
#      history.py      the tributyltin case in four entries, because the
#                      intervals between them are the lesson
#      governance.py   a convention that exists to prohibit one technology
#      linkage.py      why SDG 14 is claimed in both directions
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
KEY = "marine_biofouling_control"

NAME = "Marine Biofouling Control"

# "antifouling" is the industry term and what most readers will search for.
# "hull coatings" names the largest application, and "marine coatings" the
# sector. "biofouling" alone is included because a reader may arrive looking
# for the problem rather than its control.
ALIASES = (
    "antifouling",
    "biofouling",
    "hull coatings",
    "marine coatings",
    "fouling release",
    "ship biofouling management",
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
