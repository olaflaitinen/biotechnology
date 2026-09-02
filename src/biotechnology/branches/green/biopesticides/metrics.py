# =============================================================================
#  biotechnology.branches.green.biopesticides.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two corrections belong before the list.
#
#  FIRST: LC50 AND LT50 ARE NOT INTERCHANGEABLE, and for biological control the
#  second usually matters more. A synthetic insecticide is judged on how little
#  is needed; a biological agent is judged on how long it takes. A fungus with
#  an excellent LC50 and an LT50 of eight days will lose a crop that a grower
#  needs protected in three. Comparing a biopesticide with a synthetic on LC50
#  alone flatters it and then disappoints in the field.
#
#  SECOND: MORTALITY MUST BE CORRECTED FOR THE UNTREATED CONTROL. Insects die
#  in untreated plots too, from weather, disease and predation. Abbott's
#  correction removes that background, and an uncorrected mortality figure can
#  overstate efficacy by tens of percentage points in a season with natural
#  mortality. Every field number below assumes it has been applied.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # -------------------------------------------------------------------------
    #  How much is needed. The conventional potency measure.
    # -------------------------------------------------------------------------
    Metric(
        name="Median lethal concentration",
        symbol="LC50",
        unit="milligrams per litre, or spores or occlusion bodies per millilitre",
        typical="assay-, species- and instar-specific",
        formula="lc50_probit",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Estimated by probit or logit regression on a dose series. Strongly "
            "dependent on larval instar: a figure from first instars can be two "
            "orders of magnitude below one from fourth instars of the same "
            "species, so an LC50 quoted without the instar is not comparable "
            "with anything."
        ),
    ),
    # -------------------------------------------------------------------------
    #  How long it takes. The metric that decides adoption.
    # -------------------------------------------------------------------------
    Metric(
        name="Median lethal time",
        symbol="LT50",
        unit="days at a stated concentration",
        typical="1 - 3 days for Bt, 4 - 10 days for entomopathogenic fungi",
        formula="lt50",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The number that actually decides whether a grower adopts the "
            "product. Slow kill is the single most common reason a biological "
            "agent is rejected in favour of a synthetic, even where its LC50 is "
            "excellent. Note that a fungus-infected insect usually stops "
            "feeding well before it dies, so crop protection begins earlier "
            "than LT50 suggests, and that distinction is worth making to a "
            "sceptical grower."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Field efficacy, corrected. See the header note.
    # -------------------------------------------------------------------------
    Metric(
        name="Corrected field mortality",
        symbol="Abbott%",
        unit="per cent mortality corrected for the untreated control",
        typical="50 - 95 %",
        formula="abbott_correction",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Abbott's formula removes background mortality, which in a wet "
            "season with natural fungal epizootics can be substantial. An "
            "uncorrected figure overstates efficacy, sometimes by tens of "
            "percentage points, and is the most common error in promotional "
            "trial data."
        ),
    ),
    # -------------------------------------------------------------------------
    #  How much active substance is in the product.
    # -------------------------------------------------------------------------
    Metric(
        name="Active concentration",
        symbol="S_conc",
        unit="spores, conidia or occlusion bodies per gram or millilitre",
        typical="1e8 - 1e10 per gram",
        formula="colony_forming_units",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A count of propagules, not of activity. Viability and virulence "
            "both decline in storage while the count stays constant, so this "
            "figure is necessary and never sufficient, exactly as in "
            "`green.biofertilisers`."
        ),
    ),
    # -------------------------------------------------------------------------
    #  How long it survives on the leaf. The constraint made numerical.
    # -------------------------------------------------------------------------
    Metric(
        name="Field half-life",
        symbol="t_half_field",
        unit="hours to days of residual activity on foliage",
        typical="4 - 48 hours without ultraviolet protectants",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Ultraviolet degradation dominates, which is why formulation "
            "matters more than the organism for field performance, and why "
            "evening application is standard practice. This short half-life is "
            "simultaneously the safety profile and the efficacy problem."
        ),
    ),
    # -------------------------------------------------------------------------
    #  When to spray at all. The economic decision the whole approach rests on.
    # -------------------------------------------------------------------------
    Metric(
        name="Economic injury level and action threshold",
        symbol="EIL",
        unit="pest density per plant or per trap per unit time",
        typical="crop-, pest- and price-specific",
        formula="economic_threshold",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The density at which the cost of damage equals the cost of "
            "control. The action threshold sits below it, to allow for the lag "
            "before a slow-acting product works. Integrated pest management is, "
            "in operational terms, the discipline of spraying to this number "
            "rather than to a calendar."
        ),
    ),
    # -------------------------------------------------------------------------
    #  What it does to everything else. The point of the whole category.
    # -------------------------------------------------------------------------
    Metric(
        name="Non-target hazard quotient",
        symbol="HQ",
        unit="exposure divided by the no-effect concentration, dimensionless",
        typical="below 1 required for a favourable assessment",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Assessed against honeybees, other pollinators, predatory mites, "
            "parasitoid wasps, earthworms, fish and birds. IOBC classifies "
            "effects on beneficials on a four-point scale, and a product "
            "harmless to the predatory mite already established in a glasshouse "
            "is worth more there than one with a better kill rate."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Time from spray to harvest. Usually the strongest practical argument.
    # -------------------------------------------------------------------------
    Metric(
        name="Pre-harvest interval",
        symbol="PHI",
        unit="days between last application and harvest",
        typical="0 - 3 days for most biologicals; 7 - 30 for many synthetics",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Often the decisive commercial advantage in horticulture. A crop "
            "picked continuously cannot accommodate a three-week interval, so a "
            "product that can be applied the day before harvest wins on "
            "logistics regardless of its kill rate."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Resistance, which is not avoided merely by being biological.
    # -------------------------------------------------------------------------
    Metric(
        name="Resistance ratio",
        symbol="RR",
        unit="LC50 of a selected population divided by that of a susceptible one",
        typical="above 10 indicates meaningful resistance",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Bt resistance has evolved in several field populations where the "
            "same protein was used intensively as both spray and transgenic "
            "crop. Behavioural approaches such as mating disruption have the "
            "best record here, because a moth cannot easily evolve its way out "
            "of failing to find a mate."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  serial_dilution underlies every bioassay concentration series, and an error
#  there propagates directly into the LC50.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "lc50_probit",
    "lt50",
    "abbott_correction",
    "colony_forming_units",
    "economic_threshold",
    "serial_dilution",
    "hardy_weinberg",
)
