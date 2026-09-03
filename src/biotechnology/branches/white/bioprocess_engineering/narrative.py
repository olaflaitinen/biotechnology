# =============================================================================
#  biotechnology.branches.white.bioprocess_engineering.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two facts organise this record, and both contradict how the subject is
#  usually presented.
#
#  THE FIRST IS THE SCALE-UP PARADOX. There is no such thing as simply making a
#  vessel bigger. The criteria an engineer would want to hold constant, power
#  per unit volume, impeller tip speed, oxygen transfer coefficient and mixing
#  time, are mutually incompatible under geometric similarity. Holding any one
#  of them fixed forces the others to change, often by a large factor. Scale-up
#  is therefore the deliberate choice of which property to preserve and which
#  to sacrifice, and the choice depends on the organism.
#
#  THE SECOND IS THAT THE INTERESTING PART IS NOT THE FERMENTER. For a
#  biological product, most of the manufacturing cost sits downstream of the
#  vessel, in recovery and purification. A field that is popularly imagined as
#  being about growing cells spends most of its money separating one molecule
#  from everything else that was in the tank.
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
    "Designing, scaling and operating the equipment train that turns a "
    "laboratory biological process into reproducible manufacture, including "
    "everything downstream of the vessel."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what the discipline covers and its boundary,
#  (b) the scale-up paradox, (c) downstream, where the money is,
#  (d) why yields multiply, which is the arithmetic that governs design.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) scope and boundary
    "Bioprocess engineering designs and operates the physical train that "
    "carries a biological process from a laboratory result to reproducible "
    "manufacture: the vessel and its mixing, aeration and heat removal, the "
    "instrumentation and control, and every unit operation between the harvest "
    "and the packaged product. It is distinguished from microbial "
    "fermentation, which is the cultivation itself. That record describes what "
    "the culture demands; this one describes what the plant can supply and "
    "what happens to the broth afterwards. "
    # (b) the paradox
    "Scale-up is the discipline's characteristic problem and it has no general "
    "solution. Under geometric similarity, constant power per unit volume, "
    "constant impeller tip speed, constant oxygen transfer coefficient and "
    "constant mixing time cannot be maintained together: fixing one forces the "
    "others to move, sometimes by an order of magnitude. A large vessel is "
    "therefore not a small vessel writ large. It mixes more slowly, so a "
    "culture experiences gradients in dissolved oxygen, substrate and pH as it "
    "circulates, and cells spend part of every circulation in conditions the "
    "laboratory never presented. Choosing which criterion to preserve is an "
    "engineering judgement about which insult the organism tolerates least. "
    # (c) downstream
    "Downstream processing is where most of the cost lies for a biological "
    "product, commonly the majority of manufacturing cost for a therapeutic "
    "protein. The train separates cells from broth by centrifugation or "
    "filtration, releases intracellular product by homogenisation if it was "
    "not secreted, captures the product on a chromatographic resin, polishes "
    "away the remaining impurities, exchanges the buffer, concentrates, and "
    "formulates. Each step consumes buffer in volumes far exceeding the "
    "product, and buffer preparation and storage frequently size the facility. "
    # (d) the arithmetic
    "One piece of arithmetic governs the design of that train. Step yields "
    "multiply. Ten steps at ninety per cent each deliver thirty-five per cent "
    "overall, so removing a step is usually worth more than improving one. "
    "This is why the field pursues fewer operations rather than better ones, "
    "and why a modest gain in titre upstream can be worth less than "
    "eliminating a single purification step downstream."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Getting something to work in a laboratory flask and getting it to work in "
    "a tank the size of a room are different problems. Big tanks mix slowly, "
    "so different parts of them are not the same, and cells travelling around "
    "one experience changing conditions rather than steady ones. Then there is "
    "the part people forget: once the tank has finished, you still have a "
    "soup containing the thing you want and thousands of things you do not, "
    "and separating them is where most of the cost and most of the equipment "
    "actually is. Every separation step also loses a little of the product, "
    "and those losses multiply, so the shortest sequence usually beats the "
    "cleverest one."
)

# -----------------------------------------------------------------------------
#  The kitchen-to-canteen analogy. Chosen because scale-up failure is
#  intuitive in cooking and counterintuitive in engineering, and because it
#  carries the second half of the record too: what happens after the pot.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is the difference between cooking for four and cooking for four "
    "thousand. The recipe does not scale. A domestic pan heats evenly and a "
    "vat does not, so the edges catch while the middle is cold, and stirring a "
    "vat takes long enough that the two are never quite the same thing at the "
    "same moment. And the canteen's real work is not the cooking at all. It is "
    "everything after: portioning, straining, chilling, packing, each step "
    "losing a little and each one needing its own machine."
)

WHY_IT_MATTERS = (
    "This discipline decides whether a biological discovery becomes something "
    "people can actually obtain. A therapeutic protein that works in a "
    "laboratory is of no use to a patient until it can be made reproducibly, "
    "in quantity, to a purity specification, at a price a health system will "
    "pay, and the majority of that cost sits in purification rather than in "
    "the fermenter. The field also carries a lesson it learned expensively. "
    "Between the early 1990s and the 2010s, upstream titres for therapeutic "
    "proteins rose by roughly two orders of magnitude while downstream "
    "capacity did not follow, so the industry created a bottleneck by "
    "succeeding at the wrong end of its own process. Facilities built for the "
    "old ratio could not handle what the new cell lines produced. And because "
    "these plants are single points of failure for medicines with no "
    "alternative supplier, an engineering failure is a public health event: "
    "contamination of one manufacturing site in 2009 caused international "
    "shortages of two enzyme replacement therapies that patients had no way to "
    "substitute. The counterweight to all of this is that improvements here "
    "are permanent and cumulative. A purification step removed is removed for "
    "the life of the product."
)
