# =============================================================================
#  biotechnology.branches.grey.phytoremediation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS ARE GROUPED BY MECHANISM, BECAUSE THE MECHANISMS HAVE
#  DIFFERENT ENDPOINTS AND ARE ROUTINELY CONFLATED.
#
#      CONTAIN     the contamination stays; the plants stop it moving
#      DEGRADE     the contamination is destroyed, mostly by root-zone microbes
#      EXTRACT     the contamination leaves the soil, in the harvest
#      VOLATILISE  the contamination leaves the soil, into the air
#
#  The order is deliberate and is not the order of interest. Containment is
#  first because it is what is actually deployed at most sites. Extraction is
#  third despite being the most discussed, because it is the least deployed.
#  Volatilisation is last because it is relocation.
#
#  EVERY EXTRACTION ENTRY CARRIES ITS DISPOSAL CONSEQUENCE. Harvested
#  hyperaccumulator biomass is contaminated material. An applications list that
#  stopped at the harvest would describe half a process.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = [
    "APPLICATIONS",
    "TECHNOLOGIES",
    "ORGANISMS",
    "TECHNIQUES",
    "CHALLENGES",
]


# =============================================================================
#  APPLICATIONS
#  By mechanism, and in order of how much is actually deployed.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # ---- CONTAIN: the majority of real deployment ------------------------------
    "Hydraulic control of groundwater plumes by deep-rooted poplar and willow "
    "plantings, whose transpiration draws enough water to arrest plume "
    "migration, which is the most reliable application in this record",
    "Vegetative covers over mine tailings, smelter fallout and contaminated "
    "fill, preventing dust generation and erosion across areas too large for "
    "any engineered treatment",
    "Phytostabilisation of metal-contaminated soil by species that tolerate the "
    "metal without accumulating it, which is chosen deliberately so grazing "
    "animals and insects are not exposed",
    "Riparian buffer strips intercepting nutrient and pesticide run-off before "
    "it reaches a watercourse",
    "Landfill cap evapotranspiration covers, which use plant water demand "
    "instead of an impermeable membrane to limit leachate generation",
    # ---- DEGRADE: real, and hard to separate from the soil community ------------
    "Rhizodegradation of petroleum hydrocarbons, in which root exudates support "
    "a denser and more active microbial community and the degradation is done "
    "by those microbes rather than by the plant",
    "Constructed wetland treatment of mine drainage, sewage and industrial "
    "effluent, which runs continuously for decades on almost no input",
    "Treatment of explosives residues at former munitions sites, where several "
    "plant species transform the parent compounds",
    "Degradation of chlorinated solvents taken up by trees, where plant "
    "enzymes act on the compound in tissue",
    # ---- EXTRACT: the distinctive capability, and its waste stream --------------
    "Phytoextraction of nickel, zinc and cadmium by hyperaccumulator species, "
    "which concentrates the metal into above-ground tissue that is then cut and "
    "removed, and which produces contaminated biomass requiring managed "
    "disposal",
    "Phytomining of nickel from ultramafic and serpentine soils, where the "
    "recovered metal has enough value to offset part of the cost and the "
    "harvest is smelted deliberately rather than disposed of",
    "Arsenic extraction by fern species, which is one of the few effective "
    "biological routes for that contaminant and which produces arsenic-bearing "
    "fronds that are hazardous waste",
    "Caesium and strontium uptake from contaminated land, and the same "
    "consequence: the harvest is radioactive material and its disposal is the "
    "governing cost",
    "Rhizofiltration of metals from water by roots in a flow-through system, "
    "which is extraction applied to a stream rather than to a soil",
    # ---- VOLATILISE: recorded, and recorded as relocation ------------------------
    "Volatilisation of selenium and mercury into the atmosphere by plants that "
    "convert them to volatile forms, which moves the contaminant into shared "
    "air rather than removing it and which is treated sceptically for exactly "
    "that reason",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the constraint each addresses: reach, uptake, and what happens
