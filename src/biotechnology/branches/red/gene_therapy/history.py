# =============================================================================
#  biotechnology.branches.red.gene_therapy.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY -  the dated record.
# -----------------------------------------------------------------------------
#
#  WHY HISTORY IS A FIRST-CLASS FACET AND NOT A FOOTNOTE
#  For a reader outside the field, dates settle a question that no amount of
#  technical description settles: is this real yet? A field whose most recent
#  milestone is a 2019 laboratory demonstration and a field whose most recent
#  milestone is a 2023 regulatory approval are in completely different
#  situations, and the difference is visible at a glance from this file alone.
#
#  History also does something the rest of the record cannot: it shows the
#  failures. The 1999 and 2003 entries below are not decoration. They are the
#  reason modern gene therapy oversight looks the way it does, and a record
#  that listed only the approvals would be dishonest by omission.
#
#  EDITORIAL RULES FOR MILESTONES
#    1. Include at least one setback wherever the field has had one. A
#       timeline of unbroken triumph is a marketing document.
#    2. Prefer events that can be dated to a year without argument. Where a
#       date is disputed or gradual, choose the conventional year and say so
#       in the note.
#    3. Do not credit a discovery to a single person where it was simultaneous.
#       Several groups reached transgenic plants and CRISPR editing at nearly
#       the same time, and the record says so.
#    4. Keep events to one clause. The elaboration belongs in `note`.
#    5. Negative years are permitted for prehistoric events such as
#       domestication, and are interpreted as years before the common era.
#
#  ORDERING
#  Entries are written in chronological order for human readability, but
#  nothing depends on that: `Subtype.timeline` sorts by year, so an entry
#  inserted in the wrong place is a cosmetic problem rather than a bug.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  ORIGINS - the idea before the tools
    # =========================================================================
    Milestone(
        1972,
        "Friedmann and Roblin propose gene therapy for human genetic disease",
        note=(
            "Their paper in Science is notable less for proposing the idea "
            "than for arguing that it should not be attempted until the "
            "safety questions were answerable - a caution the field then "
            "spent thirty years learning to respect."
        ),
    ),
    # =========================================================================
    #  FIRST CLINICAL ERA - promise, then disaster
    # =========================================================================
    Milestone(
        1990,
        "First authorised human gene transfer trial, for adenosine deaminase "
        "deficiency",
        note=(
            "Two children received retrovirally corrected T cells. The result "
            "was ambiguous because enzyme replacement continued alongside, but "
            "the regulatory precedent was decisive."
        ),
    ),
    Milestone(
        1999,
        "Death of a trial participant halts the field and reshapes oversight",
        note=(
            "A fatal innate immune response to a high-dose adenoviral vector. "
            "The investigation that followed changed informed consent, adverse "
            "event reporting and conflict-of-interest rules across the whole "
            "of clinical research, not only gene therapy."
        ),
    ),
    Milestone(
        2003,
        "Leukaemias in an X-linked SCID trial reveal insertional mutagenesis",
        note=(
            "Retroviral integration near the LMO2 proto-oncogene caused "
            "leukaemia in several children who had otherwise been cured of a "
            "fatal immunodeficiency. Self-inactivating vector designs are a "
            "direct response."
        ),
    ),
    # =========================================================================
    #  RECOVERY AND APPROVAL - the tools mature
    # =========================================================================
    Milestone(
        2012,
        "Glybera becomes the first gene therapy approved in the European Union",
        note=(
            "Commercially unsuccessful and later withdrawn, treating fewer "
            "than a handful of patients, but it established the regulatory "
            "pathway that everything since has used."
        ),
    ),
    Milestone(
        2017,
        "Luxturna approved for inherited retinal dystrophy in the United States",
        note="The first in vivo adeno-associated virus therapy approved anywhere.",
    ),
    Milestone(
        2019,
        "Zolgensma approved for spinal muscular atrophy",
        note=(
            "A single systemic infusion in infants, and the first therapy to "
            "make the two-million-euro price point a mainstream policy "
            "question rather than a hypothetical one."
        ),
    ),
    # =========================================================================
    #  EDITING ERA - rewriting rather than adding
    # =========================================================================
    Milestone(
        2023,
        "First CRISPR-based therapy authorised, for sickle cell disease and "
        "beta-thalassaemia",
        note=(
            "Ex vivo editing of the BCL11A erythroid enhancer to reactivate "
            "fetal haemoglobin. Eleven years from the description of the tool "
            "to an approved medicine."
        ),
    ),
    Milestone(
        2024,
        "In vivo base editing enters registrational trials for "
        "hypercholesterolaemia",
        note=(
            "The first attempt to make a permanent, heritable-within-the-body "
            "edit in a common rather than a rare disease, which changes the "
            "risk-benefit calculation substantially."
        ),
    ),
)
