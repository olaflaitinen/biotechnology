# =============================================================================
#  biotechnology.branches.yellow.nutrigenomics.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS IS THE ONLY FACET IN THE LIBRARY WHOSE FIRST TWO METRICS ARE THERE TO
#  EXPLAIN WHY THE FIELD'S CLAIMS DO NOT HOLD.
#
#  Effect size and the sample required to detect an interaction are placed
#  first because together they account for almost everything else in the
#  record: the replication failures, the null trials, and the gap between what
#  is published and what is sold.
#
#  The arithmetic is unforgiving. Detecting an interaction reliably requires
#  roughly four times the sample needed for a main effect of the same size, and
#  gene-diet interactions are smaller than the main effects to begin with. A
#  study powered to find a variant's association with a trait is badly
#  underpowered to find how that variant modifies a dietary response, and most
#  published interactions come from exactly such studies.
#
#  THE FACET THEN RECORDS WHAT DID WORK. Postprandial response variability and
#  the predictive contribution of the microbiome are included because the
#  honest state of personalised nutrition is that its best current basis is not
#  genomic, and a facet that measured only genotype would conceal that.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # =========================================================================
    #  WHY THE POLYGENIC CLAIMS DO NOT HOLD
    # =========================================================================
    Metric(
        name="Effect size of a common variant",
        symbol="beta",
        unit="trait units per risk allele, or odds ratio",
        typical="odds ratios commonly between 1.05 and 1.20 for common "
        "variants in nutrition-related traits",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The number that decides what a genotype can and cannot tell an "
            "individual. An odds ratio of 1.1 is real, is detectable in a large "
            "cohort, and shifts one person's expected outcome by an amount that "
            "no dietary decision should turn on. It is the honest starting "
            "point for every claim in this record."
        ),
    ),
    Metric(
        name="Sample size required to detect an interaction",
        symbol="N_int",
        unit="participants",
        typical="roughly four times the sample needed for a main effect of the "
        "same magnitude, and gene-diet interactions are smaller to begin with",
        formula="statistical_power",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The arithmetic that explains the field's replication record. A "
            "study adequately powered to associate a variant with a trait is "
            "badly underpowered to detect how that variant modifies a dietary "
            "response, and most published gene-diet interactions come from such "
            "studies. This is a methodological fact rather than a criticism of "
            "any particular result."
        ),
    ),
    Metric(
        name="Replication rate of published gene-diet interactions",
        symbol="f_repl",
        unit="per cent of reported interactions confirmed in independent "
        "cohorts",
        typical="low",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The empirical consequence of the two entries above. It is recorded "
            "as a metric because a field's replication rate is a measurable "
            "property of that field, and because in this record it is the "
            "single most useful figure for judging any individual claim."
        ),
    ),
    # =========================================================================
    #  WHAT A TEST ACTUALLY PREDICTS
    # =========================================================================
    Metric(
        name="Variance explained by a polygenic score",
        symbol="R2_PGS",
        unit="per cent of trait variance explained",
        typical="single digits for most nutrition-related traits",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Useful for research and for population stratification, and "
            "insufficient for individual dietary prescription. A score "
            "explaining five per cent of variance leaves ninety-five per cent "
            "to everything else, which is the quantitative form of the "
            "objection this record makes to consumer testing."
        ),
    ),
    Metric(
        name="Portability of a polygenic score across ancestries",
        symbol="P_anc",
        unit="relative predictive performance in a non-matched population",
        typical="substantially reduced outside the ancestry the score was "
        "derived in",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Scores derived overwhelmingly in European-ancestry cohorts perform "
            "considerably worse elsewhere, so a consumer test is least "
            "informative for the populations least represented in the "
            "underlying research. It is the same equity failure "
            "`gold.genomics_data_analysis` records and it reaches consumers "
            "here."
        ),
    ),
    Metric(
        name="Number needed to genotype",
        symbol="NNG",
        unit="people tested per person whose management changes",
        typical="very small for clinically actionable monogenic variants and "
        "very large for common variant panels",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The metric that separates the two halves of this record in one "
            "figure. Newborn screening for phenylketonuria changes management "
            "for everyone who tests positive; a common variant panel changes "
            "almost nobody's management in a way that improves an outcome."
        ),
    ),
    # =========================================================================
    #  THE MONOGENIC HALF, WHERE THE NUMBERS ARE DIFFERENT
    # =========================================================================
    Metric(
        name="Penetrance of a monogenic variant",
        symbol="f_pen",
        unit="per cent of carriers showing the phenotype",
        typical="essentially complete for phenylketonuria; variable for "
        "hereditary haemochromatosis",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Why the monogenic half is actionable and why not all of it is "
            "equally so. Complete penetrance means the genotype determines the "
            "requirement. Incomplete penetrance, as in haemochromatosis where "
            "many carriers never develop iron overload, means the genotype "
            "indicates monitoring rather than treatment."
        ),
    ),
    Metric(
        name="Newborn screening coverage",
        symbol="f_screen",
        unit="per cent of births screened for treatable metabolic disorders",
        typical="high in health systems with an established programme, and "
        "absent in many others",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The delivery metric for the field's clearest success, and it is "
            "unevenly distributed. A condition entirely preventable by early "
            "dietary management still causes permanent disability where no "
            "screening programme exists, which is an access problem rather than "
            "a scientific one."
        ),
    ),
    # =========================================================================
    #  WHAT ACTUALLY PREDICTED RESPONSE
    # =========================================================================
    Metric(
        name="Interindividual variability in postprandial response",
        symbol="CV_pp",
        unit="coefficient of variation in glucose or lipid response to an "
        "identical meal",
        typical="large, and considerably greater than variability within one "
        "person on repeat testing",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The finding that made personalised nutrition credible as an idea. "
            "People differ substantially and reproducibly in how they respond "
            "to the same meal, which means personalisation has something real "
            "to personalise. What it does not establish is that genotype is how "
            "to do it."
        ),
    ),
    Metric(
        name="Predictive contribution of the microbiome relative to genotype",
        symbol="f_micro",
        unit="relative contribution to a predictive model of dietary response",
        typical="microbiome and behavioural features have contributed more "
        "than genetic features in the studies that compared them",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The most awkward number in a field named after genomes. It is "
            "graded REPORTED because it comes from a small number of large "
            "studies whose models are not fully public, and the direction has "
            "been consistent. It is the reason `linkage.py` treats "
            "`yellow.probiotics_and_prebiotics` as a live connection rather "
            "than a neighbouring topic."
        ),
    ),
    # =========================================================================
    #  THE TRIAL EVIDENCE
    # =========================================================================
    Metric(
        name="Difference in outcome between genotype-matched and unmatched "
        "diets",
        symbol="dOutcome",
        unit="difference in weight, lipid or glycaemic outcome",
        typical="no significant advantage found in the largest controlled "
        "trials",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The trial evidence the commercial field is inconsistent with. "
            "Assigning diets by genotype has not outperformed assigning them "
            "otherwise in adequately powered randomised comparisons. A null "
            "result of this kind is not proof that no such effect exists, and "
            "it is the best evidence currently available and it points one way."
        ),
    ),
    Metric(
        name="Adherence to the assigned diet",
        symbol="f_adhere",
        unit="per cent of participants following the assigned diet",
        typical="the dominant determinant of outcome in dietary trials, "
        "exceeding any genotype effect",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Included because it puts the whole record in proportion. Whether a "
            "person actually follows a diet predicts their outcome far better "
            "than which diet it was or what their genotype is. Any "
            "personalisation that improves adherence may work for that reason "
            "rather than for the reason claimed."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  The statistical relationships that this record turns on.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "statistical_power",
    "odds_ratio",
    "relative_risk",
    "heritability",
    "variance_explained",
    "bayes_theorem",
)
