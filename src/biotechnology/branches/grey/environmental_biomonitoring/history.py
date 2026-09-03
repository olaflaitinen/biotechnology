# =============================================================================
#  biotechnology.branches.grey.environmental_biomonitoring.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FOUNDING WORK OF THIS FIELD WAS A CLASSIFICATION OF DIRTINESS, PUBLISHED
#  IN 1908, AND ITS LOGIC HAS NOT BEEN IMPROVED ON.
#
#  The saprobic system classified river stretches by which organisms lived in
#  them, on the observation that species differ in what they tolerate. Every
#  index in use today is a refinement of that argument. The refinements are
#  real, and the idea is a century old and was correct when it was made.
#
#  THE SETBACK IN THIS RECORD IS UNUSUAL AND IS WORTH READING CAREFULLY,
#  BECAUSE THE PROBLEM WAS RECOGNISED RATHER THAN CAUSED.
#
#  In 1995 the shifting baseline argument was set out: fisheries scientists
#  were each taking the state of the sea at the start of their own careers as
#  the natural condition, so the estimated baseline slid downward with every
#  generation while each generation believed it was measuring against nature.
#  Nothing failed. A whole discipline discovered that its reference point had
#  been moving underneath it for decades, which is a harder kind of error than
#  a broken method and one that no instrument fixes.
#
#  A SECOND POINT ABOUT THE ENVIRONMENTAL DNA ENTRIES. The technique was
#  demonstrated in 2008, adopted for regulatory survey within about a decade,
#  and it depends entirely on reference databases built by taxonomists whose
#  discipline is declining. The record states that dependency rather than
#  presenting the method as self-sufficient.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE IDEA, AND IT WAS RIGHT THE FIRST TIME
    # =========================================================================
    Milestone(
        1908,
        "The saprobic system classifies river condition by the organisms "
        "present",
        note=(
            "Stretches of river were graded by which species lived in them, on "
            "the observation that organisms differ systematically in what "
            "pollution they tolerate. Every biotic index in use today is a "
            "refinement of that argument rather than a replacement for it, "
            "which is unusual for a technique this old."
        ),
    ),
    Milestone(
        1955,
        "Lichen surveys are used to map air quality across industrial regions",
        note=(
            "Lichens are sensitive to sulphur dioxide and accumulate deposition "
            "over years, so their distribution mapped air quality across whole "
            "cities at a time when almost no monitoring instruments existed. It "
            "is the clearest early demonstration that an organism can be a "
            "recording instrument rather than merely a subject."
        ),
    ),
    Milestone(
        1964,
        "Standardised biotic indices for river invertebrates are adopted for "
        "regulatory assessment",
        note=(
            "Turning the 1908 idea into a number that could be compared between "
            "catchments and written into policy. Standardisation is what made "
            "the method regulatory rather than descriptive, and it introduced "
            "the dependence on identical field method that the practice facet "
            "records as a limitation."
        ),
    ),
    # =========================================================================
    #  USING ORGANISMS TO FIND WHAT INSTRUMENTS CANNOT
    # =========================================================================
    Milestone(
        1976,
        "Mussel watch programmes establish bioaccumulation monitoring of "
        "coastal contaminants",
        note=(
            "Filter feeders concentrate persistent contaminants from very large "
            "volumes of water, making measurable what is below detection in the "
            "water itself. It also produced comparable long time series across "
            "coastlines, which is the property that makes a monitoring "
            "programme valuable and the property most easily destroyed by a "
            "funding gap."
        ),
    ),
    Milestone(
        1985,
        "Biomarker methods enter environmental assessment",
        note=(
            "Measuring a physiological response, such as enzyme induction in "
            "fish, rather than a concentration or a community. It gave the "
            "earliest available warning of exposure and it is the least "
            "specific evidence in the record, which is the trade the technique "
            "has always carried."
        ),
    ),
    Milestone(
        1990,
        "Whole effluent toxicity testing is incorporated into discharge "
        "permitting",
        note=(
            "Asking whether a discharge harms organisms rather than whether it "
            "exceeds a list of substance limits. It addressed the case a "
            "substance-by-substance consent cannot reach, which is a mixture "
            "whose components are each individually compliant."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE REFERENCE POINT HAD BEEN MOVING ALL ALONG
    # =========================================================================
    Milestone(
        1995,
        "The shifting baseline syndrome is described in fisheries science",
        note=(
            "Each generation of scientists was taking the state of the sea at "
            "the start of its own career as the natural condition, so the "
            "estimated baseline slid downward with every generation while each "
            "believed it was measuring against nature. No method failed. A "
            "discipline found that its reference point had been moving beneath "
            "it for decades, which is why `metrics.py` places the reference "
            "condition first and states that it is a judgement rather than an "
            "observation."
        ),
    ),
    # =========================================================================
    #  ASSESSMENT BECOMES A LEGAL OBLIGATION
    # =========================================================================
    Milestone(
        2000,
        "Water framework legislation makes ecological status a legal "
        "classification",
        note=(
            "Requiring water bodies to be classified by biological condition "
            "rather than by chemistry alone, and requiring them to reach good "
            "status. It made this record's output a legal object and it made "
            "the reference condition a matter with consequences, since the "
            "expectation a water body is judged against determines whether a "
            "state is liable."
        ),
    ),
    # =========================================================================
    #  READING WHAT ORGANISMS LEAVE BEHIND
    # =========================================================================
    Milestone(
        2008,
        "Environmental DNA is demonstrated for detecting aquatic species from "
        "water samples",
        note=(
            "Genetic material shed by animals was recovered from filtered water "
            "and used to detect their presence without catching anything. The "
            "first demonstrations targeted single species, and the significance "
            "was immediately clear: survey without capture, handling or "
            "mortality, at a fraction of the cost."
        ),
    ),
    Milestone(
        2012,
        "Metabarcoding extends environmental DNA from single species to whole "
        "communities",
        note=(
            "Universal primers and high-throughput sequencing produced a "
            "community list from one sample rather than a yes or no answer for "
            "one species. This is the point at which the method became a survey "
            "technique rather than a detection tool, and it is also the point "
            "at which reference database coverage became the limiting factor."
        ),
    ),
    Milestone(
        2016,
        "Environmental DNA is accepted in regulatory survey and invasive "
        "species programmes",
        note=(
            "Adoption for statutory survey of protected species and for early "
            "detection of invaders, which is where the method's advantage is "
            "clearest because detection while a population is still small is "
            "what makes a response possible. Acceptance came with protocols "
            "specifying filtration, contamination control and interpretation, "
            "since the method is sensitive enough to detect the previous "
            "sample."
        ),
    ),
    # =========================================================================
    #  A SEWER TURNS OUT TO BE AN INSTRUMENT FOR MEASURING PEOPLE
    # =========================================================================
    Milestone(
        2020,
        "Wastewater surveillance is deployed at population scale for infectious "
        "disease",
        note=(
            "Sewage was used to track pathogen prevalence across whole "
            "populations, including people never tested individually, giving "
            "signal days ahead of clinical reporting at a fraction of the cost. "
            "It also demonstrated that the same infrastructure can measure "
            "anything a population excretes, which is why "
            "`governance.py` treats it separately from the ecological work: "
            "nobody in the catchment consented, and the method extends readily "
            "beyond disease."
        ),
    ),
    Milestone(
        2022,
        "Taxonomic expertise decline is identified as a constraint on molecular "
        "monitoring",
        note=(
            "Metabarcoding depends entirely on reference sequence databases, "
            "and those databases are built by taxonomists identifying and "
            "depositing specimens. That discipline has been contracting for "
            "decades. The newest method in this record therefore rests on the "
            "oldest, and the dependency runs in the direction fewest people "
            "expect."
        ),
    ),
)
