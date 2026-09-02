# =============================================================================
#  biotechnology.branches.green.veterinary_vaccines.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  One difference from `red.vaccine_development` runs through this whole set
#  and is worth stating before the list.
#
#  IN HUMAN VACCINOLOGY THE ENDPOINT IS USUALLY THE INDIVIDUAL. In veterinary
#  vaccinology it is usually the POPULATION. A vaccine that does not prevent
#  infection but reduces how much virus an infected animal sheds can still
#  drive the reproduction number below one and stop an epidemic, and that is
#  frequently what is bought. Judging a veterinary vaccine on individual
#  protection alone misses the point of most of them.
#
#  A second difference: cost per dose is a first-class technical constraint
#  here, not a commercial afterthought. It is included below as a metric
#  because it determines which products can exist, and no honest account of
#  this field can leave it out.
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
    #  The population endpoint. What most veterinary vaccination is actually
    #  aiming at.
    # -------------------------------------------------------------------------
    Metric(
        name="Reproduction number under vaccination",
        symbol="R_v",
        unit="secondary cases per case, dimensionless",
        typical="target below 1",
        formula="basic_reproduction_number",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The operative endpoint for most livestock vaccination. A vaccine "
            "that reduces shedding without preventing infection can still push "
            "R_v below one and end an epidemic, which is why individual "
            "protection is often the wrong measure to judge these products by."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Shedding reduction, which is the mechanism behind the metric above.
    # -------------------------------------------------------------------------
    Metric(
        name="Reduction in pathogen shedding",
        symbol="dShed",
        unit="log10 reduction in organisms excreted",
        typical="1 - 4 log10 reduction",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Often the primary registration endpoint for a transmission-control "
            "vaccine, and the quantity that connects an individual animal's "
            "response to the herd-level result. A two-log reduction in shedding "
            "changes an epidemic curve even where every animal still becomes "
            "infected."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Individual protection, for completeness.
    # -------------------------------------------------------------------------
    Metric(
        name="Vaccine efficacy in the herd",
        symbol="VE",
        unit="per cent reduction in risk relative to unvaccinated controls",
        typical="60 - 95 % against clinical disease",
        formula="vaccine_efficacy",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Usually measured against clinical disease or mortality rather than "
            "against infection, and in a challenge study rather than a field "
            "trial, because a controlled challenge is ethically and practically "
            "possible in animals in a way it is not in people."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Coverage, and why the threshold is not the whole answer.
    # -------------------------------------------------------------------------
    Metric(
        name="Vaccination coverage",
        symbol="V_cov",
        unit="per cent of the herd, flock or target population vaccinated",
        typical="above 80 % for transmission control",
        formula="herd_immunity_threshold",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Coverage is easier to achieve in a housed flock than in an "
            "extensive grazing system or a wildlife population, so the same "
            "threshold is trivial in one production system and unreachable in "
            "another. Reported national coverage frequently overstates coverage "
            "in the herds that matter most."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The serological readout, which in poultry is the routine measure.
    # -------------------------------------------------------------------------
    Metric(
        name="Haemagglutination inhibition titre",
        symbol="log2 HI",
        unit="log2 reciprocal titre",
        typical="protective threshold around 4 to 5 log2",
        formula="geometric_mean_titre",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Reported as a geometric mean because titres are log-normally "
            "distributed. Flock uniformity matters as much as the mean: a flock "
            "with a good average and wide spread contains susceptible birds, "
            "and the coefficient of variation is watched for that reason."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The DIVA test. A performance metric with no human equivalent.
    # -------------------------------------------------------------------------
    Metric(
        name="DIVA test specificity",
        symbol="Sp_DIVA",
        unit="per cent of vaccinated animals correctly identified as uninfected",
        typical="above 99 % required for trade purposes",
        formula="sensitivity_specificity",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A very high bar, because the test is applied to whole national "
            "populations and a one per cent false positive rate across millions "
            "of animals produces thousands of spurious detections, each of "
            "which can trigger movement restrictions. This is the technical "
            "requirement that makes vaccination compatible with trade."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Antimicrobial use. The One Health outcome measure.
    # -------------------------------------------------------------------------
    Metric(
        name="Defined daily dose for animals",
        symbol="DDDvet",
        unit="milligrams of active substance per population correction unit",
        typical="the standard European benchmark; sales more than halved "
        "since 2011",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Normalised by population correction unit, an estimate of the "
            "biomass at risk of treatment, so that a country with many pigs and "
            "one with many cattle can be compared. The reduction achieved since "
            "2011 came largely from vaccination and husbandry rather than from "
            "prohibition, which is the strongest evidence for this record's "
            "SDG 3 claim."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The constraint, stated as a metric because it decides what exists.
    # -------------------------------------------------------------------------
    Metric(
        name="Cost per dose",
        symbol="C_dose",
        unit="euro cents per dose",
        typical="1 - 50 cents for poultry, higher for cattle and fish",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A first-class technical constraint rather than a commercial "
            "afterthought. It determines the platform, the adjuvant, the "
            "presentation and the route, and it is the reason many technically "
            "excellent candidates never become products. No honest account of "
            "this field can omit it."
        ),
    ),
    # -------------------------------------------------------------------------
    #  How long protection lasts, which sets the handling burden.
    # -------------------------------------------------------------------------
    Metric(
        name="Duration of immunity",
        symbol="DOI",
        unit="months of demonstrated protection",
        typical="6 months to lifetime, depending on platform and species",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Must exceed the production cycle to be useful: a broiler lives "
            "about six weeks, so a vaccine given in ovo need only protect for "
            "that long, whereas a breeding cow needs years. Each additional "
            "handling of an animal costs more than the vaccine itself, which is "
            "why multivalent products dominate."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  prevalence_estimation is included because herd-level surveillance uses
#  pooled testing, where the relationship between pool positivity and true
#  prevalence is not intuitive.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "basic_reproduction_number",
    "herd_immunity_threshold",
    "vaccine_efficacy",
    "geometric_mean_titre",
    "sensitivity_specificity",
    "prevalence_estimation",
    "serial_dilution",
)
