# =============================================================================
#  biotechnology.branches.blue.marine_enzymes.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `white.industrial_enzymes` measures an enzyme as a manufactured article and
#  puts total turnover number first, because durability decides cost. This
#  record deliberately inverts that ordering, and the inversion is the argument.
#
#  THE FIRST TWO METRICS ARE A RATIO AND A TEMPERATURE, and together they
#  define what a cold-adapted enzyme is. Activity at low temperature relative
#  to a mesophilic counterpart says whether the enzyme is genuinely adapted or
#  merely sourced from a cold place, which is a distinction the literature does
#  not always make. Inactivation temperature says how easily it can be
#  destroyed, and in this record that is a DESIRABLE property rather than a
#  weakness.
#
#  A READER COMPARING THIS FACET WITH `white.industrial_enzymes` SHOULD NOTICE
#  that the same physical quantity, thermal stability, is a virtue there and a
#  product feature here in the opposite direction. Nothing about the enzymology
#  differs; the application decides which end of the scale is wanted.
#
#  ONE CAUTION. Enzyme activity is quoted in units defined by an assay, and
#  cold-adapted enzymes are frequently assayed at their own optimum rather than
#  at a common temperature, which flatters the comparison. Where a figure
#  matters, the assay temperature matters equally.
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
    #  WHAT MAKES AN ENZYME GENUINELY COLD-ADAPTED
    # =========================================================================
    Metric(
        name="Relative activity at low temperature",
        symbol="A_rel",
        unit="per cent of maximal activity retained at 5 degrees Celsius",
        typical="30 - 70 % for a genuinely cold-adapted enzyme, against a few "
        "per cent for a mesophilic counterpart",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The measurement that separates a cold-ADAPTED enzyme from an "
            "enzyme merely isolated from a cold place, a distinction the "
            "literature does not always draw. It must be measured against a "
            "mesophilic comparator under the same conditions, since an enzyme "
            "assayed only at its own optimum will always appear excellent."
        ),
    ),
    Metric(
        name="Apparent optimum temperature",
        symbol="T_opt",
        unit="degrees Celsius",
        typical="15 - 30 degrees C for cold-adapted enzymes, and above 90 for "
        "vent-derived thermostable ones",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Apparent rather than true, because at higher temperatures the "
            "measured rate reflects both rising catalysis and accelerating "
            "denaturation. For an unstable enzyme the observed optimum is "
            "therefore an artefact of assay duration: a shorter assay moves it "
            "upwards. The figure is only meaningful with its measurement time "
            "stated."
        ),
    ),
    # =========================================================================
    #  THE PROPERTY THAT IS THE PRODUCT
    # =========================================================================
    Metric(
        name="Inactivation temperature",
        symbol="T_inact",
        unit="degrees Celsius for complete and irreversible loss of activity",
        typical="45 - 65 degrees C for a heat-labile marine enzyme",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "In `white.industrial_enzymes` a low value would be a defect. Here "
            "it is the product: an enzyme destroyed by gentle warming can be "
            "stopped without an inhibitor, without a separation step and "
            "without heating a product to a temperature that damages it. The "
            "requirement is that inactivation be complete and irreversible, "
            "since partial or recoverable inactivation is worthless for the "
            "protocols that rely on this."
        ),
    ),
    Metric(
        name="Melting temperature",
        symbol="T_m",
        unit="degrees Celsius",
        typical="40 - 55 degrees C for psychrophilic enzymes, above 100 for "
        "hyperthermophilic ones",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The unfolding midpoint. The spread across a single record, from "
            "roughly forty to above one hundred degrees, is unusual and "
            "reflects the ocean containing both permanently cold water and "
            "hydrothermal vents. It should not be read as a range for marine "
            "enzymes generally: it is two populations, not one distribution."
        ),
    ),
    # =========================================================================
    #  THE COST OF THAT PROPERTY
    # =========================================================================
    Metric(
        name="Operational half-life",
        symbol="t_half",
        unit="hours of retained activity under process conditions",
        typical="short relative to mesophilic industrial enzymes",
        formula="enzyme_half_life",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The unavoidable cost of the property above, since the same "
            "structural flexibility produces both. It feeds directly into total "
            "turnover number and therefore into cost per unit of product, and "
            "it is why immobilisation appears in this record's technologies as "
            "compensation rather than as optimisation."
        ),
    ),
    Metric(
        name="Activation energy",
        symbol="E_a",
        unit="kilojoules per mole",
        typical="lower for cold-adapted enzymes than for mesophilic "
        "counterparts",
        formula="arrhenius_equation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The physical basis of cold adaptation stated properly. A lower "
            "activation energy means the rate falls off less steeply as "
            "temperature drops, which is what retaining activity in the cold "
            "actually consists of. It is a more fundamental description than "
            "the relative activity figure and harder to measure, which is why "
            "both appear here."
        ),
    ),
    # =========================================================================
    #  THE ORDINARY KINETICS, FOR COMPARABILITY
    # =========================================================================
    Metric(
        name="Turnover number",
        symbol="k_cat",
        unit="per second",
        typical="comparable to or exceeding mesophilic counterparts at low "
        "temperature",
        formula="michaelis_menten",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Quoted here specifically to correct a common misreading. A "
            "cold-adapted enzyme is not slow: at the temperature it evolved "
            "for, it is frequently faster than a mesophilic enzyme would be "
            "there. It is slower only when compared at the mesophilic enzyme's "
            "optimum, which is not a comparison either enzyme was designed for."
        ),
    ),
    Metric(
        name="Specificity constant",
        symbol="k_cat/K_M",
        unit="per molar per second",
        formula="catalytic_efficiency",
        typical="the correct basis for comparing two enzymes at a stated "
        "temperature",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "As in `white.industrial_enzymes`, the ratio rather than either "
            "term is what should be compared. Here it must additionally be "
            "quoted at a stated temperature, because comparing two enzymes each "
            "at its own optimum answers no useful question."
        ),
    ),
    # =========================================================================
    #  TOLERANCE OF THE OTHER MARINE CONSTRAINTS
    # =========================================================================
    Metric(
        name="Salt tolerance",
        symbol="c_salt",
        unit="molar sodium chloride at which activity is retained",
        typical="up to 3 - 4 M for halophilic enzymes, where ordinary proteins "
        "precipitate well below",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Halophilic enzymes are not merely tolerant of salt; several "
            "require it for folding and lose activity in dilute buffer, which "
            "is the reverse of the usual problem. Some are consequently active "
            "in organic solvent, which is an unexpected and useful side effect."
        ),
    ),
    Metric(
        name="Pressure tolerance",
        symbol="p_tol",
        unit="megapascals at which activity is retained",
        typical="up to roughly 100 MPa for piezophilic enzymes, corresponding "
        "to the deepest ocean",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Scientifically interesting and industrially marginal, because few "
            "processes run under pressure and few laboratories own the assay "
            "equipment. Recorded honestly as a capability without a large "
            "market rather than omitted."
        ),
    ),
    # =========================================================================
    #  WHETHER THE PROTEIN CAN BE OBTAINED AT ALL
    # =========================================================================
    Metric(
        name="Soluble expression fraction",
        symbol="f_sol",
        unit="per cent of expressed protein recovered soluble and active",
        typical="frequently low for psychrophilic and piezophilic proteins in "
        "mesophilic hosts",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The practical bottleneck between a sequence and a product in this "
            "record. A protein evolved at four degrees and high pressure "
            "frequently aggregates when made at thirty-seven, so the discovery "
            "rate from sequence mining far exceeds the rate at which working "
            "enzymes are obtained."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  The temperature dependence first, since that is what the record is about.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "arrhenius_equation",
    "enzyme_half_life",
    "michaelis_menten",
    "catalytic_efficiency",
    "thermal_denaturation",
    "q10_temperature_coefficient",
)
