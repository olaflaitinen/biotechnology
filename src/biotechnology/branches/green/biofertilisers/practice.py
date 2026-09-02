# =============================================================================
#  biotechnology.branches.green.biofertilisers.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications are grouped by FUNCTIONAL GROUP, because that is what
#  determines both the expected effect size and how reliable it is. Symbiotic
#  nitrogen fixation in legumes is the one part of this field with effects
#  large enough and consistent enough that nobody argues about them. Everything
#  below it in the list is progressively more variable, and the record says so
#  rather than presenting the whole category as equally established.
#
#  Editorial rule 6 is applied strictly here, because this is a field with a
#  great deal of promotional literature. Every entry names a use with a
#  commercial product and a field evidence base behind it.
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
#  Ordered by how well established the effect is, most established first.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- the part nobody argues about ------------------------------------------
    "Rhizobium and Bradyrhizobium seed inoculation of soybean, which is "
    "standard practice across the Americas and is the largest single use of "
    "any biofertiliser",
    "Inoculation of chickpea, lentil, groundnut and common bean, where the "
    "correct rhizobial partner is species-specific and often absent from soils "
    "that have not grown that legume before",
    "First-time introduction of a legume to a new region, where inoculation is "
    "not an improvement but a precondition for the crop growing at all",
    # -- well established in the right soils -------------------------------------
    "Arbuscular mycorrhizal inoculation of orchards, vineyards and nursery "
    "transplants, where the disturbance of transplanting has removed the native "
    "fungal network",
    "Mycorrhizal inoculation in phosphorus-poor and degraded soils, where the "
    "hyphal network reaches phosphate the root cannot",
    # -- real but more variable ---------------------------------------------------
    "Phosphate-solubilising bacteria in soils where phosphorus is abundant but "
    "chemically locked to calcium, iron or aluminium",
    "Azospirillum inoculation of maize, wheat and forage grasses, where the "
    "measured effect is often growth promotion by hormone production rather "
    "than nitrogen fixation",
    # -- combinations and delivery ------------------------------------------------
    "Consortium products combining fixers, solubilisers and biocontrol strains",
    "Seed coating and pelleting for mechanised sowing, which is how most "
    "inoculant now reaches the field",
    "Fertigation and in-furrow liquid application in irrigated systems",
    # -- beyond the field ----------------------------------------------------------
    "Biofertiliser use in organic and low-input farming systems, where synthetic "
    "nitrogen is not permitted",
    "Reintroduction of soil microbial communities during land restoration",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped along the product path: pick the strain, grow it, formulate it, get
#  it onto the seed, and prove it worked.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- picking the strain --------------------------------------------------
    "Strain screening for competitiveness against the native population, which "
    "matters more than fixation rate in pure culture",
    "Rhizosphere microbiome profiling by amplicon sequencing to characterise "
    "what the inoculant will be competing with",
    "nif, nod and fix gene characterisation",
    "Host specificity testing, since a rhizobial strain effective on one legume "
    "may nodulate another without fixing anything",
    # ---- growing it ------------------------------------------------------------
    "Submerged fermentation to high cell density",
    "Trap culture and in vitro root organ culture for arbuscular mycorrhizal "
    "fungi, which cannot be grown without a host",
    # ---- formulating it ---------------------------------------------------------
    "Carrier-based formulation in sterilised peat, vermiculite, biochar or "
    "lignite",
    "Liquid formulations with osmoprotectants and cell-protective polymers",
    "Freeze-drying and encapsulation in alginate or polymer beads",
    "Shelf-life and viability testing by plate count under accelerated "
    "conditions",
    # ---- getting it onto the seed ------------------------------------------------
    "On-seed polymer coating compatible with mechanised sowing",
    "Compatibility testing against seed treatment fungicides and insecticides, "
    "which routinely kill the inoculant",
    # ---- proving it worked ---------------------------------------------------------
    "Nodule counting and acetylene reduction assay",
    "Nitrogen isotope dilution and natural abundance methods to quantify how "
    "much nitrogen actually came from the atmosphere",
    "Strain-specific markers to confirm the nodules were formed by the "
    "inoculant rather than by the native population",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "rhizobium_leguminosarum",  # pea, bean, clover and lentil symbiont
    "bradyrhizobium_japonicum",  # the soybean symbiont, the largest use by volume
    "azospirillum_brasilense",  # associative, cereals and grasses
    "azotobacter_chroococcum",  # free-living fixer
    "rhizophagus_irregularis",  # the workhorse arbuscular mycorrhizal fungus
    "bacillus_subtilis",  # growth promotion and phosphate solubilisation
    "glycine_max",  # soybean, the host that defines the market
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "microbial_plate_count",
    "amplicon_sequencing",
    "pcr",
    "microscopy",
    "isotope_analysis",
    "soil_analysis",
)


# =============================================================================
#  CHALLENGES
#  The first is the binding constraint. The fourth is the one that has done the
#  most commercial damage and is not a scientific problem at all.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the binding constraint -------------------------------------------------
    "Establishment against an incumbent native community that is adapted to "
    "that soil and vastly outnumbers the inoculant, which is why glasshouse "
    "results routinely fail to replicate in the field",
    # -- keeping a living product alive -------------------------------------------
    "Survival through formulation, storage, heat and sowing, with shelf life "
    "measured in months rather than years and viability falling throughout",
    "Incompatibility with seed treatment fungicides and insecticides applied to "
    "the same seed, which frequently kill the inoculant before it reaches soil",
    # -- the market ---------------------------------------------------------------
    "Product quality in markets where enforcement is weak, where independent "
    "testing has repeatedly found far fewer viable cells than labelled, the "
    "wrong organism, or nothing living at all, which has damaged the "
    "credibility of the whole category",
    # -- proving it -----------------------------------------------------------------
    "Demonstrating efficacy to a regulatory standard, since the effect is "
    "conditional on soil type, season, native population and host genotype, and "
    "a trial that shows nothing may mean the soil already had what the product "
    "supplies",
    # -- the fifty-year goal --------------------------------------------------------
    "Nitrogen fixation remains largely confined to legumes, and transferring it "
    "to cereals, whether by engineering the symbiosis or the nitrogenase "
    "pathway itself, has been an active goal since the 1970s without arriving",
    # -- knowing what is in the soil already ------------------------------------------
    "No routine field test tells a farmer whether the native population already "
    "provides the function, so inoculant is often applied where it cannot help",
)
