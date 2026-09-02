# =============================================================================
#  biotechnology.branches.green.plant_tissue_culture
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  GREEN BIOTECHNOLOGY  ->  PLANT TISSUE CULTURE AND
#                                               MICROPROPAGATION
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Growing whole plants from a few cells in a sterile jar, so that thousands of
#  identical, disease-free seedlings can be produced from one good parent.
#
#  THE INVISIBLE FOUNDATION OF THE GREEN BRANCH
#  Every transgenic plant and every edited plant that has ever existed was
#  regenerated from a single cell in a jar. When a genotype is described as
#  impossible to engineer, the failure is almost never DNA delivery; it is that
#  nobody can persuade that variety to become a plant again.
#
#  `green.plant_genetic_engineering` and `green.agricultural_genome_editing`
#  both DEPEND on this record. It is the only place in the branch where the
#  dependency runs in one clear direction, and neither of those records states
#  it as plainly as it should.
#
#  THE NUMBER THAT IS THE WHOLE BUSINESS CASE AND THE WHOLE RISK
#  Multiplication rate compounds geometrically. A rate of five per cycle gives
#  3125 plants after five cycles and over 390000 after eight. One elite plant
#  becomes a national planting programme inside two years.
#
#  The same exponent multiplies one undetected somaclonal variant, or one
#  latent endophyte, into four hundred thousand defective plants distributed
#  nationally. Every quality metric in `metrics.py` exists to catch that before
#  the exponent does its work, and the subculture cap exists for no other
#  reason.
#
#  It is also why `governance.py` records REGULATORY_STATUS = NOTIFIED rather
#  than UNREGULATED. Nothing regulates the technique. Plant health law governs
#  the output tightly, because propagation delivers a pathogen everywhere at
#  once rather than slowly.
#
#  THE SETBACK WORTH KNOWING
#  Millions of oil palms propagated by somatic embryogenesis produced deformed,
#  largely sterile fruit that appeared only years after planting. The cause was
#  epigenetic, invisible to every genetic test available, and no amount of
#  sequence checking would have caught it. It is why genetic fidelity testing
#  now includes methylation assays.
#
#  A NOTE ON THE VOCABULARY POSITION
#  This is the only record in the green branch that is both RISK_TIER = ROUTINE
#  and SCALE = INDUSTRIAL. A commercial micropropagation laboratory produces
#  tens of millions of plantlets a year in a facility that is a factory in
#  everything but name, while remaining an ordinary laboratory in regulatory
#  terms.
#
#  PACKAGE LAYOUT
#      narrative.py    the photocopier analogy, whose failure mode is the
#                      field's actual quality problem
#      practice.py     applications grouped by purpose, plus the group that
#                      makes two neighbouring records possible
#      metrics.py      nine metrics, with the compounding warning stated first
#      history.py      1902 to 2016, including the oil palm episode
#      governance.py   why plant health law binds and biosafety law does not
#      linkage.py      the dependency direction, and the animal-cell contrast
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
KEY = "plant_tissue_culture"

NAME = "Plant Tissue Culture and Micropropagation"

# "micropropagation" is the commercial term and the one a nursery would use;
# "in vitro culture" is the academic one; "meristem culture" names the specific
# technique most people have heard of, because virus elimination is what makes
# the news. All resolve here.
ALIASES = (
    "micropropagation",
    "in vitro culture",
    "meristem culture",
    "clonal propagation",
    "plant regeneration",
    "somatic embryogenesis",
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
