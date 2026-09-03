# =============================================================================
#  biotechnology.branches.white.microbial_fermentation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `white.metabolic_engineering` measures THE STRAIN. This record measures THE
#  CULTIVATION, and the difference shows up most clearly in what leads the
#  list: oxygen transfer, not titre.
#
#  THE ORDERING IS THE ARGUMENT. In a large aerobic process the ceiling is
#  usually set by the vessel rather than by the biology, so the transfer terms
#  come first. Then the kinetic constants that decide how the culture must be
#  fed. Then the yields. Then the two operational numbers that a plant manager
#  cares about more than any of them: how often a batch is lost, and how much
#  of the cycle is spent not fermenting.
#
#  A NOTE ON WHY kLa IS THE FIRST ENTRY. Oxygen is only sparingly soluble in
#  water, a dense culture consumes it within seconds, and the transfer
#  coefficient falls as vessels get larger because the ratio of surface and
#  power input to volume falls. This single quantity is why a strain that
#  performs in a shake flask can disappoint at cubic metre scale, and it is
#  the most common reason a scale-up fails for reasons unrelated to biology.
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
    #  THE VESSEL, NOT THE ORGANISM, IS USUALLY THE LIMIT
    # =========================================================================
    Metric(
        name="Volumetric oxygen transfer coefficient",
        symbol="kLa",
        unit="per hour",
        typical="50 - 500 h^-1 in stirred tanks, falling as scale increases",
        formula="oxygen_transfer_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The most important number in aerobic fermentation and the reason "
            "this facet begins here. Oxygen dissolves poorly, a dense culture "
            "consumes the dissolved inventory within seconds, and transfer "
            "does not improve with vessel size because power input and "
            "interfacial area per unit volume both fall. Matching kLa to the "
            "organism's demand is the central design constraint of scale-up."
        ),
    ),
    Metric(
        name="Oxygen uptake rate",
        symbol="OUR",
        unit="millimoles of oxygen per litre per hour",
        typical="50 - 250 mmol/L/h",
        formula="oxygen_transfer_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "What the culture demands, against what the vessel can supply. "
            "Measured continuously from off-gas without disturbing the "
            "culture, which makes it the practical window into a running "
            "fermentation and the usual basis for feedback control of the feed."
        ),
    ),
    Metric(
        name="Respiratory quotient",
        symbol="RQ",
        unit="moles carbon dioxide evolved per mole oxygen consumed",
        typical="near 1.0 for fully oxidative growth on glucose; a rise "
        "signals overflow or fermentative metabolism",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "An early warning rather than a performance figure. A rising RQ "
            "says the culture has crossed into overflow metabolism before any "
            "by-product assay could report it, which is why RQ is a common "
            "control handle for fed-batch feed rate. It is also one of the few "
            "measurements that costs nothing and interrupts nothing."
        ),
    ),
    Metric(
        name="Dissolved oxygen tension",
        symbol="DOT",
        unit="per cent of air saturation",
        typical="held above 20 - 30 % for most aerobic processes",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The controlled variable rather than the interesting one. What "
            "matters is that it is maintained, not its value: a culture at ten "
            "per cent that never drops is healthier than one oscillating "
            "through zero, and large vessels have gradients that a single "
            "probe does not see."
        ),
    ),
    # =========================================================================
    #  HOW THE CULTURE MUST BE FED
    # =========================================================================
    Metric(
        name="Maximum specific growth rate",
        symbol="mu_max",
        unit="per hour",
        typical="0.1 - 1.0 h^-1 depending on organism and medium",
        formula="monod_equation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Sets the shortest possible seed train and the fastest a "
            "contaminant would have to grow to displace the culture. It is "
            "rarely the rate at which a production fermentation is actually "
            "run, because growing at mu_max usually means overflowing."
        ),
    ),
    Metric(
        name="Critical specific growth rate",
        symbol="mu_crit",
        unit="per hour",
        typical="0.1 - 0.3 h^-1, well below mu_max",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The threshold above which the organism begins excreting acetate "
            "or ethanol rather than converting carbon usefully. Nearly every "
            "industrial fed-batch feeding strategy exists to hold the culture "
            "below this number, which is the operational statement of the fact "
            "that feeding faster produces less."
        ),
    ),
    Metric(
        name="Substrate saturation constant",
        symbol="K_s",
        unit="grams per litre",
        typical="0.001 - 0.5 g/L, often far below the analytical detection "
        "limit",
        formula="monod_equation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Usually so small that the culture grows at nearly maximum rate "
            "until the substrate is essentially gone, which is why the "
            "transition at the end of a batch is abrupt rather than gradual. "
            "Its smallness is also why K_s is difficult to measure and is "
            "often quoted with more confidence than it deserves."
        ),
    ),
    # =========================================================================
    #  WHAT THE FEEDSTOCK BUYS
    # =========================================================================
    Metric(
        name="Biomass yield on substrate",
        symbol="Y_xs",
        unit="grams dry cell weight per gram of substrate",
        typical="0.3 - 0.5 g/g on glucose for aerobic growth",
        formula="product_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Carbon spent on cells rather than on product. For a growth-linked "
            "product this is necessary investment; for a product made in a "
            "separate phase it is overhead, and the two-phase strategies in "
            "`practice.TECHNOLOGIES` exist to control the split."
        ),
    ),
    Metric(
        name="Maintenance coefficient",
        symbol="m_s",
        unit="grams of substrate per gram dry cell weight per hour",
        typical="0.02 - 0.1 g/gDCW/h",
        formula="pirt_equation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "What the cells consume merely to stay alive, before growing or "
            "producing anything. It is why extending a fermentation has "
            "diminishing and eventually negative returns: a dense, slow-growing "
            "culture can consume feed and deliver almost nothing."
        ),
    ),
    Metric(
        name="Dilution rate in continuous culture",
        symbol="D",
        unit="per hour",
        typical="set below mu_max; washout occurs when D exceeds it",
        formula="chemostat_dilution_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "In a chemostat the operator sets the growth rate by setting the "
            "flow, which is an elegant result and the reason continuous culture "
            "is the standard tool of physiology research. Its rarity in "
            "manufacturing, despite better productivity per unit of capital, is "
            "discussed in `governance.py` and `history.py`."
        ),
    ),
    # =========================================================================
    #  WHAT A PLANT MANAGER ACTUALLY WATCHES
    # =========================================================================
    Metric(
        name="Batch contamination rate",
        symbol="R_cont",
        unit="per cent of batches lost to contamination",
        typical="below 1 - 2 % for a well-run sterile plant",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The metric that most directly reflects plant discipline, and the "
            "one least often published. A lost batch costs the medium, the "
            "energy, the labour and the vessel time, and in a capacity-limited "
            "plant the vessel time is the largest of those."
        ),
    ),
    Metric(
        name="Sterilisation lethality",
        symbol="F0",
        unit="equivalent minutes at 121 degrees Celsius",
        typical="15 - 20 min equivalent for medium and vessel sterilisation",
        formula="thermal_death_kinetics",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Sterility is achieved to a probability rather than absolutely, and "
            "this integrates time and temperature into the delivered lethality. "
            "The trade is real: more heat gives more assurance and destroys "
            "more of the nutrients, which is precisely why continuous "
            "high-temperature short-time sterilisation exists."
        ),
    ),
    Metric(
        name="Turnaround time",
        symbol="t_turn",
        unit="hours between the end of one batch and the start of the next",
        typical="8 - 48 h",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Cleaning, sterilising, testing and refilling are not fermentation, "
            "and they occupy the asset. Annual output depends on the whole "
            "cycle, so a process with a shorter run and a fast turnaround can "
            "beat a higher-titre process that ties the vessel up for a "
            "fortnight."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Ordered as the metrics are: transfer, kinetics, yields, sterility.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "oxygen_transfer_rate",
    "monod_equation",
    "specific_growth_rate",
    "pirt_equation",
    "product_yield",
    "space_time_yield",
    "chemostat_dilution_rate",
    "thermal_death_kinetics",
    "mass_balance",
)
