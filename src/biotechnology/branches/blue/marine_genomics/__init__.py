# =============================================================================
#  biotechnology.branches.blue.marine_genomics
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BLUE BIOTECHNOLOGY  ->  MARINE GENOMICS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Reading the DNA of ocean life, including the great majority of it that
#  nobody has ever managed to grow.
#
#  THE FACT THAT ORGANISES THE WHOLE RECORD
#
#      MOST MARINE MICROORGANISMS CANNOT BE CULTURED.
#
#  Fewer than about one in a hundred will grow on a plate. For most of the
#  twentieth century, studying a microbe meant culturing it, so the marine
#  microbial world was described from an unrepresentative minority. The gap
#  between cells counted under a microscope and colonies that appeared was
#  documented in 1932, named the great plate count anomaly, and worked around
#  for fifty years because no method could do anything about it.
#
#  WHAT HAPPENED WHEN THE REQUIREMENT WAS REMOVED
#  Sequencing DNA straight out of seawater did not refine the existing picture.
#  It replaced it.
#
#      1988   Prochlorococcus is described, and turns out to be among the most
#             abundant photosynthetic organisms on Earth. It had been missed
#             because it passed through the filters surveys used.
#      1990   an abundant lineage of marine archaea is found by sequence in
#             ordinary seawater. Archaea had been thought to inhabit extreme
#             environments. A whole domain of life had been mischaracterised.
#
#  That two organisms of that abundance went unnoticed until the method changed
#  is the strongest argument this record can make for its own importance.
#
#  THE ANALOGY, AND WHY ITS LIMIT IS THE POINT
#  `narrative.ANALOGY` uses the man searching for keys under the streetlight,
#  with one difference that matters: the man KNOWS the light covers a small
#  patch. Microbiology did not. The culturable organisms were taken for the
#  ocean's inhabitants rather than the few that tolerated a plate of jelly.
#  Sequencing did not brighten the lamp; it showed how dark the street had
#  always been.
#
#  WHY MARINE SEQUENCING IS A DISTINCT PROBLEM, NOT AN APPLICATION
#      poor references   marine lineages are under-represented, so a large
#                        fraction of marine sequence matches nothing and is
#                        reported as dark matter. That measures the databases
#                        as much as the sample.
#      symbiosis         a sponge genome arrives mixed with the genomes of the
#                        community inside it. Separating them is computational,
#                        not laboratory work.
#      inverted costs    ship time and submersibles cost far more than the
#                        sequencing, so access to a VESSEL rather than to a
#                        sequencer decides what gets studied.
#
#  THE FIRST METRIC IS A MEASURE OF IGNORANCE
#  `metrics.py` opens with the unassigned sequence fraction, the proportion of
#  reads matching nothing known. It is high. Reporting it first rather than
#  burying it is the difference between a field that knows what it does not
#  know and one that describes only what it found.
#
#  TWO SETBACKS, BOTH UNUSUAL
#  In 2010 the field's productivity became its problem: sequence accumulated
#  faster than anyone could identify it, and the honest reading was ambiguous
#  between genuinely novel biology and absence from skewed databases.
#  Sequencing more did not help, since the reference gap grew with the data.
#
#  In 2023 an international agreement finally addressed marine genetic
#  resources beyond national jurisdiction. It is recorded as both milestone and
#  setback: two thirds of the ocean had no rule at all, decades of collection
#  and patenting happened in that gap, and the framework does not retroactively
#  settle what was taken.
#
#  THE VOCABULARY VALUES WORTH CHECKING
#      SCALE = POPULATION       the unit of study is a community or a water
#                               mass, not an organism and not a vessel.
#      RISK_TIER = CONTROLLED   the permit is not a biosafety permit. What
#                               needs permission is COLLECTION, and a
#                               researcher may need four separate permissions
#                               before a bottle enters the water.
#      STATUS = NOTIFIED        nothing is approved as a product; states are
#                               informed and consent is obtained.
#
#  PACKAGE LAYOUT
#      narrative.py    the culture problem and the streetlight
#      practice.py     applications by WHICH QUESTION is asked; the organisms
#                      are reference points, not production hosts
#      metrics.py      eleven metrics, opening with a measure of ignorance
#      history.py      1932 to 2023, pivoting on 1985
#      governance.py   the three ocean zones, and which law applies in each
#      linkage.py      why SDG 3 is deliberately not claimed here
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
KEY = "marine_genomics"

NAME = "Marine Genomics"

# "marine metagenomics" is the technique that made the field, and "eDNA" is
# what most readers outside the field will have encountered, so both must
# resolve here. "ocean sequencing" is the plain phrase people actually search.
ALIASES = (
    "marine metagenomics",
    "ocean genomics",
    "environmental dna",
    "edna",
    "marine microbial ecology",
    "ocean sequencing",
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
