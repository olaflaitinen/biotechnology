# =============================================================================
#  biotechnology.branches.white.cell_free_biomanufacturing
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  CELL-FREE BIOMANUFACTURING
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Taking the working parts out of cells, putting them in a tube, and giving
#  them written instructions in the form of DNA, so that biology can be done
#  with nothing alive in the vessel.
#
#  THIS RECORD CLOSES THE WHITE BRANCH BY NEGATING IT
#  Every other record here depends on a living organism. This one removes it,
#  and the trade is exact:
#
#      YOU GIVE UP   self-replication and self-repair. The catalyst is consumed
#                    rather than grown, and every component must be bought
#                    rather than made by something that feeds itself.
#      YOU GET       control and speed. No growth phase, no genetic drift, no
#                    carbon spent staying alive, and no membrane between the
#                    engineer and the chemistry.
#
#  THE BOUNDARY WITH `white.biocatalysis`, WHICH IS THE SHARPEST IN THE BRANCH
#  Both work outside a cell. The difference is how the system is SPECIFIED:
#
#      biocatalysis   defined by which enzymes were put in the vessel.
#                     Assembled by hand.
#      cell-free      defined by which template was added. PROGRAMMED WITH
#                     NUCLEIC ACID.
#
#  Add new DNA to a cell-free system and it makes something new. A biocatalytic
#  system needs a different protein in the vessel.
#
#  THE THREE THINGS IT ACTUALLY SELLS
#  `practice.APPLICATIONS` is grouped by these, because anything needing none
#  of them is cheaper to ferment and saying so is more useful than listing
#  possibilities:
#
#      SPEED         hours rather than days, with cloning and transformation
#                    removed entirely. This is why prototyping is the largest
#                    genuine application.
#      ACCESS        membrane proteins, toxins, non-standard amino acids,
#                    a redox potential set directly. There is nothing alive to
#                    poison and no cell wall in the way.
#      PORTABILITY   a complete reaction freeze-dried onto paper, stored at
#                    ambient temperature for months, started with a drop of
#                    water. No cold chain, no power, no laboratory.
#
#  IT WAS THE INSTRUMENT OF TWO FOUNDATIONAL DISCOVERIES BEFORE IT WAS A
#  MANUFACTURING PROPOSAL
#  Buchner in 1897 showed fermentation happens without a living cell, ending
#  vitalism. Nirenberg and Matthaei in 1961 cracked the genetic code in a
#  cell-free extract, choosing the format precisely because a tube accepts a
#  defined instruction and a cell does not. That ordering explains why the
#  method is so mature scientifically and so immature commercially.
#
#  THE SETBACK IS A PERSISTENT OVERSTATEMENT, NOT A COLLAPSE
#  Cell-free manufacture has been described as imminent since the 1970s and
#  remains a small share of biological production, for reasons that are
#  structural rather than solvable: substrates are bought rather than grown,
#  the catalyst is spent rather than reproducing, and the extract must itself
#  be made from cultured cells. The field did not fail. Two decades of claiming
#  it would beat fermentation on COST, when its advantages are speed, access
#  and portability, damaged its credibility with people who would otherwise
#  have adopted it.
#
#  THE METRIC THE FIELD DOES NOT PUBLISH
#  `metrics.py` records extract batch-to-batch variability as a first-class
#  metric rather than a caveat. It is the largest practical obstacle to
#  regulated manufacture and it is routinely omitted, and a record reporting
#  yields without their reproducibility would reproduce the field's own blind
#  spot.
#
#  THE GOVERNANCE FINDING, WHICH IS A GAP RATHER THAN A RULE
#  Contained use and deliberate release law is written around a LIVING modified
#  organism capable of replication and transfer. A tube of extract and DNA is
#  none of those, so the reaction falls outside rules that govern every other
#  record in this branch. That is why cell-free kits work in a classroom that
#  could not host a containment facility.
#
#  This is neither a loophole nor a safety guarantee. It MOVES THE CONTROL
#  POINT: a system programmed by nucleic acid is limited by the DNA supplied to
#  it, so screening synthesised DNA does the work that organism containment
#  does elsewhere. And one qualification is easy to miss: the extract is made
#  from cultured, often engineered, cells, so contained use applies in full to
#  producing the reagent even though it does not apply to using it.
#
#  TWO VOCABULARY VALUES DIFFER FROM EVERY OTHER WHITE RECORD, DELIBERATELY
#      MATURITY = PILOT   established as a research reagent, demonstration
#                         scale as a manufacturing platform. This record is
#                         about manufacturing.
#      SCALE = BENCH      microlitres to litres, against hundreds of cubic
#                         metres next door. The contrast is the information.
#
#  PACKAGE LAYOUT
#      narrative.py    the trade, the boundary, and the hired-kitchen analogy
#      practice.py     applications by WHICH ADVANTAGE each one buys; organisms
#                      are extract sources rather than producers
#      metrics.py      eleven metrics ordered by speed, access and portability,
#                      with extract variability recorded honestly
#      history.py      1897 to 2022, including two foundational experiments and
#                      one long overstatement
#      governance.py   the gap, and where the control point moved to
#      linkage.py      the branch's completed answer to what does the chemistry
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
KEY = "cell_free_biomanufacturing"

NAME = "Cell-Free Biomanufacturing"

# "cell-free protein synthesis" is the technique most readers arrive by name
# for, and "in vitro transcription translation" is its formal description.
# "synthetic biology prototyping" is included because that is the largest
# genuine application rather than a peripheral one.
ALIASES = (
    "cell free protein synthesis",
    "in vitro transcription translation",
    "cell free systems",
    "acellular biomanufacturing",
    "synthetic biology prototyping",
    "lysate based expression",
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
