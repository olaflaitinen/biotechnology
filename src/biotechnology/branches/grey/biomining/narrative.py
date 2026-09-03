# =============================================================================
#  biotechnology.branches.grey.biomining.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS RECORD AND ITS WORST ENVIRONMENTAL PROBLEM ARE THE SAME CHEMISTRY.
#
#  Acid mine drainage is among the most persistent industrial pollution
#  problems in existence: sulphide minerals exposed to air and water are
#  oxidised by bacteria, generating sulphuric acid that dissolves metals and
#  runs off, and it continues for centuries after a mine closes. Biomining is
#  that identical reaction, performed on purpose, inside a lined heap, with the
#  liquid collected.
#
#      THE TECHNOLOGY IS THE POLLUTION, CONTAINED AND POINTED SOMEWHERE.
#
#  Nothing else in this library has that relationship to its own worst
#  externality, and a record that presented biomining as a clean alternative
#  without stating it would be dishonest.
#
#  THE SECOND THING TO ESTABLISH IS WHAT THE ORGANISMS ACTUALLY DO, BECAUSE IT
#  IS ROUTINELY MISDESCRIBED. They do not eat metal and they do not accumulate
#  it. They oxidise iron and sulphur for energy, and the ferric iron and acid
#  that result dissolve the mineral chemically. The bacteria regenerate the
#  reagent; the leaching is chemistry. That is why the process is slow and why
#  it cannot be sped up by adding more organisms.
#
#  THIRD: THE TRADE IS GRADE AGAINST TIME. Smelting is fast and needs ore rich
#  enough to justify the furnace, and it emits sulphur dioxide. Bioleaching is
#  slow, measured in months to years, and works on ore too poor to smelt and on
#  waste rock already dug up. Copper and gold are where it pays; most other
#  metals it does not.
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
    "Recovering metals from low-grade ore using iron and sulphur oxidising "
    "bacteria, which is acid mine drainage performed deliberately inside a "
    "lined containment."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what the organisms actually do, (b) the two distinct process
#  types, which are frequently conflated, (c) the trade against smelting,
#  (d) the identity with acid mine drainage, stated plainly.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the mechanism, corrected
    "Biomining uses microorganisms to recover metals from ore that is too poor "
    "in grade to process conventionally. The mechanism is commonly "
    "misdescribed. The organisms do not consume metal and do not accumulate "
    "it. They are chemolithotrophs that obtain energy by oxidising ferrous "
    "iron and reduced sulphur compounds, and the products of that metabolism, "
    "ferric iron and sulphuric acid, are strong chemical oxidants that "
    "dissolve sulphide minerals. The dissolution is therefore chemistry, and "
    "the organisms' role is to regenerate the oxidant continuously from air "
    "and water. This is why the process is inherently slow, why raising the "
    "cell count does not accelerate it proportionally, and why the "
    "rate-limiting factors are oxygen supply, temperature and access to "
    "mineral surface rather than anything to do with biology. "
    # (b) two processes that are not the same process
    "Two distinct operations share the name and should not be conflated. In "
    "bioleaching the target metal itself is dissolved and recovered from the "
    "resulting solution, which is how a substantial share of world copper is "
    "produced, along with nickel, cobalt, zinc and uranium. In biooxidation "
    "the target is not dissolved at all: gold particles locked inside a "
    "sulphide matrix are inaccessible to cyanide extraction, and the bacteria "
    "destroy the surrounding sulphide so the gold can be reached. The gold "
    "stays in the solid and the process is a pretreatment. Confusing the two "
    "makes the recovery figures in the literature unintelligible, since one "
    "measures metal in solution and the other measures the improvement in a "
    "later step. "
    # (c) the trade against smelting
    "The comparison is with smelting, and the trade is grade against time. A "
    "smelter is fast and requires ore rich enough to justify the furnace, and "
    "it produces sulphur dioxide that must be captured. Heap bioleaching runs "
    "for months to years at ambient conditions on material that would "
    "otherwise be waste, including rock already excavated and stockpiled. Its "
    "capital cost is a fraction of a smelter's. In exchange the recovery is "
    "lower and slower, and the economics work for copper and gold and for "
    "very few other metals, because most sulphide minerals of interest do not "
    "leach readily enough to repay the wait. "
    # (d) the thing that must not be omitted
    "The chemistry of this process is identical to acid mine drainage. The "
    "same organisms, oxidising the same minerals, produce the same acid and "
    "dissolve the same metals when sulphide-bearing rock is exposed to air and "
    "water in a waste dump or an abandoned working. That reaction, once "
    "started, is self-sustaining and continues for centuries. Biomining is "
    "that reaction conducted deliberately on a lined pad with the liquid "
    "collected and processed. The engineering that separates a mine from a "
    "pollution source is containment and solution management, and where the "
    "containment fails there is no distinction between the two at all."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Certain bacteria live by rusting iron and sulphur, and in doing so they "
    "produce acid and a strong oxidising chemical. That mixture dissolves "
    "metals out of rock. Mining companies use this on purpose: they heap up "
    "rock too poor in copper to be worth smelting, keep it damp and airy, and "
    "collect the liquid that trickles out with the copper dissolved in it. For "
    "gold it works differently, because the bacteria eat away the mineral that "
    "traps the gold rather than the gold itself. It is slow, taking months or "
    "years, and it works on rock nothing else could use. The uncomfortable "
    "part is that this is exactly what causes acid mine drainage, the orange "
    "acidic water running out of old mines that poisons streams for centuries. "
    "It is the same bacteria and the same reaction. The difference is a "
    "lining underneath and a pipe to collect what comes out."
)

