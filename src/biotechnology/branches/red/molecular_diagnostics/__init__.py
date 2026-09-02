# =============================================================================
#  biotechnology.branches.red.molecular_diagnostics
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  RED BIOTECHNOLOGY  ->  MOLECULAR DIAGNOSTICS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Instead of waiting to see whether a germ grows in a dish, molecular
#  diagnostics reads the genetic material in a sample directly and says what is
#  there, often within an hour.
#
#  THE ONE THING TO TAKE FROM THIS RECORD
#  A test that is right ninety-nine times out of a hundred can still be wrong
#  most of the times it says yes, when the thing being looked for is rare. That
#  is not a defect in the test; it is arithmetic, and it is the reason
#  `metrics.py` carries the longest notes in the library and why
#  `predictive_values` exists as a formula.
#
#  Sensitivity and specificity are properties of the TEST. Predictive values
#  are properties of the TEST AND THE POPULATION TOGETHER. Almost every public
#  argument about screening is a collision between those two facts.
#
#  WHY THIS RECORD HAS THE WIDEST REACH IN THE TAXONOMY
#  The same three techniques, meaning amplification, sequencing and
#  hybridisation, answer completely different questions in at least six of the
#  ten branches. A laboratory that can detect a virus in a nasal swab can, with
#  the same equipment, detect Salmonella in a carcass, a mislabelled fish in a
#  fillet, a pathogen in a river, an invasive species in seawater, or a
#  deliberately released agent. `linkage.RELATED` makes that navigable, and
#  following those eight edges is the fastest way to see how little of
#  biotechnology is genuinely separate.
#
#  PACKAGE LAYOUT
#      narrative.py    amplification explained before accuracy, deliberately
#      practice.py     thirteen applications; challenges led by interpretation
#      metrics.py      eight metrics, and the arithmetic the public misses
#      history.py      1975 to 2022, including the 2007 pertussis non-outbreak
#      governance.py   the device gate and the laboratory gate, and the
#                      laboratory-developed test question
#      linkage.py      eight edges, seven of them cross-branch
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
KEY = "molecular_diagnostics"

NAME = "Molecular Diagnostics"

# "ivd" is the regulatory abbreviation, "pcr testing" is what most people call
# it, and "clinical genomics" is the term used for the sequencing end of the
# same discipline. All three resolve to this record.
ALIASES = (
    "in vitro diagnostics",
    "ivd",
    "pcr testing",
    "clinical genomics",
    "molecular pathology",
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
