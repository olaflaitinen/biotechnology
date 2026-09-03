# =============================================================================
#  biotechnology.branches.grey.environmental_biomonitoring.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS IS THE ONLY FACET IN THE LIBRARY WHOSE METRICS ARE THE SUBJECT MATTER
#  RATHER THAN A DESCRIPTION OF IT. The record is about measurement, so the
#  entries below are the instruments themselves.
#
#  THE FIRST ENTRY IS NOT A MEASUREMENT. IT IS THE THING EVERY MEASUREMENT IS
#  COMPARED AGAINST.
#
#  A biological index does not report a quantity. It reports a ratio between
#  what was observed and what was expected at an undisturbed site of the same
#  type, and that expectation is a judgement made by people using the least
#  disturbed places they could find. Put the reference condition first and
#  every number below it is legible; leave it out and the classifications read
#  as though they were absolute.
#
#      THE REFERENCE CONDITION IS THE MEASUREMENT THAT DECIDES ALL THE OTHERS,
#      AND IT IS NOT ITSELF MEASURED.
#
#  THE SECOND ORGANISING IDEA IS THE DETECTION PROBABILITY. In every other
#  record in this branch a non-detection means the substance was not there. In
#  this one it usually does not, because organisms are missed. Reporting
#  absence without an estimate of detection probability is the commonest error
#  in the field, so the metric is placed high and named plainly.
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
    #  THE EXPECTATION EVERYTHING IS COMPARED AGAINST
    # =========================================================================
    Metric(
        name="Reference condition",
        symbol="E_ref",
        unit="expected community composition for the water body type",
        typical="derived from the least disturbed available sites, from "
        "historical records, or from a model",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Placed first because every index below is a comparison against it "
            "and because it is a judgement rather than an observation. In most "
            "regions undisturbed sites no longer exist, so the reference is "
            "the best remaining, which means each assessment generation "
            "calibrates against the world it inherited. That is the shifting "
            "baseline problem stated as a metric rather than as a complaint."
        ),
    ),
    Metric(
        name="Ecological quality ratio",
        symbol="EQR",
        unit="observed value divided by the reference value, scaled from zero "
        "to one",
        typical="banded into classes, with a threshold defining good status",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The form in which the entry above becomes a legal judgement. It "
            "makes different index systems comparable across countries by "
            "expressing each as a fraction of its own reference. The class "
            "boundaries are negotiated as well as derived, which is worth "
            "knowing when a water body moves between classes without changing "
            "much."
        ),
    ),
    # =========================================================================
    #  THE ERROR THAT IS SPECIFIC TO MEASURING ORGANISMS
    # =========================================================================
    Metric(
        name="Detection probability",
        symbol="p_det",
        unit="probability of detecting a species given that it is present",
        formula="occupancy_model",
        typical="well below one for rare, cryptic and seasonally active "
        "species",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The metric that separates a competent survey from a misleading "
            "one. In chemistry a non-detection below a stated limit means "
            "absence; here it usually does not, because organisms are missed. "
            "Reporting an absence without estimating this is the commonest "
            "error in the field, and it matters most exactly where the stakes "
            "are highest, which is a rare species or a newly arrived invader."
        ),
    ),
    Metric(
        name="Sampling effort required for confident absence",
        symbol="n_eff",
        unit="number of samples or replicates",
        typical="rises steeply as detection probability falls",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The practical consequence of the entry above, and what a survey is "
            "actually designed around. Declaring a species absent from a site "
            "requires enough replicates that the chance of repeated misses is "
            "small, and for a cryptic species that number is large enough to "
            "change the cost of the programme."
        ),
    ),
    # =========================================================================
    #  THE COMMUNITY INDICES THEMSELVES
    # =========================================================================
    Metric(
        name="Biotic index score",
        symbol="BI",
        unit="weighted score derived from the pollution tolerance of taxa "
        "present",
        typical="high where sensitive groups persist, low where only tolerant "
        "groups remain",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The backbone of river assessment. It works because tolerance is "
            "well characterised for the groups used, and it integrates "
            "exposure over the life of the animals rather than over the moment "
            "of sampling. It tells an assessor that something is wrong and "
            "rarely what, which is why it is deployed alongside chemistry."
        ),
    ),
    Metric(
        name="Taxonomic richness and diversity",
        symbol="H",
        unit="number of taxa, or a diversity index value",
        typical="falls under most forms of disturbance, and not always",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Included with a caution that the field learned the hard way. "
            "Moderate nutrient enrichment can raise diversity, so richness "
            "alone is not a health measure. It is informative in combination "
            "with the tolerance-weighted score above and misleading on its own, "
            "which is why multimetric indices exist."
        ),
    ),
    Metric(
        name="Community composition dissimilarity",
        symbol="d_beta",
        unit="dissimilarity between observed and reference community "
        "composition",
        typical="the basis of molecular assessment, where taxonomy may be "
        "incomplete",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "How a metabarcoding result is turned into an assessment without "
            "needing every sequence identified to species. It sidesteps the "
            "reference database gap by comparing whole communities rather than "
            "naming their members, which is a real advantage and gives up the "
            "interpretability that named indicator taxa provide."
        ),
    ),
    # =========================================================================
    #  MEASURING A SUBSTANCE THROUGH AN ORGANISM
    # =========================================================================
    Metric(
        name="Bioconcentration factor",
        symbol="BCF",
        unit="ratio of tissue concentration to ambient concentration",
        formula="bioconcentration_factor",
        typical="high for persistent lipophilic compounds in filter feeders",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Why an organism can find what an instrument cannot. A filter "
            "feeder processing large volumes concentrates a persistent compound "
            "to a level that is measurable when the ambient concentration is "
            "not. The same symbol appears in `grey.phytoremediation`, where the "
            "purpose is removal rather than detection."
        ),
    ),
    Metric(
        name="Biomarker response",
        symbol="R_bio",
        unit="fold induction of an enzyme or other physiological endpoint",
        typical="responds within days of exposure and before any community "
        "change is visible",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The earliest signal available, and the least specific. It shows "
            "that an organism has responded to something, which is valuable as "
            "a warning and weak as evidence of what. It sits between chemistry, "
            "which is specific and instantaneous, and community indices, which "
            "are integrative and slow."
        ),
    ),
    Metric(
        name="Whole effluent toxicity",
        symbol="EC50",
        unit="dilution at which half of the test organisms show the measured "
        "effect",
        typical="reported for a defined species and exposure duration",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Asks whether a discharge harms organisms rather than whether it "
            "exceeds a list of limits, so it captures mixtures whose components "
            "are each individually compliant. That is precisely the case a "
            "substance-by-substance consent cannot address."
        ),
    ),
    # =========================================================================
    #  THE MOLECULAR MEASUREMENTS
    # =========================================================================
    Metric(
        name="Environmental DNA concentration",
        symbol="c_eDNA",
        unit="target copies per litre of filtered water",
        typical="varies with shedding rate, flow, temperature and degradation",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Quantifiable and only loosely related to abundance. It reflects "
            "how much material was shed, how far it travelled and how fast it "
            "degraded, all of which vary by species, season and river. It is "
            "strong evidence of presence and weak evidence of quantity, and "
            "reporting it as a population estimate is the field's commonest "
            "overreach."
        ),
    ),
    Metric(
        name="Environmental DNA persistence and transport distance",
        symbol="L_eDNA",
        unit="hours of persistence, and metres to kilometres of downstream "
        "transport",
        typical="hours to days, over distances that are substantial in flowing "
        "water",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The reason a detection is not a location. Material travels "
            "downstream and persists after the organism has gone, so a positive "
            "result places the species somewhere upstream within a window "
            "rather than at the sampling point now. Interpreting a detection "
            "spatially without this is a category error."
        ),
    ),
    Metric(
        name="Reference database coverage",
        symbol="f_ref",
        unit="per cent of expected regional taxa with a reference sequence",
        typical="high for well-studied groups in well-studied regions, and "
        "poor otherwise",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The invisible dependency of every molecular result in this record. "
            "A species with no reference entry cannot be identified however "
            "much of its DNA is in the sample, so a species list is a list of "
            "what could have been recognised. It also means the method performs "
            "best where biodiversity is already best documented, which is the "
            "opposite of where it is most needed."
        ),
    ),
    Metric(
        name="Functional gene abundance",
        symbol="N_gene",
        unit="gene copies per gram or per litre",
        typical="the standard evidence for degradation capability at a "
        "remediation site",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The service this record provides to the rest of the branch. It "
            "establishes whether the capability `grey.bioremediation` relies on "
            "is present, and whether an introduced population in "
            "`grey.bioaugmentation` survived. It shows capability rather than "
            "activity, which is why isotope evidence is used beside it."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Detection and community statistics, then the accumulation and degradation
#  relationships.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "occupancy_model",
    "shannon_diversity_index",
    "bioconcentration_factor",
    "rayleigh_fractionation",
    "dose_response_curve",
    "first_order_decay",
)
