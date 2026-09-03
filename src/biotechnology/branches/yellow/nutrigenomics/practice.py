# =============================================================================
#  biotechnology.branches.yellow.nutrigenomics.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped BY EFFECT SIZE AND EVIDENCE, from clinical
#  monogenic use down to what is sold online, and this is the most important
#  editorial decision in the record. Rule 6 forbids listing an aspiration as an
#  application, and in this field the distinction between a variant that
#  determines a diet and a variant that shifts a risk estimate slightly is the
#  whole subject.
#
#  A reader who notices that the first group concerns newborn screening
#  programmes and the last concerns consumer websites has understood the field.
#
#  THE RESEARCH GROUP IS PLACED SEPARATELY AND DELIBERATELY. Nutrigenomics
#  proper, meaning how food affects gene expression, is legitimate mechanistic
#  science that makes no predictive claim about individuals. Listing it beside
#  the consumer tests would let the credibility of one transfer to the other,
#  which is precisely how this field's marketing works.
#
#  ORGANISMS is unusual here: the subject is human, so the entry is Homo
#  sapiens, and the remaining entries are the model organisms in which the
#  mechanistic work is actually done.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = [
    "APPLICATIONS",
    "TECHNOLOGIES",
    "ORGANISMS",
    "TECHNIQUES",
    "CHALLENGES",
]


# =============================================================================
#  APPLICATIONS
#  By effect size and evidence. The ordering is the argument.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- monogenic, clinical, and preventing permanent harm ---------------------
    "Newborn screening for phenylketonuria followed by lifelong dietary "
    "phenylalanine restriction, which prevents irreversible intellectual "
    "disability and is among the clearest gene-diet interactions ever acted on",
    "Dietary management of other inherited metabolic disorders detected by "
    "newborn screening, including galactosaemia and maple syrup urine disease",
    "HLA typing to exclude coeliac disease, where the absence of defined types "
    "effectively rules out the diagnosis and prevents unnecessary lifelong "
    "restriction",
    "Hereditary haemochromatosis genotyping, which identifies people whose iron "
    "handling makes dietary and therapeutic iron management necessary",
    "Familial hypercholesterolaemia identification, where the genetic diagnosis "
    "changes management from dietary advice to pharmacological treatment",
    # -- monogenic, common, and mostly explanatory rather than actionable ---------
    "Lactase persistence genotyping, which explains rather than guides, since a "
    "person generally knows whether milk troubles them without a test",
    "Alcohol dehydrogenase and aldehyde dehydrogenase variants, which have "
    "large effects on alcohol metabolism and known health consequences",
    "Caffeine metabolism genotype, which is the most defensible of the common "
    "consumer test claims and still has modest predictive value for any "
    "individual outcome",
    # -- research: mechanism, making no claim about individuals --------------------
    "Transcriptomic and epigenetic studies of how specific nutrients regulate "
    "gene expression, which is nutrigenomics proper and is legitimate "
    "mechanistic science",
    "Investigation of early-life and prenatal nutrition effects on later "
    "metabolic health, including the epigenetic work following historical "
    "famine cohorts",
    "Nutrient regulation of transcription factors and metabolic pathways in "
    "model systems",
    # -- population genetics, which explains rather than personalises --------------
    "Population-level explanation of dietary adaptation, including lactase "
    "persistence, amylase copy number and variants associated with historical "
    "diets, which is evolutionary biology rather than dietary advice",
    # -- what is actually sold, and what the trials found -------------------------
    "Direct-to-consumer genetic tests offering diet recommendations from "
    "panels of common variants, which is the commercial bulk of the field and "
    "which controlled trials have not shown to outperform generic advice",
    "Genotype-matched weight loss diets, which the largest controlled trials "
    "found no better than diets assigned without genotype",
    "Polygenic scores for nutrition-related traits, which have research value "
    "and insufficient individual predictive power for dietary prescription",
    # -- and what did predict better ------------------------------------------------
    "Personalised nutrition based on postprandial glucose and lipid response, "
    "the gut microbiome, sleep and activity, which has outperformed genotype in "
    "the studies that compared them and which is where the defensible version "
    "of personalisation now sits",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by what is measured, which increasingly is not the genome.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- reading the genome -----------------------------------------------------
    "Targeted genotyping of defined clinically actionable variants, which is "
    "what the established applications use and is cheap and reliable",
    "Genotyping arrays and whole genome sequencing for research cohorts",
    "Polygenic score construction, with the discipline of validating in an "
    "ancestry-matched population, since scores derived in one population "
    "transfer poorly to another",
    # ---- reading gene expression, which is the other half of the name -----------
    "Transcriptomics to measure how a nutrient changes expression, which is "
    "mechanistic and makes no individual prediction",
    "Epigenetic profiling including DNA methylation, used in the early-life "
    "nutrition work",
    "Metabolomics and lipidomics, which measure what a person's metabolism is "
    "actually doing rather than what their genome permits",
    # ---- measuring the response itself, which turned out to predict better -------
    "Continuous glucose monitoring for postprandial response, which produced "
    "the finding that individual responses to identical meals differ far more "
    "than expected",
    "Gut microbiome profiling as a predictor of dietary response, which "
    "outperformed genotype in the studies that compared them and connects this "
    "record to `yellow.probiotics_and_prebiotics`",
    "Wearable and dietary intake measurement, which supplies the behavioural "
    "variables that carried much of the predictive power",
    # ---- doing the statistics honestly -------------------------------------------
    "Interaction analysis with adequate power, which requires far larger "
    "samples than main-effect analysis and is the methodological reason most "
    "published gene-diet interactions have not replicated",
    "Mendelian randomisation, which uses genetic variants to test whether a "
    "dietary exposure causes an outcome rather than to personalise advice, and "
    "is the field's most productive genetic method",
    "Preregistration and replication in independent cohorts, which is the "
    "practice whose absence produced the field's replication problem",
)


