# =============================================================================
#  biotechnology.branches.yellow.food_safety_biotechnology.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two of a kind that recur: an adulteration designed
#  specifically to defeat the test in use, and a contamination that spread
#  through a supply chain nobody could trace quickly enough.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE 2008 MELAMINE ADULTERATION IS THE MOST INSTRUCTIVE ENTRY AND IT IS NOT
#  A DETECTION FAILURE.
#
#  Protein content in milk was measured by nitrogen content, which is cheap,
#  standard and correct for genuine milk. Melamine is nitrogen-rich and cheap,
#  so adding it raised the apparent protein of diluted milk. The test performed
#  exactly as designed. It was defeated because someone understood what it
#  measured and supplied that instead.
#
#  Infants died and many thousands were injured. The lesson is that
#  authenticity testing is an ADVERSARIAL problem rather than an analytical
#  one: a test whose principle is public will be gamed by whoever profits from
#  gaming it, and the defence is unpredictability and orthogonal methods rather
#  than sensitivity.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE CULTURE ERA, AND ITS BUILT-IN DELAY
    # =========================================================================
    Milestone(
        1881,
        "Pure culture technique establishes the method food microbiology would "
        "use for a century",
        note=(
            "Growing the organism to identify it. Extremely sensitive, entirely "
            "reliable, and slow, because the answer cannot arrive faster than "
            "the bacterium divides. Every limitation this record's first "
            "milestones address is a consequence of that."
        ),
    ),
    Milestone(
        1960,
        "Aflatoxin is identified after a mass poisoning of farmed turkeys",
        note=(
            "The investigation of turkey X disease established that a fungal "
            "metabolite in feed could be a potent toxin and carcinogen. It "
            "created mycotoxin regulation as a field, and it established the "
            "principle that matters most about toxins: the hazard outlasts the "
            "organism, so killing the fungus does not make the food safe."
        ),
    ),
    Milestone(
        1971,
        "Hazard analysis and critical control points is adopted as a framework "
        "for food safety",
        note=(
            "Developed for spaceflight food, where testing a finished product "
            "to destruction was not an option. It shifted the emphasis from "
            "end-product testing to controlling the process, which is the "
            "framework every result in this record is interpreted within."
        ),
    ),
    # =========================================================================
    #  THE METHODS THAT REMOVED THE DELAY
    # =========================================================================
    Milestone(
        1985,
        "Polymerase chain reaction makes rapid nucleic acid detection possible",
        note=(
            "The technique that eventually removed the multi-day wait. Its "
            "adoption in food lagged clinical use by years because food is a "
            "far less cooperative matrix, and inhibition by fat, protein and "
            "polyphenols had to be solved before the method was usable."
        ),
    ),
    Milestone(
        1996,
        "Real-time PCR enters routine food testing",
        note=(
            "Quantification without a separate detection step, and a result in "
            "hours rather than days. This is the entry where the change "
            "described in `narrative.py` actually happens: the answer begins "
            "arriving while the batch is still under the producer's control."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: CONTAMINATION FASTER THAN TRACEABILITY
    # =========================================================================
    Milestone(
        1993,
        "A large Escherichia coli O157 outbreak in undercooked beef changes "
        "food safety regulation",
        note=(
            "Children died. The organism has a very low infectious dose and the "
            "product had been distributed widely before any case was "
            "recognised. It led to the pathogen being treated as an adulterant "
            "in certain products and to routine testing, and it demonstrated "
            "that a distribution system faster than an investigation is a "
            "safety problem in itself."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A TEST DEFEATED BY DESIGN
    # =========================================================================
    Milestone(
        2008,
        "Melamine adulteration of milk and infant formula kills infants and "
        "injures many thousands",
        note=(
            "Protein was measured by nitrogen content, which is standard and "
            "correct for genuine milk. Melamine is nitrogen-rich and cheap, so "
            "adding it to diluted milk raised the apparent protein. The test "
            "worked exactly as designed and was defeated by someone who "
            "understood what it measured. It is recorded as the record's "
            "central setback because it establishes that authenticity testing "
            "is adversarial rather than analytical: a published test principle "
            "will be gamed, and the defence is orthogonal methods and "
            "unpredictability rather than better sensitivity."
        ),
    ),
    # =========================================================================
    #  THE SECOND TRANSFORMATION
    # =========================================================================
    Milestone(
        2011,
        "A large Shiga toxin-producing Escherichia coli outbreak is resolved by "
        "rapid genome sequencing",
        note=(
            "The organism was sequenced and characterised within days by "
            "several groups working openly, which was unprecedented during an "
            "active outbreak. It demonstrated that sequencing could contribute "
            "to an investigation rather than only to its retrospective "
            "analysis. It also produced early misattribution to the wrong "
            "vegetable, with severe economic consequences for growers, which is "
            "part of the lesson."
        ),
    ),
    Milestone(
        2013,
        "The horsemeat incident establishes food authenticity as a mainstream "
        "concern",
        note=(
            "Undeclared horsemeat in products labelled beef across several "
            "countries. Nobody was made ill, which is precisely why it matters "
            "here: it revealed that supply chains were too long and too opaque "
            "for anyone to know what was in a product, and a system that cannot "
            "detect substitution cannot detect contamination either."
        ),
    ),
    Milestone(
        2015,
        "Routine whole genome sequencing of isolates begins in public health "
        "surveillance",
        note=(
            "Sequencing every isolate rather than only outbreak-associated "
            "ones. It began detecting clusters that nobody had recognised as "
            "outbreaks, because the cases were few, geographically scattered "
            "and individually unremarkable. It is the single largest advance in "
            "outbreak detection this record contains."
        ),
    ),
    # =========================================================================
    #  WHERE THE FIELD IS GOING, AND WHAT IT HAS NOT SOLVED
    # =========================================================================
    Milestone(
        2018,
        "Metagenomic and culture-independent methods are applied to food "
        "testing",
        note=(
            "Sequencing everything in a sample rather than looking for a named "
            "target, which finds organisms nobody thought to test for. It "
            "imports the interpretation problem `blue.marine_genomics` records: "
            "a sequence detected is not necessarily a viable organism and not "
            "necessarily a hazard."
        ),
    ),
    Milestone(
        2020,
        "Portable sequencing and isothermal methods move testing out of the "
        "laboratory",
        note=(
            "Testing at the production site and in the supply chain rather than "
            "in a central laboratory, which shortens the interval further and "
            "begins to address the uneven distribution of testing capacity that "
            "this record records as a fairness problem."
        ),
    ),
    Milestone(
        2022,
        "Sampling rather than analytical sensitivity is recognised as the "
        "binding constraint",
        note=(
            "Method performance improved to the point where the statistical "
            "limits of sampling plans became the dominant source of "
            "uncertainty. It is not a discovery so much as an admission, and it "
            "redirected effort towards environmental monitoring and process "
            "control, which sample the problem rather than the product."
        ),
    ),
)
