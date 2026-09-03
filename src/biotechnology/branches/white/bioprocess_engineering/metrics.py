# =============================================================================
#  biotechnology.branches.white.bioprocess_engineering.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This facet is organised to make the scale-up paradox visible rather than to
#  assert it. The first four metrics are the four quantities an engineer would
#  like to hold constant when a vessel gets larger, and their notes state, one
#  by one, what happens to the others when each is fixed.
#
#  A reader who works through those four entries in order will see the
#  contradiction assemble itself: preserving turbulence intensity raises tip
#  speed, preserving tip speed collapses transfer, preserving mixing time
#  demands power that no motor can deliver. There is no arrangement in which
#  all four survive.
#
#  After that come the downstream metrics, and the most important of them is
#  the one that looks trivial. Overall yield is the product of step yields, and
#  that single multiplication does more to shape process design than any
#  transport correlation.
#
#  A NOTE ON UNITS. Power per unit volume is given in watts per cubic metre
#  because that is the working unit in the field; readers accustomed to
#  horsepower per thousand gallons should convert before comparing.
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
    #  THE FOUR THAT CANNOT ALL BE HELD CONSTANT
    # =========================================================================
    Metric(
        name="Power input per unit volume",
        symbol="P/V",
        unit="watts per cubic metre",
        typical="500 - 5000 W/m3 for microbial culture, 10 - 100 W/m3 for "
        "animal cell culture",
        formula="power_per_volume",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The most common scale-up criterion, because it approximately "
            "preserves turbulence intensity and therefore oxygen transfer. "
            "Holding it constant forces impeller tip speed UP as the vessel "
            "grows, so a shear-sensitive culture is punished by exactly the "
            "choice that protects its oxygen supply. This is the first half of "
            "the paradox."
        ),
    ),
    Metric(
        name="Impeller tip speed",
        symbol="v_tip",
        unit="metres per second",
        typical="2 - 8 m/s for microbial, below 2 m/s for shear-sensitive "
        "cultures",
        formula="impeller_tip_speed",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The proxy for maximum local shear at the impeller. Holding it "
            "constant instead protects fragile cells and causes power per "
            "volume to FALL sharply with scale, which collapses oxygen "
            "transfer. That is the second half of the paradox: the two "
            "criteria pull in opposite directions and only one can be kept."
        ),
    ),
    Metric(
        name="Volumetric oxygen transfer coefficient",
        symbol="kLa",
        unit="per hour",
        typical="50 - 500 h^-1, and harder to sustain as volume rises",
        formula="oxygen_transfer_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Here it is a capability of the equipment; in "
            "`white.microbial_fermentation` the paired oxygen uptake rate is a "
            "demand of the organism, and a process works when this exceeds "
            "that. Holding kLa constant on scale-up is sometimes possible by "
            "raising pressure or oxygen enrichment rather than agitation, which "
            "is why those measures exist."
        ),
    ),
    Metric(
        name="Mixing time",
        symbol="t_m",
        unit="seconds to reach a stated degree of homogeneity",
        typical="5 - 10 s at laboratory scale, 30 - 200 s in large vessels",
        formula="mixing_time",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The criterion nobody can hold constant. Preserving laboratory "
            "mixing time in a large vessel would require power inputs far "
            "beyond what is mechanically or thermally feasible, so mixing time "
            "always lengthens with scale. The consequence is the gradient "
            "problem: a cell circulating through a large tank experiences "
            "changing conditions rather than the average, and it responds to "
            "the transit."
        ),
    ),
    # =========================================================================
    #  DESCRIBING THE REGIME RATHER THAN THE VESSEL
    # =========================================================================
    Metric(
        name="Impeller Reynolds number",
        symbol="Re_i",
        unit="dimensionless",
        typical="above 10^4 for fully turbulent operation",
        formula="reynolds_number",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Distinguishes flow regimes so that correlations derived on one "
            "vessel can be applied to another. It is also the honest warning "
            "against extrapolation: a correlation fitted in the turbulent "
            "regime says nothing about a viscous fungal broth that has drifted "
            "into transitional flow as it thickened."
        ),
    ),
    # =========================================================================
    #  THE MULTIPLICATION THAT SHAPES EVERY PROCESS
    # =========================================================================
    Metric(
        name="Overall process yield",
        symbol="Y_overall",
        unit="per cent of product formed that reaches the final container",
        typical="30 - 70 % for a multi-step biological purification",
        formula="overall_step_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The single most consequential number in this record. Because it "
            "is the PRODUCT of step yields, ten steps at ninety per cent give "
            "thirty-five per cent, not ninety. Removing an operation is "
            "therefore usually worth more than improving one, which is why the "
            "field pursues fewer steps rather than better steps, and why a "
            "titre improvement upstream can be worth less than a step deleted "
            "downstream."
        ),
    ),
    Metric(
        name="Step yield",
        symbol="Y_step",
        unit="per cent recovered across one unit operation",
        typical="85 - 98 % for a well-developed step",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Read only in the context of the entry above. A step at ninety-five "
            "per cent sounds excellent and, repeated ten times, still loses "
            "forty per cent of the product."
        ),
    ),
    # =========================================================================
    #  WHAT THE DOWNSTREAM TRAIN COSTS
    # =========================================================================
    Metric(
        name="Dynamic binding capacity",
        symbol="DBC",
        unit="grams of product per litre of resin at a stated residence time",
        typical="30 - 70 g/L for modern affinity resins",
        formula="dynamic_binding_capacity",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Sizes the capture column and therefore a major consumable cost. "
            "It must be quoted with the residence time, since capacity falls "
            "as flow rises, and a capacity measured at leisure does not "
            "survive a production flow rate."
        ),
    ),
    Metric(
        name="Resin lifetime",
        symbol="N_cycles",
        unit="purification cycles before replacement",
        typical="50 - 300 cycles",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Divides the resin cost across batches and is validated rather "
            "than assumed, because carryover and capacity loss must both be "
            "shown to stay within limits over the claimed lifetime."
        ),
    ),
    Metric(
        name="Buffer consumption ratio",
        symbol="B_ratio",
        unit="litres of buffer per gram of purified product",
        typical="hundreds to thousands of litres per gram",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The constraint that most often sizes a facility, and the one least "
            "often mentioned outside it. Buffer preparation, hold vessels and "
            "floor space frequently exceed the requirements of the bioreactor, "
            "which is why in-line dilution and buffer concentrates are pursued."
        ),
    ),
    Metric(
        name="Process mass intensity",
        symbol="PMI",
        unit="kilograms of total input per kilogram of product",
        typical="in the thousands for a therapeutic protein, dominated by water",
        formula="process_mass_intensity",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Far higher than for small molecule chemistry, and the difference "
            "is almost entirely water. Recording it prevents a false comparison "
            "with `white.biocatalysis`, where the same symbol describes a much "
            "smaller number for a different kind of process."
        ),
    ),
    # =========================================================================
    #  WHETHER THE ASSET IS EARNING
    # =========================================================================
    Metric(
        name="Facility utilisation",
        symbol="U_fac",
        unit="per cent of available operating time in productive use",
        typical="40 - 80 %",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Cleaning, sterilising, changeover, testing and release are not "
            "production but occupy the plant. Single-use equipment and ballroom "
            "designs are adopted largely to raise this number rather than to "
            "improve any individual operation."
        ),
    ),
    Metric(
        name="Viral clearance factor",
        symbol="LRV",
        unit="log10 reduction value, summed across orthogonal steps",
        typical="a total above 12 log10 expected for a mammalian cell product",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Each step is validated separately with a deliberately spiked "
            "challenge, and only steps that clear by different mechanisms may "
            "be added together. It is one of the few places where a "
            "manufacturing process must prove it removes something that is "
            "probably not there."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  The scale-up group first, matching the ordering of the metrics, then the
#  downstream and accounting relationships.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "power_per_volume",
    "impeller_tip_speed",
    "reynolds_number",
    "mixing_time",
    "oxygen_transfer_rate",
    "overall_step_yield",
    "dynamic_binding_capacity",
    "residence_time",
    "process_mass_intensity",
    "mass_balance",
)
