# =============================================================================
#  biotechnology.branches.grey.phytoremediation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE HEADLINE NUMBER IN THIS FIELD IS THE BIOCONCENTRATION FACTOR, AND ON
#  ITS OWN IT PREDICTS ALMOST NOTHING.
#
#  A hyperaccumulator with a spectacular concentration factor and a hundred
#  grams of tissue removes less metal than an ordinary plant with a modest
#  factor and ten tonnes of tissue. What is removed is a PRODUCT:
#
#      annual removal = tissue concentration x harvestable biomass
#
#  So the first metric here is the product and not either factor, which is the
#  opposite of how the literature reports it. The individual factors follow,
#  labelled as the components they are.
#
#  THE SECOND ORGANISING IDEA IS THAT THE DENOMINATOR IS ENORMOUS. A hectare
#  of soil to plough depth is on the order of a few thousand tonnes. Removing
#  kilograms per hectare per year from that mass is what makes the timescale
#  decades, and stating the mass balance explicitly is more useful than any
#  optimistic rate.
#
#  A THIRD POINT. Metrics for the containment applications are NOT the same
#  metrics. Transpiration and capture zone measure whether a plume stopped
#  moving; no extraction is claimed or occurring. They are grouped separately
#  so the two are not read as one performance.
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
    #  WHAT ACTUALLY LEAVES THE SITE, WHICH IS A PRODUCT
    # =========================================================================
    Metric(
        name="Annual metal removal per hectare",
        symbol="M_annual",
        unit="kilograms of metal per hectare per year",
        formula="mass_balance",
        typical="kilograms rather than tonnes, against a soil mass of "
        "thousands of tonnes per hectare",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Placed first because it is the only extraction figure that means "
            "anything on its own. It is the product of tissue concentration and "
            "harvestable biomass, so a spectacular accumulator with little "
            "tissue and an ordinary plant with a great deal of tissue can "
            "arrive at the same number. The literature reports the two factors "
            "separately far more often than it reports this."
        ),
    ),
    Metric(
        name="Time to reach the cleanup target",
        symbol="t_clean",
        unit="years",
        typical="years for lightly contaminated soil, decades or longer for "
        "heavily contaminated soil",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The entry above divided into the mass that has to be removed, and "
            "the number that decides whether phytoextraction is a candidate. It "
            "assumes a constant rate, which is optimistic: the readily "
            "available fraction is taken up first and the rate declines, for "
            "the same bioavailability reasons `grey.bioremediation` sets out. A "
            "projection that ignores that will be too short."
        ),
    ),
    # =========================================================================
    #  THE TWO COMPONENTS, LABELLED AS COMPONENTS
    # =========================================================================
    Metric(
        name="Bioconcentration factor",
        symbol="BCF",
        unit="ratio of metal concentration in tissue to concentration in soil",
        typical="around or below one for most species; greater than one is the "
        "defining property of a hyperaccumulator",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The field's headline number and half of an answer. A ratio above "
            "one means the plant concentrates the metal relative to the soil, "
            "which is genuinely remarkable and is not by itself a removal rate. "
            "It is reported without the biomass term more often than with it, "
            "which is how the field acquired its reputation for optimism."
        ),
    ),
    Metric(
        name="Harvestable biomass yield",
        symbol="Y_bio",
        unit="tonnes of dry above-ground biomass per hectare per year",
        typical="low for most hyperaccumulators, high for fast-growing trees "
        "and crops that accumulate little",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The other half, and the source of the field's central trade. The "
            "species that concentrate best are typically small and slow, and "
            "the species that produce the most tissue typically concentrate "
            "least. Only above-ground biomass counts, because roots are not "
            "harvested and their contents stay in the ground."
        ),
    ),
    Metric(
        name="Translocation factor",
        symbol="TF",
        unit="ratio of shoot concentration to root concentration",
        typical="greater than one in useful extraction species",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Determines whether uptake becomes removal. A plant that takes up a "
            "great deal of metal and holds it in the roots has moved the metal "
            "a few centimetres. Only what reaches the shoot can be cut and "
            "carried away. A low value is the signature of a stabilisation "
            "species, which is a virtue in that role."
        ),
    ),
    # =========================================================================
    #  HOW MUCH OF THE SOIL METAL IS AVAILABLE AT ALL
    # =========================================================================
    Metric(
        name="Phytoavailable metal fraction",
        symbol="f_avail",
        unit="per cent of total soil metal in plant-available form",
        typical="a minority of the total, and dependent on pH and organic "
        "matter",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The same limit that governs `grey.bioremediation`, appearing here "
            "in mineral form. Metal bound in mineral lattices or strongly "
            "sorbed is not available to roots at any rate, which is why an "
            "extraction slows as the available pool is depleted and why total "
            "soil concentration overstates what can be removed."
        ),
    ),
    Metric(
        name="Rooting depth",
        symbol="z_root",
        unit="metres",
        typical="under a metre for most herbaceous species, several metres for "
        "deep-rooted trees",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The hard scope boundary of the entire record. Contamination below "
            "the root zone is not treated slowly, it is not treated. This is "
            "the single figure that determines whether phytoremediation is even "
            "a candidate at a site, and it should be checked before any of the "
            "metrics above."
        ),
    ),
    # =========================================================================
    #  THE CONTAINMENT APPLICATIONS, WHICH MEASURE SOMETHING ELSE ENTIRELY
    # =========================================================================
    Metric(
        name="Transpiration rate",
        symbol="E_t",
        unit="litres per tree per day, or millimetres per hectare per day",
        typical="substantial for mature poplar and willow in the growing "
        "season, and effectively zero in dormancy",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The basis of hydraulic control, and no extraction is claimed by "
            "it. The trees drink enough water to draw the water table down and "
            "hold the plume. The seasonal collapse to near zero in dormancy is "
            "the design problem: a containment that works for eight months of "
            "the year is a containment with a gap in it."
        ),
    ),
    Metric(
        name="Capture zone width",
        symbol="w_cap",
        unit="metres of plume width controlled by the planting",
        typical="determined by transpiration against groundwater flux",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The engineering output of the entry above and what a hydraulic "
            "control design is actually sized on. It is a containment "
            "specification of the same kind a pump and treat system would be "
            "given, delivered by trees at a small fraction of the operating "
            "cost."
        ),
    ),
    # =========================================================================
    #  WHAT IT COSTS, AND WHAT IT LEAVES BEHIND
    # =========================================================================
    Metric(
        name="Cost per hectare treated",
        symbol="C_ha",
        unit="euro per hectare",
        typical="a small fraction of any engineered alternative, which is the "
        "entire commercial argument",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Why the technique exists. It is only a fair comparison if it "
            "includes the years of monitoring, the harvest operations and the "
            "biomass disposal below, and a figure that omits those describes "
            "planting rather than remediation."
        ),
    ),
    Metric(
        name="Contaminated biomass produced",
        symbol="M_waste",
        unit="tonnes of contaminated harvest per hectare per year",
        typical="proportional to the biomass yield, and hazardous where the "
        "extraction succeeded",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Deliberately included as a metric rather than as a footnote, "
            "because a successful extraction produces this by definition. The "
            "better the removal, the more contaminated waste there is to "
            "manage. Combustion reduces the volume and concentrates the metal "
            "into ash, so it changes the form of the problem rather than "
            "ending it."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Mass balance first, because the record is an accounting problem.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "mass_balance",
    "bioconcentration_factor",
    "first_order_decay",
    "darcy_law",
    "sorption_isotherm",
)
