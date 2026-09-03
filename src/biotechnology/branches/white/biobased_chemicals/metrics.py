# =============================================================================
#  biotechnology.branches.white.biobased_chemicals.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The first metric in this facet is unusual: it is a property of the TARGET
#  MOLECULE rather than of the process, and it is placed first because it
#  predicts the answer before any process exists.
#
#  The oxygen to carbon ratio of the desired product, compared with that of the
#  feedstock, says whether a biological route is structurally favoured. Sugar
#  sits near one oxygen per carbon. A target near that ratio can be reached
#  with little rearrangement. A hydrocarbon target at zero requires stripping
#  every oxygen out, which costs carbon and energy. Checking this ratio takes a
#  minute and has more predictive power about commercial outcome than a year of
#  strain improvement.
#
#  After that come the economics, which decide projects, and only then the
#  environmental measures, which justify them. That ordering is deliberate and
#  is the honest description of how the field actually operates: no biobased
#  chemical has ever been commercialised because its life cycle assessment was
#  good, and many have been abandoned despite it.
#
#  Fermentation performance metrics are NOT repeated here. They belong to
#  `white.metabolic_engineering` and `white.microbial_fermentation`, and
#  duplicating them would blur three records.
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
    #  THE PROPERTY OF THE TARGET THAT PREDICTS THE ANSWER
    # =========================================================================
    Metric(
        name="Oxygen to carbon ratio of the target",
        symbol="O/C",
        unit="moles of oxygen per mole of carbon, dimensionless",
        typical="about 1.0 for glucose; 0.5 - 1.0 for acids and diols; 0 for "
        "hydrocarbons",
        formula="degree_of_reduction",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The single most predictive number in this record and a property of "
            "the molecule rather than the process. A target whose ratio is near "
            "the feedstock's needs little rearrangement, so biology starts most "
            "of the way there. A hydrocarbon target requires removing every "
            "oxygen, which wastes carbon as carbon dioxide. This ratio explains "
            "why lactic acid and the diols succeeded and why bio-based olefins "
            "and aromatics have not."
        ),
    ),
    Metric(
        name="Degree of reduction of the product",
        symbol="gamma",
        unit="available electrons per carbon, dimensionless",
        typical="4.0 for glucose; higher for reduced products such as alcohols "
        "and hydrocarbons",
        formula="degree_of_reduction",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The rigorous form of the entry above. It sets the maximum carbon "
            "yield achievable from a given feedstock by electron balance alone, "
            "independent of any pathway, and it is how a process chemist "
            "establishes the ceiling before choosing an organism."
        ),
    ),
    Metric(
        name="Carbon yield from feedstock",
        symbol="Y_C",
        unit="moles of product carbon per mole of feedstock carbon",
        typical="0.3 - 0.9 Cmol/Cmol depending on how reduced the target is",
        formula="theoretical_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The dominant term in the cost of a bulk biobased chemical, because "
            "feedstock is the largest single input. It should always be quoted "
            "against the electron-balance maximum rather than alone, for the "
            "same reason given in `white.metabolic_engineering`: the absolute "
            "number is uninterpretable without its ceiling."
        ),
    ),
    # =========================================================================
    #  WHAT DECIDES WHETHER THE PLANT IS BUILT
    # =========================================================================
    Metric(
        name="Minimum selling price",
        symbol="MSP",
        unit="euro per tonne of product",
        typical="compared directly against the prevailing petrochemical price",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The output of a techno-economic model and the number that funds or "
            "kills a project years before a plant exists. It is a moving target "
            "rather than a property of the process, because the benchmark it is "
            "compared against is a petrochemical price set by an oil market "
            "nobody in this field controls."
        ),
    ),
    Metric(
        name="Capital intensity",
        symbol="C_capex",
        unit="euro of capital per annual tonne of capacity",
        typical="substantially higher than for an equivalent petrochemical "
        "plant",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Dilute aqueous processing needs large vessels and large separation "
            "trains for a given output. Combined with the need to build before "
            "any revenue exists, this is why so many companies in "
            "`history.py` reached commercial operation and still failed: the "
            "plant was financed against a price forecast that did not hold."
        ),
    ),
    Metric(
        name="Separation cost share",
        symbol="f_sep",
        unit="per cent of operating cost attributable to product recovery",
        typical="frequently the largest single share for a bulk product",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The number that surprises newcomers. Getting a dilute molecule out "
            "of water can cost more than making it, which is why titre matters "
            "commercially far beyond what the fermentation itself would "
            "suggest, and why in situ product removal appears in "
            "`practice.TECHNOLOGIES` as an economic measure rather than a "
            "biological one."
        ),
    ),
    Metric(
        name="Salt burden of acid recovery",
        symbol="m_salt",
        unit="tonnes of salt by-product per tonne of acid",
        typical="approaching or exceeding one tonne per tonne for classical "
        "neutralisation routes",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "An unglamorous and genuine environmental burden specific to "
            "organic acid fermentation. The organism prefers a pH at which the "
            "acid is ionised, so recovery by neutralisation generates "
            "stoichiometric salt. Electrodialysis and low-pH tolerant strains "
            "exist to avoid it, and a life cycle assessment that omits it is "
            "incomplete."
        ),
    ),
    # =========================================================================
    #  WHAT JUSTIFIES IT
    # =========================================================================
    Metric(
        name="Biobased carbon content",
        symbol="f_bio",
        unit="per cent of total carbon that is recently fixed",
        typical="0 - 100 %, and measurable to within a few per cent",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "One of the very few claims in this branch that can be verified "
            "analytically on the finished product rather than audited through "
            "the supply chain. Radiocarbon has decayed away in fossil carbon and "
            "is present in recently fixed carbon, so the measurement is "
            "physical. Contrast this with `white.biofuels`, where sustainability "
            "compliance must be audited because the fuel carries no such "
            "evidence."
        ),
    ),
    Metric(
        name="Cradle-to-gate greenhouse gas intensity",
        symbol="GWP",
        unit="kilograms of carbon dioxide equivalent per kilogram of product",
        typical="compared against the incumbent route, and not always lower",
        formula="carbon_intensity",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The honest form of the environmental claim. A biobased route with "
            "high energy demand, dilute processing and agricultural feedstock "
            "can exceed the petrochemical route it replaces, and the reduction "
            "should always be stated against a named benchmark rather than "
            "asserted in the abstract."
        ),
    ),
    Metric(
        name="Process mass intensity",
        symbol="PMI",
        unit="kilograms of input per kilogram of product",
        typical="dominated by water for fermentation routes",
        formula="process_mass_intensity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Comparable to the same symbol in `white.biocatalysis` and much "
            "smaller than in `white.bioprocess_engineering`, where the product "
            "is a protein at very low concentration. The three values together "
            "show how much the concentration of the target governs everything "
            "downstream of it."
        ),
    ),
    Metric(
        name="Fossil resource displacement",
        symbol="D_fossil",
        unit="kilograms of fossil feedstock avoided per kilogram of product",
        typical="near one for a true drop-in replacement",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Records the point that distinguishes this record from "
            "`white.biofuels`: carbon that ends up in a material is displaced "
            "permanently rather than burned, so the same hectare of land "
            "displaces considerably more fossil carbon making a chemical than "
            "making a fuel."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  The balance relationships that set the ceiling, then the assessment ones.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "degree_of_reduction",
    "theoretical_yield",
    "product_yield",
    "atom_economy",
    "mass_balance",
    "carbon_intensity",
    "process_mass_intensity",
    "e_factor",
    "life_cycle_impact",
)
