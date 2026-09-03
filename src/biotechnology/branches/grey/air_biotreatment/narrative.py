# =============================================================================
#  biotechnology.branches.grey.air_biotreatment.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE ORGANISMS IN THIS RECORD DO NOT LIVE IN THE AIR. THEY LIVE IN A FILM OF
#  WATER, AND THE POLLUTANT HAS TO GET INTO THAT WATER FIRST.
#
#  This single fact explains almost everything about the field, including which
#  compounds it can treat and which it cannot. A biofilter is a wet packed bed
#  with a biofilm on it. Contaminated air passes through, a compound partitions
#  from the gas into the water, and only then is it available to be degraded.
#
#      SO THE LIMIT IS NOT WHAT THE ORGANISMS CAN EAT. IT IS WHAT WILL
#      DISSOLVE.
#
#  A poorly soluble compound passes through a perfectly healthy biofilter
#  untouched, because it never entered the phase where the organisms are. This
#  is the same bioavailability argument `grey.bioremediation` makes about
#  sorbed contaminant in soil, arriving here through gas-liquid partitioning
#  instead, and it is the reason a technique that handles hydrogen sulphide
#  beautifully handles chlorinated solvents badly.
#
#  THE SECOND THING TO ESTABLISH IS THAT THIS IS THE CHEAP OPTION FOR LARGE
#  VOLUMES OF WEAKLY CONTAMINATED AIR. Thermal oxidation destroys anything and
#  costs fuel to heat air that is almost entirely nitrogen. Biological
#  treatment runs at ambient temperature on almost no energy. The trade is
#  therefore concentration: below some threshold biology wins comfortably, and
#  above it the biology is overwhelmed and combustion wins.
#
#  THIRD, AND IT IS WHY THE FIELD EXISTS COMMERCIALLY: MOST OF THIS IS ODOUR
#  CONTROL. The driver is usually a complaint from a neighbour rather than a
#  measured health risk, which makes the acceptance criterion a human nose.
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
    "Treating contaminated air by passing it through a wet biofilm, where the "
    "limit is what will dissolve rather than what the organisms will degrade."
)

# -----------------------------------------------------------------------------
#  Structure: (a) how it works and why solubility governs, (b) the three
#  configurations and what distinguishes them, (c) the trade against thermal
#  oxidation, (d) what it is actually used for, which is odour.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the mechanism, and the constraint that follows from it
    "Biological air treatment removes contaminants from gas streams by passing "
    "them through a bed carrying a microbial biofilm. The organisms are not "
    "airborne. They live in a thin film of water on a packing material, and a "
    "contaminant becomes available to them only after it has partitioned out "
    "of the gas phase and dissolved into that film. The consequence governs "
    "the whole field: the binding constraint is solubility rather than "
    "biodegradability. Hydrogen sulphide, ammonia, alcohols, aldehydes and "
    "many organic acids partition readily and are treated efficiently. Poorly "
    "soluble compounds, including many chlorinated solvents and higher "
    "hydrocarbons, pass through a perfectly healthy bed largely untouched, "
    "because they never reach the phase in which the organisms are working. "
    "This is the same bioavailability argument made in `grey.bioremediation` "
    "about contaminant sorbed into soil, reaching this record through "
    "gas-liquid partitioning instead. "
    # (b) the three configurations
    "Three configurations exist and they differ in how the water is handled. A "
    "biofilter uses an organic packing such as compost, bark or peat, kept "
    "damp, with the biofilm growing on the packing itself; it is the simplest "
    "and cheapest arrangement and it has no separate liquid phase to control. "
    "A biotrickling filter uses an inert packing with liquid recirculated over "
    "it, which allows pH and nutrients to be controlled and acidic degradation "
    "products to be washed out, and is therefore what hydrogen sulphide "
    "treatment generally uses. A bioscrubber separates the two steps entirely, "
    "absorbing the contaminant into liquid in one vessel and degrading it in a "
    "separate bioreactor, which gives the most control and costs the most. "
    # (c) the trade that decides
    "The comparison is with thermal or catalytic oxidation, which destroys "
    "essentially any organic compound and requires heating a gas stream that "
    "is almost entirely nitrogen. Biological treatment runs at ambient "
    "temperature and consumes little more than the fan power to move the air. "
    "The trade is therefore concentration and flow: for large volumes of "
    "weakly contaminated air, biology is far cheaper; at higher "
    "concentrations the biofilm cannot keep pace, the bed acidifies or dries, "
    "and combustion becomes the correct answer. Residence times are seconds, "
    "which is what makes treating very large air volumes practical at all. "
    # (d) what it is actually for
    "In deployment, most of this is odour control at wastewater works, "
    "composting and digestion facilities, rendering plants and intensive "
    "livestock housing. That matters for how success is judged. The driver is "
    "usually a neighbour's complaint rather than a measured exposure, the "
    "target is a detection threshold rather than a concentration limit, and "
    "compliance is assessed by trained human panels smelling diluted samples. "
    "A plant can therefore meet every chemical specification and still fail, "
    "because the compounds that offend a nose do so at concentrations far "
    "below anything an instrument was asked to find."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Smelly or polluted air from a factory or sewage works can be cleaned by "
    "blowing it slowly through a damp bed of bark, compost or plastic packing "
    "covered in bacteria. The bacteria are not in the air; they are in a thin "
    "layer of water on the packing, so the pollutant first has to dissolve "
    "into that water before anything can eat it. That is the catch: things "
    "that dissolve easily, like the rotten-egg smell of hydrogen sulphide, are "
    "removed very well, and things that do not dissolve pass straight through "
    "no matter how healthy the bacteria are. The alternative is burning the "
    "air clean, which works on anything and costs fuel to heat a great deal of "
    "air that was mostly harmless. So biology wins when there is a lot of air "
    "and not much pollution in it, which is most of the time. Whether it has "
    "worked is usually judged by people smelling samples, because the "
    "complaint that started it came from a neighbour."
)

