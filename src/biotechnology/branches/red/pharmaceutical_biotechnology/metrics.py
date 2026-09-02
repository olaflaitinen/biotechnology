# =============================================================================
#  biotechnology.branches.red.pharmaceutical_biotechnology.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: see `red/gene_therapy/metrics.py` for the full rationale on why
#  `typical` is a string, why symbols are ASCII, and how FORMULAS links this
#  record to the computational half of the package.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the most quantitatively mature subtype in the library. Every number
#  below is a routine release or process specification that somebody measures
#  on every batch, which is why the evidence grades are unusually strong. The
#  set is chosen to span the whole process train: two upstream productivity
#  metrics, one culture metric, one downstream yield metric and two purity
#  specifications.
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
    #  Titre. The headline number of the whole industry. Its hundredfold rise
    #  between 1990 and 2020 is the single largest reason biologics became
    #  affordable enough to use in chronic disease rather than only in cancer.
    # -------------------------------------------------------------------------
    Metric(
        name="Product titre",
        symbol="C_p",
        unit="grams per litre of harvested culture",
        typical="1 - 10 g/L for CHO fed-batch",
        formula="product_titre",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Titres rose roughly a hundredfold between 1990 and 2020 through "
            "media development, clone selection and feeding strategy rather "
            "than through any single breakthrough. Perfusion processes report "
            "lower instantaneous titre but far higher volumetric productivity."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Specific productivity. Separates the quality of the cell line from the
    #  quantity of biomass, and is therefore the number a cell-line development
    #  group is actually judged on.
    # -------------------------------------------------------------------------
    Metric(
        name="Specific productivity",
        symbol="q_p",
        unit="picograms per cell per day",
        typical="10 - 60 pg/cell/day",
        formula="specific_productivity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A high-titre process with low q_p is simply carrying more cells, "
            "which costs oxygen, nutrients and cooling. The two numbers must "
            "always be read together."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Viable cell density and viability. The daily operational readout; the
    #  point at which viability falls below roughly 80 per cent is usually the
    #  harvest trigger, because dying cells release proteases and DNA that
    #  make downstream processing harder.
    # -------------------------------------------------------------------------
    Metric(
        name="Viable cell density",
        symbol="VCD",
        unit="million viable cells per millilitre",
        typical="5 - 30 x 10^6 cells/mL peak",
        formula="viable_cell_density",
        evidence=EvidenceLevel.CONSENSUS,
        note="Harvest is normally triggered when viability falls below 80 %.",
    ),
    # -------------------------------------------------------------------------
    #  Step yield. The reason process designers fight so hard to remove unit
    #  operations: yields multiply, so five steps at 90 % leave only 59 %.
    # -------------------------------------------------------------------------
    Metric(
        name="Downstream step yield",
        symbol="Y_step",
        unit="per cent recovered per unit operation",
        typical="85 - 98 % per step",
        formula="process_yield",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Overall yield is the product of the step yields. Five steps at "
            "90 % each leave 59 % overall, which is why step count is "
            "minimised aggressively and why Protein A capture, at 90-95 % in "
            "a single step, is so hard to displace."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Host cell protein. A release specification, measured with a platform
    #  sandwich immunoassay raised against a null-cell-line lysate.
    # -------------------------------------------------------------------------
    Metric(
        name="Host cell protein residual",
        symbol="HCP",
        unit="nanograms per milligram of product",
        typical="< 100 ng/mg",
        formula="impurity_clearance",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The threshold is risk-based rather than absolute: a single "
            "immunogenic host protein at low level can matter more than a "
            "large mass of inert ones."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Aggregate content. High-molecular-weight species are both a potency
    #  problem and the main driver of immunogenicity, so this is one of the
    #  few specifications that is essentially never relaxed.
    # -------------------------------------------------------------------------
    Metric(
        name="High molecular weight aggregate",
        symbol="HMW",
        unit="per cent by size-exclusion chromatography",
        typical="< 2 - 5 % at release",
        formula="aggregate_fraction",
        evidence=EvidenceLevel.CONSENSUS,
        note="Aggregates are the principal structural driver of immunogenicity.",
    ),
)


# =============================================================================
#  FORMULAS
#  The upstream kinetics group (Monod, doubling time) is included because a
#  process development scientist reaches for them daily, even though no single
#  metric above is defined by them.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "product_titre",
    "specific_productivity",
    "viable_cell_density",
    "process_yield",
    "impurity_clearance",
    "aggregate_fraction",
    "monod_growth",
    "doubling_time",
    "beer_lambert",
    "protein_concentration_a280",
    "integral_viable_cell_density",
)
