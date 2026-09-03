# =============================================================================
#  biotechnology.branches.white.microbial_fermentation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two: the single cell protein plant of 1980, and the
#  quieter, continuing setback that continuous fermentation lost to batch
#  operation for reasons that were never scientific.
#
#  SUBTYPE-SPECIFIC NOTE
#  The 1943 entry is the pivot of this timeline and arguably of the whole white
#  branch. Penicillin made in shallow trays could not be produced in the
#  quantities a war required. Moving the culture into a deep aerated tank
#  changed the yield by orders of magnitude and created the equipment, the
#  sterile technique and the engineering discipline that every subsequent entry
#  in this record uses. Almost every fermenter operating today is a descendant
#  of that vessel.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  UNDERSTANDING WHAT FERMENTATION IS
    # =========================================================================
    Milestone(
        1857,
        "Pasteur establishes that fermentation is caused by living "
        "microorganisms",
        note=(
            "Before this, fermentation was regarded as a purely chemical "
            "decomposition. Recognising that a specific organism does the work "
            "is what made it possible to choose one, protect it, and eventually "
            "engineer it."
        ),
    ),
    Milestone(
        1881,
        "Koch introduces solid media and pure culture technique",
        note=(
            "The ability to isolate and maintain one organism free of all "
            "others. Every seed train and cell bank in "
            "`practice.TECHNOLOGIES` rests on this, and so does the entire "
            "concept of a contaminated batch."
        ),
    ),
    # =========================================================================
    #  THE FIRST LARGE INDUSTRIAL PROCESSES
    # =========================================================================
    Milestone(
        1916,
        "Weizmann's acetone-butanol-ethanol fermentation is deployed at "
        "industrial scale",
        note=(
            "Driven by wartime demand for acetone. The first genuinely large "
            "industrial fermentation, and a demonstration that microbial "
            "production could compete with chemical manufacture, at least while "
            "the alternative was unavailable."
        ),
    ),
    Milestone(
        1923,
        "Citric acid production by Aspergillus niger displaces extraction from "
        "citrus fruit",
        note=(
            "An early and complete substitution of a fermentation route for an "
            "agricultural one, and it remains among the largest organic acid "
            "fermentations in operation a century later."
        ),
    ),
    # =========================================================================
    #  THE PIVOT
    # =========================================================================
    Milestone(
        1943,
        "Submerged deep-tank aerated fermentation is developed for penicillin",
        note=(
            "Penicillin grown in shallow trays could not meet wartime demand. "
            "Moving to a deep stirred and aerated vessel, together with a "
            "higher-yielding mould strain and corn steep liquor as a cheap "
            "nutrient source, raised output by orders of magnitude. It created "
            "the vessel design, the sterile operating discipline and the "
            "engineering profession that every later entry depends on. Almost "
            "every industrial fermenter in the world today is a descendant of "
            "this one."
        ),
    ),
    # =========================================================================
    #  THE THEORY OF CONTINUOUS CULTURE
    # =========================================================================
    Milestone(
        1950,
        "The chemostat is described, allowing growth rate to be set by the "
        "operator",
        note=(
            "Monod, and independently Novick and Szilard, showed that in "
            "continuous culture the dilution rate sets the specific growth "
            "rate. It became the fundamental tool of microbial physiology and, "
            "as the 1980 entry records, did not become the fundamental tool of "
            "manufacturing."
        ),
    ),
    Milestone(
        1957,
        "Glutamate fermentation begins commercial operation",
        note=(
            "The start of the amino acid industry, now the largest tonnage in "
            "this record. Its strain history belongs to "
            "`white.metabolic_engineering`; its vessels belong here."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE PROCESS WORKED AND THE MARKET DID NOT
    # =========================================================================
    Milestone(
        1980,
        "A large continuous single cell protein plant begins operation and is "
        "closed within a decade",
        note=(
            "The process fed methanol to bacteria to make animal feed protein, "
            "and it ran in one of the largest continuous sterile fermenters "
            "ever built, sustaining aseptic operation for months. Technically "
            "it succeeded. Commercially it was destroyed by the price of soya "
            "meal, against which a purpose-built plant burning a purchased "
            "feedstock could not compete. Two lessons are recorded: a "
            "fermentation product competing with an agricultural commodity is "
            "competing with land, sunlight and millions of growers; and the "
            "most technically impressive demonstration of continuous "
            "fermentation in history became the reason the industry treated it "
            "as risky."
        ),
    ),
    # =========================================================================
    #  RECOMBINANT PRODUCTION AND THE MODERN PLANT
    # =========================================================================
    Milestone(
        1982,
        "Recombinant human insulin produced in Escherichia coli is approved",
        note=(
            "The first recombinant pharmaceutical, and the moment fermentation "
            "stopped being a way to harvest what an organism already made and "
            "became a way to manufacture what it was instructed to make."
        ),
    ),
    Milestone(
        1990,
        "Fed-batch operation with controlled feeding becomes standard "
        "industrial practice",
        note=(
            "The recognition that holding specific growth rate below the "
            "overflow threshold matters more than maximising it. This is the "
            "operational form of the record's central idea, and it is why "
            "mu_crit rather than mu_max appears in `metrics.py` as the number "
            "that governs a process."
        ),
    ),
    Milestone(
        2005,
        "Single-use bioreactors enter widespread use",
        note=(
            "Pre-sterilised disposable bags removed cleaning and sterilisation "
            "between campaigns, cutting turnaround and cross-contamination "
            "risk. They shifted the economics towards smaller, more flexible "
            "and multi-product facilities, at the cost of a plastic waste "
            "stream that a life cycle assessment must count."
        ),
    ),
    Milestone(
        2015,
        "Non-sterile and contamination-resistant fermentation is adopted for "
        "low-value products",
        note=(
            "Operating at a pH, temperature or on a substrate that only the "
            "production organism tolerates removes the largest fixed cost in "
            "the process. It is the clearest example in this record of solving "
            "a problem by making it irrelevant rather than by controlling it."
        ),
    ),
    Milestone(
        2022,
        "Gas fermentation of industrial off-gas reaches commercial operation",
        note=(
            "Carbon monoxide and carbon dioxide as feedstock rather than sugar. "
            "It addresses the food and land competition that defeated the 1980 "
            "single cell protein plant, and it does so by using a feedstock "
            "nobody else wants."
        ),
    ),
)
