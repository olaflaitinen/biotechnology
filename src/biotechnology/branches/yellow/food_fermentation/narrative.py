# =============================================================================
#  biotechnology.branches.yellow.food_fermentation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the oldest record in the library and the narrative has to resist a
#  temptation the subject invites, which is to treat the traditional practice
#  as a charming prelude to the science.
#
#  IT IS NOT A PRELUDE. Most fermented food in the world today is still made by
#  processes worked out empirically over centuries, and several of them remain
#  poorly understood. Sourdough, kimchi, natto, injera, ogi and a great many
#  regional products are communities of organisms rather than defined cultures,
#  and reproducing them from a defined starter frequently produces something
#  that is not the same food. The science has explained a great deal and has
#  not replaced the craft.
#
#  WHAT THE SCIENCE DID CHANGE IS REPRODUCIBILITY AT SCALE. A bakery that
#  cannot afford to lose a batch, a dairy that ships a million yoghurts a week,
#  and a brewery that must taste the same in March and September all need
#  something a village practice never needed: the same result every time. That
#  is the actual achievement, and it sounds smaller than it is.
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
    "Controlled microbial transformation of food and drink, the oldest "
    "biotechnology and still among the largest by volume."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what fermentation does, which is four things at once,
#  (b) defined cultures against communities, (c) what the science actually
#  contributed, (d) the constraints, which include one that is cultural.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the four functions
    "Food fermentation uses microbial metabolism to transform a raw material "
    "into something more stable, more digestible, safer or simply better. Those "
    "four functions are usually achieved together and it is worth separating "
    "them. Preservation comes from acid, alcohol and competition: organisms "
    "that drop the pH or produce ethanol exclude the ones that would spoil the "
    "food or poison the eater, which is why fermentation is a preservation "
    "technology that needs no refrigeration. Digestibility improves because "
    "microbial enzymes break down what human enzymes cannot, including lactose, "
    "phytate and some antinutritional factors. Safety improves because "
    "controlled acidification is a reliable barrier to pathogens. And flavour "
    "develops because the organisms generate hundreds of volatile compounds "
    "that no ingredient supplies directly. "
    # (b) defined against community
    "Two kinds of fermentation exist and the distinction runs through the whole "
    "field. Defined starter cultures are known organisms, propagated and added "
    "deliberately, which gives reproducibility and control. Spontaneous or "
    "backslopped fermentations rely on organisms already present in the raw "
    "material or carried over from the previous batch, and they are communities "
    "rather than cultures. Much of the world's fermented food is made the second "
    "way, and the resulting products frequently cannot be reproduced from a "
    "defined starter, because the succession of organisms over time is part of "
    "what makes them. "
    # (c) what science contributed
    "The scientific contribution has been reproducibility rather than "
    "invention. Pure culture technique made starters possible, which allowed a "
    "dairy to produce the same yoghurt every day. Strain selection improved "
    "acidification rate, flavour and phage resistance. Process control replaced "
    "judgement with measurement. And molecular methods finally made it possible "
    "to see what is actually present in a community fermentation, which for most "
    "traditional foods had never been known. "
    # (d) the constraints
    "The constraints are unusual for this library. Bacteriophage infection is "
    "the dairy industry's chronic operational problem and can idle a plant. "
    "Starter culture supply is concentrated in a small number of companies. "
    "And there is a constraint that is cultural rather than technical: a "
    "traditional fermented food is frequently the property of a community and a "
    "place, and industrialising it raises questions about ownership, "
    "authenticity and benefit that no amount of process control answers."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Fermentation is letting helpful microbes change food on purpose. It is the "
    "oldest thing in this entire library: bread, cheese, yoghurt, beer, wine, "
    "soy sauce, kimchi and vinegar are all made this way, and people were doing "
    "it for thousands of years before anyone knew microbes existed. It does "
    "four useful things at once. It keeps food from spoiling, without a fridge. "
    "It makes food easier to digest. It makes food safer, because the acid the "
    "microbes produce keeps dangerous bacteria out. And it tastes good, which "
    "is not a small point: almost nothing in this list would have survived if "
    "it did not."
)

# -----------------------------------------------------------------------------
#  The gardening analogy. Chosen because it captures what a fermenter actually
#  does, which is not building but managing a competition, and because its
#  limit carries the community-fermentation point: a garden is not a factory
#  and cannot be specified the same way.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is gardening rather than manufacturing. Nothing is built; conditions "
    "are set so that the organisms you want outcompete the ones you do not, and "
    "then you wait. The limit of the comparison is the useful part. A gardener "
    "can describe what is growing; the traditional fermenter often cannot, "
    "because a community of dozens of species arriving in succession is doing "
    "the work, and specifying it would change what grows."
)

WHY_IT_MATTERS = (
    "Fermented food is a very large fraction of what humans eat, and in much of "
    "the world it is the preservation technology that works without electricity "
    "or a cold chain. That is not a historical point: it remains how a great "
    "deal of food is kept edible today. Fermentation makes staple foods "
    "digestible that otherwise are not, breaking down lactose for people who "
    "cannot, and reducing the phytate that blocks iron and zinc absorption in "
    "cereals and legumes, which connects this record directly to the "
    "deficiencies `yellow.biofortification` addresses from the other end. It "
    "removes toxins, most strikingly in cassava processing, where fermentation "
    "reduces cyanogenic compounds that would otherwise make a staple crop "
    "dangerous. The costs are real and unevenly distributed. Bacteriophage "
    "infection can stop a dairy plant, and there is no vaccination for a "
    "starter culture. Starter supply is concentrated in a few companies, which "
    "leaves producers dependent. Industrialisation has narrowed the microbial "
    "diversity of foods that were once regionally distinct, and a defined "
    "starter is not always able to reproduce what a community fermentation "
    "produced. And traditional fermented foods belong to communities and "
    "places: taking one, characterising its organisms, and selling a defined "
    "culture back is legally permitted in most places and is not obviously "
    "fair, which is a question this record records rather than settles."
)
