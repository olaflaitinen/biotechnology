# =============================================================================
#  biotechnology.branches.yellow.food_fermentation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS pH, AND IN THIS RECORD IT IS NOT A PROCESS PARAMETER. IT
#  IS THE SAFETY BARRIER.
#
#  In most of this library a pH figure describes conditions. Here, the acid the
#  organisms produce is the thing that keeps pathogens out of the food, so a
#  fermentation that acidifies too slowly has not made a poor product, it has
#  made an unsafe one. That is why acidification rate appears immediately after
#  it, and why both are placed above anything about flavour or yield.
#
#  A NOTE ON WATER ACTIVITY. It appears here because in cured and dried
#  fermented products the barrier is not pH alone but the combination of pH,
#  water activity, salt and nitrite, and no single one of them is sufficient.
#  The hurdle concept is the correct frame and is stated in the note rather
#  than left implicit.
#
#  A NOTE ON WHAT IS DELIBERATELY UNQUANTIFIED. Flavour is the reason most of
#  these foods exist and it has no metric here beyond a volatile count, because
#  the honest position is that sensory quality is assessed by trained panels
#  rather than measured. Inventing a number for it would be worse than saying
#  so.
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
    #  THE SAFETY BARRIER
    # =========================================================================
    Metric(
        name="Final pH",
        symbol="pH_f",
        unit="dimensionless",
        typical="4.0 - 4.6 for most lactic fermentations; below 4.6 is the "
        "conventional threshold for controlling Clostridium botulinum",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Not a process parameter in this record but the safety barrier "
            "itself. The 4.6 threshold is a regulatory and microbiological "
            "landmark rather than a preference, since below it the organism "
            "responsible for botulism cannot grow. A product that fails to "
            "reach its target pH has not merely failed on quality."
        ),
    ),
    Metric(
        name="Acidification rate",
        symbol="dpH/dt",
        unit="pH units per hour",
        typical="varies by product; a stall is a food safety event rather than "
        "a delay",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How fast the barrier goes up, which matters as much as where it "
            "ends. A slow fermentation gives pathogens time to grow before the "
            "acid excludes them, so in fermented meat and dairy the rate is "
            "monitored as a critical control point and a stalled batch is "
            "usually destroyed rather than allowed to finish."
        ),
    ),
    Metric(
        name="Water activity",
        symbol="a_w",
        unit="dimensionless, 0 to 1",
        typical="below 0.91 inhibits most pathogenic bacteria; dried fermented "
        "sausage reaches 0.85 - 0.90",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The second barrier, and the reason cured products are safe at a pH "
            "that would not protect a moist food. The correct frame is hurdle "
            "technology: pH, water activity, salt, nitrite and competitive "
            "flora each contribute, none is sufficient alone, and a formulation "
            "change that weakens one must strengthen another."
        ),
    ),
    Metric(
        name="Salt concentration",
        symbol="c_NaCl",
        unit="per cent in the aqueous phase",
        typical="2 - 3 % for vegetable brines, higher in fish sauce and some "
        "cured products",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Selects for the organisms wanted by excluding those that cannot "
            "tolerate it, which is how a spontaneous vegetable fermentation "
            "becomes reliably lactic without a starter. Reducing salt for "
            "dietary reasons therefore weakens a safety barrier as well as "
            "changing flavour, which is a genuine tension in reformulation."
        ),
    ),
    # =========================================================================
    #  WHETHER THE CULTURE IS ALIVE AND WORKING
    # =========================================================================
    Metric(
        name="Viable starter count",
        symbol="N_v",
        unit="colony forming units per gram or millilitre",
        typical="10^6 - 10^9 CFU/g depending on product and stage",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A viable count is not an outcome, in exactly the sense "
            "`green.biofertilisers` insists on for its own products. What "
            "matters is whether the organisms acidify, and a high count with "
            "poor acidification usually means phage, inhibitor or a strain "
            "problem rather than a dosing one."
        ),
    ),
    Metric(
        name="Phage titre in whey or brine",
        symbol="T_phage",
        unit="plaque forming units per millilitre",
        typical="monitored continuously in dairy plants; rises sharply during "
        "an outbreak",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The dairy industry's early warning. Phage populations build in a "
            "plant over successive fermentations using the same strain, which "
            "is why rotation schedules exist, and a rising titre predicts a "
            "failed batch before the acidification curve does."
        ),
    ),
    # =========================================================================
    #  WHAT THE FERMENTATION CHANGED IN THE FOOD
    # =========================================================================
    Metric(
        name="Degree of proteolysis",
        symbol="f_prot",
        unit="per cent of total nitrogen that is soluble",
        typical="rises through cheese ripening over weeks to years",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The measurable core of ripening. Breaking proteins into peptides "
            "and amino acids produces both texture and the precursors of "
            "flavour, and it is the reason a ripened cheese is a different food "
            "from the curd it started as rather than an older one."
        ),
    ),
    Metric(
        name="Phytate reduction",
        symbol="dPhy",
        unit="per cent of phytate degraded",
        typical="substantial in cereal and legume fermentations",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The nutritional metric that connects this record to "
            "`yellow.biofortification`. Phytate binds iron and zinc and makes "
            "them unavailable, so degrading it improves absorption from foods "
            "that already contain the minerals. It is an accessible "
            "intervention requiring no new crop and no supplement."
        ),
    ),
    Metric(
        name="Cyanogenic compound reduction",
        symbol="dCN",
        unit="per cent reduction in cyanogenic glycosides",
        typical="large reductions achieved in traditional cassava processing",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The clearest case in the library of fermentation as detoxification "
            "rather than preservation. Cassava is a staple for hundreds of "
            "millions of people and is dangerous unprocessed, and the "
            "traditional fermentation sequences that make it safe were worked "
            "out empirically long before the chemistry was known."
        ),
    ),
    Metric(
        name="Volatile compound count",
        symbol="n_volatile",
        unit="distinct compounds detected",
        typical="hundreds in a ripened cheese, wine or soy sauce",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Included as the only quantitative handle on flavour, and it is a "
            "weak one: the number of compounds says nothing about which matter, "
            "and a handful at low concentration usually dominate perception. "
            "Sensory quality in this record is assessed by trained panel, and "
            "inventing a metric for it would be worse than admitting that."
        ),
    ),
    # =========================================================================
    #  WHAT THE PRODUCER ACTUALLY WATCHES
    # =========================================================================
    Metric(
        name="Fermentation time",
        symbol="t_ferm",
        unit="hours to years",
        typical="4 - 12 h for yoghurt, days for vegetables, months to years "
        "for cheese, soy sauce and cured meat",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The range across a single record is five orders of magnitude, "
            "which is unusual and is the point: these are the same underlying "
            "chemistry operating on completely different timescales, and the "
            "long ones tie up capital and space in a way the short ones do not."
        ),
    ),
    Metric(
        name="Batch loss rate",
        symbol="R_loss",
        unit="per cent of batches failing to meet specification",
        typical="low in controlled dairy production and higher in spontaneous "
        "and long-aged products",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The commercial expression of everything above. It is the number "
            "that justified defined starters historically, and it is also the "
            "cost a producer accepts in exchange for the character that a "
            "community fermentation gives."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  The safety and growth relationships first, then the kinetics.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "water_activity",
    "specific_growth_rate",
    "monod_equation",
    "arrhenius_equation",
    "thermal_death_kinetics",
    "mass_balance",
)
