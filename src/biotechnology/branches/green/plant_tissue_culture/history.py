# =============================================================================
#  biotechnology.branches.green.plant_tissue_culture.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks;
#  this record has a large one, in the 1980s oil palm entry, where an
#  epigenetic abnormality invisible to every available test cost the industry
#  years of production from millions of trees.
#
#  SUBTYPE-SPECIFIC NOTE
#  The gap between the first two entries is the striking thing. Haberlandt
#  proposed totipotency in 1902 and could not demonstrate it, because nobody
#  yet knew that plant hormones existed. Thirty-seven years passed before
#  anyone could keep plant cells dividing, and another eighteen before Skoog
#  and Miller worked out that the hormone RATIO rather than the amount decides
#  what the tissue becomes.
#
#  Everything after 1957 is engineering. Everything before it was waiting for
#  one relationship to be found.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE IDEA, LONG BEFORE THE MEANS
    # =========================================================================
    Milestone(
        1902,
        "Haberlandt proposes that any living plant cell can regenerate a whole "
        "organism",
        note=(
            "He tried it and failed. He chose mature differentiated cells and "
            "had no plant hormones, neither of which had been discovered. The "
            "idea was right and unreachable for half a century."
        ),
    ),
    Milestone(
        1934,
        "Auxin identified as a plant growth substance",
    ),
    Milestone(
        1939,
        "First indefinitely growing plant callus cultures established",
        note=(
            "Achieved independently by Gautheret, Nobecourt and White within "
            "months of each other in France and the United States. Continuous "
            "growth was possible; controlling what the tissue became was not."
        ),
    ),
    # =========================================================================
    #  THE RELATIONSHIP THAT MADE IT A TECHNIQUE
    # =========================================================================
    Milestone(
        1957,
        "Skoog and Miller describe hormonal control of organogenesis",
        note=(
            "A high cytokinin to auxin ratio gives shoots, the reverse gives "
            "roots, an intermediate ratio gives callus. The single most useful "
            "relationship in the field, and the moment tissue culture stopped "
            "being an observation and became a method."
        ),
    ),
    Milestone(
        1958,
        "Somatic embryogenesis demonstrated in carrot cell suspensions",
        note=(
            "Complete embryos from single cultured cells. Haberlandt's 1902 "
            "hypothesis, confirmed fifty-six years later."
        ),
    ),
    Milestone(
        1960,
        "Morel demonstrates meristem culture for virus elimination and clonal "
        "orchid propagation",
        note=(
            "Two industries created by one observation: that the growing tip "
            "outruns the virus moving up the plant."
        ),
    ),
    Milestone(
        1962,
        "Murashige and Skoog publish their medium formulation",
        note=(
            "Still the default basal medium worldwide more than sixty years "
            "later. Among the most cited papers in the plant sciences, and it "
            "is a table of salt concentrations."
        ),
    ),
    # =========================================================================
    #  INDUSTRY
    # =========================================================================
    Milestone(
        1974,
        "Commercial orchid and ornamental micropropagation industry forms",
    ),
    Milestone(
        1983,
        "Tissue culture regeneration becomes the enabling step for the first "
        "transgenic plants",
        note=(
            "The three groups that produced transgenic plants that year all "
            "depended on regeneration protocols developed for entirely "
            "different reasons a decade earlier."
        ),
    ),
    # =========================================================================
    #  THE SETBACK
    # =========================================================================
    Milestone(
        1986,
        "Oil palm clones planted at scale develop the mantled-fruit "
        "abnormality",
        note=(
            "Millions of trees propagated by somatic embryogenesis produced "
            "deformed, largely sterile fruit that appeared only after several "
            "years of growth. The cause was epigenetic, a methylation change "
            "invisible to every genetic test available, and no amount of "
            "sequence checking would have caught it. It remains the field's "
            "clearest warning that a clone which looks identical may not be, "
            "and it is why `metrics.py` now includes methylation assays under "
            "genetic fidelity."
        ),
    ),
    # =========================================================================
    #  CONSERVATION AND SCALE
    # =========================================================================
    Milestone(
        1985,
        "Cryopreservation of plant meristems demonstrated",
        note=(
            "Made long-term conservation possible for crops whose seed cannot "
            "be dried and frozen, including banana, potato and cassava."
        ),
    ),
    Milestone(
        2000,
        "Temporary immersion bioreactors reach commercial banana production",
        note=(
            "Attacked the labour cost that dominates the economics, by "
            "replacing hand division with periodic flooding of a vessel."
        ),
    ),
    Milestone(
        2016,
        "Developmental regulators are shown to make recalcitrant maize "
        "genotypes regenerable",
        note=(
            "Baby Boom and Wuschel transcription factors turned varieties that "
            "had resisted transformation for decades into workable ones. The "
            "first substantial progress on the constraint that limits two other "
            "records in this branch."
        ),
    ),
)
