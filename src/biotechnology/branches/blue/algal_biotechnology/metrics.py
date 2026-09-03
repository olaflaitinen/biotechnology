# =============================================================================
#  biotechnology.branches.blue.algal_biotechnology.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS THE ONE THAT DECIDES EVERYTHING, and it is not
#  productivity. It is culture density, because density sets the harvest cost
#  and harvest cost sets which products can exist.
#
#  A reader who takes only the first three entries will understand why the same
#  organisms, ponds and centrifuges support a profitable pigment business and
#  cannot support a fuel business.
#
#  A WARNING ABOUT AREAL PRODUCTIVITY. It is the figure most often quoted for
#  algae and the one most often quoted misleadingly. Short-term laboratory
#  values under optimal light, temperature and carbon dioxide supply are
#  routinely several times what an outdoor system sustains across a year, and
#  the projections behind the fuel programmes of the late 2000s were built by
#  extrapolating exactly that gap. The metric below records both figures and
#  says which is which, because presenting the laboratory number alone is how
#  the error was made.
#
#  A SECOND WARNING ABOUT LIPID CONTENT. It is usually raised by starving the
#  culture, and starved cells stop dividing. Percentage lipid and total lipid
#  output move in opposite directions, so a high lipid fraction can accompany a
#  lower yield of oil per hectare. Quoting the fraction alone is the second
#  commonest way to overstate an algal process.
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
    #  THE DILUTION THAT GOVERNS THE ECONOMICS
    # =========================================================================
    Metric(
        name="Culture density at harvest",
        symbol="C_x",
        unit="grams of dry biomass per litre",
        typical="0.5 - 1 g/L in open ponds, 2 - 8 g/L in photobioreactors, and "
        "far higher in heterotrophic fermentation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The number behind every economic conclusion in this record. At one "
            "gram per litre, recovering a tonne of biomass means handling "
            "roughly a thousand tonnes of water. It is also why heterotrophic "
            "cultivation, which abandons photosynthesis and reaches "
            "fermentation densities, is how much commercial algal oil is "
            "actually produced."
        ),
    ),
    Metric(
        name="Harvest and dewatering energy",
        symbol="E_harv",
        unit="kilowatt hours per kilogram of dry biomass",
        typical="a large and sometimes dominant share of the total energy "
        "input, and higher for centrifugation than for flocculation",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The direct consequence of the entry above and the reason the "
            "applications in `practice.py` are ordered by product value. This "
            "cost is roughly the same whatever is being grown, so it is "
            "negligible against a pigment worth tens of thousands of euro a "
            "tonne and fatal against a fuel worth a few hundred."
        ),
    ),
    Metric(
        name="Product value per tonne",
        symbol="V_t",
        unit="euro per tonne of product",
        typical="tens of thousands for pigments, thousands for nutritional "
        "oils, hundreds for fuel",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Recorded as a metric because in this record it is a technical "
            "constraint rather than a commercial afterthought. Placed "
            "immediately after harvest energy so the ratio between the two is "
            "visible, since that ratio is what decides whether an application "
            "exists."
        ),
    ),
    # =========================================================================
    #  HOW FAST IT GROWS, AND HOW THE FIGURE IS MISUSED
    # =========================================================================
    Metric(
        name="Areal productivity",
        symbol="P_a",
        unit="grams of dry biomass per square metre per day",
        typical="10 - 25 g/m2/day sustained outdoors across a year; "
        "short-term laboratory values are several times higher",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The most quoted and most misused figure in this field. Laboratory "
            "values under optimal light, temperature and carbon dioxide are "
            "routinely several times what an outdoor system sustains annually, "
            "and the fuel projections of the late 2000s were built by "
            "extrapolating the laboratory number. Both figures appear here "
            "deliberately, because presenting only the higher one is how the "
            "error was made."
        ),
    ),
    Metric(
        name="Photosynthetic efficiency",
        symbol="eta_PAR",
        unit="per cent of incident photosynthetically active radiation "
        "converted to biomass energy",
        typical="1 - 3 % in practice, against a theoretical ceiling near 10 %",
        formula="photosynthetic_efficiency",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The honest measure of how well the system uses light, and the gap "
            "between practice and the theoretical ceiling is where the "
            "remaining engineering room is. Algae outperform terrestrial crops "
            "here, which is a genuine advantage and not the one that decides "
            "the economics."
        ),
    ),
    Metric(
        name="Specific growth rate",
        symbol="mu",
        unit="per day",
        typical="0.3 - 2 per day, corresponding to doubling times of hours to "
        "days",
        formula="specific_growth_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Fast by the standards of any crop, which is the source of the "
            "field's original appeal. It is also what makes a contamination "
            "event catastrophic: an unwanted organism with a similar rate "
            "displaces the culture within days."
        ),
    ),
    # =========================================================================
    #  WHAT THE BIOMASS CONTAINS, AND WHY THE FRACTION MISLEADS
    # =========================================================================
    Metric(
        name="Lipid content of dry biomass",
        symbol="f_lipid",
        unit="per cent of dry weight",
        typical="20 - 50 % under nutrient limitation, lower during rapid "
        "growth",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Read alone, this figure overstates. Lipid fraction is raised by "
            "starving the culture, and starved cells stop dividing, so the "
            "fraction and the total output move in opposite directions. A "
            "process reporting fifty per cent lipid may yield less oil per "
            "hectare than one reporting twenty. Always pair it with the entry "
            "below."
        ),
    ),
    Metric(
        name="Lipid productivity",
        symbol="P_lipid",
        unit="grams of lipid per square metre per day",
        typical="the product of areal productivity and lipid fraction, and "
        "the only figure that settles the trade between them",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The correct measure, because it captures the trade that the "
            "fraction hides. It is the number that should be compared between "
            "processes, and it is quoted far less often than the fraction "
            "precisely because it is less flattering."
        ),
    ),
    Metric(
        name="Target compound content",
        symbol="f_target",
        unit="per cent of dry weight",
        typical="1 - 5 % for astaxanthin under stress, up to 60 - 70 % for "
        "protein in spirulina",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Determines how much biomass must be processed per kilogram of "
            "product, and therefore multiplies the harvest cost. A compound at "
            "one per cent of dry weight requires a hundred kilograms of biomass "
            "per kilogram of product, before extraction losses."
        ),
    ),
    # =========================================================================
    #  WHAT THE PROCESS CONSUMES
    # =========================================================================
    Metric(
        name="Carbon dioxide utilisation efficiency",
        symbol="eta_CO2",
        unit="per cent of supplied carbon dioxide fixed into biomass",
        typical="frequently below 50 % in open systems, since undissolved gas "
        "escapes",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Central to any carbon capture claim and routinely omitted from "
            "one. Gas that bubbles through an open pond and leaves has been "
            "moved rather than captured, and a capture claim that does not "
            "state this efficiency is not a measurement."
        ),
    ),
    Metric(
        name="Water demand including evaporative loss",
        symbol="W_a",
        unit="cubic metres per tonne of dry biomass",
        typical="substantial in open systems, and dominated by evaporation "
        "rather than by the culture volume",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Included because low land use is claimed for this field far more "
            "often than water use is reported. The water may be saline or waste "
            "rather than fresh, which changes the significance considerably, so "
            "the figure should always be stated with the water type."
        ),
    ),
    Metric(
        name="Energy return on investment",
        symbol="EROI",
        unit="megajoules delivered per megajoule consumed, dimensionless",
        typical="reported below or near 1 for most algal fuel routes",
        formula="energy_return_on_investment",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Applies only to the fuel application and is the quantitative form "
            "of that programme's failure. A value near or below one means the "
            "process consumes about as much energy as the fuel delivers, and "
            "harvest, dewatering and extraction are where it goes. The same "
            "figure is irrelevant to every other application in this record, "
            "since nobody burns astaxanthin."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Growth and light first, then the assessment relationships.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "specific_growth_rate",
    "monod_equation",
    "photosynthetic_efficiency",
    "product_yield",
    "energy_return_on_investment",
    "mass_balance",
    "life_cycle_impact",
)
