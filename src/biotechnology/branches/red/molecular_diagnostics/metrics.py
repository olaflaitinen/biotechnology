# =============================================================================
#  biotechnology.branches.red.molecular_diagnostics.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the most consequential set of metric notes in the library, because
#  these are the numbers the public reads about testing and they are almost
#  always reported in a way that omits the thing that matters.
#
#  The distinction that carries the weight is between the two pairs:
#
#    SENSITIVITY and SPECIFICITY are properties of the TEST. They do not change
#    when the disease becomes rarer.
#
#    POSITIVE and NEGATIVE PREDICTIVE VALUE are properties of the TEST AND THE
#    POPULATION TOGETHER. They change dramatically with prevalence, and they
#    are what a person actually wants to know when they are handed a result.
#
#  A test with 99 % sensitivity and 99 % specificity, applied where one person
#  in ten thousand has the condition, produces roughly one true positive for
#  every hundred false ones. Nothing is wrong with the test. That is why the
#  `predictive_values` formula exists and why every note below points at it.
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
    #  Quantification cycle. The raw output of every real-time PCR instrument.
    # -------------------------------------------------------------------------
    Metric(
        name="Quantification cycle",
        symbol="Cq",
        unit="amplification cycles",
        typical="15 - 40 cycles",
        formula="qpcr_quantification_cycle",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Also written Ct in older literature. A lower Cq means more "
            "starting template, and the relationship is logarithmic: a "
            "difference of about 3.3 cycles is a tenfold difference in "
            "starting material. A Cq is not comparable between assays, "
            "instruments or laboratories without a common calibrator."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Amplification efficiency. The quality control on the assay itself.
    # -------------------------------------------------------------------------
    Metric(
        name="Amplification efficiency",
        symbol="E",
        unit="dimensionless fraction",
        typical="0.90 - 1.10, reported as 90 - 110 per cent",
        formula="pcr_efficiency",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Derived from the slope of a standard curve as E = 10^(-1/slope) - 1. "
            "An efficiency outside this window invalidates any quantitative "
            "claim made from the Cq, which is why the MIQE guidelines require "
            "it to be reported."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Limit of detection. Where the assay stops being able to answer.
    # -------------------------------------------------------------------------
    Metric(
        name="Limit of detection",
        symbol="LoD",
        unit="copies per millilitre of original specimen",
        typical="10 - 1000 copies/mL",
        formula="limit_of_detection",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Conventionally the concentration detected in 95 per cent of "
            "replicates. Quoted per millilitre of specimen rather than per "
            "reaction, because the extraction step concentrates or dilutes and "
            "a figure per reaction hides that."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Sensitivity. A property of the test.
    # -------------------------------------------------------------------------
    Metric(
        name="Diagnostic sensitivity",
        symbol="Se",
        unit="fraction of true cases correctly identified",
        typical="0.90 - 0.999",
        formula="sensitivity_specificity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Of the people who have the condition, the fraction the test finds. "
            "It is a property of the test and does not change with prevalence. "
            "It is also measured against a reference standard, so a sensitivity "
            "figure is only as good as the standard it was compared with."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Specificity. Also a property of the test, and the one that dominates
    #  when a condition is rare.
    # -------------------------------------------------------------------------
    Metric(
        name="Diagnostic specificity",
        symbol="Sp",
        unit="fraction of true non-cases correctly cleared",
        typical="0.95 - 0.9999",
        formula="sensitivity_specificity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Of the people who do not have the condition, the fraction the test "
            "correctly clears. When prevalence is low this is the number that "
            "decides how many false positives a programme generates, because "
            "the non-cases vastly outnumber the cases."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Positive predictive value. A property of the test AND the population.
    #  The metric the public actually cares about.
    # -------------------------------------------------------------------------
    Metric(
        name="Positive predictive value",
        symbol="PPV",
        unit="probability, dimensionless",
        typical="prevalence-dependent, from below 0.05 to above 0.99",
        formula="predictive_values",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "If your test is positive, the probability you actually have the "
            "condition. Unlike sensitivity and specificity this collapses when "
            "prevalence is low, however good the assay is. It is the single "
            "most misunderstood number in diagnostics, and the reason screening "
            "an entire population is a different proposition from testing "
            "someone with symptoms."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Likelihood ratio. Prevalence-independent, and therefore portable.
    # -------------------------------------------------------------------------
    Metric(
        name="Positive likelihood ratio",
        symbol="LR+",
        unit="dimensionless",
        typical="> 10 is considered strong evidence",
        formula="likelihood_ratio",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How much a positive result shifts the odds. Unlike predictive "
            "value it does not depend on prevalence, which makes it the right "
            "figure to carry between settings."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Turnaround time. The clinical metric, and often the one that decides
    #  whether a result changes anything.
    # -------------------------------------------------------------------------
    Metric(
        name="Turnaround time",
        symbol="TAT",
        unit="hours from sample receipt to reported result",
        typical="0.5 h at the point of care to 72 h for a sequencing panel",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A perfectly accurate result that arrives after the treatment "
            "decision has been made has no clinical value. This is why "
            "isothermal and cartridge platforms displace better-performing "
            "laboratory assays in acute settings."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  melting_temperature and poisson_partition are included because they underlie
#  assay design and digital PCR counting respectively, even though neither is
#  attached to a metric above.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "qpcr_quantification_cycle",
    "pcr_efficiency",
    "delta_delta_ct",
    "sensitivity_specificity",
    "predictive_values",
    "likelihood_ratio",
    "limit_of_detection",
    "poisson_partition",
    "melting_temperature",
    "gc_content",
    "serial_dilution",
)
