# =============================================================================
#  biotechnology.branches.blue.aquaculture_biotechnology.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the second record in the library whose subject can suffer, after
#  `green.animal_biotechnology`, and the same editorial discipline applies:
#  welfare is recorded in the data rather than appended as a caveat.
#
#  THE ORGANISING FACT IS A REVERSAL THAT MOST READERS HAVE NOT REGISTERED.
#  Aquaculture now supplies about half of the fish people eat, and it passed
#  capture fisheries within the last two decades. Farming, not fishing, is how
#  most seafood reaches a plate.
#
#  THE ORGANISING TENSION FOLLOWS IMMEDIATELY. Farmed carnivorous fish were
#  historically fed on wild fish, so the industry that was supposed to relieve
#  pressure on wild stocks was drawing on them. That is the fish-in fish-out
#  problem, and the honest account is that it has been very substantially
#  reduced rather than solved: feed formulation moved to plant proteins, algal
#  oils and processing trimmings, and the ratio for salmon fell by a large
#  factor. It has not reached zero, and the species that are farmed most are
#  not the ones that were the problem.
#
#  A THIRD FACT SHAPES THE WHOLE RECORD: A FISH FARM IS OPEN TO THE SEA. What
#  happens in a net pen does not stay there, which is why disease, escape and
#  chemical use are the field's defining difficulties rather than incidental
#  ones.
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
    "Breeding, health management and feed technology for farmed aquatic "
    "animals, now the source of about half the fish that people eat."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the scale and the reversal, (b) the four areas of the field,
#  (c) the feed problem and how far it has moved, (d) the openness of the
#  system, which is the binding constraint.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the reversal
    "Aquaculture biotechnology applies breeding, genetics, veterinary medicine "
    "and nutrition to farmed aquatic animals. Its context is a reversal that "
    "happened recently and quietly: farmed production overtook capture "
    "fisheries within the last two decades, and about half the fish eaten "
    "worldwide is now farmed. The sector is also unusual in how young its "
    "domestication is. Salmon breeding programmes began in the 1970s, which "
    "means the animals are a few generations from wild, and the genetic gains "
    "available are correspondingly large and are still being taken. "
    # (b) the four areas
    "Four areas carry the field. Selective breeding, increasingly genomic, has "
    "improved growth rate, feed conversion and disease resistance faster than "
    "in any terrestrial livestock species, because fecundity is enormous and "
    "selection intensity can be extreme. Health management is dominated by "
    "vaccination, and the salmon industry's near elimination of antibiotic use "
    "through vaccines is one of the clearest successes in this library. Feed "
    "technology has reformulated diets away from wild fish towards plant "
    "proteins, algal oils and processing by-products. Reproductive control, "
    "including induced spawning, sex control and sterility, exists both to "
    "manage production and to limit the consequences of escape. "
    # (c) the feed problem
    "The feed question deserves precision because it is usually stated too "
    "simply in both directions. Carnivorous farmed fish were historically fed "
    "meal and oil from wild-caught small pelagic fish, so a sector intended to "
    "relieve wild stocks was consuming them. Reformulation has reduced the "
    "quantity of wild fish per kilogram of salmon produced by a large factor, "
    "and much of the remaining marine content comes from trimmings rather than "
    "from fish caught for the purpose. The problem is therefore much smaller "
    "than it was and is not gone, and the substitution has its own costs, since "
    "plant protein means land, water and fertiliser. "
    # (d) the openness
    "The binding constraint is that most marine aquaculture is open to the sea. "
    "A net pen exchanges water, parasites, pathogens, waste and occasionally "
    "animals with the environment around it, so sea lice move between farmed "
    "and wild populations, escapees interbreed with wild stocks whose local "
    "adaptation they dilute, and treatments applied to the farm enter the water. "
    "Recirculating systems and offshore siting address this at substantial "
    "capital and energy cost. Nothing else in this record can be evaluated "
    "without it."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "About half the fish people eat is now farmed rather than caught, and that "
    "change happened within the last twenty years or so. Farming fish means the "
    "same problems as farming anything else: breeding animals that grow well, "
    "keeping them healthy, and working out what to feed them. There is one "
    "extra problem that land farming does not have. Most fish farms sit in open "
    "water, so whatever happens inside the pens does not stay inside them. "
    "Parasites and diseases can pass between farmed and wild fish, escaped fish "
    "breed with wild ones, and anything used to treat the fish ends up in the "
    "sea. Almost every argument about fish farming comes back to that."
)

# -----------------------------------------------------------------------------
#  The open window analogy. Chosen because the openness of the system is the
#  record's defining property and is easy to miss, and because its limit is
#  stated: closing the window is possible and expensive, which is exactly the
#  recirculating aquaculture trade.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is keeping animals in a barn with the windows permanently open. "
    "Everything else about the husbandry is ordinary, and that one feature "
    "governs the rest: what is inside gets out, what is outside gets in, and no "
    "amount of care within the barn changes it. Windows can be fitted, and "
    "that is what a fully enclosed recirculating farm is. They cost a great "
    "deal, and somebody has to pay for the air handling afterwards."
)

WHY_IT_MATTERS = (
    "This is where a large and growing share of the world's animal protein "
    "comes from, and it is produced with feed conversion ratios that "
    "terrestrial livestock cannot approach, because a fish is buoyant and does "
    "not spend energy staying warm. Vaccination in salmon farming reduced "
    "antibiotic use to a very small fraction of what it had been, which is a "
    "veterinary success of the kind that `green.veterinary_vaccines` argues is "
    "systematically underappreciated. Breeding programmes only a few "
    "generations old have delivered large and continuing gains. And well over a "
    "hundred million people depend on the sector for a livelihood, "
    "predominantly in Asia and predominantly at small scale. The costs are "
    "serious and this record does not minimise them. Sea lice move from farms "
    "to wild salmon populations, and the treatments used against them have "
    "repeatedly lost effectiveness through resistance. Escaped farmed fish "
    "interbreed with wild populations and dilute local adaptation that took "
    "many generations to accumulate. Disease outbreaks have removed a "
    "substantial share of national production in a single year. Mangrove "
    "clearance for shrimp ponds destroyed coastal habitat that protected the "
    "coast behind it. Feed still draws on wild fish, though far less than it "
    "did. And welfare is a genuine and unresolved question: stocking density, "
    "handling, disease burden and slaughter method all matter, the evidence "
    "base on fish sentience has strengthened considerably, and regulation has "
    "not kept pace with it."
)
