# =============================================================================
#  biotechnology.branches.blue.marine_natural_products
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BLUE BIOTECHNOLOGY  ->  MARINE NATURAL PRODUCTS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Finding medicines in the chemistry that sea creatures use to defend
#  themselves, and then facing the fact that there is almost none of it.
#
#  WHY THE SEA PRODUCES DRUG-LIKE CHEMISTRY
#  A sponge cannot run away and cannot hide. Its defence is chemical, released
#  into an ocean that dilutes it immediately, so anything that works at all
#  must work at very low concentration. That is precisely the property a drug
#  needs. It is why the sea has produced pharmacology out of all proportion to
#  how little of it has been sampled, and it is a mechanism rather than a
#  coincidence.
#
#  THE CONSTRAINT THAT DEFINES THE RECORD
#
#      THE PROBLEM IS NEVER DISCOVERY. THE PROBLEM IS SUPPLY.
#
#  These compounds occur at roughly a gram per tonne of animal, in creatures
#  that grow slowly, cannot be farmed and are sometimes protected. A clinical
#  supply corresponds to hundreds or thousands of tonnes of organism. So
#  `metrics.py` opens with yield from source biomass rather than with potency,
#  which would be the normal order for a pharmacology facet and would
#  misdescribe the discipline entirely.
#
#  `practice.APPLICATIONS` is grouped by HOW SUPPLY WAS SOLVED rather than by
#  therapeutic area. A reader scanning the groups will notice that there is no
#  group headed harvesting, and that absence is the record's central claim made
#  visible rather than asserted.
#
#  THE FOUR ROUTES OUT, EACH WITH A PRODUCT
#      total synthesis    ziconotide, a cone snail peptide simple enough to
#                         build, delivered into spinal fluid because it
#                         survives no other route
#      semisynthesis      trabectedin, made from a bacterial fermentation
#                         product. Twenty years from isolation to approval, and
#                         almost all of it manufacturing rather than
#                         pharmacology
#      analogue design    eribulin, a simplified molecule keeping the active
#                         portion of a sponge macrolide and discarding what
#                         could not be made
#      the symbiont       culture or heterologously express the bacterium that
#                         actually makes the compound
#
#  THE DISCOVERY THAT REDIRECTED THE PROBLEM
#  From the late 1990s it became clear that compounds credited to sponges,
#  tunicates and bryozoans for decades were being made by BACTERIA LIVING
#  INSIDE THEM. This did not solve the supply problem, it moved it: the target
#  became culturing a symbiont rather than farming an animal, and most such
#  symbionts do not grow either. It is recorded as a setback as well as a
#  discovery, because a generation of attribution had been wrong and
#  aquaculture efforts had been aimed at the wrong organism.
#
#  THE OTHER TWO SETBACKS
#  Bryostatin, isolated in 1981, is highly active, has consumed decades of
#  work, required many tonnes of animal for grams of material, and still has no
#  settled manufacturing route. It is the standing example of a compound whose
#  pharmacology was never the obstacle.
#
#  And in the 1990s the pharmaceutical industry left natural product discovery
#  for combinatorial chemistry. The libraries underperformed; the extraction,
#  isolation and taxonomic expertise had by then dispersed and was not rebuilt.
#  The timeline of this record therefore has an unusual shape: the science
#  improves steadily while the commercial position gets worse, and both are
#  true at once.
#
#  THE GOVERNANCE COLLISION, WHICH IS TEMPORAL
#  Two complete legal systems meet only here. Medicines law governs what the
#  compound becomes; biodiversity and law of the sea govern where it came from.
#  The collision is that A MEDICINE TAKES LONGER TO DEVELOP THAN THE INTERVAL
#  OVER WHICH THE ACCESS RULES CHANGED. Material collected in 1985 predates the
#  Convention on Biological Diversity; material from 2005 predates the Nagoya
#  Protocol; high seas material predates the 2023 agreement. A company may hold
#  a library assembled under three successive regimes, none applied
#  retroactively. That is a practical reason programmes were abandoned, not a
#  compliance detail.
#
#  A VOCABULARY VALUE WORTH CHECKING
#  `SCALE = BENCH`, despite marketed products. The characteristic unit of this
#  discipline is milligrams: structures are elucidated below a milligram and
#  the supply problem exists precisely BECAUSE the scale never rises. Once a
#  compound is made at tonnage it has become a manufacturing question and
#  belongs to `red.pharmaceutical_biotechnology`.
#
#  PACKAGE LAYOUT
#      narrative.py    dilution-driven potency, and the recipe analogy whose
#                      stated limit is that a cook can find another shop
#      practice.py     applications grouped by how supply was solved
#      metrics.py      twelve metrics, opening with grams per tonne
#      history.py      1951 to 2023, with three setbacks
#      governance.py   two legal systems, and why their timescales collide
#      linkage.py      every edge read as a route out of the supply problem
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
KEY = "marine_natural_products"

NAME = "Marine Natural Products"

# "marine pharmacology" and "drugs from the sea" are what readers outside the
# field will search for. "marine bioprospecting" is the activity, and it
# carries the legal connotation that `governance.py` is about, so it resolves
# here deliberately rather than to `blue.marine_genomics`.
ALIASES = (
    "marine drug discovery",
    "marine pharmacology",
    "drugs from the sea",
    "marine bioprospecting",
    "marine secondary metabolites",
    "marine chemical ecology",
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
