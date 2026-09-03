# =============================================================================
#  biotechnology.branches.blue.marine_genomics.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This facet measures a method rather than a product, so its metrics are
#  mostly measures of how much is known and how much is not. Two of them are
#  unusual enough to explain before the list.
#
#  THE FIRST METRIC IS A MEASURE OF IGNORANCE. The unassigned sequence
#  fraction, the proportion of reads matching nothing in any reference
#  database, is the number that most honestly describes the state of marine
#  genomics. It is high, and reporting it prominently rather than burying it is
#  the difference between a field that knows what it does not know and one that
#  describes only what it found.
#
#  THE CULTURABLE FRACTION IS RECORDED AS A METRIC because it is the single
#  quantity that justifies the existence of this record. If most marine
#  microorganisms grew on a plate, culture-independent sequencing would be a
#  convenience rather than a necessity.
#
#  A WARNING ABOUT ENVIRONMENTAL DNA. Detection and abundance are different
#  questions, and eDNA answers the first far better than the second. A strong
#  signal may mean many animals, one animal recently, or one animal upstream.
#  The metric below carries that caution rather than leaving it to the reader.
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
    #  HOW MUCH IS NOT KNOWN
    # =========================================================================
    Metric(
        name="Unassigned sequence fraction",
        symbol="f_dark",
        unit="per cent of reads with no match in reference databases",
        typical="commonly a third to two thirds in open ocean metagenomes, "
        "and higher in deep sea and sediment samples",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The most honest single description of this field's state, and the "
            "reason it is placed first. It measures the reference databases as "
            "much as the sample: a high fraction means marine lineages are "
            "under-represented in what has been sequenced before, not "
            "necessarily that the sample is exotic. It falls as databases "
            "improve, which makes it a moving figure rather than a property of "
            "the ocean."
        ),
    ),
    Metric(
        name="Culturable fraction",
        symbol="f_cult",
        unit="per cent of cells observed that will grow in laboratory culture",
        typical="commonly quoted as around 1 %, and varying by habitat",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The quantity that justifies culture-independent sequencing "
            "existing at all. Long known as the great plate count anomaly, the "
            "gap between cells counted under a microscope and colonies that "
            "appear on a plate. If this figure were high, this record would be "
            "a convenience rather than a necessity."
        ),
    ),
    # =========================================================================
    #  WHETHER A GENOME RECONSTRUCTED FROM A MIXTURE CAN BE TRUSTED
    # =========================================================================
    Metric(
        name="Genome completeness",
        symbol="C_gen",
        unit="per cent of expected single-copy marker genes present",
        typical="above 90 % for a high-quality metagenome-assembled genome",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Estimated from marker genes expected once in every genome of a "
            "lineage, so it is an inference rather than a measurement. It "
            "cannot detect the absence of a gene family that the marker set "
            "does not cover, which matters when the organism is from a lineage "
            "with no cultured representative and therefore no well-calibrated "
            "marker set."
        ),
    ),
    Metric(
        name="Contamination of an assembled genome",
        symbol="X_gen",
        unit="per cent of markers present in more than one copy",
        typical="below 5 % for a high-quality bin",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Always read together with completeness, since the two trade "
            "against each other: a permissive binning threshold raises "
            "completeness and drags in sequence from relatives. It is "
            "particularly awkward in this field because host and symbiont "
            "genomes arrive together by design rather than by accident."
        ),
    ),
    Metric(
        name="Assembly contiguity",
        symbol="N50",
        unit="base pairs",
        typical="kilobases for a short-read metagenome, megabases for a "
        "long-read single genome",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The length such that half the assembly sits in fragments at least "
            "that long. It is a convenience statistic rather than a quality "
            "measure and can be improved by discarding short fragments, so it "
            "should be quoted with the total assembly length beside it."
        ),
    ),
    # =========================================================================
    #  HOW MUCH SEQUENCING IS ENOUGH
    # =========================================================================
    Metric(
        name="Sequencing depth",
        symbol="D_seq",
        unit="gigabases per sample",
        typical="1 - 100 Gb depending on community complexity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "What counts as sufficient depends entirely on the community: a "
            "low-diversity vent community is well covered by an effort that "
            "barely scratches a sediment sample. Depth also determines which "
            "organisms are recovered at all, since rare members appear only "
            "above a threshold that is rarely stated."
        ),
    ),
    Metric(
        name="Coverage of the rare biosphere",
        symbol="f_rare",
        unit="per cent of estimated diversity recovered at a given depth",
        typical="rarely above 60 - 80 % for a complex marine community",
        formula="rarefaction_curve",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Marine communities are dominated by a few abundant taxa and a very "
            "long tail of rare ones, and the tail is where most of the "
            "biosynthetic novelty in `blue.marine_natural_products` sits. "
            "Sampling to exhaustion is generally impossible, so this metric "
            "records how far short of it a study stopped."
        ),
    ),
    # =========================================================================
    #  DETECTING ANIMALS FROM WATER
    # =========================================================================
    Metric(
        name="Environmental DNA detection probability",
        symbol="p_det",
        unit="probability of detecting a species present, per sample",
        typical="high for abundant species close by, poor for rare or distant "
        "ones",
        formula="detection_probability",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Detection and abundance are different questions and eDNA answers "
            "the first far better. A strong signal may mean many animals, one "
            "animal recently, or one animal upstream, since transport and "
            "degradation both act on the trace before it is collected. "
            "Quantitative claims from eDNA require calibration that most "
            "studies do not have."
        ),
    ),
    Metric(
        name="Environmental DNA persistence",
        symbol="t_eDNA",
        unit="hours to days before degradation below detection",
        typical="hours to a few days in warm surface water, longer in cold "
        "and dark conditions",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Short persistence is the property that makes eDNA useful: a "
            "detection means recent presence rather than historical. It is also "
            "what makes negative results weak, since an animal present "
            "yesterday may leave nothing detectable today."
        ),
    ),
    # =========================================================================
    #  THE COST THAT ACTUALLY GOVERNS
    # =========================================================================
    Metric(
        name="Cost per sample including collection",
        symbol="C_sample",
        unit="euro per sample, collection included",
        typical="dominated by ship time rather than by sequencing, and orders "
        "of magnitude higher for deep-sea access",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The metric that explains this field's geography. Sequencing costs "
            "have fallen by orders of magnitude and ship time has not, so the "
            "expensive step is now getting the water rather than reading it. "
            "This is why re-analysis of existing expedition data is such a "
            "productive activity and why open deposition matters more here "
            "than in most fields."
        ),
    ),
    Metric(
        name="Biosynthetic gene clusters per genome",
        symbol="n_BGC",
        unit="predicted clusters per assembled genome",
        typical="varying widely; enriched in sponge and sediment symbionts",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The bridge from this record to `blue.marine_natural_products`. A "
            "predicted cluster is a hypothesis about chemistry, not a compound: "
            "most predicted clusters are never expressed under any condition "
            "anyone has tried, and prediction of the product's structure from "
            "sequence remains unreliable."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Fewer than a process record and mostly statistical, which is what a
#  measurement discipline looks like.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "rarefaction_curve",
    "shannon_diversity",
    "detection_probability",
    "sequencing_coverage",
    "n50_statistic",
)