# =============================================================================
#  ORGANISMS
#  The subject is human; the rest are where mechanism is actually studied.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "homo_sapiens",  # the subject of the entire record
    "mus_musculus",  # where nutrient regulation of expression is actually tested
    "caenorhabditis_elegans",  # dietary restriction and longevity mechanism
    "drosophila_melanogaster",  # nutrient sensing pathways
    "saccharomyces_cerevisiae",  # the conserved nutrient sensing machinery
    "escherichia_coli",  # a gut community member, and the microbiome connection
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "genotyping",
    "next_generation_sequencing",
    "transcriptomics",
    "metabolomics",
    "metagenomics",
    "randomised_controlled_trial",
    "mendelian_randomisation",
    "continuous_glucose_monitoring",
)


# =============================================================================
#  CHALLENGES
#  The statistical problem first, because it explains the replication failures.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- why the polygenic claims do not hold -----------------------------------
    "Small effect sizes for common variants, and smaller effects still for "
    "their interaction with a dietary component, so an interaction requires far "
    "larger samples to detect reliably than a main effect does",
    "Widespread failure to replicate published gene-diet interactions, which "
    "follows directly from the point above combined with flexible analysis and "
    "selective reporting",
    "Absence of trial evidence that genotype-matched diets outperform "
    "alternatives, which is the finding the commercial layer of the field has "
    "not absorbed",
    # -- measuring the exposure is the unglamorous obstacle -------------------------
    "Dietary intake measurement error, since self-reported intake is "
    "systematically inaccurate and an interaction cannot be estimated more "
    "precisely than the exposure it involves",
    "Confounding by ancestry, since both genotype and dietary pattern vary with "
    "population structure and an uncontrolled association may reflect neither "
    "biology nor diet",
    # -- who the research was done on ------------------------------------------------
    "Overwhelming derivation of polygenic scores from European-ancestry "
    "cohorts, so they transfer poorly to other populations, which makes this "
    "field's equity problem the same one `gold.genomics_data_analysis` records",
    # -- what the commercial layer does ------------------------------------------------
    "Direct-to-consumer tests giving generic dietary advice with a genetic "
    "justification attached, which lends the authority of a genome to a "
    "recommendation that did not come from one",
    "Displacement of attention from interventions with strong evidence towards "
    "personalisation with weak evidence, which is the practical harm of an "
    "otherwise ineffective product",
    "Risk of unnecessary dietary restriction based on a variant with a small "
    "effect, particularly where a consumer interprets a risk score as a "
    "diagnosis",
    # -- the data ----------------------------------------------------------------------
    "Genetic privacy, since a dietary test is a genetic test and the resulting "
    "data is frequently collected without the consent process a clinical test "
    "would require, and is retained and shared under commercial terms",
    "Incidental findings of clinical significance in a test sold for dietary "
    "purposes, with no clinical pathway to interpret or act on them",
    # -- and the awkward finding ----------------------------------------------------------
    "The finding that microbiome and behaviour predict dietary response better "
    "than genotype, which is a problem for a field named after genomes and "
    "which the research half has accepted faster than the commercial half",
)
