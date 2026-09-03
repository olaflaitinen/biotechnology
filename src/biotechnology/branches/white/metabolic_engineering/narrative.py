# =============================================================================
#  biotechnology.branches.white.metabolic_engineering.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The technical register here carries an idea that most short accounts of the
#  field get wrong, so it is stated in the DESCRIPTION rather than left to
#  `metrics.py`: THERE IS USUALLY NO RATE-LIMITING STEP.
#
#  Metabolic control analysis showed in 1973 that control over a pathway's flux
#  is distributed across many enzymes, and that the control coefficients sum to
#  one. Overexpressing the enzyme that looks like the bottleneck typically does
#  not raise output, because control simply moves elsewhere. A generation of
#  disappointing results came from assuming otherwise, and a reader who takes
#  only one idea from this record should take that one.
#
#  The public register uses a city traffic analogy for exactly this reason: it
#  is the only everyday system most readers already understand as one where
#  widening a single road does not make the journey faster.
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
    "Rewiring the metabolism of a living cell so that it converts a cheap "
    "feedstock into a chosen product at commercially useful yield."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what the discipline is and how it differs from biocatalysis,
#  (b) the control insight that governs everything, (c) how the work is
#  actually done, (d) what limits the answer.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the discipline, defined against its neighbour
    "Metabolic engineering modifies the metabolic network of a living organism "
    "so that carbon and energy flow towards a chosen product instead of "
    "towards biomass and the cell's own priorities. It differs from "
    "biocatalysis in the unit of work: biocatalysis performs one or a few "
    "steps outside a cell with purified enzymes, whereas metabolic engineering "
    "installs a whole pathway inside an organism that then feeds itself, "
    "regenerates its own cofactors, and repairs its own catalysts. That is a "
    "large advantage and it is bought at a price, because the organism is also "
    "growing, mutating and spending carbon on staying alive. "
    # (b) the control insight
    "The governing insight is that pathway output is not usually set by a "
    "single rate-limiting step. Metabolic control analysis established that "
    "control is distributed, and that the flux control coefficients of the "
    "enzymes in a pathway sum to one. Removing what appears to be the "
    "bottleneck therefore redistributes control rather than eliminating it, "
    "and a great deal of early disappointment in this field followed from "
    "expecting otherwise. Useful gains come from balancing expression across "
    "the pathway, from relieving cofactor and precursor competition, and from "
    "deleting the branches that divert carbon elsewhere. "
    # (c) how it is done
    "Practice is organised as a design, build, test and learn cycle. Design "
    "uses genome-scale stoichiometric models and flux balance analysis to "
    "predict which deletions and insertions move flux towards the product. "
    "Build assembles the pathway and adjusts expression through promoter, "
    "ribosome binding site and copy number choices. Test measures titre, rate "
    "and yield, and increasingly measures internal flux directly using labelled "
    "carbon. Learn feeds the result back into the model. The build and test "
    "steps are now heavily automated, which has moved the bottleneck of the "
    "whole discipline to measurement and to design quality rather than to "
    "construction. "
    # (d) the limits
    "Two limits are absolute and one is practical. Stoichiometry sets a maximum "
    "yield from a given feedstock that no amount of engineering can exceed, and "
    "the redox and energy balance of the pathway sets another. The practical "
    "limit is evolutionary: a strain engineered to divert carbon away from "
    "growth is at a competitive disadvantage against any mutant that stops "
    "doing so, and over the many generations of a production fermentation, "
    "that mutant will be selected for. Genetic stability is therefore an "
    "engineering requirement rather than an assumption."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Every living cell is a chemical factory that runs itself. It takes in "
    "sugar and turns it into the hundreds of things it needs in order to grow. "
    "Metabolic engineering means rearranging that factory so that it also, or "
    "instead, makes something we want: a fuel, a plastic ingredient, a "
    "vitamin, a flavour, a medicine. The work is less like inventing a new "
    "machine and more like rerouting a road network so that traffic ends up "
    "somewhere else. And the awkward part is that the cell has its own "
    "priorities. It wants to grow, and anything we divert away from growth is "
    "something it is quietly under pressure to stop doing."
)

# -----------------------------------------------------------------------------
#  The traffic analogy. Chosen because it is the one everyday system readers
#  already understand as having distributed rather than single-point control,
#  which is the misconception this record exists to correct.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is traffic engineering for a city, not a new engine for a car. When a "
    "city is congested, the instinct is to find the worst junction and widen "
    "it. It rarely works, because the queue simply forms at the next junction "
    "instead; the congestion was a property of the whole network rather than of "
    "one place in it. Metabolic engineering works the same way. Progress comes "
    "from rebalancing the whole route, closing the side roads that lead "
    "nowhere useful, and accepting that the residents still need to get to "
    "work."
)

WHY_IT_MATTERS = (
    "This is how a large share of the world's amino acids, vitamins and "
    "organic acids are already made. Engineered bacteria produce lysine for "
    "animal feed at millions of tonnes a year, which reduces the protein crop "
    "that livestock would otherwise need. Engineered routes supply 1,3-"
    "propanediol and 1,4-butanediol for polymers, the second by a pathway that "
    "does not exist in any organism and had to be assembled from parts. The "
    "field also produced one of biotechnology's most instructive stories. A "
    "yeast strain engineered to make the precursor of the antimalarial "
    "artemisinin was a genuine scientific triumph, delivered on its technical "
    "promise, and then failed commercially against farmers growing sweet "
    "wormwood more cheaply. The honest lesson is that a working pathway is not "
    "the same as a viable product, and that agricultural supply chains are "
    "harder to displace than they look. The constraints are equally honest. "
    "Stoichiometry caps yield from a given sugar and no engineering can pass "
    "it. Fermentation feedstock competes with food and land. And an engineered "
    "strain is under constant selective pressure to revert to simply growing, "
    "which means stability over hundreds of generations is a design "
    "requirement rather than a detail."
)
