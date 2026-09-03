# =============================================================================
#  biotechnology.branches.yellow.biofortification.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `yellow.food_fermentation` is the edge that most deserves a reader's
#  attention and is the one nobody expects.
#
#  This record raises the iron and zinc CONTENT of a grain. That record
#  degrades the PHYTATE that stops the iron and zinc being absorbed. They
#  address the same deficiency from opposite ends, they are complementary
#  rather than competing, and fermentation requires no new variety, no seed
#  system, no regulatory approval and no donor programme. A household already
#  fermenting its porridge is already doing half of what this record is trying
#  to achieve.
#
#  That is worth stating plainly because this record's own `metrics.py` records
#  the phytate to mineral ratio as the link in the chain most likely to break,
#  and the cheapest intervention against it is a practice that predates all of
#  this by millennia.
#
#  `green.molecular_plant_breeding` supplies the methods, and the distinction
#  is the objective: that record breeds for yield, and this one breeds for a
#  nutrient that a farmer cannot see and does not get paid for. That difference
#  makes yield parity a hard constraint here rather than a target, which is why
#  `metrics.py` opens with the yield penalty.
#
#  `green.agricultural_genome_editing` holds the regulatory divergence that is
#  the most plausible route past this record's twenty-five year obstacle.
#
#  `purple.access_benefit_sharing` binds because conventional biofortification
#  depends entirely on genebank variation collected decades ago, frequently
#  from the same countries the resulting varieties are distributed in.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and this is one of the few records in the library where a broad claim
#  is genuinely earned rather than reached for.
#
#  Goal 2 is claimed on its second target rather than its first. Zero hunger
#  covers malnutrition in all its forms, and micronutrient deficiency is
#  precisely the form that calorie-based measures miss. This record addresses
#  it directly.
#
#  Goal 3 is claimed on documented outcomes: vitamin A deficiency is a leading
#  cause of preventable childhood blindness and increases mortality from
#  ordinary infection, and efficacy trials have measured improvements in status
#  from biofortified crops.
#
#  Goal 1 is claimed because the affected populations are overwhelmingly poor
#  subsistence farmers, and because the delivery argument in `narrative.py` is
#  specifically that this intervention reaches people no supply chain reaches.
#
#  Goal 5 is claimed narrowly: iron deficiency anaemia in women of reproductive
#  age is among the largest deficiency burdens anywhere and contributes to
#  maternal mortality, and the crops here are frequently grown and prepared by
#  women.
#
#  GOAL 12 IS DELIBERATELY NOT CLAIMED. Nothing here reduces resource use;
#  biofortification changes what is in a crop rather than how it is grown.
# =============================================================================
SDGS: Tuple[int, ...] = (
    1,  # No poverty, on reaching subsistence households no supply chain reaches
    2,  # Zero hunger, on malnutrition in the form calorie measures miss
    3,  # Health, on blindness, cognitive development and child mortality
    5,  # Gender equality, on iron deficiency anaemia in women
)


# =============================================================================
#  GLOSSARY
#  Grouped: the problem, the breeding, the nutritional chain, and delivery.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the problem -----------------------------------------------------------
    "micronutrient_deficiency",
    "hidden_hunger",
    "vitamin_a_deficiency",
    "iron_deficiency_anaemia",
    "zinc_deficiency",
    "dietary_diversity",
    "staple_crop",
    # -- the routes ------------------------------------------------------------
    "biofortification",
    "agronomic_biofortification",
    "marker_assisted_selection",
    "genomic_selection",
    "genetic_transformation",
    "genome_editing",
    "germplasm",
    "genebank",
    # -- the nutritional chain -------------------------------------------------
    "bioavailability",
    "phytate",
    "retention",
    "provitamin_a",
    "carotenoid",
    "estimated_average_requirement",
    "nutritional_biomarker",
    # -- getting it to people --------------------------------------------------
    "variety_release",
    "seed_system",
    "participatory_variety_selection",
    "adoption_rate",
    "efficacy_trial",
    "cost_effectiveness",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "harvestplus_biofortification_review",
    "hidden_hunger_global_burden",
    "orange_fleshed_sweet_potato_efficacy",
    "iron_bean_efficacy_trial",
    "zinc_wheat_south_asia",
    "golden_rice_second_generation",
    "golden_rice_philippines_approval",
    "philippines_court_biosafety_ruling",
    "phytate_mineral_bioavailability",
    "biofortification_cost_effectiveness",
)


# =============================================================================
#  RELATED
#  Six edges. The first is the unexpected complement.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same deficiency attacked from the absorption end ------------------
    "yellow.food_fermentation",
    # -- the same methods, a different objective, and yield as a constraint ----
    "green.molecular_plant_breeding",
    # -- the regulatory divergence that may be the route past the obstacle -----
    "green.agricultural_genome_editing",
    # -- the transgenic route, and its twenty-five year history ----------------
    "green.plant_genetic_engineering",
    # -- fortification of the crop against fortification of the diet -----------
    "yellow.nutrigenomics",
    # -- the genebank variation every conventional programme depends on --------
    "purple.access_benefit_sharing",
)
