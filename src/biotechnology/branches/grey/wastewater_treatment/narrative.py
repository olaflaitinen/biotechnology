# =============================================================================
#  biotechnology.branches.grey.wastewater_treatment.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS IS THE LARGEST DELIBERATE USE OF MICROORGANISMS ON EARTH AND ALMOST
#  NOBODY THINKS OF IT AS BIOTECHNOLOGY.
#
#  Every sewage works in every city is a continuously operated microbial
#  process. The volumes exceed all the fermentation in `white` and all the food
#  processing in `yellow` combined by a very wide margin, they have run without
#  interruption for a century, and the organisms doing the work were never
#  isolated, characterised, purchased or inoculated. They arrived in the
#  sewage.
#
#      THE ENGINEERING IS NOT IN THE ORGANISMS. IT IS IN THE SELECTION.
#
#  This is the record's central idea and it is the inverse of `white`
#  biotechnology. There, a defined strain is protected inside a sterile vessel.
#  Here, an open, undefined, continuously reseeded community is shaped by
#  operating conditions: how long the water stays, how long the biomass stays,
#  how much oxygen is supplied, and in what sequence the tanks are arranged.
#  Change the residence times and a different community grows. The operator
#  chooses the conditions and the conditions choose the organisms.
#
#  A SECOND THING WORTH ESTABLISHING. The public health achievement here is
#  larger than that of any single medicine in this library and predates
#  antibiotics. It is recorded plainly rather than modestly.
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
    "Continuous treatment of sewage and effluent by managed microbial "
    "communities, in which the engineering selects the organisms rather than "
    "supplying them."
)

# -----------------------------------------------------------------------------
#  Structure: (a) scale and the selection principle, (b) the three jobs and
#  why nitrogen and phosphorus are separate problems, (c) the sludge, which is
#  half the cost, (d) what the process cannot remove.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) scale, and the idea that governs everything
    "Biological wastewater treatment is the largest deliberate application of "
    "microorganisms anywhere, operating continuously in every city that has "
    "sewerage. Its defining feature is that the organisms are neither supplied "
    "nor defined. They arrive in the influent, and the plant is engineered to "
    "select for the ones that do the required work. Solids retention time "
    "determines which organisms can grow fast enough to remain in the system, "
    "hydraulic retention time sets the contact available, aeration decides "
    "what respires and what does not, and the sequence of aerobic, anoxic and "
    "anaerobic zones determines which metabolisms are favoured in turn. An "
    "operator changes an outcome by changing a condition, which is the exact "
    "inverse of the sterile defined-strain approach recorded in "
    "`white.microbial_fermentation`. "
    # (b) the three jobs, which are not one job
    "Three separate jobs are done and they compete for the same reactor. "
    "Organic carbon removal is fast, robust and largely solved: heterotrophic "
    "organisms oxidise dissolved organic matter within hours, and this is what "
    "the original activated sludge process was built for. Nitrogen removal is "
    "harder because it takes two contradictory steps. Nitrification, which "
    "oxidises ammonium to nitrate, is performed by slow-growing autotrophs "
    "that need oxygen and a long solids retention time and that are the first "
    "thing lost when a plant is overloaded or cold. Denitrification, which "
    "converts nitrate to nitrogen gas, requires the absence of oxygen and a "
    "supply of organic carbon, so the plant must provide anoxic and aerobic "
    "conditions in sequence, and the carbon that would have been removed in "
    "step one is needed in step two. Phosphorus removal is different again, "
    "since phosphorus is neither degraded nor volatilised: it can only be "
    "moved into biomass or precipitated, and the biological route depends on "
    "alternating anaerobic and aerobic exposure to select organisms that store "
    "it in excess. "
    # (c) the sludge, which is the honest half of the subject
    "Every one of those processes produces sludge, and sludge handling is "
    "commonly around half the cost of running a treatment works. This is the "
    "part of the subject that public accounts omit. Removing pollutants from "
    "water converts them into a wet solid containing the organisms, the "
    "phosphorus, the metals and whatever else was in the sewage. It is "
    "thickened, frequently digested anaerobically to reduce its mass and "
    "produce methane, dewatered, and then applied to land, incinerated or "
    "landfilled. The treatment plant does not make the material disappear; it "
    "concentrates it into a form that can be dealt with. "
    # (d) what gets through
    "What the process does not remove matters increasingly. Pharmaceuticals, "
    "hormones, per- and polyfluoroalkyl substances and microplastics pass "
    "through a plant designed decades ago for carbon and nutrients, and "
    "removing them requires additional physical or chemical stages rather than "
    "better biology. Antibiotic resistance genes are concentrated rather than "
    "destroyed in the dense mixed community of a reactor, which is a concern "
    "shared with `dark.antimicrobial_resistance`. And the whole system is "
    "energy-intensive, since aeration alone accounts for a substantial share "
    "of many municipalities' electricity use."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "A sewage works is a farm for bacteria. The sewage arrives already full of "
    "microbes, and the plant is built to give the useful ones the conditions "
    "they need and to wash the rest out. Nobody buys the bacteria or puts them "
    "in; the design decides which ones thrive. They eat the organic matter "
    "within hours. Getting rid of nitrogen takes two opposite steps, one "
    "needing air and one needing none, so the water is moved between tanks. "
    "Phosphorus cannot be destroyed at all and is instead stored inside the "
    "bacteria and taken away with them. That is the catch nobody mentions: "
    "everything removed from the water ends up in a wet sludge, and dealing "
    "with the sludge costs about as much as treating the water. This process "
    "protects the drinking water of most of the world, it is over a century "
    "old, and it is probably the largest use of biology anywhere."
)

