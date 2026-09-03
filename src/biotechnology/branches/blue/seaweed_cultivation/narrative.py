# =============================================================================
#  biotechnology.branches.blue.seaweed_cultivation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has to correct an assumption that most readers of this library
#  will arrive with, and the correction is placed first in both registers.
#
#      SEAWEED FARMING IS NOT AN EMERGING TECHNOLOGY. IT IS ONE OF THE LARGEST
#      FORMS OF AQUACULTURE IN THE WORLD, IT HAS BEEN INDUSTRIAL FOR DECADES,
#      AND ALMOST ALL OF IT HAPPENS IN ASIA.
#
#  Tens of millions of tonnes are produced annually, overwhelmingly in China,
#  Indonesia, the Republic of Korea, the Philippines and Japan. European and
#  North American seaweed farming is genuinely emerging; the industry is not.
#  Writing this record from a European vantage point would misdescribe the
#  subject entirely, which is a specific instance of the geographic lean that
#  `CHANGELOG.md` records as a known limitation of the whole project.
#
#  THE SECOND CORRECTION IS THE BOUNDARY WITH `blue.algal_biotechnology`. That
#  record is governed by a harvest problem: microalgae are single cells in
#  dilute suspension and separating them from water dominates the economics.
#  Seaweed is large. It is grown on ropes and lifted out of the sea. The
#  constraint that defines the neighbouring record does not exist here at all,
#  and that single difference explains why seaweed is farmed at tens of
#  millions of tonnes and microalgae at tens of thousands.
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
    "Farming macroalgae at sea for food, hydrocolloids and feed, one of the "
    "largest forms of aquaculture and requiring no land, fresh water or feed."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the scale and where it is, (b) what makes it unusual as
#  farming, (c) the two products and the two industries, (d) the constraints,
#  which are biological and social rather than technical.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the scale, stated first because it corrects the assumption
    "Seaweed cultivation grows macroalgae on ropes, nets and rafts in coastal "
    "water. It is among the largest aquaculture sectors in the world by tonnage, "
    "producing tens of millions of tonnes a year, and the great majority of "
    "that production is in East and Southeast Asia. The industry is mature, "
    "employs very large numbers of people, and predates most of what this "
    "library describes. Cultivation in Europe and North America is recent by "
    "comparison and small. "
    # (b) what makes it unusual
    "It is unusual among forms of farming in requiring almost nothing. There "
    "is no land, no fresh water, no fertiliser and no feed: the crop takes "
    "nitrogen, phosphorus and carbon from the seawater around it and light from "
    "above. That property is why the same activity appears as food production, "
    "as a nutrient removal service and as a climate proposal, and why claims "
    "about it need to be read carefully, since a genuine advantage attracts "
    "exaggerated versions of itself. "
    # (c) two products, two industries
    "Two distinct industries sit under one heading. The first is food. Whole "
    "seaweed has been eaten for centuries in Japan, Korea and China, and the "
    "cultivated species grown for it are the largest tonnages in the sector. "
    "The second is hydrocolloids: agar, carrageenan and alginate, extracted "
    "polysaccharides that gel, thicken and stabilise, and that appear in a very "
    "large share of processed food, in pharmaceutical formulation, in "
    "microbiology media and in dentistry. The two industries use different "
    "species, different regions and different economics, and conflating them "
    "produces confused statements about the sector's value. "
    # (d) the constraints
    "The constraints are not technical. Farming methods for the major species "
    "are well established and require little capital. What limits the sector is "
    "biological and social: disease and epiphyte outbreaks that spread quickly "
    "through a monoculture of clonal material; genetic narrowness in stock that "
    "has been vegetatively propagated for decades; the labour intensity of "
    "seeding and harvesting, which is why production sits where labour is "
    "available; competition for coastal space with fishing, shipping, tourism "
    "and conservation; and the fact that a crop grown in coastal water "
    "accumulates whatever the water contains, including heavy metals and "
    "iodine."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Seaweed farming means growing seaweed on ropes in the sea. It is already "
    "enormous, mostly in Asia, and it has been for a long time. What makes it "
    "remarkable is what it does not need: no land, no fresh water, no "
    "fertiliser and no feed, because seaweed takes what it needs from the water "
    "and the sunlight. Some of it is eaten directly, and the rest is processed "
    "into thickeners that are in a great deal of ordinary food, in medicines "
    "and in the jelly a dentist uses to take an impression of your teeth. Most "
    "people have eaten seaweed extract today without knowing it."
)

# -----------------------------------------------------------------------------
#  The orchard analogy. Chosen because seaweed farming is genuinely closer to
#  horticulture than to fishing, and because the analogy's stated limit carries
#  the record's principal risk: the sea is a shared space and an orchard is not.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is an orchard rather than a fishery. Nothing is hunted; the crop is "
    "planted on lines, tended and cut, and the same water grows it again next "
    "season. The comparison stops at the fence, and the missing fence is the "
    "difficulty: an orchard occupies ground somebody owns, while a seaweed farm "
    "occupies water that fishermen, shipping, tourism and conservation all have "
    "claims on, and none of them was asked."
)

WHY_IT_MATTERS = (
    "This is food production that competes for nothing. It uses no arable land "
    "and no fresh water at a time when both constrain agriculture, it adds no "
    "fertiliser, and it supports very large numbers of coastal livelihoods in "
    "regions with few alternatives, frequently including women who have limited "
    "access to other income. It removes nitrogen and phosphorus from coastal "
    "water, which is a genuine service where run-off from land has caused "
    "eutrophication. The hydrocolloids extracted from it are difficult to "
    "replace: agar underpins microbiology, and carrageenan and alginate are in "
    "a very wide range of foods and medicines. The costs and the overstatements "
    "both need naming. Disease and epiphyte outbreaks have collapsed "
    "regional industries within a season, and decades of vegetative propagation "
    "have left major crops genetically narrow and vulnerable. Seaweed "
    "accumulates what the water holds, so heavy metals and very high iodine "
    "content are real food safety questions rather than theoretical ones. "
    "Farms compete for coastal space and can damage the habitats they occupy. "
    "And the climate claims made for seaweed are the weakest part of the case: "
    "carbon fixed by a crop that is then eaten or processed returns to the "
    "atmosphere, so the durable sequestration sometimes claimed for cultivation "
    "is not what cultivation does."
)
