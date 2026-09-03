# =============================================================================
#  biotechnology.branches.grey.phytoremediation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `grey.bioremediation` is first because this record is defined against it.
#  The two treat the same contamination with different organisms, and the
#  division of labour is clean enough to state in a line:
#
#      MICROBES DESTROY ORGANICS AND CANNOT REMOVE A METAL.
#      PLANTS REMOVE A METAL AND MOSTLY DO NOT DESTROY ORGANICS THEMSELVES.
#
#  Even rhizodegradation, the plant contribution to organic breakdown, is
#  performed by the microbes the roots feed. That is worth a reader knowing,
#  because it means the two records are complements rather than competitors.
#
#  `grey.biomining` is linked for a reason that is not obvious. Nickel
#  phytomining and microbial heap leaching are the same proposition, that a
#  metal too dilute to mine conventionally can be recovered biologically, and
#  they are pursued by different communities that rarely cite each other.
#
#  `blue.marine_biomaterials` IS DELIBERATELY NOT LINKED despite the shared
#  vocabulary of biosorption. That record is about material properties, and the
#  overlap is a word rather than a mechanism.
#
#  `green.molecular_plant_breeding` is linked for something this record admits
#  about itself. Its useful species were FOUND rather than bred: surveyed off
#  serpentine outcrops and mine spoil by botanists with no cleanup in mind. So
#  the four-way trade in `governance.py` between accumulation, biomass,
#  tolerance and climate is not a trade anybody designed, it is whatever the
#  wild happened to supply. That record holds the methods by which such a trade
#  would ordinarily be improved, and they have barely been applied here.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, each on a mechanism the record actually performs.
#
#  Goal 15 is the strongest and is claimed twice over: contaminated soil is
#  degraded land, and vegetative covers over tailings are literally land
#  restoration at a scale nothing else reaches.
#
#  Goal 6 is claimed on constructed wetlands treating mine drainage and
#  effluent, and on hydraulic control preventing plumes reaching abstraction
#  points. Both are established applications rather than proposals.
#
#  Goal 3 is claimed on the same basis as elsewhere in the branch, since
#  cleanup targets are derived from human exposure pathways.
#
#  Goal 12 is claimed narrowly, for phytomining alone, where a metal is
#  recovered from material too dilute to process conventionally. It is NOT
#  claimed for the record as a whole, because most of the practice generates a
#  hazardous waste stream rather than reducing one.
#
#  GOAL 2 IS DELIBERATELY NOT CLAIMED although this record grows crops on
#  farmland with farm equipment. Nothing here produces food, and the governance
#  work goes into making sure of it. Claiming a food goal would be the sort of
#  association-by-appearance that rule 12 exists to catch.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on exposure-derived cleanup targets
    6,  # Water, on constructed wetlands and hydraulic plume control
    12,  # Responsible production, narrowly, for phytomining recovery
    15,  # Land, on restoring contaminated and degraded ground
)


# =============================================================================
#  GLOSSARY
#  Grouped by the four mechanisms, then the plant biology, then the accounting.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the mechanisms, which have different endpoints ------------------------
    "phytoremediation",
    "phytoextraction",
    "phytostabilisation",
    "phytodegradation",
    "rhizodegradation",
    "phytovolatilisation",
    "rhizofiltration",
    "hydraulic_control",
    "constructed_wetland",
    "evapotranspiration_cover",
    # -- the plant biology it depends on ---------------------------------------
    "hyperaccumulator",
    "metal_tolerance",
    "rhizosphere",
    "root_exudate",
    "translocation",
    "transpiration",
    "rooting_depth",
    "phytotoxicity",
    "mycorrhiza",
    # -- what governs how much can be taken ------------------------------------
    "phytoavailability",
    "chelating_agent",
    "sequential_extraction",
    "soil_amendment",
    # -- and the accounting ----------------------------------------------------
    "bioconcentration_factor",
    "translocation_factor",
    "biomass_yield",
    "phytomining",
    "contaminated_biomass",
    "hazardous_waste",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "phytoremediation_field_review",
    "hyperaccumulator_species_survey",
    "chelate_assisted_extraction_leaching",
    "nickel_phytomining_field_trial",
    "arsenic_hyperaccumulating_fern",
    "poplar_hydraulic_control",
    "constructed_wetland_mine_drainage",
    "phytoextraction_biomass_disposal",
)


# =============================================================================
#  RELATED
#  Six edges. The complement first, then the plant biology, then the
#  applications that share the recovery proposition.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the microbial half of the same job, and its complementary limits ------
    "grey.bioremediation",
    # -- the species were surveyed rather than bred, and this is where the
    #    breeding methods that were never applied to them live ----------------
    "green.molecular_plant_breeding",
    # -- the same proposition about dilute metal, pursued separately -----------
    "grey.biomining",
    # -- the effluent side, where wetlands and reactors overlap ----------------
    "grey.wastewater_treatment",
    # -- measuring the site and the tissue over decades ------------------------
    "grey.environmental_biomonitoring",
    # -- the enhanced-uptake varieties that regulation keeps in containment ----
    "green.plant_genetic_engineering",
)
