# =============================================================================
#  biotechnology.branches.blue.marine_biofouling_control.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record closes the blue branch and it is the only one that treats marine
#  life as the ADVERSARY rather than the resource. Everything humans put into
#  the sea is colonised within hours, and preventing that is a large industry
#  in its own right.
#
#  THE SCALE IS THE REASON IT MATTERS AND IT IS EASY TO MISS. A fouled hull
#  increases drag substantially, and a large fraction of world trade moves by
#  sea, so hull coatings are among the most consequential surface treatments in
#  the world for fuel consumption and emissions. This is an environmental
#  technology that is not usually filed as one.
#
#  THE RECORD'S CENTRAL LESSON IS A REGULATORY ONE, AND IT IS THE CLEAREST
#  CASE OF ITS KIND IN THE LIBRARY. Tributyltin was an outstandingly effective
#  antifouling agent. It was also an endocrine disruptor that caused imposex in
#  molluscs at concentrations in the nanograms per litre, devastating shellfish
#  populations near ports and shipping lanes. It was banned globally in 2008.
#
#  A technology can be excellent at its stated purpose and unacceptable, and
#  the two judgements are independent. This record is written around that.
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
    "Preventing marine organisms from colonising submerged surfaces, and the "
    "shift from broad-spectrum biocides to non-toxic and biological methods."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what fouling is and why it is inevitable, (b) what it costs,
#  (c) the biocide era and its end, (d) the four alternatives and their
#  limitations.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the process
    "Biofouling is the colonisation of any submerged surface by marine "
    "organisms, and it proceeds in a sequence that is well described and "
    "difficult to interrupt. Within minutes a conditioning film of dissolved "
    "organic molecules adsorbs; within hours bacteria attach and form a "
    "biofilm; within days diatoms and protozoa follow; and within weeks the "
    "larvae of barnacles, mussels, tubeworms and bryozoans settle on what has "
    "already accumulated. Each stage prepares the surface for the next, which "
    "is why the biofilm stage matters out of proportion to its mass: prevent "
    "it and much of what follows does not arrive. "
    # (b) the cost
    "The cost is chiefly hydrodynamic. A fouled hull increases frictional drag "
    "substantially, and since most world trade moves by sea, the aggregate fuel "
    "and emissions consequence is large enough that hull coatings are a "
    "climate technology whether or not they are described as one. Fouling also "
    "blocks seawater intakes and heat exchangers, fouls aquaculture nets to the "
    "point of restricting water exchange, degrades sensor and instrument "
    "performance, and transports species between ports on hulls, which is a "
    "principal vector for marine invasions. "
    # (c) the biocide era and its end
    "For decades the answer was a broad-spectrum biocide released slowly from "
    "a coating. Tributyltin was exceptionally effective and was banned "
    "globally in 2008 after it was shown to cause imposex in molluscs at "
    "concentrations in the nanograms per litre, with severe effects on "
    "shellfish populations near ports. Copper-based coatings replaced it and "
    "are themselves under regulatory pressure, since copper is toxic to "
    "non-target organisms and accumulates in sediment in enclosed harbours. The "
    "field's history is largely a sequence of effective biocides being "
    "withdrawn. "
    # (d) the alternatives
    "Four approaches now compete, and none is a complete replacement. "
    "Foul-release coatings use very low surface energy silicone or fluoropolymer "
    "so that organisms attach weakly and are removed by the vessel's own motion, "
    "which works well above a threshold speed and poorly for a vessel that sits "
    "idle. Biomimetic surface texturing copies the microtopography of shark "
    "skin and other naturally resistant surfaces, and performs well in the "
    "laboratory while proving difficult to maintain on a hull for years. "
    "Natural product antifoulants, drawn from the chemistry that keeps sessile "
    "marine organisms clean, are effective and face the supply constraint that "
    "governs `blue.marine_natural_products`. Enzymatic and quorum-sensing "
    "approaches attack the biofilm stage rather than the settled organism, "
    "which is the most promising direction and the least commercially "
    "established."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Anything left in the sea gets covered in life. Within hours there is a "
    "slime of bacteria, and within weeks barnacles, mussels and weed. On a "
    "ship this is expensive: a rough, fouled hull drags through the water and "
    "burns far more fuel, and since most of world trade goes by sea, ship "
    "paint turns out to be one of the more important surfaces on the planet "
    "for fuel use. The old solution was paint that poisoned anything touching "
    "it. It worked extremely well and it poisoned a great deal else besides, "
    "so it was banned. The newer approaches try to make surfaces that nothing "
    "can grip, rather than surfaces that kill."
)

# -----------------------------------------------------------------------------
#  The non-stick pan analogy. Chosen because it captures the actual mechanism
#  of foul-release coatings, which is release rather than prevention, and
#  because its stated limit is the honest one: a pan that is never used still
#  gets dirty.
# -----------------------------------------------------------------------------
ANALOGY = (
    "The modern approach is a non-stick pan rather than a strong detergent. "
    "Nothing is killed and nothing is dissolved; things simply cannot get a "
    "grip, and ordinary movement takes them away. The limit is the same as with "
    "the pan: it works when the surface is in use. A ship that sits in harbour "
    "for a month, like a pan left on the side, accumulates whatever settles on "
    "it, because there is nothing to sweep it clean."
)

WHY_IT_MATTERS = (
    "The fuel consequence is large and unglamorous. Effective hull coatings "
    "reduce drag across the world fleet, and the emissions avoided are "
    "substantial enough that this is a climate technology filed under marine "
    "paint. Fouling on aquaculture nets restricts the water exchange that "
    "farmed fish depend on, so it is a welfare and a disease question as well "
    "as a maintenance one. Hull fouling is a principal vector for marine "
    "invasive species, which move between ports attached to vessels rather "
    "than in ballast water alone. And this record contains the library's "
    "clearest instance of a technology that was excellent and unacceptable at "
    "once: tributyltin worked outstandingly well and caused reproductive "
    "damage in molluscs at concentrations of nanograms per litre, and the two "
    "facts were both true for years before the second was acted on. Its "
    "replacement, copper, is now under the same pressure for weaker versions "
    "of the same reason. The alternatives all have honest limitations. "
    "Foul-release coatings need the vessel to move. Textured surfaces perform "
    "in a laboratory and are hard to sustain on a hull for years. Natural "
    "antifoulants meet the supply problem that constrains the whole branch. "
    "And cleaning a fouled hull in the water releases both the accumulated "
    "organisms and the coating's own biocide into the harbour, which turns "
    "maintenance into a regulated activity in its own right."
)
