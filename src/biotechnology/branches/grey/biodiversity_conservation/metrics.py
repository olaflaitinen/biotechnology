# =============================================================================
#  biotechnology.branches.grey.biodiversity_conservation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS NOT HOW MANY ANIMALS THERE ARE. IT IS HOW MANY OF THEM
#  ARE GENETICALLY CONTRIBUTING, WHICH IS ALWAYS A SMALLER NUMBER AND IS OFTEN
#  VERY MUCH SMALLER.
#
#  A population of a thousand animals in which a few males father most of the
#  offspring behaves genetically like a population of a few dozen. The census
#  number is what gets reported, and the effective size is what determines how
#  fast variation is lost and how soon inbreeding depression appears. Placing
#  the census figure first would reproduce the error the field spent decades
#  correcting.
#
#      COUNT WHAT IS BREEDING, NOT WHAT IS ALIVE.
#
#  THE SECOND ORGANISING IDEA IS THAT THIS FACET CONTAINS A METRIC FOR THE
#  DECISION ITSELF. Genetic rescue trades inbreeding depression against
#  outbreeding depression, and there is no formula that settles it. The
#  genetic distance between the donor and recipient populations is what the
#  judgement is made on, and it is recorded here as a metric so that the
#  decision is visible as a judgement rather than hidden inside a
#  recommendation.
#
#  A THIRD POINT. Two entries measure institutions rather than organisms:
#  biobank coverage and continuity. They belong here because the commonest way
#  banked material is lost is a funding decision, not a freezer failure, and a
#  facet that measured only biology would miss the actual risk.
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
    #  HOW MANY ARE ACTUALLY CONTRIBUTING
    # =========================================================================
    Metric(
        name="Effective population size",
        symbol="Ne",
        unit="individuals",
        formula="effective_population_size",
        typical="a fraction of the census count, and frequently a small "
        "fraction",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Placed first because it is what governs the loss of variation and "
            "the onset of inbreeding depression, and because the census count "
            "is what gets reported. Unequal breeding success, skewed sex "
            "ratios and fluctuating numbers all push it down, so a population "
            "that looks secure by headcount can be failing genetically. "
            "Conservation genetics is largely the practice of taking this "
            "number seriously."
        ),
    ),
    Metric(
        name="Census population size",
        symbol="N_c",
        unit="individuals",
        typical="the number reported publicly and in status assessments",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Recorded second and deliberately so. It is what a survey counts, "
            "what a listing decision uses and what the public hears, and on its "
            "own it says nothing about whether the population can persist. The "
            "ratio between this and the entry above is one of the more useful "
            "single diagnostics in the field."
        ),
    ),
    # =========================================================================
    #  HOW MUCH VARIATION IS LEFT, AND HOW FAST IT IS GOING
    # =========================================================================
    Metric(
        name="Genetic diversity",
        symbol="H_e",
        unit="expected heterozygosity, from zero to one",
        typical="lower in small, isolated and recently bottlenecked "
        "populations",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The standing variation a population has to respond to disease, "
            "climate and any other change. It is meaningful in comparison "
            "rather than in absolute terms, which is why museum specimen "
            "sequencing matters: it supplies the value from before the decline "
            "and turns a number into a trend."
        ),
    ),
    Metric(
        name="Inbreeding coefficient",
        symbol="F",
        unit="probability that two alleles at a locus are identical by descent",
        typical="rises steadily in small closed populations",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Now measured directly from genomic data through runs of "
            "homozygosity rather than inferred from a pedigree, which matters "
            "because pedigrees are incomplete, assume unrelated founders, and "
            "are wrong more often than they are known to be wrong."
        ),
    ),
    Metric(
        name="Genetic load",
        symbol="L_gen",
        unit="burden of deleterious variants carried by the population",
        typical="expressed as inbreeding depression when homozygosity rises",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The mechanism connecting the two entries above to actual harm. "
            "Deleterious recessive variants are harmless while rare and are "
            "exposed when relatives breed. A subtlety that changes management: "
            "a population that has been small for a very long time may have "
            "purged part of its load, so recent bottlenecks are more dangerous "
            "than ancient ones at the same inbreeding coefficient."
        ),
    ),
    Metric(
        name="Inbreeding depression",
        symbol="delta_fit",
        unit="reduction in survival, fertility or fecundity per unit increase "
        "in inbreeding",
        typical="measurable in survival and reproductive output before it is "
        "visible in population trend",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The observable consequence, and what genetic rescue is intended to "
            "reverse. It is the endpoint that matters, since a change in "
            "heterozygosity with no change in fitness would be an academic "
            "result rather than a conservation one."
        ),
    ),
    # =========================================================================
    #  THE DECISION, RECORDED AS A METRIC SO IT STAYS VISIBLE
    # =========================================================================
    Metric(
        name="Genetic distance between donor and recipient populations",
        symbol="F_ST",
        unit="proportion of variation attributable to differences between "
        "populations",
        typical="low values favour rescue, high values raise outbreeding risk",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The number a genetic rescue decision is argued over, and it does "
            "not settle the argument. A low value suggests the populations were "
            "recently connected and a cross is safe; a high one suggests local "
            "adaptation that mixing would destroy. Between those lies a range "
            "in which the risk of intervening and the risk of doing nothing are "
            "both real, and choosing is a judgement about which population is "
            "worth preserving."
        ),
    ),
    Metric(
        name="Gene flow and migration rate",
        symbol="Nm",
        unit="effective migrants exchanged per generation",
        typical="a small number per generation is sufficient to prevent "
        "divergence",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How connected populations are, and therefore whether a corridor "
            "would help or a translocation is required. It is a strikingly "
            "small number: very few effective migrants per generation prevent "
            "populations drifting apart, which is why fragmentation causes "
            "genetic harm long before it causes visible isolation."
        ),
    ),
    # =========================================================================
    #  MEASURING THE INSTITUTIONS, WHICH IS WHERE MATERIAL IS ACTUALLY LOST
    # =========================================================================
    Metric(
        name="Biobank taxonomic coverage",
        symbol="f_bank",
        unit="per cent of threatened species with preserved viable material",
        typical="low, and concentrated in large vertebrates",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Included because banking is the one intervention in this record "
            "that cannot be performed later. The gap between what is threatened "
            "and what is preserved is therefore a measure of options closing "
            "permanently, and it is closing fastest for the taxa nobody is "
            "collecting."
        ),
    ),
    Metric(
        name="Biobank continuity risk",
        symbol="R_cont",
        unit="qualitative, indexed by funding horizon, redundancy and "
        "distributed duplication",
        typical="funding horizons of years against a preservation requirement "
        "of centuries",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "A metric about institutions rather than organisms, and it belongs "
            "here because the commonest way banked material is lost is a budget "
            "decision rather than a freezer failure. Duplicate storage at a "
            "separate institution is the mitigation, and it costs money that "
            "the same budget decision removes."
        ),
    ),
    Metric(
        name="Post-thaw viability",
        symbol="v_thaw",
        unit="per cent of cells or gametes viable after cryopreservation and "
        "thawing",
        typical="species-specific, and unmeasured for most taxa because no "
        "protocol exists",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Whether the banked material will be usable, which is not the same "
            "question as whether it was stored. Protocols must be developed "
            "species by species, and a bank holding material for which no "
            "viable protocol exists holds a sample rather than an option."
        ),
    ),
    # =========================================================================
    #  DID THE INTERVENTION WORK
    # =========================================================================
    Metric(
        name="Population growth rate after intervention",
        symbol="lambda",
        unit="ratio of population size between successive generations",
        typical="the endpoint by which genetic rescue is judged",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The outcome that matters. A rescue that raises heterozygosity and "
            "leaves the population declining has not worked, and the documented "
            "successes in this field are documented precisely because this "
            "number moved and stayed moved for more than one generation."
        ),
    ),
    Metric(
        name="Assisted reproduction success rate",
        symbol="p_ART",
        unit="per cent of procedures resulting in a live birth",
        typical="low, and available for a small number of species",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Recorded honestly. Artificial insemination is routine in a few "
            "well-studied species and unavailable in most because the "
            "reproductive biology is unknown. Cloning and interspecies "
            "surrogacy have produced live animals in a handful of cases at low "
            "rates, which makes them demonstrations rather than tools."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Population genetics, with the drift and inbreeding relationships first.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "effective_population_size",
    "hardy_weinberg_equilibrium",
    "inbreeding_coefficient",
    "fixation_index",
    "wright_fisher_drift",
    "population_growth_rate",
)
