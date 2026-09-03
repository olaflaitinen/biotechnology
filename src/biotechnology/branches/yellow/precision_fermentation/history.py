# =============================================================================
#  biotechnology.branches.yellow.precision_fermentation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two: a product that worked and was withdrawn on
#  acceptance rather than on evidence, and a sector whose cost projections have
#  repeatedly not been met.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE 1988 AND 1994 ENTRIES SHOULD BE READ TOGETHER, because between them
#  they contain the most useful lesson this record has about consumer
#  acceptance.
#
#  Fermentation-produced chymosin was approved in 1988 and went on to be used
#  in the majority of cheese made in several countries. It attracted almost no
#  opposition.
#
#  Recombinant bovine somatotropin was approved in 1994, was scientifically
#  defensible, and became one of the most successfully opposed agricultural
#  biotechnologies in Europe.
#
#  The difference was not the science and not the risk. Chymosin is purified
#  away from the organism, replaces an enzyme taken from slaughtered calves,
#  and gives the consumer something. The hormone was administered to animals,
#  raised welfare questions, and gave the consumer nothing they had asked for.
#  A product in this record that cannot say what the eater gains is starting
#  from the second position rather than the first.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE TECHNIQUE ARRIVES, IN MEDICINE
    # =========================================================================
    Milestone(
        1982,
        "Recombinant human insulin produced in bacteria is approved",
        note=(
            "The first recombinant protein product of any kind. Everything in "
            "this record uses the method established here, which is why the "
            "claim that precision fermentation is a new technology does not "
            "survive contact with its own history. What differs later is the "
            "target and the price it must meet."
        ),
    ),
    # =========================================================================
    #  THE FIRST FOOD PRODUCT, AND IT WENT WELL
    # =========================================================================
    Milestone(
        1988,
        "Fermentation-produced chymosin is approved for cheesemaking",
        note=(
            "The first recombinant product accepted into the food chain. It "
            "replaced an enzyme extracted from the stomachs of slaughtered "
            "calves, is purified away from the production organism, and "
            "improved supply and consistency. It went on to be used in the "
            "majority of cheese produced in several countries with almost no "
            "opposition, which makes it the most successful and least discussed "
            "product in this record."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE SAME SCIENCE, THE OPPOSITE RECEPTION
    # =========================================================================
    Milestone(
        1994,
        "Recombinant bovine somatotropin is approved in the United States and "
        "rejected in Europe",
        note=(
            "Scientifically defensible and commercially damaging. It was "
            "administered to animals rather than purified from a fermenter, it "
            "raised welfare questions, and it offered the consumer nothing they "
            "had asked for. Europe declined it and the resulting labelling "
            "campaigns shaped public attitudes to food biotechnology for a "
            "generation. Recorded as a setback because it demonstrates that "
            "approval and acceptance are different problems, and that the "
            "second is decided by what the eater gains."
        ),
    ),
    # =========================================================================
    #  THE LEGAL FRAMEWORK THAT STILL GOVERNS THE FIELD
    # =========================================================================
    Milestone(
        1997,
        "European novel food authorisation is established",
        note=(
            "Prior approval becomes the rule for foods without a significant "
            "history of consumption in the Union. It is the instrument that "
            "makes this record AUTHORISED where `yellow.food_fermentation` is "
            "UNREGULATED, for the same underlying biology, and it applies in "
            "full to a molecule identical to one eaten for millennia."
        ),
    ),
    # =========================================================================
    #  QUIET SUCCESS AT SCALE
    # =========================================================================
    Milestone(
        2005,
        "Fermentation-derived vitamins and amino acids dominate their markets",
        note=(
            "Vitamin B2, vitamin B12 and the feed amino acids are made this "
            "way at very large scale and are almost never described by this "
            "record's name. For B12 the fermentation route is the only "
            "practical source for people eating no animal products."
        ),
    ),
    Milestone(
        2019,
        "Yeast-produced heme protein enters wide use in plant-based meat",
        note=(
            "Approved after a novel food and colour additive assessment, and it "
            "became the most widely eaten product in this record that consumers "
            "do not associate with it. It also demonstrated the value of a "
            "clear consumer benefit, since the protein is what makes the "
            "product taste as intended."
        ),
    ),
    Milestone(
        2020,
        "Precision fermentation dairy proteins reach the market",
        note=(
            "Beta-lactoglobulin and other whey proteins approved and sold, in "
            "ice cream and protein products first because those applications "
            "are the least demanding functionally. It is the point at which the "
            "term entered general use, roughly forty years after the technique "
            "was established."
        ),
    ),
    Milestone(
        2021,
        "Human milk oligosaccharides produced by fermentation are authorised "
        "for infant formula",
        note=(
            "Compounds with no other practical source at scale, in one of the "
            "most heavily regulated food categories that exists. It is the "
            "clearest case in this record of fermentation supplying something "
            "that cannot otherwise be supplied, rather than a cheaper route to "
            "something that can."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE COST CURVE DID NOT ARRIVE
    # =========================================================================
    Milestone(
        2023,
        "Cost projections for bulk precision fermentation proteins prove "
        "optimistic and funding contracts",
        note=(
            "Projections had assumed rapid cost declines with scale, on "
            "analogy with technologies whose costs are dominated by "
            "manufacturing learning rather than by feedstock and downstream "
            "processing. Neither falls that way. Several companies reduced "
            "scope or failed, and the sector's centre moved towards "
            "high-value proteins where the price target is reachable. Recorded "
            "as a setback because the technical work was sound and the "
            "economic reasoning was not, which is the same pattern "
            "`white.biobased_chemicals` records for succinic acid."
        ),
    ),
    Milestone(
        2024,
        "Regulatory approvals accumulate across jurisdictions on divergent "
        "timelines",
        note=(
            "Products approved in one market remained years from another, and "
            "naming and labelling questions were decided differently in each. "
            "The divergence is a barrier to entry that favours companies able "
            "to fund several parallel dossiers, which is the practical effect "
            "of a precautionary regime rather than its intent."
        ),
    ),
)
