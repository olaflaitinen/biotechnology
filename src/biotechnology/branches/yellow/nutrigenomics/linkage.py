# =============================================================================
#  biotechnology.branches.yellow.nutrigenomics.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `yellow.probiotics_and_prebiotics` names this record as a warning, and the
#  edge is reciprocated for the same reason from this side. Both fields
#  promised personalisation ahead of the evidence, both attracted consumer
#  products before the trials, and both were corrected by better measurement
#  rather than by better argument.
#
#  There is a second and stronger reason for the edge. The microbiome is what
#  turned out to predict dietary response better than genotype. So that record
#  is simultaneously this one's cautionary parallel and the source of the
#  finding that displaced its central premise, which is an unusual relationship
#  and worth a reader's attention.
#
#  `gold.genomics_data_analysis` holds the methods and the equity problem. The
#  polygenic scores this record depends on are derived overwhelmingly in
#  European-ancestry cohorts and transfer poorly, so the consumer product is
#  least informative for the populations least represented in the research. It
#  is that record's failure reaching consumers directly.
#
#  `purple.genetic_data_privacy` is binding rather than decorative. A dietary
#  test is a genetic test; the data does not change, cannot be reissued, and
#  identifies relatives who never consented, and it is frequently collected
#  under commercial terms rather than clinical ones.
#
#  `yellow.biofortification` is the deliberate contrast. Both records address
#  nutrition and genetics. One changes a population's food supply through the
#  seed and has measured effects on nutritional status; the other proposes
#  changing an individual's choices through their genotype and has not.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  One, which is the fewest of any record in this library, and the restraint is
#  deliberate and defensible.
#
#  Goal 3 is claimed on the established monogenic applications alone: newborn
#  screening for treatable inherited metabolic disorders, and the exclusion of
#  coeliac disease by HLA typing. Those prevent permanent harm and are in
#  routine clinical use.
#
#  NOTHING ELSE IS CLAIMED, and the reason is that nothing else has been
#  demonstrated. Goal 2 would be reachable for a nutrition record and this one
#  does not affect food supply or access. Goal 10 would be tempting given the
#  personalisation framing, and this record's ancestry portability problem
#  means it currently works LEAST well for the least represented populations,
#  which is the opposite of reducing inequality.
#
#  A record whose own metrics facet documents null trials and failed
#  replications should claim the goals its evidence supports and no others.
#  Claiming more would be exactly the behaviour rule 12 exists to prevent, and
#  a single SDG is the honest answer.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on the established monogenic clinical applications only
)


# =============================================================================
#  GLOSSARY
#  Grouped: the two halves of the field, the statistics that decide it, the
#  established variants, and the data question.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the two questions that get conflated ----------------------------------
    "nutrigenomics",
    "nutrigenetics",
    "gene_diet_interaction",
    "personalised_nutrition",
    "precision_nutrition",
    # -- the difference that decides everything --------------------------------
    "monogenic_trait",
    "polygenic_trait",
    "effect_size",
    "penetrance",
    "polygenic_score",
    "variance_explained",
    "statistical_power",
    "replication_crisis",
    "mendelian_randomisation",
    # -- the established examples ----------------------------------------------
    "phenylketonuria",
    "newborn_screening",
    "lactase_persistence",
    "coeliac_disease",
    "haemochromatosis",
    "familial_hypercholesterolaemia",
    # -- what actually predicted response --------------------------------------
    "postprandial_response",
    "gut_microbiome",
    "continuous_glucose_monitoring",
    "dietary_adherence",
    # -- the data --------------------------------------------------------------
    "direct_to_consumer_testing",
    "genetic_privacy",
    "incidental_finding",
    "ancestry_portability",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "phenylketonuria_newborn_screening_history",
    "lactase_persistence_genetics",
    "gene_diet_interaction_replication_review",
    "genotype_matched_diet_trial",
    "postprandial_response_microbiome_prediction",
    "polygenic_score_ancestry_portability",
    "direct_to_consumer_nutrigenomic_test_evaluation",
    "mendelian_randomisation_diet_review",
    "dutch_famine_epigenetics",
    "ivdr_genetic_test_scope",
)


# =============================================================================
#  RELATED
#  Six edges. The first is both a parallel and the source of the finding that
#  displaced this record's premise.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same overpromise, and the variable that predicted better ----------
    "yellow.probiotics_and_prebiotics",
    # -- the methods, and the ancestry problem that reaches consumers here -----
    "gold.genomics_data_analysis",
    # -- a dietary test is a genetic test --------------------------------------
    "purple.genetic_data_privacy",
    # -- nutrition through the food supply, with measured outcomes -------------
    "yellow.biofortification",
    # -- where the monogenic applications are clinically managed ---------------
    "red.pharmacogenomics",
    # -- the diagnostics that deliver the established tests --------------------
    "red.molecular_diagnostics",
)
