# =============================================================================
#  biotechnology.branches.yellow.food_safety_biotechnology.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS A TIME, NOT A LIMIT OF DETECTION, AND THAT ORDERING IS
#  THE ARGUMENT OF THE RECORD.
#
#  Sensitivity was never the binding problem. Culture-based detection is
#  extremely sensitive and takes days, by which time a chilled product has been
#  eaten. What molecular methods changed is when the answer arrives, and a
#  result that arrives while the batch is still on site is a different kind of
#  thing from one that arrives afterwards.
#
#  THE SECOND GROUP IS WHERE THE FIELD'S HONESTY IS TESTED. Sensitivity and
#  specificity are reported for every method and mean less here than in
#  `red.molecular_diagnostics`, because the sample analysed is a few hundred
#  grams from a consignment of tonnes. The probability of detection at a given
#  prevalence, which combines method performance with the sampling plan, is the
#  figure that actually describes what a test achieves, and it is quoted far
#  less often because it is far less flattering.
#
#  A NOTE ON WHY A FALSE POSITIVE IS EXPENSIVE HERE. In clinical testing a
#  false positive leads to a confirmatory test. In food it can lead to the
#  destruction of a batch, so the cost asymmetry runs the other way and the
#  viability question becomes commercially decisive rather than academic.
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
    #  THE QUANTITY THAT CHANGED THE FIELD
    # =========================================================================
    Metric(
        name="Time to result",
        symbol="t_result",
        unit="hours from sample receipt to reportable answer",
        typical="2 - 24 h for molecular methods including enrichment, against "
        "48 - 120 h for culture confirmation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Placed first because it is what actually changed. Sensitivity was "
            "never the binding constraint: culture is extremely sensitive and "
            "slow. A result arriving while the batch is still under the "
            "producer's control is a decision; the same result three days later "
            "is a record. Everything else in this record follows from that "
            "distinction."
        ),
    ),
    Metric(
        name="Enrichment time",
        symbol="t_enrich",
        unit="hours of incubation before detection",
        typical="6 - 24 h, and the dominant component of the entry above",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The remaining bottleneck, and it is biological rather than "
            "instrumental. A pathogen present at one cell in twenty-five grams "
            "must be multiplied before any method can find it. Enrichment also "
            "does useful work by selecting for viable organisms, which is why "
            "removing it entirely would worsen the viability problem below."
        ),
    ),
    # =========================================================================
    #  WHAT THE METHOD CAN DO, AND WHY IT MATTERS LESS THAN IT SEEMS
    # =========================================================================
    Metric(
        name="Limit of detection",
        symbol="LOD",
        unit="colony forming units per twenty-five grams of sample",
        typical="1 - 10 CFU per 25 g after enrichment",
        formula="limit_of_detection",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Quoted per twenty-five grams because that is the standard sample "
            "unit in food microbiology, and the unit is the point: the method "
            "finds a single cell in the sample it is given, and says nothing "
            "about the rest of the consignment."
        ),
    ),
    Metric(
        name="Diagnostic sensitivity and specificity",
        symbol="Se_Sp",
        unit="per cent, against a reference method on the same matrix",
        typical="both above 95 % for validated methods",
        formula="sensitivity_specificity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Must be established in the food matrix rather than in broth, "
            "because inhibition by fat, protein and polyphenols is matrix "
            "specific. A method validated on chicken rinse is not validated on "
            "chocolate, and the distinction is a formal part of method "
            "approval."
        ),
    ),
    Metric(
        name="Probability of detection at a given prevalence",
        symbol="P_det",
        unit="probability that a contaminated lot is detected by the sampling "
        "plan",
        formula="detection_probability",
        typical="low for the low prevalences that matter, even with a perfect "
        "method",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The figure that actually describes what a testing programme "
            "achieves, and the least often quoted because it is the least "
            "flattering. It combines method performance with the sampling plan, "
            "and it shows why sampling rather than sensitivity is this record's "
            "binding constraint. A perfect test on an unrepresentative sample "
            "is an unrepresentative result."
        ),
    ),
    # =========================================================================
    #  WHAT A POSITIVE COSTS
    # =========================================================================
    Metric(
        name="False positive rate",
        symbol="R_fp",
        unit="per cent of positives not confirmed by the reference method",
        typical="low for validated methods and consequential when it occurs",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The cost asymmetry here is the reverse of clinical testing. A "
            "clinical false positive leads to a confirmatory test; a food false "
            "positive can lead to the destruction of a batch. That is why "
            "confirmation remains mandatory before action and why the viability "
            "question below is commercial rather than academic."
        ),
    ),
    Metric(
        name="Viable versus total nucleic acid discrimination",
        symbol="f_viable",
        unit="qualitative, whether the method distinguishes live from dead "
        "cells",
        typical="not distinguished by standard amplification without a "
        "viability treatment",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The characteristic weakness of molecular detection in food. After "
            "a kill step the dead organisms remain and their nucleic acid is "
            "amplifiable, so a positive may report a hazard that no longer "
            "exists. Viability dyes and enrichment both address it partially "
            "and neither resolves it."
        ),
    ),
    # =========================================================================
    #  LINKING CASES TO A SOURCE
    # =========================================================================
    Metric(
        name="Genomic cluster distance threshold",
        symbol="d_SNP",
        unit="single nucleotide polymorphisms or allele differences between "
        "isolates",
        typical="commonly fewer than 5 to 10 differences taken as evidence of "
        "a close epidemiological relationship",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A convention rather than a fact, and one that must be set per "
            "organism because mutation rates differ. Isolates within the "
            "threshold are not necessarily linked and isolates outside it are "
            "not necessarily unrelated. It is the number on which outbreak "
            "attributions turn and it deserves more scepticism than it usually "
            "receives."
        ),
    ),
    Metric(
        name="Outbreak detection interval",
        symbol="t_outbreak",
        unit="days from first case to cluster identification",
        typical="substantially shortened by routine genomic surveillance",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The public health equivalent of the first metric. Shortening it "
            "means fewer subsequent cases, which is the actual benefit of "
            "routine sequencing. It has also produced the resourcing problem in "
            "`practice.CHALLENGES`, since clusters are now identified faster "
            "than investigators can follow them."
        ),
    ),
    # =========================================================================
    #  THE THRESHOLDS THAT ARE LEGAL FACTS
    # =========================================================================
    Metric(
        name="Allergen quantification limit",
        symbol="LOQ_allergen",
        unit="milligrams of allergen protein per kilogram of food",
        typical="single-digit mg/kg for validated immunoassays; the gluten-free "
        "threshold is 20 mg/kg",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The gluten-free threshold is one of the few allergen limits with a "
            "numerical legal definition, which makes it measurable rather than "
            "arguable. Results vary between kits because immunoassays respond "
            "differently to processed proteins, so a result depends on the "
            "method as well as on the food."
        ),
    ),
    Metric(
        name="Mycotoxin maximum level",
        symbol="c_myco",
        unit="micrograms per kilogram",
        typical="set in legislation by toxin and food category, with the "
        "tightest limits on infant food",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A legal limit rather than a technical capability, and the reason "
            "mycotoxin testing is routine rather than investigative. The toxin "
            "persists after the fungus is gone, so this is one of the few "
            "hazards where testing the finished product is the only control "
            "available."
        ),
    ),
    Metric(
        name="Species substitution rate in surveys",
        symbol="f_subst",
        unit="per cent of sampled products not matching their declared species",
        typical="repeatedly found to be substantial in fish and in some meat "
        "products",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Recorded because authenticity is not a lesser subject in this "
            "record. Substitution is an economic crime with safety "
            "consequences, including undeclared allergens and species carrying "
            "specific hazards, and survey results have consistently been higher "
            "than the industry expected."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Detection performance first, then the sampling statistics that qualify it.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "limit_of_detection",
    "sensitivity_specificity",
    "detection_probability",
    "prevalence_estimation",
    "bayes_theorem",
    "serial_dilution",
)
