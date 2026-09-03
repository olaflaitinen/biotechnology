# =============================================================================
#  biotechnology.branches.yellow.alternative_proteins.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record covers proteins that REPLACE animal protein by resembling it,
#  which is a different proposition from `yellow.precision_fermentation`, where
#  the molecule is the animal molecule. That record makes a copy; this one
#  makes a description.
#
#  THE FACT THE RECORD IS BUILT ON IS THAT PROTEIN IS NOT THE PROBLEM. Nobody
#  in a wealthy market is short of protein, and a product sold on protein
#  content alone is competing with dried beans. What these products actually
#  sell is the EXPERIENCE of meat without the animal, and that means texture,
#  flavour, appearance, cooking behaviour and price simultaneously. It is a
#  materials engineering problem wearing a nutrition label.
#
#  THE SECOND FACT IS THE ONE THE SECTOR FOUND OUT EXPENSIVELY. Between roughly
#  2019 and 2023 plant-based meat grew rapidly and then contracted, and the
#  contraction was driven by repeat purchase rather than by trial. People
#  bought the products once and did not buy them again, on taste and price. A
#  category can have excellent trial rates and fail, and that is recorded here
#  as a setback rather than passed over.
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
    "Protein foods from plants, fungi and insects intended to replace animal "
    "products by resembling them in use rather than in molecule."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the four sources and what distinguishes them, (b) why the
#  problem is texture rather than protein, (c) what the processing actually
#  does, (d) the constraints, which are sensory, economic and reputational.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the four sources
    "Alternative proteins are foods that supply protein without an animal and "
    "that are intended to occupy the place an animal product occupied. Four "
    "sources dominate. Plant protein, chiefly from soy, pea, wheat gluten and "
    "increasingly from other legumes, is the largest and the cheapest. Fungal "
    "protein, produced by fermenting a filamentous fungus, has a fibrous "
    "structure that plant protein has to be engineered to imitate and has been "
    "sold since 1985. Insect protein is efficient to produce and faces an "
    "acceptance problem in most Western markets that is not technical. And "
    "microbial and gas-fermented single cell protein sits at the boundary with "
    "`white.microbial_fermentation`, entering mainly as animal feed where "
    "consumer acceptance does not arise. "
    # (b) the real problem
    "The engineering problem is not protein supply. Protein is abundant and "
    "cheap in plant form, and a product sold on protein content competes with "
    "dried beans at a fraction of the price. What these products sell is the "
    "experience of an animal product, which requires texture, flavour, "
    "appearance during cooking, mouthfeel and price to be right at once. Meat "
    "is an anisotropic fibrous material whose structure comes from muscle, and "
    "reproducing that from a globular plant protein is a materials problem "
    "rather than a nutritional one. "
    # (c) what the processing does
    "The processing reflects that. Extrusion, in which protein is heated, "
    "sheared and forced through a die, aligns molecules into fibres and is the "
    "core technology of the sector; high-moisture extrusion produces something "
    "closer to whole muscle than the textured protein of earlier decades. "
    "Shear cell processing and fibre spinning pursue the same alignment by "
    "other means. Fermentation-derived flavours and heme proteins supply what "
    "plant protein does not taste of, and fat structuring addresses the fact "
    "that much of what people identify as meat flavour is released from fat "
    "during cooking. "
    # (d) the constraints
    "The constraints are sensory, economic and reputational rather than "
    "technical. Repeat purchase depends on taste and price, and between 2019 "
    "and 2023 the sector demonstrated that a category can achieve wide trial "
    "and still contract when repeat purchase does not follow. Price parity with "
    "commodity meat has not been reached for most products. And the sector "
    "acquired a health liability it did not anticipate, since the "
    "classification of these products as ultra-processed placed them in a "
    "category consumers were simultaneously being advised to avoid."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "These are foods made from plants, fungi or insects that are meant to be "
    "used the way meat is used. The difficulty is not getting enough protein "
    "into them, because beans and peas are full of protein and cost very "
    "little. The difficulty is that meat is not just protein: it has a grain, "
    "it holds together in a particular way, it browns, and much of what people "
    "recognise as the taste comes out of the fat while it cooks. So most of "
    "the work is about structure and flavour rather than nutrition. The "
    "products sold in the last few years showed that people will try them "
    "readily and will only buy them again if they taste good and do not cost "
    "more."
)

# -----------------------------------------------------------------------------
#  The upholstery analogy. Chosen because it separates composition from
#  structure, which is the record's central point, and because its limit is
#  honest: nobody eats a chair, and a food is judged by senses that a material
#  specification does not capture.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is upholstery rather than nutrition. The stuffing is not the hard "
    "part; anyone can supply protein, as anyone can supply foam. What is "
    "difficult is the covering, the grain, the way it gives when pressed and "
    "springs back. The comparison fails in the way that matters most: nobody "
    "eats a chair, and a food is judged by taste and smell, which no "
    "specification captures and which decide whether it is bought twice."
)

WHY_IT_MATTERS = (
    "Livestock occupies most of the world's agricultural land while supplying a "
    "minority of its calories and protein, and it is a substantial source of "
    "methane. Substituting even part of that has a large arithmetic effect, and "
    "the substitutes are genuinely more efficient: fungal protein and insect "
    "protein convert feed into edible protein far better than ruminants do. "
    "Fungal protein has been sold for four decades, which makes this a mature "
    "category rather than an emerging one in at least one of its forms. And "
    "insect protein in animal feed addresses the fishmeal demand recorded in "
    "`blue.aquaculture_biotechnology` without asking any consumer to change "
    "what they eat. The costs are specific and were learned expensively. The "
    "sector grew rapidly to 2019 and then contracted, on taste and on price "
    "rather than on availability or awareness, which is a lesson about repeat "
    "purchase that no amount of trial data predicts. Price parity with "
    "commodity meat remains unreached for most products, and meat is cheap "
    "partly because it is supported. The ultra-processed classification "
    "attached to many of these products is a genuine reputational problem and "
    "not merely a misunderstanding, since a long ingredient list is a fair "
    "description of how the texture is achieved. Soy and pea protein depend on "
    "crops with their own land and water demands, so the environmental case is "
    "comparative rather than absolute. And insect protein faces an acceptance "
    "barrier in Western markets that has no technical solution and that most "
    "companies have responded to by selling into feed instead."
)
