# =============================================================================
#  biotechnology.branches.green.molecular_plant_breeding
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  GREEN BIOTECHNOLOGY  ->  MOLECULAR PLANT BREEDING
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Ordinary plant breeding, made far faster by reading a seedling's DNA to
#  predict what the adult plant will be like, instead of waiting a season to
#  find out.
#
#  THE QUIET GIANT OF THE GREEN BRANCH
#  Genetic engineering attracts the argument. Marker-assisted and genomic
#  selection delivered most of the actual yield gain. Almost all of the
#  improvement in the world's staple crops over the last thirty years came from
#  breeding, and molecular tools roughly doubled the rate at which breeders can
#  deliver it.
#
#  Nothing here creates a genetically modified organism. The alleles being
#  selected already exist in the species, and every plant produced this way
#  could have been produced by a breeder with a paintbrush and enough seasons.
#  Only the speed of choosing changed. That is why this is the only record in
#  the green branch with RISK_TIER = ROUTINE and REGULATORY_STATUS =
#  UNREGULATED, and it is the most useful single fact in the record.
#
#  THE EQUATION THE WHOLE FIELD RUNS ON
#      dG/t = (i * r * sigma_A) / L
#
#  Genetic gain per year equals selection intensity, times prediction accuracy,
#  times additive genetic standard deviation, divided by generation interval.
#  Every metric in `metrics.py` is one of those four terms, and every
#  technology in `practice.py` exists to improve one.
#
#  It also explains a decision that looks irrational from outside: a breeder
#  will deliberately accept LOWER prediction accuracy in exchange for a SHORTER
#  cycle, because r sits in the numerator and L sits in the denominator.
#  Halving L beats a modest loss in r.
#
#  THE SETBACK WORTH KNOWING
#  Two decades of quantitative trait locus mapping produced thousands of
#  publications and very few varieties. Loci found in one population failed to
#  replicate in another, and effects estimated in small populations were
#  systematically overstated. The 2001 genomic selection paper resolved it by
#  giving up on finding significant markers altogether: fit all of them, accept
#  that no individual effect is estimable, and predict the total.
#
#  WHERE THE COST NOW SITS
#  Genotyping is cheap. Phenotyping is not. Measuring a thousand plots
#  accurately is expensive, unglamorous and poorly funded, and it is the
#  bottleneck. The largest single improvement available to the field, meaning
#  larger and more diverse training populations, is blocked by commercial data
#  confidentiality rather than by any scientific difficulty.
#
#  PACKAGE LAYOUT
#      narrative.py    the form-guide analogy, with its real weakness stated
#      practice.py     applications grouped by genetic architecture, since that
#                      decides the method
#      metrics.py      eight metrics, all terms of one equation
#      history.py      domestication to 2020, including the mapping era that
#                      produced papers rather than varieties
#      governance.py   why nothing regulates the technique, and what regulates
#                      the variety instead
#      linkage.py      the shared-method edge to livestock breeding
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
KEY = "molecular_plant_breeding"

NAME = "Molecular Plant Breeding"

# "mas" and "genomic selection" are the two methods this record covers, and
# most readers arrive with one or the other rather than with the umbrella term.
# "plant breeding" resolves here too, because a reader searching for it is
# almost certainly looking for how it is done now.
ALIASES = (
    "marker assisted selection",
    "mas",
    "genomic selection",
    "genomic prediction",
    "plant breeding",
    "speed breeding",
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