# -----------------------------------------------------------------------------
#  The analogy is chosen to carry the regenerated-reagent idea, which is the
#  record's corrected mechanism, and to carry the slowness with it.
# -----------------------------------------------------------------------------
ANALOGY = (
    "The bacteria are not the miners. They are a chemical works that runs on "
    "air and water and never stops, making the acid that does the mining. That "
    "is why hiring more of them does not speed the job: the works can only "
    "supply reagent as fast as air reaches it, and the rock only dissolves as "
    "fast as the reagent reaches its surfaces. And the same works, built by "
    "nobody on a heap of spoil behind an abandoned mine, has been running "
    "there for a hundred years."
)

WHY_IT_MATTERS = (
    "Ore grades have fallen steadily for a century. The rich deposits were "
    "mined first, and what remains is progressively poorer, which means "
    "conventional processing consumes more energy per unit of metal every "
    "decade. Bioleaching works on material below the grade a smelter can "
    "justify, including waste rock and tailings already excavated, so it "
    "extends reserves without new ground being disturbed. It runs at ambient "
    "temperature, its capital cost is a fraction of a smelter's, and it emits "
    "no sulphur dioxide, which is the pollutant that made historic smelting "
    "notorious. Biooxidation makes refractory gold deposits workable that "
    "would otherwise require roasting or pressure oxidation, both of which are "
    "energy-intensive and, in the case of roasting, release arsenic. Demand "
    "for copper, nickel and cobalt is rising with electrification, and these "
    "are among the metals the technique handles. "
    "The limits and the harms are equally real and deserve equal weight. The "
    "process is the acid mine drainage reaction, so a heap that leaks, a liner "
    "that fails or a closure that is not managed produces exactly the "
    "pollution the technique is otherwise credited with avoiding, and it "
    "produces it for centuries. Recovery is lower than smelting and the "
    "timescales are long enough to expose an operation to a price cycle it "
    "cannot wait out. The economics are confined to a few metals. Heap "
    "leaching consumes large volumes of water, frequently in arid regions "
    "where it competes with other users, and it needs a large land footprint. "
    "Residual heaps must be neutralised and monitored after closure, and the "
    "liability outlasts the company more often than not. And the deeper point "
    "is one the record should not soften: this technique makes it economic to "
    "mine material that was previously left alone, which is a genuine benefit "
    "where it displaces new extraction and a genuine harm where it simply "
    "extends the reach of mining into ground that would otherwise have stayed "
    "undisturbed."
)
