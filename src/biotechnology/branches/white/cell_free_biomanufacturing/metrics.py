# =============================================================================
#  biotechnology.branches.white.cell_free_biomanufacturing.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Every other record in this branch measures a process that runs for days in a
#  vessel. This one measures a reaction that runs for hours in a tube, and the
#  metrics that matter are correspondingly different.
#
#  THE FACET IS ORDERED TO MATCH THE THREE ADVANTAGES the record actually
#  sells: speed, access and portability. Time to result comes first, because it
#  is the only quantity on which this technology beats fermentation by orders
#  of magnitude rather than by a factor. Titre appears further down, where it
#  belongs, since a cell-free system that matched a fermenter's titre would
#  still be chosen for the same reasons.
#
#  ONE METRIC HERE IS UNUSUAL AND DELIBERATE. Extract batch variability is
#  recorded as a first-class metric rather than as a caveat. It is the largest
#  practical obstacle to using these systems in regulated manufacture, it is
#  routinely omitted from publications, and a record that reported yields
#  without reporting their reproducibility would be reproducing the field's own
#  blind spot.
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
    #  ADVANTAGE ONE: SPEED
    # =========================================================================
    Metric(
        name="Time from template to product",
        symbol="t_result",
        unit="hours",
        typical="2 - 8 h, against 2 - 5 days for an equivalent result in cells",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The only figure on which this technology beats fermentation by "
            "orders of magnitude rather than by a factor, and therefore the one "
            "that justifies it. It excludes cloning and transformation entirely, "
            "because a linear template can be used directly, and that omission "
            "is most of the saving."
        ),
    ),
    Metric(
        name="Design-build-test cycle time",
        symbol="t_DBTL",
        unit="hours per iteration",
        typical="under 24 h, against days to weeks in a living host",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The metric that explains why prototyping is this record's largest "
            "genuine application. A field limited by how many designs can be "
            "tested rather than by how many can be conceived gains more from "
            "cycle time than from yield, which is the same argument "
            "`white.metabolic_engineering` makes about its own bottleneck."
        ),
    ),
    # =========================================================================
    #  WHAT THE REACTION ACTUALLY PRODUCES
    # =========================================================================
    Metric(
        name="Protein titre",
        symbol="C_p",
        unit="grams of protein per litre of reaction",
        typical="0.1 - 1 g/L routinely, with above 2 g/L reported for "
        "optimised bacterial extracts in batch",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Respectable against a fermentation on a per-litre basis and "
            "irrelevant on a per-euro basis, because the litre costs far more "
            "here. Reconstituted systems typically fall an order of magnitude "
            "below crude extracts, which is the price of knowing exactly what "
            "is present."
        ),
    ),
    Metric(
        name="Volumetric productivity",
        symbol="Q_p",
        unit="grams per litre per hour",
        typical="often favourable against fermentation, since the same titre "
        "is reached in hours rather than days",
        formula="space_time_yield",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The comparison that flatters cell-free systems most, and it should "
            "be read with the reaction duration beside it: high productivity "
            "sustained for four hours is a different asset from moderate "
            "productivity sustained for a fortnight."
        ),
    ),
    Metric(
        name="Reaction duration before stall",
        symbol="t_run",
        unit="hours of continued synthesis",
        typical="2 - 6 h in batch; 10 - 24 h or more in continuous exchange "
        "formats",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Ended by substrate depletion and by inhibitory by-product "
            "accumulation rather than by the machinery wearing out, which is "
            "why dialysis and continuous exchange formats extend it so "
            "effectively."
        ),
    ),
    # =========================================================================
    #  WHAT IT COSTS, WHICH IS THE HONEST WEAKNESS
    # =========================================================================
    Metric(
        name="Cost per milligram of product",
        symbol="C_mg",
        unit="euro per milligram",
        typical="one to three orders of magnitude above fermentation for the "
        "same protein",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The number that confines this technology to applications where "
            "speed, access or portability are worth paying for. It is dominated "
            "by the energy substrates and the extract, not by the template, and "
            "the shift from phosphorylated energy sources to glucose-based "
            "regeneration was the largest single reduction the field has "
            "achieved."
        ),
    ),
    Metric(
        name="Energy substrate consumption",
        symbol="n_ATP",
        unit="ATP equivalents per peptide bond formed",
        typical="at least 4 by stoichiometry, and considerably more in "
        "practice",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The stoichiometric floor is fixed by the mechanism of translation "
            "and cannot be engineered away. What can be improved is everything "
            "above the floor, meaning the energy lost to competing reactions in "
            "the extract, and the gap between the two is where the field's "
            "cost reduction work actually happens."
        ),
    ),
    # =========================================================================
    #  THE METRIC THE FIELD DOES NOT PUBLISH
    # =========================================================================
    Metric(
        name="Extract batch-to-batch variability",
        symbol="CV_extract",
        unit="per cent coefficient of variation in yield between preparations",
        typical="frequently substantial and rarely reported",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Recorded as a first-class metric rather than a caveat, because it "
            "is the largest practical obstacle to regulated manufacture and it "
            "is routinely omitted from publications. A crude extract is a "
            "complex undefined mixture whose composition depends on the growth "
            "and lysis of the cells it came from, and a process cannot be "
            "validated against a reagent whose behaviour is not characterised."
        ),
    ),
    # =========================================================================
    #  ADVANTAGE THREE: PORTABILITY
    # =========================================================================
    Metric(
        name="Shelf life of the lyophilised reaction",
        symbol="t_shelf",
        unit="months of retained activity at ambient temperature",
        typical="6 - 12 months reported without refrigeration",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The property that turns a biological process into a reagent that "
            "can be posted. It is what allows a specific molecular diagnostic to "
            "be performed where there is no laboratory, no power and no cold "
            "chain, and it is the basis of this record's SDG 3 claim."
        ),
    ),
    Metric(
        name="Limit of detection of a cell-free sensor",
        symbol="LOD",
        unit="molar concentration or copies per reaction",
        typical="picomolar to femtomolar when coupled to isothermal "
        "amplification, far poorer without it",
        formula="limit_of_detection",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Stated with its qualification because the qualification is the "
            "whole point: the cell-free readout supplies specificity and "
            "portability, and the amplification step supplies sensitivity. "
            "Reported sensitivities that omit the amplification are describing a "
            "different assay."
        ),
    ),
    # =========================================================================
    #  ADVANTAGE TWO: ACCESS
    # =========================================================================
    Metric(
        name="Non-standard amino acid incorporation efficiency",
        symbol="f_nsAA",
        unit="per cent of target sites correctly substituted",
        typical="above 90 % achievable at a single site in an optimised system",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Substantially easier here than in a living cell, because there is "
            "no competing native translation to outrun and no requirement that "
            "the organism survive the substitution. It is the clearest "
            "quantitative case of buying access to chemistry a cell will not "
            "permit."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Fewer than most records in this branch, which is itself informative: a
#  reaction in a tube has no transport correlations, no scale-up criteria and
#  no growth kinetics.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "space_time_yield",
    "michaelis_menten",
    "limit_of_detection",
    "mass_balance",
    "arrhenius_equation",
)
