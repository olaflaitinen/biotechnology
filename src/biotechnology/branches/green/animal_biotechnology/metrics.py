# =============================================================================
#  biotechnology.branches.green.animal_biotechnology.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record shares its governing equation with
#  `green.molecular_plant_breeding`:
#
#      dG/t = (i * r * sigma_A) / L
#
#  Genetic gain per year equals selection intensity, times prediction accuracy,
#  times additive genetic standard deviation, divided by generation interval.
#  The mathematics is identical; the biology differs in two ways that change
#  everything about how the terms are moved.
#
#  FIRST, REPRODUCTIVE RATE IS ASYMMETRIC. One bull can sire tens of thousands
#  of calves; one cow produces a handful. Selection intensity on the male side
#  is therefore enormous and on the female side is nearly fixed, which is why
#  embryo technologies exist at all and why the male side dominates genetic
#  progress.
#
#  SECOND, THE DENOMINATOR WAS THE WHOLE PRIZE. Genomic selection did not
#  improve prediction accuracy over a progeny test; a progeny-tested bull is
#  measured more accurately than any genomic prediction. What it did was cut
#  the generation interval from about five years to about two, and because L
#  sits in the denominator, that nearly doubled annual gain while ACCEPTING
#  LOWER ACCURACY. That trade is the single most important thing to understand
#  about this record.
#
#  The last three metrics are not gain terms. They measure what the gain costs.
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
    #  The prediction itself.
    # -------------------------------------------------------------------------
    Metric(
        name="Genomic estimated breeding value",
        symbol="GEBV",
        unit="trait units, as a deviation from a defined base population",
        typical="expressed per trait, and combined into a selection index",
        formula="genomic_breeding_value",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Always a deviation from a base population, so a value is "
            "meaningful only against a stated base and year. Published values "
            "are routinely rebased, which makes historical figures look like "
            "they have changed when nothing about the animal has."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The denominator that genomic selection attacked. See the header note.
    # -------------------------------------------------------------------------
    Metric(
        name="Generation interval",
        symbol="L",
        unit="years, as the average age of parents when progeny are born",
        typical="1.5 - 2 years in genomic dairy schemes, against 5 or more "
        "under progeny testing",
        formula="generation_interval",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The term genomic selection actually moved. Halving it roughly "
            "doubles annual genetic gain, all else equal, and that gain was "
            "obtained while accepting LOWER prediction accuracy than a progeny "
            "test provides. The trade is deliberate and is the core of the "
            "record."
        ),
    ),
    # -------------------------------------------------------------------------
    #  What the whole system optimises.
    # -------------------------------------------------------------------------
    Metric(
        name="Genetic gain per year",
        symbol="dG/t",
        unit="genetic standard deviations or trait units per year",
        typical="roughly doubled in dairy cattle after 2009",
        formula="genetic_gain",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Realised gain in commercial herds lags the gain in the breeding "
            "population, because it takes years for the improved genetics to "
            "reach farms and be expressed under commercial management."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Prediction accuracy. Lower than a progeny test, and that is the point.
    # -------------------------------------------------------------------------
    Metric(
        name="Reliability of genomic prediction",
        symbol="r2",
        unit="squared correlation with true breeding value, dimensionless",
        typical="0.4 - 0.75 for a genomic young bull, above 0.9 for a "
        "progeny-tested one",
        formula="prediction_accuracy",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Reported as reliability rather than accuracy in livestock "
            "evaluation, which is the square of the correlation and therefore a "
            "smaller-looking number for the same prediction. Depends heavily on "
            "reference population size and on relatedness, which is why "
            "numerically small breeds and low-recording regions benefit least."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Selection intensity, and the asymmetry that defines this record.
    # -------------------------------------------------------------------------
    Metric(
        name="Selection intensity",
        symbol="i",
        unit="standard deviations of the selection differential",
        typical="above 2.5 on the sire side, near 0.5 on the dam side",
        formula="selection_intensity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The asymmetry is the whole reason embryo technologies exist. One "
            "bull can sire tens of thousands of calves, so a very small "
            "fraction of males is used; one cow produces a handful of calves in "
            "a lifetime, so almost all females must be kept. Male-side "
            "selection therefore contributes most of the genetic progress."
        ),
    ),
    # -------------------------------------------------------------------------
    #  What the gain costs, part one.
    # -------------------------------------------------------------------------
    Metric(
        name="Rate of inbreeding per generation",
        symbol="dF",
        unit="proportional increase in inbreeding coefficient",
        typical="below 0.01 recommended; observed rates have exceeded it in "
        "some breeds",
        formula="inbreeding_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The conventional ceiling of one per cent per generation comes from "
            "conservation genetics. Genomic selection can raise dF, because "
            "selecting on markers concentrates on the same favourable "
            "haplotypes, but it also provides the relationship information "
            "needed to constrain it. Which of those happens is a breeding "
            "programme design decision, not a property of the technology."
        ),
    ),
    # -------------------------------------------------------------------------
    #  What the gain costs, part two.
    # -------------------------------------------------------------------------
    Metric(
        name="Effective population size",
        symbol="Ne",
        unit="idealised breeding individuals",
        typical="50 - 150 in major commercial dairy breeds",
        formula="effective_population_size",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A conservation biologist regards an Ne below 50 as immediately "
            "concerning and below 500 as unsustainable in the long term. Major "
            "dairy breeds with millions of animals sit in that range because "
            "so few sires contribute, which is the quantitative form of the "
            "diversity challenge in `practice.py`."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The reproductive efficiency the first layer depends on.
    # -------------------------------------------------------------------------
    Metric(
        name="Conception rate per insemination",
        symbol="CR",
        unit="per cent of inseminations resulting in a pregnancy",
        typical="30 - 60 %, and lower with sexed semen",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Declined for decades in high-producing dairy cattle as an "
            "unfavourable correlated response to selection on milk yield, and "
            "has recovered since fertility traits were deliberately added to "
            "the breeding goal. One of the clearest demonstrations that a "
            "breeding index is a choice rather than a measurement."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The third layer's efficiency, stated plainly.
    # -------------------------------------------------------------------------
    Metric(
        name="Cloning efficiency",
        symbol="E_scnt",
        unit="per cent of reconstructed embryos yielding a live healthy birth",
        typical="1 - 10 %",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Low, and the losses include late gestation failures, large "
            "offspring syndrome and placental abnormality. The figure is "
            "reported here without comment on whether the practice is "
            "acceptable, because that judgement belongs in "
            "`purple.bioethics` and not in a metric note."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  heritability and breeders_equation are included because every figure above
#  rests on them, and hardy_weinberg because allele frequency tracking is how
#  a breed's diversity is actually monitored.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "genomic_breeding_value",
    "generation_interval",
    "genetic_gain",
    "prediction_accuracy",
    "selection_intensity",
    "inbreeding_rate",
    "effective_population_size",
    "heritability",
    "breeders_equation",
    "hardy_weinberg",
)
