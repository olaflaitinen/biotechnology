# =============================================================================
#  biotechnology.branches.red.regenerative_medicine.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has a hard physical limit that no amount of biology will move,
#  and the whole field is organised around it. Oxygen diffuses about two
#  hundred micrometres through living tissue before it runs out. Any construct
#  thicker than that dies in the middle unless it carries its own plumbing.
#
#  That single number explains why skin, cartilage and cornea reached patients
#  decades ago and a liver has not. The public register states it explicitly
#  rather than leaving it to `metrics.py`, because a reader who does not know
#  it will assume the obstacle is cell biology and will therefore misjudge
#  every claim made about grown organs.
#
#  WHY_IT_MATTERS also carries a warning the field does not usually put in its
#  own summaries: unproven stem cell clinics sell to desperate patients in
#  jurisdictions with weak oversight, and people have been blinded and killed.
#  Omitting that from a record aimed partly at patients would be a failure of
#  editorial rule 3.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

__all__ = [
    "SUMMARY",
    "DESCRIPTION",
    "PLAIN_LANGUAGE",
    "ANALOGY",
    "WHY_IT_MATTERS",
]


# =============================================================================
#  TECHNICAL REGISTER
# =============================================================================

SUMMARY = (
    "Restoring the structure and function of damaged tissue by combining "
    "cells, scaffolds and signalling molecules."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the aim and the three-component idea, (b) what each component
#  can be, (c) what has and has not reached patients, (d) the binding
#  constraint, which is physical rather than biological.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the aim
    "Regenerative medicine aims to restore lost tissue function rather than to "
    "compensate for it. Tissue engineering, its main engineering arm, builds "
    "constructs from three components, and removing any one of them causes "
    "failure. "
    # (b) the components
    "Cells may be primary, expanded from a biopsy, or derived from induced "
    "pluripotent stem cells. Scaffolds may be synthetic polymers, natural "
    "polymers such as collagen and alginate, or decellularised extracellular "
    "matrix that retains the architecture of the original organ. Signals "
    "include soluble growth factors, immobilised peptide motifs, and mechanical "
    "conditioning in a bioreactor, since many tissues will not mature unless "
    "they are loaded while they grow. Scaffold stiffness is itself a signal: "
    "identical stem cells differentiate towards bone on a hard substrate and "
    "towards nerve on a soft one. "
    # (c) what has reached patients
    "Simple avascular tissues have reached clinical use because they can "
    "survive on diffusion alone: skin, cartilage, cornea and bladder. Thick, "
    "metabolically demanding organs have not. "
    # (d) the constraint
    "The binding constraint is physical, not biological. Oxygen diffuses "
    "roughly one hundred to two hundred micrometres from a capillary before it "
    "is exhausted, so no construct thicker than about two hundred micrometres "
    "survives without a perfusable vascular network. Two lines of work address "
    "this: three-dimensional bioprinting of sacrificial channels that are "
    "flushed out to leave plumbing behind, and organoids, which are "
    "self-organising miniature tissues used today mainly as disease models and "
    "drug-screening platforms rather than as implants."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "If you break a bone it heals, but if you lose a large piece of liver or a "
    "heart valve, the body cannot rebuild it. Regenerative medicine supplies "
    "what is missing: living cells, a supporting framework for them to grow on, "
    "and chemical instructions telling them what to become. Thin tissues such "
    "as skin and cartilage are already made this way and used in hospitals. "
    "Whole complex organs are not, and the reason is simpler than most people "
    "expect. Oxygen can only soak about a fifth of a millimetre into living "
    "tissue before it runs out. Anything thicker needs its own blood vessels, "
    "and building a working network of blood vessels from scratch is the "
    "problem the field has not yet solved."
)

# -----------------------------------------------------------------------------
#  The hedge analogy. Its limit is deliberately the actual problem: a hedge
#  dies in the middle if water does not reach it, which is exactly the
#  diffusion limit.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Think of planting a hedge rather than building a fence. The fence is a hip "
    "replacement: manufactured, inert, and eventually worn out. The hedge is "
    "regenerative medicine: you supply seedlings, a trellis and the right "
    "conditions, and the living thing grows into the gap and maintains itself. "
    "The comparison holds all the way down to the failure mode. A hedge planted "
    "too thick dies in the middle, because water never reaches the centre, and "
    "that is precisely what happens to a tissue construct without blood "
    "vessels."
)

WHY_IT_MATTERS = (
    "Organ transplantation is limited by donors, not by surgical skill. Tens of "
    "thousands of people are on European waiting lists and a significant number "
    "die waiting. Engineered tissue would remove the donor constraint and the "
    "lifelong immunosuppression that follows a transplant. Even short of that, "
    "organoids are already changing drug development by letting a compound be "
    "tested on human tissue, and on tissue from a specific patient, before "
    "anyone is dosed. Two costs belong in the same paragraph. The first is that "
    "the field has promised grown organs for three decades and delivered thin "
    "tissues, which has made honest assessment of its timelines difficult. The "
    "second is more serious: unproven stem cell clinics sell unregulated "
    "injections to desperate patients in jurisdictions with weak oversight. "
    "People have been permanently blinded by intraocular injections marketed as "
    "stem cell therapy, and people have died. The gap between what this field "
    "can do and what is sold in its name is itself a public health problem."
)
