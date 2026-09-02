# =============================================================================
#  biotechnology.branches.green.molecular_plant_breeding.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is the most quantitative in the green branch, because breeding
#  is the one part of biotechnology with a governing equation that practitioners
#  actually use to make decisions.
#
#  The breeder's equation, in the form that matters here, is
#
#      dG/t = (i * r * sigma_A) / L
#
#  meaning genetic gain per year equals selection intensity, times prediction
#  accuracy, times additive genetic standard deviation, divided by the
#  generation interval.
#
#  Every metric below is one of those four terms or a component of one, and
#  every technology in `practice.py` exists to improve a term. That is the
#  whole field in one line, and it explains a decision that otherwise looks
#  irrational: a breeder will deliberately accept LOWER prediction accuracy in
#  exchange for a SHORTER cycle, because r sits in the numerator while L sits
#  in the denominator, and halving L beats a modest loss in r.
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
    #  Heritability. How much of what you can see is worth selecting on.
    # -------------------------------------------------------------------------
    Metric(
        name="Narrow-sense heritability",
        symbol="h2",
        unit="fraction of phenotypic variance that is additive genetic",
        typical="0.1 for grain yield to 0.9 for plant height",
        formula="heritability",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The fraction of observed variation that a parent can actually "
            "transmit. It is a property of a population in an environment, not "
            "of a trait, so a heritability measured in one trial does not "
            "transfer to another. Low heritability is precisely why yield "
            "needs genomic selection while plant height does not."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The breeder's equation, in its classical per-cycle form.
    # -------------------------------------------------------------------------
    Metric(
        name="Response to selection",
        symbol="R",
        unit="trait units gained per cycle",
        typical="crop-, trait- and programme-specific",
        formula="breeders_equation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "R = h2 * S, where S is the selection differential. Formulated by "
            "Lush in the 1930s and still the equation every breeding programme "
            "is designed around. The modern form divides by generation interval "
            "to give gain per year, which is what is actually optimised."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Genetic gain per year. The quantity the whole field optimises.
    # -------------------------------------------------------------------------
    Metric(
        name="Genetic gain per year",
        symbol="dG/t",
        unit="per cent of the trait mean per year",
        typical="0.5 - 2.5 %/year in well-resourced programmes",
        formula="genetic_gain",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "dG/t = (i * r * sigma_A) / L. Molecular tools roughly doubled this "
            "in the crops where they were adopted, mostly by cutting L rather "
            "than by improving r. Realised gain in farmers' fields is usually "
            "lower than in trials, because varieties reach farms years after "
            "they are selected."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Prediction accuracy. The term genomic selection exists to raise, and the
    #  one that collapses outside the training population.
    # -------------------------------------------------------------------------
    Metric(
        name="Prediction accuracy",
        symbol="r_gy",
        unit="correlation between predicted and true breeding value",
        typical="0.3 - 0.7 within a training population, far lower outside it",
        formula="prediction_accuracy",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Depends on training population size, on marker density, on trait "
            "heritability and above all on relatedness between the training and "
            "prediction sets. An accuracy quoted without saying which "
            "cross-validation scheme produced it is not interpretable, and "
            "within-family accuracy is routinely reported as though it were "
            "across-population accuracy."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Selection intensity. Bounded above by how much seed and land exist.
    # -------------------------------------------------------------------------
    Metric(
        name="Selection intensity",
        symbol="i",
        unit="standard deviations of the selection differential",
        typical="1.0 to 2.7, corresponding to selecting 20 % down to 1 %",
        formula="selection_intensity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Rises with the fraction discarded, so a cheap early-stage screen "
            "that lets a programme evaluate ten times as many candidates raises "
            "i without any change to the genetics. It is bounded by seed "
            "availability and by the risk of losing diversity."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Generation interval. The denominator, and where molecular breeding won.
    # -------------------------------------------------------------------------
    Metric(
        name="Generation interval",
        symbol="L",
        unit="years per breeding cycle",
        typical="0.2 years under speed breeding to 10 years in tree crops",
        formula="generation_interval",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The denominator of genetic gain per year, and the term molecular "
            "breeding has moved furthest. It is why a breeder will accept lower "
            "prediction accuracy for a shorter cycle: halving L beats a modest "
            "loss in r."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Linkage disequilibrium. Determines how many markers are needed at all.
    # -------------------------------------------------------------------------
    Metric(
        name="Linkage disequilibrium decay distance",
        symbol="r2_LD",
        unit="kilobases at which r-squared falls below 0.2",
        typical="1 kb in outcrossing maize to over 100 kb in selfing wheat",
        formula="linkage_disequilibrium",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Slow decay means fewer markers capture the genome, which is why "
            "self-pollinating crops need far smaller marker panels than "
            "outcrossing ones. It sets the cost floor for genotyping in a given "
            "species."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Recurrent parent recovery. What marker-assisted backcrossing buys.
    # -------------------------------------------------------------------------
    Metric(
        name="Recurrent parent genome recovery",
        symbol="RPG",
        unit="per cent of the genome matching the recurrent parent",
        typical="99 % in three backcrosses with markers, six without",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Selecting against the donor genome away from the target locus "
            "halves the number of backcross generations. Linkage drag around "
            "the introgressed locus itself is the part markers help with least, "
            "because recombination there is rare by definition."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  hardy_weinberg and mendelian_segregation underlie the population genetics
#  every figure above rests on, and effective_population_size is how a
#  programme checks it is not narrowing its own base.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "heritability",
    "breeders_equation",
    "genetic_gain",
    "selection_intensity",
    "prediction_accuracy",
    "generation_interval",
    "linkage_disequilibrium",
    "hardy_weinberg",
    "mendelian_segregation",
    "effective_population_size",
)
