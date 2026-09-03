# =============================================================================
#  biotechnology.branches.yellow.cultivated_meat.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has three: a cost curve that did not arrive, a set of
#  outright prohibitions that no technical progress addresses, and a funding
#  contraction that followed both.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE 2013 ENTRY IS ROUTINELY MISREAD AND THE MISREADING MATTERS.
#
#  The first cultivated burger was presented publicly at a cost in the hundreds
#  of thousands of euro. It was a demonstration that the biology worked, funded
#  as such, and it was never a product. What followed was a decade in which the
#  cost fell by orders of magnitude, which is a genuine achievement, and did
#  not reach commodity meat, which is a genuine failure. Both statements are
#  true and the field's coverage has generally carried one or the other.
#
#  A second point about attribution. Animal cell culture at manufacturing scale
#  was developed by the pharmaceutical industry over forty years, and this
#  record inherited it. What is new here is the requirement to do it at food
#  cost, which is a different problem and which the inherited equipment and
#  reagents were never designed for.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE IDEA, AND THE INHERITED CAPABILITY
    # =========================================================================
    Milestone(
        1931,
        "Churchill speculates that meat might be grown from the relevant parts "
        "rather than from a whole animal",
        note=(
            "Frequently quoted and worth including for what it is: a "
            "speculation with no technical content, made when animal cell "
            "culture did not yet exist. It is included because the field cites "
            "it often, and it should not be mistaken for a scientific "
            "antecedent."
        ),
    ),
    Milestone(
        1951,
        "Continuously culturable human cells establish that animal cells can be "
        "propagated indefinitely",
        note=(
            "The HeLa line demonstrated immortalised animal cell culture. "
            "Everything in this record depends on the capability established "
            "here, and the ethical history of that particular line is a matter "
            "`purple.bioethics` addresses rather than this record."
        ),
    ),
    Milestone(
        1986,
        "Large-scale mammalian cell culture becomes routine in pharmaceutical "
        "manufacture",
        note=(
            "Forty years of equipment, media and process development, inherited "
            "wholesale by this record. What was not inherited was a cost "
            "structure: pharmaceutical culture is sized for grams of product "
            "worth thousands of euro, and food requires tonnes worth a few euro."
        ),
    ),
    # =========================================================================
    #  THE DEMONSTRATION
    # =========================================================================
    Milestone(
        2013,
        "The first cultivated beef burger is presented publicly",
        note=(
            "Cost in the hundreds of thousands of euro, funded as a "
            "demonstration and never intended as a product. It proved the "
            "biology and set the field's public expectations, and the "
            "expectations it set were about timelines rather than about "
            "science. Reading it as a failed product misses what it was; "
            "reading it as a near-market achievement misses it equally."
        ),
    ),
    # =========================================================================
    #  REMOVING THE CONTRADICTION AT THE CENTRE OF THE PROPOSITION
    # =========================================================================
    Milestone(
        2017,
        "Serum-free media suitable for cultivated meat are developed",
        note=(
            "Foetal bovine serum is a slaughterhouse product, so a meat "
            "alternative depending on it was incoherent as well as expensive. "
            "Removing it was necessary before the field could make its own "
            "argument, and it remains among the most substantial technical "
            "achievements recorded here."
        ),
    ),
    # =========================================================================
    #  APPROVAL, TWICE, AT SMALL SCALE
    # =========================================================================
    Milestone(
        2020,
        "Singapore approves the sale of cultivated chicken",
        note=(
            "The first regulatory approval anywhere. Small volumes, formed "
            "products rather than cuts, and sold through restaurants. It "
            "established that a regulator would assess and approve such a "
            "product, which had not previously been demonstrated."
        ),
    ),
    Milestone(
        2023,
        "The United States approves cultivated chicken for sale",
        note=(
            "A joint assessment between two agencies, reflecting that the "
            "product is a cell culture process producing a meat product and "
            "falls between existing frameworks. Volumes remained small and "
            "availability limited to a few restaurants."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: PROHIBITION FOR REASONS TECHNOLOGY CANNOT ADDRESS
    # =========================================================================
    Milestone(
        2023,
        "Italy prohibits the production and sale of cultivated meat",
        note=(
            "A national ban enacted before any such product was on sale there, "
            "on grounds concerning food heritage and agricultural livelihoods "
            "rather than safety. Several jurisdictions elsewhere followed with "
            "comparable measures. It is recorded as a setback of a kind this "
            "library rarely contains: the objection is cultural and political, "
            "it is not answerable by evidence, and no amount of technical "
            "progress addresses it."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE COST CURVE, AND THE MONEY
    # =========================================================================
    Milestone(
        2024,
        "Cost reduction slows and investment in the sector contracts sharply",
        note=(
            "The decline from 2013 had been rapid and it flattened as the "
            "remaining cost concentrated in medium inputs and in capital for "
            "capacity that does not exist. Several companies closed or reduced "
            "scope, and attention moved to hybrid products using cultivated fat "
            "with plant protein, where a small quantity of the expensive "
            "component carries the flavour. Recorded as a setback because the "
            "projections had assumed a learning curve that this cost structure "
            "does not produce, which is the same error "
            "`yellow.precision_fermentation` made in 2023."
        ),
    ),
    # =========================================================================
    #  WHERE THE FIELD ACTUALLY IS
    # =========================================================================
    Milestone(
        2022,
        "Cultivated pet food reaches market ahead of human food in some "
        "jurisdictions",
        note=(
            "A shorter regulatory path and no consumer acceptance question in "
            "the same form. It is a rational commercial response and it is also "
            "an admission about where the barriers are, since the technical "
            "requirements are not lower."
        ),
    ),
    Milestone(
        2024,
        "Food-grade medium components and recombinant growth factor production "
        "become the field's principal work",
        note=(
            "Replacing pharmaceutical-grade inputs with food-grade equivalents "
            "and producing growth factors by microbial fermentation, which "
            "connects directly to `yellow.precision_fermentation`. It is "
            "unglamorous, it is where the remaining cost is, and it is the "
            "clearest sign the field has correctly identified its own problem."
        ),
    ),
)
