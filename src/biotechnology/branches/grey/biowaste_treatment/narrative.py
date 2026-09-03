# =============================================================================
#  biotechnology.branches.grey.biowaste_treatment.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS IS THE ONE RECORD IN THE BRANCH WHERE THE WASTE IS WORTH SOMETHING,
#  AND THAT CHANGES WHO PAYS.
#
#  Everywhere else in grey biotechnology, treatment is a cost imposed by
#  regulation on somebody who would rather not bear it. Here the material has
#  positive value: anaerobic digestion converts food and agricultural waste
#  into methane that can be burned or injected into the gas grid, and into a
#  digestate that returns nitrogen and phosphorus to soil. A disposal cost
#  becomes a revenue line.
#
#      WHICH MEANS THE ECONOMICS DEPEND ON WHAT THE MATERIAL WOULD OTHERWISE
#      HAVE COST TO DISPOSE OF, NOT ON WHAT THE GAS IS WORTH.
#
#  That is the honest statement of the business case, and it explains why the
#  same plant is viable in a country with a landfill tax and unviable next
#  door without one.
#
#  THE SECOND THING TO ESTABLISH IS THE COMPARISON WITH LANDFILL, WHICH IS NOT
#  A COMPARISON WITH DOING NOTHING. Organic waste in a landfill decomposes
#  anaerobically anyway and emits methane, a far more potent greenhouse gas
#  than carbon dioxide, from a structure that captures only part of it. The
#  climate case for digestion is therefore not that it produces energy. It is
#  that the methane is produced in a vessel with a pipe on it instead of under
#  a field.
#
#  THIRD, AND IT IS WHERE THESE PROJECTS ACTUALLY FAIL: CONTAMINATION. Plastic,
#  glass and metal in the feedstock wreck equipment and end up in the digestate
#  spread on farmland. The determining variable is how the waste was collected,
#  which is a matter of household behaviour and municipal policy rather than of
#  process engineering.
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
    "Anaerobic digestion and composting of organic waste into methane and soil "
    "amendment, where the economics turn on avoided disposal cost and the "
    "failures turn on feedstock contamination."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the two routes and what each is for, (b) the four-stage
#  microbiology and where it breaks, (c) the climate argument, which is about
#  landfill rather than about energy, (d) contamination, which is the real
#  operational problem.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the two routes
    "Biowaste treatment converts the organic fraction of municipal, food and "
    "agricultural waste into usable products by two routes that suit different "
    "material. Anaerobic digestion excludes oxygen and produces biogas, "
    "typically somewhat over half methane, together with a wet digestate; it "
    "suits wet, energy-dense material such as food waste, manure and slurry. "
    "Composting admits oxygen and produces a stable solid and heat but no "
    "recoverable fuel; it suits drier, more fibrous material such as garden "
    "waste, and it is far simpler to operate. The choice between them is "
    "decided by the moisture and the energy content of the feedstock rather "
    "than by preference, and many facilities do both, digesting the wet "
    "fraction and composting what the digester rejects. "
    # (b) the microbiology, and where it goes wrong
    "Digestion is performed by a community in four sequential steps, each "
    "feeding the next. Hydrolysis breaks polymers into soluble molecules and "
    "is the rate-limiting step for fibrous material. Acidogenesis converts "
    "those into organic acids. Acetogenesis converts the acids to acetate and "
    "hydrogen. Methanogenesis, performed by archaea rather than bacteria, "
    "produces methane. The important operational fact is that the last group "
    "grows far more slowly than the first, so overfeeding produces acid faster "
    "than the methanogens can consume it, the pH falls, and the organisms most "
    "needed to recover are the ones the falling pH inhibits most. That is the "
    "characteristic failure of a digester and it takes weeks to reverse. "
    # (c) the climate argument, stated correctly
    "The climate case is frequently stated wrongly as a case about renewable "
    "energy. The correct comparison is with landfill, where the same organic "
    "material decomposes anaerobically regardless and releases methane from a "
    "structure that captures only a fraction of it. Methane is a far more "
    "potent greenhouse gas than carbon dioxide over the timescales that "
    "matter. So the benefit is chiefly that the methane is generated inside a "
    "sealed vessel with a pipe on it, and the energy recovered is a "
    "consequence of that rather than the reason for it. This also means the "
    "benefit is largest where the alternative is landfill and much smaller "
    "where it is incineration with energy recovery. "
    # (d) what actually determines success
    "Operationally, the determining variable is feedstock contamination. "
    "Plastic film, glass and metal in collected food waste damage pumps and "
    "mixers, accumulate in the vessel, and pass into the digestate that is "
    "spread on farmland, which is how microplastic reaches agricultural soil "
    "through a route intended as recycling. Removing contamination after "
    "collection is expensive and imperfect; separating it at the household is "
    "cheap and effective. The performance of a digester is therefore set "
    "largely by municipal collection policy and household behaviour, which is "
    "an uncomfortable finding for a process discipline and is the single most "
    "reliable predictor of whether a plant meets its design output."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Food and farm waste can be sealed in a tank without air, where microbes "
    "break it down and give off a gas that is mostly methane, which is the "
    "same thing as natural gas and can be burned for electricity or put into "
    "the gas grid. What is left over is a wet fertiliser. Drier garden waste "
    "is better composted, which needs air and produces no fuel. The real "
    "reason this is good for the climate is not the energy. It is that the "
    "same waste in a landfill produces that methane anyway and most of it "
    "escapes into the sky, where it is a much stronger greenhouse gas than "
    "carbon dioxide. Doing it in a sealed tank means the methane goes down a "
    "pipe instead. The thing that makes these plants fail is not the biology "
    "at all: it is plastic bags and broken glass in the food waste, which wreck "
    "the machinery and end up spread on farm fields."
)

