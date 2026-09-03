# =============================================================================
#  biotechnology.branches.grey.phytoremediation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks;
#  this record has a substantial one, and it is a setback in which the
#  technique worked too well.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE CHELATE EPISODE IS THE MOST INSTRUCTIVE THING IN THIS TIMELINE.
#
#  By the late 1990s the obstacle to phytoextraction was clear: most soil metal
#  is not available to roots. The solution was equally clear, and it worked.
#  Adding a strong synthetic chelating agent dissolved the metal, uptake rose
#  several-fold, and the published results were the best the field had seen.
#
#  The chelate also dissolved metal the plants did not take up, and that metal
#  moved downwards toward groundwater. A technique for cleaning soil had been
#  turned into a technique for washing metal into an aquifer. The practice was
#  curtailed.
#
#  It is worth recording precisely because nothing went wrong scientifically.
#  The mechanism was understood, the result was reproducible, and the "failure"
#  was that the system boundary had been drawn around the soil when it should
#  have been drawn around the soil and the water beneath it. That is a general
#  lesson about remediation, and this is the clearest instance of it in the
#  library.
#
#  A SECOND POINT ABOUT THIS TIMELINE. The oldest entries are not remediation
#  at all. Hyperaccumulation was found by botanists studying why certain plants
#  grow on metal-rich soils, and by prospectors using them to find ore. The
#  cleanup application arrived last, which is why the useful species were
#  discovered rather than designed.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  FOUND BY BOTANISTS, NOT BY ENGINEERS
    # =========================================================================
    Milestone(
        1865,
        "Unusually high zinc content is reported in a plant growing on "
        "metal-rich soil",
        note=(
            "An observation of natural history rather than a technology. "
            "Certain plants growing on mineralised ground were found to contain "
            "metal concentrations far above the surrounding vegetation, which "
            "was a curiosity for a century before anybody proposed using it."
        ),
    ),
    Milestone(
        1948,
        "Nickel hyperaccumulation is documented in serpentine flora",
        note=(
            "Plants on ultramafic soils accumulating nickel to percentages of "
            "dry weight, which is the concentration that makes phytomining "
            "conceivable. The species that matter to this record were found by "
            "surveying such soils rather than by breeding or engineering, which "
            "is why the field's capability is bounded by what happens to exist."
        ),
    ),
    Milestone(
        1960,
        "Geobotanical prospecting uses metal-accumulating plants to locate ore "
        "bodies",
        note=(
            "The capability was first put to work in the opposite direction, "
            "to find metal rather than to remove it. It established the "
            "botanical survey methods and the species records that the "
            "remediation application later drew on."
        ),
    ),
    # =========================================================================
    #  THE IDEA IS TURNED AROUND
    # =========================================================================
    Milestone(
        1983,
        "The term phytoremediation is introduced and cleanup applications are "
        "proposed",
        note=(
            "The proposal that accumulation could be used deliberately to strip "
            "metal from contaminated soil. It arrived after a century of "
            "botanical observation, which is unusual: the phenomenon was fully "
            "described long before anyone thought to apply it."
        ),
    ),
    Milestone(
        1991,
        "Constructed wetlands are established for mine drainage and wastewater "
        "treatment",
        note=(
            "A different and more immediately practical branch of the record. "
            "Wetland systems treat acid mine drainage and effluent continuously "
            "for decades on almost no operating input, and they were working at "
            "scale while the extraction work was still in trials."
        ),
    ),
    Milestone(
        1994,
        "Poplar and willow plantings are used for hydraulic control of "
        "groundwater plumes",
        note=(
            "The application that turned out to be the field's most reliable, "
            "and it extracts nothing. Trees transpiring enough water to arrest "
            "a plume provide containment at a small fraction of the cost of "
            "pumping and treating, and the mechanism is hydraulic rather than "
            "biochemical."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: IT WORKED, AND THAT WAS THE PROBLEM
    # =========================================================================
    Milestone(
        1997,
        "Chelate-assisted extraction raises metal uptake several-fold",
        note=(
            "The obstacle was bioavailability, and adding a strong synthetic "
            "chelating agent removed it. Uptake rose sharply and the results "
            "were the most encouraging the extraction field had produced. The "
            "mechanism was understood and the effect was reproducible."
        ),
    ),
    Milestone(
        2001,
        "Chelate-mobilised metal is shown to leach toward groundwater, and the "
        "practice is curtailed",
        note=(
            "The chelate dissolved far more metal than the plants took up, and "
            "the excess moved downward. A soil cleanup technique had been "
            "converted into a route for contaminating an aquifer. Regulatory "
            "and practical restriction followed, and biodegradable agents were "
            "developed as a partial replacement. The scientific work was sound "
            "throughout; the system boundary had been drawn around the soil "
            "alone."
        ),
    ),
    # =========================================================================
    #  THE CAPABILITIES THAT WERE ACTUALLY MISSING
    # =========================================================================
    Milestone(
        2001,
        "Arsenic hyperaccumulation is identified in a fern",
        note=(
            "Arsenic had no effective biological removal route, and the "
            "discovery of a fern that accumulates it strongly supplied one. It "
            "is a good illustration of the field's dependence on survey: the "
            "capability was found in an existing species rather than "
            "constructed, and there is no method for producing an equivalent "
            "for a contaminant that lacks one."
        ),
    ),
    Milestone(
        2005,
        "Nickel phytomining is demonstrated at field scale on ultramafic soils",
        note=(
            "The only application in this record where the extracted metal has "
            "enough value to offset part of the cost. The harvest is smelted "
            "deliberately rather than disposed of, which inverts the record's "
            "usual waste problem and is the reason nickel is the case that "
            "works commercially."
        ),
    ),
    # =========================================================================
    #  REGULATORY ACCEPTANCE, AND THE PART NOBODY BUDGETED FOR
    # =========================================================================
    Milestone(
        2010,
        "Phytostabilisation and vegetative covers are accepted as remediation "
        "outcomes at large mining sites",
        note=(
            "Acceptance that holding contaminated material in place with "
            "vegetation is a legitimate endpoint over areas too large for any "
            "engineered treatment. It is containment rather than removal and "
            "it is recorded as such, which is the same honesty "
            "`grey.bioremediation` applies to monitored natural attenuation."
        ),
    ),
    Milestone(
        2015,
        "Contaminated harvest disposal is recognised as a governing cost of "
        "extraction projects",
        note=(
            "The step most often omitted from early cost estimates. A "
            "successful phytoextraction produces contaminated biomass by "
            "definition, and that material is hazardous waste. Combustion "
            "reduces its volume and concentrates the metal into ash. Recording "
            "this as a milestone rather than as a caveat reflects how much it "
            "changed the economics of the technique."
        ),
    ),
    Milestone(
        2018,
        "Transgenic enhancement of uptake is demonstrated in the laboratory "
        "and remains excluded from field use",
        note=(
            "Engineered tolerance and transformation capabilities exceed what "
            "the surveyed species offer, and deliberate release requirements "
            "keep them in containment. The constraint here is regulatory rather "
            "than technical, which is the same position "
            "`grey.bioaugmentation` records for engineered degraders."
        ),
    ),
)
