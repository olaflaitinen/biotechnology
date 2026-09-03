# =============================================================================
#  biotechnology.branches.white.metabolic_engineering.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This field has a standard trio that everyone quotes, TITRE, RATE AND YIELD,
#  usually abbreviated TRY. They are listed first because a strain is reported
#  in those terms in every paper and every investor deck.
#
#  THE POINT OF THIS FACET IS THAT THE TRIO IS INCOMPLETE. Three things it
#  omits routinely decide whether a strain becomes a process:
#
#      the ceiling      yield means little without the stoichiometric maximum
#                       it is measured against. Eighty per cent of theoretical
#                       is remarkable; 0.2 g/g is uninterpretable alone.
#      the stability    a strain that loses productivity over a hundred
#                       generations does not survive a production fermentation,
#                       and TRY is measured long before that matters.
#      the control      the flux control coefficient, which tells an engineer
#                       WHERE to intervene and is the formal refutation of the
#                       rate-limiting step assumption.
#
#  So the order here is: the trio, then the ceiling that interprets it, then
#  the two things the trio hides.
#
#  A NOTE ON UNITS. Yield is given in Cmol/Cmol as well as g/g because carbon
#  yield is the form in which a stoichiometric limit is meaningful: it asks
#  what fraction of the carbon fed in leaves as product rather than as carbon
#  dioxide or biomass.
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
    #  THE TRIO EVERYONE QUOTES
    # =========================================================================
    Metric(
        name="Product titre",
        symbol="C_p",
        unit="grams of product per litre of broth",
        typical="1 - 200 g/L, with roughly 50 g/L a common commercial threshold "
        "for a bulk product",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Sets the cost of separating the product from the broth, which for "
            "a low-value product frequently exceeds the cost of making it. A "
            "dilute product in a large volume of water is a downstream problem "
            "rather than a fermentation achievement."
        ),
    ),
    Metric(
        name="Volumetric productivity",
        symbol="Q_p",
        unit="grams of product per litre per hour",
        typical="0.5 - 5 g/L/h",
        formula="space_time_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How hard the vessel works, and therefore how much capital a given "
            "annual output requires. It is the metric that punishes a strain "
            "which reaches a high titre only after two hundred hours."
        ),
    ),
    Metric(
        name="Product yield on substrate",
        symbol="Y_ps",
        unit="grams of product per gram of substrate, or Cmol/Cmol",
        typical="0.1 - 0.5 g/g depending on the product",
        formula="product_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Usually the dominant term in the cost of goods for a bulk "
            "product, because feedstock is the largest single input. Reported "
            "alone it is close to meaningless: it must be read against the "
            "stoichiometric maximum in the next entry, since 0.3 g/g may be "
            "either excellent or poor depending on the product."
        ),
    ),
    # =========================================================================
    #  THE CEILING THAT MAKES YIELD INTERPRETABLE
    # =========================================================================
    Metric(
        name="Fraction of theoretical maximum yield",
        symbol="Y_frac",
        unit="per cent of the stoichiometric maximum",
        typical="40 - 90 %, with above 90 % rare and usually growth-coupled",
        formula="theoretical_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The honest way to report a strain. The maximum follows from "
            "carbon, redox and energy balances and cannot be exceeded by any "
            "engineering whatsoever, so this fraction says how much room is "
            "actually left. A field that reported only g/g would keep "
            "celebrating improvements that are approaching a wall."
        ),
    ),
    Metric(
        name="Carbon balance closure",
        symbol="C_bal",
        unit="per cent of input carbon accounted for in products",
        typical="95 - 105 % for a trustworthy dataset",
        formula="mass_balance",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A data quality check rather than a performance figure, and it is "
            "included because it is the fastest way to detect that a reported "
            "result is wrong. Carbon that does not appear as product, biomass "
            "or carbon dioxide went somewhere, and the usual answer is an "
            "unmeasured by-product."
        ),
    ),
    # =========================================================================
    #  WHAT THE TRIO HIDES: THE STRAIN DEGRADES
    # =========================================================================
    Metric(
        name="Genetic stability over generations",
        symbol="G_stab",
        unit="generations of retained productivity",
        typical="60 - 100 generations required for a large-scale process",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The metric most often absent from a publication and most often "
            "decisive in a plant. Producing something the cell does not need is "
            "a fitness cost, so any mutant that stops producing outgrows the "
            "engineered strain, and a seed train plus a production fermentation "
            "spans enough generations for that to matter. This is why "
            "growth-coupled designs, which make production necessary for "
            "growth, are valued out of proportion to their titres."
        ),
    ),
    Metric(
        name="Specific productivity",
        symbol="q_p",
        unit="grams of product per gram of dry cell weight per hour",
        typical="0.01 - 0.5 g/gDCW/h",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Separates a strain that is genuinely more productive from one that "
            "simply grew to a higher cell density. Two processes with identical "
            "volumetric productivity can differ entirely in whether the "
            "improvement came from the pathway or from the fermentation."
        ),
    ),
    Metric(
        name="Specific growth rate",
        symbol="mu",
        unit="per hour",
        typical="0.05 - 0.7 h^-1 depending on organism and phase",
        formula="monod_equation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Included because it is the quantity the engineered strain is in "
            "competition with. Growth and production draw on the same carbon "
            "and the same cofactors, and the central design decision in this "
            "field is how far the two can be decoupled without the culture "
            "dying or reverting."
        ),
    ),
    # =========================================================================
    #  WHAT THE TRIO HIDES: WHERE TO INTERVENE
    # =========================================================================
    Metric(
        name="Flux control coefficient",
        symbol="C_J_i",
        unit="dimensionless, and the coefficients over a pathway sum to 1",
        typical="rarely above 0.3 for any single enzyme",
        formula="flux_control_coefficient",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The formal refutation of the rate-limiting step. Because the "
            "coefficients sum to one across the pathway, control is shared, and "
            "an enzyme with a coefficient of 0.2 will return only a fifth of "
            "any improvement made to it. This single summation theorem explains "
            "why overexpressing the apparent bottleneck so often does nothing."
        ),
    ),
    Metric(
        name="Intracellular flux distribution",
        symbol="v",
        unit="millimoles per gram dry cell weight per hour",
        formula="flux_balance_analysis",
        typical="reported as a map rather than a single number",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "What the cell is actually doing, as distinct from what the model "
            "predicted or the product titre implies. Measured with labelled "
            "carbon rather than inferred, and it is the measurement that "
            "usually reveals the unexpected branch consuming the carbon."
        ),
    ),
    # =========================================================================
    #  THE CONSTRAINT THE VESSEL IMPOSES
    # =========================================================================
    Metric(
        name="Oxygen uptake rate",
        symbol="OUR",
        unit="millimoles of oxygen per litre per hour",
        typical="50 - 250 mmol/L/h, and often the true ceiling at scale",
        formula="oxygen_transfer_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "For an aerobic process this is frequently what actually limits "
            "production in a large vessel, rather than anything about the "
            "strain. Oxygen transfer does not scale with volume, which is why a "
            "strain that performs beautifully in a shake flask can disappoint "
            "at cubic metre scale, and why this record links to "
            "`white.bioprocess_engineering` rather than treating scale-up as "
            "someone else's problem."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Ordered as the metrics are: performance, then the stoichiometric ceiling,
#  then growth and control, then the vessel constraint.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "product_yield",
    "space_time_yield",
    "theoretical_yield",
    "mass_balance",
    "degree_of_reduction",
    "monod_equation",
    "specific_growth_rate",
    "flux_balance_analysis",
    "flux_control_coefficient",
    "oxygen_transfer_rate",
)
