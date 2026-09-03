# =============================================================================
#  biotechnology.branches.yellow.food_safety_biotechnology
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  FOOD SAFETY BIOTECHNOLOGY
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Testing food for things that would make people ill, and working out where a
#  contaminated batch came from.
#
#  THE CHANGE WAS NOT A BETTER TEST. IT WAS WHEN THE ANSWER ARRIVES.
#
#      culture-based   two to five days. A chilled product with a ten-day shelf
#                      life has been eaten before the laboratory reports, so
#                      the test says what WENT WRONG.
#      molecular       hours. The result arrives while the batch is still on
#                      site, so the test says what TO DO.
#
#  Nothing about the pathogen changed. The interval did, and that converted
#  food safety from an investigation into a control. `metrics.py` therefore
#  opens with a TIME rather than a limit of detection, because sensitivity was
#  never the binding problem: culture is extremely sensitive and slow.
#
#  THE CONSTRAINT NO METHOD IMPROVEMENT ADDRESSES
#  A pathogen is distributed unevenly through a batch, and a test examines a
#  few hundred grams from a consignment of tonnes. `narrative.ANALOGY` is a
#  smoke alarm rather than a fire report, and its stated limit is exactly this:
#  a smoke alarm sits in the room with the smoke.
#
#  So `metrics.py` records the probability of detection at a given prevalence,
#  which combines method performance with the sampling plan. It is the figure
#  that actually describes what a testing programme achieves and it is quoted
#  far less often, because it is far less flattering. In 2022 the field
#  effectively admitted that sampling rather than sensitivity is the limit, and
#  redirected effort towards environmental monitoring, which samples the
#  problem rather than the product.
#
#  THE COST ASYMMETRY RUNS THE OPPOSITE WAY TO CLINICAL TESTING
#  A clinical false positive leads to a confirmatory test. A food false
#  positive can destroy a batch. And molecular methods detect NUCLEIC ACID
#  RATHER THAN VIABLE ORGANISMS, so after a kill step a positive may report a
#  hazard that no longer exists. That makes the viability question commercial
#  rather than academic.
#
#  FOOD FRAUD IS NOT A LESSER SUBJECT, AND 2008 PROVES IT
#  Protein in milk was measured by nitrogen content, which is standard, cheap
#  and correct for genuine milk. Melamine is nitrogen-rich and cheap, so adding
#  it to diluted milk raised the apparent protein. Infants died and many
#  thousands were injured.
#
#      THE TEST PERFORMED EXACTLY AS DESIGNED. It was defeated by someone who
#      understood what it measured and supplied that instead.
#
#  Authenticity testing is therefore an ADVERSARIAL problem rather than an
#  analytical one. A published test principle will be gamed by whoever profits
#  from gaming it, and the defence is orthogonal methods and unpredictability
#  rather than better sensitivity. `practice.APPLICATIONS` places authenticity
#  alongside pathogens rather than as an appendix for this reason.
#
#  THE SECOND TRANSFORMATION: SEQUENCING EVERY ISOLATE
#  Routine whole genome sequencing detects clusters nobody had recognised as
#  outbreaks, because the cases were few, scattered and individually
#  unremarkable. It turned outbreak investigation from interviewing patients
#  about what they ate into matching genomes between a clinical case and a food
#  sample.
#
#  It also created a resourcing problem: clusters are now identified faster
#  than investigators can follow them, which is why `linkage.py` points at
#  `dark.biosurveillance`, where detection capacity exceeding response capacity
#  is the same structural finding.
#
#  THREE GOVERNANCE FEATURES WORTH CARRYING AWAY
#      the METHOD is regulated, not only the result. A better method that has
#      not been validated against a reference standard on that matrix cannot be
#      used to release product, however good it is.
#
#      a result creates a LEGAL DUTY. An operator with reason to believe food
#      is unsafe must withdraw it and notify. There is no discretion to
#      investigate quietly.
#
#      microbiological criteria are NOT PASS MARKS. They verify that a process
#      is under control, and a food meeting them is not thereby safe. The
#      legislation says so and it is widely misread.
#
#  PACKAGE LAYOUT
#      narrative.py    timing rather than capability, and the smoke alarm
#      practice.py     applications BY WHAT IS LOOKED FOR, with authenticity
#                      alongside rather than after; organisms are the targets
#      metrics.py      twelve metrics opening with a time, and insisting on the
#                      sampling probability the field prefers not to quote
#      history.py      1881 to 2022, centred on the 2008 adulteration
#      governance.py   the method is what requires approval
#      linkage.py      why SDG 12 is claimed with the waste qualification
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
KEY = "food_safety_biotechnology"

NAME = "Food Safety Biotechnology"

# "food authenticity" and "food fraud" are included deliberately rather than
# left to a separate record, because the 2008 adulteration establishes that
# they are not separable from safety in practice. "rapid methods" is what the
# industry calls the field's central achievement.
ALIASES = (
    "food testing",
    "pathogen detection",
    "food authenticity",
    "food fraud detection",
    "rapid methods",
    "foodborne outbreak investigation",
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
