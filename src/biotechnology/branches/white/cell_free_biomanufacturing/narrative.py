# =============================================================================
#  biotechnology.branches.white.cell_free_biomanufacturing.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record closes the white branch and it is the branch's own negation:
#  every other record here depends on a living organism, and this one removes
#  it. The trade is stated in the first paragraph of the DESCRIPTION because
#  everything else follows from it.
#
#  YOU GIVE UP SELF-REPLICATION AND SELF-REPAIR. YOU GET CONTROL AND SPEED.
#
#  A cell is a catalyst that makes more of itself, which is why fermentation
#  scales so cheaply. It is also an organism with its own priorities: it grows,
#  it mutates, it spends carbon staying alive, it refuses to make things that
#  poison it, and it keeps a membrane between the engineer and the chemistry. A
#  cell-free system has none of those properties in either direction. It does
#  exactly what it is told, in hours rather than days, and then it stops.
#
#  THE BOUNDARY WITH `white.biocatalysis` IS EXACT AND WORTH LEARNING: a
#  cell-free system is PROGRAMMED WITH NUCLEIC ACID. A biocatalytic system is
#  assembled by hand from chosen enzymes. Add DNA to the first and it makes
#  something new; the second requires a different enzyme in the vessel.
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
    "Producing proteins and metabolites using extracted cellular machinery "
    "rather than living cells, programmed directly with DNA or RNA."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the trade and the boundary, (b) the two kinds of system,
#  (c) what the absence of a membrane actually buys, (d) why it has not
#  displaced fermentation.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the trade
    "Cell-free biomanufacturing carries out biological synthesis in a reaction "
    "mixture rather than inside an organism. A crude extract or a reconstituted "
    "set of components supplies the transcription and translation machinery, "
    "and a DNA or RNA template supplies the instruction. The trade against "
    "fermentation is sharp in both directions: the system cannot replicate "
    "itself, so the catalyst is consumed rather than grown, and every component "
    "must be supplied rather than made. In exchange there is no growth phase, "
    "no genetic drift, no carbon diverted to biomass, and no membrane between "
    "the operator and the reaction. "
    # (b) the two kinds
    "Two kinds of system exist and they answer different questions. Crude "
    "extracts, prepared by lysing cells and removing the debris, are cheap, "
    "productive and chemically complex, retaining metabolism that can be "
    "exploited for energy regeneration or that can consume the product "
    "unhelpfully. Reconstituted systems, assembled from individually purified "
    "components, contain only what was deliberately added, which makes them "
    "clean, fully defined, expensive and much less productive. Extracts are "
    "used for making things; reconstituted systems are used for answering "
    "questions about what is sufficient. "
    # (c) what the open reaction buys
    "The absence of a membrane is the practical advantage. The reaction "
    "environment can be set directly rather than through what a cell will "
    "tolerate, so redox potential, chaperones, unusual cofactors and "
    "non-standard amino acids can simply be added. Products that would kill an "
    "organism, including membrane proteins, toxins and antimicrobial peptides, "
    "can be produced because there is nothing alive to poison. A linear DNA "
    "template works directly, so the cloning and transformation steps "
    "disappear, and a design-build-test cycle that takes days in cells takes "
    "hours here. Reactions can also be freeze-dried onto paper or into pellets "
    "and rehydrated later, which turns a biological process into a shelf-stable "
    "reagent that needs no cold chain and no laboratory. "
    # (d) why it has not won
    "It has nonetheless not displaced fermentation, and the reasons are "
    "economic rather than conceptual. The energy substrates that drive protein "
    "synthesis cost more than sugar, the extract itself must be manufactured "
    "from cells that were grown conventionally, batch-to-batch variability in "
    "crude extracts is a real and under-reported problem, and the catalyst is "
    "consumed rather than reproducing. Cell-free manufacture therefore competes "
    "where speed, control or portability are worth more than cost per gram, "
    "which is a narrower set of applications than its advocates have "
    "historically claimed."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Normally, making a protein means growing bacteria or yeast and persuading "
    "them to produce it. Cell-free manufacturing skips the organism: the "
    "working parts are taken out of cells, put in a tube, and given written "
    "instructions in the form of DNA. Nothing in the tube is alive. That has "
    "real advantages. It is fast, taking hours rather than days. You can make "
    "things that would kill a living cell. You can reach in and adjust the "
    "conditions directly, because there is no cell wall in the way. And the "
    "whole mixture can be freeze-dried, stored on a shelf without "
    "refrigeration, and started later by adding water, which means a "
    "biological test can be carried out somewhere with no laboratory at all."
)

# -----------------------------------------------------------------------------
#  The hired kitchen analogy. It carries the trade in both directions: the
#  ingredients do not renew themselves, and nobody objects to what you cook.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Fermentation is hiring a chef who will cook for you but has opinions, "
    "needs feeding, takes days to arrive and refuses certain dishes. Cell-free "
    "is taking the chef's kitchen and doing it yourself. Everything is to hand "
    "and nothing argues, so an unusual dish is no harder than an ordinary one. "
    "The catch is that the chef would have gone shopping and the kitchen will "
    "not: when the ingredients run out, they run out, and you paid for all of "
    "them in advance."
)

WHY_IT_MATTERS = (
    "Two capabilities are difficult to obtain any other way. The first is "
    "speed: a design-build-test cycle measured in hours rather than days makes "
    "it practical to test hundreds of genetic designs before committing any of "
    "them to an organism, which is why this technique now underpins much of the "
    "prototyping in synthetic biology. The second is portability. A freeze-dried "
    "reaction on paper needs no cold chain, no power and no laboratory, and "
    "rehydrating it with a drop of sample can give a specific diagnostic result "
    "in the field. That has been demonstrated for outbreak pathogens and it "
    "puts molecular diagnosis somewhere a molecular laboratory will never be. "
    "Manufacturing biologics on demand, at the point of care, from a stored "
    "template rather than a stored product, is the same argument applied to "
    "medicines. The honest counterweight is that this technology has been "
    "described as imminent for a very long time and remains a small share of "
    "biological manufacturing. Energy substrates cost more than sugar, the "
    "extract must itself be grown, crude preparations vary between batches in "
    "ways that are poorly documented, and the catalyst is spent rather than "
    "self-renewing. It wins on speed, on control and on portability, and it "
    "does not win on cost per gram."
)
