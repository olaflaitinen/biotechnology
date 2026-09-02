# =============================================================================
#  biotechnology.branches.green.biopesticides.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The central trade-off in this record is narrowness, and it cuts both ways in
#  a manner that is unusually clean.
#
#  A biopesticide that kills one pest species and nothing else is exactly what
#  is wanted ecologically: pollinators, natural enemies and soil fauna are
#  spared, and there is no residue. The same narrowness is a commercial
#  disadvantage, because a product with one target has a small market and still
#  needs a full registration dossier. Selectivity is simultaneously the whole
#  benefit and the whole business problem, and neither half is a consequence of
#  the other being overstated.
#
#  The sniffer dog analogy is chosen because it carries that trade-off
#  intact: a dog trained on one scent is useless against anything else, and
#  that is precisely why it does not wreck the room.
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
    "Pest and disease management with living organisms or their natural "
    "products instead of broad-spectrum synthetic chemistry."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the three regulatory classes, (b) how the microbial ones
#  actually work, (c) the fourth class that is genuinely new, (d) the
#  constraint that follows from all of them being alive or labile.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the three classes
    "Biopesticides fall into three classes that are both biological and "
    "regulatory. Microbial biopesticides use a living organism as the active "
    "substance. Biochemical biopesticides use a naturally occurring substance "
    "with a non-toxic mode of action, including sex pheromones for mating "
    "disruption, plant extracts such as azadirachtin, and defence elicitors "
    "that prime the plant's own responses. Macrobial biological control "
    "releases predators and parasitoids, and is the backbone of protected-crop "
    "production in northern Europe, where a glasshouse tomato crop is now "
    "routinely grown with almost no insecticide at all. "
    # (b) how the microbials work
    "Among the microbials, Bacillus thuringiensis is by far the largest single "
    "product: its crystal proteins are inert until solubilised and "
    "proteolytically activated in the alkaline insect midgut, which is why the "
    "same protein is harmless to vertebrates whose stomachs are acidic. "
    "Entomopathogenic fungi such as Beauveria and Metarhizium do not need to be "
    "eaten at all; they penetrate the cuticle directly, which makes them "
    "effective against sucking pests that ingest nothing. Entomopathogenic "
    "nematodes carry symbiotic bacteria into the pest, and baculoviruses are "
    "extremely host-specific, often to a single species. "
    # (c) the newest class
    "A fourth class delivers double-stranded RNA that silences an essential "
    "gene in the target pest through RNA interference, giving species-level "
    "selectivity that no chemistry can match, because the specificity is "
    "sequence-based rather than biochemical. "
    # (d) the constraint
    "The binding constraint is that all of this is alive or labile. Persistence "
    "in the field is measured in days rather than weeks, ultraviolet light and "
    "heat degrade the active substance, and rain washes it off. That short "
    "persistence is what makes these products safe and what makes them fail."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Instead of spraying a chemical that kills most insects it touches, "
    "biological control uses nature's own arrangements. Some products are a "
    "bacterium that makes a protein poisonous only to caterpillars and harmless "
    "to everything else, including us, because it only becomes active in a "
    "caterpillar's gut. Some are fungi that grow through an insect's skin. Some "
    "release the wasps or mites that already eat the pest. Some flood the air "
    "with the scent females use to attract males, so the males spend the whole "
    "season searching and never find one. The pest is controlled, and the bees, "
    "ladybirds and earthworms are not. The catch is that living things do not "
    "keep. These products break down in sunlight within days, so they have to "
    "be applied at exactly the right moment."
)

# -----------------------------------------------------------------------------
#  The sniffer dog analogy. Its limit is the trade-off itself, stated inside
#  the analogy rather than after it.
# -----------------------------------------------------------------------------
ANALOGY = (
    "A synthetic pesticide is a fire hose aimed at a room. Biological control "
    "is a trained sniffer dog: slower to deploy, useless against anything it "
    "was not trained for, and it does not soak everything else in the room. The "
    "comparison holds in the awkward direction too. A dog that finds only one "
    "thing is worth having precisely because it ignores everything else, and it "
    "is also a much harder product to sell than a hose."
)

WHY_IT_MATTERS = (
    "Broad-spectrum insecticides have been implicated in pollinator decline and "
    "routinely destroy the natural enemies that were quietly suppressing "
    "secondary pests, producing outbreaks worse than the original problem. "
    "Biological control avoids that trap and leaves no residue, which matters "
    "for export markets with tight maximum residue limits and, more directly, "
    "for the farm workers doing the spraying, since much of the world's "
    "insecticide is applied by hand without protective equipment. It is also "
    "the only tool that still works once a pest has evolved resistance to every "
    "registered chemical, a situation now ordinary in horticulture. Against "
    "that: these products act slowly, and a grower watching a crop being eaten "
    "while a fungus takes a week to kill is making a decision under real "
    "pressure. They cost more per hectare and demand more knowledge, because "
    "using them well means monitoring pest populations rather than spraying on "
    "a calendar. And the registration system was designed for synthetic "
    "molecules, so a product with a small single-species market still faces a "
    "dossier priced for a blockbuster, which is why the sector is dominated by "
    "a handful of organisms that were registered decades ago."
)
