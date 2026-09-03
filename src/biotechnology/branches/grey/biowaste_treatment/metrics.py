# =============================================================================
#  biotechnology.branches.grey.biowaste_treatment.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE METRIC THAT DECIDES WHETHER A PLANT IS ABOUT TO FAIL IS NOT A YIELD.
#  IT IS A RATIO BETWEEN AN INTERMEDIATE AND A BUFFER.
#
#  Methane yield tells an operator how the plant performed last week. The ratio
#  of volatile fatty acids to alkalinity tells them what is going to happen
#  next, because it shows acid accumulating before the pH has moved. By the
#  time pH falls the methanogens are already inhibited and recovery is a matter
#  of weeks. That is why the early indicator is placed first here and the yield
#  figures follow it.
#
#  THE SECOND ORGANISING IDEA IS THAT THE CLIMATE RESULT IS DECIDED BY A NUMBER
#  MOST PLANTS DO NOT MEASURE.
#
#      METHANE LEAKAGE IS A SMALL PERCENTAGE THAT CONTROLS A LARGE FRACTION OF
#      THE BENEFIT.
#
#  Methane is a far stronger greenhouse gas than the carbon dioxide from
#  burning it, so a few per cent escaping unburned cancels much of what the
#  plant achieved. It is recorded here with an INDICATIVE evidence level, which
#  is deliberate: the honest state of the field is that leakage is measured
#  rarely and estimated often.
#
#  A THIRD POINT. Biomethane potential is a LABORATORY CEILING, not a
#  prediction. Field yields fall short of it, for the same reason
#  `grey.bioremediation` reports laboratory rates it cannot reproduce on site.
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
    #  THE EARLY WARNING, WHICH MATTERS MORE THAN ANY YIELD
    # =========================================================================
    Metric(
        name="Volatile fatty acid to alkalinity ratio",
        symbol="VFA/TA",
        unit="dimensionless ratio",
        typical="a low ratio indicates a stable digester; a rising ratio is the "
        "warning before pH moves",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Placed first because it is predictive rather than descriptive. "
            "Acid accumulates before the buffer is exhausted, so this ratio "
            "moves while there is still time to reduce the feed. Once pH itself "
            "has fallen the methanogens are inhibited and recovery takes weeks, "
            "which makes this the most operationally valuable number in the "
            "record."
        ),
    ),
    Metric(
        name="Organic loading rate",
        symbol="OLR",
        unit="kilograms of volatile solids per cubic metre of reactor per day",
        typical="raised cautiously toward the design value and reduced "
        "immediately when the ratio above rises",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The lever the operator actually pulls, and the cause of the "
            "characteristic failure when it is pulled too far. Hydrolysis and "
            "acidogenesis respond to an increase within hours; methanogenesis "
            "responds over days. Overfeeding exploits exactly that mismatch."
        ),
    ),
    Metric(
        name="Hydraulic retention time",
        symbol="HRT",
        unit="days",
        typical="weeks for mesophilic digestion of typical feedstock",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How long material stays in the vessel, which must exceed the "
            "generation time of the slowest organisms or they are washed out. "
            "For fibrous feedstock it is set by hydrolysis rather than by "
            "methanogenesis, and it determines the vessel volume and therefore "
            "most of the capital cost."
        ),
    ),
    # =========================================================================
    #  WHAT COMES OUT, AND THE CEILING IT IS MEASURED AGAINST
    # =========================================================================
    Metric(
        name="Specific methane yield",
        symbol="Y_CH4",
        unit="cubic metres of methane per tonne of volatile solids added",
        formula="biogas_yield",
        typical="high for food waste and fats, low for manure and fibrous "
        "material",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The headline performance figure and the basis of the revenue. It "
            "is quoted per volatile solids rather than per tonne of feedstock, "
            "because a tonne of wet material is mostly water and comparing raw "
            "tonnages between feedstocks is meaningless."
        ),
    ),
    Metric(
        name="Biomethane potential",
        symbol="BMP",
        unit="cubic metres of methane per tonne of volatile solids",
        typical="a laboratory ceiling that field plants approach and do not "
        "reach",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A batch assay run to completion under ideal conditions. It is a "
            "ceiling rather than a prediction: a continuous plant operates at "
            "finite residence time with variable feedstock, so its yield sits "
            "below this figure. Quoting the assay as an expected output is the "
            "commonest overstatement in project proposals, and it is the same "
            "laboratory-to-field gap `grey.bioremediation` documents."
        ),
    ),
    Metric(
        name="Volatile solids destruction",
        symbol="VS_dest",
        unit="per cent of volatile solids converted",
        typical="a majority for readily degradable food waste, considerably "
        "less for fibrous material",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How much of the organic matter was actually converted, which "
            "determines both the gas produced and the mass of digestate "
            "remaining. It is the direct measure of what the process did, and "
            "it is the number that says whether a disappointing yield reflects "
            "poor conversion or simply a low-energy feedstock."
        ),
    ),
    Metric(
        name="Methane content of raw biogas",
        symbol="x_CH4",
        unit="per cent by volume",
        typical="somewhat over half, with most of the balance carbon dioxide",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Sets the calorific value directly and determines how much work "
            "upgrading has to do to reach grid quality. A falling value during "
            "operation is a useful corroborating signal of the acidification "
            "problem, since inhibited methanogens shift the gas composition "
            "before anything else visible happens."
        ),
    ),
    # =========================================================================
    #  THE NUMBER THAT DECIDES THE CLIMATE RESULT
    # =========================================================================
    Metric(
        name="Methane leakage rate",
        symbol="f_leak",
        unit="per cent of methane produced that escapes unburned",
        typical="small in percentage terms and large in effect, and measured "
        "at few plants",
        evidence=EvidenceLevel.INDICATIVE,
        note=(
            "The evidence level is deliberate and is the point of the entry. "
            "Methane is a far stronger greenhouse gas than the carbon dioxide "
            "produced by burning it, so a few per cent escaping from vessels, "
            "storage or upgrading cancels much of the benefit the plant was "
            "built for. Most plants estimate this rather than measure it, which "
            "means the sector's headline climate figures rest on an assumption."
        ),
    ),
    Metric(
        name="Avoided landfill methane emission",
        symbol="M_avoid",
        unit="tonnes of carbon dioxide equivalent per tonne of waste diverted",
        typical="the largest single term in the climate case, and larger than "
        "the energy displacement term",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The comparison that the whole record should be judged on. The "
            "benefit is chiefly that methane is generated in a sealed vessel "
            "rather than under a field with partial capture, and the energy "
            "recovered is a consequence of that rather than the reason for it. "
            "The term shrinks substantially where the alternative is "
            "incineration with energy recovery rather than landfill."
        ),
    ),
    # =========================================================================
    #  THE DIGESTATE, WHICH IS HALF THE OUTPUT AND MOST OF THE LOGISTICS
    # =========================================================================
    Metric(
        name="Digestate nutrient content",
        symbol="c_NPK",
        unit="kilograms of nitrogen, phosphorus and potassium per tonne",
        typical="dilute, and with a nutrient ratio that rarely matches what a "
        "crop needs",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "What makes the residue a product rather than a waste. Because the "
            "ratio does not match crop demand, applying enough of one nutrient "
            "over-applies another, which is the practical constraint on "
            "application rate and the reason nutrient regulation bites here."
        ),
    ),
    Metric(
        name="Digestate transport radius",
        symbol="r_econ",
        unit="kilometres within which spreading remains economic",
        typical="short, because the material is mostly water",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The constraint that decides plant siting and that separation and "
            "dewatering exist to relax. A plant without sufficient agricultural "
            "land inside this radius, available at the right time of year, has "
            "a disposal problem rather than a product, whatever its gas yield "
            "says."
        ),
    ),
    Metric(
        name="Physical contaminant content of digestate",
        symbol="c_phys",
        unit="per cent by mass of plastic, glass and metal",
        typical="low where waste is separated at the household, higher where "
        "it is separated mechanically afterwards",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The measurable consequence of collection policy, and the number "
            "that determines whether digestate may go to agricultural land at "
            "all. It is also the route by which a process intended as recycling "
            "delivers microplastic to soil, which is why quality protocols set "
            "a limit on it."
        ),
    ),
    # =========================================================================
    #  AND WHETHER THE PLANT PAYS FOR ITSELF
    # =========================================================================
    Metric(
        name="Gate fee",
        symbol="C_gate",
        unit="euro per tonne of waste accepted",
        typical="set by what disposal would otherwise have cost, which is set "
        "by landfill tax",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The honest statement of the business model. Most plants earn more "
            "from accepting the waste than from selling the gas, which means "
            "the sector's viability is a function of disposal policy rather "
            "than of energy prices, and explains why the same plant is viable "
            "in one jurisdiction and not across the border."
        ),
    ),
    Metric(
        name="Parasitic energy demand",
        symbol="f_para",
        unit="per cent of energy produced consumed by the plant itself",
        typical="a modest but not negligible share, for heating, mixing and "
        "upgrading",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Digesters must be heated and stirred, and upgrading to biomethane "
            "costs energy of its own. Net rather than gross output is what the "
            "plant actually delivers, and thermophilic operation trades a "
            "higher rate for a higher demand here."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Yield and kinetics, then the balances the climate case rests on.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "biogas_yield",
    "first_order_decay",
    "monod_equation",
    "mass_balance",
    "energy_balance",
    "global_warming_potential",
)
