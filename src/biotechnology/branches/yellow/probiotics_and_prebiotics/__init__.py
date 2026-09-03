# =============================================================================
#  biotechnology.branches.yellow.probiotics_and_prebiotics
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  PROBIOTICS AND PREBIOTICS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Swallowing live bacteria on purpose, and feeding the ones already there, in
#  a field where the evidence and the marketing have drifted a long way apart.
#
#  THE RECORD IS WRITTEN TO BE WRONG IN NEITHER DIRECTION
#  Dismissing the category is as inaccurate as accepting its advertising.
#
#      SUPPORTED   specific strains, at specific doses, for specific
#                  conditions: reduced duration of infectious diarrhoea in
#                  children, reduced antibiotic-associated diarrhoea, reduced
#                  necrotising enterocolitis in preterm infants. Faecal
#                  transplantation for recurrent C. difficile infection is
#                  highly effective.
#      NOT SUPPORTED  the general proposition, sold on most shelves, that live
#                  bacteria improve health in a healthy adult. Not disproved.
#                  The trials mostly have not been done at the required
#                  quality, and those that have are often for a different
#                  strain from the one in the product.
#
#  THE ONE FACT THAT EXPLAINS MOST OF THE CONFUSION
#
#      EFFECTS ARE STRAIN-SPECIFIC, NOT SPECIES-SPECIFIC.
#
#  Two strains of one species differ in adhesion, metabolites and effect.
#  Evidence for one does not transfer to another, any more than one breed of
#  dog tells you about another. Most marketing treats the species name as the
#  active ingredient. It is not, and `metrics.py` records strain identification
#  completeness as a metric because it decides whether ANY published evidence
#  can be attached to a product.
#
#  WHY `metrics.py` OPENS WITH THE NUMBER THAT PROVES LEAST
#  Colony forming units per dose is on almost every package. It counts live
#  organisms and is not an outcome, in exactly the sense
#  `green.biofertilisers` insists on for soil inoculants. It is placed first
#  BECAUSE it is what consumers see, and its note is where the correction
#  belongs.
#
#  THE 2012 REGULATORY FINDING, WHICH IS RARELY PRESENTED AS WHAT IT IS
#  European authorities assessed hundreds of probiotic health claims and
#  authorised NONE. The field's usual account is that the requirements were
#  unsuited to foods. The stronger reading, taken here, is that the assessment
#  revealed how much of the market rested on evidence for a different strain,
#  on surrogate endpoints, or on trials too small to conclude anything.
#
#  Because the word probiotic itself implies a benefit, several member states
#  restrict the word on labels. A category that may be sold freely and may not
#  be described is an unusual position, and it produced the marketing by
#  implication this record records as a challenge.
#
#  THE FINDING THAT CONTRADICTED THE INTUITIVE ACCOUNT
#  In 2018, direct gut sampling showed that administered strains colonise some
#  people and not others, that the resident community decides which, and that
#  detection ceases within days to weeks of stopping.
#
#  `narrative.ANALOGY` is scattering seed on an established lawn: something
#  changes while you keep scattering, and the lawn returns to what it was when
#  you stop, because the existing plants were not there by accident.
#
#  THE EVIDENCE BAR RISES WITH THE REGIME, AND SO DOES THE EFFECT
#      a yoghurt                 food. No authorisation.
#      a capsule                 supplement. Notification.
#      a defined consortium      licensed MEDICINE, with trial evidence.
#      faecal transplantation    medicine, tissue, or bespoke framework, and
#                                the classification is contested.
#
#  That correlation is the most useful thing this record's governance can point
#  out, and it is why `SCALE = POPULATION` rather than INDUSTRIAL: the
#  manufacturing is unremarkable and the questions that decide the field are
#  population questions.
#
#  THE PREBIOTIC HALF HAS FIRMER GROUND
#  Feeding the resident community is more reproducible than introducing a new
#  member, because it does not depend on anything establishing. Short-chain
#  fatty acid production is measurable and repeatable, and the human milk
#  oligosaccharides now authorised for infant formula are the clearest case in
#  the record of a defined compound, a defined population and a defined
#  rationale.
#
#  SAFETY, WHICH THE CASUAL FRAMING GETS WRONG
#  These products are not harmless merely because they are frequently
#  ineffective. Live organisms have caused bloodstream infections in
#  immunocompromised and critically ill patients, and resistance gene transfer
#  to the resident community is why screening is a requirement.
#
#  ONLY TWO SDGs ARE CLAIMED, WHICH IS THE FEWEST IN THIS BRANCH
#  Goal 3 for the specific clinical applications, and not for the general
#  wellbeing market. Goals 2 and 12 are declined: nothing here addresses food
#  security or resource use, and a record whose own claims failed regulatory
#  assessment should be the last in the branch to reach for extra goals.
#
#  PACKAGE LAYOUT
#      narrative.py    what is supported and what is not, and the lawn
#      practice.py     applications BY STRENGTH OF EVIDENCE, hospitals first
#                      and supermarket shelves last
#      metrics.py      twelve metrics opening with the one that proves least
#      history.py      1907 to 2023, with two setbacks twenty years apart
#      governance.py   regulation of a CLAIM rather than of a product
#      linkage.py      nutrigenomics as a warning, biofertilisers as a parallel
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
KEY = "probiotics_and_prebiotics"

NAME = "Probiotics and Prebiotics"

# "gut microbiome" is what most readers will search for and is broader than the
# record. "faecal microbiota transplantation" is included because it is where
# the strongest evidence in the record sits and a reader looking for it should
# arrive here rather than in a clinical record.
ALIASES = (
    "probiotics",
    "prebiotics",
    "gut microbiome",
    "synbiotics",
    "postbiotics",
    "faecal microbiota transplantation",
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
