# =============================================================================
#  biotechnology.branches.grey.bioaugmentation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks.
#  This record has the opposite difficulty: it is largely a sequence of
#  setbacks, and the editorial work is making sure the successes are not lost
#  in them.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE SHAPE OF THIS TIMELINE IS UNUSUAL AND IS THE POINT.
#
#  Most records here run from a discovery, through difficulty, to a working
#  practice. This one runs from an intuitive idea, through repeated failure to
#  reproduce it in the field, to an UNDERSTANDING OF WHY IT FAILS, and then to
#  a narrow, well-founded success derived from that understanding.
#
#  That is a good outcome rather than a sad one. A field that discovered the
#  boundary of its own technique and then worked inside it is in better
#  condition than one still selling across the boundary, and the entries below
#  are ordered to show that progression.
#
#  ONE ENTRY NEEDS CARE. The 1980 patent is recorded in `grey.bioremediation`
#  as well. It belongs in both: there as the origin of organism patenting, and
#  here as the first and most famous demonstration that a superior engineered
#  degrader still has to survive the site.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE PRACTICE THAT ALWAYS WORKED, BECAUSE THERE WAS NO INCUMBENT
    # =========================================================================
    Milestone(
        1920,
        "Seeding of new wastewater and digester systems with sludge from "
        "operating plants becomes routine",
        note=(
            "The oldest form of bioaugmentation and the one nobody disputes, "
            "which is instructive. A new vessel contains nothing, so the "
            "introduced community faces no competition and establishes "
            "reliably. Every legitimate case in this record shares that "
            "property, and it was visible from the beginning without being "
            "recognised as the governing principle."
        ),
    ),
    # =========================================================================
    #  THE INTUITIVE IDEA, AND THE FIRST DISAPPOINTMENT
    # =========================================================================
    Milestone(
        1975,
        "Commercial microbial products for waste treatment and spill cleanup "
        "enter the market",
        note=(
            "The proposition was straightforward: isolate a good degrader, "
            "grow it, sell it. The laboratory evidence was genuine. The step "
            "that was not examined was whether a strain that degrades well in "
            "a flask can survive in a field, and that step is where the next "
            "thirty years went."
        ),
    ),
    Milestone(
        1980,
        "A patented multi-plasmid oil-degrading bacterium is never deployed at "
        "any site",
        note=(
            "The organism was engineered to degrade several hydrocarbon "
            "fractions at once, it was the subject of the decision that "
            "established organism patenting, and it was never used. It could "
            "not compete with the indigenous communities already present. It is "
            "the earliest and clearest demonstration of this record's central "
            "finding: capability is not the constraint, survival is."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE FIELD TRIALS THAT DID NOT REPRODUCE
    # =========================================================================
    Milestone(
        1989,
        "Shoreline treatment after a major oil spill finds nutrient addition "
        "effective and added cultures not measurably so",
        note=(
            "The comparison mattered because it was made at scale, with "
            "controls, under public scrutiny. Feeding the indigenous degraders "
            "produced a measurable acceleration. Adding cultures did not add to "
            "it. The field's founding public success was a success for "
            "BIOSTIMULATION, and it was frequently reported afterwards as a "
            "success for bioaugmentation, which is a confusion this library "
            "corrects wherever it appears."
        ),
    ),
    Milestone(
        1993,
        "Systematic reviews of commercial bioaugmentation products find no "
        "consistent field advantage over biostimulation",
        note=(
            "The central setback. Assessments across many sites found that "
            "products which performed well in laboratory tests did not "
            "outperform supplying oxygen or nutrients in controlled field "
            "comparisons. The finding was unwelcome, it was reproduced, and it "
            "has not been overturned in the thirty years since. Most of the "
            "commercial market predates this result and continues after it."
        ),
    ),
    # =========================================================================
    #  UNDERSTANDING WHY, WHICH IS WHAT MADE PROGRESS POSSIBLE
    # =========================================================================
    Milestone(
        1995,
        "Microbial ecology establishes colonisation resistance as the "
        "explanation rather than product quality",
        note=(
            "Work on invasion into established communities showed that "
            "introduced populations decline for ecological reasons: "
            "competition, predation and niche occupancy, none of which is "
            "improved by selecting a better degrader. This converted a "
            "commercial disappointment into a mechanism, and a mechanism can be "
            "used to predict when the technique will work."
        ),
    ),
    # =========================================================================
    #  THE PREDICTION, AND THE CASE THAT CONFIRMED IT
    # =========================================================================
    Milestone(
        1997,
        "Dehalococcoides is identified as the only genus completing reductive "
        "dechlorination to ethene",
        note=(
            "A capability that many contaminated aquifers genuinely lack, which "
            "is precisely the condition the 1995 mechanism predicts "
            "augmentation should succeed under. Without these organisms the "
            "reaction stalls at vinyl chloride, which is more toxic than the "
            "solvent it came from, so the absence is not academic."
        ),
    ),
    Milestone(
        2002,
        "Commercial dechlorinating consortia are deployed and complete "
        "dechlorination at sites where the process had stalled",
        note=(
            "The confirmation. Sites that had been stalled for years completed "
            "to ethene after the consortium was added, and the result held up "
            "under controlled comparison. It is the field's genuine success and "
            "it succeeded for the reason the mechanism predicted, which is "
            "stronger evidence than the success alone would be."
        ),
    ),
    # =========================================================================
    #  MEASURING IT PROPERLY AT LAST
    # =========================================================================
    Milestone(
        2005,
        "Quantitative molecular tracking of introduced strains becomes "
        "standard practice",
        note=(
            "Being able to count the introduced population over time, "
            "separately from the residents, turned an argument into a "
            "measurement. It is what established the decline rates in "
            "`metrics.py`, and it also made it possible to prove when a "
            "consortium HAD established, which is what the dechlorination case "
            "needed."
        ),
    ),
    Milestone(
        2010,
        "Pre-application molecular site screening is recommended in "
        "remediation guidance",
        note=(
            "Guidance began to direct that a site be tested for the relevant "
            "organisms before augmentation is considered. This is the practical "
            "form of the whole record: measure whether the capability is "
            "absent, and augment only if it is. It arrived thirty-five years "
            "after the products did."
        ),
    ),
    # =========================================================================
    #  THE SAME LESSON, LEARNED AGAIN ELSEWHERE
    # =========================================================================
    Milestone(
        2016,
        "Gut microbiome research independently reaches the same conclusion "
        "about colonisation resistance",
        note=(
            "Studies of probiotic organisms found that most introduced strains "
            "are cleared within days and do not durably alter an established "
            "gut community, for the same ecological reasons documented here for "
            "soil. `yellow.probiotics_and_prebiotics` holds that literature and "
            "`green.biofertilisers` holds the agricultural equivalent. Three "
            "fields, separated by decades and by discipline, arriving at one "
            "result is what makes it worth stating as a general principle."
        ),
    ),
    Milestone(
        2020,
        "Engineered organism release for environmental treatment remains "
        "regulatorily foreclosed",
        note=(
            "Advances in `purple.synthetic_biology` have made it possible to "
            "construct degraders with capabilities no natural isolate has. "
            "Deliberate release requirements mean essentially none has been "
            "deployed for site remediation. The constraint here is legal and "
            "the ecological constraint would remain regardless: an engineered "
            "strain still has to survive the meadow."
        ),
    ),
)
