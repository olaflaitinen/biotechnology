# =============================================================================
#  biotechnology.branches.white.metabolic_engineering
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  METABOLIC ENGINEERING
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Rearranging the chemical factory that every living cell already is, so that
#  it turns cheap sugar into something we want rather than only into more of
#  itself.
#
#  THE ONE IDEA TO TAKE AWAY: THERE IS NO RATE-LIMITING STEP
#  This is the misconception the record is built to correct, and it is stated
#  in the narrative rather than buried in the metrics.
#
#  Metabolic control analysis showed in 1973 that control over a pathway's
#  output is DISTRIBUTED, and that the flux control coefficients of its enzymes
#  SUM TO ONE. An enzyme with a coefficient of 0.2 returns only a fifth of any
#  improvement made to it. So overexpressing the apparent bottleneck typically
#  does not raise output; it moves the control somewhere else. A generation of
#  disappointing results came from assuming otherwise, and the assumption is
#  still common in summaries of the field.
#
#  `narrative.ANALOGY` uses city traffic for exactly this reason. Widening the
#  worst junction does not shorten the journey, because the queue re-forms at
#  the next one. Congestion was a property of the network, not of a place.
#
#  THE BOUNDARY WITH BIOCATALYSIS
#  `white.biocatalysis` names this record as its strategic alternative, and the
#  choice between them is a real engineering decision with no general answer:
#
#      biocatalysis            a few steps, outside a cell. Total control of
#                              medium and temperature; every cofactor paid for.
#      metabolic engineering   the whole pathway inside a living organism. Free
#                              cofactor regeneration and self-repairing
#                              catalysts; in exchange the organism grows,
#                              mutates and spends carbon staying alive.
#
#  Long pathways with expensive cofactors favour the cell. Short pathways with
#  toxic or insoluble substrates favour the isolated enzyme.
#
#  THE HISTORY IS NOT A PROGRESSION FROM CRUDE TO RATIONAL
#  The two largest products in this field, glutamate from 1957 and lysine
#  shortly after, predate the discipline's name by more than thirty years and
#  were built by mutagenesis and selection with no molecular biology at all.
#  Adaptive laboratory evolution, an explicitly non-rational method, is in
#  routine industrial use today. A reader expecting a clean march towards
#  design will not find one here.
#
#  THE MOST INSTRUCTIVE FAILURE IN THE LIBRARY
#  Yeast engineered to make artemisinic acid, the precursor of the antimalarial
#  artemisinin, was a genuine scientific landmark. The strain worked. The
#  process worked. The product met specification. It then lost commercially to
#  farmers growing sweet wormwood more cheaply, and production was largely
#  idled within a few years.
#
#  Nothing went wrong scientifically, which is precisely why it is recorded at
#  length. A working pathway is not a viable product; an agricultural supply
#  chain of millions of low-cost growers is far harder to displace than it
#  looks; and what survived was value as a supply and price buffer rather than
#  as a replacement.
#
#  WHY THE METRICS FACET ARGUES WITH ITS OWN FIELD
#  Everyone quotes titre, rate and yield. That trio is incomplete, and
#  `metrics.py` is ordered to show what it hides:
#
#      the ceiling      yield is uninterpretable without the stoichiometric
#                       maximum it is measured against. 0.3 g/g may be
#                       excellent or poor.
#      the stability    a strain that loses productivity over a hundred
#                       generations does not survive a production run, and TRY
#                       is measured long before that matters.
#      the control      the flux control coefficient tells an engineer WHERE to
#                       intervene, which the trio never does.
#
#  WHY THE REGULATORY STATUS IS `VARIES`
#  This record is why that value exists. Contained use rules govern the
#  organism identically whatever it makes. Everything afterwards depends on the
#  molecule: a food ingredient meets novel food law, a feed amino acid meets
#  feed additive law, a drug substance meets GMP, a polymer precursor meets
#  chemicals law. The same strain technology faces five different regulators.
#  That dispersal is the finding, not a gap in the record.
#
#  PACKAGE LAYOUT
#      narrative.py    the distributed-control correction, and the traffic
#                      analogy chosen to carry it
#      practice.py     applications from the 1950s amino acids to gas
#                      fermentation; technologies as the design, build, test,
#                      learn cycle, showing where the bottleneck now sits
#      metrics.py      eleven metrics, arguing with the standard trio
#      history.py      1957 to 2022, with the artemisinin case in full
#      governance.py   why this technology has no regulator of its own
#      linkage.py      the reciprocal boundary with biocatalysis
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
KEY = "metabolic_engineering"

NAME = "Metabolic Engineering"

# "strain engineering" and "cell factory design" are what the work is called in
# industry. "systems metabolic engineering" is the term for the model-guided
# form specifically. "pathway engineering" is included because a reader
# searching for how a natural product route is reconstituted should land here.
ALIASES = (
    "strain engineering",
    "cell factory design",
    "pathway engineering",
    "systems metabolic engineering",
    "industrial strain development",
    "microbial cell factories",
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
