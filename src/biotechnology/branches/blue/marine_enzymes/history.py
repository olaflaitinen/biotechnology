# =============================================================================
#  biotechnology.branches.blue.marine_enzymes.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two: an expectation that sequence mining would deliver
#  enzymes faster than it did, and a legal dispute over a marine enzyme patent
#  that shaped how the whole branch thinks about ownership.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record's timeline contains the blue branch's single largest commercial
#  success, and it is worth being precise about it, because the story is
#  routinely told wrong.
#
#  THE POLYMERASE THAT MADE PCR PRACTICAL WAS NOT MARINE. It came from a
#  terrestrial hot spring. The marine contribution came afterwards and was a
#  different thing: a polymerase from a deep-sea vent archaeon with
#  proofreading activity, and therefore far higher fidelity, which is what made
#  accurate amplification of long sequences possible. Conflating the two
#  overstates the marine claim, and this facet separates them deliberately in
#  the 1976 and 1991 entries.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE IDEA THAT EXTREME HABITATS HOLD USEFUL ENZYMES
    # =========================================================================
    Milestone(
        1969,
        "A thermophilic bacterium from a terrestrial hot spring is described, "
        "establishing that enzymes can be sought where the conditions are",
        note=(
            "Not marine, and included because it created the heuristic the "
            "whole field runs on: if you want an enzyme that tolerates a "
            "condition, look in an organism that lives under it. Every entry "
            "below applies that heuristic to the sea."
        ),
    ),
    Milestone(
        1976,
        "A thermostable polymerase is purified from that hot spring organism",
        note=(
            "The enzyme that later made PCR practical, and it is terrestrial. "
            "It is recorded here because this record's own polymerase entry is "
            "frequently confused with it, and the marine claim should be stated "
            "accurately rather than generously."
        ),
    ),
    Milestone(
        1977,
        "Hydrothermal vents are discovered, revealing organisms living above "
        "one hundred degrees Celsius under pressure",
        note=(
            "The habitat that supplies this record's thermostable enzymes. It "
            "also extended the known limits of life, which changed expectations "
            "about where enzymes might be found at all."
        ),
    ),
    # =========================================================================
    #  THE OTHER EXTREME
    # =========================================================================
    Milestone(
        1984,
        "Psychrophilic enzymes are systematically characterised and their "
        "activity and stability trade is described",
        note=(
            "Cold-adapted enzymes were shown to be structurally distinct rather "
            "than simply slow, with greater flexibility, lower activation "
            "energy and much reduced stability. The trade was framed as a cost. "
            "Industry later inverted that reading, since instability is exactly "
            "what makes an enzyme switchable off."
        ),
    ),
    # =========================================================================
    #  THE BRANCH'S LARGEST COMMERCIAL SUCCESS
    # =========================================================================
    Milestone(
        1991,
        "A high-fidelity proofreading polymerase from a deep-sea "
        "hyperthermophilic archaeon enters routine use",
        note=(
            "Genuinely marine, and a different capability from the 1976 "
            "enzyme: proofreading activity gave far lower error rates, which "
            "made accurate amplification of long sequences practical. It is the "
            "blue branch's most widely used product by a large margin, present "
            "in laboratories that have no connection to marine science, and it "
            "supplies the sequencing on which `blue.marine_genomics` depends."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: WHO OWNS AN ENZYME FROM A NATIONAL PARK
    # =========================================================================
    Milestone(
        1997,
        "Disputes over commercial benefit from enzymes collected in protected "
        "areas force the question of who owns an extremophile",
        note=(
            "Enzymes worth a great deal commercially had been collected under "
            "arrangements that returned nothing to the jurisdictions holding "
            "the habitats. The disputes were partly terrestrial and their "
            "consequence was general: they made access and benefit sharing a "
            "practical commercial question rather than a diplomatic one, and "
            "they shaped how marine sampling has been negotiated ever since. "
            "Recorded as a setback because the field's most valuable products "
            "predate any framework for sharing what they earned."
        ),
    ),
    # =========================================================================
    #  READING ENZYMES OUT OF WATER
    # =========================================================================
    Milestone(
        2000,
        "Functional metagenomic screening recovers enzymes from organisms that "
        "have never been cultured",
        note=(
            "Environmental DNA expressed in a laboratory host and screened for "
            "activity, which found enzymes without needing to grow, or even to "
            "identify, whatever made them. It removed the culturability barrier "
            "that had confined this field to the small fraction of marine "
            "organisms that will grow."
        ),
    ),
    Milestone(
        2005,
        "Cold-active enzymes reach commercial molecular biology products",
        note=(
            "Heat-labile phosphatases and nucleases sold specifically because "
            "they can be destroyed by gentle warming. The commercial argument "
            "was explicitly the removal of a purification step rather than "
            "catalytic performance, which is the inversion this record is built "
            "on arriving in a catalogue."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: CANDIDATES WITHOUT PROTEINS
    # =========================================================================
    Milestone(
        2012,
        "Sequence mining produces candidate enzymes faster than they can be "
        "expressed and characterised",
        note=(
            "Marine metagenomes yielded very large numbers of predicted enzyme "
            "genes, and the expectation was that discovery had been solved. It "
            "had not. Proteins evolved for cold and pressure frequently express "
            "as insoluble aggregate in mesophilic hosts, and characterisation "
            "remained slow and manual. The bottleneck moved from finding to "
            "obtaining a working protein, which is where it remains."
        ),
    ),
    # =========================================================================
    #  COMPETITION FROM THE LABORATORY
    # =========================================================================
    Milestone(
        2018,
        "Directed evolution of mesophilic enzymes towards cold activity "
        "becomes a practical alternative to marine discovery",
        note=(
            "A well-characterised terrestrial enzyme evolved in the laboratory "
            "can reach a cold-active phenotype without any of this record's "
            "sampling, legal or expression difficulties. It is recorded because "
            "it constrains the field honestly: marine discovery now competes "
            "with engineering, and it wins where the natural solution is "
            "structurally unlike anything a mesophilic starting point would "
            "reach."
        ),
    ),
    Milestone(
        2023,
        "The agreement on marine biological diversity beyond national "
        "jurisdiction brings high seas sequences within a framework",
        note=(
            "Directly relevant here, because in this record the product IS the "
            "sequence: once a gene is known it can be expressed anywhere, with "
            "no further reference to the organism or the water it came from. "
            "That is exactly the case the agreement's digital sequence "
            "information provisions had to address."
        ),
    ),
)
