# =============================================================================
#  biotechnology.branches.green.biopesticides
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  GREEN BIOTECHNOLOGY  ->  BIOPESTICIDES AND BIOLOGICAL
#                                               CONTROL
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Using living organisms, or substances they make, to control crop pests: a
#  predator, a disease of the pest, or a natural toxin, instead of a
#  broad-spectrum synthetic chemical.
#
#  THE TRADE-OFF THAT IS THE WHOLE RECORD
#  Biopesticides are narrow. That is simultaneously the entire ecological
#  benefit and the entire commercial problem, and neither half is a consequence
#  of the other being overstated.
#
#  A product that kills one pest species spares pollinators, natural enemies
#  and soil fauna, and leaves no residue. The same product has a small market
#  and still needs a full registration dossier. Selectivity does both things at
#  once.
#
#  THE TWO CORRECTIONS IN metrics.py
#  LC50 and LT50 are not interchangeable, and for biological control the second
#  usually decides adoption. A fungus with an excellent LC50 and an LT50 of
#  eight days loses a crop a grower needed protected in three. Comparing a
#  biopesticide with a synthetic on LC50 alone flatters it and then disappoints
#  in the field.
#
#  Mortality must be corrected for the untreated control. Insects die in
#  untreated plots too, and an uncorrected figure can overstate efficacy by
#  tens of percentage points.
#
#  THE REGULATORY OUTCOME NOBODY WANTED
#  The modern pesticide framework was built after Silent Spring to control
#  persistent synthetic molecules. Applied to a fungus that dies in sunlight
#  within two days, most of its data requirements answer questions that cannot
#  arise. The result is a sector dominated by a handful of organisms registered
#  decades ago. Regulation (EU) 2022/1439 is the first serious correction, and
#  `governance.py` explains why it matters more than any technical advance of
#  the last twenty years.
#
#  TWO EDGES THAT COMPLETE THE RECORD
#  `green.plant_genetic_engineering` uses the same Bt proteins, moved into the
#  plant instead of sprayed onto it. Deploying one protein both ways across the
#  same landscape doubled the selection pressure on the same resistance allele,
#  and field-evolved resistance followed where refuges were not enforced.
#
#  `green.biofertilisers` is separated from this record by a claim on a label
#  rather than by biology: the same Bacillus strain, sold for root growth or
#  for pathogen suppression, at one to two orders of magnitude different
#  dossier cost.
#
#  PACKAGE LAYOUT
#      narrative.py    the sniffer dog, whose limit is the trade-off itself
#      practice.py     applications grouped by mode of action, including the
#                      group that kills nothing at all
#      metrics.py      nine metrics, with the two corrections stated first
#      history.py      1888 to 2022, including Silent Spring and Bt resistance
#      governance.py   a framework built for the opposite kind of substance
#      linkage.py      the shared protein, and the label that draws the line
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
KEY = "biopesticides"

NAME = "Biopesticides and Biological Control"

# "bt spray" is included because it is what most growers call the largest
# product in the category, and "ipm" because integrated pest management is the
# framework people arrive looking for even when the specific question is about
# a product.
ALIASES = (
    "biocontrol",
    "biological control",
    "biopesticide",
    "bt spray",
    "integrated pest management",
    "ipm",
    "biological pest control",
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
