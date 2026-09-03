# =============================================================================
#  biotechnology.branches.blue.seaweed_cultivation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The edge to `blue.algal_biotechnology` is reciprocal and the boundary is
#  drawn at the organism rather than the application, because that is where the
#  economics actually diverge.
#
#      microalgae   single cells in dilute suspension. Harvest dominates the
#                   economics, and the record opens with culture density.
#                   Grown in vessels. SCALE = INDUSTRIAL.
#      macroalgae   large plants on ropes, lifted out of the sea. The harvest
#                   constraint does not exist. Grown in a place.
#                   SCALE = FIELD.
#
#  One difference in organism size produces two entirely different industries,
#  one at tens of millions of tonnes and one at tens of thousands. A reader who
#  follows this edge should come away understanding why.
#
#  `green.molecular_plant_breeding` is the edge this record most needs and is
#  the one a reader is least likely to expect. Seaweed breeding is decades
#  behind terrestrial crop breeding, and the vulnerability recorded in
#  `history.py` is precisely what a terrestrial breeding programme exists to
#  prevent. The effective population size metric in this record is the same one
#  `green.animal_biotechnology` uses for livestock breeds, and it is low here
#  for the same reason: propagation from a narrow founding stock.
#
#  `grey.wastewater_treatment` carries the nutrient removal service, which is
#  this record's most defensible environmental claim and which is worth more
#  where somebody pays for the treatment than where the biomass must carry the
#  cost.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Five, which is more than most records in this library claim, and each is
#  defensible for a specific reason rather than by association.
#
#  Goal 1 and Goal 5 are unusual and are claimed deliberately. This sector
#  supports very large numbers of coastal households in regions with few
#  alternatives, and in several of the largest producing countries seaweed
#  farming is work that women do and control, in settings where other income is
#  difficult for them to access. It is a livelihood claim rather than a
#  technology claim, and it is the honest reason this sector matters to the
#  people in it.
#
#  Goal 14 is claimed on nutrient removal, which is measurable and real, and
#  NOT on carbon sequestration, which `metrics.py` and `history.py` both record
#  as unsupported for a crop that is eaten or processed.
#
#  GOAL 13 IS DELIBERATELY NOT CLAIMED. Climate action is the claim most often
#  made for this sector and the one it cannot support: carbon fixed in a
#  harvested crop returns to the atmosphere within months. The methane
#  reduction application might eventually justify it; it does not yet.
# =============================================================================
SDGS: Tuple[int, ...] = (
    1,  # No poverty, on coastal livelihoods where alternatives are few
    2,  # Zero hunger, on food grown without land, fresh water or fertiliser
    5,  # Gender equality, on work that women do and control in the sector
    12,  # Responsible production, on a crop requiring no inputs
    14,  # Life below water, on nutrient removal rather than on carbon
)


# =============================================================================
#  GLOSSARY
#  Grouped: the crop, how it is farmed, what is extracted, and what goes wrong.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the crop --------------------------------------------------------------
    "macroalgae",
    "seaweed",
    "kelp",
    "nori",
    "thallus",
    "gametophyte",
    "sporophyte",
    "alternation_of_generations",
    "conchocelis",
    # -- how it is farmed ------------------------------------------------------
    "seed_string",
    "long_line_cultivation",
    "off_bottom_cultivation",
    "vegetative_propagation",
    "integrated_multi_trophic_aquaculture",
    "marine_spatial_planning",
    # -- what is extracted -----------------------------------------------------
    "hydrocolloid",
    "agar",
    "carrageenan",
    "alginate",
    "gel_strength",
    "biostimulant",
    # -- what goes wrong -------------------------------------------------------
    "ice_ice_disease",
    "epiphyte",
    "effective_population_size",
    "marine_heatwave",
    "bioaccumulation",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "fao_seaweed_production_review",
    "drew_baker_conchocelis",
    "nori_cultivation_history",
    "carrageenan_seaweed_disease_review",
    "seaweed_hydrocolloid_industry_review",
    "imta_commercial_assessment",
    "seaweed_carbon_sequestration_critique",
    "asparagopsis_methane_trials",
    "seaweed_iodine_food_safety",
    "seaweed_genetic_diversity_review",
)


# =============================================================================
#  RELATED
#  Six edges. The first is the boundary that explains both records.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- microalgae, where the harvest constraint governs everything -----------
    "blue.algal_biotechnology",
    # -- the extracted polymers as materials -----------------------------------
    "blue.marine_biomaterials",
    # -- the enzymes that process these polysaccharides ------------------------
    "blue.marine_enzymes",
    # -- grown beside fed fish, taking up their dissolved waste ----------------
    "blue.aquaculture_biotechnology",
    # -- the breeding programme this crop has never had ------------------------
    "green.molecular_plant_breeding",
    # -- nutrient removal, where somebody else pays for the service ------------
    "grey.wastewater_treatment",
)
