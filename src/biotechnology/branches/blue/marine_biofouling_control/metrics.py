# =============================================================================
#  biotechnology.branches.blue.marine_biofouling_control.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS NOT ABOUT FOULING. It is added drag, because that is
#  what fouling costs and what the entire industry exists to prevent. A facet
#  that opened with settlement counts would describe the biology and miss the
#  reason anyone pays for this.
#
#  THE MOST IMPORTANT PAIR IN THIS FACET IS THE THIRD AND FOURTH ENTRIES, and
#  they should be read together. Efficacy and environmental concentration are
#  separate axes, and the record's central historical lesson is that a
#  technology can score outstandingly on one and unacceptably on the other.
#  Tributyltin did. Presenting efficacy without the environmental figure is
#  precisely the error that took decades to correct.
#
#  A WARNING ABOUT SETTLEMENT ASSAYS. Laboratory settlement inhibition is the
#  most commonly reported number in this field and correlates poorly with
#  multi-year field performance. A surface that halves barnacle settlement in a
#  fourteen-day assay may foul completely in a season, because the assay uses
#  one species under constant conditions and a hull meets a succession of them
#  under varying ones. The metric below carries that caution.
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
    #  WHAT FOULING ACTUALLY COSTS
    # =========================================================================
    Metric(
        name="Added frictional resistance",
        symbol="dC_F",
        unit="per cent increase in frictional drag relative to a clean hull",
        typical="a few per cent for a biofilm, and very large for heavy "
        "calcareous fouling",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The quantity the industry exists to prevent, and the reason this "
            "facet opens here rather than with settlement counts. Even a slime "
            "layer of negligible mass raises drag measurably, which is why the "
            "biofilm stage matters out of proportion to how little of it there "
            "is. Frictional resistance dominates total resistance for a large "
            "slow vessel, so the effect on fuel is close to proportional."
        ),
    ),
    Metric(
        name="Excess fuel consumption",
        symbol="dF",
        unit="per cent increase in fuel burned for the same speed and "
        "distance",
        typical="follows added resistance closely, and accumulates over the "
        "interval between cleanings",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The commercial and the climate figure at once. Because most world "
            "trade moves by sea, a small percentage across a fleet is a large "
            "absolute quantity of fuel and emissions, which is the basis of "
            "this record's claim to be an environmental technology filed under "
            "marine paint."
        ),
    ),
    # =========================================================================
    #  THE PAIR THAT MUST BE READ TOGETHER
    # =========================================================================
    Metric(
        name="Fouling rating after field immersion",
        symbol="R_foul",
        unit="percentage of surface covered, by fouling type, after a stated "
        "immersion period",
        typical="assessed on static panels and on service hulls over months "
        "to years",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The efficacy axis, and it must be reported by fouling type rather "
            "than as a single coverage figure, since slime, weed and calcareous "
            "fouling have very different consequences for drag. A coating that "
            "prevents barnacles and permits heavy slime is not equivalent to "
            "one that prevents both."
        ),
    ),
    Metric(
        name="Predicted environmental concentration",
        symbol="PEC",
        unit="micrograms or nanograms per litre in the receiving water",
        typical="modelled for harbours and marinas, where exchange is poor and "
        "vessel density is high",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The other axis, and the reason this pair is placed together. "
            "Tributyltin caused imposex in molluscs at nanograms per litre "
            "while performing outstandingly on the metric above, and both were "
            "true simultaneously for years. Reporting efficacy without this "
            "figure is the error the field spent decades correcting, and "
            "enclosed harbours are where the ratio between the two is worst."
        ),
    ),
    Metric(
        name="Predicted no effect concentration",
        symbol="PNEC",
        unit="micrograms or nanograms per litre",
        typical="derived from ecotoxicity testing across trophic levels",
        formula="risk_quotient",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The threshold the entry above is compared against, and the ratio "
            "of the two is what an authorisation decision actually turns on. "
            "For tributyltin the effect concentration was far below anything "
            "the original assessments had considered plausible, which is an "
            "argument for testing at concentrations lower than expected to "
            "matter."
        ),
    ),
    # =========================================================================
    #  HOW THE COATING BEHAVES OVER TIME
    # =========================================================================
    Metric(
        name="Biocide release rate",
        symbol="R_rel",
        unit="micrograms per square centimetre per day",
        typical="must be high enough to deter settlement and low enough to be "
        "environmentally acceptable",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The design variable for a self-polishing coating, and the whole "
            "difficulty of biocidal antifouling in one number. The window "
            "between effective and unacceptable has narrowed with each "
            "regulatory cycle, which is what has driven the move to non-biocidal "
            "approaches."
        ),
    ),
    Metric(
        name="Service interval",
        symbol="t_service",
        unit="months between cleaning or years between drydockings",
        typical="coatings are specified for a drydocking interval of several "
        "years",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The commercial specification a coating is sold against. It is why "
            "laboratory durability results are treated sceptically here: a "
            "surface must survive years of abrasion, fouling, cleaning and "
            "mechanical damage, and many promising approaches fail on this "
            "rather than on efficacy."
        ),
    ),
    Metric(
        name="Critical removal shear stress",
        symbol="tau_c",
        unit="pascals",
        typical="the threshold water shear at which attached organisms detach "
        "from a foul-release surface",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The quantity that decides whether a foul-release coating works for "
            "a given vessel, because the shear available depends on speed. It "
            "is the honest expression of that technology's limitation: below "
            "the threshold speed nothing is removed, which is why a stationary "
            "vessel fouls regardless of coating quality."
        ),
    ),
    Metric(
        name="Surface free energy",
        symbol="gamma_s",
        unit="millijoules per square metre",
        typical="around 20 - 25 for silicone foul-release surfaces",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The physical property foul-release coatings are designed around, "
            "with a minimum in adhesion falling in a characteristic range. It "
            "predicts adhesion strength usefully and predicts field performance "
            "only loosely, since a real hull also has roughness, damage and "
            "biofilm on it."
        ),
    ),
    # =========================================================================
    #  THE MOST QUOTED NUMBER, AND WHY TO DISTRUST IT
    # =========================================================================
    Metric(
        name="Settlement inhibition in laboratory assay",
        symbol="EC50_settle",
        unit="concentration or surface property giving half maximal reduction "
        "in settlement",
        typical="reported for barnacle cyprids, algal spores and bacterial "
        "attachment",
        formula="dose_response",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The most commonly reported figure in this field and the least "
            "predictive. A short assay with one species under constant "
            "conditions correlates poorly with a hull meeting a succession of "
            "species over years, so a surface that halves settlement in "
            "fourteen days may foul completely in a season. It is useful for "
            "ranking candidates and not for claiming performance."
        ),
    ),
    Metric(
        name="Biofilm coverage",
        symbol="f_biofilm",
        unit="per cent of surface covered by microbial film",
        typical="establishes within days on any unprotected surface",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Tracked separately from macrofouling because it is the stage that "
            "enables the others: many larvae settle in response to a bacterial "
            "biofilm cue rather than onto bare substrate. Preventing the film "
            "prevents much of what would follow, which is why quorum sensing "
            "and enzymatic approaches target it."
        ),
    ),
    # =========================================================================
    #  THE OBJECTIVE THAT IS NOT ABOUT FUEL
    # =========================================================================
    Metric(
        name="Species transfer risk from hull fouling",
        symbol="R_bio",
        unit="qualitative or index-based assessment of transportable organisms",
        typical="assessed by inspection of niche areas rather than of the "
        "open hull",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "A different objective from every other metric here, and the two do "
            "not always align. A hull smooth enough to be fuel-efficient may "
            "still carry viable organisms in sea chests, thrusters and other "
            "niche areas, which is where invasive species are actually "
            "transported and where inspection regimes concentrate."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Drag first, matching the facet's opening, then the environmental assessment.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "frictional_resistance",
    "reynolds_number",
    "dose_response",
    "risk_quotient",
    "surface_free_energy",
    "mass_balance",
)
