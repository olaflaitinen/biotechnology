# =============================================================================
#  biotechnology.branches.blue.algal_biotechnology.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped BY PRODUCT VALUE PER TONNE, from the most valuable
#  downwards, because that ordering is the record's argument. The harvest cost
#  described in `narrative.py` is roughly the same whatever is being grown, so
#  value per tonne alone decides whether an application is a business. A reader
#  moving down this list is watching the economics deteriorate, and the fuel
#  entries at the bottom are where they stop working.
#
#  This grouping also makes an editorial point that a therapeutic-area or
#  organism-based grouping would hide: the successful applications and the
#  failed ones use the SAME organisms, the SAME ponds and the SAME harvesting
#  equipment. Nothing technical separates them.
#
#  ORGANISMS are production species, and each entry notes the property that
#  makes it usable at scale, which is usually a defence against contamination
#  rather than productivity.
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
#  Ordered by product value per tonne, highest first. Watch the economics fail.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- very high value: harvest cost is a rounding error ----------------------
    "Astaxanthin from Haematococcus for pigmentation and as an antioxidant, "
    "among the most valuable products in this record and the reason "
    "photobioreactors can be justified at all",
    "Phycocyanin and phycoerythrin as natural colourants and as fluorescent "
    "labels in diagnostics, where the fluorescence application commands "
    "laboratory reagent prices",
    "Beta-carotene from Dunaliella grown in hypersaline ponds, one of the "
    "oldest commercial algal products",
    "Isotopically labelled biomass and speciality biochemicals for research use",
    # -- high value: works, at scale, profitably --------------------------------
    "Long-chain omega-3 fatty acids from marine microalgae, which supply the "
    "compound directly rather than through the fish that concentrate it, "
    "serving both a fishery under pressure and consumers who eat no fish",
    "Algal oils as an ingredient in infant formula, where regulatory acceptance "
    "and price both favour a controlled source",
    "Feed ingredients for aquaculture, including the pigment that makes farmed "
    "salmon pink and the live microalgal feeds that hatcheries in "
    "`blue.aquaculture_biotechnology` cannot operate without",
    # -- moderate value: works, on volume and with a story -----------------------
    "Spirulina and chlorella as protein and nutritional supplements, grown for "
    "decades without arable land or fresh water",
    "Whole algal biomass as a protein ingredient in food manufacture, "
    "overlapping with `yellow.alternative_proteins`",
    "Cosmetic ingredients, including extracts sold for their marine origin as "
    "much as for a demonstrated effect",
    # -- services rather than products, where somebody else pays -----------------
    "Wastewater treatment coupled to biomass production, where the value is the "
    "treatment and the biomass is a by-product, which inverts the economics "
    "favourably",
    "Carbon dioxide capture from industrial flue gas into biomass, useful where "
    "an emitter pays for the service and marginal where the biomass must carry "
    "the cost",
    # -- low value: the same technology, and it does not pay ---------------------
    "Biofertiliser and soil amendment from algal biomass",
    "Biogas from algal biomass by anaerobic digestion, which avoids the drying "
    "step and therefore avoids part of the harvest cost",
    "Algal biodiesel and hydrocarbon fuels, which absorbed substantial "
    "investment in the late 2000s and did not become commercial, for the reason "
    "this list is ordered to demonstrate",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the four problems: grow it, keep it, get it out, open it up.
