# =============================================================================
#  biotechnology.branches.blue.marine_enzymes.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record must earn its separation from `white.industrial_enzymes`, and
#  the argument is made in the first paragraph of the DESCRIPTION rather than
#  left to the linkage facet.
#
#  THE SEPARATION IS NOT ABOUT PROVENANCE. An enzyme is not interesting because
#  it came from the sea. It is interesting when the sea imposed a constraint
#  that terrestrial life never faced, and the enzyme solved it. Two such
#  constraints matter industrially.
#
#      COLD          most of the ocean by volume is between minus one and four
#                    degrees. An enzyme that works there is not a warm enzyme
#                    running slowly; it is a structurally distinct solution,
#                    more flexible, faster at low temperature, and easy to
#                    destroy with mild heat. That last property is the useful
#                    one.
#      PRESSURE      the deep sea combines cold with hundreds of atmospheres,
#                    and pressure-adapted enzymes behave differently again.
#
#  The commercially decisive property of a cold-adapted enzyme is not its
#  activity in the cold. IT IS THAT IT CAN BE SWITCHED OFF BY GENTLE HEATING.
#  A reaction that can be stopped without adding anything, without a
#  purification step and without harming the product is worth more than a fast
#  reaction, and this record is built around that inversion.
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
    "Enzymes from marine organisms whose adaptations to cold, pressure and "
    "salt give them properties terrestrial enzymes do not have."
)

# -----------------------------------------------------------------------------
#  Structure: (a) why marine provenance matters only where it changes the
#  enzyme, (b) the cold adaptation trade and why the weakness is the product,
#  (c) the other marine constraints, (d) what limits the field.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the separation argument
    "Marine enzymes are catalysts from marine organisms, and they constitute a "
    "distinct subject only where the marine environment imposed a constraint "
    "that terrestrial life did not face. Provenance alone is uninteresting: a "
    "protease from a fish gut and a protease from a pig behave similarly and "
    "belong to the same industrial category. What separates this record is a "
    "set of adaptations with no terrestrial equivalent at industrial scale, "
    "chiefly to permanent cold, to hydrostatic pressure and to high salt. "
    # (b) the cold trade, and the inversion
    "Cold adaptation is the most consequential. Most of the ocean by volume "
    "sits between about minus one and four degrees Celsius, and enzymes that "
    "work there are not warm enzymes running slowly. They are structurally "
    "distinct: more flexible, with fewer stabilising interactions, higher "
    "catalytic rates at low temperature and much lower thermal stability. That "
    "combination is usually described as a trade in which stability is "
    "sacrificed for activity. Industrially the description is backwards. The "
    "instability IS the product. An enzyme that works at four degrees and is "
    "destroyed at forty can be added to a reaction, allowed to act, and then "
    "switched off by gentle warming, with no inhibitor, no separation step and "
    "no damage to a heat-sensitive product. Very few terrestrial enzymes offer "
    "that. "
    # (c) the other constraints
    "Other marine adaptations matter more narrowly. Piezophilic enzymes from "
    "the deep sea retain function under hundreds of atmospheres, which is of "
    "scientific interest and limited industrial use because few processes run "
    "at pressure. Halophilic enzymes from hypersaline environments tolerate "
    "salt concentrations that precipitate ordinary proteins, and some function "
    "in organic solvent as a consequence. And hyperthermophiles from "
    "hydrothermal vents supplied one of the most widely used reagents in "
    "molecular biology, a high-fidelity polymerase, which is the field's "
    "clearest commercial success and sits at the opposite end of the "
    "temperature range from everything else here. "
    # (d) the limits
    "The limits are those of the branch. The producing organisms mostly cannot "
    "be cultured, so discovery has moved to sequence-based mining, which finds "
    "candidates faster than they can be expressed and characterised. "
    "Heterologous expression of a protein from a cold, high-pressure organism "
    "in a mesophilic host frequently yields insoluble aggregate. And the "
    "supply argument that governs `blue.marine_natural_products` does not "
    "apply here at all, because an enzyme is a gene: once the sequence is "
    "known it can be manufactured by fermentation like any other protein, "
    "which is why this record has products and that one has a supply problem."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Enzymes are the tools living things use to build and break down "
    "molecules, and they are usually tuned to the temperature of whatever made "
    "them. Most of the ocean is close to freezing, so the creatures living "
    "there needed tools that still work in the cold. Those tools are useful to "
    "us for a reason that sounds like a flaw: they fall apart when warmed "
    "gently. That means you can add one to food or to a laboratory reaction, "
    "let it do its job in the cold, then warm it slightly to stop it "
    "completely, without adding chemicals and without cooking what you were "
    "working on. Being easy to destroy is the whole point."
)

# -----------------------------------------------------------------------------
#  The ice sculpting analogy. Chosen because it carries the inversion, that
#  fragility is the desirable property, and because its limit is honest: a
#  chisel that melts is useless for most jobs, and cold-adapted enzymes are
#  likewise unsuitable wherever a process needs heat.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is a chisel made of ice. That sounds like a poor chisel, and for most "
    "work it is: anything requiring heat or force will destroy it immediately. "
    "But if the job is delicate and cold, and if what you most need is for the "
    "tool to disappear completely the moment you have finished without leaving "
    "anything behind, then a chisel that melts in your hand is exactly the "
    "right one."
)

WHY_IT_MATTERS = (
    "One marine enzyme is in almost every molecular biology laboratory in the "
    "world. A high-fidelity polymerase from a deep-sea hyperthermophile made "
    "accurate amplification of long sequences practical, and the sequencing "
    "that underpins `blue.marine_genomics` depends on reagents of this kind. "
    "Cold-adapted enzymes allow food processing at refrigeration temperature, "
    "which preserves flavour and texture that heating destroys, and allow "
    "detergents to clean in cold water, which saves the electricity that "
    "`white.industrial_enzymes` records as its largest environmental claim. In "
    "molecular biology, a cold-active phosphatase or nuclease can be "
    "inactivated by warming rather than by adding an inhibitor that must then "
    "be removed, which removes a step from thousands of protocols. The limits "
    "are real. Cold-adapted enzymes are unstable by design, so they have short "
    "operational lifetimes and cannot be used in any warm process. Deep-sea "
    "and polar sampling is expensive, and the organisms mostly refuse to grow. "
    "Expressing a protein evolved for cold and pressure in a mesophilic host "
    "often produces insoluble aggregate rather than working enzyme. And the "
    "access rules that govern the rest of this branch apply here too: a "
    "sequence from another country's waters carries obligations, and a "
    "sequence from the high seas carried none at all until very recently."
)
