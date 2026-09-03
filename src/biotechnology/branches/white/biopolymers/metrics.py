# =============================================================================
#  biotechnology.branches.white.biopolymers.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The first two metrics are the two independent axes of `narrative.py`, and
#  placing them first, adjacent, is the point of this facet. A reader who takes
#  in that biobased carbon content and degree of mineralisation are separate
#  measurements, made by different methods, answering different questions, has
#  the record's central idea.
#
#  THE MINERALISATION ENTRY CARRIES THE HARDEST WARNING IN THIS RECORD. A
#  biodegradation figure is meaningless without its test conditions, and the
#  same material honestly reports ninety per cent under one standard and
#  essentially zero under another. Anyone quoting a single number without the
#  environment, the temperature and the duration is either careless or selling
#  something.
#
#  A SEPARATE WARNING BELONGS BESIDE IT: DISINTEGRATION IS NOT BIODEGRADATION.
#  A material can pass a disintegration test by breaking into fragments small
#  enough to fall through a sieve while mineralising almost nothing. That is
#  not degradation, it is microplastic formation, and it is precisely what got
#  oxo-degradable additives restricted. The two are recorded as separate
#  metrics so they cannot be confused.
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
    #  THE TWO INDEPENDENT AXES
    # =========================================================================
    Metric(
        name="Biobased carbon content",
        symbol="f_bio",
        unit="per cent of total carbon that is recently fixed",
        typical="0 - 100 %; about 30 % for partly bio-based PET, 100 % for "
        "polylactic acid",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Axis one: where the carbon came from. Measured by radiocarbon on "
            "the finished article, so it is a physical determination rather "
            "than an audit. It says NOTHING about end of life: a fully "
            "biobased polyethylene is as persistent as any plastic."
        ),
    ),
    Metric(
        name="Degree of mineralisation",
        symbol="D_min",
        unit="per cent of organic carbon converted to carbon dioxide under a "
        "named test",
        typical="90 % within 180 days at 58 degrees C for industrial "
        "compostability; the same material may reach near zero in soil or "
        "seawater",
        formula="mineralisation_degree",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Axis two: what happens at the end, and independent of axis one. "
            "The figure is meaningless without its environment, temperature and "
            "duration, because those are what the test measures. Polylactic "
            "acid passes industrial composting and effectively fails home "
            "compost, soil and marine tests; polyhydroxyalkanoates pass all "
            "four. A single unqualified percentage is not a specification."
        ),
    ),
    Metric(
        name="Disintegration",
        symbol="D_dis",
        unit="per cent of mass passing a 2 millimetre sieve after a defined "
        "period",
        typical="90 % within 12 weeks for industrial compostability",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Recorded as a SEPARATE metric precisely so it is not mistaken for "
            "the one above. Disintegration measures breaking into pieces; "
            "mineralisation measures being consumed. A material can pass this "
            "and fail that, and when it does, what has been produced is "
            "microplastic. This distinction is what the oxo-degradable "
            "restriction in `history.py` turned on."
        ),
    ),
    # =========================================================================
    #  WHETHER THE MATERIAL CAN BE MADE AND USED
    # =========================================================================
    Metric(
        name="Weight average molecular weight",
        symbol="M_w",
        unit="grams per mole",
        typical="100000 - 300000 g/mol for a structural polyester",
        formula="molecular_weight_average",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Determines whether the material has useful mechanical properties "
            "at all. It is also fragile here in a way it is not for polyolefins: "
            "biopolyesters hydrolyse in the melt if the resin is not thoroughly "
            "dried, so molecular weight can be lost during processing rather "
            "than during synthesis."
        ),
    ),
    Metric(
        name="Glass transition temperature",
        symbol="T_g",
        unit="degrees Celsius",
        typical="about 60 degrees C for polylactic acid, near or below ambient "
        "for several polyhydroxyalkanoates",
        formula="glass_transition",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The practical limit on service temperature, and the reason an "
            "untreated polylactic acid cup deforms in a hot drink. Raising "
            "usable heat resistance is done by increasing crystallinity rather "
            "than by changing this value, which is why the crystallinity entry "
            "below matters commercially."
        ),
    ),
    Metric(
        name="Degree of crystallinity",
        symbol="X_c",
        unit="per cent",
        typical="0 - 60 % depending on stereochemistry and thermal history",
        formula="crystallinity_degree",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Controlled in polylactic acid through the ratio of the two lactic "
            "acid isomers in the feed, which is a direct link back to the "
            "fermentation in `white.biobased_chemicals`. It cuts both ways: "
            "crystallinity buys heat resistance and slows hydrolysis, so the "
            "same change that makes a cup usable makes it compost more slowly."
        ),
    ),
    Metric(
        name="Oxygen transmission rate",
        symbol="OTR",
        unit="cubic centimetres per square metre per day at stated thickness, "
        "temperature and humidity",
        typical="poorer than the incumbent polymers for most biopolymers",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Barrier performance is where biopolymers most often lose a "
            "packaging application, because inadequate barrier shortens shelf "
            "life and food waste outweighs packaging impact in most life cycle "
            "studies. The conditions must be quoted, since humidity strongly "
            "affects the barrier of hydrophilic materials such as starch."
        ),
    ),
    # =========================================================================
    #  THE POLYHYDROXYALKANOATE-SPECIFIC ECONOMICS
    # =========================================================================
    Metric(
        name="Polymer content of dry cell mass",
        symbol="f_PHA",
        unit="per cent of dry cell weight accumulated as polymer",
        typical="60 - 85 % in a well-performing accumulation",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Specific to polymers stored inside cells, and the number that "
            "governs their cost. A high polymer fraction means less cell mass "
            "to remove per kilogram of product, so this single figure largely "
            "determines the recovery cost that has kept an environmentally "
            "excellent material in niche use."
        ),
    ),
    Metric(
        name="Recovery yield of extracted polymer",
        symbol="Y_rec",
        unit="per cent of accumulated polymer recovered at specification",
        typical="80 - 95 %",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Extraction must remove the cell without degrading the polymer, and "
            "solvent-based routes trade recovery against solvent inventory and "
            "molecular weight loss. It is the step at which a promising "
            "fermentation becomes an expensive product."
        ),
    ),
    # =========================================================================
    #  WHAT THE MATERIAL COSTS THE WORLD
    # =========================================================================
    Metric(
        name="Cradle-to-gate greenhouse gas intensity",
        symbol="GWP",
        unit="kilograms of carbon dioxide equivalent per kilogram of polymer",
        typical="often lower than the fossil equivalent, and not always",
        formula="carbon_intensity",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Highly sensitive to how biogenic carbon and end-of-life are "
            "accounted for, and those conventions must be declared for two "
            "figures to be comparable. Composting returns the carbon to the "
            "atmosphere within months while a durable article retains it, so "
            "the end-of-life assumption can change the ranking."
        ),
    ),
    Metric(
        name="Land and water footprint of feedstock",
        symbol="F_ag",
        unit="hectares and cubic metres per tonne of polymer",
        typical="material for crop-derived polymers, near zero for waste-derived",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The term most often omitted from a favourable comparison. "
            "Eutrophication and land use frequently move in the opposite "
            "direction to greenhouse gas intensity, which is why a single-issue "
            "carbon comparison is not an environmental assessment."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  The end-of-life measure first, matching the facet's emphasis, then the
#  material characterisation, then the assessment.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "mineralisation_degree",
    "molecular_weight_average",
    "degree_of_polymerisation",
    "glass_transition",
    "crystallinity_degree",
    "permeability_coefficient",
    "carbon_intensity",
    "life_cycle_impact",
)
