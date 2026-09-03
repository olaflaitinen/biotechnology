# =============================================================================
#  biotechnology.branches.grey.bioremediation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS NOT A RATE. IT IS THE FRACTION THAT CAN BE REACHED AT
#  ALL.
#
#  A degradation rate constant describes how fast the accessible contaminant
#  disappears, and it is the figure the field reports. The bioavailable
#  fraction describes how much of the contaminant is accessible in the first
#  place, and it is what determines where the treatment stops. A site can have
#  an excellent rate constant and an endpoint far above the target, and that
#  combination is the commonest disappointment in the field.
#
#  THE SECOND METRIC IS THE ONE THAT SEPARATES REMEDIATION FROM DILUTION.
#  Concentration falls for two reasons: the contaminant was destroyed, or it
#  spread out. Only one of those is remediation. Compound-specific isotope
#  fractionation distinguishes them, because degradation enriches the heavier
#  isotope in what remains and dilution does not. Without it, a falling
#  concentration is an ambiguous observation, and monitored natural attenuation
#  in particular cannot be justified on concentration data alone.
#
#  A NOTE ON WHAT IS DELIBERATELY ABSENT. There is no metric for metal removal,
#  because there is no metal removal. The metal metrics here measure MOBILITY
#  and PARTITIONING, and they are named to make that unmistakable.
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
    #  HOW MUCH CAN BE REACHED, WHICH DECIDES THE ENDPOINT
    # =========================================================================
    Metric(
        name="Bioavailable fraction",
        symbol="f_bio",
        unit="per cent of total contaminant accessible to organisms",
        typical="falls with contamination age; frequently a minority of the "
        "total at historically contaminated sites",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Placed first because it determines where treatment stops, which "
            "matters more than how fast it gets there. Contaminant sorbed to "
            "organic matter and diffused into intraparticle pores is not "
            "available at any rate constant. It is measured by mild extraction "
            "or by passive samplers rather than by total extraction, and the "
            "difference between the two numbers is the part of the problem "
            "biology cannot address."
        ),
    ),
    Metric(
        name="Sorption coefficient",
        symbol="K_oc",
        unit="litres per kilogram of organic carbon",
        typical="orders of magnitude higher for polycyclic aromatics than for "
        "light hydrocarbons",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Predicts the entry above from the compound and the soil, before "
            "any site work. A high value means the contaminant partitions into "
            "soil organic matter and stays there, which is why the larger "
            "polycyclic aromatics are slow to treat despite being degradable "
            "in a flask."
        ),
    ),
    # =========================================================================
    #  IS IT BEING DESTROYED, OR ONLY SPREAD OUT
    # =========================================================================
    Metric(
        name="Isotopic enrichment factor",
        symbol="epsilon",
        unit="per mille",
        formula="rayleigh_fractionation",
        typical="compound and pathway specific, and established by laboratory "
        "calibration before field use",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The metric that separates remediation from dilution. Degradation "
            "preferentially consumes the lighter isotope, so the remaining "
            "contaminant becomes isotopically heavier; dilution changes "
            "concentration and not isotope ratio. It is the strongest single "
            "line of evidence available, and monitored natural attenuation "
            "cannot honestly be justified without it or an equivalent."
        ),
    ),
    Metric(
        name="First-order degradation rate constant",
        symbol="k",
        unit="per day",
        formula="first_order_decay",
        typical="corresponding to half-lives of days for light hydrocarbons "
        "and years for heavy polycyclic aromatics",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The figure the field reports and it describes only the accessible "
            "fraction. First-order kinetics is an approximation that holds "
            "while contaminant is plentiful and fails as the accessible "
            "fraction is exhausted, which is exactly when a project most needs "
            "a prediction."
        ),
    ),
    Metric(
        name="Half-life in the field",
        symbol="t_half",
        unit="days to years",
        typical="commonly an order of magnitude longer than the same compound "
        "in a laboratory microcosm",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The gap between laboratory and field is the entire subject of this "
            "facet's first two entries. A microcosm has the contaminant in "
            "suspension, mixed, at a controlled temperature, with nutrients "
            "sufficient. A site has none of those. Quoting a laboratory "
            "half-life as a field expectation is the field's commonest "
            "overstatement."
        ),
    ),
    # =========================================================================
    #  ARE THE ORGANISMS THERE, AND ARE THEY WORKING
    # =========================================================================
    Metric(
        name="Functional gene abundance",
        symbol="N_gene",
        unit="gene copies per gram of soil or per litre of groundwater",
        typical="detection of the relevant degradation genes is a prerequisite "
        "rather than a demonstration",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Establishes that the capability is present, which is the question "
            "biostimulation assumes and bioaugmentation denies. It does not "
            "establish that the genes are being expressed or that degradation "
            "is occurring, so it belongs alongside the isotope evidence rather "
            "than instead of it."
        ),
    ),
    Metric(
        name="Electron acceptor availability",
        symbol="c_EA",
        unit="milligrams per litre of oxygen, nitrate, sulphate or their "
        "reduced products",
        typical="dissolved oxygen below about 1 mg/L indicates aerobic "
        "degradation is limited",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "What aerobic degradation runs out of first, and the target of most "
            "biostimulation. The pattern of acceptors consumed and products "
            "accumulated across a plume is a geochemical footprint that "
            "corroborates degradation independently of the contaminant "
            "measurements."
        ),
    ),
    # =========================================================================
    #  IS THE PLUME WINNING OR LOSING
    # =========================================================================
    Metric(
        name="Plume stability",
        symbol="dL/dt",
        unit="metres of plume front movement per year",
        typical="a stable or receding plume is the criterion for monitored "
        "natural attenuation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The condition under which measuring and waiting is a defensible "
            "intervention rather than an evasion. If degradation exceeds "
            "migration the plume stops advancing, and the question becomes "
            "whether anyone is exposed in the interval rather than whether "
            "anything is happening."
        ),
    ),
    Metric(
        name="Time to remediation target",
        symbol="t_target",
        unit="years",
        typical="months to decades, and frequently longer than the initial "
        "estimate",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The number that decides against biology as often as cost decides "
            "for it. It is systematically underestimated, because projections "
            "extrapolate the early rapid phase into the asymptotic one. A "
            "property transaction or a regulatory deadline that does not "
            "accommodate this will select a physical method regardless of the "
            "biology."
        ),
    ),
    # =========================================================================
    #  WHAT IT COSTS, WHICH IS WHY THE FIELD EXISTS
    # =========================================================================
    Metric(
        name="Cost per cubic metre treated",
        symbol="C_m3",
        unit="euro per cubic metre",
        typical="substantially below excavation and disposal for in situ "
        "biological treatment",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The whole commercial argument, and the reason contaminated sites "
            "get treated rather than fenced. It must be compared on a "
            "like-for-like basis including monitoring over the treatment "
            "period, which for a decade-long project is not a small addition."
        ),
    ),
    # =========================================================================
    #  METALS: MOBILITY AND PARTITIONING, NOT REMOVAL
    # =========================================================================
    Metric(
        name="Metal leachability",
        symbol="L_metal",
        unit="milligrams per litre in a standard leaching test",
        typical="the endpoint for immobilisation treatments",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Named for what it measures. An immobilisation treatment is judged "
            "by whether the metal leaches, not by whether it is gone, because "
            "it is not gone. A successful result means the metal remains in "
            "place in a less mobile form and continues to require monitoring."
        ),
    ),
    Metric(
        name="Metal partitioning into biomass",
        symbol="f_part",
        unit="per cent of metal transferred into harvestable biomass",
        typical="the endpoint for biosorption and accumulation approaches",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Also named for what it measures. The metal has moved from a "
            "diffuse matrix into a concentrated one, which is genuinely useful "
            "because a small volume of contaminated biomass is easier to manage "
            "than a large volume of contaminated soil. It is concentration "
            "rather than destruction, and the biomass is now the problem."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Transport and kinetics, then the evidence relationships.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "first_order_decay",
    "monod_equation",
    "rayleigh_fractionation",
    "sorption_isotherm",
    "advection_dispersion",
    "mass_balance",
)
