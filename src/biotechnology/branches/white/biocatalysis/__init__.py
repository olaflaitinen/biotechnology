# =============================================================================
#  biotechnology.branches.white.biocatalysis
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  BIOCATALYSIS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Designing the manufacture of a chemical around enzymes, so that the plant
#  makes one mirror image of a molecule in warm water instead of making both
#  and discarding half under heat, pressure and solvent.
#
#  READ THIS FIRST: THE BOUNDARY WITH THE NEIGHBOURING RECORD
#  `white.industrial_enzymes` and this record are easily confused and are
#  deliberately kept apart.
#
#      industrial_enzymes   the enzyme as a MANUFACTURED ARTICLE
#                           discovery, engineering, fermentation, formulation,
#                           sale. Measured by k_cat, titre, cost per kilogram
#                           of enzyme.
#
#      biocatalysis         the enzyme as a STEP IN A SYNTHETIC ROUTE
#                           which disconnection, what medium, what substrate
#                           loading, cofactor paid for how. Measured by
#                           substrate loading, cofactor turnover, process mass
#                           intensity.
#
#  One supplies the tool; the other decides what to build with it. Both records
#  state this boundary in their linkage facets, from their own side.
#
#  WHY HANDEDNESS IS THE ORGANISING IDEA
#  Many molecules exist as two non-superimposable mirror images. In a medicine
#  one may be the drug and the other inert or harmful. Conventional catalysis
#  frequently makes both and then discards half the output. An enzyme is itself
#  handed and typically makes one. That single property is what turns a
#  biocatalytic route from a cheaper option into sometimes the only sensible
#  one, and it is why `narrative.ANALOGY` is about gloves rather than locks.
#
#  THE THREE NUMBERS THAT KILL ROUTES
#  `metrics.py` is ordered to put these first, ahead of anything elegant:
#
#      substrate loading      enzymes work in water, substrates often do not.
#                             A reaction at 2 g/L may be two orders of
#                             magnitude from manufacturable.
#      cofactor turnover      a nicotinamide cofactor used once costs more
#                             than the product. Recycled ten thousand times it
#                             costs almost nothing. This ratio, not the
#                             enzyme's own turnover, usually governs.
#      biocatalyst yield      kilograms of product per kilogram of enzyme,
#                             which is what decides whether immobilisation
#                             earns its development cost.
#
#  THE WARNING THIS RECORD INSISTS ON
#  Enantiomeric excess is the most quoted and most flattering number in the
#  field. Ninety-nine per cent reads as near-perfect and means one part in two
#  hundred is the wrong hand. It also says nothing about how much product
#  exists: a kinetic resolution can post an excellent ee at low conversion
#  precisely BECAUSE it has barely run. Always read it beside conversion.
#
#  TWO SETBACKS, AND NEITHER IS AN ACCIDENT
#  Unusually for this library, both setbacks in `history.py` are cases where
#  the field promised more than it delivered and had to correct its own
#  account. In 1984 enzymes were shown to work in organic solvents, and the
#  anticipated general-purpose solvent-tolerant biocatalysis never arrived;
#  activity in organic media runs orders of magnitude below activity in water.
#  In 2008 computationally designed enzymes catalysed reactions nature never
#  invented, and were so slow that directed evolution had to rescue them. Both
#  results were real. Both surrounding claims were not.
#
#  THE CASE THAT CHANGED THE FIELD
#  The 2010 sitagliptin transaminase. The starting enzyme did not accept the
#  substrate at all; directed evolution produced one that worked at
#  manufacturing concentration. The new route removed a high-pressure
#  hydrogenation, eliminated the rhodium catalyst and the metal removal step,
#  raised yield and cut waste. What it proved matters more than what it made:
#  an enzyme can be engineered to fit a route chosen for other reasons, rather
#  than the route being bent around whatever enzyme happened to exist.
#
#  A GOVERNANCE POINT WORTH CARRYING AWAY
#  The regulated thing here is THE ROUTE, NOT THE PRODUCT. The molecule is
#  identical however it was made, but under ICH Q11 the synthetic route sits
#  inside the approved dossier, and changing it needs a variation. So the
#  choice to go enzymatic is made once, early, and then locked for the
#  product's commercial life. Against that, biocatalysis is one of the few
#  technologies in this library that makes a regulatory burden SMALLER: a route
#  with no metal catalyst has no elemental impurity to control under ICH Q3D.
#
#  PACKAGE LAYOUT
#      narrative.py    handedness, the four reaction classes, and where the
#                      field genuinely loses to chemistry
#      practice.py     applications by REACTION CLASS, not by industry, since
#                      a chemist chooses by bond rather than by sector
#      metrics.py      eleven metrics, route-killing constraints first
#      history.py      1858 to 2022, with two overpromises recorded honestly
#      governance.py   why an approved route is expensive to improve
#      linkage.py      the reciprocal boundary, and metabolic engineering as
#                      the genuine strategic alternative
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
KEY = "biocatalysis"

NAME = "Biocatalysis and Enzymatic Synthesis"

# "biotransformation" is the older term and still standard for whole-cell work.
# "chemoenzymatic synthesis" is what most real routes are, since enzymatic and
# conventional steps alternate. "green chemistry" is included because it is the
# framing under which this work is funded and justified inside companies, even
# though it is broader than this record.
ALIASES = (
    "biotransformation",
    "enzymatic synthesis",
    "chemoenzymatic synthesis",
    "applied biocatalysis",
    "green chemistry",
    "whole cell biocatalysis",
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