# -----------------------------------------------------------------------------
#  The tea analogy carries the phase-transfer point, which is the record's one
#  hard idea, and carries the failure mode with it: what does not dissolve is
#  not extracted no matter how long the contact.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is brewing rather than filtering. A filter catches what is too big to "
    "pass; a brew extracts only what the water will take up, and whatever is "
    "insoluble stays in the leaf however long it steeps. These beds work the "
    "second way. The air is not strained, it is washed, and a compound that "
    "will not dissolve is not washed out of it. Steeping longer, which is to "
    "say building a bigger bed, does not change that."
)

WHY_IT_MATTERS = (
    "Odour is the commonest cause of complaint against waste and food "
    "processing facilities, and it determines whether such a facility can be "
    "sited near where people live. That is not a trivial matter: a wastewater "
    "works, a composting site or a digester has to be near the population it "
    "serves, and effective odour control is frequently the condition on which "
    "planning permission rests. This record is therefore what allows a great "
    "deal of `grey.wastewater_treatment` and `grey.biowaste_treatment` to "
    "exist in the places they need to be. "
    "The energy argument is real as well. Treating large volumes of weakly "
    "contaminated air thermally means heating mostly nitrogen, and doing it "
    "biologically means running a fan. For the flows involved that difference "
    "is substantial, and it is one of the few places where the biological "
    "option is cheaper on energy by an order of magnitude rather than by a "
    "margin. Hydrogen sulphide removal has a specific value beyond odour, "
    "since it is toxic and corrosive and destroys the gas engines that "
    "digester biogas is meant to run. "
    "The limits are firm. Poorly soluble compounds are outside the technique "
    "rather than treated slowly by it. Beds are large, because seconds of "
    "residence time at high flow still means a substantial volume, and land "
    "near a plant is not free. Compost and bark packing compacts and channels "
    "over a few years and has to be replaced, which is a recurring cost that "
    "proposals tend to omit. The community is slow to recover from drying out "
    "or from an interruption in the air supply, so a plant that stops for "
    "maintenance may smell for weeks afterwards. Acidic products from sulphur "
    "and chlorine compounds accumulate and kill the biofilm unless they are "
    "washed out. And there is an honest limitation on the objective itself: "
    "odour is measured against a human detection threshold, which varies "
    "between people and is not a health-based standard, so a plant can be "
    "compliant and still be a genuine nuisance to the person living nearest."
)