#  The third group is the largest, which is the honest proportion.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- growing it -----------------------------------------------------------
    "Open raceway ponds with paddlewheel mixing, cheap to build and operate and "
    "open to whatever arrives",
    "Closed tubular and flat-panel photobioreactors, which give species purity "
    "and higher density at a capital cost only a valuable product can carry",
    "Hybrid systems using a closed reactor for inoculum and a pond for bulk "
    "growth, which is how several commercial operations actually run",
    "Heterotrophic fermentation in the dark on organic carbon, which abandons "
    "photosynthesis entirely, reaches far higher densities, and is how much "
    "commercial algal oil is really made",
    "Light management by mixing, path length and dilution, since a dense "
    "culture shades itself within centimetres and a reactor cannot be made "
    "deeper",
    "Extremophilic cultivation at high pH or high salinity, which builds a "
    "chemical moat that competitors cannot cross",
    # ---- keeping it -----------------------------------------------------------
    "Contamination and grazer monitoring, since a rotifer bloom can clear a "
    "pond within days",
    "Strain selection and adaptive laboratory evolution for robustness rather "
    "than for peak productivity, which is usually the better trade outdoors",
    "Nutrient limitation strategies that trigger lipid or pigment accumulation, "
    "exploiting the fact that stressed cells store rather than divide",
    # ---- getting it out of the water, which is where the money goes -------------
    "Centrifugation, effective and energy-intensive",
    "Flocculation and coagulation, much cheaper and leaving the flocculant in "
    "the product",
    "Dissolved air flotation and gravity settling for species that will "
    "cooperate",
    "Membrane filtration, which works and fouls",
    "Dewatering and drying, including spray and drum drying, which is a further "
    "large energy demand after the water has already been mostly removed",
    # ---- opening the cell ------------------------------------------------------
    "Cell disruption by bead milling, high pressure homogenisation or enzymatic "
    "lysis, necessary because many algal walls resist extraction",
    "Solvent and supercritical carbon dioxide extraction for lipids and "
    "pigments",
    "Biorefinery fractionation recovering several products from one biomass, "
    "which is the standing proposal for making low-value products viable and "
    "which adds complexity faster than it adds revenue",
)


# =============================================================================
#  ORGANISMS
#  Production species. The note gives the property that makes each usable.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "arthrospira_platensis",  # spirulina; grows at high pH, so few competitors follow
    "chlorella_vulgaris",  # robust, fast, and grows heterotrophically in the dark
    "dunaliella_salina",  # hypersaline tolerance is its moat; beta-carotene
    "haematococcus_pluvialis",  # astaxanthin; slow and fragile, hence photobioreactors
    "nannochloropsis_gaditana",  # marine, high lipid, a standard omega-3 organism
    "chlamydomonas_reinhardtii",  # the genetic model rather than a production species
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "cell_culture",
    "photobioreactor_cultivation",
    "centrifugation",
    "solvent_extraction",
    "chromatography",
    "flow_cytometry",
    "life_cycle_assessment",
    "genome_editing",
)


# =============================================================================
#  CHALLENGES
#  Harvest first, because it decides which applications exist.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the constraint that governs the economics ------------------------------
    "Harvest and dewatering energy, since a culture at about a gram per litre "
    "means separating a tonne of biomass from roughly a thousand tonnes of "
    "water, which is fatal to any low-value product and irrelevant to a "
    "valuable one",
    "Cell disruption cost, because many algal cell walls resist extraction and "
    "the biomass must be opened before anything can be recovered from it",
    # -- the physics of light -----------------------------------------------------
    "Light penetration, since a dense culture shades itself within centimetres "
    "and a photobioreactor cannot be scaled by making it deeper",
    "Photoinhibition and the mismatch between full sunlight and what a cell can "
    "use, so much of the incident light is wasted or damaging",
    "Seasonal and diurnal variation in output, which no outdoor system escapes "
    "and which forces either oversized capacity or interrupted supply",
    # -- what happens in an open system --------------------------------------------
    "Contamination by unwanted algae, bacteria and grazing rotifers, which can "
    "clear an open pond within days and is the reason successful open-pond "
    "species are those with an extremophilic defence",
    "Strain stability outdoors, where a laboratory-optimised high performer is "
    "frequently outcompeted by a hardier organism",
    # -- resources -------------------------------------------------------------------
    "Water use and evaporative loss in open systems, which is substantial even "
    "though the water may be saline or waste",
    "Nutrient demand, particularly nitrogen and phosphorus, whose production "
    "carries a footprint that a life cycle assessment must count against the "
    "biomass",
    "Carbon dioxide supply and delivery, since ambient air cannot sustain a "
    "dense culture and concentrated supply must come from somewhere",
    # -- the claims -------------------------------------------------------------------
    "Extrapolation of laboratory productivity to open systems, which was the "
    "specific error behind the fuel programmes of the late 2000s and which "
    "reappears whenever a new application is proposed",
    "Regulatory acceptance for novel species in food, where a new organism "
    "requires authorisation that the established few already hold",
)
