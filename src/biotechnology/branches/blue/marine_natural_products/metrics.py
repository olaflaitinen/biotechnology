# =============================================================================
#  biotechnology.branches.blue.marine_natural_products.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IN THIS FACET IS THE ONE THE FIELD IS ACTUALLY ABOUT, and
#  it is not a measure of potency.
#
#  Yield from source biomass, expressed as grams of compound per tonne of
#  animal, decides whether a molecule can ever become a medicine. Values in the
#  region of a gram per tonne are ordinary for this field, and a compound at
#  that yield requires a supply route other than collection before anything
#  else about it matters. Placing potency first, as a pharmacology facet
#  normally would, would misdescribe the discipline.
#
#  A NOTE ON POTENCY MEASURES. IC50 and Ki appear below and both are highly
#  assay-dependent: cell line, incubation time, serum concentration and readout
#  all move the number, sometimes by an order of magnitude. Comparisons across
#  publications are unreliable unless the assay is the same, and this facet
#  says so in the notes rather than presenting the figures as properties of the
#  molecules.
#
#  A NOTE ON THE REDISCOVERY RATE. It is included because it measures the
#  efficiency of the field rather than the quality of any compound, and because
#  it is the metric that justifies dereplication existing as a discipline.
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
    #  THE METRIC THAT DECIDES EVERYTHING
    # =========================================================================
    Metric(
        name="Yield from source biomass",
        symbol="Y_bio",
        unit="grams of purified compound per tonne of wet organism",
        typical="commonly around 1 g per tonne, and lower for several "
        "well-known compounds",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The number that determines whether a molecule can become a "
            "medicine, and the reason it is placed first. At a gram per tonne, "
            "a single clinical trial's requirement corresponds to a quantity of "
            "animal that cannot be collected sustainably or at all. A compound "
            "at this yield needs a synthetic, semisynthetic or fermentative "
            "route before any of its pharmacology matters."
        ),
    ),
    Metric(
        name="Biomass required for a clinical supply",
        symbol="M_req",
        unit="tonnes of wet organism per kilogram of compound",
        typical="hundreds to thousands of tonnes per kilogram at typical yields",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The same quantity inverted, and stated because the inversion is "
            "what makes the constraint intuitive. It converts an abstract "
            "concentration into a barge of animals, and it is the calculation "
            "that ended several programmes before any pharmacology was "
            "questioned."
        ),
    ),
    # =========================================================================
    #  HOW HARD IT IS TO MAKE INSTEAD
    # =========================================================================
    Metric(
        name="Total synthesis step count",
        symbol="n_steps",
        unit="linear steps in the longest sequence",
        typical="20 - 60 linear steps for a complex marine macrolide",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The linear count matters more than the total, because yield "
            "compounds along the longest sequence. It is the practical test of "
            "whether total synthesis is a supply route or an academic "
            "demonstration, and for many marine targets it is the latter."
        ),
    ),
    Metric(
        name="Overall synthetic yield",
        symbol="Y_syn",
        unit="per cent from starting material to final compound",
        typical="frequently below 1 % over a long linear sequence",
        formula="overall_step_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Multiplicative across steps, in exactly the way "
            "`white.bioprocess_engineering` records for purification trains. "
            "Thirty steps at ninety per cent each give roughly four per cent "
            "overall, which is why step count and yield must be read together "
            "and why analogue simplification is so often the winning strategy."
        ),
    ),
    Metric(
        name="Number of stereocentres",
        symbol="n_stereo",
        unit="count",
        typical="often more than ten in a marine macrolide or polyketide",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A structural proxy for synthetic difficulty. Each centre must be "
            "set correctly and the number of possible stereoisomers rises as a "
            "power of two, so a molecule with twelve centres has thousands of "
            "wrong answers and one right one."
        ),
    ),
    # =========================================================================
    #  WHETHER THE MOLECULE IS WORTH THE TROUBLE
    # =========================================================================
    Metric(
        name="Half maximal inhibitory concentration",
        symbol="IC50",
        unit="nanomolar",
        typical="sub-nanomolar to nanomolar for the cytotoxins that reach "
        "development",
        formula="dose_response",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Highly assay-dependent. Cell line, incubation time, serum "
            "concentration and readout each shift it, sometimes by an order of "
            "magnitude, so figures from different publications are not "
            "comparable unless the assay is. Extreme potency here is not "
            "incidental: it is the property the branch header predicts, since "
            "chemistry released into seawater must work at low concentration to "
            "work at all."
        ),
    ),
    Metric(
        name="Binding affinity",
        symbol="K_i",
        unit="nanomolar",
        typical="picomolar to nanomolar for the venom peptides",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Reported for the channel-blocking peptides where the mechanism is "
            "a defined molecular target rather than general cytotoxicity. Cone "
            "snail peptides are valued as much for selectivity between closely "
            "related channel subtypes as for raw affinity, and selectivity is "
            "the harder property."
        ),
    ),
    Metric(
        name="Therapeutic index",
        symbol="TI",
        unit="ratio of toxic to effective dose, dimensionless",
        typical="narrow for the marine cytotoxins in clinical use",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The reason several marine compounds are delivered as antibody drug "
            "conjugate payloads rather than as free drugs. A molecule too toxic "
            "to give systemically becomes usable when an antibody restricts "
            "where it goes, which converts a poor therapeutic index into an "
            "engineering problem."
        ),
    ),
    # =========================================================================
    #  HOW EFFICIENTLY THE FIELD SEARCHES
    # =========================================================================
    Metric(
        name="Rediscovery rate",
        symbol="f_redis",
        unit="per cent of isolated compounds already described",
        typical="high, and the principal argument for systematic "
        "dereplication",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Measures the efficiency of the field rather than the quality of "
            "any compound. Isolating a known molecule consumes the same months "
            "as isolating a new one, which is why dereplication against "
            "databases early in the workflow is worth more than any "
            "improvement in separation."
        ),
    ),
    Metric(
        name="Hit rate from marine extracts",
        symbol="f_hit",
        unit="per cent of extracts showing activity in a primary screen",
        typical="reported as higher than for terrestrial extract libraries",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Graded REPORTED rather than higher because the comparison depends "
            "on the screen, the library and the threshold chosen. The claimed "
            "advantage is consistent with the branch header's argument about "
            "dilution-driven potency, and consistency with a plausible "
            "mechanism is not the same as demonstration."
        ),
    ),
    Metric(
        name="Silent biosynthetic gene clusters",
        symbol="f_silent",
        unit="per cent of predicted clusters with no product observed under "
        "laboratory conditions",
        typical="the large majority",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The gap between what a genome can encode and what an organism "
            "actually makes. It is the reason genome mining has not simply "
            "replaced extraction: a predicted cluster is a hypothesis about "
            "chemistry, and most hypotheses remain untested because nothing "
            "known will switch the cluster on."
        ),
    ),
    Metric(
        name="Halogen incorporation",
        symbol="f_halo",
        unit="per cent of marine natural products containing halogen",
        typical="substantially higher than in terrestrial natural products",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A structural signature of the environment rather than a "
            "performance measure. Seawater supplies bromine and chlorine "
            "abundantly and marine enzymes use them, which places marine "
            "chemistry in regions of chemical space that plant and soil "
            "chemistry rarely reach. It is one concrete reason novelty is high."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Supply and synthesis first, matching the facet's emphasis, then the
#  pharmacology.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "overall_step_yield",
    "dose_response",
    "hill_equation",
    "therapeutic_index",
    "mass_balance",
    "atom_economy",
)
