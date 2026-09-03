# =============================================================================
#  biotechnology.branches.grey.wastewater_treatment.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS ARE GROUPED BY WHICH POLLUTANT IS BEING REMOVED, BECAUSE THE
#  THREE JOBS OF A TREATMENT WORKS ARE NOT ONE JOB AND THEY COMPETE FOR THE
#  SAME REACTOR.
#
#      CARBON       fast, robust, and what the process was originally built for
#      NITROGEN     two contradictory steps, and the first thing lost when a
#                   plant is cold or overloaded
#      PHOSPHORUS   cannot be destroyed, only moved into biomass or precipitated
#      PATHOGENS    a separate objective with a separate unit process
#      SLUDGE       what all of the above produce, and half the cost
#
#  THE SLUDGE GROUP IS NOT AN APPENDIX. Treating water converts dissolved
#  pollution into a wet solid, and a record that stopped at the effluent would
#  describe the half of the plant that the public sees.
#
#  TECHNOLOGIES ARE GROUPED BY HOW THE BIOMASS IS HELD, which is the real
#  taxonomy of treatment engineering: in suspension, on a surface, or behind a
#  membrane. That choice determines footprint, sludge behaviour and what the
#  plant can be pushed to do.
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
#  By pollutant, in the order a plant deals with them, ending with the solid.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # ---- CARBON: the original job, and the one that is solved ------------------
    "Municipal sewage treatment by activated sludge, which is the largest "
    "single deployment of microorganisms anywhere and which oxidises dissolved "
    "organic matter within hours",
    "Trickling filter and rotating biological contactor treatment, which "
    "achieve the same removal with the biomass fixed on a surface and far less "
    "energy for mixing",
    "High-strength industrial effluent treatment at breweries, dairies, pulp "
    "mills and food factories, where the organic load per volume is many times "
    "that of sewage",
    "Anaerobic treatment of high-strength effluent in upflow sludge blanket "
    "reactors, which converts the organic load to methane instead of to "
    "biomass and therefore produces energy rather than consuming it",
    "Lagoon and waste stabilisation pond treatment, which is the low-cost "
    "option where land is available and which is how a large share of the "
    "world's treated wastewater is actually handled",
    # ---- NITROGEN: two steps that contradict each other ------------------------
    "Nitrification of ammonium to nitrate by slow-growing autotrophs, which "
    "requires oxygen and a long solids retention time and which is the first "
    "capability a plant loses when it is overloaded or cold",
    "Denitrification of nitrate to nitrogen gas, which requires the absence of "
    "oxygen and a supply of organic carbon, so the plant must sequence anoxic "
    "and aerobic zones and must not have removed all the carbon first",
    "Anaerobic ammonium oxidation for concentrated side streams, which "
    "converts ammonium directly to nitrogen gas without the full oxygen demand "
    "or the carbon requirement of the conventional pair",
    "Nitrite shunt operation, stopping the oxidation one step early to save "
    "aeration energy and carbon, which requires holding a community in a state "
    "it does not naturally settle into",
    # ---- PHOSPHORUS: not destroyed, only relocated -----------------------------
    "Enhanced biological phosphorus removal, in which alternating anaerobic and "
    "aerobic exposure selects organisms that store phosphorus far in excess of "
    "their needs, so the phosphorus leaves in the sludge rather than in the "
    "water",
    "Chemical precipitation with iron or aluminium salts, which is the reliable "
    "alternative and which produces more sludge and no recoverable product",
    "Struvite crystallisation from digester liquors, which recovers phosphorus "
    "as a usable fertiliser and simultaneously prevents the scaling that the "
    "same chemistry causes inside the pipework",
    # ---- PATHOGENS: a separate objective -----------------------------------------
    "Pathogen reduction by disinfection and by retention in ponds, which is a "
    "distinct unit process rather than a by-product of the biological stages "
    "and which is the objective most directly tied to public health",
    "Water reuse treatment for irrigation and industrial supply, and potable "
    "reuse where the additional physical and chemical barriers are present",
    # ---- SLUDGE: half the cost, and the part nobody sees -------------------------
    "Anaerobic digestion of sludge, which reduces its mass, destroys pathogens "
    "and produces methane that offsets part of the plant's energy demand",
    "Thickening and dewatering, which determine the mass of material that has "
    "to be transported and are therefore the dominant handling cost",
    "Land application of treated biosolids, which returns nitrogen and "
    "phosphorus to soil and simultaneously returns the metals and persistent "
    "chemicals that arrived in the sewage",
    "Incineration and thermal treatment, which destroys organic contaminants "
    "and concentrates metals into ash that must then be disposed of",
)


