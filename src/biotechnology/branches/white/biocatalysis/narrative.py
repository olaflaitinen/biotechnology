# =============================================================================
#  biotechnology.branches.white.biocatalysis.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The boundary against `white.industrial_enzymes` is declared in that record's
#  linkage facet and is repeated here because it is the first thing a reader
#  needs. THAT record is about the enzyme as a manufactured article: discovery,
#  engineering, fermentation, formulation, sale. THIS record is about the
#  enzyme as a STEP IN A SYNTHETIC ROUTE: which reaction, in what solvent, at
#  what substrate loading, with the cofactor regenerated how, and what the
#  chemical route it replaced actually cost.
#
#  The public register is built on handedness rather than on catalysis, because
#  chirality is the one property that makes an enzymatic route not merely
#  cheaper but sometimes the only sensible option, and because the left-hand
#  and right-hand glove image needs no chemistry to follow.
#
#  The record's anchor example is the sitagliptin transaminase, and it is
#  described in `history.py` rather than here, because the narrative should not
#  turn into a single case study.
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
    "Designing chemical synthesis around enzymes as the catalytic step, in "
    "place of metal catalysis, protecting groups and organic solvents."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what the discipline is and how it differs from its sibling,
#  (b) the four reaction classes that carry the field, (c) the two engineering
#  problems that decide whether a route works, (d) where it loses.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the discipline
    "Biocatalysis is synthetic chemistry in which one or more steps are "
    "performed by an enzyme. It is distinguished from industrial enzyme "
    "production, which supplies the catalyst, by concerning itself with the "
    "route: which disconnection to make enzymatically, at what substrate "
    "loading, in what reaction medium, and against what the alternative "
    "chemical step would have cost in yield, solvent and waste. A chemist "
    "planning a synthesis now treats enzymatic steps as ordinary "
    "retrosynthetic options rather than as curiosities, which is a change that "
    "happened within one professional generation. "
    # (b) what enzymes are actually used for
    "Four reaction classes carry most of the industrial work. Hydrolases, "
    "chiefly lipases, esterases, proteases and nitrilases, need no cofactor "
    "and are therefore the easiest to deploy. Ketoreductases and other "
    "oxidoreductases install stereocentres by reducing ketones, and require a "
    "nicotinamide cofactor. Transaminases install chiral amines, which are "
    "present in a large share of pharmaceuticals and are difficult to make "
    "selectively by chemical means. Lyases and, more recently, engineered "
    "carbene and nitrene transferases form carbon-carbon and carbon-heteroatom "
    "bonds, including reactions with no natural counterpart at all. "
    # (c) the two engineering problems
    "Two problems decide whether a route is viable. The first is the reaction "
    "medium: enzymes evolved in water, most organic substrates dissolve poorly "
    "in it, and the answers are two-phase systems, water-miscible cosolvents, "
    "neat substrate with a little water, or engineered solvent tolerance. The "
    "second is cofactor cost. A nicotinamide cofactor used once would cost "
    "more than the product, so it is regenerated in situ by a second enzyme, "
    "typically a glucose or formate dehydrogenase, so that each cofactor "
    "molecule turns over thousands of times. Cofactor total turnover, not "
    "enzyme turnover, is frequently the number that determines the economics. "
    # (d) where it loses
    "Biocatalysis loses where the substrate is insoluble and unstable in "
    "water, where the reaction has no enzymatic precedent and screening finds "
    "no starting point, where product inhibition caps conversion below what "
    "the process needs, and wherever an established chemical route is already "
    "cheap. The honest position is that it is now one option among several "
    "rather than a superior replacement for chemistry."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Many molecules come in two forms that are mirror images of each other, "
    "like a left and a right hand. They are built from the same parts in the "
    "same order, and they are not interchangeable. In a medicine this matters "
    "enormously: one hand can be the drug and the other can be useless or "
    "harmful. Ordinary chemical methods often make both hands at once, so half "
    "the output has to be separated out and thrown away. Enzymes are "
    "themselves handed, so they naturally make one form and not the other. "
    "Building a manufacturing process around enzymes therefore means less "
    "waste, fewer steps, no need for the harsh solvents and rare metals that "
    "the alternative requires, and a plant that runs in warm water instead of "
    "under heat and pressure."
)

# -----------------------------------------------------------------------------
#  The gloves analogy. Chosen over a lock-and-key image because that one is
#  already used by `white.industrial_enzymes` for selectivity, and because
#  handedness is the specific property this record is about. The final sentence
#  carries the cost, which is the part a promotional account would omit.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Conventional chemistry is a glove factory that makes left and right "
    "gloves in one machine and then pays somebody to sort them, discarding "
    "every glove of the wrong hand. An enzyme is a machine that only ever "
    "makes right gloves. Nothing is sorted and nothing is discarded. The cost "
    "of the second machine is that it makes exactly one size and style, and "
    "retooling it for a different glove is the work of months."
)

WHY_IT_MATTERS = (
    "Pharmaceutical manufacturing produces more waste per kilogram of product "
    "than any other chemical sector, commonly tens of kilograms of waste for "
    "each kilogram of drug substance, most of it solvent. Biocatalytic route "
    "redesign is the single most effective response the industry has found. "
    "Replacing a metal-catalysed step with an engineered enzyme has, in "
    "documented cases, raised yield, removed a high-pressure hydrogenation, "
    "eliminated the heavy metal catalyst entirely, and cut total waste "
    "substantially, all at once. Enzymatic manufacture of the penicillin "
    "intermediate 6-aminopenicillanic acid replaced a route that used "
    "dichloromethane and operated far below room temperature, at a scale of "
    "tens of thousands of tonnes a year. Multi-enzyme cascades now build "
    "complex molecules in a single vessel, without isolating the intermediates "
    "and without the protecting groups that conventional synthesis spends much "
    "of its effort installing and removing. The limits are real. Water is a "
    "poor solvent for most organic substrates. Cofactors cost more than the "
    "products unless they are recycled. A new reaction with no enzymatic "
    "precedent may have no starting point to evolve from. And once a route is "
    "in a regulatory dossier it is expensive to change, which means the "
    "decision to go enzymatic is effectively made once, early, and then locked "
    "in for the life of the product."
)
