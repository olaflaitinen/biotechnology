# =============================================================================
#  biotechnology.branches.blue.algal_biotechnology
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BLUE BIOTECHNOLOGY  ->  ALGAL BIOTECHNOLOGY
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Growing microscopic algae in water for the pigments, oils and proteins they
#  make, and dealing with the fact that a tank of algae is almost entirely
#  water.
#
#  THE ONE SENTENCE THAT EXPLAINS BOTH THE SUCCESSES AND THE FAILURES
#
#      THE BIOLOGY WAS NEVER THE PROBLEM. THE HARVEST WAS.
#
#  Microalgae genuinely are among the most productive photosynthetic organisms
#  known, and the projections made for them were not fabricated. What defeats
#  applications is that a culture holds about a gram of dry biomass per litre,
#  so recovering a tonne of biomass means processing roughly a thousand tonnes
#  of water. Concentrating that costs energy.
#
#  AND THE COROLLARY, WHICH IS WHERE THE FIELD SUCCEEDED
#  That harvest cost is roughly the SAME whatever is being grown. So:
#
#      product worth tens of thousands per tonne   the cost is a rounding error
#                                                  -> profitable for decades
#      product worth a few hundred per tonne       the cost exceeds the product
#                                                  -> two failed fuel programmes
#
#  One constraint, both outcomes. `practice.APPLICATIONS` is therefore ordered
#  BY PRODUCT VALUE PER TONNE, highest first, so a reader moving down the list
#  watches the economics deteriorate and reaches the fuel entries exactly where
#  they stop working. Nothing technical separates the top of that list from the
#  bottom: the same organisms, the same ponds, the same centrifuges.
#
#  THE FIELD MADE THE SAME MISTAKE TWICE, AND THAT IS THE LESSON
#  A national algal fuel programme ran from 1978 to 1996 and concluded, in an
#  unusually candid final report, that the approach could not compete at
#  prevailing oil prices. It named low density, harvest cost, contamination and
#  the laboratory-to-outdoor productivity gap.
#
#  About a decade later a second, much larger wave of investment began against
#  projections built by extrapolating laboratory productivity to open systems,
#  which is precisely what the earlier report had shown to be unsound. It ended
#  the same way. Most companies then redirected to high-value products and
#  several became profitable, which is the resolution rather than a further
#  failure.
#
#  TWO WAYS THIS FIELD'S NUMBERS MISLEAD, BOTH RECORDED IN `metrics.py`
#      areal productivity   short-term laboratory values are several times what
#                           an outdoor system sustains annually. Both figures
#                           are recorded, because quoting only the higher one
#                           is how the fuel projections were built.
#      lipid content        raised by starving the culture, and starved cells
#                           stop dividing. Fraction and total output move in
#                           OPPOSITE directions, so fifty per cent lipid can
#                           mean less oil per hectare than twenty. Lipid
#                           productivity is the honest figure.
#
#  THE GOVERNANCE FACT THAT SURPRISES PEOPLE ARRIVING FROM THE FUEL STORY
#  This field is principally regulated as FOOD. Almost every commercial success
#  is eaten, by a person or a farmed animal, so novel food authorisation, feed
#  additive authorisation and food hygiene law are what actually govern it.
#
#  The practical consequence is a barrier to new species: the handful with a
#  history of consumption can be sold, while a newly isolated species with
#  better productivity needs a safety dossier and years. That is a REGULATORY
#  explanation for what looks like scientific conservatism in the organism list.
#
#  And because an open pond can be colonised by a toxin-producing
#  cyanobacterium, toxin monitoring is routine rather than exceptional in
#  food-grade production. What grows in the pond is not only what was put there.
#
#  THE BOUNDARY WITH THE NEIGHBOURING RECORD
#  `blue.seaweed_cultivation` is drawn at the ORGANISM, not the application.
#  Microalgae are single cells in suspension and must be separated from water.
#  Macroalgae are large, grow on lines, and are lifted out. The harvest
#  constraint that governs everything here does not exist there, which is why
#  the economics differ completely.
#
#  PACKAGE LAYOUT
#      narrative.py    the harvest constraint, and the panning analogy
#      practice.py     applications ordered BY VALUE PER TONNE, so the argument
#                      is demonstrated rather than asserted
#      metrics.py      twelve metrics opening with culture density, and warning
#                      about the two figures that mislead
#      history.py      1940 to 2021, with the same setback recorded twice
#      governance.py   why this is food law rather than energy law
#      linkage.py      why SDG 7 is deliberately not claimed
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
KEY = "algal_biotechnology"

NAME = "Algal Biotechnology"

# "microalgae" is the precise term and the one that distinguishes this record
# from `blue.seaweed_cultivation`. "algae biofuel" is included deliberately:
# it is what many readers will search for, and this is the record that explains
# honestly why it did not work.
ALIASES = (
    "microalgae",
    "microalgal cultivation",
    "cyanobacteria biotechnology",
    "algae biofuel",
    "phycotechnology",
    "algal cultivation",
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
