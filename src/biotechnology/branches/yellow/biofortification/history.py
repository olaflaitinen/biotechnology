# =============================================================================
#  biotechnology.branches.yellow.biofortification.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks.
#  The provitamin A rice sequence between 1999 and the 2020s is the longest
#  single setback in this library and is recorded across several entries
#  because its duration is the point.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE RICE STORY IS TOLD BADLY BY EVERYONE AND THE FACTS ARE UNCOMFORTABLE FOR
#  ALL SIDES.
#
#  The original 1999 construct produced too little provitamin A to matter
#  nutritionally, which is a scientific fact and was not always stated clearly
#  by its advocates. A second-generation construct in 2005 raised the content
#  by a large factor and made the nutritional argument real. Approvals for food
#  use followed in several countries from 2018, and the Philippines approved
#  commercial propagation in 2021, becoming the first country to do so. In 2024
#  an appellate court there revoked the biosafety permits, and the position has
#  remained subject to further legal process.
#
#  So the honest summary is: the first version did not work well enough, the
#  second did, and twenty-five years after the first publication the crop has
#  still not been grown at scale by farmers. Advocates who blame opposition
#  alone omit the first fact. Opponents who cite the first version's weakness
#  omit that it was superseded in 2005.
#
#  MEANWHILE the conventionally bred crops were released and eaten, which is
#  the comparison this record exists to make.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE PROBLEM IS NAMED
    # =========================================================================
    Milestone(
        1990,
        "Micronutrient deficiency is recognised as a distinct global health "
        "problem separate from calorie deficiency",
        note=(
            "The term hidden hunger enters use. It matters because every "
            "measurement system in place was counting calories, so a population "
            "eating enough and deficient in iron, zinc and vitamin A was "
            "invisible to the statistics used to direct food policy."
        ),
    ),
    Milestone(
        1993,
        "Vitamin A supplementation is shown to reduce child mortality "
        "substantially",
        note=(
            "Trials established that the deficiency was not only causing "
            "blindness but killing children through increased susceptibility to "
            "ordinary infections. It made micronutrient status a mortality "
            "question and created the urgency that funded everything after."
        ),
    ),
    # =========================================================================
    #  THE ENGINEERED ROUTE, AND ITS FIRST VERSION
    # =========================================================================
    Milestone(
        1999,
        "Provitamin A biosynthesis is engineered into rice endosperm",
        note=(
            "Rice endosperm makes no carotenoid at all, so the pathway had to "
            "be introduced rather than enhanced, which no amount of breeding "
            "could achieve. It was a genuine scientific achievement and the "
            "content was too low to meet a meaningful share of vitamin A "
            "requirement, a limitation that was not always stated clearly by "
            "its advocates at the time."
        ),
    ),
    Milestone(
        2005,
        "A second-generation construct raises provitamin A content by a large "
        "factor",
        note=(
            "The version that made the nutritional argument real, and the one "
            "every subsequent regulatory submission concerns. Criticism of the "
            "1999 content is frequently still repeated as though this entry had "
            "not happened."
        ),
    ),
    # =========================================================================
    #  THE CONVENTIONAL ROUTE, WHICH DELIVERED
    # =========================================================================
    Milestone(
        2003,
        "A coordinated international biofortification programme is established",
        note=(
            "HarvestPlus and its partners set breeding targets derived from "
            "deficiency prevalence, consumption data, retention and "
            "bioavailability, which is the backwards calculation "
            "`metrics.py` records as the field taking its own chain seriously. "
            "It concentrated on conventional breeding, which turned out to be "
            "the decision that mattered."
        ),
    ),
    Milestone(
        2007,
        "Orange-fleshed sweet potato is released and distributed at scale in "
        "sub-Saharan Africa",
        note=(
            "Conventionally bred, vegetatively propagated through community "
            "vine multiplication, and accompanied by demand creation for a "
            "visible trait in populations accustomed to white varieties. It is "
            "the field's clearest delivered success and the work that made it "
            "succeed was distribution and acceptance rather than breeding."
        ),
    ),
    Milestone(
        2012,
        "Iron-biofortified beans and pearl millet are released in Africa and "
        "India",
        note=(
            "Crops chosen because the baseline content was high enough for "
            "breeding to make a difference and because they are eaten daily in "
            "populations with high deficiency prevalence. Invisible traits, so "
            "no acceptance problem and no marketing advantage either."
        ),
    ),
    Milestone(
        2014,
        "Efficacy trials show measurable improvement in nutritional status "
        "from biofortified crops",
        note=(
            "The last link in the chain demonstrated rather than assumed: "
            "improvements in vitamin A status from orange-fleshed sweet potato "
            "and in iron status from biofortified beans and millet. It is the "
            "evidence that distinguishes this record from a plausible "
            "hypothesis."
        ),
    ),
    Milestone(
        2016,
        "Zinc-biofortified wheat is released in south Asia",
        note=(
            "Wheat is the staple across a region with widespread zinc "
            "deficiency, which makes it the largest single population any "
            "biofortified variety addresses. Zinc absorption remains limited by "
            "phytate in the same grain, which is why low-phytate breeding runs "
            "alongside."
        ),
    ),
    # =========================================================================
    #  THE SETBACK, MEASURED IN DECADES
    # =========================================================================
    Milestone(
        2018,
        "Provitamin A rice receives food safety approvals in several countries "
        "that do not grow it",
        note=(
            "Approvals for food, feed and processing in countries that import "
            "rather than cultivate, which is a regulatory step rather than a "
            "deployment. Nineteen years after the first publication, no farmer "
            "was growing it."
        ),
    ),
    Milestone(
        2021,
        "The Philippines approves provitamin A rice for commercial propagation",
        note=(
            "The first approval anywhere for cultivation, in a country with "
            "high vitamin A deficiency prevalence and rice as the staple. "
            "Twenty-two years after the original publication."
        ),
    ),
    Milestone(
        2024,
        "An appellate court in the Philippines revokes the biosafety permits "
        "for provitamin A rice",
        note=(
            "The permits for the crop, and for an insect-resistant aubergine, "
            "were revoked on grounds concerning the adequacy of the safety and "
            "consultation process, and the position remained subject to further "
            "legal process. Recorded as the longest setback in this library "
            "because the sequence is now more than twenty-five years from "
            "publication to a crop that farmers are still not growing at scale, "
            "and because the obstacle at every stage since 2005 has been "
            "regulatory, legal and political rather than scientific."
        ),
    ),
    # =========================================================================
    #  THE ROUTE THAT MAY AVOID THE OBSTACLE
    # =========================================================================
    Milestone(
        2020,
        "Genome editing is applied to micronutrient traits, and falls under "
        "different regulatory treatment in several jurisdictions",
        note=(
            "Editing transporters and phytate biosynthesis produces changes "
            "that in several countries are regulated as conventional breeding "
            "rather than as transgenesis. It is the same divergence "
            "`green.agricultural_genome_editing` records, and for this record "
            "it is the most plausible route past a twenty-five year obstacle."
        ),
    ),
    Milestone(
        2022,
        "Biofortified varieties are reported to have reached tens of millions "
        "of farming households",
        note=(
            "Cumulative across crops and countries, and achieved almost "
            "entirely by the conventionally bred varieties. The comparison with "
            "the entry two above is the point of this timeline: one route "
            "produced a great deal of attention and the other produced food."
        ),
    ),
)
