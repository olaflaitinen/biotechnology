# =============================================================================
#  biotechnology.branches.white.microbial_fermentation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  MICROBIAL FERMENTATION
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Growing microbes on purpose, in a large tank, under conditions strict enough
#  that only the intended organism grows and it does what it was built to do.
#
#  WHY THIS RECORD SITS UNDER SO MANY OTHERS
#  Antibiotics, insulin, industrial enzymes, feed amino acids, vitamins, citric
#  acid, ethanol and animal-free proteins all reach the world through this one
#  operation. The same vessel design serves a pharmaceutical, a feed additive
#  and a polymer precursor. Few subtypes in this library are upstream of so
#  many others, which is why three completed records already point here.
#
#  THE ONE COUNTERINTUITIVE FACT: FEEDING FASTER PRODUCES LESS
#  Above a critical feed rate, most organisms switch to overflow metabolism and
#  excrete acetate or ethanol instead of making biomass or product. The sugar
#  is consumed, the by-product accumulates, it inhibits growth, and the
#  fermentation does worse than if it had been fed more slowly.
#
#  Nearly every industrial fermentation is run fed-batch for precisely this
#  reason, and that is why `metrics.py` records mu_crit, the threshold, rather
#  than treating mu_max as the number that matters. `narrative.ANALOGY` uses a
#  stove because fuel piled on faster than the air supply makes smoke rather
#  than heat, which is what overflow metabolism is.
#
#  THE TWO THINGS THAT DECIDE A CAMPAIGN, AND NEITHER IS THE STRAIN
#      sterility   a production vessel is a warm, rich, well-mixed nutrient
#                  broth, which is to say an excellent medium for whatever
#                  arrives first. A faster-growing contaminant displaces the
#                  production organism within hours, so sterilisation is not a
#                  precaution but the process itself.
#      oxygen      an aerobic culture consumes oxygen far faster than it
#                  dissolves, and transfer does not improve with vessel size.
#                  In most large aerobic processes the ceiling is set by the
#                  vessel, not the biology.
#
#  This is why `metrics.py` opens with kLa rather than with titre, which is the
#  reverse of `white.metabolic_engineering`. That record measures the strain;
#  this one measures the cultivation.
#
#  THE ANOMALY THIS RECORD REFUSES TO TIDY AWAY
#  Continuous culture is more productive per unit of capital and is barely
#  used. The reasons are not scientific. A long run gives contamination more
#  chances; selection favours any mutant that stops producing; and a regulated
#  product is released, traced and recalled BY BATCH, which a process without
#  batches does not naturally provide. `governance.py` treats that last point
#  as a real constraint rather than as paperwork, because it is the part most
#  technical accounts omit.
#
#  THE SETBACK
#  In 1980 one of the largest continuous sterile fermenters ever built began
#  making single cell protein from methanol, and held aseptic operation for
#  months. It was closed within a decade, destroyed by the price of soya meal.
#  A fermentation product competing with an agricultural commodity is competing
#  with land, sunlight and millions of growers. And the most impressive
#  demonstration of continuous fermentation in history ended up being cited as
#  the reason to avoid it.
#
#  A GOVERNANCE POINT MOST ACCOUNTS OMIT
#  This record is regulated as a large industrial installation as well as a
#  biological one. Pressure vessels, continuous water and energy demand, and a
#  substantial organic effluent in the spent broth mean a plant above a
#  threshold capacity needs an environmental permit under the Industrial
#  Emissions Directive. That burden belongs to process industry rather than to
#  biology, and it is real.
#
#  PACKAGE LAYOUT
#      narrative.py    overflow metabolism, sterility, oxygen, and why
#                      continuous operation lost
#      practice.py     applications showing the breadth; technologies as the
#                      four operational problems in the order a plant meets them
#      metrics.py      thirteen metrics, opening with the vessel rather than
#                      the organism, and closing with what a plant manager
#                      actually watches
#      history.py      1857 to 2022, pivoting on deep-tank penicillin in 1943
#      governance.py   the site permit, the organism, and batch as a legal idea
#      linkage.py      the three-way division of labour in the white branch
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
KEY = "microbial_fermentation"

NAME = "Microbial Fermentation"

# "industrial fermentation" and "submerged culture" are the process terms.
# "biomanufacturing" is what the sector calls itself now, particularly where
# the product is a medicine. "cultivation" is included because it is the
# neutral word used when the organism is not a bacterium.
ALIASES = (
    "industrial fermentation",
    "submerged culture",
    "biomanufacturing",
    "microbial cultivation",
    "fermentation technology",
    "deep tank fermentation",
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
