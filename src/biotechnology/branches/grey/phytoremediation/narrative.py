# =============================================================================
#  biotechnology.branches.grey.phytoremediation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS IS THE ONE PLACE IN THE BRANCH WHERE A METAL CAN ACTUALLY BE REMOVED
#  FROM THE GROUND.
#
#  `grey.bioremediation` establishes that no organism destroys a metal, which
#  remains true here. But a plant can do something bacteria cannot: it can pull
#  a metal out of the soil, concentrate it in tissue above ground, and then be
#  cut down and carried away. The metal still exists, and it is now in a
#  compact, transportable form rather than dispersed through thousands of
#  tonnes of soil.
#
#      THAT IS EXTRACTION RATHER THAN DESTRUCTION, AND THE DISTINCTION MUST
#      BE HELD, BECAUSE THE HARVESTED BIOMASS IS NOW HAZARDOUS WASTE.
#
#  A phytoextraction project that does not plan for the disposal of its own
#  harvest has not finished the job. This is stated plainly because it is the
#  step most often left out of enthusiastic accounts.
#
#  THE SECOND THING TO ESTABLISH IS THAT MOST DEPLOYED PHYTOREMEDIATION DOES
#  NOT EXTRACT ANYTHING. The commonest real uses are hydraulic control, where
#  trees drink enough water to stop a plume moving, and stabilisation, where a
#  cover crop holds contaminated soil in place so it does not blow or wash
#  away. Those are containment. They work, they are cheap, and they leave the
#  contamination where it is.
#
#  THIRD: THE BINDING CONSTRAINT IS DEPTH AND TIME. Roots reach a few metres
#  at most, so anything deeper is out of scope entirely, and growing seasons
#  make decades a realistic timescale for extraction.
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
    "Using plants to extract, degrade, stabilise or hydraulically contain "
    "contamination, limited to the depth roots reach and to timescales "
    "measured in growing seasons."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the mechanisms, which are genuinely different from each
#  other, (b) the one thing plants can do that microbes cannot, and its
#  waste consequence, (c) what is actually deployed, (d) the constraints of
#  depth and time.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the mechanisms, kept separate because they have different endpoints
    "Phytoremediation uses plants to deal with contaminated soil, sediment and "
    "groundwater through several mechanisms that are frequently grouped under "
    "one name and have quite different endpoints. Phytoextraction moves a "
    "contaminant into harvestable tissue. Phytodegradation and "
    "rhizodegradation break organic contaminants down, the second by "
    "supporting microbial activity in the root zone rather than by any plant "
    "enzyme. Phytostabilisation immobilises a contaminant and holds soil in "
    "place. Phytovolatilisation moves a contaminant into the air. And "
    "hydraulic control uses the water demand of deep-rooted trees to hold a "
    "groundwater plume in place. Only the first removes anything from the "
    "site, only the second destroys anything, and the last two do neither. "
    # (b) the capability microbes lack, and its cost
    "Phytoextraction is the reason this record exists separately from "
    "`grey.bioremediation`. No organism destroys a metal, which remains true "
    "of plants. What a plant can do, and bacteria cannot, is concentrate a "
    "metal into above-ground tissue that is then cut and removed, converting a "
    "diffuse contamination through a large soil volume into a small mass of "
    "concentrated material. Certain hyperaccumulator species take up metal "
    "concentrations that would kill ordinary plants, and in a few cases the "
    "recovered metal has value, which is the practice called phytomining. The "
    "consequence has to be stated with the capability: the harvested biomass "
    "is contaminated and is generally hazardous waste, so a project that has "
    "not planned its disposal has not finished. "
    # (c) what is actually deployed, which is not extraction
    "In deployment the containment mechanisms dominate. Poplar and willow "
    "plantings that transpire enough water to arrest a plume are the most "
    "reliable application in the record and are used at many sites. Vegetative "
    "covers over mine tailings and contaminated fill prevent dust and erosion "
    "and are cheap enough to apply over large areas. Constructed wetlands "
    "treat mine drainage and run-off continuously. Rhizodegradation of "
    "petroleum hydrocarbons is real and is difficult to distinguish from what "
    "the soil community would have done unassisted. "
    # (d) the constraints
    "Two constraints define the scope. Roots reach a few metres at best, and "
    "deeper contamination is out of reach entirely rather than merely slow, so "
    "the technique does not compete for deep aquifer work. And plants grow on "
    "a seasonal schedule, so extraction is measured in years to decades, "
    "halts in winter, and depends on weather nobody controls. Against that, "
    "the cost per hectare is a small fraction of any engineered alternative, "
    "the site remains vegetated and usable, and the treatment continues "
    "without an operator."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Some plants will pull pollution out of the ground through their roots. "
    "Certain species take up remarkable amounts of metal, storing it in leaves "
    "and stems that can then be cut and taken away, which is the only way "
    "biology can genuinely get a metal out of soil. The metal is not "
    "destroyed, it is moved, so the cut plants are hazardous waste and have to "
    "be dealt with. Other plants break down fuel and solvent pollution, "
    "mostly by feeding the microbes around their roots. In practice the "
    "commonest uses are simpler than any of that: trees planted to drink so "
    "much water that polluted groundwater stops spreading, and grass planted "
    "to stop contaminated dust blowing off a site. It is very cheap, the site "
    "looks like a field rather than a works, and it takes years, because "
    "plants grow when they grow."
)

# -----------------------------------------------------------------------------
#  The chosen analogy is drainage rather than mining, because it carries the
#  slowness, the shallowness and the passivity in one image, and because the
#  harvest step is what distinguishes extraction from the rest.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is draining a wet field with grass and willows rather than digging a "
    "ditch. The ditch works this week and costs what earthmoving costs. The "
    "planting works over seasons, costs almost nothing, needs nobody to "
    "operate it, and only reaches as deep as roots go. And where the planting "
    "is cut and carted off, something has genuinely left the field, which is "
    "the part that separates extraction from merely holding the ground "
    "together."
)

WHY_IT_MATTERS = (
    "Cost and scale are the argument. Contaminated land exists in quantities "
    "that engineered treatment cannot economically address: mine tailings, "
    "smelter fallout, irrigated land accumulating metals, and large low-level "
    "industrial sites. Planting is cheap enough per hectare to apply across "
    "those areas, it requires no plant and no operator, and it leaves a site "
    "vegetated rather than fenced. Hydraulic control by tree planting is a "
    "genuinely reliable containment method at a small fraction of the cost of "
    "pumping and treating groundwater indefinitely. Constructed wetlands treat "
    "mine drainage continuously for decades on almost no input. "
    "The limits are firm. Roots reach a few metres, so deeper contamination is "
    "outside the technique rather than slow within it. Extraction timescales "
    "run to decades for a substantial reduction, which suits abandoned land "
    "and does not suit a development schedule. High concentrations kill the "
    "plants that were supposed to treat them. Chelate-assisted extraction "
    "raises uptake and simultaneously mobilises metal toward groundwater, "
    "which is why it is now restricted. Contaminated biomass is a waste stream "
    "the project must handle, and burning it concentrates rather than removes "
    "the metal. Volatilisation moves a contaminant into shared air, which is "
    "relocation rather than treatment and is regarded sceptically for that "
    "reason. And there is a pathway risk worth stating plainly: a plant that "
    "accumulates metal can be eaten by grazing animals or by insects, so a "
    "phytoextraction site is only safe if it is managed as a contaminated "
    "site and not as a meadow."
)
