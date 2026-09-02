# =============================================================================
#  biotechnology.branches.red.antibody_engineering.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires that
#  setbacks appear; here that is the 2006 TGN1412 trial, in which six healthy
#  volunteers suffered multi-organ failure within hours of the first human dose.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two entries in this timeline are there for reasons beyond the science.
#
#  The 1975 hybridoma paper was deliberately not patented. Kohler and Milstein
#  published without seeking protection, and the technique became freely
#  available worldwide. Whether that was admirable or negligent was argued
#  about for decades; what is not arguable is that it shaped how fast the field
#  moved.
#
#  The 1993 camelid discovery came from a student project examining camel blood
#  that had been sitting in a freezer. Heavy-chain-only antibodies had been
#  overlooked because nobody had reason to look, and they became the basis of
#  an entire format class.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  BEFORE MONOCLONALS: SERUM THERAPY
    # =========================================================================
    Milestone(
        1890,
        "Behring and Kitasato demonstrate serum therapy against diphtheria",
        note=(
            "Antibody therapy predates the discovery of antibodies. Serum from "
            "an immunised animal worked without anyone knowing what was in it, "
            "and it earned the first Nobel Prize in Physiology or Medicine."
        ),
    ),
    # =========================================================================
    #  THE ENABLING TECHNIQUE
    # =========================================================================
    Milestone(
        1975,
        "Kohler and Milstein describe hybridoma monoclonal antibodies",
        note=(
            "Fusing an antibody-producing B cell with a myeloma gave an "
            "immortal line secreting one defined antibody. They did not patent "
            "it. The technique spread worldwide within months, which is "
            "probably the single largest reason the field developed as fast as "
            "it did."
        ),
    ),
    # =========================================================================
    #  FIRST PRODUCTS, AND WHY THEY DISAPPOINTED
    # =========================================================================
    Milestone(
        1986,
        "Muromonab-CD3 approved: the first therapeutic monoclonal antibody",
        note=(
            "Fully murine. Patients mounted a human anti-mouse antibody "
            "response that neutralised it, often within a single course. The "
            "commercial failure of the first generation is what drove "
            "humanisation."
        ),
    ),
    Milestone(
        1988,
        "Complementarity-determining region grafting demonstrated",
        note="Humanisation: mouse binding loops on a human framework.",
    ),
    # =========================================================================
    #  DISPLAY: DIRECTED EVOLUTION REPLACES IMMUNISATION
    # =========================================================================
    Milestone(
        1990,
        "Phage display of antibody fragments demonstrated",
        note=(
            "A library of billions of variants, searchable in a fortnight, "
            "without immunising anything. It made antibodies against toxic and "
            "non-immunogenic targets possible for the first time."
        ),
    ),
    Milestone(
        1993,
        "Camelid heavy-chain-only antibodies described",
        note=(
            "Found during a student project on frozen camel serum. A functional "
            "antibody with no light chain at all, one tenth the size of an IgG, "
            "and the origin of every single-domain format since."
        ),
    ),
    # =========================================================================
    #  THE MODALITY MATURES
    # =========================================================================
    Milestone(
        1997,
        "Rituximab approved, establishing antibodies as a mainstream modality",
    ),
    Milestone(
        1998,
        "Trastuzumab approved alongside a companion diagnostic",
        note=(
            "The first time a medicine was licensed together with a test that "
            "selects who should receive it. It set the pattern that "
            "`red.molecular_diagnostics` now describes."
        ),
    ),
    # =========================================================================
    #  THE SETBACK
    # =========================================================================
    Milestone(
        2006,
        "The TGN1412 first-in-human trial causes multi-organ failure in six "
        "healthy volunteers",
        note=(
            "A CD28 superagonist antibody. Preclinical models predicted safety "
            "because the target differs subtly between species, and all six "
            "participants were dosed within minutes of each other. The response "
            "changed first-in-human practice permanently: sequential dosing "
            "with intervals, the minimum anticipated biological effect level "
            "replacing the no-observed-adverse-effect level, and explicit "
            "assessment of species relevance."
        ),
    ),
    # =========================================================================
    #  FORMATS BEYOND THE NATURAL MOLECULE
    # =========================================================================
    Milestone(
        2011,
        "Modern antibody-drug conjugates reach approval",
        note=(
            "Earlier attempts failed on linker instability, releasing the "
            "payload in circulation. The advance was chemistry, not biology."
        ),
    ),
    Milestone(
        2014,
        "Checkpoint inhibitor antibodies transform oncology practice",
        note=(
            "The mechanism is unusual: the antibody does nothing to the tumour "
            "directly. It removes a brake on the patient's own immune "
            "response."
        ),
    ),
    Milestone(
        2017,
        "Emicizumab approved, a bispecific antibody that substitutes for a "
        "missing clotting factor",
        note=(
            "It does not block or mark anything. It bridges two proteins that "
            "would otherwise never meet, performing the geometric job of a "
            "protein the patient lacks. A demonstration that the format had "
            "escaped its immunological origins entirely."
        ),
    ),
    Milestone(
        2021,
        "Deep-learning structure prediction enters routine antibody design",
        note=(
            "Loop conformation prediction remains the weak point, and the loops "
            "are precisely the part that binds, so the technology helps most "
            "with the framework and least with the interesting part."
        ),
    ),
)