# -----------------------------------------------------------------------------
#  The pasture analogy. Chosen because selection by conditions rather than by
#  planting is precisely what the record turns on, and because the manure in
#  the image carries the sludge point without strain.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is grazing management rather than sowing a crop. Nobody plants the "
    "pasture; what grows is decided by how often it is cut, how wet it is kept "
    "and how long the animals stay. Change the schedule and different plants "
    "take over. A treatment works is run the same way, by adjusting residence "
    "times and aeration until the community that thrives is the one doing the "
    "job. And as on any farm, the material that comes out at the other end is "
    "half the work."
)

WHY_IT_MATTERS = (
    "This is among the largest public health interventions ever deployed. "
    "Separating sewage from drinking water is what ended cholera and typhoid "
    "as ordinary urban facts, and biological treatment is what makes that "
    "possible at city scale without simply moving the problem downstream. It "
    "predates antibiotics, it has run continuously for a century, and it "
    "protects more people daily than any medicine in this library. "
    "It also protects surface waters directly. Untreated sewage strips oxygen "
    "from a river and kills it; nutrient discharge causes the algal blooms and "
    "dead zones recorded in `blue.algal_biotechnology`. Anaerobic digestion of "
    "the resulting sludge recovers methane, which turns part of the energy "
    "cost back. "
    "The limits are substantial and are becoming more visible. Aeration is "
    "energy-intensive enough to be a significant share of municipal "
    "electricity consumption. Sludge disposal is roughly half the operating "
    "cost and has no comfortable answer: land application returns nutrients "
    "and also returns metals and persistent chemicals, incineration costs "
    "energy, and landfill defers the question. Pharmaceuticals, hormones and "
    "fluorinated compounds pass through a process not designed to catch them. "
    "Combined sewer overflows discharge untreated sewage during heavy rain by "
    "design, which is a structural feature of old networks rather than a "
    "failure of the biology. Nutrient removal costs considerably more than "
    "carbon removal and is therefore the first thing not built where budgets "
    "are short. And the deepest inequity in this record is one of coverage: a "
    "large share of the world's population is not connected to any treatment "
    "at all, so the technology is mature, proven, and absent exactly where the "
    "disease burden is highest."
)
