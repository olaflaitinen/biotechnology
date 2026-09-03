# =============================================================================
#  biotechnology.branches.blue.marine_genomics.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by WHAT QUESTION IS BEING ASKED, because marine
#  genomics is a method rather than a product and its applications are
#  otherwise a list of unrelated results. The four questions are: what is
#  there, what is it doing, what can we use, and what is changing.
#
#  ORGANISMS needs a note. The entries below are not production hosts and are
#  not, for the most part, organisms anyone has grown. They are the reference
#  points of the field: two that were invisible until sequencing found them,
#  one whose genome rewrote animal phylogeny, and one whose entire scientific
#  value is that it is a symbiont which cannot be separated from its host.
#  Recording them as organisms is correct and would be misread without this
#  note.
#
#  A NOTE ON WHAT IS ABSENT. The enzymes and molecules that this field's
#  catalogues make findable belong to `blue.marine_enzymes` and
#  `blue.marine_natural_products`. This record is the reading, not the using.
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
#  Grouped by the question being asked.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- what is there? ---------------------------------------------------------
    "Ocean-scale metagenomic surveys that catalogue the genes present in "
    "seawater across depths and latitudes, which multiplied the number of known "
    "protein families several times over",
    "Reconstruction of genomes from metagenomes for organisms that have never "
    "been cultured and may never be",
    "Single-cell genomics of individual sorted cells, which resolves which gene "
    "belongs to which organism where a metagenome cannot",
    "Ribosomal gene surveys for community composition, still the cheapest way "
    "to ask what is present before deciding what to sequence deeply",
    "Reference genome assembly for marine species of scientific, commercial or "
    "conservation interest",
    # -- what is it doing? ------------------------------------------------------
    "Metatranscriptomics and metaproteomics, which distinguish the genes a "
    "community carries from the genes it is actually using",
    "Resolution of host and symbiont genomes in sponges, corals and "
    "chemosynthetic animals, where the biology of interest belongs to the "
    "partnership rather than to either partner",
    "Comparative genomics of adaptation to pressure, cold, darkness and "
    "hypersalinity, which is where the enzymes in `blue.marine_enzymes` are "
    "first identified",
    "Genomic study of coral bleaching and of the algal symbionts whose loss "
    "causes it",
    # -- what can we use? -------------------------------------------------------
    "Biosynthetic gene cluster mining for natural products, which finds the "
    "chemistry a sequence encodes without needing to isolate the compound",
    "Identification of the microbial symbiont that actually produces a "
    "compound attributed to its animal host, which is frequently the route out "
    "of the supply problem described in the branch header",
    "Sequence-based discovery of enzymes with unusual stability, which is what "
    "makes a laboratory reagent out of a deep-sea organism",
    # -- what is changing? ------------------------------------------------------
    "Environmental DNA surveys that detect species present in a water body from "
    "shed traces, without catching, seeing or disturbing them",
    "Invasive species detection in ballast water and in ports, where early "
    "detection is worth more than accurate abundance",
    "Fisheries stock structure and traceability, including identification of "
    "the species actually present in a sold product",
    "Genetic monitoring of populations under exploitation or climate stress",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the order of the workflow, from getting wet to answering.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- collecting, which is the expensive part -------------------------------
    "Research vessel sampling with depth-resolved water bottles and filtration "
    "onto membranes, which is where most of the cost of this field sits",
    "Remotely operated and autonomous vehicles for deep and hazardous sampling",
    "Autonomous samplers and floats that collect and preserve without a ship "
    "present",
    "In situ preservation and cold chain from sample to laboratory, since "
    "nucleic acid degrades before it is analysed",
    # ---- extracting from an unhelpful matrix -------------------------------------
    "Nucleic acid extraction from low-biomass seawater, where the target is "
    "dilute and the volume is large",
    "Extraction from sediment and from calcifying tissue, where inhibitors "
    "co-purify with the nucleic acid and defeat the enzymes used downstream",
    "Whole genome amplification for single cells and for samples below the "
    "input requirement of a sequencer",
    # ---- reading -----------------------------------------------------------------
    "Short-read sequencing for depth and accuracy, and long-read sequencing for "
    "assembly across repeats",
    "Portable nanopore sequencing aboard ship, which removes the delay between "
    "sampling and result",
    "Amplicon sequencing of marker genes for community composition and for "
    "environmental DNA",
    # ---- making sense of it, which is where the difficulty moved -----------------
    "Metagenome assembly and binning into metagenome-assembled genomes",
    "Taxonomic assignment against reference databases, and the honest reporting "
    "of the large fraction that matches nothing",
    "Biosynthetic gene cluster prediction from sequence",
    "Phylogenomic placement of lineages with no cultured representative",
    "Reference barcode library construction, without which environmental DNA "
    "detects an organism it cannot name",
    "Open data deposition, which in this field is unusually consequential "
    "because re-analysis of existing expedition data is cheaper than any new "
    "sampling",
)


