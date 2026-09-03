# =============================================================================
#  biotechnology.branches.blue.aquaculture_biotechnology.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  TWO METRICS IN THIS FACET ARE ROUTINELY QUOTED IN WAYS THAT MISLEAD, and
#  both are corrected in their notes rather than left to a reader.
#
#  FEED CONVERSION RATIO is the figure the industry leads with, and the
#  comparison it invites is unfair in the sector's favour. A fish is quoted on
#  wet weight while cattle and poultry are commonly quoted the same way, but a
#  fish is buoyant and does not maintain body temperature, so the biological
#  advantage is real and the numerical advantage is larger than the biological
#  one. The honest comparison uses dry matter or edible yield, and it still
#  favours fish, by less.
#
#  FISH-IN FISH-OUT is quoted by both sides of the argument and calculated
#  differently by each. Whether trimmings are counted, and whether oil or meal
#  is the limiting input, changes the answer by a factor. The note states the
#  convention problem rather than picking a number.
#
#  A THIRD POINT: THIS FACET CONTAINS WELFARE AND ESCAPE METRICS. They are
#  measurements of harm rather than of performance, and they are included for
#  the same reason `green.animal_biotechnology` includes its welfare terms:
#  a facet that measured only output would describe the industry as it
#  advertises itself.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # =========================================================================
    #  WHAT THE INDUSTRY LEADS WITH
    # =========================================================================
    Metric(
        name="Feed conversion ratio",
        symbol="FCR",
        unit="kilograms of feed per kilogram of weight gain",
        typical="1.1 - 1.5 for salmon, 1.5 - 1.8 for tilapia, against roughly "
        "6 - 10 for beef",
        formula="feed_conversion_ratio",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The sector's headline advantage and it is genuine: a fish is "
            "buoyant and does not spend energy maintaining body temperature. "
            "The comparison is nonetheless flattering, because wet-weight "
            "figures are not directly comparable across species with different "
            "moisture and edible yield. On a dry matter or edible portion basis "
            "the advantage remains and is smaller, and quoting the wet figure "
            "against terrestrial livestock without that caveat overstates it."
        ),
    ),
    Metric(
        name="Specific growth rate",
        symbol="SGR",
        unit="per cent body weight gain per day",
        typical="0.5 - 2 % per day depending on species, size and temperature",
        formula="specific_growth_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Strongly temperature dependent, since these animals do not "
            "regulate their own body temperature. A growth figure without its "
            "water temperature is close to uninterpretable, and the same stock "
            "performs very differently across a farm's seasonal range."
        ),
    ),
    Metric(
        name="Genetic gain per generation",
        symbol="dG",
        unit="per cent improvement in the selected trait per generation",
        typical="10 - 15 % per generation for growth in well-run programmes",
        formula="breeders_equation",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Far above what terrestrial livestock programmes achieve, and the "
            "reason is fecundity: a single female may produce thousands of "
            "offspring, so selection intensity can be extreme without "
            "collapsing the population. Domestication began only in the 1970s "
            "for salmon, so these animals remain a few generations from wild "
            "and the gains are still being taken."
        ),
    ),
    # =========================================================================
    #  THE METRIC BOTH SIDES QUOTE AND NEITHER DEFINES THE SAME WAY
    # =========================================================================
    Metric(
        name="Fish-in fish-out ratio",
        symbol="FIFO",
        unit="kilograms of wild fish input per kilogram of farmed fish "
        "produced",
        typical="reduced by a large factor for salmon since the 1990s, and "
        "reported differently depending on the convention used",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Graded REPORTED because the number depends on the accounting. "
            "Whether processing trimmings count as an input, and whether the "
            "calculation is limited by fishmeal or by fish oil, changes the "
            "result by a factor, and advocates on both sides select the "
            "convention that suits them. What is not in dispute is the "
            "direction: the ratio has fallen substantially and has not reached "
            "zero."
        ),
    ),
    Metric(
        name="Marine ingredient inclusion",
        symbol="f_marine",
        unit="per cent of feed by weight from marine sources",
        typical="much reduced in salmon feed since the 1990s, with a growing "
        "share of the remainder from trimmings",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A more transparent figure than the ratio above because it does not "
            "depend on an allocation convention. It should be read with the "
            "source of the marine fraction stated, since trimmings from fish "
            "already caught for human consumption are a different proposition "
            "from fish caught for reduction."
        ),
    ),
    # =========================================================================
    #  WHAT HAPPENS TO THE ANIMALS
    # =========================================================================
    Metric(
        name="Cycle mortality",
        symbol="M_cycle",
        unit="per cent of stocked animals dying before harvest",
        typical="commonly 10 - 20 % in salmon production, and higher in "
        "outbreak years",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A welfare measurement and an economic one at once, and it is "
            "higher than most consumers would assume. It is included here "
            "rather than left to an impact assessment because a facet reporting "
            "only growth and conversion would describe the sector as it "
            "advertises itself."
        ),
    ),
    Metric(
        name="Sea lice count per fish",
        symbol="n_lice",
        unit="adult female lice per fish",
        typical="regulatory thresholds are typically set below one adult "
        "female per fish during wild migration periods",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "One of very few metrics in this library that is a direct legal "
            "trigger: exceeding the threshold requires treatment or harvest. "
            "The threshold is set low and seasonally because the concern is "
            "transmission to wild juvenile salmon passing the farm, not the "
            "health of the farmed fish."
        ),
    ),
    Metric(
        name="Stocking density",
        symbol="rho_stock",
        unit="kilograms of fish per cubic metre",
        typical="10 - 25 kg/m3 in salmon pens, with limits set by regulation "
        "or certification",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A contested welfare indicator that is a poor one used alone. Water "
            "quality, oxygen and behaviour matter more than density itself, and "
            "for some species low density is worse because they shoal. It is "
            "recorded because it is what regulation actually limits, not "
            "because it is the best measure of welfare."
        ),
    ),
    # =========================================================================
    #  WHAT LEAVES THE FARM
    # =========================================================================
    Metric(
        name="Escape rate",
        symbol="R_esc",
        unit="escaped fish per million produced",
        typical="highly variable, dominated by rare large structural failures "
        "rather than by steady leakage",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The distribution matters more than the mean: most escapes come "
            "from a small number of large events such as storm damage, so an "
            "average rate misrepresents the risk. Genetic assignment of "
            "escapees to their farm of origin is what makes this enforceable, "
            "and the consequence of interbreeding with wild populations is "
            "irreversible once it has occurred."
        ),
    ),
    Metric(
        name="Nitrogen and phosphorus discharge",
        symbol="N_disc",
        unit="kilograms per tonne of fish produced",
        typical="determined by feed conversion, feed composition and uneaten "
        "feed",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Follows almost directly from feed conversion ratio, which is why "
            "improving that figure is an environmental measure as well as an "
            "economic one. It sets how densely an area may be farmed and is "
            "what integrated multi-trophic systems are designed to recapture."
        ),
    ),
    Metric(
        name="Antibiotic use",
        symbol="U_abx",
        unit="grams of active substance per tonne of production",
        typical="very low in vaccinated salmon production, and substantially "
        "higher in several other farmed species and regions",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The clearest documented success in this record, achieved by "
            "vaccination rather than by prohibition, exactly as "
            "`green.veterinary_vaccines` describes. The qualification matters: "
            "the achievement is specific to salmon and to jurisdictions with "
            "effective vaccines, and it should not be generalised to "
            "aquaculture as a whole."
        ),
    ),
    Metric(
        name="Survival to harvest in hatchery stages",
        symbol="S_hatch",
        unit="per cent of larvae reaching juvenile stage",
        typical="low and highly variable for marine species with small larvae",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The bottleneck that decides which species can be farmed at all. "
            "Species whose larvae are large and robust were domesticated "
            "readily; those with tiny larvae requiring live feed remain "
            "difficult, which is why the farmed species list is shorter than "
            "the list of species people eat."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Production first, then the genetics, then the balances.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "feed_conversion_ratio",
    "specific_growth_rate",
    "breeders_equation",
    "heritability",
    "mass_balance",
    "mortality_rate",
    "effective_population_size",
)
