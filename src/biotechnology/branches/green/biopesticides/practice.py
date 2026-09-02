# =============================================================================
#  biotechnology.branches.green.biopesticides.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications are grouped by MODE OF ACTION rather than by crop, because
#  mode of action determines everything a grower needs to know: how fast it
#  works, whether the pest has to eat it, how narrow it is, and how quickly
#  resistance can arise.
#
#  Note the third group. Mating disruption and mass trapping kill nothing at
#  all; they interfere with the pest finding a mate. It is the only pest
#  control approach in this taxonomy with no dose-response relationship in the
#  usual sense, and it is also the one with the best resistance record, because
#  a moth cannot easily evolve its way out of not finding a female.
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
#  Grouped by mode of action, which is what a grower actually has to reason
#  about.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- must be eaten: gut-active toxins ---------------------------------------
    "Bacillus thuringiensis sprays against lepidopteran caterpillars in "
    "vegetables, orchards and forestry",
    "Bacillus thuringiensis israelensis against mosquito and blackfly larvae, "
    "used in public health vector control as well as agriculture",
    "Baculovirus products against codling moth, armyworm and Spodoptera, often "
    "specific to a single pest species",
    # -- penetrate the cuticle: no ingestion required -----------------------------
    "Beauveria bassiana and Metarhizium against thrips, whitefly and weevils, "
    "which suck sap and would never eat a gut-active toxin",
    "Metarhizium acridum against locusts and grasshoppers in rangeland, where "
    "it is used precisely because it spares other insects",
    "Entomopathogenic nematodes against soil-dwelling larvae such as vine "
    "weevil, where no spray can reach the pest",
    # -- interfere with behaviour: nothing is killed -------------------------------
    "Pheromone mating disruption in orchards and vineyards, which has held "
    "codling moth below threshold for decades without selecting for resistance",
    "Mass trapping and attract-and-kill systems",
    "Push-pull cropping systems that repel a pest from the crop and attract it "
    "to a trap plant",
    # -- occupy the niche or prime the plant ----------------------------------------
    "Trichoderma against soil-borne fungal pathogens, largely by competitive "
    "exclusion in the rhizosphere",
    "Bacillus subtilis and related strains as foliar biofungicides",
    "Plant defence elicitors that prime systemic acquired resistance before "
    "infection",
    # -- release the natural enemy -----------------------------------------------------
    "Augmentative release of predatory mites, parasitic wasps and predatory "
    "bugs in glasshouse tomato, pepper and cucumber, where it is now the "
    "standard system rather than an alternative one",
    "Sterile insect technique against fruit flies and screwworm",
    # -- sequence-based selectivity ------------------------------------------------------
    "RNA interference sprays against Colorado potato beetle, the first "
    "commercial product whose specificity is a DNA sequence rather than a "
    "biochemical property",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the problem each solves: find it, make it, keep it alive on a
#  leaf, and stop resistance arising.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- finding and characterising the agent --------------------------------
    "Microbial strain screening against target and non-target species",
    "Genome sequencing of candidate strains to exclude toxin and virulence "
    "genes that would matter in a vertebrate",
    "Pheromone identification and blend optimisation, since the ratio of "
    "components matters as much as the components",
    # ---- making it -------------------------------------------------------------
    "Submerged fermentation for bacterial actives",
    "Solid-state fermentation for fungal conidia, which do not form well in "
    "liquid culture",
    "In vivo production in host insects for baculoviruses, which cannot be "
    "grown without them",
    "Double-stranded RNA synthesis by bacterial or cell-free production",
    # ---- keeping it alive where it has to work ---------------------------------
    "Formulation with ultraviolet protectants, the single largest determinant "
    "of field persistence",
    "Encapsulation and adjuvants for rainfastness and leaf adhesion",
    "Oil-based formulations for ultra-low-volume application in dry regions",
    "Cold chain and shelf-life management for living products",
    # ---- deciding when to use it ------------------------------------------------
    "Pest population monitoring and economic threshold determination, without "
    "which a slow-acting product is applied too late",
    "Degree-day models to time application to a susceptible life stage",
    # ---- keeping it working -----------------------------------------------------
    "Structured refuge and rotation strategies for resistance management",
    "Non-target and beneficial organism testing to IOBC protocols",
)


# =============================================================================
#  ORGANISMS
#  Note that the last two are not agents but the organisms a product must NOT
#  harm, which is a testing requirement rather than an ingredient.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "bacillus_thuringiensis",  # the largest single product by volume
    "beauveria_bassiana",  # cuticle-penetrating fungus
    "metarhizium_anisopliae",  # locusts, and soil pests
    "trichoderma_harzianum",  # competitive exclusion against soil pathogens
    "steinernema_feltiae",  # entomopathogenic nematode
    "bacillus_subtilis",  # foliar biofungicide
    "apis_mellifera",  # the non-target that defines much of the testing regime
    "phytoseiulus_persimilis",  # predatory mite, the glasshouse workhorse
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "microbial_plate_count",
    "bioassay",
    "pcr",
    "chromatography",
    "microscopy",
    "next_generation_sequencing",
    "field_trial",
)


# =============================================================================
#  CHALLENGES
#  Three technical, then five commercial, regulatory and structural. The
#  weighting is honest: the biology has been understood for decades and the
#  obstacles are almost entirely elsewhere.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the physical constraint -----------------------------------------------
    "Short field persistence, since ultraviolet light, heat and rain degrade a "
    "living or labile active within days, so timing matters more than dose",
    "Slower knockdown than a synthetic insecticide, which is a real agronomic "
    "cost and the most common reason a grower reverts under pressure",
    "Narrow host range, which is the ecological benefit and the commercial "
    "problem in the same property",
    # -- resistance -------------------------------------------------------------
    "Resistance evolution to Bt in intensively treated systems, particularly "
    "where the same protein is deployed both as a spray and in a transgenic "
    "crop across the same landscape",
    # -- the market and the rules -------------------------------------------------
    "Registration dossiers designed for synthetic chemistry, applying data "
    "requirements built for a persistent molecule to an organism that dies in "
    "sunlight, at a cost a single-species market cannot repay",
    "Cold chain and shelf life for living products, which limits distribution "
    "in exactly the hot regions with the highest pest pressure",
    # -- knowledge -----------------------------------------------------------------
    "Higher knowledge requirement, because using these products well means "
    "monitoring pest populations and spraying to a threshold rather than to a "
    "calendar, and advisory capacity is thin in most of the world",
    # -- credibility -----------------------------------------------------------------
    "A market segment that also contains unproven products with vague claims, "
    "which makes it harder for a grower to distinguish a rigorously tested "
    "biological control agent from a bottle of unspecified microbes",
)
