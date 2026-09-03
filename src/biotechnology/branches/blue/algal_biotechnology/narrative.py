# =============================================================================
#  biotechnology.branches.blue.algal_biotechnology.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `white.biofuels` records the algal fuel disappointment and points here for
#  where algal biotechnology actually succeeded. This record has to carry both
#  halves honestly, and the honest account is a single sentence:
#
#      THE BIOLOGY WAS NEVER THE PROBLEM. THE HARVEST WAS.
#
#  Microalgae genuinely are among the most productive photosynthetic organisms
#  known, and the projections made for them in the 2000s were not fabricated.
#  What defeated the fuel programmes is that a culture is a very dilute
#  suspension, commonly around one gram of dry biomass per litre, so producing
#  a tonne of anything means processing something like a thousand tonnes of
#  water. Concentrating that costs energy, and for a product worth a few
#  hundred euro a tonne the energy costs more than the product.
#
#  THE COROLLARY IS WHERE THE FIELD SUCCEEDED. The same harvest cost is
#  irrelevant when the product is worth tens of thousands of euro a tonne. So
#  algal biotechnology works, profitably and at scale, in pigments,
#  nutraceuticals and speciality lipids, and fails in fuel. That is one
#  constraint producing both outcomes, and this record is organised to show it.
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
    "Cultivation of microalgae and cyanobacteria for pigments, lipids, "
    "proteins and speciality compounds, and the harvest cost that governs it."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what the organisms offer, (b) the two cultivation systems and
#  their trade, (c) the harvest constraint, (d) what it implies about which
#  products exist.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the promise, stated accurately
    "Algal biotechnology cultivates microalgae and cyanobacteria for the "
    "compounds they produce. The organisms are attractive for reasons that are "
    "genuine rather than promotional: they convert light and carbon dioxide "
    "directly, achieve areal productivities above those of terrestrial crops, "
    "require no arable land, can grow on saline or waste water, and include "
    "species that accumulate lipid, protein or pigment to a very large fraction "
    "of their dry mass. Several make compounds that no crop plant makes at all. "
    # (b) the two systems
    "Two cultivation systems exist and the choice between them is the field's "
    "central engineering decision. Open ponds are cheap to build and operate, "
    "and accept whatever arrives: contamination, grazers, weather and the "
    "seasonal collapse of the intended species. They suit robust organisms "
    "growing under conditions few competitors tolerate, such as extreme "
    "alkalinity or extreme salinity, which is why the successful open-pond "
    "species are precisely those with a chemical moat around them. Closed "
    "photobioreactors give control, higher cell density and reliable species "
    "purity, at a capital cost per unit of output that only a valuable product "
    "can carry. Light penetration limits both: a dense culture shades itself "
    "within centimetres, so a reactor cannot simply be made deeper. "
    # (c) the constraint
    "The constraint that governs the economics is harvest. Culture densities "
    "are low, commonly around a gram of dry biomass per litre, so recovering a "
    "tonne of biomass means separating it from roughly a thousand tonnes of "
    "water. Centrifugation works and is energy-intensive; flocculation is "
    "cheaper and contaminates the product; filtration blocks. Dewatering and "
    "drying then follow, and cell disruption after that, since many algal cells "
    "have walls that resist extraction. "
    # (d) the consequence
    "What follows determines which products exist. Where the product is worth "
    "tens of thousands of euro a tonne, the harvest cost is a detail and the "
    "field is commercially successful: pigments, carotenoids, long-chain "
    "omega-3 lipids and protein supplements are produced profitably at "
    "industrial scale. Where the product competes with a commodity, the same "
    "cost is fatal, which is why algal fuel absorbed substantial investment in "
    "the late 2000s and largely did not arrive. The biology was never the "
    "obstacle."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Algae are tiny plants that grow in water, using sunlight and carbon "
    "dioxide, without needing soil or farmland. Some of them are extraordinary "
    "producers: they can double in a day and fill themselves with oil, protein "
    "or brightly coloured pigments. The problem is not growing them, it is "
    "getting them out of the water. A tank of algae is mostly water, so "
    "collecting a tonne of algae means dealing with about a thousand tonnes of "
    "liquid, and separating that takes a great deal of energy. If what you are "
    "making is expensive, that hardly matters and the business works well. If "
    "you are making fuel, which is cheap, it matters enormously and the "
    "business does not work at all."
)

# -----------------------------------------------------------------------------
#  The panning analogy. Chosen because it makes the dilution problem physical
#  rather than numerical, and because its limit carries the record's central
#  point: the value of what you are recovering decides whether the labour is
#  worth it.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is panning a river. The work is not in the finding, since the material "
    "is genuinely there and evenly spread, but in the sheer quantity of water "
    "you must move to collect any of it. That is why people pan for gold and "
    "not for sand. Both are in the river; only one repays the effort of "
    "separating it out."
)

WHY_IT_MATTERS = (
    "Algae supply things that have no comfortable alternative. Long-chain "
    "omega-3 fatty acids are made by marine microalgae, and the fish that are "
    "normally harvested for them are simply concentrating what they ate, so "
    "growing the algae directly removes a step from a fishery under pressure "
    "and supplies people who eat no fish. Astaxanthin from microalgae is the "
    "pigment that makes farmed salmon pink and one of the more valuable "
    "products in this record. Spirulina and chlorella have been eaten as "
    "protein for decades and grow without arable land or fresh water. Algae can "
    "be cultivated on saline water, on wastewater, and in coupling with "
    "industrial carbon dioxide, none of which competes with food production. "
    "The costs are as real as the benefits and this record does not soften "
    "them. Harvest and dewatering dominate the energy budget and defeat any "
    "low-value product. Open ponds are vulnerable to contamination, grazing and "
    "weather, so a crop can be lost in days. Photobioreactors avoid that at a "
    "capital cost most products cannot bear. Land use is genuinely low but "
    "water use, nutrient demand and the fertiliser required are not trivial. "
    "And the fuel programmes of the late 2000s consumed substantial public and "
    "private money against projections that extrapolated laboratory "
    "productivity to open systems, which is a mistake worth recording rather "
    "than passing over."
)
