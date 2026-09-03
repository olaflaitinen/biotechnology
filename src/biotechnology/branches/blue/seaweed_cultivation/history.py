# =============================================================================
#  biotechnology.branches.blue.seaweed_cultivation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two disease events that between them explain why the
#  sector's principal risk is biological rather than technical.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE 1949 ENTRY IS THE ONE THAT MATTERS AND IT IS ALMOST UNKNOWN OUTSIDE THE
#  FIELD. Nori had been farmed for centuries by putting bundles of sticks in
#  the water and hoping. Nobody knew where the spores came from, so harvests
#  varied unpredictably and a bad year could not be explained or prevented.
#
#  Kathleen Drew-Baker, working in Manchester on a species from the Welsh
#  coast, showed that a small filamentous organism previously classified as a
#  separate genus was in fact a stage in the life cycle of the same seaweed.
#  That single result made hatchery seeding possible and converted nori farming
#  from a gamble into an industry. She never visited Japan; there is a memorial
#  to her there.
#
#  It is recorded at length because it is the clearest case in this library of
#  a purely taxonomic observation, made far from any application, transforming
#  a major food industry.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  CENTURIES OF FARMING WITHOUT UNDERSTANDING
    # =========================================================================
    Milestone(
        1670,
        "Nori cultivation using bundled sticks and nets is established in Japan",
        note=(
            "Farmed by placing material in the water where spores were known "
            "to settle, without any understanding of where the spores came "
            "from. Harvests varied enormously between years and a failure could "
            "not be explained. The practice is centuries older than the science "
            "that eventually made it reliable."
        ),
    ),
    Milestone(
        1658,
        "Agar is discovered in Japan and enters use as a food gelling agent",
        note=(
            "Recorded because of what it later became. The property that makes "
            "agar valuable to a cook is the one that made it indispensable to "
            "microbiology two centuries later."
        ),
    ),
    Milestone(
        1881,
        "Agar is adopted as a solid culture medium for microbiology",
        note=(
            "Suggested to Koch's laboratory by Angelina Hesse, who knew it from "
            "domestic use, after gelatin proved unsatisfactory because it melts "
            "at incubation temperature and many bacteria digest it. Pure "
            "culture technique, and therefore most of microbiology, rests on a "
            "seaweed extract."
        ),
    ),
    # =========================================================================
    #  THE OBSERVATION THAT MADE AN INDUSTRY
    # =========================================================================
    Milestone(
        1949,
        "The conchocelis stage is shown to be part of the nori life cycle",
        note=(
            "Kathleen Drew-Baker demonstrated that a filamentous organism "
            "boring into shells, classified as a separate genus, was a phase in "
            "the life cycle of the seaweed farmed for nori. Once the source of "
            "the spores was known it could be cultured in a hatchery and seeded "
            "onto nets deliberately. Yields became predictable and the industry "
            "was transformed. The work was taxonomic, done in Manchester on a "
            "Welsh species, with no application in view."
        ),
    ),
    # =========================================================================
    #  THE SECTOR BECOMES INDUSTRIAL
    # =========================================================================
    Milestone(
        1950,
        "Hatchery seeding of nori nets becomes standard practice",
        note=(
            "The direct consequence of the previous entry. It is the origin of "
            "the seed string technology that `practice.TECHNOLOGIES` records, "
            "and it is why nori is the most intensively developed cultivation "
            "in the sector."
        ),
    ),
    Milestone(
        1970,
        "Large-scale kelp cultivation expands rapidly in China",
        note=(
            "Long-line cultivation, cold-tolerant selected strains and "
            "systematic site development made kelp the largest single tonnage "
            "in world aquaculture by weight. It is the reason any accurate "
            "description of this sector has to be written from an Asian rather "
            "than a European vantage point."
        ),
    ),
    Milestone(
        1971,
        "Commercial cultivation of tropical carrageenan seaweeds begins in the "
        "Philippines",
        note=(
            "Vegetative propagation from cuttings on simple off-bottom lines, "
            "requiring almost no capital and a great deal of labour. It created "
            "livelihoods for very large numbers of coastal households and, by "
            "propagating clonally from a narrow founding stock, created the "
            "genetic vulnerability recorded in the setbacks below."
        ),
    ),
    # =========================================================================
    #  THE SETBACKS: WHAT CLONAL MONOCULTURE COSTS
    # =========================================================================
    Milestone(
        2011,
        "Ice-ice disease and epiphyte outbreaks devastate tropical carrageenan "
        "production",
        note=(
            "Production in affected regions fell sharply and in places "
            "collapsed. The crop had been propagated vegetatively for decades "
            "from a narrow base, so a whole growing region was effectively one "
            "genotype and an outbreak met no resistance anywhere. Recovery "
            "required new planting material rather than better husbandry, and "
            "the underlying vulnerability was not removed."
        ),
    ),
    Milestone(
        2013,
        "Repeated disease and warming events establish that the sector's "
        "principal risk is biological",
        note=(
            "Successive outbreaks and marine heatwaves made clear that the "
            "limits on this industry are pathogens, genetics and temperature "
            "rather than cultivation technique or market demand. It redirected "
            "research towards breeding, gametophyte banking and disease "
            "resistance, which had been neglected because the farming itself "
            "was easy."
        ),
    ),
    # =========================================================================
    #  NEW CLAIMS, NEW SCRUTINY
    # =========================================================================
    Milestone(
        2016,
        "Integrated multi-trophic aquaculture is demonstrated at commercial "
        "scale",
        note=(
            "Seaweed grown beside fed fish takes up dissolved nitrogen and "
            "phosphorus, converting a waste stream into a crop. It is the "
            "clearest case where seaweed's nutrient uptake is worth paying for "
            "in its own right rather than being an incidental benefit."
        ),
    ),
    Milestone(
        2020,
        "Red seaweed supplementation is reported to reduce enteric methane in "
        "ruminants",
        note=(
            "Substantial reductions were reported in feeding trials, and the "
            "constraints appeared immediately: cultivating the species at the "
            "required scale, consistency of the active compound between "
            "batches, its stability, and questions about long-term animal and "
            "food safety. It is recorded as a promising result with its "
            "limitations attached rather than as an achievement."
        ),
    ),
    Milestone(
        2021,
        "Seaweed carbon sequestration claims come under sustained scientific "
        "scrutiny",
        note=(
            "Cultivation was widely proposed as a climate measure. Analysis "
            "established the distinction this record insists on: carbon fixed "
            "in a crop that is eaten, fed or extracted returns to the "
            "atmosphere within months, and durable sequestration requires a "
            "mechanism for keeping it out of circulation. The scrutiny "
            "strengthened the sector's defensible claims by separating them "
            "from the indefensible one."
        ),
    ),
)
