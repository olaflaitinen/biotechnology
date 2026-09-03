# =============================================================================
#  biotechnology.branches.grey.biodiversity_conservation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS ARE GROUPED BY HOW MUCH IS BEING CHANGED, FROM NOTHING UPWARDS.
#
#      KNOW      find out what exists and how it is related
#      KEEP      preserve material against a future without the living animal
#      BREED     move genetic material between animals that cannot meet
#      CHANGE    alter the population, or the genome
#
#  The order matters. The first two groups are uncontroversial, effective and
#  comparatively cheap; the last is where the arguments are. Presenting them
#  in that order shows how much of this field is quiet work and how little of
#  it is what receives attention.
#
#  THE FOURTH GROUP IS LABELLED HONESTLY AND IN PROPORTION. Gene drives have
#  not been deployed in a wild population. No extinct species has been
#  restored. Rule 6 forbids listing aspirations as applications, so these
#  appear with what they actually are stated in the entry, because a reader
#  encountering the coverage these attract deserves to know where they stand
#  rather than to find them silently omitted.
#
#  A DELIBERATE CROSS-REFERENCE. Molecular survey work is summarised here and
#  held in full by `grey.environmental_biomonitoring`, to avoid two records
#  arguing the same evidence.
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
#  By how much is being changed, from nothing upwards.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # ---- KNOW: cheap, effective, and it redirects everything else --------------
    "Population genomic assessment of remaining genetic variation, inbreeding "
    "and effective population size, which establishes how much trouble a "
    "population is in rather than how few animals are visible",
    "Resolution of taxonomic and conservation unit boundaries, which has "
    "repeatedly shown that protected units were defined wrongly and has "
    "redirected effort at very low cost",
    "Species identification from environmental DNA and from seized material, "
    "which is held in full by `grey.environmental_biomonitoring`",
    "Forensic genetics for wildlife trade enforcement, establishing the species "
    "and frequently the source population of confiscated ivory, timber or meat, "
    "which turns a seizure into evidence against a supply route",
    "Pedigree reconstruction and parentage analysis in managed populations, "
    "which is what allows a studbook to be based on actual relatedness rather "
    "than on assumed descent",
    "Detection of hybridisation with domestic or invasive relatives, which is a "
    "quiet and widespread cause of loss that no field observation reveals",
    "Pathogen surveillance in wild populations, including the fungal and viral "
    "diseases that have driven amphibian and bat declines",
    # ---- KEEP: the one intervention that cannot be deferred --------------------
    "Cryopreservation of gametes, embryos, tissue and cell lines in biobanks, "
    "which is the only action here that cannot be performed later, since "
    "material not collected while a population exists cannot be collected "
    "afterwards",
    "Establishment of cultured cell lines from tissue samples, which preserves "
    "a complete genome in a form that can be grown, sequenced and potentially "
    "used decades later",
    "Seed banking and cryopreservation of plant germplasm, including species "
    "whose seeds do not survive conventional drying and freezing",
    "Whole genome sequencing and archiving as a permanent record, which "
    "preserves information rather than material and is therefore not a "
    "substitute for the entries above",
    # ---- BREED: moving material between animals that cannot meet ---------------
    "Artificial insemination in managed populations, which moves genetic "
    "material between institutions without moving the animals and is the "
    "practical form of most studbook management",
    "Embryo transfer and interspecies surrogacy, used where a female of the "
    "target species is unavailable and a close relative can carry the "
    "pregnancy",
    "In vitro fertilisation and embryo production for species reduced to very "
    "few individuals, which is a small number of high-profile programmes and "
    "not a general capability",
    "Genome resource banking integrated with studbook management, which is what "
    "makes a captive population a genetic reservoir rather than a display "
    "collection",
    # ---- CHANGE: where the arguments are ---------------------------------------
    "Genetic rescue by translocating individuals from another population, which "
    "has produced documented recovery from inbreeding depression and which "
    "changes the population it saves",
    "Assisted gene flow and managed relocation ahead of climate change, moving "
    "populations or variants toward conditions they are adapted to, which is "
    "deliberate intervention in a distribution",
    "Breeding for disease resistance in threatened populations, including "
    "resistance to introduced pathogens, which selects on standing variation "
    "rather than introducing anything",
    "Engineering of resistance traits, including work on chestnut blight "
    "resistance in trees, which is genuine, is at the point of regulatory "
    "consideration in specific cases, and is not general practice",
    "Gene drive systems proposed for suppressing invasive rodents and insects "
    "on islands, which are RESEARCH: none has been deployed in a wild "
    "population, and the governance question of an intentionally spreading "
    "genetic element is unresolved",
    "De-extinction and proxy creation, which is recorded as an aspiration "
    "rather than an application, since no extinct species has been restored "
    "and what is conceivable is an existing species edited to carry some traits "
    "of a lost one",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by what each is for. Note how much of the list is preservation and
