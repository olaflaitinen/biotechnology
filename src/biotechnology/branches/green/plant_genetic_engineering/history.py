# =============================================================================
#  biotechnology.branches.green.plant_genetic_engineering.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks;
#  this record has two, in 1999 and 2013, and neither is a technical failure.
#  Both are failures of communication and of trust, which is the characteristic
#  failure mode of this field.
#
#  Rule 3 also applies with force: transgenic plants were achieved by at least
#  three groups independently and essentially simultaneously in 1983. Crediting
#  one would misrepresent the history.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two dates in this timeline are worth holding together. The Golden Rice
#  prototype was published in 2000. It was approved for cultivation in 2021.
#  Twenty-one years separate a working proof of concept aimed squarely at
#  childhood blindness from a regulatory permission, and almost none of that
#  interval was spent on science. That gap is the clearest single illustration
#  of the constraint named in `narrative.DESCRIPTION`.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE NATURAL GENETIC ENGINEER
    # =========================================================================
    Milestone(
        1977,
        "Agrobacterium tumefaciens is shown to transfer its own DNA into plant "
        "genomes",
        note=(
            "Crown gall disease turned out to be natural genetic engineering: "
            "the bacterium inserts genes that make the plant produce food for "
            "it. The entire field consists of borrowing that mechanism and "
            "replacing the cargo."
        ),
    ),
    # =========================================================================
    #  FIRST TRANSGENIC PLANTS: THREE GROUPS AT ONCE
    # =========================================================================
    Milestone(
        1983,
        "First transgenic plants reported by three groups independently within "
        "months of each other",
        note=(
            "Presented at the same January meeting by teams in Ghent, St Louis "
            "and Wisconsin. Simultaneous discovery, and crediting any single "
            "group would misrepresent it."
        ),
    ),
    Milestone(
        1987,
        "Bacillus thuringiensis toxin genes expressed in plants",
        note=(
            "The Bt protein had been sprayed on organic farms for decades. "
            "Moving the gene into the plant changed the delivery mechanism, not "
            "the molecule."
        ),
    ),
    # =========================================================================
    #  THE MARKET
    # =========================================================================
    Milestone(
        1994,
        "Flavr Savr tomato becomes the first genetically modified food sold",
        note=(
            "Engineered for delayed softening. It failed commercially on "
            "agronomy and shipping economics rather than on consumer "
            "resistance, and was withdrawn within three years."
        ),
    ),
    Milestone(
        1996,
        "Large-scale commercial planting of transgenic soybean and cotton "
        "begins",
        note=(
            "The traits benefited the farmer and the seed supplier. No product "
            "in this first generation offered anything a consumer could "
            "perceive, which shaped the public argument for the next thirty "
            "years."
        ),
    ),
    # =========================================================================
    #  THE FIRST SETBACK: A PAPER, A PRESS CONFERENCE, AND A COLLAPSE OF TRUST
    # =========================================================================
    Milestone(
        1999,
        "A monarch butterfly laboratory study is publicised before peer review "
        "and drives European opposition",
        note=(
            "Bt maize pollen dusted onto milkweed in a laboratory dish harmed "
            "larvae. Subsequent field studies found negligible exposure under "
            "realistic conditions. By then the image had done its work. The "
            "episode is included because it shows the field losing an argument "
            "it was scientifically winning, which is the pattern that has "
            "repeated since."
        ),
    ),
    # =========================================================================
    #  A SUCCESS WITH NO COMMERCIAL LOGIC
    # =========================================================================
    Milestone(
        1998,
        "Virus-resistant papaya rescues the Hawaiian crop from ringspot virus",
        note=(
            "Developed by a public university programme with no company behind "
            "it, for an industry that had no other remedy. Still the clearest "
            "case of the technology solving a problem nothing else could, and "
            "still one of very few public-sector products to reach farmers."
        ),
    ),
    Milestone(
        2000,
        "Golden Rice prototype published",
        note=(
            "Provitamin A biosynthesis engineered into rice endosperm, aimed at "
            "childhood blindness and mortality from vitamin A deficiency. Held "
            "up for two decades by regulatory process, patent negotiation and "
            "organised opposition."
        ),
    ),
    # =========================================================================
    #  THE SECOND SETBACK: DESTROYING THE EVIDENCE RATHER THAN CONTESTING IT
    # =========================================================================
    Milestone(
        2013,
        "A Golden Rice field trial in the Philippines is destroyed by "
        "protesters",
        note=(
            "An approved trial of a humanitarian, royalty-free, "
            "public-sector product was uprooted before it could generate data. "
            "Recorded as a setback because the destruction of a trial removes "
            "the evidence on which any judgement, favourable or unfavourable, "
            "would have to rest."
        ),
    ),
    # =========================================================================
    #  CONSOLIDATION, AND EVENTUAL APPROVAL
    # =========================================================================
    Milestone(
        2016,
        "More than a hundred Nobel laureates sign an open letter supporting "
        "genetically modified crops",
        note=(
            "Notable less for its scientific content, which was uncontroversial "
            "among plant scientists, than for what it revealed: the dispute had "
            "not been about evidence for a long time."
        ),
    ),
    Milestone(
        2021,
        "Golden Rice approved for commercial cultivation in the Philippines",
        note=(
            "Twenty-one years after the prototype. Almost none of that interval "
            "was scientific work."
        ),
    ),
)
