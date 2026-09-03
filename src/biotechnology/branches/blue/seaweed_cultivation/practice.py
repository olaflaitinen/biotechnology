# =============================================================================
#  biotechnology.branches.blue.seaweed_cultivation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by the two industries that sit under this heading,
#  because they are genuinely separate: different species, different regions,
#  different buyers and different economics. Food comes first because it is the
#  larger tonnage; hydrocolloids second because they are the larger presence in
#  the daily life of a reader who has never eaten seaweed knowingly.
#
#  The later groups are the proposed uses, and they are labelled as proposals
#  where that is what they are. This matters in a record where enthusiasm runs
#  ahead of evidence, particularly on climate.
#
#  ORGANISMS are cultivated species. The note on each gives what it is grown
#  for and where, since the sector is geographically concentrated in a way that
#  a bare species list would hide.
#
#  A NOTE ON WHAT IS ABSENT. The enzymes that degrade these polysaccharides are
#  `blue.marine_enzymes`. The extracted polymers as materials are
#  `blue.marine_biomaterials`. This record is the farming and the primary
#  processing.
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
#  Two established industries first, then the proposals labelled as proposals.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- industry one: food, and the largest tonnage ---------------------------
    "Cultivation of kelp and related species as a staple food, eaten directly "
    "and in very large quantity across East Asia",
    "Nori production for sheet seaweed, an intensive and highly developed "
    "cultivation with its own hatchery technology",
    "Sea grapes, wakame and other regional food species grown on established "
    "coastal systems",
    "Seaweed as a salt replacement and as an umami ingredient in processed "
    "food, which is a small volume with an outsized nutritional argument",
    # -- industry two: hydrocolloids, present in most kitchens unnoticed --------
    "Agar extraction for food gelling and, decisively, for microbiological "
    "culture media, which is a small tonnage on which an entire scientific "
    "discipline depends",
    "Carrageenan extraction for dairy, meat and plant-based products, where it "
    "stabilises emulsions and prevents separation",
    "Alginate extraction for food thickening, pharmaceutical formulation, wound "
    "dressings and dental impression materials",
    "Seaweed extracts for cosmetics, where the marine origin is part of what is "
    "sold",
    # -- agriculture and animal feed ---------------------------------------------
    "Seaweed extracts as plant biostimulants, which is a long-established use "
    "with a mixed evidence base and a large market",
    "Seaweed meal as a feed supplement in livestock and aquaculture diets",
    "Red seaweed supplementation investigated for reducing enteric methane "
    "production in ruminants, promising in trials and constrained by supply, "
    "consistency and questions about the active compound",
    # -- services rather than products --------------------------------------------
    "Integrated multi-trophic aquaculture, where seaweed grown beside fed fish "
    "takes up dissolved nitrogen and phosphorus, which is where its nutrient "
    "removal is most clearly valuable",
    "Bioremediation of eutrophied coastal water, where the crop is a nutrient "
    "extraction service and the biomass is a by-product",
    # -- proposals, labelled as proposals ------------------------------------------
    "Seaweed as a feedstock for fuels and biobased chemicals, technically "
    "workable and economically difficult for the reasons `white.biofuels` sets "
    "out, with the additional problem of high ash and salt content",
    "Cultivation proposed for carbon sequestration, which is the weakest claim "
    "in this record, since carbon in a crop that is eaten or processed returns "
    "to the atmosphere and only a mechanism for durable storage would change "
    "that",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the crop cycle: start it, grow it, take it, process it. The
