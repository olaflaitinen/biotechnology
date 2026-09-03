# =============================================================================
#  biotechnology.branches.white.biofuels.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the most contested record in the white branch, and the editorial
#  position is the same one taken in `green.plant_genetic_engineering`: report
#  the disagreement accurately, state what is actually settled, and decline to
#  adjudicate what is not.
#
#  WHAT IS GENUINELY SETTLED: that sugarcane ethanol returns far more energy
#  than it consumes; that maize ethanol returns much less and its exact figure
#  is disputed; that indirect land use change is real and its magnitude is
#  uncertain; and that cellulosic ethanol did not arrive at the scale that was
#  mandated for it.
#
#  WHAT IS NOT SETTLED: how to allocate emissions to co-products, how to price
#  land use change, and whether crop-based fuel was a transitional necessity or
#  a costly detour. A reader will find advocates of each in the literature, and
#  this record does not pretend the question closed.
#
#  The one number that deserves to be in the narrative rather than only in the
#  metrics is 0.51. Fermenting glucose to ethanol cannot exceed 0.51 grams of
#  ethanol per gram of sugar, because the remainder leaves as carbon dioxide by
#  stoichiometry. Roughly half the mass is lost before any engineering begins.
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
    "Producing liquid and gaseous transport fuels from biological feedstocks "
    "by fermentation, conversion or hydroprocessing."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the generations and what distinguishes them, (b) why the
#  second generation is hard, (c) the two questions that decide whether any of
#  it is worth doing, (d) where the demand now actually is.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the generations
    "Biofuels are conventionally described in generations. The first ferments "
    "sugar or starch to ethanol, or esterifies vegetable oil to biodiesel, "
    "using feedstocks that are also food. It is mature, it operates at very "
    "large scale, and it is the source of the field's central controversy. The "
    "second converts lignocellulosic residues, meaning straw, bagasse, forest "
    "residue and energy grasses, which do not compete directly for food. The "
    "third uses algae. A fourth category, made from carbon dioxide and "
    "renewable electricity, is really chemistry with a biological step "
    "optional. "
    # (b) why the second generation is hard
    "The second generation is where biotechnology matters most and where the "
    "field has disappointed most. Plant cell walls evolved specifically to "
    "resist microbial degradation, and that recalcitrance is the whole "
    "problem. Lignin must be disrupted by a pretreatment that is energy "
    "intensive and that generates furans and organic acids which inhibit the "
    "organisms in the next step. Cellulase enzyme loadings are high and their "
    "cost per litre of fuel has remained a principal barrier. And hydrolysis "
    "releases xylose alongside glucose, which the standard ethanol yeast does "
    "not naturally ferment, so the organism must be engineered to use a sugar "
    "it evolved to ignore. "
    # (c) the two questions
    "Two questions decide whether any biofuel is worth producing, and neither "
    "is answered by the fermentation. The first is energy return: how much "
    "energy the fuel delivers relative to the energy consumed growing, "
    "harvesting, transporting and converting it. The second is greenhouse gas "
    "intensity over the full life cycle, including the emissions caused when "
    "land is converted to grow the feedstock, or when displaced food "
    "production converts land elsewhere. That second effect, indirect land use "
    "change, is real, is difficult to measure, and can be large enough to "
    "reverse the apparent benefit of a crop-based fuel. "
    # (d) where demand is now
    "Demand has shifted accordingly. Road transport is electrifying, which "
    "removes the largest market that first generation fuels were built for. "
    "What cannot easily electrify is aviation, shipping and heavy freight, and "
    "the sector's centre of gravity has moved to drop-in fuels for those uses, "
    "particularly sustainable aviation fuel made from waste oils and residues "
    "rather than from crops."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Biofuels are fuels made from plants or waste rather than from oil wells. "
    "The simple version, turning maize or sugarcane into alcohol for cars, "
    "works and is made in enormous quantities. The argument about it is "
    "whether it is worth doing: growing the crop takes land, fertiliser, water "
    "and fuel, so the honest question is not whether you get energy out but how "
    "much is left after everything you put in. For sugarcane the answer is "
    "clearly favourable. For maize it is much closer, and people who have "
    "studied it carefully still disagree. The version that would avoid the "
    "argument entirely, making fuel from straw and other waste nobody eats, "
    "turned out to be far harder than expected, and most of the plants built "
    "to do it have closed."
)

# -----------------------------------------------------------------------------
#  The commute analogy. Chosen because energy return on investment is the
#  concept a reader most needs and least often meets, and because a wage
#  consumed by the cost of getting to work is immediately intuitive.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Judging a fuel by how much energy it contains is like judging a job by "
    "its salary while ignoring the commute. If most of the wage goes on "
    "getting to work, the number on the contract tells you very little. Some "
    "biofuels are a short walk from home and some are a long expensive drive, "
    "and the whole argument in this field is about which is which."
)

WHY_IT_MATTERS = (
    "Transport is one of the hardest sectors to decarbonise, and aviation, "
    "shipping and heavy freight have no near-term electric answer, so a liquid "
    "fuel that is not fossil remains genuinely necessary for them. Brazil has "
    "run a substantial share of its light vehicle fleet on sugarcane ethanol "
    "for decades, which is a real and large-scale demonstration rather than a "
    "proposal. Biogas from waste turns a disposal problem into an energy "
    "supply. Against that stand costs this record states plainly. Crop-based "
    "fuel competes for land, water and fertiliser with food, and the "
    "displacement effects reach countries that never produced the fuel. "
    "Cellulosic ethanol, the technology that would have resolved that "
    "conflict, was mandated in volumes it never came close to delivering, and "
    "most of the flagship plants built for it have closed. Algal fuel absorbed "
    "large investment in the late 2000s and largely redirected itself towards "
    "higher value products. And a fuel is a low-value, high-volume commodity "
    "competing against an incumbent with a century of cost optimisation and, "
    "in many jurisdictions, subsidies of its own. Biofuel policy has been "
    "unusually prone to mandating outcomes that the underlying technology "
    "could not supply, which is a lesson about policy design as much as about "
    "biology."
)