# =============================================================================
#  TECHNOLOGIES
#  By how the biomass is held, which is the real taxonomy of this engineering.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- biomass in suspension --------------------------------------------------
    "Activated sludge with return of settled biomass, which is the whole "
    "invention: separating solids retention time from hydraulic retention time "
    "so slow-growing organisms can be kept in a fast-flowing system",
    "Sequencing batch reactors, which perform the same sequence of conditions "
    "in time within one tank rather than in space across several",
    "Oxidation ditches and extended aeration, which trade footprint and energy "
    "for stability and a simpler operating regime",
    # ---- biomass fixed on a surface ---------------------------------------------
    "Trickling filters and rotating contactors, where the community grows as a "
    "film on media and the water passes over it",
    "Moving bed and integrated fixed-film systems, which suspend carrier media "
    "in a reactor to add biomass without adding settling duty",
    "Granular sludge processes, in which the biomass self-aggregates into dense "
    "granules that settle rapidly and hold aerobic and anoxic zones within a "
    "single granule",
    # ---- biomass held behind a membrane -----------------------------------------
    "Membrane bioreactors, which remove the settling constraint entirely and "
    "permit very high biomass concentrations at the cost of energy and "
    "membrane fouling",
    "Anaerobic membrane bioreactors, which combine energy recovery with "
    "complete solids retention",
    # ---- controlling which organisms win ------------------------------------------
    "Solids retention time control, which is the primary lever: it decides "
    "whether slow-growing nitrifiers can persist at all",
    "Dissolved oxygen control and aeration management, which is the largest "
    "energy cost in the plant and therefore the largest optimisation target",
    "Anaerobic, anoxic and aerobic zone sequencing, which is how nitrogen and "
    "phosphorus removal are engineered into the same reactor",
    "Real-time sensing and model-based control, including ammonium-based "
    "aeration control that matches air supply to actual load",
    # ---- looking at what is actually growing -------------------------------------
    "Molecular community profiling of the mixed liquor, which turned plant "
    "operation from inference into observation and identified organisms that "
    "had never been cultured",
    "Microscopic examination of floc structure and filament identification, "
    "which remains the fastest practical diagnostic for settling problems",
    # ---- and recovering something from it ------------------------------------------
    "Biogas capture and combined heat and power generation, which is what makes "
    "an energy-neutral works conceivable",
    "Nutrient recovery as struvite and ammonium salts, and polyhydroxyalkanoate "
    "recovery from sludge, which links this record to `white.biopolymers`",
)


# =============================================================================
#  ORGANISMS
#  Almost none of these were ever added to a plant. They arrived and were
#  selected for.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "nitrosomonas_europaea",  # ammonium to nitrite, slow, and lost first
    "nitrobacter_winogradskyi",  # nitrite to nitrate, the second half
    "candidatus_brocadia_anammoxidans",  # ammonium straight to nitrogen gas
    "candidatus_accumulibacter_phosphatis",  # stores phosphorus in excess
    "zoogloea_ramigera",  # floc formation, which is what makes settling work
    "methanosaeta_concilii",  # acetate to methane in the digester
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "respirometry",
    "fluorescence_in_situ_hybridisation",
    "metagenomics",
    "qpcr",
    "process_modelling",
    "online_sensing",
    "microscopy",
    "gas_chromatography",
)


# =============================================================================
#  CHALLENGES
#  Settling first, because it is the failure that shuts a plant down.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the failure that stops everything ---------------------------------------
    "Filamentous bulking, in which filament-forming organisms prevent the "
    "sludge from settling, so biomass leaves with the effluent and the plant "
    "loses the community it depends on, which is the commonest serious "
    "operational failure",
    "Foaming caused by hydrophobic filamentous organisms, which floats biomass "
    "off the surface and is difficult to eliminate once established",
    "Loss of nitrification under cold, overload or toxic conditions, since the "
    "autotrophs grow slowly enough that recovery takes weeks rather than days",
    "Toxic and hydraulic shock loads from industrial discharges, which can kill "
    "the biomass outright and leave reseeding as the only recovery",
    # -- the costs that dominate --------------------------------------------------
    "Aeration energy, which is a substantial share of the electricity use of "
    "many municipalities and is the single largest operating cost",
    "Sludge handling and disposal, commonly around half the cost of running a "
    "works, with no comfortable destination for the material",
    "Metals and persistent organic chemicals accumulating in biosolids, which "
    "constrain land application and are the reason a nutrient resource is "
    "treated as a waste",
    # -- what the process was not designed to remove -------------------------------
    "Pharmaceuticals, hormones and endocrine active compounds passing through "
    "at concentrations sufficient to affect receiving water organisms",
    "Per- and polyfluoroalkyl substances, which resist biological treatment "
    "entirely and require additional physical or chemical stages",
    "Microplastics, which are largely captured into the sludge and therefore "
    "returned to land with it rather than removed from the system",
    "Antibiotic resistance genes, which are concentrated rather than destroyed "
    "in a dense mixed community and are discharged in both effluent and "
    "biosolids",
    # -- the structural problems that are not biological ------------------------------
    "Combined sewer overflows discharging untreated sewage during heavy "
    "rainfall by design, which is a property of old networks rather than a "
    "failure of treatment",
    "Nutrient removal costing considerably more than carbon removal, so it is "
    "the first capability omitted where budgets are constrained",
    "Ageing infrastructure and deferred renewal, which is the commonest reason "
    "a plant underperforms its design",
    "Absence of any treatment for a large share of the world's population, "
    "which is the deepest inequity in this record and is a matter of capital "
    "and governance rather than of technology",
)
