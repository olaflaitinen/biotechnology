# =============================================================================
#  biotechnology.branches.yellow.alternative_proteins.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record's principal one is unusually well documented because it
#  happened in public markets: a category that grew rapidly, was widely
#  covered, and then contracted on repeat purchase.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE OLDEST ENTRIES ARE THE MOST INSTRUCTIVE AND THE LEAST DISCUSSED.
#
#  Tofu, tempeh and seitan are plant protein foods of considerable antiquity
#  that are cheap, minimally processed, and eaten daily by very large numbers
#  of people. Mycoprotein has been sold since 1985 and is fibrous without
#  extrusion. None of these belongs to the wave that began around 2015, and all
#  of them are more successful by any measure of longevity.
#
#  A record that began in 2013 with the first cultivated burger and treated the
#  rest as prehistory would misdescribe the subject, and would also miss the
#  most useful comparison available: the traditional products avoid every one
#  of the ultra-processing, price and repeat-purchase problems that defeated
#  the new ones, because they are not trying to imitate meat.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE PRODUCTS THAT WERE ALREADY WORKING
    # =========================================================================
    Milestone(
        -200,
        "Tofu production is established in China",
        note=(
            "A plant protein food that is cheap, minimally processed and eaten "
            "daily by very large numbers of people. The conventional date "
            "stands for a practice of uncertain origin. It is included first "
            "because it avoids every problem the modern sector encountered, by "
            "not attempting to imitate meat."
        ),
    ),
    Milestone(
        1600,
        "Tempeh fermentation is established in Java",
        note=(
            "Fungal fermentation binding soybeans into a firm cake, which "
            "improves digestibility and produces a fibrous structure "
            "biologically. It is the traditional ancestor of the mycoprotein "
            "entry below and predates it by centuries."
        ),
    ),
    # =========================================================================
    #  THE INDUSTRIAL ERA BEGINS, AND FOR THE WRONG REASON
    # =========================================================================
    Milestone(
        1960,
        "Textured vegetable protein is developed by low-moisture extrusion",
        note=(
            "Developed as a cheap protein extender for meat products rather "
            "than as a replacement for them, which is worth noting: the "
            "technology that underlies the modern sector entered food "
            "manufacture as a cost-reduction measure."
        ),
    ),
    Milestone(
        1985,
        "Mycoprotein is approved and sold as a food",
        note=(
            "Filamentous fungal biomass whose hyphae give a fibrous texture "
            "without extrusion. Forty years on the market makes this the "
            "longest-established purpose-built meat alternative, and it "
            "achieved that with a structure obtained biologically rather than "
            "mechanically."
        ),
    ),
    # =========================================================================
    #  THE TECHNOLOGY THAT MADE THE MODERN SECTOR POSSIBLE
    # =========================================================================
    Milestone(
        2000,
        "High-moisture extrusion produces anisotropic whole-muscle-like "
        "structures",
        note=(
            "Long cooling dies allowed protein to align into fibres rather than "
            "expand into a sponge, which is the difference between textured "
            "protein and something resembling a cut of meat. Every product in "
            "the 2015 wave depends on it."
        ),
    ),
    Milestone(
        2016,
        "Plant-based burgers using fermentation-derived heme reach wide retail "
        "distribution",
        note=(
            "The combination of high-moisture extrusion, fat structuring and a "
            "flavour compound from `yellow.precision_fermentation` produced "
            "products that behaved like meat during cooking. Trial rates were "
            "very high and the category expanded rapidly."
        ),
    ),
    Milestone(
        2019,
        "The plant-based meat category peaks",
        note=(
            "Rapid growth, wide distribution, substantial investment and heavy "
            "media coverage. Every technical metric in `metrics.py` was "
            "improving. The one that was not being measured publicly was repeat "
            "purchase."
        ),
    ),
    # =========================================================================
    #  THE SETBACK, IN PUBLIC
    # =========================================================================
    Milestone(
        2023,
        "The plant-based meat category contracts on repeat purchase rather "
        "than on trial",
        note=(
            "Sales fell, companies restructured and several failed. Awareness "
            "and distribution had not been the problem: people bought the "
            "products once and did not buy them again, on taste and on price. "
            "Two further factors compounded it. Price parity with commodity "
            "meat was never reached, and the ultra-processed classification "
            "placed the products in a category consumers were simultaneously "
            "being advised to avoid. It is recorded as a setback because the "
            "technical work was sound and the category still contracted, which "
            "is the clearest demonstration in this branch that acceptance is an "
            "engineering constraint rather than a communications problem."
        ),
    ),
    # =========================================================================
    #  THE PARTS THAT KEPT WORKING
    # =========================================================================
    Milestone(
        2021,
        "Insect protein is authorised as a novel food in the European Union",
        note=(
            "Mealworm was the first, followed by other species. Authorisation "
            "removed the regulatory barrier and left the acceptance barrier "
            "untouched, and most producers responded by selling into animal "
            "feed, where the question does not arise."
        ),
    ),
    Milestone(
        2017,
        "Insect meal is authorised for use in aquaculture feed in the European "
        "Union",
        note=(
            "The commercially significant insect protein decision, and it "
            "concerns feed rather than food. It addresses the fishmeal demand "
            "recorded in `blue.aquaculture_biotechnology` without asking any "
            "consumer to change what they eat, which is why it succeeded where "
            "the food route has not."
        ),
    ),
    Milestone(
        2020,
        "Plant-based dairy alternatives continue growing while meat analogues "
        "contract",
        note=(
            "Recorded as a contrast that is easy to miss. Milk is a "
            "less demanding target than muscle: it has no fibre structure to "
            "reproduce, it is consumed in applications where difference is "
            "tolerated, and the price gap is smaller. The divergence between "
            "the two categories is a statement about how hard the texture "
            "problem is."
        ),
    ),
    Milestone(
        2024,
        "The sector moves towards whole-cut products, fermentation-derived "
        "structure and shorter ingredient lists",
        note=(
            "A response to both problems at once: mycelium and fungal "
            "fermentation give structure biologically, which shortens the "
            "ingredient list that produced the ultra-processed classification. "
            "It is a return to the approach mycoprotein took in 1985, arrived "
            "at from the other direction."
        ),
    ),
)