#  hatchery group is where the actual biotechnology sits.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- starting the crop, which is where the science is ---------------------
    "Hatchery production of seed strings, in which spores are settled onto twine "
    "under controlled conditions before being taken to sea",
    "Life cycle control across the alternation of generations, which for kelps "
    "means managing a microscopic gametophyte stage that bears no resemblance "
    "to the harvested plant",
    "Gametophyte culture and cryopreservation, which allows a strain to be kept, "
    "shared and reseeded without maintaining live stock continuously",
    "Selective breeding and hybrid production, which is far less developed than "
    "in terrestrial crops and is where the sector's largest genetic gains "
    "remain available",
    "Vegetative propagation from cuttings, cheap and universal in the tropical "
    "carrageenan crops, and the direct cause of their genetic narrowness",
    # ---- growing it ------------------------------------------------------------
    "Long-line and raft cultivation systems in sheltered coastal water",
    "Off-bottom and floating line methods for tropical species, which need "
    "little capital and a great deal of labour",
    "Offshore and submersible systems designed to survive exposed conditions, "
    "which is the direction European cultivation has taken and which changes "
    "the capital requirement completely",
    "Site selection by nutrient availability, current, temperature and depth, "
    "which decides yield more than any husbandry decision",
    # ---- taking it -------------------------------------------------------------
    "Manual harvesting, which remains the dominant method worldwide and is why "
    "production sits where labour is available",
    "Mechanical harvesting for long-line systems, which is what would be needed "
    "for the sector to expand into high-wage economies",
    "Post-harvest handling, since wet seaweed degrades within hours and the "
    "distance to processing is a real constraint on where farms can be",
    # ---- processing it ----------------------------------------------------------
    "Sun drying and mechanical drying, the first cheap and weather-dependent, "
    "the second the largest energy cost in the chain",
    "Alkaline and hot water extraction of hydrocolloids, followed by "
    "precipitation and milling",
    "Enzymatic processing using the polysaccharide-degrading enzymes recorded "
    "in `blue.marine_enzymes`, which allows milder conditions and defined "
    "oligosaccharide products",
    "Biorefinery fractionation recovering protein, polysaccharide and mineral "
    "streams from one crop, proposed widely and implemented rarely",
)


# =============================================================================
#  ORGANISMS
#  Cultivated species, with what and where.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "saccharina_japonica",  # kelp, food and alginate, the largest single tonnage
    "pyropia_yezoensis",  # nori, intensive cultivation with hatchery technology
    "undaria_pinnatifida",  # wakame, food, and invasive well outside its range
    "kappaphycus_alvarezii",  # tropical carrageenan crop, vegetatively propagated
    "gracilaria_gracilis",  # agar source, and used in nutrient bioremediation
    "asparagopsis_taxiformis",  # investigated for ruminant methane reduction
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "hatchery_culture",
    "selective_breeding",
    "cryopreservation",
    "solvent_extraction",
    "enzymatic_hydrolysis",
    "chromatography",
    "environmental_monitoring",
    "life_cycle_assessment",
)


# =============================================================================
#  CHALLENGES
#  Biological and social rather than technical, which is the honest ordering.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- what destroys a crop --------------------------------------------------
    "Disease and epiphyte outbreaks, including ice-ice disease and epiphytic "
    "infestation, which spread rapidly through clonal monocultures and have "
    "collapsed regional industries within a single season",
    "Genetic narrowness from decades of vegetative propagation, which leaves "
    "major crops with little capacity to respond to a new pathogen or to "
    "warming water",
    "Marine heatwaves and rising sea temperature, which are outside a farmer's "
    "control and shift where a species can be grown at all",
    # -- who else wants the water ------------------------------------------------
    "Competition for coastal space with fishing, shipping, tourism and "
    "conservation designation, in a setting where property rights are usually "
    "weaker and more contested than on land",
    "Licensing and consenting timelines in jurisdictions without an established "
    "framework, which is the principal barrier to European and North American "
    "expansion rather than any biological difficulty",
    "Habitat effects of farm structures, including shading of the seabed and "
    "alteration of local currents",
    "Escape and invasiveness of cultivated species outside their native range",
    # -- what is in the crop -------------------------------------------------------
    "Heavy metal and arsenic accumulation, since the crop concentrates whatever "
    "the water contains and cannot be sited away from a polluted coast without "
    "moving the farm",
    "Very high iodine content in some species, which is a genuine food safety "
    "limit on how much can be eaten rather than a theoretical concern",
    # -- the economics --------------------------------------------------------------
    "Labour intensity of seeding and harvesting, which sustains the industry "
    "where labour is available and prevents it establishing where labour is "
    "expensive",
    "Drying energy and rapid post-harvest degradation, which together restrict "
    "how far a farm can be from processing",
    "Price volatility in hydrocolloid markets, which passes directly to "
    "smallholder farmers who have no other buyer",
    # -- the claims ------------------------------------------------------------------
    "Overstated carbon sequestration claims, since carbon in a crop that is "
    "eaten or processed returns to the atmosphere, and conflating cultivation "
    "with durable storage undermines the sector's genuine and defensible "
    "environmental arguments",
)
