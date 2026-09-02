# =============================================================================
#  biotechnology.branches.red.vaccine_development.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  These are the numbers that appear in public debate, which makes their notes
#  more important here than anywhere else in the taxonomy. Two distinctions in
#  particular are routinely collapsed in reporting and are spelled out below:
#
#    * EFFICACY is measured in a trial, under trial conditions, in the
#      population that was enrolled. EFFECTIVENESS is the same quantity
#      measured in the field. They are different numbers and the second is
#      almost always lower.
#    * A HERD IMMUNITY THRESHOLD is a property of a pathogen and a population,
#      not of a vaccine. It assumes homogeneous mixing, which no real
#      population has, so the real figure is always higher than the formula
#      gives.
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
    #  Vaccine efficacy. The headline number, and the most misreported one.
    # -------------------------------------------------------------------------
    Metric(
        name="Vaccine efficacy",
        symbol="VE",
        unit="per cent reduction in risk relative to control",
        typical="50 - 97 % against symptomatic disease",
        formula="vaccine_efficacy",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "VE = 1 - RR, where RR is the risk ratio between the vaccinated and "
            "unvaccinated arms. Efficacy is measured in a trial; effectiveness "
            "is the same quantity measured in the field and is almost always "
            "lower. A figure quoted without saying which one it is, and against "
            "which endpoint, is not interpretable."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Basic reproduction number. A property of the pathogen and the
    #  population, not of the vaccine, and the input to the threshold below.
    # -------------------------------------------------------------------------
    Metric(
        name="Basic reproduction number",
        symbol="R0",
        unit="secondary cases per case, dimensionless",
        typical="1.5 for seasonal influenza to 15 or more for measles",
        formula="basic_reproduction_number",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "R0 depends on the contact structure of the population as much as "
            "on the pathogen, so a value measured in one setting does not "
            "transfer to another."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Herd immunity threshold. Derived from R0, and the number most often
    #  quoted with more confidence than it deserves.
    # -------------------------------------------------------------------------
    Metric(
        name="Herd immunity threshold",
        symbol="H_c",
        unit="fraction of the population immune",
        typical="1 - 1/R0, so about 0.93 for measles",
        formula="herd_immunity_threshold",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Assumes homogeneous mixing and sterilising immunity. Real "
            "populations mix assortatively, so outbreaks occur in tight "
            "communities well above the nominal national threshold. The formula "
            "gives a floor, not a target."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Geometric mean titre. The immunogenicity readout used when a full
    #  efficacy trial is impossible, for instance for an annual strain update.
    # -------------------------------------------------------------------------
    Metric(
        name="Geometric mean titre",
        symbol="GMT",
        unit="reciprocal serum dilution",
        typical="platform-specific and assay-specific",
        formula="geometric_mean_titre",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Geometric rather than arithmetic because antibody titres are "
            "log-normally distributed. Titres from different assays are not "
            "comparable without a common international standard."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Seroconversion rate. A regulatory immunogenicity endpoint.
    # -------------------------------------------------------------------------
    Metric(
        name="Seroconversion rate",
        symbol="SCR",
        unit="per cent of subjects reaching a defined titre rise",
        typical="> 70 % for a licensable candidate in adults",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Thresholds are set by regulators per pathogen and per age group, "
            "and are lower in older adults, where the immune response is "
            "weaker."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Number needed to vaccinate. The metric that connects efficacy to public
    #  health value, and the one that shows why a modest efficacy against a
    #  common disease can outperform a high efficacy against a rare one.
    # -------------------------------------------------------------------------
    Metric(
        name="Number needed to vaccinate",
        symbol="NNV",
        unit="people vaccinated per case prevented",
        typical="10 to several thousand, depending on incidence",
        formula="number_needed_to_treat",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Depends on background incidence as much as on efficacy. A vaccine "
            "with 50 % efficacy against a common disease prevents more illness "
            "than one with 95 % efficacy against a rare one."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Cold chain tolerance. A physical property, and the one that decides
    #  whether a dose reaches a rural clinic.
    # -------------------------------------------------------------------------
    Metric(
        name="Storage temperature requirement",
        symbol="T_store",
        unit="degrees Celsius",
        typical="-70 degC to +8 degC depending on platform",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The single largest determinant of whether a vaccine can be used "
            "outside a well-resourced health system. Thermostable formulation "
            "is worth more in the field than a few points of efficacy."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  serial_dilution is included because every titre in this record ultimately
#  comes from one, and a dilution error is the most common source of a wrong
#  immunogenicity number.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "vaccine_efficacy",
    "herd_immunity_threshold",
    "basic_reproduction_number",
    "geometric_mean_titre",
    "number_needed_to_treat",
    "serial_dilution",
    "sensitivity_specificity",
    "relative_risk",
)
