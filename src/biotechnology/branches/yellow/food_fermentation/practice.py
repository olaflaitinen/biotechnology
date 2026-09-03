# =============================================================================
#  biotechnology.branches.yellow.food_fermentation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by WHAT THE FERMENTATION IS FOR rather than by
#  product category, because the same organism does different jobs in different
#  foods and grouping by dairy, cereal and vegetable would obscure that. The
#  four groups are the four functions named in `narrative.py`: preserve,
#  transform, make safe, and make good.
#
#  The list is deliberately not confined to European products. Most fermented
#  food is made outside Europe, several of the most interesting processes are
#  African and Asian, and a record that listed cheese, bread, beer and wine
#  would describe a corner of the subject while appearing to describe the
#  subject.
#
#  ORGANISMS are the working organisms, and the note on each says what it does
#  rather than what it is, because in this record the same species appears in
#  foods that have nothing else in common.
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
#  By what the fermentation is for, not by product category.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- to preserve, without refrigeration ------------------------------------
    "Lactic acid vegetable fermentation, including sauerkraut, kimchi and a "
    "great many regional pickles, which keeps a harvest edible through a season "
    "without any cold chain",
    "Fermented dairy products including yoghurt, kefir and cheese, where "
    "acidification and salt together make milk keep",
    "Fermented and cured meat products, where acidification, drying and nitrite "
    "chemistry combine, and where the safety margin is narrower than in any "
    "other group here",
    "Fermented fish and shrimp pastes and sauces, staples across Southeast Asia "
    "and among the oldest continuously made processed foods",
    # -- to transform what the raw material is ----------------------------------
    "Bread and sourdough, where yeast leavens and lactic acid bacteria "
    "contribute acidity, flavour and keeping quality",
    "Soy fermentation into soy sauce, miso, tempeh and natto, which converts a "
    "difficult legume into several entirely different foods",
    "Cocoa and coffee fermentation, which is a required processing step rather "
    "than an optional one, since the flavour precursors of both are generated "
    "by microbes on the farm",
    "Vinegar production by acetic acid bacteria, and the fermented condiments "
    "built on it",
    # -- to make a food safe to eat ----------------------------------------------
    "Cassava fermentation into gari, fufu and related products, which reduces "
    "cyanogenic compounds in a staple crop that is dangerous unprocessed, and "
    "which feeds hundreds of millions of people",
    "Cereal and legume fermentation reducing phytate, which improves the "
    "absorption of iron and zinc from foods that otherwise bind them",
    "Fermentation of grains into weaning foods such as ogi and uji, where "
    "acidification protects an infant food in the absence of refrigeration",
    # -- to make it worth eating ---------------------------------------------------
    "Brewing and winemaking, the largest fermentations in the world by volume "
    "and the ones whose organisms are best characterised",
    "Cheese ripening, where secondary cultures and moulds develop flavour over "
    "months by proteolysis and lipolysis",
    "Distilled spirits, where fermentation supplies the alcohol and the "
    "congeners that survive distillation",
    "Koji cultivation, in which a filamentous fungus supplies the enzymes that "
    "make sake, soy sauce and miso possible and which is a fermentation whose "
    "product is an enzyme preparation rather than a food",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the four things a modern producer actually has to do.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- deciding what does the work -------------------------------------------
    "Defined starter culture selection and propagation, which is what makes the "
    "same product possible twice",
    "Adjunct and secondary cultures added for flavour, texture or ripening "
    "rather than for acidification",
    "Backslopping, carrying a portion of a finished batch into the next, which "
    "is how most traditional fermentation is actually maintained and which "
    "propagates a community rather than a strain",
    "Spontaneous fermentation relying on the organisms present on the raw "
    "material, in the vessel or in the building",
    # ---- keeping the culture working ---------------------------------------------
    "Phage-resistant strain selection and starter rotation, which is the dairy "
    "industry's standing answer to its chronic operational problem",
    "Culture preservation by freeze drying and deep freezing, and the direct-vat "
    "inoculation formats that removed the need for a producer to propagate "
    "cultures themselves",
    "Culture collection maintenance and strain authentication",
    # ---- controlling the process --------------------------------------------------
    "Temperature, pH and salt control, which is how the competition described "
    "in `narrative.ANALOGY` is actually steered",
    "Controlled atmosphere and brine management for vegetable and dairy "
    "fermentations",
    "Endpoint determination by acidity, texture or sensory assessment rather "
    "than by time alone",
    # ---- finding out what is in there -----------------------------------------------
    "Amplicon and shotgun sequencing of fermented food communities, which for "
    "many traditional products revealed for the first time what organisms are "
    "responsible",
    "Metabolomics and volatile analysis linking specific organisms to specific "
    "flavour compounds",
    "Culture-independent monitoring of succession over the course of a "
    "fermentation, which is how a community process becomes describable without "
    "becoming a defined one",
    "Genomic characterisation of starter strains, including their metabolic "
    "capabilities and their phage defence systems",
)


# =============================================================================
#  ORGANISMS
#  What each one does, since the same species appears across unrelated foods.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "saccharomyces_cerevisiae",  # leavens bread and makes beer and wine
    "lactococcus_lactis",  # the dairy acidifier, and the phage industry's target
    "lactiplantibacillus_plantarum",  # the generalist of vegetable fermentation
    "aspergillus_oryzae",  # koji; supplies the enzymes for soy sauce, miso, sake
    "bacillus_subtilis",  # natto and several African alkaline fermentations
    "acetobacter_aceti",  # oxidises ethanol to acetic acid, making vinegar
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "cell_culture",
    "amplicon_sequencing",
    "metagenomics",
    "gas_chromatography",
    "sensory_analysis",
    "ph_measurement",
    "bioassay",
)


# =============================================================================
#  CHALLENGES
#  Phage first, because it is the one that stops production.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- what stops a plant ----------------------------------------------------
    "Bacteriophage infection of dairy starter cultures, which is chronic rather "
    "than exceptional, can idle a plant, and against which the only durable "
    "answers are strain rotation and resistance breeding",
    "Starter culture failure and slow acidification, which in a fermented meat "
    "or dairy product is a food safety event rather than a quality one, since "
    "the acid is the safety barrier",
    # -- the narrow safety margins -----------------------------------------------
    "Mycotoxin and biogenic amine formation by unwanted organisms, particularly "
    "in spontaneous fermentations and in products aged for long periods",
    "Pathogen survival where acidification is too slow or too weak, which is why "
    "fermented meat and raw milk cheese carry tighter controls than their "
    "apparent simplicity suggests",
    "Alcohol and histamine formation in products not intended to contain them",
    # -- what industrialisation costs ----------------------------------------------
    "Loss of microbial diversity as defined starters replace community "
    "fermentations, which narrows both the products and the reservoir of "
    "strains available to improve them",
    "Inability to reproduce a community fermentation from a defined starter, "
    "since the succession of organisms over time is part of what makes the "
    "food",
    "Concentration of starter culture supply in a small number of companies, "
    "leaving producers dependent on a market they cannot influence",
    # -- who owns a food ------------------------------------------------------------
    "Ownership of traditional fermented foods, where characterising a "
    "community's product and selling a defined culture derived from it is "
    "generally lawful and not obviously fair",
    "Protected designation and authenticity requirements, which restrict what "
    "may be called by a traditional name and which cut both ways for the "
    "communities they are meant to protect",
    # -- and what the consumer will accept ---------------------------------------------
    "Consumer expectation of consistency, which pushes producers towards "
    "defined starters and away from the variability that characterised the "
    "products in the first place",
)
