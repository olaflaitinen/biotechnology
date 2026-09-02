# =============================================================================
#  biotechnology.branches.green.plant_genetic_engineering.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications list is deliberately grouped by WHO BENEFITS, because that
#  grouping makes visible the pattern that most descriptions of this field
#  obscure: the overwhelming majority of deployed hectares carry traits whose
#  benefit accrues to the farmer or the seed company, and the handful of traits
#  aimed at the eater or at a public health problem are the ones that took
#  twenty years or have not arrived.
#
#  That is not an argument against the technology. It is a consequence of the
#  regulatory cost structure named in `narrative.DESCRIPTION`, and stating it
#  as an observation is the honest way to present the list.
#
#  Editorial rule 6 is applied strictly. Golden Rice appears because it has now
#  been approved for cultivation, not because it is frequently discussed.
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
#  Grouped by who benefits. See the header note.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- benefit to the farmer: the overwhelming majority of hectares ---------
    "Bt insect-resistant cotton, maize and aubergine",
    "Glyphosate- and glufosinate-tolerant soybean, maize and canola",
    "Stacked events combining insect resistance and herbicide tolerance",
    "Drought-tolerant maize events for water-limited environments",
    # -- benefit to a whole industry that had no alternative -------------------
    "Virus-resistant papaya, which rescued the Hawaiian crop from ringspot "
    "virus",
    "Virus-resistant summer squash",
    # -- benefit to the processor -----------------------------------------------
    "Low-acrylamide potato, reducing a compound formed during frying",
    "Altered oil-profile soybean giving a more stable frying oil without "
    "hydrogenation",
    # -- benefit to the consumer, rare and slow to arrive ------------------------
    "Non-browning apple, reducing waste from cosmetic rejection",
    "Provitamin-A biofortified rice, approved for cultivation in 2021, "
    "twenty-one years after the prototype",
    # -- benefit outside food entirely --------------------------------------------
    "Plants as production platforms for pharmaceutical proteins",
    "Blue-flowered ornamentals expressing a pathway absent from the species",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped along the workflow: get the DNA in, find the cells that took it,
#  grow a plant, then prove what you made.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- getting the DNA in ---------------------------------------------------
    "Agrobacterium tumefaciens mediated transformation using a disarmed Ti "
    "plasmid",
    "Biolistic particle bombardment with DNA-coated gold or tungsten",
    "Floral dip transformation, which avoids tissue culture entirely in a few "
    "species",
    "Chloroplast transformation, which gives very high expression and maternal "
    "inheritance that limits pollen-mediated spread",
    # ---- controlling where and when it is expressed ----------------------------
    "Constitutive, tissue-specific and inducible promoters",
    "Codon optimisation for plant expression",
    "Matrix attachment regions to reduce position effects",
    # ---- finding the transformed cells -----------------------------------------
    "Antibiotic and herbicide selectable markers",
    "Marker-free systems using co-transformation and segregation, or "
    "site-specific recombinase excision",
    "Visual reporters for non-destructive screening",
    # ---- getting a plant back ---------------------------------------------------
    "Regeneration through tissue culture, the step that limits which genotypes "
    "can be transformed at all",
    "Developmental regulators such as Baby Boom and Wuschel to make "
    "recalcitrant genotypes regenerable",
    # ---- proving what you made ---------------------------------------------------
    "Southern blot and whole-genome sequencing for event characterisation",
    "Junction sequencing across the insertion site",
    "Event-specific detection assays for traceability and labelling compliance",
    "Gene stacking by conventional crossing of separately approved events",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "agrobacterium_tumefaciens",  # the natural genetic engineer, disarmed
    "bacillus_thuringiensis",  # source of the cry genes
    "zea_mays",  # maize, the highest-acreage transgenic crop
    "glycine_max",  # soybean
    "gossypium_hirsutum",  # cotton
    "oryza_sativa",  # rice, including the biofortified event
    "arabidopsis_thaliana",  # the model in which most constructs are first tested
    "carica_papaya",  # the industry saved by a transgenic event
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "plant_transformation",
    "tissue_culture",
    "pcr",
    "next_generation_sequencing",
    "southern_blot",
    "electrophoresis",
    "elisa",
    "phenotyping",
)


# =============================================================================
#  CHALLENGES
#  The first is the binding constraint and is economic. Three are biological,
#  and the rest are structural and social. Editorial rule 7 is comfortably met.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the binding constraint, which is not scientific -----------------------
    "Regulatory cost per event, running into tens of millions of euro, which "
    "excludes minor crops, public-sector breeders and every trait without a "
    "commodity-scale market behind it",
    # -- evolution answers back --------------------------------------------------
    "Evolution of Bt-resistant pest populations where refuge requirements are "
    "not enforced or not practical",
    "Herbicide-resistant weeds selected by the associated weed management "
    "system rather than by the transgene itself",
    # -- the laboratory bottleneck ------------------------------------------------
    "Recalcitrance to regeneration in elite cereal genotypes, so the varieties "
    "farmers actually want are often the hardest to transform",
    # -- coexistence ---------------------------------------------------------------
    "Gene flow to wild relatives and to neighbouring non-GM fields, and the "
    "coexistence rules and buffer distances that follow",
    # -- structural ------------------------------------------------------------------
    "Concentration of germplasm, traits and enabling patents in a handful of "
    "companies, which the regulatory cost structure actively reinforces",
    # -- social -----------------------------------------------------------------------
    "Public acceptance in the European Union and several export markets, which "
    "conditions what can be planted far beyond the countries that reject it",
    "A first product generation offering no benefit a consumer could perceive, "
    "which made the technology easy to characterise as serving only its makers",
)
