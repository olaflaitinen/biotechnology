# =============================================================================
#  biotechnology.branches.yellow.food_biopreservation
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  FOOD BIOPRESERVATION
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Using harmless microbes, or the substances they make, to stop food spoiling
#  or making people ill, while changing nothing else about it.
#
#  THE DISTINCTION FROM ITS NEIGHBOUR IS INTENT, NOT MECHANISM
#      food_fermentation      the microbes TRANSFORM the food. Preservation is
#                             one of four things happening, and the product is
#                             deliberately different from what went in.
#      food_biopreservation   the microbes PROTECT the food and are meant to
#                             change nothing else. A biopreserved ham is still
#                             a ham.
#
#  The requirement is strict: a protective culture that acidifies the product
#  perceptibly has FAILED even if the food is safe. `metrics.py` therefore
#  records sensory difference from an untreated control as a performance
#  metric, where the target is no detectable difference.
#
#  THE ORGANISM THAT EXPLAINS THE WHOLE FIELD
#  Before the listeriosis outbreaks of the 1980s, food microbiology was
#  organised around organisms that grow warm and die when cooked. Listeria
#  monocytogenes does neither:
#
#      it GROWS AT REFRIGERATION TEMPERATURE, so chilling does not stop it
#      it contaminates AFTER the kill step, in slicing, packing and handling
#      it has a high case fatality rate
#
#  That left a specific gap: something acting in the finished, packaged,
#  chilled product across its whole shelf life. Heat cannot, the product is
#  already made. Chemical preservatives were being reduced, not added.
#  Biopreservation is what was available, and this record's shape follows from
#  that one organism.
#
#  NOTHING HERE WORKS ALONE, AND SAYING OTHERWISE MISDESCRIBES THE FIELD
#  Nisin is excluded by the outer membrane of Gram-negative bacteria and does
#  essentially nothing to Salmonella. Protective cultures need time and
#  temperature. Phages act on one species. Each is a PARTIAL barrier.
#
#  They work because several partial barriers combine with pH, water activity,
#  salt, chilling and packaging into a set no organism crosses. That is hurdle
#  technology, articulated in 1976, and it is the correct frame for everything
#  here. `narrative.ANALOGY` is several ordinary locks rather than one
#  exceptional one, and its stated flaw is the important part: a lock stays as
#  good as it was, and a bacterium adapts.
#
#  WHY `metrics.py` INSISTS ON THE MATRIX
#  Almost every published figure is generated in broth, where a peptide meets
#  its target unimpeded. In a food it meets fat, protein, a solid matrix and a
#  resident flora. An agent reported at five logs in vitro may deliver one in a
#  sausage. That is not a failure of the agent; it is a property of food, and
#  reporting broth activity as performance is this field's commonest
#  overstatement.
#
#  The second metric is why the first is rarely enough: for a chilled
#  ready-to-eat product, regulation requires that Listeria NOT GROW across
#  shelf life. Killing organisms once is a delay. Preventing growth is control.
#
#  THE SETBACK THE FIELD SHOULD NOT HAVE FOUND SURPRISING
#  In 1999 nisin resistance was documented in Listeria. The food industry had
#  used nisin for thirty years as though it were a permanent property of the
#  world. These are ANTIMICROBIALS under the same evolutionary pressure as any
#  other, and this field was slower than clinical microbiology to say so.
#  `linkage.py` points at `dark.biosurveillance` for exactly that reason.
#
#  THE GOVERNANCE POINT THAT DRIVES TECHNICAL CHOICES
#  One protective effect, three legal routes:
#
#      additive        declared on the label, authorised by name and food
#                      category. Nisin is E 234.
#      processing aid  acts during production, no function in the finished
#                      food, no declaration.
#      culture         an ingredient, declared as such, no additive
#                      authorisation.
#
#  So producing a bacteriocin IN SITU with a culture rather than adding a
#  purified preparation is frequently a REGULATORY decision presented as a
#  technical one. Phage preparations fit none of the three cleanly, which is
#  why `REGULATORY_STATUS = VARIES`.
#
#  And the clean label pressure driving adoption works against the field as
#  often as for it: a manufacturer replacing a chemical preservative to shorten
#  an ingredient list may find the replacement is also declarable.
#
#  THE STRONGEST SDG CLAIM IS THE LEAST OBVIOUS
#  Goal 12, on food waste. Roughly a third of food produced is lost, spoilage
#  is a large part of it, and shelf life extension reduces that without asking
#  anyone to change their behaviour. Very few interventions in this library
#  have that property.
#
#  PACKAGE LAYOUT
#      narrative.py    intent versus mechanism, and the several locks
#      practice.py     applications BY TARGET ORGANISM, with Listeria first
#                      because it is why the field exists; organisms include
#                      the targets as well as the friendly cultures
#      metrics.py      twelve metrics insisting on the food matrix throughout
#      history.py      1928 to 2020, pivoting on the 1980s outbreaks
#      governance.py   one effect, three legal routes
#      linkage.py      biopesticides as the parallel whose arguments transfer
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
KEY = "food_biopreservation"

NAME = "Food Biopreservation"

# "nisin" and "protective cultures" are what a practitioner searches for, and
# "bacteriophage biocontrol" names the newest agent. "natural preservatives" is
# included because it is the marketing term and a reader arriving with it
# should meet this record's qualifications rather than a promotional page.
ALIASES = (
    "biopreservation",
    "protective cultures",
    "bacteriocins",
    "nisin",
    "bacteriophage biocontrol",
    "natural preservatives",
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
