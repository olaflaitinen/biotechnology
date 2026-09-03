# =============================================================================
#  biotechnology.branches.grey.wastewater_treatment.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS RECORD HAS THE OLDEST AND MOST CONSEQUENTIAL METRIC IN THE LIBRARY,
#  AND IT IS DEFINED BY A PROCEDURE RATHER THAN BY A QUANTITY.
#
#  Biochemical oxygen demand is not a measurement of any substance. It is the
#  oxygen consumed by a sample's own microorganisms over five days at twenty
#  degrees. It is slow, imprecise, dependent on the seed organisms, and it is
#  written into discharge law worldwide because it measures the thing that
#  actually matters: how much oxygen this water will take out of the river.
#
#      IT IS A BETTER DESIGNED METRIC THAN ITS CRITICS ALLOW, AND IT IS A
#      MEASUREMENT THAT TAKES FIVE DAYS TO REPORT A PROBLEM THAT NEEDS AN
#      ANSWER IN AN HOUR.
#
#  Both of those are true, which is why chemical oxygen demand exists beside it.
#
#  THE SECOND ORGANISING IDEA IS SOLIDS RETENTION TIME, WHICH IS THE MASTER
#  CONTROL VARIABLE OF THE WHOLE FIELD. Separating how long the biomass stays
#  from how long the water stays is the entire invention of activated sludge,
#  and it is what decides which organisms can exist in the plant at all. An
#  operator adjusting it is choosing a community.
#
#  A THIRD POINT. The sludge metrics are not secondary. Sludge production and
#  the sludge volume index govern about half the cost and the commonest mode of
#  failure respectively.
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
    #  THE MASTER CONTROL VARIABLE
    # =========================================================================
    Metric(
        name="Solids retention time",
        symbol="SRT",
        unit="days",
        formula="solids_retention_time",
        typical="a few days for carbon removal alone; substantially longer "
        "where nitrification must be maintained",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The variable an operator actually controls and the one that "
            "decides which organisms can exist in the plant. Any organism whose "
            "growth rate is slower than the rate at which biomass is wasted is "
            "washed out, which is why nitrifiers require a long value and why "
            "shortening it to save energy silently removes the plant's nitrogen "
            "capability. Separating this from the hydraulic retention time "
            "below is the whole invention of activated sludge."
        ),
    ),
    Metric(
        name="Hydraulic retention time",
        symbol="HRT",
        unit="hours",
        typical="hours for the aerated stages of a municipal works",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How long the water stays, as against how long the biomass stays. "
            "Before biomass return was introduced the two were the same number, "
            "and a plant therefore had to be as large as its slowest organism "
            "required. Uncoupling them is what made city-scale treatment "
            "possible on a practical footprint."
        ),
    ),
    Metric(
        name="Food to microorganism ratio",
        symbol="F/M",
        unit="kilograms of biochemical oxygen demand per kilogram of mixed "
        "liquor suspended solids per day",
        typical="low values give stable well-settling sludge, high values give "
        "rapid growth and poor settling",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The loading expressed per unit of biomass rather than per unit of "
            "tank, which is what the organisms experience. It is the traditional "
            "operator's dial and it is closely tied to the settleability index "
            "below, since overloading is one route into a bulking event."
        ),
    ),
    # =========================================================================
    #  THE OLD METRIC THAT DISCHARGE LAW IS WRITTEN IN
    # =========================================================================
    Metric(
        name="Biochemical oxygen demand",
        symbol="BOD5",
        unit="milligrams of oxygen per litre over five days at twenty degrees",
        typical="a few hundred in raw municipal sewage, a small fraction of "
        "that in treated effluent",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A procedure rather than a quantity: the oxygen consumed by the "
            "sample's own organisms under standardised conditions. It is slow, "
            "imprecise and dependent on the seed, and it measures exactly the "
            "harm that matters, which is how much oxygen the discharge will "
            "strip from the receiving water. It is written into discharge "
            "consents worldwide, and its five-day delay is why the next entry "
            "exists."
        ),
    ),
    Metric(
        name="Chemical oxygen demand",
        symbol="COD",
        unit="milligrams of oxygen per litre",
        typical="higher than the biochemical value for the same sample, since "
        "it includes matter the organisms will not oxidise",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The same question answered chemically in hours instead of "
            "biologically in days. The ratio between the two is itself "
            "diagnostic: a wide gap indicates organic matter present but not "
            "biodegradable, which tells an operator that more residence time "
            "will not help and that the problem is not one biology will solve."
        ),
    ),
    Metric(
        name="Removal efficiency",
        symbol="eta",
        unit="per cent of influent load removed",
        typical="high for carbon in any functioning works; lower and far more "
        "variable for nitrogen and phosphorus",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The headline compliance figure, and it should always be read "
            "alongside the influent load rather than alone. A high percentage "
            "removal from a dilute influent can discharge more mass than a "
            "lower percentage from a concentrated one, and it is the mass that "
            "reaches the river."
        ),
    ),
    # =========================================================================
    #  NUTRIENTS, WHICH ARE THE HARD PART
    # =========================================================================
    Metric(
        name="Ammonium and total nitrogen in effluent",
        symbol="c_N",
        unit="milligrams of nitrogen per litre",
        typical="tightly limited in sensitive catchments and unregulated in "
        "many others",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Ammonium is directly toxic to fish, and total nitrogen drives the "
            "eutrophication recorded in `blue.algal_biotechnology`. Meeting a "
            "total nitrogen limit requires both nitrification and "
            "denitrification to work, which is why it is the consent condition "
            "most often missed."
        ),
    ),
    Metric(
        name="Total phosphorus in effluent",
        symbol="c_P",
        unit="milligrams of phosphorus per litre",
        typical="low limits in sensitive catchments, achieved biologically, "
        "chemically or by both together",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Phosphorus is frequently the limiting nutrient in fresh water, so "
            "a small residual concentration still drives algal growth. It is "
            "never destroyed: whatever leaves the water has entered the sludge "
            "or a chemical precipitate, and that is the whole of the "
            "phosphorus story."
        ),
    ),
    # =========================================================================
    #  THE SOLID, WHICH IS HALF THE COST AND THE COMMONEST FAILURE
    # =========================================================================
    Metric(
        name="Sludge volume index",
        symbol="SVI",
        unit="millilitres per gram of settled sludge",
        typical="a low value settles well; a high value indicates bulking",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The early warning for the failure that shuts plants down. If "
            "sludge does not settle it leaves with the effluent, taking the "
            "community with it, and the plant loses both its compliance and its "
            "biomass at once. Watching this index is a large part of what "
            "day-to-day operation consists of."
        ),
    ),
    Metric(
        name="Sludge production",
        symbol="Y_obs",
        unit="kilograms of dry solids per kilogram of oxygen demand removed",
        typical="substantially lower for anaerobic processes than for aerobic "
        "ones",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The pollutant that was removed from the water, now expressed as a "
            "mass of solid to be handled. This governs roughly half the "
            "operating cost, and it is the strongest argument for anaerobic "
            "treatment of concentrated effluent: less biomass grown, and "
            "methane produced instead of oxygen consumed."
        ),
    ),
    Metric(
        name="Mixed liquor suspended solids",
        symbol="MLSS",
        unit="milligrams per litre",
        typical="a few thousand in conventional activated sludge, several times "
        "that in a membrane bioreactor",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How much biomass the reactor holds. In a conventional plant it is "
            "capped by what the settling tank can separate, which is precisely "
            "the constraint a membrane removes, and that is why membrane "
            "systems achieve the same treatment in a much smaller footprint."
        ),
    ),
    # =========================================================================
    #  ENERGY, WHICH IS THE OTHER HALF OF THE COST
    # =========================================================================
    Metric(
        name="Aeration energy per volume treated",
        symbol="E_air",
        unit="kilowatt hours per cubic metre",
        typical="the dominant electricity demand of a conventional works",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Supplying oxygen against the resistance of water is expensive, and "
            "it is where almost all the optimisation effort goes. Ammonium-based "
            "aeration control, which matches air supply to actual load rather "
            "than to a fixed setpoint, is the commonest saving available to an "
            "existing plant."
        ),
    ),
    Metric(
        name="Biogas yield from digestion",
        symbol="Y_gas",
        unit="cubic metres of methane per kilogram of volatile solids destroyed",
        formula="biogas_yield",
        typical="sufficient at many works to offset a substantial share of the "
        "site electricity demand",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The energy recovered from the sludge, and the reason an "
            "energy-neutral works is conceivable rather than fanciful. It is "
            "the same process and the same measurement as "
            "`grey.biowaste_treatment`, applied to the solid a treatment plant "
            "produces rather than to material collected separately."
        ),
    ),
    # =========================================================================
    #  AND WHAT THE PROCESS WAS NOT BUILT TO CATCH
    # =========================================================================
    Metric(
        name="Micropollutant removal",
        symbol="eta_micro",
        unit="per cent removal of a named pharmaceutical or industrial compound",
        typical="highly compound-dependent, from near complete to negligible",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Reported per compound because a single figure would be "
            "meaningless. Some pharmaceuticals are removed incidentally by "
            "sorption to sludge, which is transfer rather than destruction; "
            "fluorinated compounds are not removed at all. Improving these "
            "numbers is a matter of adding ozonation or activated carbon rather "
            "than of better biology."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Retention and growth first, then the oxygen and gas balances.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "solids_retention_time",
    "monod_equation",
    "specific_growth_rate",
    "oxygen_transfer_rate",
    "biogas_yield",
    "mass_balance",
    "first_order_decay",
)
