# =============================================================================
#  biotechnology.branches.blue.seaweed_cultivation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two things about this facet need stating before the list.
#
#  FIRST, THE UNITS ARE DECEPTIVE UNLESS THE MOISTURE BASIS IS GIVEN. Seaweed
#  is roughly eighty to ninety per cent water when harvested, so a yield quoted
#  wet is around ten times the same yield quoted dry. A great deal of confusion
#  in published figures for this sector comes from comparing one with the
#  other, and every entry below states its basis explicitly.
#
#  SECOND, THIS RECORD DELIBERATELY INCLUDES METRICS THAT CONSTRAIN THE
#  SECTOR'S CLAIMS RATHER THAN SUPPORTING THEM. Iodine content and heavy metal
#  accumulation are limits on how much of this food can be eaten. Carbon
#  retention time is the quantity that decides whether a sequestration claim
#  means anything. Including them is the difference between describing an
#  industry and advertising it.
#
#  A NOTE ON WHY NO HARVEST-COST METRIC APPEARS. `blue.algal_biotechnology`
#  opens with culture density because separating microalgae from water governs
#  its economics. Seaweed is lifted out of the sea by hand or by boat. The
#  constraint simply does not exist here, and its absence is the clearest
#  quantitative statement of why the two records are separate.
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
    #  WHAT THE FARM PRODUCES
    # =========================================================================
    Metric(
        name="Areal yield",
        symbol="Y_a",
        unit="tonnes of fresh weight per hectare per year",
        typical="20 - 100 t fresh weight per hectare per year for kelp, "
        "corresponding to roughly 2 - 15 tonnes dry",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Always state the moisture basis. Seaweed is roughly eighty to "
            "ninety per cent water at harvest, so a wet figure is about ten "
            "times its dry equivalent, and comparing one with the other is the "
            "commonest error in published figures for this sector. Yield "
            "depends more on site nutrient supply and current than on any "
            "husbandry decision."
        ),
    ),
    Metric(
        name="Specific growth rate",
        symbol="mu",
        unit="per cent increase in wet weight per day",
        typical="5 - 20 % per day during the active growing season",
        formula="specific_growth_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Rapid by the standards of terrestrial crops, and strongly "
            "seasonal. Growth concentrates in a window set by temperature, "
            "light and nutrient availability, so a farm's annual output is "
            "determined by a few months rather than spread evenly."
        ),
    ),
    Metric(
        name="Dry matter content",
        symbol="f_dm",
        unit="per cent of fresh weight",
        typical="10 - 20 %",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The conversion factor behind every other figure in this facet, "
            "and the reason drying is the largest energy cost in the chain. It "
            "is also why wet seaweed cannot travel far: the crop degrades "
            "within hours and most of what would be transported is water."
        ),
    ),
    # =========================================================================
    #  WHAT IS EXTRACTED FROM IT
    # =========================================================================
    Metric(
        name="Hydrocolloid yield",
        symbol="Y_hyd",
        unit="per cent of dry weight recovered as extracted polysaccharide",
        typical="15 - 40 % depending on species, season and extraction method",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Varies with season as much as with species, since the plant's "
            "polysaccharide content changes across its growing cycle. Harvest "
            "timing is therefore a processing decision as well as an "
            "agricultural one, and a farm optimised for food tonnage is not "
            "optimised for extract yield."
        ),
    ),
    Metric(
        name="Gel strength",
        symbol="S_gel",
        unit="grams per square centimetre at stated concentration and "
        "temperature",
        typical="the primary quality specification for agar and carrageenan",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "What the buyer actually pays for. Two batches with identical "
            "hydrocolloid yield can differ substantially in value if their gel "
            "strength differs, which is why extraction conditions and harvest "
            "timing matter commercially rather than only technically."
        ),
    ),
    Metric(
        name="Protein content",
        symbol="f_prot",
        unit="per cent of dry weight",
        typical="5 - 25 % depending on species and season, higher in red "
        "seaweeds",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Frequently quoted in support of seaweed as a protein source, and "
            "it should be read with two qualifications: digestibility is lower "
            "than for terrestrial protein because of the polysaccharide matrix, "
            "and nitrogen-to-protein conversion factors developed for plants "
            "overestimate seaweed protein unless corrected."
        ),
    ),
    # =========================================================================
    #  WHAT THE CROP REMOVES FROM THE WATER
    # =========================================================================
    Metric(
        name="Nitrogen removal",
        symbol="N_rem",
        unit="kilograms of nitrogen per hectare per year",
        typical="substantial, and the basis of the nutrient bioremediation case",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The most defensible environmental claim in this record, because "
            "the nitrogen is physically removed from the water when the crop is "
            "landed. It is measurable, it addresses eutrophication directly, "
            "and unlike the carbon claim it does not depend on what happens to "
            "the biomass afterwards."
        ),
    ),
    Metric(
        name="Carbon retention time",
        symbol="t_C",
        unit="years before fixed carbon returns to the atmosphere",
        typical="months for a crop that is eaten or processed",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The metric that decides whether a sequestration claim means "
            "anything, and it is included precisely because it usually is not. "
            "Carbon fixed by a crop that is eaten, fed or extracted returns "
            "within months. Durable sequestration requires a mechanism for "
            "keeping the carbon out of circulation, and cultivation alone is "
            "not one."
        ),
    ),
    # =========================================================================
    #  WHAT LIMITS HOW MUCH CAN BE EATEN
    # =========================================================================
    Metric(
        name="Iodine content",
        symbol="c_I",
        unit="milligrams per kilogram of dry weight",
        typical="very high in brown seaweeds, exceeding daily intake limits in "
        "small portions",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A genuine constraint on consumption rather than a theoretical "
            "concern. Some kelps concentrate iodine to a level where a few "
            "grams exceed a recommended daily intake, which is why several "
            "jurisdictions set limits or require labelling and why processing "
            "to reduce iodine is a real part of the food chain."
        ),
    ),
    Metric(
        name="Heavy metal and arsenic content",
        symbol="c_metal",
        unit="milligrams per kilogram of dry weight",
        typical="site-dependent, and regulated by maximum levels for food",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The crop concentrates what the water holds, so this is a property "
            "of the site rather than of the species, and it cannot be improved "
            "by husbandry. Arsenic speciation matters: the organic forms that "
            "dominate in seaweed are far less toxic than inorganic arsenic, and "
            "a total figure without speciation overstates the hazard."
        ),
    ),
    # =========================================================================
    #  WHETHER THE FARM SURVIVES THE SEASON
    # =========================================================================
    Metric(
        name="Crop loss to disease and epiphytes",
        symbol="L_crop",
        unit="per cent of expected harvest lost in an affected season",
        typical="capable of approaching total loss in an outbreak",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The risk that dominates this sector and the one least visible in "
            "its production statistics. Clonal monoculture across a whole "
            "growing region means an outbreak spreads without meeting "
            "resistance, and regional industries have collapsed within a single "
            "season."
        ),
    ),
    Metric(
        name="Effective population size of cultivated stock",
        symbol="N_e",
        unit="dimensionless",
        typical="low in vegetatively propagated tropical crops",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The underlying cause of the entry above, and the same measure "
            "`green.animal_biotechnology` uses for livestock breeds. Decades of "
            "cutting propagation from a narrow founding stock leave a crop with "
            "little capacity to respond to a new pathogen or to warming water, "
            "and rebuilding diversity means returning to wild populations."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Growth and yield first, then the balances that support or limit the claims.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "specific_growth_rate",
    "product_yield",
    "mass_balance",
    "nutrient_uptake_rate",
    "effective_population_size",
    "life_cycle_impact",
)