#  to the harvest.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- choosing what to plant -------------------------------------------------
    "Hyperaccumulator species screening and selection, which is largely a "
    "botanical survey exercise since the useful species were found in the wild "
    "rather than bred",
    "Fast-growing tree selection for hydraulic control, where the relevant "
    "property is water demand and root depth rather than any uptake capability",
    "Cultivar and provenance matching to site climate and soil, since a species "
    "that performs in one region may not establish in another",
    "Mycorrhizal and rhizosphere inoculation, which improves establishment on "
    "hostile substrates and which faces the same colonisation problem "
    "`grey.bioaugmentation` documents",
    # ---- getting the plants to grow on contaminated ground ----------------------
    "Soil amendment with organic matter, lime and fertiliser to make a tailings "
    "or spoil substrate plantable at all",
    "Irrigation and establishment management through the first seasons, which is "
    "when most plantings fail",
    "Deep planting and borehole planting techniques to place roots nearer the "
    "contaminated horizon",
    # ---- raising uptake, and the reason that is now restricted -------------------
    "Chelate-assisted extraction using synthetic aminopolycarboxylates, which "
    "raises metal uptake substantially and simultaneously mobilises metal "
    "toward groundwater, and which is restricted for that reason",
    "Biodegradable chelating agents and acidification, developed as the "
    "lower-risk replacement for the above",
    "Transgenic enhancement of uptake, tolerance and transformation, which is "
    "demonstrated in research and effectively excluded from field use by "
    "deliberate release requirements",
    # ---- and what happens to the harvest -----------------------------------------
    "Harvest scheduling and biomass handling, which determines whether the "
    "metal actually leaves the site or returns to it as litter",
    "Biomass volume reduction by controlled combustion, which concentrates the "
    "metal into ash and does not remove it, so the ash is the disposal object",
    "Metal recovery from ash in phytomining, which is the only route in this "
    "record where the harvested contaminant has value",
    "Contaminated biomass disposal to hazardous waste routes, which is the step "
    "most often omitted from cost estimates",
)


# =============================================================================
#  ORGANISMS
#  Plants, and the reason each is listed is its specific capability.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "populus_species",  # hydraulic control, the most deployed application
    "salix_species",  # willow, hydraulic control and moderate uptake
    "brassica_juncea",  # the standard extraction workhorse
    "pteris_vittata",  # arsenic hyperaccumulator, a rare capability
    "helianthus_annuus",  # rhizofiltration and extraction, high biomass
    "phragmites_australis",  # constructed wetlands, and an invasive risk
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "greenhouse_pot_trial",
    "field_plot_trial",
    "inductively_coupled_plasma_spectrometry",
    "sequential_extraction",
    "sap_flow_measurement",
    "soil_sampling",
    "biomass_measurement",
    "process_modelling",
)


# =============================================================================
#  CHALLENGES
#  The two hard physical limits first, because they define the scope.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the physical limits -----------------------------------------------------
    "Rooting depth, which confines the technique to the upper few metres and "
    "places deeper contamination outside the method rather than slow within it",
    "Timescale, since extraction proceeds one growing season at a time and a "
    "substantial reduction takes years to decades, which suits abandoned land "
    "and not a development schedule",
    "Seasonality and weather, which halt the process in winter and in drought "
    "and which no operator controls",
    # -- the plants have to survive the contamination -----------------------------
    "Phytotoxicity, since concentrations high enough to require remediation are "
    "frequently high enough to prevent establishment, so the most contaminated "
    "zone is the hardest to plant",
    "Poor substrate condition on tailings and spoil, which lack structure, "
    "organic matter and nutrients before any contaminant is considered",
    "The trade between accumulation and biomass, because hyperaccumulators are "
    "typically small and slow-growing while high-biomass species accumulate "
    "little, and total removal is the product of the two",
    # -- what is done with what is removed -----------------------------------------
    "Contaminated biomass disposal, which is hazardous waste, is frequently "
    "omitted from cost estimates, and is the step that makes an extraction "
    "project complete rather than merely started",
    "Combustion concentrating rather than removing the metal, so the ash "
    "becomes the disposal object and the problem has changed form again",
    # -- the pathways the technique itself creates -----------------------------------
    "Entry of accumulated metal into food chains through grazing animals, "
    "insects and leaf litter, which means a phytoextraction site must be "
    "managed as a contaminated site rather than left as a meadow",
    "Return of contaminant to soil in unharvested litter, which reverses part "
    "of the extraction if harvest timing is wrong",
    "Chelate-induced leaching of mobilised metal toward groundwater, which is "
    "why the most effective uptake enhancement is restricted",
    "Volatilisation transferring a contaminant to shared air, which is "
    "relocation and not treatment",
    # -- and the containment applications have their own -------------------------------
    "Failure of hydraulic control during dormancy, when transpiration stops and "
    "the plume resumes moving, which requires the design to accommodate a "
    "seasonal gap",
    "Invasive species risk where a vigorous treatment species escapes the site, "
    "which is a real cost of some wetland plantings",
    "Demonstrating that degradation was attributable to the planting rather "
    "than to the soil community that would have acted anyway",
)
