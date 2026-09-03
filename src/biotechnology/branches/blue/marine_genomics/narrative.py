# =============================================================================
#  biotechnology.branches.blue.marine_genomics.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The organising fact of this record is that MOST MARINE MICROORGANISMS CANNOT
#  BE GROWN. For most of the twentieth century, studying a microbe meant
#  culturing it, and the fraction of marine microbes that will grow on a plate
#  is somewhere around one per cent. Everything else was invisible, not because
#  it was rare but because the method could not see it.
#
#  Sequencing removed the requirement to culture, and the result was not a
#  refinement of the existing picture but its replacement. An entire abundant
#  lineage of marine archaea had been missed. The most numerous photosynthetic
#  organism on the planet was described only in 1988. A single expedition
#  multiplied the count of known genes several times over.
#
#  This is therefore a record about a METHOD that changed what was known to
#  exist, and the narrative is built on that rather than on applications.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

__all__ = [
    "SUMMARY",
    "DESCRIPTION",
    "PLAIN_LANGUAGE",
    "ANALOGY",
    "WHY_IT_MATTERS",
]


# =============================================================================
#  TECHNICAL REGISTER
# =============================================================================

SUMMARY = (
    "Sequencing and analysing the genomes of marine organisms and communities, "
    "including the great majority that cannot be cultured."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the culture problem and what removing it revealed, (b) what
#  the field actually does, (c) why the sea is a distinct sequencing problem,
#  (d) the binding constraints.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the culture problem
    "Marine genomics reads the genetic material of marine organisms and, more "
    "consequentially, of whole marine communities without isolating their "
    "members first. The distinction matters because only a small minority of "
    "marine microorganisms will grow in laboratory culture, so for most of the "
    "history of microbiology the marine microbial world was described from the "
    "unrepresentative fraction that happened to be cultivable. Sequencing DNA "
    "extracted directly from seawater removed that requirement and did not "
    "refine the existing picture so much as replace it: abundant lineages that "
    "no survey had recorded turned out to dominate whole water columns. "
    # (b) what the field does
    "Practice spans four scales. Single-organism genomics assembles reference "
    "genomes for species of scientific or commercial interest. Metagenomics "
    "sequences everything in a water or sediment sample together and "
    "reconstructs the genomes present computationally. Metatranscriptomics and "
    "single-cell genomics ask what is being expressed and what belongs to which "
    "cell, since a metagenome alone cannot always say which gene sits in which "
    "organism. Environmental DNA surveys detect the species present in a body "
    "of water from the traces they shed, which turns a genetic method into a "
    "monitoring tool for animals nobody has seen. "
    # (c) why the sea is different
    "Three features make marine sequencing a distinct problem rather than an "
    "application of the general method. Reference databases are poor, because "
    "marine lineages are under-represented, so a large fraction of marine "
    "sequence matches nothing known and is reported as dark matter. Symbiosis "
    "is pervasive, so a sponge genome arrives mixed with the genomes of the "
    "microbial community inside it, and separating them is a computational "
    "problem rather than a laboratory one. And sampling is expensive and "
    "sparse, since ship time and submersibles cost more than any sequencing, "
    "which inverts the usual economics of genomics. "
    # (d) the constraints
    "The binding constraints are therefore sampling cost, reference database "
    "poverty, and the legal position of samples taken outside national waters, "
    "which was unresolved until very recently and remains unsettled in "
    "practice. None of the three is a sequencing problem, and none is solved by "
    "sequencing more."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Almost everything we knew about life in the sea used to come from what we "
    "could catch and keep alive. That turns out to be a very small and very "
    "misleading sample: fewer than one in a hundred ocean microbes will grow in "
    "a laboratory. Reading DNA directly from a bucket of seawater removed that "
    "limit, and what appeared was not a few extra species but whole groups of "
    "organisms nobody knew existed, some of them among the most abundant living "
    "things on Earth. The same trick now identifies which fish are in a river "
    "from the traces they leave in the water, without catching or even seeing "
    "them."
)

# -----------------------------------------------------------------------------
#  The streetlight analogy. Chosen because the culture bias is precisely a
#  search-where-the-light-is problem, and because the analogy's own limit,
#  that the searcher at least knew the light was there, is the useful part:
#  microbiologists did not know the culturable fraction was unrepresentative.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is the old story of looking for keys under the streetlight, with one "
    "difference that matters. The man in the story knows the light is only "
    "covering a small patch. Microbiology did not: the culturable organisms "
    "were assumed to be the ocean's inhabitants rather than the few that "
    "tolerated a plate of jelly. Sequencing did not brighten the lamp, it "
    "showed how dark the rest of the street had always been."
)

WHY_IT_MATTERS = (
    "This method rewrote the census of life. The most abundant photosynthetic "
    "organism on the planet was not described until 1988, and an entire "
    "abundant group of marine archaea was invisible until sequencing found "
    "them. Ocean-scale sampling expeditions have multiplied the number of known "
    "genes several times over, and the resulting catalogues are the raw "
    "material for the enzyme and natural product records elsewhere in this "
    "branch: you cannot search for a cold-adapted enzyme in organisms nobody "
    "knows exist. Environmental DNA has become a practical monitoring tool, "
    "detecting invasive species and rare animals from water samples rather "
    "than from nets. The costs are structural rather than technical. Ship time "
    "and deep-sea access are expensive enough that sampling, not sequencing, "
    "sets what gets studied, which concentrates knowledge in the waters of "
    "wealthy countries and near convenient ports. Reference databases are "
    "correspondingly skewed, so an unfamiliar sequence is often unidentifiable "
    "rather than novel. And a very large fraction of the ocean lies beyond any "
    "national jurisdiction, where the question of who may take a sample, "
    "publish its sequence and patent what it encodes had no clear answer at all "
    "until 2023, and where practice is still settling."
)
