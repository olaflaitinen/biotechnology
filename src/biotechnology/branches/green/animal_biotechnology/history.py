# =============================================================================
#  biotechnology.branches.green.animal_biotechnology.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks.
#  This record has two of quite different kinds, in the 1990s and in 2019, and
#  the second is a documentation failure rather than a biological one, which
#  makes it more instructive.
#
#  SUBTYPE-SPECIFIC NOTE
#  Dolly, in 1996, is the most publicly recognised event in this entire
#  taxonomy, and it is worth being precise about what it demonstrated. It was
#  not the first cloned mammal; it was the first cloned from an ADULT somatic
#  cell, which established that differentiation is reversible and that a
#  specialised cell retains the complete genome in usable form. That single
#  result underlies induced pluripotent stem cells in `red.regenerative_medicine`
#  ten years later, and its scientific descendants have mattered far more than
#  cloning itself ever did commercially.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  REPRODUCTION, LONG BEFORE GENETICS
    # =========================================================================
    Milestone(
        1780,
        "Spallanzani reports the first successful artificial insemination, in a "
        "dog",
        note=(
            "A century and a quarter before Mendel was rediscovered, and the "
            "foundation of the first of this record's three layers."
        ),
    ),
    Milestone(
        1949,
        "Glycerol is found to protect sperm through freezing",
        note=(
            "Discovered by accident when a solution was mislabelled. It made "
            "semen storable and shippable, which is what turned artificial "
            "insemination from a technique into an industry and allowed one "
            "bull to sire calves on another continent."
        ),
    ),
    Milestone(
        1951,
        "First calf born from embryo transfer",
    ),
    # =========================================================================
    #  QUANTITATIVE GENETICS MEETS THE HERD
    # =========================================================================
    Milestone(
        1936,
        "Lush formalises the breeder's equation, working on livestock",
        note=(
            "The same equation that governs `green.molecular_plant_breeding` "
            "was written for animals first."
        ),
    ),
    Milestone(
        1975,
        "Best linear unbiased prediction becomes the standard method for "
        "national genetic evaluation",
        note=(
            "Henderson's mixed model separated genetic merit from herd, year "
            "and management effects, which made it possible to compare animals "
            "that had never been in the same place."
        ),
    ),
    # =========================================================================
    #  DIRECT ALTERATION
    # =========================================================================
    Milestone(
        1985,
        "First transgenic livestock produced by pronuclear microinjection",
        note=(
            "Very low efficiency and no control over where the construct "
            "integrated. The technique worked and was not usable at scale."
        ),
    ),
    Milestone(
        1996,
        "Dolly the sheep is cloned from an adult somatic cell",
        note=(
            "Not the first cloned mammal, but the first from an adult "
            "differentiated cell, which established that differentiation is "
            "reversible and that a specialised cell keeps its complete genome "
            "in usable form. Its most important consequence was not cloning: it "
            "is the direct ancestor of induced pluripotent stem cells a decade "
            "later, and of much of `red.regenerative_medicine`."
        ),
    ),
    # =========================================================================
    #  THE FIRST SETBACK: SELECTION WORKING TOO WELL IN ONE DIRECTION
    # =========================================================================
    Milestone(
        1995,
        "Declining fertility in high-producing dairy cattle is recognised as a "
        "correlated response to decades of selection on milk yield",
        note=(
            "Conception rates fell steadily while yield rose. Nothing had gone "
            "wrong technically; the breeding goal had simply asked for one "
            "thing and got it, along with everything genetically tied to it. "
            "The remedy was to rewrite the index to include fertility, health "
            "and longevity, and it took roughly fifteen years to reverse. It is "
            "the clearest demonstration in this record that a selection index "
            "is an ethical choice rather than a measurement."
        ),
    ),
    # =========================================================================
    #  THE METHOD THAT CHANGED THE ECONOMICS
    # =========================================================================
    Milestone(
        2001,
        "Meuwissen, Hayes and Goddard propose genomic selection",
        note=(
            "Proposed for livestock, adopted there first, and only later moved "
            "into crops. `green.molecular_plant_breeding` records the same "
            "paper for that reason."
        ),
    ),
    Milestone(
        2009,
        "Genomic selection is adopted across the dairy industry",
        note=(
            "Within about three years the progeny testing system that had "
            "organised dairy breeding for half a century was largely abandoned. "
            "One of the fastest wholesale method changes in any applied "
            "biological field."
        ),
    ),
    # =========================================================================
    #  EDITING
    # =========================================================================
    Milestone(
        2016,
        "PRRS-resistant pigs produced by editing the CD163 receptor",
        note=(
            "The animals cannot be infected by a virus that kills millions of "
            "pigs a year. A welfare, economic and antimicrobial resistance "
            "argument in a single edit."
        ),
    ),
    # =========================================================================
    #  THE SECOND SETBACK: NOT BIOLOGY, DOCUMENTATION
    # =========================================================================
    Milestone(
        2019,
        "Plasmid sequences are found integrated in hornless cattle that had "
        "been reported as free of foreign DNA",
        note=(
            "A regulator reanalysing the original sequencing data found the "
            "editing plasmid had integrated at the target site. The animals "
            "were healthy and the edit worked; the characterisation had missed "
            "it. Recorded as a setback because it damaged confidence in "
            "developer-supplied molecular data at exactly the moment regulators "
            "were deciding how much to require, and it is why whole-genome "
            "characterisation of founders is now expected rather than "
            "encouraged."
        ),
    ),
    # =========================================================================
    #  REGULATORY MOVEMENT
    # =========================================================================
    Milestone(
        2020,
        "The first genome-edited food animal is approved for sale in the United "
        "States",
    ),
    Milestone(
        2025,
        "PRRS-resistant pigs receive United States approval for food use",
        note=(
            "Nine years from the first published animals to a marketing "
            "decision, which is the binding constraint named in "
            "`narrative.DESCRIPTION` made concrete."
        ),
    ),
)
