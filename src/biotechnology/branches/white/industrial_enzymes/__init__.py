# =============================================================================
#  biotechnology.branches.white.industrial_enzymes
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  INDUSTRIAL ENZYMES
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Purifying and selling the tools that living things use to build and break
#  molecules, so that factories can work in warm water instead of with heat,
#  pressure and solvents.
#
#  THE RECORD YOU HAVE ALREADY USED TODAY
#  Enzymes are in the washing powder, the bread, the cheese, the fruit juice,
#  the denim and the animal feed. This is the least visible and most widely
#  encountered subtype in the library, and `narrative.PLAIN_LANGUAGE` opens
#  there deliberately: an abstract subject becomes concrete fastest when the
#  reader is pointed at their own kitchen.
#
#  THE ONE NUMBER WORTH REMEMBERING
#  Detergent enzymes are why a domestic wash cleans at 30 degrees rather than
#  60, and a 30 degree wash uses roughly a third of the electricity. Across the
#  world's washing machines that is one of the largest emissions reductions
#  attributable to any biotechnology. Almost nobody knows it happened, which is
#  a fair summary of the branch as a whole.
#
#  THE THREE PROPERTIES THAT ARE THE ENTIRE COMMERCIAL CASE
#      water, near ambient temperature, near neutral pH   -> less energy
#      one reaction rather than a mixture                 -> fewer separations
#      chiral by construction                             -> one mirror image
#
#  Everything else in this record follows from those three.
#
#  THE MISTAKE THIS RECORD IS BUILT TO CORRECT
#  A biochemistry course measures an enzyme by k_cat and K_M. An industrial
#  buyer measures the same enzyme by TOTAL TURNOVER NUMBER, meaning how many
#  molecules it converts before it dies, and by cost per kilogram of product.
#
#  A variant with twice the speed and half the working life is a WORSE product.
#  `metrics.py` is therefore ordered process figures first and kinetics second,
#  which is the reverse of a textbook and the right way round for this field.
#  Most engineering effort here goes into stability, not into speed.
#
#  ENGINEERING RAN AHEAD OF THEORY, AND STILL DOES
#  Directed evolution improved enzymes from 1993 onwards without any
#  understanding of why the mutations helped, and for many targets it still
#  beats rational design. The 2018 Nobel citation says as much explicitly. Even
#  now, deep learning predicts a structure for any sequence but does not
#  predict activity or stability, so the screening bottleneck recorded in
#  `practice.CHALLENGES` is unchanged.
#
#  THE SETBACK THAT SHAPED THE PRODUCTS
#  In 1969 occupational asthma among detergent factory workers nearly ended the
#  industry. Enzymes are potent respiratory sensitisers. The response was to
#  encapsulate and granulate every product, which is why detergent enzymes are
#  sold as coated granules to this day, and why the occupational exposure
#  entries appear FIRST in `governance.py` rather than last.
#
#  A GOVERNANCE POINT WORTH CARRYING AWAY
#  The enzyme is regulated as a CHEMICAL, not as an organism. The modified
#  microorganism that made it stays in the fermenter and is removed during
#  purification, so the product falls under chemicals, food additive and
#  occupational law rather than under the deliberate release regime that
#  governs `green.plant_genetic_engineering`. That legal distinction is why
#  fermentation-produced chymosin entered the food supply in 1988 with almost
#  none of the opposition later directed at modified crops.
#
#  PACKAGE LAYOUT
#      narrative.py    the kitchen, the wash temperature, the key-not-hammer
#                      analogy that the branch header uses at larger scale
#      practice.py     applications by INDUSTRY in descending volume, so that a
#                      reader sees detergent and feed above pharmaceuticals
#      metrics.py      twelve metrics, process economics before kinetics
#      history.py      1833 to 2021, including the 1969 setback
#      governance.py   occupational law first, then food, feed and chemicals
#      linkage.py      the boundary with `white.biocatalysis`, stated explicitly
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
KEY = "industrial_enzymes"

NAME = "Industrial Enzymes"

# "technical enzymes" is the trade term for the non-food grades. "enzyme
# engineering" and "protein engineering" are what the discovery and
# improvement work is called in the literature, and a reader searching either
# should arrive here rather than at a medical record.
ALIASES = (
    "enzyme technology",
    "technical enzymes",
    "enzyme engineering",
    "protein engineering",
    "detergent enzymes",
    "feed enzymes",
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
