# =============================================================================
#  biotechnology.branches.blue.marine_biofouling_control.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks.
#  The tributyltin sequence between 1960 and 2008 is the largest setback in the
#  blue branch and one of the clearest in the library, and it is recorded as
#  four entries rather than one because the interval between them is the point.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE TIMELINE OF THE TRIBUTYLTIN CASE IS THE LESSON.
#
#      1960s   introduced, and outstandingly effective
#      1970s   oyster farms near marinas report shell deformation and
#              recruitment failure
#      1981    imposex is described: female molluscs developing male
#              characteristics, at concentrations of nanograms per litre
#      1982    first national restrictions, on small vessels only
#      2008    global prohibition takes effect
#
#  Roughly three decades separate the first substantial evidence of harm from
#  the global ban, and about a quarter of a century separates the mechanism
#  being described from the prohibition. The effect concentration was orders of
#  magnitude below anything the original assessment had considered worth
#  testing.
#
#  Two conclusions belong in the data rather than in commentary. A technology
#  can be excellent at its purpose and unacceptable in its consequences, and
#  the two judgements are independent. And an assessment that tests only at
#  concentrations expected to matter will not detect an effect that occurs
#  below them.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE PROBLEM IS AS OLD AS SHIPPING
    # =========================================================================
    Milestone(
        -700,
        "Lead sheathing and pitch are used to protect wooden hulls",
        note=(
            "Fouling and shipworm have been attacked with whatever was toxic or "
            "impermeable for as long as vessels have gone to sea. The problem "
            "is not modern and neither is the instinct to solve it with poison."
        ),
    ),
    Milestone(
        1761,
        "Copper sheathing is adopted for naval hulls",
        note=(
            "Highly effective, and it introduced the galvanic corrosion problem "
            "of copper against iron fastenings, which took decades to solve. "
            "Copper remains the principal antifouling biocide two and a half "
            "centuries later, which is an unusual continuity."
        ),
    ),
    # =========================================================================
    #  THE SETBACK, IN FOUR PARTS
    # =========================================================================
    Milestone(
        1960,
        "Tributyltin antifouling coatings are introduced",
        note=(
            "Outstandingly effective across the full range of fouling "
            "organisms, and combined with self-polishing copolymer chemistry it "
            "gave controlled release over a multi-year drydocking interval. By "
            "any measure of its stated purpose it was the best antifouling "
            "technology ever deployed."
        ),
    ),
    Milestone(
        1970,
        "Oyster farms near marinas report shell deformation and recruitment "
        "failure",
        note=(
            "Commercial oyster production in affected areas suffered severely, "
            "and the cause was not immediately identified. The first "
            "substantial evidence of harm arrives here, roughly four decades "
            "before the global prohibition."
        ),
    ),
    Milestone(
        1981,
        "Imposex is described in marine molluscs and attributed to tributyltin",
        note=(
            "Female molluscs developing male characteristics and becoming "
            "unable to reproduce, at water concentrations in the nanograms per "
            "litre. The effect occurred orders of magnitude below anything the "
            "original assessment had thought worth testing, which is the "
            "methodological lesson: an assessment that tests only where an "
            "effect is expected will not find one that occurs below."
        ),
    ),
    Milestone(
        2008,
        "The international convention prohibiting harmful antifouling systems "
        "takes effect globally",
        note=(
            "Restrictions began on small vessels in the early 1980s and the "
            "global ban took effect in 2008, roughly three decades after the "
            "first strong evidence of harm and about twenty-five years after "
            "the mechanism was described. Populations in affected areas have "
            "recovered in many places, which is the encouraging half. The "
            "interval is the discouraging half, and it is recorded here rather "
            "than smoothed over."
        ),
    ),
    # =========================================================================
    #  THE ALTERNATIVE THAT DOES NOT KILL ANYTHING
    # =========================================================================
    Milestone(
        1977,
        "Silicone foul-release coatings are developed",
        note=(
            "A different mechanism entirely: very low surface energy so that "
            "organisms attach weakly and are removed by the vessel's own "
            "motion. Nothing is killed and nothing is released. It was "
            "commercially marginal while tributyltin remained available and "
            "became the principal alternative once it did not, which is a "
            "reminder that regulation redirects development as much as it "
            "restricts it."
        ),
    ),
    Milestone(
        1998,
        "Shark skin microtopography is shown to deter settlement",
        note=(
            "Surface texture at the scale of the settling larva, deterring "
            "attachment mechanically rather than chemically. It performs well "
            "in the laboratory and has proved difficult to maintain on a hull "
            "for the years a coating must last, which is where much of this "
            "field's laboratory promise has gone."
        ),
    ),
    # =========================================================================
    #  ATTACKING THE FIRST STAGE INSTEAD OF THE VISIBLE ONE
    # =========================================================================
    Milestone(
        1996,
        "Furanones from a marine alga are shown to interfere with bacterial "
        "quorum sensing",
        note=(
            "A red alga that stays notably clean was found to produce compounds "
            "that disrupt the signalling bacteria use to coordinate biofilm "
            "formation. It opened a strategy of preventing the first stage of "
            "the fouling sequence rather than killing the settled organism, and "
            "it is the clearest link between this record and "
            "`blue.marine_natural_products`."
        ),
    ),
    Milestone(
        2011,
        "Guidelines for controlling ship biofouling to limit invasive species "
        "transfer are adopted",
        note=(
            "A second objective for the same technology, and not an identical "
            "one. Fuel efficiency is served by a smooth open hull; biosecurity "
            "depends on niche areas such as sea chests and thrusters, which "
            "foul heavily and are rarely inspected. The two objectives usually "
            "align and do not always."
        ),
    ),
    # =========================================================================
    #  THE SUCCESSOR COMES UNDER THE SAME PRESSURE
    # =========================================================================
    Milestone(
        2013,
        "Copper-based coatings come under regulatory restriction in enclosed "
        "waters",
        note=(
            "Copper accumulates in the sediment of marinas and harbours where "
            "water exchange is poor, and is toxic to non-target organisms. "
            "Restrictions and local bans followed. The pattern of the "
            "tributyltin case is repeating in a weaker form, which is why "
            "`practice.CHALLENGES` records that an effective biocide should be "
            "assumed to have a regulatory lifetime."
        ),
    ),
    Milestone(
        2019,
        "Proactive hull grooming and in-water cleaning with capture become "
        "established practice",
        note=(
            "Cleaning lightly and often so that fouling never establishes, "
            "which needs no biocide at all. It introduced its own regulated "
            "problem: cleaning releases both the accumulated organisms and the "
            "coating's biocide into the harbour, so capture of the removed "
            "material became a condition rather than a refinement."
        ),
    ),
)
