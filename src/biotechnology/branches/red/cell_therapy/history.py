# =============================================================================
#  biotechnology.branches.red.cell_therapy.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires that
#  setbacks appear; here that is the 1957 entry, in which every patient died.
#
#  SUBTYPE-SPECIFIC NOTE
#  This timeline shows something the technical description cannot: cell
#  therapy is old. Bone marrow transplantation has been routine clinical
#  practice since the 1970s, which means the safety and infrastructure
#  questions that CAR-T raises were answered once already, for a different
#  product, by the same hospital departments.
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
    #  THE TRANSPLANT ERA
    # =========================================================================
    Milestone(
        1956,
        "First successful bone marrow transplant, between identical twins",
        note=(
            "Identical twins sidestepped the rejection problem entirely, "
            "which is why it worked before anyone understood tissue matching."
        ),
    ),
    Milestone(
        1957,
        "Thomas reports six unrelated-donor marrow infusions; none survives",
        note=(
            "The setback that defined the next fifteen years of work. It "
            "established that the barrier was immunological, not technical, "
            "and sent the field to the histocompatibility problem."
        ),
    ),
    Milestone(
        1968,
        "First successful allogeneic transplant for severe combined "
        "immunodeficiency, using a matched sibling",
        note="The first cure of a genetic disease by cell transfer.",
    ),
    Milestone(
        1990,
        "Nobel Prize in Physiology or Medicine awarded for organ and cell "
        "transplantation",
    ),
    # =========================================================================
    #  THE ENGINEERING ERA
    # =========================================================================
    Milestone(
        1989,
        "Gross, Waks and Eshhar describe the first chimeric antigen receptor",
        note=(
            "A T-cell receptor with an antibody binding domain grafted on. "
            "Twenty-eight years passed between this construct and an approved "
            "product."
        ),
    ),
    Milestone(
        2002,
        "Second-generation CAR designs add a costimulatory domain",
        note=(
            "The change that made CAR-T work. First-generation constructs "
            "bound their target but the cells did not persist."
        ),
    ),
    Milestone(
        2010,
        "Durable complete remission reported in chronic lymphocytic leukaemia "
        "after CD19 CAR-T therapy",
        note=(
            "Three patients, two lasting remissions, and a result striking "
            "enough to redirect the whole field within a year."
        ),
    ),
    # =========================================================================
    #  THE PRODUCT ERA
    # =========================================================================
    Milestone(
        2017,
        "Tisagenlecleucel approved: the first CAR-T product anywhere",
        note=(
            "Also the first medicine approved on the basis of a single-arm "
            "trial in a paediatric population with no comparator, which set a "
            "regulatory precedent still being argued about."
        ),
    ),
    Milestone(
        2021,
        "First BCMA-directed CAR-T approvals for multiple myeloma",
    ),
    Milestone(
        2023,
        "Regulators begin requiring long-term follow-up for secondary "
        "malignancy after CAR-T therapy",
        note=(
            "A reminder that integrating vectors carry a lifelong monitoring "
            "obligation, exactly as in `red.gene_therapy`."
        ),
    ),
    Milestone(
        2024,
        "Allogeneic and in vivo CAR platforms enter late-stage trials",
        note=(
            "If in vivo CAR generation succeeds, the entire bespoke "
            "manufacturing problem described in practice.py disappears."
        ),
    ),
)
