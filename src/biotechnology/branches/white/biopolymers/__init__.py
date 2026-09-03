# =============================================================================
#  biotechnology.branches.white.biopolymers
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  BIOPOLYMERS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Plastics and other polymers made from plants or by living cells, some of
#  which break down afterwards and many of which do not.
#
#  THE CORRECTION THIS RECORD EXISTS TO MAKE
#
#      BIOBASED AND BIODEGRADABLE ARE INDEPENDENT PROPERTIES.
#
#  One says where the carbon came from. The other says what happens at the end.
#  All four combinations are manufactured at scale today:
#
#                       biodegradable          not biodegradable
#      biobased         PLA, PHA, starch       bio-PE, bio-PET
#      fossil           PBAT, PCL              conventional plastics
#
#  A sugarcane-derived polyethylene bottle is chemically identical to a fossil
#  one and persists exactly as long. A certified compostable film may be made
#  entirely from petroleum. `practice.APPLICATIONS` is grouped by these
#  quadrants rather than by industry, so a reader learns the distinction by
#  reading the list rather than by being told twice.
#
#  AND THE SECOND CORRECTION, WHICH IS HARDER
#  Biodegradable on its own means nothing. Biodegradation is A RATE, IN AN
#  ENVIRONMENT, AT A TEMPERATURE. Polylactic acid meets the industrial
#  composting standard at 58 degrees and behaves like ordinary plastic in home
#  compost, in soil and in seawater. Polyhydroxyalkanoates degrade in all of
#  them, because they are natural bacterial storage granules and environmental
#  organisms already carry the enzymes.
#
#  `narrative.ANALOGY` puts it as calling a log burnable: true, and silent on
#  whether it will burn in a damp field. The honest question is never whether a
#  material CAN break down but whether it WILL, where it is actually going.
#
#  A THIRD DISTINCTION, WHICH COST TWO DECADES TO SETTLE
#  DISINTEGRATION IS NOT BIODEGRADATION. A material can pass a disintegration
#  test by fragmenting small enough to fall through a sieve while mineralising
#  almost nothing. That is microplastic formation, not degradation, and it is
#  what oxo-degradable additives did while being marketed as degradable. They
#  were restricted only in 2019. `metrics.py` records the two as separate
#  quantities so they cannot be conflated again.
#
#  THE CONSTRAINT IS NOT CHEMISTRY
#  A compostable item needs an industrial composter that will accept it. Where
#  that infrastructure is absent, the article behaves as ordinary plastic AND
#  contaminates the recycling stream it visually resembles, so it can be worse
#  than the conventional package it replaced. Legislators reached the same
#  conclusion independently: single-use plastic restrictions deliberately did
#  NOT exempt compostable items.
#
#  PLASTICS BEGAN BIOBASED
#  Celluloid, from cellulose, was commercialised in 1869 and casein plastics in
#  1897. The first fully synthetic polymer came in 1907, and petroleum
#  dominated only from mid-century. This record is not introducing a novelty;
#  it is attempting a return against a material that already won on cost and
#  performance once.
#
#  THE SETBACK: THE RIGHT MATERIAL, THE WRONG DECADE
#  A bacterial polyhydroxyalkanoate was commercialised in 1990, genuinely
#  biodegradable in ordinary environments, and sold in consumer packaging.
#  Production ceased by 2001. Nothing was wrong with the material. It cost
#  several times more than polyethylene, recovering a polymer from inside cells
#  proved expensive, and the regulatory and public pressure that would have
#  paid the premium arrived about twenty years too late. The field has been
#  rebuilding that capacity since.
#
#  WHY THE STANDARDS MATTER MORE THAN THE LAW HERE
#  Compostable has no meaning in ordinary use. What gives it meaning is a test
#  standard fixing temperature, medium, duration and threshold, so EN 13432 and
#  its equivalents are the operative definitions rather than background. And
#  they name FOUR DIFFERENT ENVIRONMENTS: industrial compost, home compost,
#  soil and marine. Passing one implies nothing about the others, and
#  presenting an industrial composting certificate as a general environmental
#  credential is the most common misuse of these documents.
#
#  PACKAGE LAYOUT
#      narrative.py    the two axes, and the burnable-log analogy for the
#                      environment-dependence of degradation
#      practice.py     applications BY QUADRANT, each stating its end of life
#      metrics.py      eleven metrics, opening with the two axes side by side
#                      and keeping disintegration separate from mineralisation
#      history.py      1869 to 2023, with two setbacks
#      governance.py   why the standards are the operative definitions
#      linkage.py      the bioremediation edge, which asks whether the claims
#                      hold outside a standardised test
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
KEY = "biopolymers"

NAME = "Biopolymers and Bioplastics"

# "bioplastics" is the term most readers arrive with, and it is precisely the
# ambiguous one: it is used for both axes of the classification above. It is
# included so that a reader searching it lands on the record that explains the
# ambiguity rather than on one that reproduces it. "compostable plastics" is
# included for the same reason.
ALIASES = (
    "bioplastics",
    "biodegradable plastics",
    "compostable plastics",
    "biobased polymers",
    "renewable polymers",
    "polyhydroxyalkanoates",
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
