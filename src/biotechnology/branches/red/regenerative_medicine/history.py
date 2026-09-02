# =============================================================================
#  biotechnology.branches.red.regenerative_medicine.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires that
#  setbacks appear. This field has had two of a kind that are rare in the rest
#  of the taxonomy: a research fraud that retracted a clinical claim, and a
#  commercial sector that harms patients while the legitimate field looks on.
#  Both are recorded, in 2014 and 2017.
#
#  SUBTYPE-SPECIFIC NOTE
#  The shape of this timeline is worth noticing. Thin tissues reached patients
#  in the early 1980s and have stayed there. Every subsequent entry is either
#  an enabling technique, a model system, or a failure. Four decades of work
#  have produced extraordinary tools and have not moved the thickness limit,
#  which is exactly what a physical constraint rather than a biological one
#  looks like from the outside.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE ENABLING CULTURE TECHNIQUE
    # =========================================================================
    Milestone(
        1975,
        "Rheinwald and Green establish serial cultivation of human "
        "keratinocytes",
        note=(
            "The first practical way to expand a small skin biopsy into enough "
            "tissue to cover a person. Everything clinical in this record "
            "descends from it."
        ),
    ),
    # =========================================================================
    #  THE FIRST PATIENTS
    # =========================================================================
    Milestone(
        1981,
        "First cultured epidermal autografts used on burn patients",
        note=(
            "Two children with burns over most of their body surface. The "
            "technique worked because skin is thin enough to survive on "
            "diffusion, which is the whole reason it came first."
        ),
    ),
    Milestone(
        1987,
        "The term tissue engineering is formalised at a National Science "
        "Foundation workshop",
    ),
    # =========================================================================
    #  THE FIELD ACQUIRES ITS FRAMEWORK
    # =========================================================================
    Milestone(
        1993,
        "Langer and Vacanti publish the cells, scaffolds and signals framework",
        note=(
            "The three-component idea that the field has used ever since, and "
            "that `narrative.DESCRIPTION` is still organised around."
        ),
    ),
    Milestone(
        1997,
        "A cartilage construct grown in the shape of a human ear on a mouse is "
        "widely publicised",
        note=(
            "Scientifically modest and reported everywhere. It shaped public "
            "expectation of the field for a generation, and arguably set that "
            "expectation two decades ahead of what was achievable."
        ),
    ),
    # =========================================================================
    #  NEW CELL SOURCES
    # =========================================================================
    Milestone(
        1998,
        "Human embryonic stem cell lines derived",
        note=(
            "Solved the cell supply problem and created an ethical dispute "
            "that dominated the field's public discussion for a decade."
        ),
    ),
    Milestone(
        2006,
        "Yamanaka reprograms adult cells to pluripotency",
        note=(
            "Four transcription factors turned an ordinary skin cell into a "
            "pluripotent one. It largely dissolved the embryonic stem cell "
            "dispute by making it unnecessary, and it made patient-specific "
            "cells possible."
        ),
    ),
    # =========================================================================
    #  ORGANOIDS: THE FIELD FINDS A USE THAT DOES NOT NEED VESSELS
    # =========================================================================
    Milestone(
        2009,
        "Intestinal organoids grown from single stem cells",
        note=(
            "Self-organising miniature tissue, no scaffold required. Organoids "
            "sidestep the diffusion limit by staying small, and have become the "
            "field's most widely used product even though nothing is implanted."
        ),
    ),
    # =========================================================================
    #  THE SETBACKS
    # =========================================================================
    Milestone(
        2014,
        "Stimulus-triggered acquisition of pluripotency papers retracted",
        note=(
            "Claimed that ordinary cells could be reprogrammed by acid stress. "
            "The results could not be replicated anywhere, the papers were "
            "retracted, and one investigator died by suicide. It is included "
            "because a field under pressure to deliver produced a fraud, and "
            "omitting that from the record would be dishonest."
        ),
    ),
    Milestone(
        2017,
        "Patients permanently blinded by unregulated intraocular stem cell "
        "injections",
        note=(
            "Marketed as stem cell therapy for macular degeneration at a "
            "commercial clinic. Three women lost their sight. The episode is "
            "the clearest instance of the gap between what this field can do "
            "and what is sold in its name, and it is why "
            "`practice.CHALLENGES` lists unproven clinics as a challenge to the "
            "field rather than as someone else's problem."
        ),
    ),
    # =========================================================================
    #  ATTACKING THE LIMIT DIRECTLY
    # =========================================================================
    Milestone(
        2015,
        "Bioprinted vascular channels perfused in vitro",
        note=(
            "Sacrificial ink printed into a construct and flushed out, leaving "
            "plumbing. A direct attack on the diffusion limit, and still short "
            "of the capillary scale where gas exchange actually happens."
        ),
    ),
    Milestone(
        2021,
        "Organ-on-a-chip data accepted in some regulatory submissions",
        note=(
            "Human tissue models used in place of animal data. The field's "
            "largest realised impact so far has been on how drugs are tested "
            "rather than on how tissue is replaced, which is not what anyone "
            "predicted in 1993."
        ),
    ),
)
