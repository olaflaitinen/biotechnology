# =============================================================================
#  biotechnology.branches.green.plant_genetic_engineering.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Few topics in this taxonomy attract more heat, and the editorial position
#  taken here is stricter than elsewhere as a result. The fields below report
#  what the technology does, what is deployed, what the measured outcomes have
#  been, and what the open disputes are. They argue for nothing.
#
#  Editorial rule 3 does unusually heavy work in this record. The genuine
#  situation is that several things are true at once which are normally
#  presented as alternatives: insecticide use fell, seed supply concentrated,
#  resistant weeds emerged, and public trust in Europe never recovered from how
#  the first products were introduced. WHY_IT_MATTERS states all four and
#  explicitly refuses to resolve them into a verdict, because resolving them is
#  advocacy and this library does not do that.
#
#  The card-deck analogy is chosen because it corrects the most common
#  misconception directly: that conventional breeding is a small genetic change
#  and engineering is a large one. The reverse is true by orders of magnitude,
#  and the analogy makes that visible without argument.
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
    "Introducing defined genes into crop genomes to confer traits such as "
    "insect resistance, herbicide tolerance or enhanced nutrition."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what is actually inserted, (b) the two delivery routes,
#  (c) what happens after delivery, (d) the constraint that explains why the
#  deployed trait set is so narrow.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) what is inserted
    "Plant genetic engineering inserts one or more defined transgenes into a "
    "plant genome, together with the promoter and terminator sequences that "
    "control when and where they are expressed. The insert is characterised to "
    "a level no conventional breeding programme approaches: its exact sequence, "
    "its insertion site, its copy number, its inheritance across generations, "
    "and the absence of unintended open reading frames across the junctions. "
    # (b) delivery
    "Two delivery routes dominate. Agrobacterium tumefaciens, a soil bacterium "
    "that naturally transfers DNA into plant cells and causes crown gall "
    "disease, is disarmed and loaded with the construct of interest; it is "
    "efficient in dicotyledons and, with modification, in cereals. Biolistic "
    "delivery coats gold or tungsten microparticles with DNA and fires them "
    "into tissue, which works in species Agrobacterium will not infect. "
    # (c) after delivery
    "Transformed cells are selected on a marker and regenerated into whole "
    "plants through tissue culture, which is why `green.plant_tissue_culture` "
    "is a prerequisite rather than a neighbour. A single successful insertion "
    "with acceptable characteristics is called an event, and the commercial "
    "product is that one event, backcrossed into hundreds of locally adapted "
    "varieties. "
    # (d) the constraint
    "The binding constraint is regulatory cost per event, not biology. "
    "Assembling a dossier runs into tens of millions of euro and takes years, "
    "which only high-acreage commodity crops repay. That single fact explains "
    "why the deployed trait set has remained essentially unchanged for three "
    "decades and why no public-sector programme has brought a transgenic crop "
    "to market at scale."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Every living thing carries instructions written in DNA, and the chemical "
    "alphabet is the same in a bacterium, a fish and a maize plant. That means "
    "an instruction that works in one can often be copied into another. Genetic "
    "engineering copies a specific, known instruction into a crop. One common "
    "example is an instruction from a soil bacterium for making a protein that "
    "certain caterpillars cannot digest, so the plant defends itself without "
    "being sprayed. The change is small and precisely documented: one or two "
    "known genes, in a known place. The plant is then grown and tested for "
    "years before anyone is allowed to sell it."
)

# -----------------------------------------------------------------------------
#  The card-deck analogy. It corrects the misconception that engineering is the
#  larger genetic change. Its limit is that a named card can still land
#  somewhere unhelpful, which is why insertion site characterisation exists.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Conventional breeding is shuffling two whole decks of cards together and "
    "hoping for a good hand: tens of thousands of genes move at once and nobody "
    "records which. Genetic engineering takes one named card out of one deck "
    "and places it, face up, into the other. It is the smaller change of the "
    "two, and unlike the shuffle it is fully documented. The comparison has a "
    "real limit: a card placed into a deck still lands somewhere, and where it "
    "lands can matter, which is exactly why every commercial event has its "
    "insertion site sequenced and disclosed."
)

WHY_IT_MATTERS = (
    "Bt cotton and Bt maize cut insecticide applications substantially wherever "
    "they were adopted, which matters most for smallholders who spray by hand "
    "without protective equipment. Virus-resistant papaya saved the Hawaiian "
    "industry from a disease that had no other remedy. Golden Rice was designed "
    "for populations where vitamin A deficiency blinds and kills children. "
    "Against that, the technology concentrated seed supply into very few "
    "companies, herbicide-tolerant systems selected for resistant weeds and in "
    "some regions increased total herbicide volume, and public trust in Europe "
    "never recovered from the way the first products were introduced without "
    "any consumer benefit to offer. All of those statements are true at the "
    "same time. The most consequential fact is the least discussed: the "
    "regulatory cost of bringing one event to market excludes every crop that "
    "is not planted across millions of hectares, so cassava, sorghum, cowpea "
    "and banana, the crops eaten by the people with the least food security, "
    "have benefited least from a technology often justified by their needs."
)
