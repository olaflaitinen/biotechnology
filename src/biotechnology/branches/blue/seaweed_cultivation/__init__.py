# =============================================================================
#  biotechnology.branches.blue.seaweed_cultivation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BLUE BIOTECHNOLOGY  ->  SEAWEED CULTIVATION
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Growing seaweed on ropes in the sea, for food and for the thickeners that
#  are in a great deal of ordinary food, using no land, no fresh water, no
#  fertiliser and no feed.
#
#  THE CORRECTION THIS RECORD OPENS WITH
#
#      SEAWEED FARMING IS NOT AN EMERGING TECHNOLOGY. It is one of the largest
#      forms of aquaculture in the world, it has been industrial for decades,
#      and almost all of it happens in Asia.
#
#  Tens of millions of tonnes a year, overwhelmingly in China, Indonesia, the
#  Republic of Korea, the Philippines and Japan. European and North American
#  cultivation is genuinely emerging; the industry is not. Writing this record
#  from a European vantage point would misdescribe the subject, and
#  `MATURITY = ESTABLISHED` reflects the sector rather than its periphery.
#
#  THE BOUNDARY WITH `blue.algal_biotechnology`, WHICH EXPLAINS BOTH RECORDS
#  Drawn at the ORGANISM, because that is where the economics diverge:
#
#      microalgae   single cells in dilute suspension. Separating them from
#                   water dominates the economics. Grown in vessels.
#                   SCALE = INDUSTRIAL. Tens of thousands of tonnes.
#      macroalgae   large plants on ropes, lifted out of the sea. That harvest
#                   constraint does not exist at all. Grown in a place.
#                   SCALE = FIELD. Tens of millions of tonnes.
#
#  `metrics.py` therefore contains no harvest-cost metric, and its absence is
#  the clearest quantitative statement of why the two records are separate.
#
#  TWO INDUSTRIES UNDER ONE HEADING
#      food            whole seaweed, eaten for centuries, the larger tonnage
#      hydrocolloids   agar, carrageenan and alginate: extracted
#                      polysaccharides in a large share of processed food, in
#                      pharmaceutical formulation, in wound dressings and in
#                      dental impression material
#
#  Different species, different regions, different buyers. Conflating them
#  produces confused statements about what the sector is worth.
#
#  AND AGAR HOLDS UP MICROBIOLOGY. It was suggested to Koch's laboratory in
#  1881 by Angelina Hesse, who knew it from domestic cooking, after gelatin
#  proved useless because it melts at incubation temperature and bacteria
#  digest it. Pure culture technique rests on a seaweed extract.
#
#  THE OBSERVATION THAT MADE AN INDUSTRY
#  Nori was farmed for centuries by putting sticks in the water and hoping.
#  Nobody knew where the spores came from, so a bad year could not be
#  explained. In 1949 Kathleen Drew-Baker, working in Manchester on a Welsh
#  species, showed that a filamentous organism classified as a separate genus
#  was a stage in the same seaweed's life cycle. Hatchery seeding became
#  possible and the industry was transformed. The work was taxonomic, with no
#  application in view. She never visited Japan; there is a memorial to her
#  there.
#
#  THE RISK IS BIOLOGICAL, NOT TECHNICAL
#  The farming is easy and needs little capital, which is precisely why
#  breeding was neglected. Tropical carrageenan crops have been propagated
#  vegetatively for decades from a narrow founding stock, so a whole growing
#  region is effectively one genotype. When ice-ice disease and epiphyte
#  outbreaks arrived they met no resistance anywhere, and regional industries
#  collapsed within a season.
#
#  `metrics.py` records effective population size for this crop, the same
#  measure `green.animal_biotechnology` uses for livestock breeds, and it is
#  low for the same reason.
#
#  THE GOVERNANCE QUESTION THAT SCARCELY ARISES ELSEWHERE
#  WHO HAS THE RIGHT TO USE A PIECE OF SEA? A terrestrial farm sits on owned
#  and registered land. A seaweed farm occupies public water that fishing,
#  shipping, tourism, conservation and customary community rights all have
#  claims on, frequently with no register and no procedure for deciding between
#  them. This is the principal barrier to expansion outside Asia, and it is
#  administrative rather than biological.
#
#  A related point a European account would miss: most world production is by
#  smallholders under customary tenure, and formalising marine rights can
#  dispossess the people already farming as readily as it can protect them.
#
#  THE CLAIM THIS RECORD REFUSES TO MAKE
#  Carbon sequestration. Carbon fixed in a crop that is eaten, fed or extracted
#  returns to the atmosphere within months, so `metrics.py` records carbon
#  retention time precisely because it is usually omitted, and `linkage.py`
#  declines SDG 13 while claiming SDG 14 on nutrient removal, which is
#  measurable and real. Separating the defensible claims from the indefensible
#  one strengthens the sector's case rather than weakening it.
#
#  PACKAGE LAYOUT
#      narrative.py    the scale correction, and the orchard analogy whose
#                      missing fence is the record's principal difficulty
#      practice.py     two established industries, then proposals labelled as
#                      proposals
#      metrics.py      twelve metrics, every one stating its moisture basis,
#                      including the ones that constrain the sector's claims
#      history.py      1658 to 2021, centred on 1949
#      governance.py   who has the right to use a piece of sea
#      linkage.py      why SDG 13 is declined and SDG 5 is claimed
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
KEY = "seaweed_cultivation"

NAME = "Seaweed Cultivation"

# "macroalgae" is the precise term that distinguishes this record from
# `blue.algal_biotechnology`. "kelp farming" and "ocean farming" are what a
# reader in Europe or North America is most likely to search for, and
# "hydrocolloids" brings in the half of the industry that is not food.
ALIASES = (
    "macroalgae cultivation",
    "seaweed farming",
    "kelp farming",
    "ocean farming",
    "marine agronomy",
    "hydrocolloid production",
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
