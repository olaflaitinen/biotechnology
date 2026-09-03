# =============================================================================
#  biotechnology.branches.yellow.biofortification.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is about a problem most readers of this library will never have
#  had, and the narrative has to establish that before anything else.
#
#  HIDDEN HUNGER IS NOT HUNGER. A person eating enough calories every day can
#  be severely deficient in iron, zinc or vitamin A, because a diet built on a
#  single staple cereal supplies energy and very little else. The consequences
#  are permanent: childhood blindness, impaired cognitive development,
#  increased maternal and child mortality. It affects billions of people and it
#  is invisible in any measure based on calories.
#
#  THE ARGUMENT FOR BIOFORTIFICATION IS NOT THAT IT IS BETTER THAN THE
#  ALTERNATIVES. Supplementation works. Industrial fortification of flour, salt
#  and oil works and is among the most cost-effective public health
#  interventions there is. The argument is that both require a delivery system,
#  and the people most affected are subsistence farmers who eat what they grow
#  and do not buy processed flour or reach a clinic. A nutrient bred into the
#  seed reaches them because it travels with the crop.
#
#  THAT IS ALSO ITS LIMITATION. It works for staple crops in populations that
#  grow and eat them, and it is not an intervention for anyone else.
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
    "Raising the micronutrient content of staple crops by breeding or "
    "engineering, so the nutrient travels with the seed rather than through a "
    "supply chain."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the problem, (b) why a nutrient in the seed is different from
#  a nutrient in a supplement, (c) the two routes and why one has delivered far
#  more, (d) the constraints, including the one that is not agronomic.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the problem
    "Biofortification raises the micronutrient content of staple food crops "
    "through the crop itself. The problem it addresses is micronutrient "
    "deficiency, sometimes called hidden hunger, in which a diet supplies "
    "sufficient energy and insufficient iron, zinc, vitamin A or other "
    "micronutrients. It is a consequence of dietary monotony rather than of "
    "food shortage, it affects billions of people, and its effects on "
    "cognitive development, immune function, maternal mortality and vision are "
    "permanent where they occur in childhood. "
    # (b) why the seed matters
    "The distinguishing feature is the delivery mechanism rather than the "
    "nutrition. Supplementation and industrial fortification both work and both "
    "are cost-effective, and both require a person to reach a clinic or to buy "
    "centrally processed food. The populations with the highest deficiency "
    "rates are frequently subsistence farmers who consume what they grow, and "
    "for them a nutrient bred into the seed arrives with the harvest and "
    "requires no continuing programme, no purchase and no behaviour change. "
    "That is a delivery argument, and it is the whole argument. "
    # (c) the two routes
    "Two routes exist and their records differ sharply. Conventional breeding "
    "and marker-assisted selection exploit existing variation, and where the "
    "variation is sufficient this route has delivered varieties at scale: "
    "iron-biofortified beans and pearl millet, zinc-biofortified wheat and "
    "rice, and provitamin A orange-fleshed sweet potato, maize and cassava are "
    "in farmers' fields across many countries. Genetic engineering is required "
    "where the pathway does not exist in the crop at all, which is the case for "
    "provitamin A in rice endosperm, and that route has produced far more "
    "scientific attention and far less deployed food. "
    # (d) the constraints
    "The constraints are agronomic, nutritional and political in roughly equal "
    "measure. A biofortified variety must yield as well as the one it replaces, "
    "because a farmer will not accept less harvest for a nutrient they cannot "
    "see. The nutrient must survive processing and cooking, and must be "
    "absorbed, which for iron and zinc is limited by the phytate in the same "
    "cereals. Consumer acceptance matters where the trait is visible, as it is "
    "for orange maize in populations accustomed to white. And where the route "
    "is genetic engineering, the regulatory and political position has been "
    "decisive rather than incidental, as the history of provitamin A rice "
    "demonstrates."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Billions of people eat enough food and still do not get enough iron, zinc "
    "or vitamin A, because their diet is built around one staple crop that "
    "supplies energy and little else. The results are permanent: children go "
    "blind, do not develop properly, and are more likely to die of ordinary "
    "infections. Vitamin pills and added nutrients in flour both work, and both "
    "need the person to buy something or visit a clinic. Many of the people "
    "most affected grow their own food and do neither. Biofortification puts "
    "the nutrient in the seed instead, so it arrives with the harvest, every "
    "year, without anyone having to do anything differently."
)

# -----------------------------------------------------------------------------
#  The water treatment analogy. Chosen because it captures the delivery
#  argument exactly and is familiar, and because its limit carries the record's
#  own boundary: treating a supply only reaches people connected to it.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is adding fluoride to a water supply rather than handing out tablets. "
    "The tablets work, and they require somebody to collect them and remember "
    "to take them, every day, indefinitely. Treating the supply reaches "
    "everyone who drinks the water without asking anything of them. The "
    "comparison also carries the limitation honestly: it reaches only the "
    "people connected to that supply, and a household growing a different crop "
    "is a household on a different pipe."
)

WHY_IT_MATTERS = (
    "Micronutrient deficiency affects billions of people, and its consequences "
    "in childhood are irreversible. Vitamin A deficiency remains a leading "
    "cause of preventable childhood blindness and increases mortality from "
    "ordinary infections. Iron deficiency anaemia impairs cognitive development "
    "and contributes to maternal death. Zinc deficiency increases the severity "
    "of diarrhoeal disease, which kills large numbers of small children. "
    "Biofortified varieties are in farmers' fields in many countries, and "
    "orange-fleshed sweet potato in particular has been distributed at "
    "considerable scale with measured effects on vitamin A status. The costs "
    "and limitations deserve stating with equal precision. Biofortification "
    "reaches people who grow and eat the staple, which is a real population and "
    "not everyone. Yield parity is a hard requirement rather than a "
    "preference, since a farmer will not trade harvest for an invisible "
    "nutrient. Bioavailability limits what a content figure means, because the "
    "phytate in cereals binds the iron and zinc being added. Visible traits "
    "meet consumer resistance, and orange maize in a population accustomed to "
    "white maize is a marketing problem before it is a nutritional one. And "
    "where the nutrient requires genetic engineering, the twenty-year "
    "regulatory and political history of provitamin A rice is a caution about "
    "assuming that a demonstrated benefit produces deployment."
)
