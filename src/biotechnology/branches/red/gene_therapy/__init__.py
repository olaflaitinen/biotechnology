# =============================================================================
#  biotechnology.branches.red.gene_therapy
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  RED BIOTECHNOLOGY  ->  GENE THERAPY
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Some diseases are caused by a single faulty instruction in a person's DNA.
#  Gene therapy delivers a corrected instruction into the patient's own cells,
#  so that the body starts making the missing or broken protein itself.
#
#  WHAT THIS PACKAGE IS
#  Every subtype in this library is a *package*, not a module. The record is
#  split into six facet files, each of which can be read, reviewed and edited
#  by a different kind of specialist without any of them having to understand
#  the others:
#
#      narrative.py    the prose, in a technical and a public register
#      practice.py     applications, technologies, organisms, techniques,
#                      and an honest list of what does not work yet
#      metrics.py      the measurable quantities, with units, typical ranges,
#                      evidence grades and links to computable formulas
#      history.py      the dated record, including the failures
#      governance.py   maturity, risk, scale, domains, regulations, standards
#      linkage.py      SDGs, glossary terms, citations and cross-references
#
#  This file - the package initialiser - does one job: it imports those six
#  facets and assembles them into a single frozen `Subtype` object. It holds
#  no descriptive content of its own beyond identity, so a reviewer never has
#  to read it to check a fact.
#
#  WHY SPLIT A RECORD ACROSS SIX FILES?
#  Three concrete reasons, learned from maintaining curated datasets:
#
#    1. REVIEWABILITY. A clinical geneticist can review `narrative.py` and
#       `metrics.py` and ignore the rest. A regulatory affairs professional
#       can review `governance.py` alone. A science communicator can rewrite
#       the plain-language paragraph without opening anything that contains a
#       regulation citation. One file per concern means one reviewer per file.
#
#    2. DIFF HYGIENE. Correcting a single milestone touches `history.py` and
#       nothing else. In a single-file layout every correction produces a diff
#       against a six-hundred-line file, and two contributors working on
#       different aspects of the same subtype collide every time.
#
#    3. MECHANICAL CHECKING. Each facet exports a fixed set of names with
#       fixed types. `tests/test_facets.py` walks every subtype package and
#       asserts that the contract holds, which catches a missing field at
#       import time rather than as an empty column in a generated table.
#
#  THE FACET CONTRACT
#  Every subtype package in this library exports exactly these names from
#  these files. Nothing more, nothing less.
#
#      narrative     SUMMARY, DESCRIPTION, PLAIN_LANGUAGE, ANALOGY,
#                    WHY_IT_MATTERS                              (5 strings)
#      practice      APPLICATIONS, TECHNOLOGIES, ORGANISMS, TECHNIQUES,
#                    CHALLENGES                            (5 string tuples)
#      metrics       METRICS (tuple of Metric), FORMULAS (string tuple)
#      history       MILESTONES (tuple of Milestone)
#      governance    MATURITY, RISK_TIER, SCALE, DOMAINS, REGULATORY_STATUS,
#                    REGULATIONS, STANDARDS
#      linkage       SDGS (ints), GLOSSARY, REFERENCES, RELATED
#
#  ADDING A NEW SUBTYPE
#  Copy this directory, keep all seven filenames, replace the content, and add
#  one import line to the parent branch package. Nothing else in the codebase
#  needs to change: the registry, the search engine, the exporters, the command
#  line interface and the documentation generator all discover it automatically.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ....core.models import Subtype

# -----------------------------------------------------------------------------
#  The six facets. Imported as modules rather than with `from x import *` so
#  that the origin of every field below is visible at the point of use: a
#  reader who wants to know where APPLICATIONS came from can see `practice`
#  in the expression and open exactly one file.
# -----------------------------------------------------------------------------
from . import governance, history, linkage, metrics, narrative, practice

__all__ = ["SUBTYPE"]


# =============================================================================
#  IDENTITY
#  The only descriptive content that lives in this file.
# -----------------------------------------------------------------------------
#  KEY must equal the directory name. The parent branch package asserts this
#  at import time, because a mismatch produces a subtype that exists but
#  cannot be addressed by its own path.
# =============================================================================
KEY = "gene_therapy"

NAME = "Gene Therapy"

# Alternative names that people actually type into a search box. These resolve
# without a branch prefix through `biotechnology.get_subtype("gene transfer")`.
# Keep them lowercase; the alias index normalises but readers should not have
# to rely on that.
ALIASES = (
    "gene transfer",
    "genetic medicine",
    "gene addition",
    "in vivo gene editing",
    "gene augmentation",
)


# =============================================================================
#  ASSEMBLY
#  A single call. Every argument is pulled from a facet module, in the same
#  order as the facet list at the top of this file, so that the mapping from
#  file to field is obvious by inspection.
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