#  measurement rather than modification.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- reading the population -------------------------------------------------
    "Reduced representation and whole genome sequencing of non-model species, "
    "which is what made population genomics affordable for animals with no "
    "prior genomic resources",
    "Reference genome assembly for threatened species, increasingly through "
    "coordinated sequencing initiatives",
    "Museum and historical specimen sequencing, which recovers the genetic "
    "state of a population before its decline and supplies the baseline no "
    "contemporary sample can",
    "Runs of homozygosity and inbreeding coefficient estimation from genomic "
    "data, which measures inbreeding directly rather than inferring it from a "
    "pedigree",
    "Landscape genomics identifying barriers to gene flow, which locates where "
    "a corridor would actually help",
    # ---- keeping material alive, or keeping it frozen ----------------------------
    "Cryopreservation protocols for sperm, oocytes, embryos and tissue, which "
    "must be developed species by species and exist for a small fraction of "
    "those that need them",
    "Primary cell line establishment and culture from biopsy or post-mortem "
    "tissue, which preserves a viable genome rather than a sample",
    "Induced pluripotent stem cell derivation from preserved cell lines, which "
    "is the route by which banked material might one day produce gametes and "
    "which is demonstrated in very few species",
    "Cryobanking infrastructure, including liquid nitrogen supply, redundancy "
    "and distributed duplicate storage, which is an institutional problem more "
    "than a technical one",
    "Seed banking and cryopreservation for recalcitrant seeds that do not "
    "survive conventional storage",
    # ---- moving genetic material ------------------------------------------------
    "Semen collection, evaluation and artificial insemination protocols, which "
    "are species-specific and unavailable for most taxa",
    "Oestrous synchronisation and reproductive endocrine monitoring, frequently "
    "from faecal hormone metabolites so the animal is not handled",
    "In vitro fertilisation, embryo culture and transfer, including "
    "interspecies surrogacy",
    "Studbook and pedigree management software integrating molecular relatedness "
    "with breeding recommendations across institutions",
    # ---- and the modification tools -----------------------------------------------
    "Genome editing applied to resistance traits, which is at regulatory "
    "consideration in specific tree and amphibian cases",
    "Gene drive construct design and containment strategies, including "
    "self-limiting and reversal systems, which exist because the governance "
    "problem is recognised as unsolved",
    "Cloning by somatic cell nuclear transfer from banked cell lines, which has "
    "produced live animals in a handful of species and has a low success rate",
)


# =============================================================================
#  ORGANISMS
#  Each entry is here because a specific case turned on it.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "puma_concolor_coryi",  # Florida panther, the genetic rescue case
    "ceratotherium_simum_cottoni",  # northern white rhino, assisted reproduction
    "castanea_dentata",  # American chestnut, engineered blight resistance
    "sarcophilus_harrisii",  # Tasmanian devil, transmissible cancer and disease
    "mus_musculus",  # house mouse, the island eradication gene drive target
    "batrachochytrium_dendrobatidis",  # the amphibian pathogen being surveyed
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "dna_sequencing",
    "metabarcoding",
    "qpcr",
    "cryopreservation",
    "cell_culture",
    "genome_editing",
    "somatic_cell_nuclear_transfer",
    "population_genetic_analysis",
)


# =============================================================================
#  CHALLENGES
#  The framing problem first, because it governs how everything else should be
#  read.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the problem these tools do not address --------------------------------
    "Habitat loss, fragmentation and degradation as the principal drivers of "
    "extinction, none of which any technology in this record touches, so the "
    "entire field manages consequences rather than causes",
    "Climate change outpacing the rate at which populations can adapt or move, "
    "which makes some conservation targets unreachable regardless of genetic "
    "management",
    "Risk that a credible promise of reversal reduces the perceived cost of "
    "loss, which is an argument made most forcefully by conservation "
    "biologists about their own field",
    # -- what gets attention, and what does not ---------------------------------
    "Concentration of effort on large vertebrates that attract funding, while "
    "most biodiversity is invertebrate, fungal and microbial and most of it has "
    "never been described",
    "High cost per species, which makes these methods viable for a small "
    "fraction of threatened taxa",
    "Photogenic work attracting support disproportionately, which distorts "
    "priorities toward the visible and away from the numerous",
    # -- the tools do not exist for most species --------------------------------
    "Absence of reproductive biology knowledge for most taxa, so assisted "
    "reproduction succeeds in a small number of species and is unavailable for "
    "the rest",
    "Species-specific cryopreservation protocols, which must be developed "
    "individually and exist for a small fraction of those that need them",
    "Low success rates in cloning and interspecies surrogacy, which makes them "
    "demonstrations rather than tools",
    "Reference genome and database coverage concentrated in well-studied taxa "
    "and regions, so the methods perform worst where biodiversity is greatest",
    # -- the interventions carry their own risks ---------------------------------
    "Outbreeding depression, where introduced individuals bring genes adapted "
    "elsewhere and the cross performs worse than either parent population",
    "Loss of local adaptation and of population identity through genetic "
    "rescue, so the population saved is not the population that was there",
    "Ecological uncertainty in assisted relocation, which introduces a species "
    "to a community that did not previously contain it",
    "Unresolved governance of an intentionally spreading genetic element, since "
    "a gene drive does not respect a property boundary or a national one",
    # -- and the institutions ------------------------------------------------------
    "Biobank dependence on institutional continuity measured in centuries "
    "against funding measured in grant cycles, so material can be lost to a "
    "budget decision rather than to any biological failure",
    "Concentration of genomic expertise and infrastructure in wealthy countries "
    "while biodiversity is concentrated elsewhere, which is the imbalance "
    "access and benefit sharing law exists to address",
    "Permitting complexity for collecting, transporting and storing material "
    "from protected species across jurisdictions",
)
