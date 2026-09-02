# =============================================================================
#  biotechnology.branches.red.vaccine_development
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  RED BIOTECHNOLOGY  ->  VACCINE DEVELOPMENT
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  A vaccine shows the immune system a harmless preview of a germ, so that the
#  body already knows how to fight it if the real thing ever arrives.
#
#  WHY THIS RECORD IS WRITTEN WITH UNUSUAL CARE
#  Vaccination is the single intervention with the largest measured effect on
#  human mortality after clean water, and it is also the subject of more public
#  misunderstanding than anything else in this taxonomy. Two consequences run
#  through every facet:
#
#    * The public register explains the MECHANISM before the BENEFIT. A reader
#      who does not understand how a vaccine works cannot evaluate a claim
#      about one, and most misinformation exploits exactly that gap.
#    * The metrics carry longer notes than anywhere else in the library,
#      because efficacy, effectiveness and herd immunity threshold are the
#      three numbers most often quoted with more confidence than they deserve.
#
#  WHAT IS UNUSUAL ABOUT ITS GOVERNANCE
#  It is the only record in the red branch with SCALE = POPULATION: a vaccine
#  is the one medicine here whose therapeutic unit is a population rather than
#  a patient. And WHO prequalification, a standard with no legal force
#  anywhere, is arguably the most consequential entry in its governance facet,
#  because it decides what United Nations agencies may buy.
#
#  PACKAGE LAYOUT
#      narrative.py    prose, mechanism first, in both registers
#      practice.py     twelve applications, and eight challenges of which six
#                      are not technical
#      metrics.py      the seven numbers that appear in public debate
#      history.py      1721 to 2023, including the 1955 Cutter incident
#      governance.py   batch release, and a voluntary standard as a market gate
#      linkage.py      the One Health and biodefence edges
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
KEY = "vaccine_development"

NAME = "Vaccine Development"

# "immunisation" is the term public health services use; "vaccinology" is the
# academic one; "mrna vaccine" is what most people typed into a search box
# between 2020 and 2022. All three resolve.
ALIASES = (
    "vaccinology",
    "immunisation",
    "immunization",
    "mrna vaccine",
    "prophylactic vaccine",
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
