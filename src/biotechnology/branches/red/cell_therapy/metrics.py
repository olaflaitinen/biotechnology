# =============================================================================
#  biotechnology.branches.red.cell_therapy.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Every metric below is a release specification: a number that must be
#  measured and must fall inside a range before the product may be given to a
#  patient. That is unusual. In most subtypes the metrics are descriptive; here
#  they are gating. A batch that misses viability is not a suboptimal batch, it
#  is not a medicine, and for an autologous product there is no second batch.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # -------------------------------------------------------------------------
    #  Dose. Expressed per kilogram in paediatrics and as a flat dose in
    #  adults, which is a frequent source of confusion when comparing trials.
    # -------------------------------------------------------------------------
    Metric(
        name="Cell dose",
        symbol="D_cell",
        unit="CAR-positive cells per kilogram body weight",
        typical="1e6 - 5e6 CAR-positive T cells/kg",
        formula="cell_dose",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Adult products are frequently dosed as a flat total cell number "
            "rather than per kilogram, so cross-trial comparison requires "
            "converting one to the other with an assumed body weight."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Viability. The classic release gate. Seventy per cent is the number
    #  that appears in most specifications, and it is a floor rather than a
    #  target.
    # -------------------------------------------------------------------------
    Metric(
        name="Cell viability",
        symbol="V",
        unit="per cent viable",
        typical="> 70 % at release",
        formula="cell_viability",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Measured by trypan blue exclusion or by flow-cytometric dye "
            "exclusion. Post-thaw viability, measured after the product "
            "reaches the clinic, is the number that actually matters and is "
            "always lower than the number at freeze."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Population doubling level. The cumulative history of the culture, and
    #  the parameter that predicts replicative senescence and loss of potency.
    # -------------------------------------------------------------------------
    Metric(
        name="Population doubling level",
        symbol="PDL",
        unit="cumulative doublings",
        typical="10 - 30 before senescence in primary T cells",
        formula="population_doubling_level",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Counter-intuitively, less expansion is often better: a product "
            "expanded fewer times retains more early-memory phenotype and "
            "persists longer in vivo."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Transduction efficiency, here reported as the CAR-positive fraction.
    #  Shared formula with red.gene_therapy, which is exactly the kind of
    #  overlap the FORMULAS registry exists to make visible.
    # -------------------------------------------------------------------------
    Metric(
        name="Transduction efficiency",
        symbol="TE",
        unit="per cent CAR-positive cells",
        typical="20 - 60 %",
        formula="transduction_efficiency",
        evidence=EvidenceLevel.CONSENSUS,
        note="Determines the dose calculation, since dosing is on CAR-positive cells.",
    ),
    # -------------------------------------------------------------------------
    #  Fold expansion. The manufacturing output measure, and the one that
    #  fails first in patients whose lymphocytes are exhausted.
    # -------------------------------------------------------------------------
    Metric(
        name="Fold expansion",
        symbol="FE",
        unit="dimensionless multiple",
        typical="50 - 1000 x over 7 - 14 days",
        formula="fold_expansion",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The single most common cause of a manufacturing failure is that "
            "the starting material never reaches the required expansion."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Vector copy number. A safety specification rather than a potency one:
    #  it bounds the insertional mutagenesis risk from an integrating vector.
    # -------------------------------------------------------------------------
    Metric(
        name="Vector copy number per cell",
        symbol="VCN",
        unit="copies per diploid genome",
        typical="< 5 copies/genome as a safety limit",
        formula="vector_copy_number",
        evidence=EvidenceLevel.CONSENSUS,
        note="Regulators normally require a justification above five copies.",
    ),
)


# =============================================================================
#  FORMULAS
#  Includes the haemocytometer counting formula, which sounds trivially basic
#  but is the actual origin of most of the numbers above and a routine source
#  of error when the dilution factor is mishandled.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "cell_dose",
    "cell_viability",
    "population_doubling_level",
    "fold_expansion",
    "transduction_efficiency",
    "vector_copy_number",
    "doubling_time",
    "cell_counting_haemocytometer",
    "specific_growth_rate",
)
