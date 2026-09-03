# =============================================================================
#  biotechnology.branches.yellow.alternative_proteins
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  ALTERNATIVE PROTEINS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Foods made from plants, fungi or insects that are meant to be used the way
#  meat is used, and the discovery that this is a texture problem rather than a
#  protein problem.
#
#  THE FACT THE RECORD IS BUILT ON
#
#      PROTEIN IS NOT THE PROBLEM.
#
#  Nobody in a wealthy market is short of protein, and a product sold on
#  protein content is competing with dried beans at a fraction of the price.
#  What these products sell is the EXPERIENCE of meat without the animal:
#  texture, flavour, appearance, cooking behaviour and price, all of which must
#  be right at once.
#
#  Meat is an anisotropic fibrous material whose structure comes from muscle.
#  Reproducing that from a globular plant protein is materials engineering
#  wearing a nutrition label, which is why `narrative.ANALOGY` is upholstery:
#  the stuffing is not the hard part, the covering and the grain are.
#
#  WHY `metrics.py` OPENS WITH REPEAT PURCHASE RATE
#  Between roughly 2019 and 2023 the plant-based meat category grew rapidly,
#  achieved wide trial and heavy coverage, and then contracted. Awareness was
#  high and distribution was wide. Every technical metric in this facet was
#  improving throughout.
#
#      PEOPLE BOUGHT THE PRODUCTS ONCE AND DID NOT BUY THEM AGAIN.
#
#  On taste and on price. A facet that opened with protein content or texture
#  would describe a field that was succeeding, which is not what happened. It
#  is the clearest demonstration in this branch that acceptance is an
#  engineering constraint rather than a communications problem.
#
#  TWO NUMBERS THAT MISLEAD, BOTH RECORDED HONESTLY
#      protein content    the number on the front of the pack and the least
#                         informative here. DIAAS is the honest measure, since
#                         it accounts for the limiting amino acid and for
#                         digestibility. A product can be high in protein and
#                         nutritionally inferior to what it replaces.
#      greenhouse gas     strong against beef and not seriously disputed.
#                         Narrower against chicken. Against pulses eaten
#                         directly it usually disappears, because the
#                         processing is what the product is. The comparator
#                         must be named.
#
#  THE OLDEST ENTRIES ARE THE LEAST DISCUSSED AND THE MOST INSTRUCTIVE
#  Tofu and tempeh are ancient, cheap and minimally processed. Mycoprotein has
#  been sold since 1985 and is fibrous WITHOUT extrusion, because fungal hyphae
#  arrive that way. None of these belongs to the 2015 wave, and all avoid every
#  one of its problems: they are not trying to imitate meat.
#
#  The 2024 move towards mycelium and fermentation-derived structure is a
#  return to what mycoprotein did in 1985, arrived at from the other direction
#  and for a second reason: growing the structure biologically shortens the
#  ingredient list that produced the ultra-processed classification.
#
#  THE REPUTATIONAL PROBLEM THE SECTOR DID NOT EXPECT
#  Ultra-processed classification placed these products in a category consumers
#  were simultaneously being advised to avoid. It is recorded here as a fair
#  description of how the texture is achieved rather than as a
#  misunderstanding to be corrected, because a long ingredient list is what
#  extrusion, flavour systems and fat structuring produce.
#
#  WHY `REGULATORY_STATUS = VARIES`
#  Four sources, four positions, on the same shelf:
#
#      plant protein   ordinary food, no authorisation. Soy and pea have been
#                      eaten for millennia.
#      fungal protein  authorised, and the authorisation is decades old.
#      insect protein  novel food, authorised SPECIES BY SPECIES.
#      microbial and   novel food for humans, feed additive for animals, and
#      gas protein     the feed route is where nearly all of it goes.
#
#  Again the variable is consumption history rather than hazard, which is the
#  same finding `yellow.precision_fermentation` records from its own side.
#
#  ONE CONSTRAINT WITH NO TECHNICAL ANSWER
#  Insect protein is efficient, authorised and cheap to produce, and Western
#  consumers will not eat it. Most producers responded by selling into animal
#  feed, where the question does not arise and where it displaces the fishmeal
#  recorded in `blue.aquaculture_biotechnology`. That is a solved commercial
#  problem and an unsolved cultural one.
#
#  THE SPECTRUM THIS RECORD SITS IN
#  Three answers to one question, ordered by how much of the animal is kept:
#
#      alternative_proteins      none. A description of the product.
#      precision_fermentation    one molecule. A copy of it.
#      cultivated_meat           the actual cells.
#
#  Cost and regulatory burden rise in the same order, and so does the claim to
#  be the thing rather than a version of it.
#
#  PACKAGE LAYOUT
#      narrative.py    texture rather than protein, and the upholstery analogy
#      practice.py     applications BY PROTEIN SOURCE, since the four have
#                      different economics and acceptance
#      metrics.py      thirteen metrics opening with the one that decided the
#                      sector, and warning about the two that mislead
#      history.py      tofu to 2024, opening with the products that were
#                      already working
#      governance.py   four sources, four regulatory positions
#      linkage.py      why SDG 3 is deliberately not claimed
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
KEY = "alternative_proteins"

NAME = "Alternative Proteins"

# "plant-based meat" is what most readers will search for and is narrower than
# the record. "mycoprotein" and "insect protein" name the two sources that are
# routinely forgotten, and both are older and steadier than the category that
# gets the coverage.
ALIASES = (
    "plant based meat",
    "meat alternatives",
    "mycoprotein",
    "insect protein",
    "novel protein",
    "protein transition",
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