# -----------------------------------------------------------------------------
#  The stomach analogy is the standard one for digestion and is used here
#  because it carries the four-stage sequence, the overfeeding failure and the
#  slow recovery in a single familiar image.
# -----------------------------------------------------------------------------
ANALOGY = (
    "A digester is a stomach with a schedule. It handles a steady diet well "
    "and it handles a sudden large meal badly, because the first stages of "
    "digestion run much faster than the last, so the intermediates pile up, "
    "the contents turn acid, and the organisms that would clear the acid are "
    "the ones the acid disables. Recovery takes weeks of careful feeding. And "
    "as with any stomach, what it is given matters more than how it is run: "
    "nothing about the vessel can deal with the swallowed plastic."
)

WHY_IT_MATTERS = (
    "Organic waste is a large share of what municipalities collect, and in "
    "landfill it is the principal source of the methane the site emits. "
    "Diverting it to digestion addresses that at the source rather than "
    "capturing it afterwards, which is why landfill diversion targets and "
    "landfill taxes have driven the sector more effectively than any energy "
    "policy. The material recovered is real: methane displacing fossil gas, "
    "and a digestate returning nitrogen and phosphorus to soil at a time when "
    "phosphate rock is a finite imported resource. On farms the same process "
    "manages slurry that would otherwise be a nutrient runoff problem, which "
    "connects this record to `green.biofertilisers`. "
    "The limits are as concrete. The economics depend on avoided disposal "
    "cost, so the same plant is viable under a landfill tax and unviable "
    "without one, and the sector is consequently policy-dependent rather than "
    "self-supporting. Digestate is bulky and wet, so it can only be spread "
    "economically near the plant, and if there is not enough land within reach "
    "at the right time of year the plant has a disposal problem of its own. "
    "Spreading is seasonally restricted precisely when storage is fullest. "
    "Contamination in the feedstock damages equipment and carries plastic on "
    "to farmland. Methane leakage from the plant erodes the climate benefit "
    "quickly, since a small percentage loss offsets a large share of the gain, "
    "and it is measured far less often than it should be. Ammonia and odour "
    "emissions make siting genuinely contentious with neighbours. And the "
    "hierarchy point deserves stating plainly: preventing food waste is "
    "considerably better than digesting it, and a well-run digester should not "
    "be read as a reason to be relaxed about producing the material."
)
