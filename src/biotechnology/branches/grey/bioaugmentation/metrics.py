# =============================================================================
#  biotechnology.branches.grey.bioaugmentation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE ONLY METRIC THAT SETTLES ANYTHING IS A DIFFERENCE AGAINST A CONTROL.
#
#  Every other measurement in this facet can look excellent while the treatment
#  does nothing. The introduced population can be large on day one; the strain
#  can degrade beautifully in a flask; the contaminant concentration can fall
#  steadily for a year. None of that distinguishes the product from what would
#  have happened anyway, because the residents were also degrading, the
#  contaminant was also dispersing, and the introduced cells were also dying.
#
#      MEASURE THE AUGMENTED PLOT AGAINST AN UNAUGMENTED ONE, OR MEASURE
#      NOTHING.
#
#  So this facet is ordered deliberately: the incremental benefit first, the
#  survival metrics second because they explain the usual result, and the
#  performance figures last with an explicit warning about what they do not
#  show. That ordering is itself the argument.
#
#  A SECOND POINT. Survival is measured as a DECLINE RATE rather than as a
#  count, because a count on the day of application measures the dose and a
#  decline rate measures the outcome. The field spent years reporting the
#  first.
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
    #  THE ONLY METRIC THAT SETTLES THE QUESTION
    # =========================================================================
    Metric(
        name="Incremental benefit over unaugmented control",
        symbol="delta_aug",
        unit="difference in removal or rate between augmented and control plots",
        typical="not detectable in most controlled field comparisons; "
        "substantial and reproducible for dechlorination at sites lacking the "
        "organisms",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The metric this record is organised around, and the one the "
            "commercial literature most often omits. Everything below can look "
            "good while this is zero, because the residents degrade, the plume "
            "disperses and the introduced cells die, all at the same time. A "
            "before-and-after comparison at a single site cannot produce this "
            "number no matter how carefully it is done."
        ),
    ),
    Metric(
        name="Statistical power of the comparison",
        symbol="1 - beta",
        unit="probability of detecting a specified effect if it exists",
        typical="frequently too low to detect a modest effect, given site "
        "variability and the number of plots a project can afford",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Placed second because it governs how the entry above should be "
            "read. Site heterogeneity is large, replication is expensive, and "
            "an underpowered trial that finds nothing has not shown that "
            "nothing happened. This cuts both ways and is recorded for that "
            "reason: it is as much a caution to the sceptic as to the vendor."
        ),
    ),
    # =========================================================================
    #  SURVIVAL, WHICH IS THE ACTUAL BINDING CONSTRAINT
    # =========================================================================
    Metric(
        name="Survival decline rate of the introduced population",
        symbol="k_decline",
        unit="log reduction per week",
        formula="first_order_decay",
        typical="commonly several orders of magnitude within weeks in soil and "
        "groundwater",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Expressed as a rate rather than as a count deliberately. A count "
            "on the day of application measures the dose; a decline rate "
            "measures whether the organisms are still there to do anything. "
            "This is the number that explains the incremental benefit above, "
            "and it is largely independent of how good a degrader the strain "
            "is."
        ),
    ),
    Metric(
        name="Establishment fraction",
        symbol="f_est",
        unit="per cent of the introduced population persisting at a defined "
        "time after application",
        typical="low without a vacant niche; high where there was no incumbent, "
        "as in digester seeding and plant recovery",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The clearest single discriminator between the cases that work and "
            "the cases that do not. Where an incumbent community exists this is "
            "small; where the vessel was sterile or the biomass was killed it "
            "is large. The mechanism and the outcome agree, which is why the "
            "exception in this record is convincing rather than anecdotal."
        ),
    ),
    Metric(
        name="Colonisation resistance of the resident community",
        symbol="R_col",
        unit="qualitative, indexed by resident diversity and niche occupancy",
        typical="higher in diverse, established communities",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Names the property being fought. A diverse community leaves fewer "
            "unused resources and is correspondingly harder to invade, which is "
            "why augmentation succeeds in disturbed or sterile settings and "
            "fails in mature ones. The same property is described in "
            "`yellow.probiotics_and_prebiotics` for the gut, using almost the "
            "same words for an entirely separate literature."
        ),
    ),
    # =========================================================================
    #  IS THE SITE A CANDIDATE AT ALL
    # =========================================================================
    Metric(
        name="Baseline functional gene abundance",
        symbol="N_gene_0",
        unit="gene copies per gram or per litre before any addition",
        typical="detectable at most hydrocarbon sites; frequently below "
        "detection for complete dechlorination",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The measurement that should be taken before anything is purchased. "
            "Present means biostimulation; absent means augmentation may be "
            "justified. Almost every documented failure in this record is a "
            "site where this was never measured, and the commercial incentive "
            "runs against measuring it."
        ),
    ),
    Metric(
        name="Dose applied",
        symbol="N_dose",
        unit="viable cells per gram of soil or per litre of groundwater",
        typical="orders of magnitude below the resident population in soil",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Recorded to make the arithmetic visible. The residents outnumber a "
            "typical dose substantially at the moment of application, before "
            "any decline has occurred, which is the scale of the problem stated "
            "as a number rather than as an argument."
        ),
    ),
    # =========================================================================
    #  WHAT THE PRODUCT ACTUALLY CONTAINS
    # =========================================================================
    Metric(
        name="Viable count on delivery",
        symbol="N_viable",
        unit="colony forming units per gram or millilitre of product",
        typical="lower than the label where the cold chain was interrupted",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The gap between what was manufactured and what arrives. It is a "
            "genuine quality issue and it is not the main reason augmentation "
            "fails, which matters because it is the explanation vendors reach "
            "for first. A perfectly delivered dose still faces the competition "
            "in the entries above."
        ),
    ),
    Metric(
        name="Specific degradation rate in pure culture",
        symbol="q_max",
        unit="milligrams of substrate per gram of biomass per hour",
        formula="monod_equation",
        typical="high for selected strains, which is what selection selects for",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Placed last, and with a warning. This is the number on the product "
            "literature and it is measured with no competitors, no predators "
            "and no shortage of substrate. It is a real property of the "
            "organism and it predicts field performance poorly, because the "
            "field constraint is survival."
        ),
    ),
    # =========================================================================
    #  AND WHETHER IT WAS WORTH IT
    # =========================================================================
    Metric(
        name="Cost per unit of incremental removal",
        symbol="C_delta",
        unit="euro per kilogram of contaminant attributable to the addition",
        typical="undefined where the incremental benefit is not detectable",
        evidence=EvidenceLevel.INDICATIVE,
        note=(
            "The commercial version of the first metric, and it has the same "
            "property: where the numerator is real the technique is worth "
            "buying, and where the denominator cannot be demonstrated the cost "
            "per unit is not a small number but an undefined one."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Population dynamics first, since this record is about survival.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "first_order_decay",
    "monod_equation",
    "logistic_growth",
    "specific_growth_rate",
    "mass_balance",
)
