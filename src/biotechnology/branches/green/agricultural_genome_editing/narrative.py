# =============================================================================
#  biotechnology.branches.green.agricultural_genome_editing.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the clearest case in the entire taxonomy of law lagging behind
#  biology, and the record is built around that rather than around the
#  chemistry.
#
#  A plant carrying a four-base deletion made with CRISPR is legally a
#  genetically modified organism in the European Union and legally a
#  conventional variety in Japan, Argentina and the United States. No
#  laboratory test can tell it apart from a spontaneous mutant, and none can
#  tell it apart from a variety produced by the chemical and radiation
#  mutagenesis that has been used without special regulation since the 1950s.
#  The same plant, three answers.
#
#  The find-and-replace analogy is chosen because it corrects the misconception
#  that editing is a larger intervention than older breeding methods. It is
#  smaller by orders of magnitude, and the analogy makes that visible without
#  arguing a position on how it should be regulated.
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
    "Making targeted, often transgene-free edits in crop and livestock genomes "
    "rather than inserting foreign genes."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what an edit is, (b) the three classes that policy turns on,
#  (c) how the machinery is delivered and then removed, (d) the constraint.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) what an edit is
    "Genome editing introduces a double-strand break, a single-strand nick or a "
    "direct chemical conversion at a chosen genomic position, and lets the "
    "cell's own repair machinery produce the change. The tool supplies the "
    "address; the cell supplies the edit. "
    # (b) the three classes
    "Three classes are distinguished in the policy literature and increasingly "
    "in law. A site-directed nuclease type 1 edit is a small insertion or "
    "deletion produced by error-prone non-homologous end joining, typically "
    "knocking a gene out. Type 2 uses a short repair template to make a precise "
    "substitution, often copying an allele that already exists elsewhere in the "
    "species and could in principle have been introduced by crossing. Type 3 "
    "inserts a whole cassette and is, biologically and legally, transgenesis. "
    "Almost every regulatory dispute in this field is an argument about where "
    "to draw the line between type 1, type 2 and type 3. "
    # (c) delivery and removal
    "Delivery to plants may use Agrobacterium, in which case the editing "
    "machinery is present in the genome and is segregated away in later "
    "generations, leaving an edited plant carrying no foreign DNA. Or it may "
    "use preassembled ribonucleoprotein complexes delivered directly into "
    "protoplasts, which leaves no foreign DNA at any stage. Base editors "
    "convert one base pair into another without a double-strand break; prime "
    "editors write short defined sequences from an attached template. In "
    "livestock, editing is applied in zygotes. "
    # (d) the constraint
    "The binding constraint is regeneration and regulation rather than editing. "
    "Cutting the genome is now reliable; recovering a whole plant from the "
    "edited cell is not, and knowing which of thirty jurisdictions will treat "
    "the result as conventional is not either."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "All plants and animals accumulate small random changes in their DNA over "
    "generations, and that is where the variety in every crop originally came "
    "from. Plant breeders have deliberately increased that randomness for a "
    "century, using chemicals and radiation to scramble genes and then "
    "selecting whichever results turned out useful. Genome editing does the "
    "same kind of thing, but aimed. It makes one small change at one chosen "
    "place, usually switching off a gene that was causing a problem. In most "
    "cases nothing from another species remains in the finished plant, and "
    "nothing distinguishes it from a change that could have happened on its "
    "own."
)

# -----------------------------------------------------------------------------
#  The find-and-replace analogy. Its limit is stated: a proofreader can still
#  introduce an error somewhere else, which is exactly what off-target editing
#  is and why `metrics.py` measures it.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Older breeding methods were a spelling change made by shaking the whole "
    "book until a letter fell out somewhere, then reading the result to see "
    "whether it had improved. Genome editing is using find-and-replace on one "
    "word you have already identified. The finished book reads the same either "
    "way; the difference is how many other pages were disturbed on the way. "
    "The comparison has an honest limit: find-and-replace can also match "
    "somewhere you did not intend, which is why edited lines are sequenced to "
    "look for changes at similar-looking sites elsewhere in the genome."
)

WHY_IT_MATTERS = (
    "Editing collapses the cost and the timeline of crop improvement. A trait "
    "that took a decade of backcrossing can be produced in two generations, "
    "and because no foreign gene is present the product may escape the "
    "regulatory burden that made conventional genetic modification viable only "
    "for four global commodity crops. That opens improvement to minor crops, "
    "to public-sector breeders and to national programmes, which is the single "
    "most consequential difference between this record and "
    "`green.plant_genetic_engineering`. The costs are equally specific. The "
    "regulatory divergence fragments trade: a shipment that is conventional "
    "grain in one port is an unauthorised genetically modified organism in the "
    "next. Because a type 1 edit leaves no unique sequence to detect, "
    "enforcement of that divergence may be impossible in practice, which is an "
    "uncomfortable position for every side of the argument. And the tools "
    "themselves are covered by a patent thicket dense enough that the freedom "
    "to operate, rather than the biology, decides what a small breeder can "
    "attempt."
)
