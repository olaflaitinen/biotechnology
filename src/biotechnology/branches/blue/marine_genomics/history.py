# =============================================================================
#  biotechnology.branches.blue.marine_genomics.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks.
#  This record's setbacks are of an unusual kind: the field's two largest
#  problems are that it produced more sequence than anyone could identify, and
#  that it collected samples for decades under a legal framework that did not
#  exist.
#
#  SUBTYPE-SPECIFIC NOTE
#  The 1985 entry is the pivot and deserves attention. Ribosomal gene sequences
#  amplified directly from seawater showed organisms that no culture collection
#  contained. Before it, marine microbiology described what would grow. After
#  it, the culturable organisms were understood to be an unrepresentative
#  minority, and the discipline had to accept that its central method had been
#  selecting its subject matter.
#
#  Two entries record organisms found by looking rather than by growing, in
#  1988 and 1990, and both turned out to be among the most abundant living
#  things on the planet. That two such organisms went unnoticed until the
#  method changed is the strongest evidence this record has for its own
#  importance.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE PROBLEM IS NAMED BEFORE IT IS SOLVED
    # =========================================================================
    Milestone(
        1932,
        "The gap between cells counted under a microscope and colonies grown "
        "on a plate is documented",
        note=(
            "Later called the great plate count anomaly. It was known for half "
            "a century that culture recovered a small minority of the cells "
            "present, and there was no method that could do anything about it, "
            "so the anomaly was recorded and worked around rather than solved."
        ),
    ),
    Milestone(
        1977,
        "Ribosomal RNA sequence comparison establishes that microbial "
        "relationships can be read from molecules",
        note=(
            "It became possible to place an organism on a tree of life from a "
            "single gene rather than from its appearance or its growth "
            "requirements. This is what later made it possible to identify an "
            "organism that had never been seen."
        ),
    ),
    Milestone(
        1977,
        "Hydrothermal vent communities are discovered",
        note=(
            "Ecosystems running on chemistry rather than sunlight, with animals "
            "wholly dependent on bacterial symbionts. Recorded here because it "
            "established that marine habitats contain biology with no "
            "terrestrial analogue, which is the scientific premise of the whole "
            "blue branch."
        ),
    ),
    # =========================================================================
    #  THE PIVOT: READING WITHOUT GROWING
    # =========================================================================
    Milestone(
        1985,
        "Ribosomal gene sequences are recovered directly from seawater, "
        "revealing organisms absent from every culture collection",
        note=(
            "The moment marine microbiology stopped being limited to what would "
            "grow. It was not an incremental improvement: the organisms found "
            "were not rare members of a known community but abundant ones that "
            "the culturing method had systematically excluded. The discipline "
            "had to accept that its central technique had been selecting its "
            "subject matter."
        ),
    ),
    # =========================================================================
    #  TWO ORGANISMS NOBODY HAD NOTICED
    # =========================================================================
    Milestone(
        1988,
        "Prochlorococcus is described and proves to be among the most abundant "
        "photosynthetic organisms on Earth",
        note=(
            "Extremely small, extremely numerous, and missed because it passed "
            "through the filters and stains that surveys had used. A primary "
            "producer at global scale, unrecorded until 1988."
        ),
    ),
    Milestone(
        1990,
        "An abundant lineage of marine archaea is found by sequence in ordinary "
        "seawater",
        note=(
            "Archaea had been regarded as inhabitants of extreme environments. "
            "They turned out to be a large fraction of the cells in the open "
            "ocean everywhere. A whole domain of life had been "
            "mischaracterised because the method that described it could not "
            "grow it."
        ),
    ),
    Milestone(
        1991,
        "A thermostable polymerase from a deep-sea hyperthermophile enters "
        "routine laboratory use",
        note=(
            "Recorded here rather than only in `blue.marine_enzymes` because it "
            "closed a loop: a marine organism supplied a reagent on which "
            "marine sequencing itself depends. Its higher fidelity than the "
            "earlier hot spring enzyme made accurate long amplification "
            "practical."
        ),
    ),
    # =========================================================================
    #  SEQUENCING EVERYTHING AT ONCE
    # =========================================================================
    Milestone(
        2004,
        "Shotgun sequencing of Sargasso Sea water produces a very large number "
        "of previously unknown genes from a single expedition",
        note=(
            "Metagenomics at ocean scale. The result was widely reported as a "
            "discovery of new species, and the more durable outcome was "
            "methodological: it established that sequencing an entire community "
            "was a practical way to survey life, and it produced a mass of "
            "sequence that nobody could assign to an organism."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: MORE SEQUENCE THAN MEANING
    # =========================================================================
    Milestone(
        2010,
        "The accumulation of unassignable marine sequence outpaces the ability "
        "to identify it",
        note=(
            "Recorded as a setback because the field's productivity became its "
            "problem. A large fraction of marine sequence matched nothing, and "
            "the honest interpretation was ambiguous: it might be genuinely "
            "novel biology or merely absent from databases that "
            "under-represent marine lineages. Sequencing more did not resolve "
            "it, since the reference gap grew alongside the data. The response "
            "was investment in reference genomes, cultivation of previously "
            "uncultured organisms, and single-cell methods rather than in more "
            "shotgun depth."
        ),
    ),
    # =========================================================================
    #  SURVEYING AT SCALE, AND DETECTING WITHOUT SEEING
    # =========================================================================
    Milestone(
        2015,
        "A global ocean sampling expedition publishes depth-resolved and "
        "systematically collected metagenomes",
        note=(
            "Standardised protocols across ocean basins and depths, released "
            "openly. Its value has been less the initial findings than the "
            "resource: re-analysis of that data is cheaper than any new "
            "expedition, which is why open deposition matters more in this "
            "field than in most."
        ),
    ),
    Milestone(
        2016,
        "Environmental DNA becomes an accepted survey method for aquatic "
        "animals",
        note=(
            "Detecting which species are present from the traces they shed, "
            "without capture or observation. It moved a genomic technique into "
            "routine ecological monitoring and into regulatory use for invasive "
            "species, and it works far better for presence than for abundance."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A LEGAL FRAMEWORK ARRIVING DECADES LATE
    # =========================================================================
    Milestone(
        2023,
        "An international agreement addresses marine genetic resources beyond "
        "national jurisdiction",
        note=(
            "Two thirds of the ocean lies outside any state's jurisdiction, and "
            "until this agreement there was no clear answer to who might "
            "sample it, publish the sequence or patent what it encodes. "
            "Decades of collection, publication and patenting happened in that "
            "gap. It is recorded here as both a milestone and a setback: the "
            "framework is a real achievement, and it arrived long after the "
            "practice it governs, which leaves historical collections and the "
            "sequences derived from them in an unresolved position."
        ),
    ),
)
