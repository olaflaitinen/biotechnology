# =============================================================================
#  biotechnology.branches.white.biofuels.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This facet is deliberately ordered so that the metrics which DECIDE whether
#  a fuel is worth making come before the metrics that describe how well the
#  fermentation ran. In no other record in this library is that inversion so
#  important, because a biofuel process can be excellent by every fermentation
#  measure and still consume more energy than it delivers.
#
#  TWO WARNINGS BELONG WITH THIS FACET RATHER THAN INSIDE ANY ONE ENTRY.
#
#  FIRST, ENERGY RETURN AND CARBON INTENSITY ARE MODEL OUTPUTS, NOT
#  MEASUREMENTS. Both depend on system boundary, on how co-products are
#  credited, and on which land use change model is applied. Published figures
#  for the same fuel differ by more than a factor of two for exactly these
#  reasons, and a reader who compares two numbers from two studies is usually
#  comparing two sets of assumptions. The metrics below record the disputed
#  ranges rather than picking a preferred value.
#
#  SECOND, THE 0.51 CEILING IS NOT A MODEL. It follows from the stoichiometry
#  of glucose to ethanol and carbon dioxide, and no organism, enzyme or process
#  improvement can exceed it. It is the one hard number in a record otherwise
#  full of contested ones, which is why it appears among the first entries.
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
    #  WHETHER IT IS WORTH MAKING AT ALL
    # =========================================================================
    Metric(
        name="Energy return on investment",
        symbol="EROI",
        unit="megajoules of fuel delivered per megajoule consumed, "
        "dimensionless",
        typical="around 8 - 10 for sugarcane ethanol; roughly 1.2 - 1.6 for "
        "maize ethanol, and disputed",
        formula="energy_return_on_investment",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The first question to ask of any fuel and the source of the "
            "field's longest argument. A value near one means almost all the "
            "energy delivered was spent producing it. The sugarcane and maize "
            "figures differ by nearly an order of magnitude, which is why "
            "treating biofuels as a single category is the most common error "
            "in discussing them. Marked REPORTED rather than CONSENSUS because "
            "the maize figure genuinely is contested by careful people."
        ),
    ),
    Metric(
        name="Life cycle greenhouse gas intensity",
        symbol="CI",
        unit="grams of carbon dioxide equivalent per megajoule",
        typical="roughly 90 for fossil petrol; 15 - 80 for biofuels depending "
        "on feedstock and on the land use change assumption",
        formula="carbon_intensity",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The number that determines whether a fuel counts towards a "
            "renewable target and therefore whether it can be sold at a "
            "premium. It is a model output: the same physical fuel can be "
            "assigned very different intensities depending on system boundary, "
            "co-product allocation and land use change treatment. Regulators "
            "resolve this by prescribing a methodology, which makes the "
            "resulting number a legal fact rather than a physical one."
        ),
    ),
    Metric(
        name="Indirect land use change penalty",
        symbol="ILUC",
        unit="grams of carbon dioxide equivalent per megajoule added",
        typical="near zero for wastes and residues; substantial and disputed "
        "for crop-based fuels, largest for those displacing oilseed",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The emissions caused when displaced food production converts land "
            "somewhere else. It is real in principle, difficult to observe "
            "directly, estimated by economic modelling, and large enough in "
            "some estimates to reverse a fuel's apparent benefit entirely. It "
            "is the single most contested quantity in this record and is "
            "recorded as such rather than resolved."
        ),
    ),
    Metric(
        name="Fuel yield per hectare per year",
        symbol="Y_land",
        unit="litres of fuel per hectare per year",
        typical="roughly 6000 - 8000 L/ha for sugarcane ethanol; roughly 3500 - "
        "4500 for maize; roughly 1000 - 1500 for rapeseed biodiesel",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Converts the abstract land argument into a number. It is also the "
            "quantity that makes the scale problem concrete: replacing a "
            "meaningful share of a country's liquid fuel from crops requires an "
            "area comparable to its entire arable base, which is the arithmetic "
            "behind the food and fuel debate."
        ),
    ),
    # =========================================================================
    #  THE ONE HARD CEILING
    # =========================================================================
    Metric(
        name="Theoretical ethanol yield from glucose",
        symbol="Y_max",
        unit="grams of ethanol per gram of glucose",
        typical="0.511 g/g, with industrial processes reaching 90 - 95 % of it",
        formula="theoretical_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Not a model and not disputed. Each glucose yields two ethanol and "
            "two carbon dioxide, so roughly half the feedstock mass leaves as "
            "carbon dioxide by stoichiometry before any inefficiency is "
            "counted. Since good plants already achieve most of what remains, "
            "there is very little room left in this step, and improvement must "
            "come from feedstock, pretreatment or energy integration instead."
        ),
    ),
    # =========================================================================
    #  WHAT THE CONVERSION ACTUALLY ACHIEVES
    # =========================================================================
    Metric(
        name="Ethanol titre",
        symbol="C_EtOH",
        unit="per cent weight per volume in the fermented broth",
        typical="12 - 16 % w/v for starch and sugar feedstocks; 4 - 6 % is "
        "common for lignocellulosic",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "In most records a low titre is a downstream inconvenience. Here it "
            "is decisive, because distillation energy per litre of product "
            "rises steeply as titre falls, and a fuel that costs a large "
            "fraction of its own energy content to purify has no reason to "
            "exist. The gap between the two figures above is much of why "
            "cellulosic ethanol struggled."
        ),
    ),
    Metric(
        name="Sugar release from pretreatment and hydrolysis",
        symbol="X_sugar",
        unit="per cent of theoretically available sugar released",
        typical="65 - 90 % depending on feedstock and pretreatment severity",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The measure of how successfully the plant cell wall was defeated. "
            "It trades directly against inhibitor formation: harsher "
            "pretreatment releases more sugar and generates more of the furans "
            "and acids that poison the fermentation, so the optimum is a "
            "compromise rather than a maximum."
        ),
    ),
    Metric(
        name="Enzyme cost per litre of fuel",
        symbol="C_enz",
        unit="euro cents per litre",
        typical="historically the largest single unresolved operating cost for "
        "lignocellulosic ethanol",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The number that has kept the second generation uncompetitive. It "
            "connects directly to `white.industrial_enzymes`, where the same "
            "quantity appears as a market constraint rather than a process one, "
            "and it is the reason consolidated bioprocessing is pursued despite "
            "being harder."
        ),
    ),
    # =========================================================================
    #  WHAT THE FUEL IS LIKE TO USE
    # =========================================================================
    Metric(
        name="Volumetric energy density",
        symbol="E_v",
        unit="megajoules per litre",
        typical="about 21 for ethanol, 27 for butanol, 33 for biodiesel, "
        "against about 32 for petrol and 36 for diesel",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Ethanol carries roughly two thirds of petrol's energy per litre, "
            "so a litre-for-litre price comparison is misleading and fuel "
            "consumption rises correspondingly. It is also why butanol and "
            "drop-in hydrocarbons attract interest despite being harder to "
            "produce."
        ),
    ),
    Metric(
        name="Blend limit",
        symbol="B_max",
        unit="per cent by volume compatible with the existing vehicle fleet",
        typical="around 10 % ethanol in petrol for unmodified vehicles; higher "
        "only with flex-fuel engines",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A demand ceiling that has nothing to do with how much fuel can be "
            "produced. Once a market is saturated at its blend limit, "
            "additional supply has nowhere to go, which is why drop-in fuels "
            "that meet existing specifications are valued above better "
            "fermentation."
        ),
    ),
    Metric(
        name="Water footprint",
        symbol="W_f",
        unit="litres of water per litre of fuel",
        typical="dominated by feedstock irrigation, and negligible for rain-fed "
        "or residue feedstocks",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Almost all of it is agricultural rather than industrial, so the "
            "figure says more about where the crop was grown than about the "
            "conversion plant. Recorded because water scarcity, not carbon, is "
            "the binding constraint in several of the regions where biofuel "
            "feedstock is produced."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  The assessment relationships first, matching the ordering above, then the
#  conversion ones.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "energy_return_on_investment",
    "carbon_intensity",
    "theoretical_yield",
    "product_yield",
    "higher_heating_value",
    "space_time_yield",
    "mass_balance",
    "life_cycle_impact",
)