# =============================================================================
#  ORGANISMS
#  Reference points of the field, not production hosts. See the module header.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "prochlorococcus_marinus",  # described 1988, among the most abundant on Earth
    "pelagibacter_ubique",  # the most abundant bacterium in the ocean, found by sequence
    "emiliania_huxleyi",  # coccolithophore, blooms visible from orbit
    "amphimedon_queenslandica",  # sponge genome that informed early animal phylogeny
    "symbiodinium_microadriaticum",  # the coral symbiont whose loss is bleaching
    "pyrococcus_furiosus",  # deep-sea hyperthermophile, source of a standard polymerase
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "next_generation_sequencing",
    "metagenomics",
    "pcr",
    "bioinformatics",
    "phylogenetic_analysis",
    "flow_cytometry",
    "environmental_sampling",
    "mass_spectrometry",
)


# =============================================================================
#  CHALLENGES
#  The first is the one that decides what gets studied, and it is not
#  scientific.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the cost that governs the field ----------------------------------------
    "Sampling cost, since ship time, submersibles and deep-sea access cost far "
    "more than the sequencing, which inverts the usual economics of genomics "
    "and means access to a vessel rather than to a sequencer decides what is "
    "studied",
    "Geographic bias in what has been sampled, concentrated near wealthy "
    "countries, convenient ports and existing research stations, so the ocean "
    "is described unevenly rather than representatively",
    # -- the reference problem ---------------------------------------------------
    "Reference database poverty, so a large fraction of marine sequence matches "
    "nothing known and is reported as unidentified rather than as novel",
    "Absence of barcode reference libraries for many taxa, which lets "
    "environmental DNA detect an organism it cannot name",
    # -- the biology that resists ------------------------------------------------
    "The unculturable majority, which can now be sequenced but still cannot be "
    "grown, tested, mutated or asked a question experimentally",
    "Pervasive symbiosis, so a host genome arrives mixed with its microbial "
    "community and separating them is a computational rather than a laboratory "
    "problem",
    "Inhibitors co-purifying from sediment, mucus and calcifying tissue, which "
    "defeat the enzymes used in the next step",
    # -- what the samples are like -----------------------------------------------
    "Low biomass in open ocean water, so large volumes must be filtered to "
    "recover enough nucleic acid",
    "Degradation between sampling and analysis, which the cold chain addresses "
    "and does not eliminate",
    # -- the law ------------------------------------------------------------------
    "The legal position of samples taken beyond national jurisdiction, "
    "unaddressed until 2023 and still settling in practice, which leaves "
    "historical collections in an uncertain position",
    "Access and benefit sharing obligations for samples from within national "
    "waters, which attach to the sequence and not only to the physical sample",
    # -- and what sampling costs the thing sampled ---------------------------------
    "Damage to the habitat being surveyed, particularly where deep-sea sampling "
    "is destructive of slow-growing communities that will not recover within a "
    "human lifetime",
)
