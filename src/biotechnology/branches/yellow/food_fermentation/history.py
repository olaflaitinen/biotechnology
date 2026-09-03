# =============================================================================
#  biotechnology.branches.yellow.food_fermentation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two of a kind that appear nowhere else in the library:
#  a loss of diversity caused by success, and a persistent operational problem
#  that has never been solved and is instead managed forever.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS TIMELINE IS MOSTLY PREHISTORY, AND THAT IS THE FINDING RATHER THAN A
#  GAP. The dates before 1857 are approximate, regionally uncertain and
#  attributable to no one, because the technology was developed by populations
#  over generations rather than by investigators. Rule 8 requires that
#  simultaneous discovery not be credited to a single group, and here the
#  stronger statement applies: almost nothing in the first four entries can be
#  credited to anyone at all.
#
#  A second point worth making explicitly. When Pasteur showed in 1857 that
#  fermentation is caused by living organisms, he was explaining a technology
#  that was already thousands of years old and in daily use worldwide. The
#  science did not enable the practice. It enabled doing the practice the same
#  way twice.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  PREHISTORY, ATTRIBUTABLE TO NOBODY
    # =========================================================================
    Milestone(
        -7000,
        "Fermented beverages are produced in China, evidenced by residues on "
        "pottery",
        note=(
            "Rice, honey and fruit, identified chemically from vessel residues "
            "at Jiahu. The conventional date stands for a practice that "
            "certainly developed gradually and in more than one place. It is "
            "older than writing, and probably older than settled agriculture in "
            "some regions, which makes fermentation a strong candidate for the "
            "oldest deliberate biotechnology of any kind."
        ),
    ),
    Milestone(
        -3000,
        "Bread leavening, brewing and dairy fermentation are established across "
        "the ancient world",
        note=(
            "Documented in Egyptian and Mesopotamian records. The date is "
            "conventional and the practices are older than the documents. "
            "Cheese, beer and leavened bread all predate any understanding of "
            "why they work by several thousand years."
        ),
    ),
    Milestone(
        -300,
        "Soy fermentation into sauces and pastes is established in China",
        note=(
            "The koji system, in which a filamentous fungus is cultivated to "
            "supply enzymes that then act on a substrate, is a two-stage "
            "biotechnology of considerable sophistication developed entirely "
            "empirically. It is the direct ancestor of the industrial enzyme "
            "production in `white.industrial_enzymes`."
        ),
    ),
    Milestone(
        1000,
        "Cassava fermentation processes make a toxic staple safe across west "
        "Africa",
        note=(
            "Grating, soaking and fermenting reduce cyanogenic glycosides to "
            "tolerable levels. The date is a conventional marker for a practice "
            "of uncertain antiquity. It is the clearest example of a population "
            "developing a detoxification biotechnology by observation alone, "
            "and it feeds hundreds of millions of people today."
        ),
    ),
    # =========================================================================
    #  THE SCIENCE ARRIVES AND EXPLAINS WHAT IS ALREADY HAPPENING
    # =========================================================================
    Milestone(
        1857,
        "Pasteur establishes that fermentation is caused by living "
        "microorganisms",
        note=(
            "The practice was thousands of years old and in daily use "
            "worldwide. What the finding enabled was not fermentation but "
            "control of it, and everything after this entry follows from being "
            "able to name and then choose the organism."
        ),
    ),
    Milestone(
        1881,
        "Pure culture technique makes defined starter cultures possible",
        note=(
            "Koch's methods allowed a single organism to be isolated and "
            "propagated. Within two decades commercial dairy starters existed, "
            "and the transition from a village practice to an industry runs "
            "through this entry."
        ),
    ),
    Milestone(
        1890,
        "Commercial dairy starter cultures are introduced",
        note=(
            "A dairy could now produce the same product every day rather than "
            "relying on what was in the previous batch. This is the "
            "reproducibility that `narrative.py` argues is the science's actual "
            "contribution, arriving as a product."
        ),
    ),
    # =========================================================================
    #  THE SETBACK THAT HAS NEVER BEEN SOLVED
    # =========================================================================
    Milestone(
        1935,
        "Bacteriophage is identified as the cause of failed dairy "
        "fermentations",
        note=(
            "Cheese and yoghurt production had suffered unexplained failures "
            "since starters were introduced, and the cause was a virus "
            "infecting the starter. Recorded as a setback because it has never "
            "been eliminated: phage populations build in any plant using the "
            "same strain repeatedly, and the answer is strain rotation and "
            "resistance breeding rather than a cure. Ninety years later it is "
            "still the dairy industry's chronic operational problem, managed "
            "permanently rather than fixed."
        ),
    ),
    # =========================================================================
    #  INDUSTRIALISATION
    # =========================================================================
    Milestone(
        1960,
        "Direct-vat inoculation cultures remove the need for producers to "
        "propagate their own starters",
        note=(
            "Concentrated frozen or freeze-dried cultures added straight to the "
            "vat. It improved consistency and hygiene and moved control of the "
            "organisms from thousands of producers to a small number of culture "
            "companies, which is the concentration recorded as a challenge in "
            "this record."
        ),
    ),
    Milestone(
        1988,
        "Fermentation-produced chymosin is approved for cheesemaking",
        note=(
            "Recorded in `green.veterinary_vaccines` and "
            "`white.industrial_enzymes` from other angles and belonging here "
            "too, because it is the first recombinant product accepted into a "
            "traditional fermented food. It replaced an enzyme extracted from "
            "the stomachs of slaughtered calves and attracted remarkably little "
            "opposition, which is informative about what consumers actually "
            "object to."
        ),
    ),
    # =========================================================================
    #  THE SETBACK CAUSED BY SUCCESS
    # =========================================================================
    Milestone(
        1990,
        "Industrial starter cultures displace regional fermentation "
        "communities",
        note=(
            "Defined starters gave consistency, safety and shelf life, and in "
            "doing so narrowed the microbial diversity of foods that had been "
            "regionally distinct. Several traditional products cannot be "
            "reproduced from a defined starter at all, because a succession of "
            "dozens of species over time is part of what makes them. It is "
            "recorded as a setback because the loss was a consequence of "
            "solving a real problem, and because the strains lost were also the "
            "reservoir from which future starters would have been selected."
        ),
    ),
    # =========================================================================
    #  SEEING INSIDE A COMMUNITY FERMENTATION AT LAST
    # =========================================================================
    Milestone(
        2010,
        "Sequencing reveals the microbial communities of traditional fermented "
        "foods",
        note=(
            "For most traditional products it had never been known which "
            "organisms were responsible, because the great majority could not "
            "be cultured, exactly as `blue.marine_genomics` records for "
            "seawater. Culture-independent sequencing made a craft describable "
            "without requiring it to become a defined process."
        ),
    ),
    Milestone(
        2015,
        "Fermented foods are investigated systematically for effects on the "
        "gut microbiome",
        note=(
            "A very old food category examined with a new question, connecting "
            "this record to `yellow.probiotics_and_prebiotics`. The evidence is "
            "uneven and the enthusiasm has run ahead of it, which that record "
            "addresses at length."
        ),
    ),
    Milestone(
        2020,
        "Protected designation schemes and starter culture standardisation come "
        "into tension",
        note=(
            "Rules protecting traditional names increasingly encounter "
            "producers using standardised commercial cultures, raising the "
            "question of whether a food is defined by its place, its method or "
            "its organisms. The question is unresolved and is recorded here "
            "rather than answered."
        ),
    ),
)
