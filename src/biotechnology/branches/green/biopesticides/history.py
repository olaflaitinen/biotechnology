# =============================================================================
#  biotechnology.branches.green.biopesticides.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks;
#  this record carries two. The 1962 entry is a setback for the technology this
#  field replaces rather than for the field itself, and it belongs here because
#  it is the reason the field has a market at all. The 2010s Bt resistance
#  entry is the field's own.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two dates in this timeline deserve to be read together. Ishiwata isolated
#  the bacterium behind Bacillus thuringiensis in 1901 while investigating a
#  disease killing silkworms, meaning the organism was first noticed as a pest
#  rather than as a tool. The first commercial product appeared in 1938.
#  Thirty-seven years from observation to product, and the same organism is
#  still the largest biopesticide in the world nearly a century later.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE AGENT, FIRST NOTICED AS A PROBLEM
    # =========================================================================
    Milestone(
        1901,
        "Ishiwata isolates the bacterium later named Bacillus thuringiensis "
        "from diseased silkworms",
        note=(
            "Found while investigating an epidemic destroying a silk industry. "
            "The organism was a pest before it was a tool, and it was named a "
            "decade later after being rediscovered in flour moths in "
            "Thuringia."
        ),
    ),
    Milestone(
        1888,
        "Vedalia beetle introduced to California controls cottony cushion scale",
        note=(
            "Classical biological control before the term existed: an imported "
            "predator eliminated an invasive pest that had threatened the "
            "entire citrus industry, within two years and permanently. Still "
            "cited as the most cost-effective pest control intervention ever "
            "undertaken."
        ),
    ),
    # =========================================================================
    #  THE FIRST PRODUCTS
    # =========================================================================
    Milestone(
        1938,
        "The first commercial Bacillus thuringiensis product is sold in France",
        note=(
            "Sporeine. Thirty-seven years after the organism was isolated, and "
            "still, in modern form, the largest biopesticide in the world."
        ),
    ),
    # =========================================================================
    #  THE SETBACK THAT CREATED THE MARKET
    # =========================================================================
    Milestone(
        1962,
        "Silent Spring documents the ecological consequences of broad-spectrum "
        "organochlorine insecticides",
        note=(
            "A setback for the chemistry this record offers an alternative to, "
            "and the reason the alternative has a market. It also created the "
            "modern pesticide regulatory system, which then applied its data "
            "requirements to biological agents as well, an outcome nobody "
            "intended and which `governance.py` describes."
        ),
    ),
    # =========================================================================
    #  THE FRAMEWORK
    # =========================================================================
    Milestone(
        1959,
        "The integrated control concept is formalised in California",
        note=(
            "Chemical and biological control as complements rather than "
            "alternatives, keyed to an economic threshold. It later became "
            "integrated pest management and is the framework every entry below "
            "operates inside."
        ),
    ),
    Milestone(
        1967,
        "Sterile insect technique eradicates screwworm from the southern United "
        "States",
        note=(
            "Mass-reared males sterilised by irradiation and released to "
            "outnumber wild ones. Eradication of a major livestock pest from a "
            "continent, achieved by releasing more insects."
        ),
    ),
    # =========================================================================
    #  BEHAVIOUR RATHER THAN MORTALITY
    # =========================================================================
    Milestone(
        1970,
        "Pheromone mating disruption demonstrated in orchards",
        note=(
            "Nothing is killed. The air is saturated with the female signal and "
            "males cannot locate a mate. Fifty years later it still works "
            "against codling moth, which is a resistance record no insecticide "
            "of any kind can match."
        ),
    ),
    Milestone(
        1970,
        "Commercial augmentative release of predatory mites begins in European "
        "glasshouses",
        note=(
            "Now the standard system rather than an alternative one: a "
            "glasshouse tomato crop in northern Europe is routinely grown with "
            "almost no insecticide."
        ),
    ),
    # =========================================================================
    #  UNDERSTANDING WHY IT IS SELECTIVE
    # =========================================================================
    Milestone(
        1981,
        "The Bt cry gene is cloned and the mechanism of gut-specific activation "
        "is established",
        note=(
            "Explained why a protein lethal to caterpillars is harmless to "
            "vertebrates: it requires an alkaline midgut and specific receptors "
            "to become active. The same understanding made "
            "`green.plant_genetic_engineering` possible six years later."
        ),
    ),
    Milestone(
        1995,
        "Baculovirus products registered for major lepidopteran pests",
        note=(
            "Often specific to a single host species, which is the extreme end "
            "of the selectivity trade-off: ecologically ideal, commercially "
            "very difficult."
        ),
    ),
    # =========================================================================
    #  THE FIELD'S OWN SETBACK
    # =========================================================================
    Milestone(
        2013,
        "Field-evolved resistance to Bt proteins confirmed in several pest "
        "populations",
        note=(
            "Documented where the same proteins were deployed intensively as "
            "both sprays and transgenic crops across the same landscape, and "
            "where refuge requirements were not enforced. Being biological "
            "confers no exemption from evolution, and the episode is why "
            "resistance management is now a licence condition rather than "
            "advice."
        ),
    ),
    # =========================================================================
    #  SEQUENCE-BASED SELECTIVITY, AND A REGULATORY REFORM
    # =========================================================================
    Milestone(
        2017,
        "The first RNA interference based pesticide is approved in the United "
        "States",
        note=(
            "Specificity determined by a DNA sequence rather than by a "
            "biochemical property, which allows a product targeting one beetle "
            "species and nothing else, including its close relatives."
        ),
    ),
    Milestone(
        2022,
        "The European Union adopts data requirements written specifically for "
        "micro-organisms",
        note=(
            "Regulation (EU) 2022/1439 replaced requirements designed for "
            "synthetic molecules. Sixty years after the regulatory system that "
            "created the mismatch, and the most consequential change to this "
            "field's economics in decades."
        ),
    ),
)
