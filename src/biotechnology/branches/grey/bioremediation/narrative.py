# =============================================================================
#  biotechnology.branches.grey.bioremediation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The single most useful thing this record can establish is what
#  bioremediation CANNOT do, because the misconception is widespread and
#  consequential.
#
#      ORGANISMS DESTROY ORGANIC CONTAMINANTS. THEY DO NOT DESTROY METALS.
#
#  A hydrocarbon can be mineralised to carbon dioxide and water and genuinely
#  ceases to exist as a contaminant. Lead, cadmium and arsenic are elements.
#  Nothing in biology or chemistry destroys them. What biological treatment can
#  do is move them, concentrate them or change their oxidation state so they
#  become less mobile, and every one of those outcomes leaves the metal
#  somewhere. A record that presented both under one heading would mislead
#  about the most important decision a remediation engineer makes.
#
#  THE SECOND THING TO ESTABLISH IS THAT BIOAVAILABILITY, NOT BIODEGRADABILITY,
#  IS USUALLY THE LIMIT. Most contaminants that persist in soil after decades
#  are degradable in a flask. They persist because they have sorbed to organic
#  matter and diffused into pores the organisms cannot reach. The organisms are
#  willing and the contaminant is not available, which is a mass transfer
#  problem wearing a microbiology label.
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
    "Using microorganisms to degrade contaminants in soil and groundwater, "
    "limited by bioavailability rather than by biodegradability."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what it is and the organic-metal division, (b) the strategies,
#  (c) why the limit is mass transfer, (d) the trade against excavation, which
#  is what actually decides.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the division that governs everything
    "Bioremediation uses microbial metabolism to remove contamination from "
    "soil and groundwater. Its scope is set by a distinction that decides "
    "every project. Organic contaminants, including petroleum hydrocarbons, "
    "solvents, and to varying degrees the chlorinated compounds and polycyclic "
    "aromatics, can be mineralised: an organism uses them as a carbon or "
    "energy source and converts them to carbon dioxide, water and biomass, so "
    "the contaminant genuinely ceases to exist. Metals cannot. They are "
    "elements, no biological or chemical process destroys them, and biological "
    "treatment can only change where they are or what form they are in. That "
    "is a real capability and it is not destruction, and conflating the two is "
    "the field's most consequential misunderstanding. "
    # (b) the strategies
    "Four strategies are used and they differ mainly in how much is added. "
    "Monitored natural attenuation adds nothing and documents that indigenous "
    "organisms are degrading the contamination faster than it spreads, which "
    "is an approved intervention rather than an absence of one. Biostimulation "
    "supplies what the resident organisms lack, usually oxygen or an electron "
    "acceptor, sometimes nitrogen and phosphorus, on the reasoning that the "
    "capability is present and the conditions are not. Bioaugmentation "
    "introduces organisms, which usually does not work and is treated at length "
    "in `grey.bioaugmentation`. And engineered systems, including bioreactors "
    "and permeable reactive barriers, move the problem into a controlled "
    "environment. "
    # (c) the actual limit
    "The binding constraint is rarely whether an organism can degrade the "
    "compound. Most contaminants that have persisted in soil for decades are "
    "degradable in a laboratory flask. They persist because they have "
    "partitioned into soil organic matter and diffused into intraparticle "
    "pores, where an organism cannot reach them and from which they release "
    "slowly over years. Bioavailability rather than biodegradability sets the "
    "rate, which is why a treatment can proceed rapidly for months and then "
    "asymptote well above the target concentration. "
    # (d) the trade that decides
    "What decides a project is the comparison with excavation. Digging the "
    "material out and disposing of it elsewhere always works, works quickly, "
    "and costs a great deal, and it relocates the contamination rather than "
    "removing it. Bioremediation costs a fraction as much and takes months to "
    "years. So the choice turns on whether the site is needed by a date, "
    "whether anyone is currently exposed, and whether the contaminant is the "
    "sort of thing an organism will consume, which are three questions that "
    "have little to do with microbiology."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Some bacteria will eat spilled fuel, solvents and similar pollution, "
    "breaking it down into ordinary carbon dioxide and water. If you give them "
    "what they are short of, usually oxygen, they will do this in contaminated "
    "ground for a fraction of what it costs to dig the soil out and take it "
    "away. There are two catches worth knowing. Metals like lead and arsenic "
    "cannot be destroyed by anything at all, so biological methods can only "
    "move them somewhere else or lock them in place. And pollution that has "
    "been in the ground for years is often stuck inside soil particles where "
    "the bacteria simply cannot get at it, which is why cleanup slows down and "
    "stops short of the target."
)

# -----------------------------------------------------------------------------
#  The stain analogy. Chosen because it carries bioavailability, which is the
#  record's hard idea, and because its limit distinguishes destruction from
#  relocation, which is the record's other hard idea.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is soaking a stain out rather than cutting the fabric away. Soaking is "
    "cheap and slow and works on the sort of stain that dissolves, and it "
    "reaches the surface long before it reaches what has soaked into the "
    "fibres, which is why the last of a stain is so much harder than the "
    "first. Cutting the piece out is quick, certain and expensive, and it "
    "leaves you holding the stained piece: exactly what excavation does with "
    "contaminated soil, and exactly what biology cannot do with a metal."
)

WHY_IT_MATTERS = (
    "Contaminated land is a very large inherited problem. Former industrial "
    "sites, fuel depots, dry cleaners and gasworks exist in and around most "
    "cities, and the cost of dealing with them determines whether they are "
    "cleaned, built on, or fenced off for a generation. Bioremediation is "
    "frequently the difference, because at a fraction of the cost of "
    "excavation a site becomes economic to treat. It also removes the "
    "contaminant rather than relocating it, which excavation does not: soil "
    "taken to landfill is contaminated soil in a different place. Petroleum "
    "hydrocarbon contamination, which is the commonest kind by a wide margin, "
    "is genuinely well suited to the approach. The limits deserve equal "
    "prominence. Metals cannot be destroyed, so any metal work produces "
    "concentrated contamination that still requires disposal. Treatment stalls "
    "when the remaining contaminant is inaccessible rather than resistant, and "
    "the last fraction of a cleanup is disproportionately hard. Chlorinated "
    "solvents can degrade into intermediates more toxic than the parent "
    "compound, so an incomplete treatment can leave a site worse. Timescales "
    "of years sit badly with regulatory deadlines and with property "
    "transactions, which is why physical methods are chosen on sites where "
    "biology would have worked. And contaminated land is not evenly "
    "distributed: it sits disproportionately in poorer neighbourhoods, so a "
    "decision to fence rather than treat falls on people who did not create "
    "the contamination and cannot move away from it."
)
