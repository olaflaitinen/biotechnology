# =============================================================================
#  biotechnology.branches.red.antibody_engineering
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  RED BIOTECHNOLOGY  ->  ANTIBODY ENGINEERING
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Antibodies are the immune system's guided missiles. Antibody engineering
#  redesigns them: sharpening the aim, changing the payload, or building shapes
#  that do not occur in nature at all.
#
#  THE IDEA THAT MAKES THE WHOLE RECORD LEGIBLE
#  MODULARITY. A natural antibody is two functional halves joined together: an
#  end that grips one specific target, and a tail that calls the immune system
#  over to deal with whatever has been gripped. Those halves fold independently
#  and can be separated, swapped, duplicated, silenced, or attached to things
#  that are not antibodies at all.
#
#  Every format in `practice.TECHNOLOGIES` is a consequence of that one fact,
#  and a reader who holds it can follow the entire record without knowing what
#  an immunoglobulin domain is.
#
#  THE CORRECTION THIS RECORD MAKES
#  Tighter binding is not better binding. Below roughly one nanomolar, a
#  tumour-targeting molecule is captured by the first cells it meets and never
#  penetrates the tissue behind them. This is the binding-site barrier, and it
#  means the optimum affinity is often deliberately worse than the best
#  achievable. `metrics.py` says so at length, because the field's own
#  literature routinely reports affinity as though more were always better.
#
#  WHY IT SITS APART FROM PHARMACEUTICAL BIOTECHNOLOGY
#      red.pharmaceutical_biotechnology   how a biologic is MANUFACTURED
#      red.antibody_engineering           how the molecule is DESIGNED
#
#  This record is BENCH scale; that one is INDUSTRIAL. The split is the reason
#  both exist.
#
#  PACKAGE LAYOUT
#      narrative.py    built around modularity, not around immunology
#      practice.py     thirteen applications, from plain blockers to molecules
#                      that no longer look like antibodies
#      metrics.py      eight metrics, including why avidity inflates a
#                      reported affinity
#      history.py      1890 to 2021, including the 2006 TGN1412 trial
#      governance.py   animal use, naming as classification, first-in-human
#                      design after TGN1412
#      linkage.py      the component this record supplies to four other records
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
KEY = "antibody_engineering"

NAME = "Antibody Engineering"

# "monoclonal antibody" is what most readers will search for, even though it
# names one product class rather than the discipline. "nanobody" is a trade
# name in origin but has become the common term for the single-domain format.
ALIASES = (
    "monoclonal antibody",
    "antibody discovery",
    "nanobody",
    "bispecific",
    "antibody drug conjugate",
    "biologics discovery",
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
