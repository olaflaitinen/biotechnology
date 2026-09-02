# =============================================================================
#  biotechnology.branches.green.animal_biotechnology
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  GREEN BIOTECHNOLOGY  ->  ANIMAL BIOTECHNOLOGY
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Applying reproductive and genetic technology to farm animals so that fewer
#  animals produce more food, get sick less often, and suffer less.
#
#  AN ETHICAL NOTE THAT BELONGS IN THE DATA, NOT A FOOTNOTE
#  This is the only record in the green branch whose subject can suffer. Every
#  technique here acts on a sentient animal.
#
#  Several of them exist SPECIFICALLY to reduce suffering that current farming
#  imposes: removing horn growth so calves are not disbudded with a hot iron,
#  making pigs immune to a virus that kills millions a year, breeding cattle
#  that tolerate heat. Others raise welfare concerns of their own, particularly
#  selection pressed hard on production traits. Both directions are recorded,
#  and `linkage.py` points at `purple.bioethics` rather than implying the
#  question is settled.
#
#  Public opinion distinguishes sharply between an edit that reduces suffering
#  and one that increases output. The underlying science does not. That gap is
#  stated in `practice.CHALLENGES` as a challenge rather than resolved.
#
#  THE THREE LAYERS
#      1. REPRODUCTION multiplies the influence of chosen parents.
#      2. GENOMICS changes how those parents are chosen.
#      3. EDITING alters the animal directly.
#
#  Each has a different maturity, a different regulator and a different public
#  reception, which is why `governance.py` is organised around three separate
#  legal threads rather than one.
#
#  THE TRADE THAT DEFINES THE RECORD
#  Genomic selection did NOT improve prediction accuracy. A progeny-tested bull
#  is measured far more accurately than any genomic prediction. What it did was
#  cut the generation interval from about five years to about two, and because
#  L sits in the denominator of
#
#      dG/t = (i * r * sigma_A) / L
#
#  that nearly doubled annual genetic gain WHILE ACCEPTING LOWER ACCURACY. The
#  dairy industry abandoned a progeny testing system that had organised it for
#  half a century, within about three years.
#
#  THE ASYMMETRY THAT EXPLAINS THE REST
#  One bull can sire tens of thousands of calves; one cow produces a handful.
#  Selection intensity is therefore enormous on the male side and nearly fixed
#  on the female side. That is why embryo technologies exist, and why the male
#  side contributes most genetic progress and most of the loss of diversity.
#
#  WHAT THE GAIN COSTS
#  Major dairy breeds with millions of animals have an effective population
#  size of 50 to 150, a range a conservation biologist would call unsustainable.
#  And selecting hard on milk yield carried declining fertility with it for
#  decades until the breeding index was deliberately rewritten, which is the
#  clearest demonstration anywhere in this library that a selection index is an
#  ethical choice rather than a measurement.
#
#  PACKAGE LAYOUT
#      narrative.py    the racehorse analogy, with its real limit stated
#      practice.py     applications by layer, then by welfare or production
#                      purpose, because that is the split people actually make
#      metrics.py      nine metrics; six are gain terms and three are costs
#      history.py      1780 to 2025, including Dolly and two setbacks
#      governance.py   welfare law, breeding law and medicines law at once
#      linkage.py      the shared equation, and what Dolly actually led to
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
KEY = "animal_biotechnology"

NAME = "Animal Biotechnology"

# "livestock genomics" and "animal breeding" are what practitioners call the
# second layer, which is where most of the activity is. "cloning" is included
# because it is what most people associate with the field, even though it is
# commercially the smallest part of it.
ALIASES = (
    "livestock genomics",
    "animal breeding",
    "reproductive technology",
    "livestock genetics",
    "cloning",
    "gene edited livestock",
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
