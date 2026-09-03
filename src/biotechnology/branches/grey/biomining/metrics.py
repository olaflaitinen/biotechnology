# =============================================================================
#  biotechnology.branches.grey.biomining.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  A RECOVERY PERCENTAGE IN THIS RECORD IS AMBIGUOUS UNLESS YOU KNOW WHICH
#  PROCESS PRODUCED IT.
#
#      BIOLEACHING   per cent of the metal dissolved into solution
#      BIOOXIDATION  per cent of the sulphide destroyed, which is a
#                    PRETREATMENT result, measured downstream as the
#                    improvement in gold recovery by a later cyanide step
#
#  The two numbers are not comparable and the trade literature prints them in
#  the same tables. They are therefore recorded here as separate metrics with
#  the distinction stated in each.
#
#  THE SECOND ORGANISING IDEA IS THAT THE RATE-LIMITING VARIABLES ARE NOT
#  BIOLOGICAL. Oxygen transport through a pile of rock, iron precipitation on
#  mineral surfaces and heap temperature govern the outcome. Cell count is
#  recorded and it is deliberately placed low, because raising it does not
#  raise the rate.
#
#  A THIRD POINT, AND IT IS THE MOST IMPORTANT NUMBER HERE. Acid generation
#  potential describes what the material will do FOR CENTURIES AFTER THE
#  OPERATION ENDS. It is measured before mining begins, it determines the
#  closure liability, and it is the one figure in this facet that outlives
#  everyone involved.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # =========================================================================
    #  THE TWO RECOVERY FIGURES, WHICH ARE NOT THE SAME FIGURE
    # =========================================================================
    Metric(
        name="Metal extraction in bioleaching",
        symbol="R_leach",
        unit="per cent of contained metal dissolved into solution",
        typical="lower than smelting and achieved over months to years rather "
        "than hours",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The bioleaching result: metal that has left the rock and entered "
            "the liquid, where a recovery circuit can take it. It is measured "
            "against the metal contained in the heap, so a heap with poor flow "
            "distribution reports a low figure even where the leached fraction "
            "leached completely."
        ),
    ),
    Metric(
        name="Sulphide oxidation extent in biooxidation",
        symbol="X_sulphide",
        unit="per cent of sulphide mineral oxidised",
        typical="taken far enough to liberate the enclosed gold, which is a "
        "downstream criterion rather than a target in itself",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The biooxidation result, and it is not a recovery. No gold is "
            "dissolved: the sulphide enclosing it is destroyed so that a later "
            "cyanide step can reach it. The process is judged by the entry "
            "below rather than by this number, and printing it in the same "
            "table as the one above is how the literature becomes "
            "unintelligible."
        ),
    ),
    Metric(
        name="Downstream gold recovery after pretreatment",
        symbol="R_Au",
        unit="per cent of gold recovered by cyanidation after biooxidation",
        typical="substantially higher than cyanidation of untreated refractory "
        "material",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The figure that actually justifies a biooxidation plant. It is the "
            "improvement in a subsequent process, which is why the pretreatment "
            "is specified by how much sulphide it must destroy rather than by "
            "any output of its own."
        ),
    ),
    # =========================================================================
    #  HOW FAST, AND WHAT ACTUALLY LIMITS IT
    # =========================================================================
    Metric(
        name="Leaching rate",
        symbol="r_leach",
        unit="per cent of contained metal extracted per month",
        formula="shrinking_core_model",
        typical="slow in heaps, an order of magnitude faster in stirred tanks",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The number that determines whether an operation can wait out a "
            "price cycle. Heap kinetics are governed by transport rather than "
            "by reaction: solution reaching a particle, oxygen reaching the "
            "solution, and the reaction front advancing into the particle, "
            "which is what the shrinking core description captures."
        ),
    ),
    Metric(
        name="Oxygen supply rate",
        symbol="q_O2",
        unit="moles of oxygen delivered per tonne of ore per day",
        typical="the binding constraint in most heaps",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Placed high because it is usually what limits the process. The "
            "organisms regenerate ferric iron from ferrous iron using oxygen, "
            "so the whole system runs no faster than air reaches it. That makes "
            "aeration design and heap permeability the real levers, and it is "
            "why forced aeration through the pad base is standard."
        ),
    ),
    Metric(
        name="Ferric to ferrous iron ratio",
        symbol="Fe3/Fe2",
        unit="dimensionless ratio in the leach solution",
        typical="held high, since ferric iron is the oxidant that dissolves "
        "the mineral",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The direct measure of whether the biology is doing its job. The "
            "bacteria convert ferrous to ferric; the ferric attacks the "
            "sulphide and is reduced back. A falling ratio means the biological "
            "regeneration is not keeping pace, which is nearly always an oxygen "
            "or temperature problem rather than a shortage of organisms."
        ),
    ),
    Metric(
        name="Heap temperature",
        symbol="T_heap",
        unit="degrees Celsius",
        typical="rises through the operation, since sulphide oxidation is "
        "exothermic",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A variable the heap sets for itself. The reaction generates heat, "
            "which accelerates it further, until the temperature exceeds what "
            "the mesophilic organisms that started it can tolerate and the "
            "community must shift to thermophiles or the rate collapses. "
            "Managing that succession is a real operating problem and it is "
            "invisible from outside the pile."
        ),
    ),
    Metric(
        name="Cell concentration in the leach solution",
        symbol="N_cell",
        unit="cells per millilitre",
        typical="high, and not the variable that limits the process",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Deliberately placed low in this facet. Because the organisms "
            "regenerate a reagent rather than performing the dissolution, "
            "raising their number does not raise the rate proportionally. It is "
            "worth measuring as evidence that the community is alive and "
            "adapted, and it is not a performance figure."
        ),
    ),
    # =========================================================================
    #  WHY A HEAP STOPS WORKING WHILE EVERYTHING LOOKS RIGHT
    # =========================================================================
    Metric(
        name="Surface passivation index",
        symbol="f_pass",
        unit="fraction of reactive mineral surface coated by precipitate",
        typical="rises with jarosite and elemental sulphur accumulation",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The commonest reason a heap underperforms with correct solution "
            "chemistry, adequate aeration and a healthy community. Iron "
            "precipitates and sulphur layers coat the very surfaces the "
            "chemistry needs to attack, so the reagent arrives and cannot "
            "reach the mineral. It is diagnosed mineralogically rather than "
            "from the solution."
        ),
    ),
    Metric(
        name="Solution flow distribution",
        symbol="f_wet",
        unit="fraction of heap volume contacted by irrigation solution",
        typical="well below unity where fines have blocked flow paths",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Channelling means solution and air pass through part of the heap "
            "and never reach the rest, so a large fraction of the contained "
            "metal is never presented to the chemistry at all. This is what "
            "agglomeration and particle size control exist to prevent, and it "
            "is the difference between a low recovery and a low reaction rate."
        ),
    ),
    # =========================================================================
    #  THE NUMBER THAT OUTLIVES THE OPERATION
    # =========================================================================
    Metric(
        name="Acid generation potential",
        symbol="NAG",
        unit="kilograms of sulphuric acid equivalent per tonne of material, net "
        "of neutralising capacity",
        typical="positive for sulphide-bearing material, which means the "
        "reaction is self-sustaining",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The most consequential figure in this facet and the only one that "
            "describes what happens after everybody has left. It is measured "
            "before mining begins, it determines whether residual material will "
            "generate acid indefinitely, and it sets the closure liability. A "
            "positive net value means the reaction that made the mine work "
            "continues for centuries whether or not anyone is operating it."
        ),
    ),
    Metric(
        name="Residual drainage quality after closure",
        symbol="q_close",
        unit="pH and dissolved metal concentration in seepage",
        typical="requires monitoring and frequently treatment for decades or "
        "longer",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The measured consequence of the entry above. It is recorded as a "
            "metric rather than as a governance note because it is monitored, "
            "reported and enforced against, and because a closure plan without "
            "a number here is not a closure plan."
        ),
    ),
    # =========================================================================
    #  AND WHETHER IT PAYS
    # =========================================================================
    Metric(
        name="Cut-off grade",
        symbol="g_cut",
        unit="per cent metal, or grams per tonne",
        typical="considerably lower than for smelting, which is the entire "
        "commercial argument",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The lowest grade worth processing, and the number that defines "
            "what this record is for. Lowering it converts waste rock into ore, "
            "which extends reserves without new ground being disturbed and "
            "simultaneously extends the reach of mining into material that "
            "would otherwise have been left alone. Both readings are correct."
        ),
    ),
    Metric(
        name="Acid consumption",
        symbol="C_acid",
        unit="kilograms of acid per tonne of ore",
        typical="high where the ore contains carbonate that neutralises what "
        "the process generates",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "A significant operating cost and a useful early screen. Carbonate "
            "in the ore consumes the acid the bacteria produce, so a "
            "carbonate-rich deposit can be technically leachable and "
            "economically hopeless. It is also, conversely, the property that "
            "makes such material safer at closure."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Particle-scale kinetics, transport, and the balances that govern closure.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "shrinking_core_model",
    "monod_equation",
    "arrhenius_equation",
    "mass_balance",
    "oxygen_transfer_rate",
    "acid_base_accounting",
)
