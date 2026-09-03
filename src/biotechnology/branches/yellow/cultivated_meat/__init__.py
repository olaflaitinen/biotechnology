# =============================================================================
#  biotechnology.branches.yellow.cultivated_meat
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  CULTIVATED MEAT
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Growing meat from animal cells in a tank instead of from animals, which
#  works, and costs far too much.
#
#  THE TWO FACTS THIS RECORD HOLDS AT ONCE
#  It is the most publicised record in the branch and among the least
#  commercially realised in the library. Both halves are true and the coverage
#  generally carries one or the other.
#
#      WHAT IS TRUE       the biology works. Cells grow, differentiate into
#                         muscle and fat, and the product is meat by any
#                         compositional test. Two jurisdictions have approved
#                         sales. This is not speculative.
#      ALSO TRUE          production is in kilograms, not tonnes. No published
#                         cost figure approaches commodity meat. Several
#                         jurisdictions have prohibited sale outright.
#
#  The honest frame is A DEMONSTRATED CAPABILITY WITH AN UNSOLVED COST
#  STRUCTURE. That is a real thing to be, and it is not what the coverage
#  describes.
#
#  WHY THE COST DOES NOT FALL THE WAY THE PROJECTIONS ASSUMED
#  `metrics.py` opens with a cost and then immediately with its dominant
#  component, because that ordering is the argument:
#
#      the medium is a CONSUMABLE INPUT, not a fixed cost that volume spreads.
#
#  Its price falls when the formulation changes, when pharmaceutical-grade
#  components are replaced with food-grade ones, and when medium is recycled.
#  It does not fall because the factory is larger. The second cost is capital
#  for bioreactor capacity that does not exist at food scale, which also does
#  not fall with volume.
#
#  Most projections in this field borrowed learning curves from technologies
#  where they apply. It is the same error `yellow.precision_fermentation`
#  records for 2023 and the same shape `white.biobased_chemicals` records for
#  succinic acid.
#
#  `narrative.ANALOGY` is a heated greenhouse in winter: the tomatoes are real
#  and the heating bill decides the business. Its stated limit is that a
#  greenhouse at least gets its light free.
#
#  THE WALL THIS RECORD SHARES WITH A COMPLETELY DIFFERENT FIELD
#  Whole cuts have not been produced at any commercial scale, and the reason is
#  not technique. It is the OXYGEN DIFFUSION LIMIT of roughly one to two
#  hundred micrometres, beyond which tissue cannot be kept alive without a
#  vascular supply.
#
#  That is precisely the constraint `red.regenerative_medicine` is organised
#  around. Two fields with different purposes, funding and regulators are
#  blocked by one number, and neither has solved it. It is why formed products
#  from loose cells are on sale and a steak is not.
#
#  THE PROHIBITIONS CAME BEFORE THE PRODUCTS
#  `governance.py` records the most divergent regulatory picture in the
#  library: approved in Singapore and the United States, prohibited in Italy
#  and elsewhere, unassessed in the European Union.
#
#  What is unusual is not the divergence. It is that bans were enacted where
#  nothing was on sale, on grounds concerning food heritage, cultural identity
#  and agricultural livelihoods rather than safety. That is a legitimate thing
#  for a legislature to weigh, and it should be described precisely: a decision
#  that this food should not exist in that market, taken independently of any
#  evidence about the food. No technical progress addresses it.
#
#  `REGULATORY_STATUS = VARIES` is the only value that reports this. AUTHORISED
#  would conceal the bans; PROHIBITED would conceal the approvals.
#
#  WHY `MATURITY = PILOT` AND `SCALE = PILOT`
#  Not EMERGING: regulators have approved products and the public has bought
#  them. Not COMMERCIAL: kilogram production, a few restaurants, no facility at
#  industrial volume, cost nowhere near the market addressed. A handful of
#  approved sales at demonstration volume is a pilot, and the value will change
#  when a facility operates at tonne scale rather than when another approval is
#  granted.
#
#  THE SDG OMISSION THAT MATTERS
#  Goal 13 is DELIBERATELY NOT CLAIMED, for a technology usually presented as a
#  climate measure. Published life cycle assessments disagree on whether
#  cultivated meat beats conventional beef, and the answer turns chiefly on the
#  energy source and on how medium inputs are made. A disputed comparison is
#  not a goal claim, and claiming it would be the clearest possible failure of
#  the sceptical-auditor test.
#
#  What IS claimed, and holds at any scale because it is a property of the
#  method rather than of the volume: no living animal means no enteric pathogen
#  reservoir, no antibiotics and no zoonotic risk.
#
#  THE STRONGEST ARGUMENT IS ETHICAL, NOT ENVIRONMENTAL
#  Every other record in this branch reduces animal use. This one removes the
#  animal, which is a different claim, and it is why `linkage.py` points at
#  `purple.bioethics` rather than treating that as a footnote.
#
#  PACKAGE LAYOUT
#      narrative.py    both facts at once, and the greenhouse analogy
#      practice.py     applications ordered by WHAT HAS ACTUALLY BEEN DONE,
#                      with the aspirational group labelled as such
#      metrics.py      thirteen metrics opening with cost and its dominant
#                      component, and recording genuine uncertainty as such
#      history.py      1931 to 2024, with three setbacks
#      governance.py   approved, prohibited and unassessed simultaneously
#      linkage.py      why SDG 13 is declined and SDG 3 is not
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
KEY = "cultivated_meat"

NAME = "Cultivated Meat"

# The terminology is unsettled and the choice is regulatory as much as
# descriptive: "cultivated" is the industry's preferred term, "lab-grown" is
# what most readers will search for, and "cell-based" is used in some
# regulatory contexts. All resolve here, which is the point of the alias list.
ALIASES = (
    "cultured meat",
    "lab grown meat",
    "cell based meat",
    "in vitro meat",
    "cellular agriculture",
    "cultivated seafood",
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
