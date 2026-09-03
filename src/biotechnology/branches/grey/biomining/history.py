# =============================================================================
#  biotechnology.branches.grey.biomining.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS FIELD WAS PRACTISED FOR CENTURIES BEFORE ANYONE KNEW IT WAS BIOLOGY,
#  AND THE ORGANISM WAS IDENTIFIED AS A POLLUTER BEFORE IT WAS RECOGNISED AS A
#  TOOL.
#
#  Copper was recovered from mine water in the Mediterranean and in central
#  Europe from antiquity onwards, by collecting the blue liquid running out of
#  workings and precipitating metal onto scrap iron. Nobody suspected an
#  organism. When Acidithiobacillus ferrooxidans was finally isolated in 1947,
#  it was isolated from acid mine drainage, as the cause of a pollution problem.
#  Only afterwards did anyone realise that the pollution and the ancient
#  recovery practice were the same reaction.
#
#      THE CULPRIT AND THE TOOL WERE THE SAME ORGANISM, FOUND IN THAT ORDER.
#
#  That sequence is the reason `narrative.py` insists on the identity between
#  biomining and acid mine drainage. It is not an editorial framing imposed on
#  the field; it is how the field actually discovered itself.
#
#  THE SETBACK RECORDED HERE IS THE 1990s ATTEMPT TO EXTEND THE TECHNIQUE
#  BEYOND COPPER AND GOLD. Several nickel and polymetallic ventures were
#  built on rate assumptions from laboratory columns that heaps did not
#  reproduce, and the gap was transport and passivation rather than
#  microbiology.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  DONE FOR CENTURIES WITHOUT KNOWING WHY IT WORKED
    # =========================================================================
    Milestone(
        1000,
        "Copper is recovered from mine drainage water by precipitation onto "
        "scrap iron",
        note=(
            "Practised at Rio Tinto and in central European workings, and "
            "recorded from antiquity onward. Blue copper-bearing water ran out "
            "of the workings, and metal was precipitated from it by contact "
            "with iron. The chemistry was entirely empirical and the "
            "microbiology was unsuspected for another nine hundred years."
        ),
    ),
    Milestone(
        1670,
        "Systematic heap leaching of copper ore is documented in Spain",
        note=(
            "Deliberate stacking and irrigation of ore to produce the copper "
            "solution, rather than merely collecting what drained naturally. It "
            "is the direct ancestor of modern heap leaching, and it was "
            "operated as a chemical practice for three centuries before anyone "
            "understood that living organisms were driving it."
        ),
    ),
    # =========================================================================
    #  THE ORGANISM IS FOUND, AS A POLLUTER
    # =========================================================================
    Milestone(
        1947,
        "Acidithiobacillus ferrooxidans is isolated from acid mine drainage",
        note=(
            "The bacterium was isolated while investigating the acidic "
            "metal-laden water draining from coal and metal mines, which is to "
            "say it was identified as the cause of a pollution problem. Only "
            "subsequently was it recognised that the same organism was "
            "responsible for the copper recovery practised for centuries. The "
            "culprit and the tool were the same, and they were found in that "
            "order."
        ),
    ),
    Milestone(
        1958,
        "A patent is granted for the deliberate use of bacteria in copper "
        "leaching",
        note=(
            "The point at which an ancient practice became an engineered "
            "process with a specified organism. It established that the "
            "leaching could be managed rather than merely permitted to happen, "
            "which is the distinction the whole record rests on."
        ),
    ),
    # =========================================================================
    #  BECOMING A REAL INDUSTRY
    # =========================================================================
    Milestone(
        1980,
        "Commercial heap bioleaching of low-grade copper is established at "
        "large scale",
        note=(
            "Lined and drained pads with managed irrigation, solution "
            "collection and solvent extraction circuits. It made material below "
            "smelting grade into ore, and it is the application that carries "
            "the field commercially to this day."
        ),
    ),
    Milestone(
        1986,
        "The first commercial biooxidation plant for refractory gold begins "
        "operation",
        note=(
            "Stirred tank oxidation of a sulphide concentrate so that cyanide "
            "could reach the enclosed gold. It is the most industrially "
            "controlled part of this record, and it is worth noting that its "
            "product is not metal but access: the bacteria dissolve nothing of "
            "value and remove what was in the way."
        ),
    ),
    Milestone(
        1990,
        "Solvent extraction and electrowinning are integrated with heap "
        "leaching to produce cathode copper on site",
        note=(
            "Closing the circuit from rock to finished metal without a smelter "
            "removed the sulphur dioxide emission that made historic copper "
            "production notorious. It is the strongest environmental argument "
            "the record has, and it sits beside the containment liability "
            "recorded below rather than cancelling it."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: LABORATORY RATES THAT HEAPS DID NOT REPRODUCE
    # =========================================================================
    Milestone(
        1998,
        "Several nickel and polymetallic bioleaching ventures underperform "
        "against projections based on laboratory columns",
        note=(
            "Projects were financed on extraction rates measured in "
            "well-mixed, well-aerated, temperature-controlled columns. Full "
            "heaps channelled, passivated and ran hot, and the shortfall was "
            "transport and mineral surface chemistry rather than microbiology. "
            "It is the same laboratory-to-field gap `grey.bioremediation` "
            "records, arriving here as a financing problem, and it slowed "
            "investment in metals beyond copper and gold for a decade."
        ),
    ),
    # =========================================================================
    #  FINDING OUT WHAT IS ACTUALLY IN A HEAP
    # =========================================================================
    Milestone(
        2000,
        "Thermophilic and archaeal consortia are applied to raise leaching "
        "rates",
        note=(
            "Sulphide oxidation is exothermic, so a heap heats itself beyond "
            "the tolerance of the mesophiles that started it. Using organisms "
            "adapted to those temperatures turned a failure mode into an "
            "operating regime, and it raised rates substantially for "
            "chalcopyrite, which had resisted leaching."
        ),
    ),
    Milestone(
        2005,
        "Molecular community analysis shows that heap populations differ from "
        "what was inoculated and from what was assumed",
        note=(
            "Sequence-based surveys of operating heaps found Leptospirillum "
            "species dominant where Acidithiobacillus had been assumed, and "
            "found the community shifting with temperature and depth. As in "
            "`grey.wastewater_treatment`, an industrial process had been run "
            "successfully for decades on an incorrect picture of who was doing "
            "the work."
        ),
    ),
    # =========================================================================
    #  THE LIABILITY THAT OUTLASTS THE COMPANY
    # =========================================================================
    Milestone(
        2010,
        "Acid rock drainage closure liability is formally recognised as "
        "multi-century in mine permitting",
        note=(
            "Regulators began requiring closure plans and financial assurance "
            "sized to a reaction that continues long after any company exists "
            "to manage it. It is the governance consequence of the identity in "
            "`narrative.py`, and it changed mine economics more than any "
            "process development in this timeline."
        ),
    ),
    Milestone(
        2015,
        "Bioleaching of electronic waste and spent catalysts is demonstrated at "
        "pilot scale",
        note=(
            "Applying the chemistry to material that is already waste rather "
            "than to ore. It works, and it remains a small fraction of what is "
            "recycled because mechanical and pyrometallurgical routes are much "
            "faster. It is recorded honestly as a demonstrated capability at "
            "pilot scale rather than as an established application."
        ),
    ),
    Milestone(
        2020,
        "Demand for copper, nickel and cobalt from electrification renews "
        "investment in low-grade bioleaching",
        note=(
            "Falling ore grades and rising demand for exactly the metals this "
            "technique handles have made low-grade processing economic again. "
            "The unresolved question is the one `narrative.py` states plainly: "
            "whether making poor material workable displaces new extraction or "
            "extends mining into ground that would otherwise have been left "
            "alone."
        ),
    ),
)
