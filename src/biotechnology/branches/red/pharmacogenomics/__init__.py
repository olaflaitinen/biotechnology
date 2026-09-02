# =============================================================================
#  biotechnology.branches.red.pharmacogenomics
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  RED BIOTECHNOLOGY  ->  PHARMACOGENOMICS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  The same dose of the same medicine does not do the same thing to everyone.
#  Pharmacogenomics reads the genes that control how a person processes a drug
#  and adjusts the prescription before the harm happens rather than after.
#
#  WHAT MAKES THIS RECORD DIFFERENT FROM ITS NEIGHBOURS
#  Every other subtype in the red branch is limited by something scientific.
#  This one is not. The genes are known, the variants are catalogued, the
#  prescribing guidelines are written and free to read, and the test costs less
#  than a single day in a hospital bed.
#
#  Debrisoquine polymorphism was described in 1977 and characterised
#  molecularly in 1988. Routine pre-emptive panel testing began appearing in
#  European health systems only in the 2020s. Four decades separate a solved
#  scientific problem from a delivered clinical one, and nothing in that gap
#  was a laboratory difficulty. It was electronic health records,
#  reimbursement rules and clinical workflow.
#
#  That is why `narrative.WHY_IT_MATTERS` spends its final paragraph on
#  implementation, why `practice.CHALLENGES` lists one technical problem and
#  six structural ones, and why `history.py` records a label change that
#  changed nothing as a setback.
#
#  SCOPE BOUNDARY
#      germline variation, inherited      -> this record
#      somatic variation, acquired by a
#      tumour and used to pick a therapy  -> red.molecular_diagnostics
#
#  THE THING A READER SHOULD NOT ASSUME
#  The activity score looks like a measurement and is not. It is a consensus
#  construct: an expert panel assigns 1, 0.5 or 0 to each allele, the
#  assignments have been revised, and two laboratories using different versions
#  of the table can report different phenotypes from identical genotype data.
#  `metrics.py` says so plainly.
#
#  PACKAGE LAYOUT
#      narrative.py    ends on implementation, not on biology
#      practice.py     applications grouped by the kind of harm prevented
#      metrics.py      eight metrics from two disciplines that meet here
#      history.py      1957 to 2023, and the gap between the dates
#      governance.py   three unreconciled regimes: device, label, data
#      linkage.py      why the privacy edge is not optional here
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
KEY = "pharmacogenomics"

NAME = "Pharmacogenomics"

# "pharmacogenetics" is the older term for the same field, still widely used,
# and historically meant single-gene work while pharmacogenomics meant
# genome-wide. The distinction has largely dissolved. "precision medicine" and
# "personalised medicine" are broader marketing terms that most people arrive
# with, so both resolve here.
ALIASES = (
    "pharmacogenetics",
    "pgx",
    "precision medicine",
    "personalised medicine",
    "personalized medicine",
    "drug gene interaction",
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
