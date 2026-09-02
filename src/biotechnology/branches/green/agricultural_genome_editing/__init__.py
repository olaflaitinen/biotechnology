# =============================================================================
#  biotechnology.branches.green.agricultural_genome_editing
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  GREEN BIOTECHNOLOGY  ->  AGRICULTURAL GENOME EDITING
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Instead of adding a gene from another species, genome editing rewrites a few
#  letters of the crop's own DNA: the same kind of change that happens
#  naturally, but aimed.
#
#  THE REGULATORY FAULT LINE
#  This is the clearest case in the taxonomy of law lagging behind biology. A
#  plant carrying a four-base deletion made with CRISPR is:
#
#      a genetically modified organism   in the European Union
#      a conventional variety            in Japan, Argentina, Brazil, the
#                                        United States and England
#
#  No laboratory test can tell it apart from a spontaneous mutant, and none can
#  tell it apart from a variety produced by the chemical and radiation
#  mutagenesis used without special regulation since the 1950s. Same plant,
#  different answers.
#
#  `governance.py` sets out the three defensible philosophies behind that
#  divergence, meaning process-based, product-based and novelty-based, and
#  adjudicates none of them. That restraint is deliberate.
#
#  THE CORRECTION THIS RECORD MAKES
#  Off-target editing is real and is small relative to its alternatives. A
#  screened line carries a handful of detectable unintended changes. The tissue
#  culture step that accompanies the edit introduces hundreds to thousands of
#  somaclonal mutations; chemical and radiation mutagenesis introduce tens of
#  thousands. The number is only meaningful against a comparator, and the
#  comparator is usually left out. `metrics.py` supplies it.
#
#  THE ASYMMETRY THAT SHAPES THE FIELD MORE THAN POLICY DOES
#  Removing a gene is far easier than adding a function, because
#  template-directed repair happens in well under ten per cent of edits in
#  plant cells. So the deployed trait set is dominated by knockouts: a browning
#  enzyme, a susceptibility gene, a horn-growth locus, an antinutrient pathway.
#
#  THE COMPARISON WORTH MAKING
#  Read this record beside `green.plant_genetic_engineering`, and then beside
#  `red.gene_therapy`. The first isolates how much is attributable to law
#  rather than to technology. The second shows the identical molecular
#  operation being celebrated in one branch and prohibited in another, with
#  nothing in the biology to explain the difference.
#
#  PACKAGE LAYOUT
#      narrative.py    the find-and-replace analogy, with its limit stated
#      practice.py     applications grouped by edit class, since class decides
#                      the legal object
#      metrics.py      eight metrics, with the off-target comparator first
#      history.py      1996 to 2023, including the 2018 CJEU judgment
#      governance.py   three philosophies, recorded and not adjudicated
#      linkage.py      the two edges that make this record legible
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
KEY = "agricultural_genome_editing"

NAME = "Agricultural Genome Editing"

# "new genomic techniques" and "ngt" are the terms the European Union uses in
# its 2023 proposal; "precision breeding" is the term in the England Act;
# "crispr crops" is what most people search for. All resolve here, because a
# reader arriving with any of them is asking about the same thing.
ALIASES = (
    "crispr crops",
    "gene editing crops",
    "new genomic techniques",
    "ngt",
    "precision breeding",
    "genome edited crops",
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
