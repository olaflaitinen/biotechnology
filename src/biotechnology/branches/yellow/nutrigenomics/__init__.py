# =============================================================================
#  biotechnology.branches.yellow.nutrigenomics
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  YELLOW BIOTECHNOLOGY  ->  NUTRIGENOMICS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  How what you eat interacts with the genes you were born with, where a little
#  is firmly established and a great deal is sold on evidence that does not
#  support it.
#
#  THIS RECORD CLOSES THE YELLOW BRANCH AND HAS THE WIDEST GAP IN IT BETWEEN
#  CLAIM AND EVIDENCE
#
#      ESTABLISHED       monogenic. Single genes, large effects, clinically
#                        actionable. Phenylketonuria, lactase persistence,
#                        coeliac risk by HLA type, hereditary
#                        haemochromatosis.
#      NOT ESTABLISHED   polygenic. That a panel of common variants predicts
#                        how you respond to fat, carbohydrate or caffeine well
#                        enough to guide your diet. This is what is sold.
#
#  THE ARITHMETIC THAT EXPLAINS EVERYTHING ELSE
#  `metrics.py` is the only facet in the library whose first two entries exist
#  to explain why the field's claims do not hold:
#
#      effect sizes for common variants are small
#      detecting an INTERACTION needs roughly four times the sample of a main
#      effect of the same size, and gene-diet interactions are smaller than the
#      main effects to begin with
#
#  A study powered to associate a variant with a trait is badly underpowered to
#  find how that variant modifies a dietary response. Most published gene-diet
#  interactions came from exactly such studies, and most did not replicate.
#  That is a methodological fact rather than an accusation.
#
#  THE TRIAL
#  In 2018 a large, preregistered, adequately powered randomised trial assigned
#  low-fat and low-carbohydrate diets by genotype pattern. Genotype-matched
#  diets did no better. A null result of that quality is worth more than a
#  great many positive small studies.
#
#  AND THE FINDING THAT DISPLACED THE PREMISE
#  People eating identical meals differ substantially and reproducibly in their
#  glucose and lipid responses, so personalisation has something real to
#  personalise. What predicts it is the gut microbiome, meal composition, sleep
#  and activity, with genetics contributing modestly.
#
#      PERSONALISED NUTRITION IS A DEFENSIBLE IDEA WHOSE BEST CURRENT BASIS IS
#      NOT GENOMIC.
#
#  which is an awkward finding for a field named after genomes, and one the
#  research half has absorbed considerably faster than the commercial half.
#
#  THE SHAPE OF THE TIMELINE IS THE FINDING
#  The two strongest results, phenylketonuria screening and lactase
#  persistence, date from the 1960s. They predate the field's name by forty
#  years, they are monogenic, and they concern large effects. Everything after
#  2000 divides into mechanistic research that has been productive and makes no
#  individual predictions, and a predictive commercial programme that has
#  repeatedly failed to replicate.
#
#      THE FIELD'S BEST RESULTS ARE OLD. ITS MARKETING IS NEW.
#
#  `narrative.ANALOGY` is a nut allergy: a genuine large-effect instruction
#  about one person, which nobody doubts. The claim being sold is that everyone
#  carries a subtler version of the same thing. That is where it breaks, since
#  a collection of very small effects in everyone is a different kind of thing
#  rather than a quieter version of the same one.
#
#  THE GOVERNANCE GAP, NAMED PRECISELY
#  A clinical genetic test is a regulated diagnostic device with evidence
#  requirements and a care pathway. The SAME genotyping sold for "wellness" has
#  frequently sat outside that framework on the argument that it makes no
#  medical claim. The European in vitro diagnostic regulation narrowed the gap
#  considerably; it has not closed everywhere.
#
#  And the data outlives the product. A genome does not change, cannot be
#  reissued, and identifies relatives who never consented, which is why
#  `linkage.py` treats `purple.genetic_data_privacy` as binding.
#
#  ONE SDG, WHICH IS THE FEWEST IN THE LIBRARY
#  Goal 3, on the established monogenic applications alone. Nothing else is
#  claimed because nothing else has been demonstrated, and Goal 10 would be
#  actively wrong: the ancestry portability problem means this field currently
#  works LEAST well for the least represented populations.
#
#  A record whose metrics facet documents null trials and failed replications
#  should claim what its evidence supports and no more.
#
#  PACKAGE LAYOUT
#      narrative.py    the two halves, and the nut allergy that breaks the claim
#      practice.py     applications BY EFFECT SIZE, newborn screening first and
#                      consumer websites last, with mechanism kept separate so
#                      its credibility cannot transfer
#      metrics.py      twelve metrics, the first two explaining why the field's
#                      claims fail, and the last recording what did predict
#      history.py      1934 to 2023, with three setbacks
#      governance.py   a gap rather than a regime
#      linkage.py      why exactly one SDG is claimed
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
KEY = "nutrigenomics"

NAME = "Nutrigenomics"

# "personalised nutrition" is what the field is sold as and is broader than
# genetics, which is the record's point. "dna diet" is included because it is
# the consumer phrasing, and a reader arriving with it should meet this
# record's qualifications rather than a sales page.
ALIASES = (
    "nutrigenetics",
    "personalised nutrition",
    "precision nutrition",
    "nutritional genomics",
    "dna diet",
    "gene diet interaction",
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
