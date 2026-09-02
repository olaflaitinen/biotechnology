# =============================================================================
#  biotechnology.branches.red.pharmacogenomics.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The metrics here come from two different disciplines that meet in this
#  record and use numbers differently.
#
#  PHARMACOKINETICS supplies clearance, half-life and exposure. These are
#  continuous, measurable in an individual, and predict what a dose will do.
#
#  GENETICS supplies the activity score and the allele frequency. These are
#  discrete, defined by committee rather than measured, and predict which group
#  a patient belongs to.
#
#  The activity score is worth particular attention: it is a consensus
#  construct, not a measurement. Assigning a value of 0.5 to a reduced-function
#  allele is a decision made by an expert panel, it has been revised, and two
#  laboratories using different versions of the table can report different
#  phenotypes from identical genotype data. That is recorded here rather than
#  glossed over, because it is the kind of thing a reader assumes is a
#  measurement when it is not.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # -------------------------------------------------------------------------
    #  Activity score. A consensus construct rather than a measurement, and the
    #  central object of the field.
    # -------------------------------------------------------------------------
    Metric(
        name="Activity score",
        symbol="AS",
        unit="dimensionless, summed across two alleles",
        typical="0 to 3, occasionally higher with gene duplication",
        formula="pharmacogene_activity_score",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The sum of the functional values assigned to the two inherited "
            "alleles: typically 1 for normal function, 0.5 for reduced, 0 for "
            "none. Those values are assigned by expert consensus, not measured, "
            "and the assignments have been revised. Two laboratories using "
            "different versions of the allele definition table can report "
            "different phenotypes from identical genotype data, which is why "
            "the table version belongs on the report."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Metaboliser phenotype. The discrete category the score maps onto, and
    #  the thing a guideline actually keys on.
    # -------------------------------------------------------------------------
    Metric(
        name="Metaboliser phenotype",
        symbol="PM/IM/NM/RM/UM",
        unit="ordered category",
        typical="poor, intermediate, normal, rapid, ultrarapid",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A discretisation of a continuous quantity, and therefore lossy at "
            "the boundaries. A patient just inside one category behaves almost "
            "identically to one just inside the next. The categories exist "
            "because prescribing advice has to be actionable, not because "
            "metabolism is discrete."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Clearance. The pharmacokinetic quantity the genotype is predicting.
    # -------------------------------------------------------------------------
    Metric(
        name="Apparent oral clearance",
        symbol="CL/F",
        unit="litres per hour",
        typical="drug- and genotype-specific",
        formula="drug_clearance",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Clearance between a poor and an ultrarapid metaboliser can differ "
            "by more than tenfold for a drug handled by a single enzyme. Where "
            "two or more enzymes share the work, the genotype of any one of "
            "them matters far less, which is why only some drugs are worth "
            "genotyping for."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Exposure. What toxicity and efficacy actually track.
    # -------------------------------------------------------------------------
    Metric(
        name="Area under the concentration-time curve",
        symbol="AUC",
        unit="milligram hours per litre",
        typical="drug-specific",
        formula="area_under_curve",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Total exposure. For most drugs toxicity tracks AUC more closely "
            "than it tracks peak concentration, which is why a slow metaboliser "
            "on a standard dose is at risk even though nothing about any single "
            "measurement looks alarming."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Half-life. Determines how long a wrong dose keeps being wrong.
    # -------------------------------------------------------------------------
    Metric(
        name="Elimination half-life",
        symbol="t_half",
        unit="hours",
        typical="1 - 100 h",
        formula="elimination_half_life",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Steady state is reached after roughly five half-lives. A poor "
            "metaboliser therefore accumulates for far longer than expected "
            "before the problem becomes visible, which is why the harm often "
            "appears days into a course rather than after the first dose."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Allele frequency. The number that decides whether population screening
    #  is worthwhile, and the one most distorted by the ancestry problem.
    # -------------------------------------------------------------------------
    Metric(
        name="Allele frequency",
        symbol="f",
        unit="fraction of chromosomes in a population",
        typical="0.001 - 0.40, varying sharply between ancestries",
        formula="hardy_weinberg",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "HLA-B*15:02 is common in parts of Southeast Asia and rare in "
            "Europe, so the same screening policy is cost-effective in one "
            "place and not in another. Reference frequencies are drawn "
            "overwhelmingly from European-ancestry cohorts, which is the "
            "quantitative form of the equity problem in "
            "practice.CHALLENGES."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Number needed to genotype. The health economics metric.
    # -------------------------------------------------------------------------
    Metric(
        name="Number needed to genotype",
        symbol="NNG",
        unit="patients tested per adverse event prevented",
        typical="15 to several hundred",
        formula="number_needed_to_treat",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Falls sharply under pre-emptive panel testing, because one test "
            "serves every future prescription rather than one. That is the "
            "whole economic argument for testing before anyone is ill, and it "
            "is why reactive reimbursement rules understate the value."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Therapeutic index. Explains why the field concentrates where it does.
    # -------------------------------------------------------------------------
    Metric(
        name="Therapeutic index",
        symbol="TI",
        unit="ratio of toxic to effective dose",
        typical="< 3 for the drugs where genotyping matters most",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A wide therapeutic index absorbs a tenfold difference in clearance "
            "without consequence. Every drug on the actionable list has a "
            "narrow one, which is the single best predictor of whether a gene "
            "is worth testing."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  loading_dose is included because it is the calculation most directly changed
#  by a genotype result, and odds_ratio because it is how the association
#  between an HLA allele and a hypersensitivity reaction is reported.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "pharmacogene_activity_score",
    "drug_clearance",
    "area_under_curve",
    "elimination_half_life",
    "loading_dose",
    "maintenance_dose",
    "hardy_weinberg",
    "number_needed_to_treat",
    "odds_ratio",
)
