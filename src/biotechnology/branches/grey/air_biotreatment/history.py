# =============================================================================
#  biotechnology.branches.grey.air_biotreatment.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS FIELD BEGAN AS A SOIL BED WITH A PIPE UNDER IT, AND THAT ORIGIN
#  EXPLAINS ITS LATER DIFFICULTIES.
#
#  Early odour control consisted of venting foul air into buried soil and
#  letting whatever lived there deal with it. It worked, cost almost nothing,
#  and carried three problems that the next eighty years were spent solving:
#  soil compacts so the air channels, soil dries so the organisms die, and soil
#  has no buffer so acid-producing degradation destroys its own community.
#
#      EVERY LATER CONFIGURATION IN THIS RECORD IS AN ANSWER TO ONE OF THOSE
#      THREE.
#
#  Structured packing answers compaction, humidification and irrigation answer
#  drying, and recirculating liquid answers acidification. That is a tidy
#  history and it is genuinely how the field developed.
#
#  THE SETBACK RECORDED HERE IS AN HONEST ONE AND IT IS NOT A FAILURE OF
#  EXECUTION. In the 1990s the technique was extended from odour to chlorinated
#  and other poorly soluble solvents, on the reasonable assumption that a
#  degradable compound could be treated. It failed, and it failed for a reason
#  that no improvement in the biology could address: the compounds were never
#  entering the water phase. The boundary that resulted is a real scientific
#  boundary rather than a temporary limitation.
#
#  RULE 8 NOTE: the 1970s development was parallel in several countries, with
#  the Netherlands, Germany and Japan working on the same problem at the same
#  time, and it is recorded without crediting one.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  A HOLE IN THE GROUND WITH A PIPE IN IT
    # =========================================================================
    Milestone(
        1923,
        "Soil beds are used to treat odorous air from sewage installations",
        note=(
            "Foul air vented into buried soil and left to whatever lived there. "
            "It worked, it cost almost nothing, and it carried the three "
            "problems the rest of this timeline addresses: the soil compacts so "
            "the air channels through, it dries so the organisms die, and it "
            "has no buffer so acid-producing degradation kills its own "
            "community."
        ),
    ),
    Milestone(
        1955,
        "Open soil biofilters are installed at wastewater and rendering sites",
        note=(
            "The first deliberate engineering of the arrangement above, with "
            "distribution pipework and a designed bed depth rather than an "
            "improvised trench. Odour control had become a specifiable service, "
            "and the driver was already what it remains: complaints from the "
            "people living nearby."
        ),
    ),
    # =========================================================================
    #  ENGINEERED BEDS, DEVELOPED IN SEVERAL PLACES AT ONCE
    # =========================================================================
    Milestone(
        1970,
        "Engineered biofilters on compost and bark packing are developed in "
        "parallel in several countries",
        note=(
            "Replacing soil with a designed organic packing gave better void "
            "structure, more surface area and lower pressure drop, and it "
            "answered the compaction problem for a few years at a time. The "
            "work proceeded simultaneously in the Netherlands, Germany and "
            "Japan under similar regulatory pressure, and it is not properly "
            "attributable to any one of them."
        ),
    ),
    Milestone(
        1980,
        "Humidification of the incoming air is established as a requirement "
        "rather than an option",
        note=(
            "Beds were failing from the inlet end, and the cause was that dry "
            "air was drying the biofilm faster than irrigation could replace "
            "the water. Saturating the air before it enters is now standard and "
            "it is the single most effective correction ever made to this "
            "technique."
        ),
    ),
    # =========================================================================
    #  SOLVING ACIDIFICATION BY GIVING THE BED A LIQUID PHASE
    # =========================================================================
    Milestone(
        1985,
        "Biotrickling filters with recirculated liquid enter use for hydrogen "
        "sulphide",
        note=(
            "Sulphide oxidation produces sulphuric acid, which destroys the "
            "community producing it. Recirculating liquid over an inert packing "
            "allows the acid to be washed out and the pH and nutrients to be "
            "controlled. This is why sulphide treatment uses this "
            "configuration rather than a compost bed, and it is a case of a "
            "process being redesigned around its own product."
        ),
    ),
    Milestone(
        1990,
        "Air emission legislation extends to odour and volatile organic "
        "compounds at waste facilities",
        note=(
            "Regulatory limits turned odour control from a neighbourly courtesy "
            "into a permit condition, and they created the commercial sector. "
            "It is the same pattern as `grey.biowaste_treatment`, where "
            "legislation rather than science drove deployment."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A BOUNDARY, NOT A FAILURE
    # =========================================================================
    Milestone(
        1995,
        "Extension to chlorinated and poorly soluble solvents fails, and the "
        "cause is identified as partitioning rather than degradation",
        note=(
            "The technique was applied to compounds that organisms will degrade "
            "in suspension, on the reasonable assumption that degradability was "
            "the criterion. Performance was poor and could not be improved by "
            "longer beds, better packing or better organisms, because the "
            "compounds were not entering the water film where the organisms "
            "live. The resulting boundary is a property of chemistry rather "
            "than a limitation of engineering, and it is why this record's "
            "scope is a list of compounds."
        ),
    ),
    # =========================================================================
    #  WORKING ON THE BOUNDARY RATHER THAN AGAINST IT
    # =========================================================================
    Milestone(
        2000,
        "Two-phase partitioning bioreactors are developed to carry poorly "
        "soluble compounds into the aqueous phase",
        note=(
            "Adding a second liquid phase that dissolves what water will not, "
            "and releases it gradually to the organisms. It is a direct attack "
            "on the 1995 boundary, it works, and it costs enough that it has "
            "remained a specialist rather than a general solution."
        ),
    ),
    Milestone(
        2003,
        "Dynamic olfactometry is standardised, giving odour a reproducible "
        "measurement",
        note=(
            "EN 13725 defined the odour unit through a standardised procedure "
            "using trained human panels. It made a subjective nuisance into a "
            "measurable quantity that could be written into a permit, which is "
            "what allowed odour to be regulated numerically at all. The unit "
            "remains a person, and it is reproducible."
        ),
    ),
    Milestone(
        2008,
        "Landfill biocovers using methanotrophic soil layers are demonstrated "
        "at field scale",
        note=(
            "Engineered cover layers in which methanotrophs oxidise methane "
            "escaping the cap. It works at low flux and cannot handle a "
            "concentrated stream, since methane is the least soluble compound "
            "this record deals with, so it is a partial answer to a large "
            "problem rather than a solution to it."
        ),
    ),
    # =========================================================================
    #  BECOMING PART OF ANOTHER PROCESS
    # =========================================================================
    Milestone(
        2012,
        "Biological desulphurisation is integrated into biogas plants by "
        "controlled micro-aeration",
        note=(
            "Admitting a small, carefully controlled quantity of air into the "
            "digester headspace lets sulphide-oxidising organisms remove "
            "hydrogen sulphide without a separate vessel. It protects the gas "
            "engines that `grey.biowaste_treatment` depends on, and it is the "
            "point at which this record stopped being a bolt-on and became part "
            "of the process it serves."
        ),
    ),
    Milestone(
        2018,
        "Bioaerosol emission from biofilter media is recognised as an exposure "
        "concern in its own right",
        note=(
            "Organic packings release spores and bacterial fragments into the "
            "treated air stream, so a technique installed to remove an emission "
            "generates one of its own. It is recorded because it is the "
            "clearest instance in this record of a treatment whose own "
            "byproduct had to be assessed, and it pushed installations near "
            "housing toward inert media."
        ),
    ),
)
