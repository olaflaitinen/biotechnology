# =============================================================================
#  biotechnology.branches.red.antibody_engineering.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the most quantitatively precise record in the red branch, because
#  antibody binding is one of the few interactions in biology that can be
#  measured directly, in real time, without a label, to two significant figures.
#
#  One correction runs through the notes below, because it is the most common
#  error in the field's own literature: TIGHTER IS NOT BETTER. Affinity below
#  roughly one nanomolar buys almost nothing in a solid tumour, because the
#  molecule is consumed by the first cells it meets and never penetrates
#  further. This is the binding-site barrier, and it means the optimum affinity
#  for a tumour-targeting molecule is often deliberately worse than the best
#  achievable.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # -------------------------------------------------------------------------
    #  Equilibrium dissociation constant. The headline number of the field, and
    #  the one most often optimised past the point of usefulness.
    # -------------------------------------------------------------------------
    Metric(
        name="Equilibrium dissociation constant",
        symbol="K_D",
        unit="molar",
        typical="1e-12 - 1e-8 M",
        formula="dissociation_constant",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "K_D = k_off / k_on, and equals the concentration at which half the "
            "target is occupied. Lower means tighter. Tighter is not always "
            "better: below about 1e-9 M a tumour-targeting molecule is captured "
            "by the first antigen-positive cells it encounters and never "
            "penetrates the tissue behind them. This is the binding-site "
            "barrier, and it is why affinity is sometimes deliberately reduced."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Association rate. Diffusion sets a ceiling; nothing can bind faster than
    #  it can arrive.
    # -------------------------------------------------------------------------
    Metric(
        name="Association rate constant",
        symbol="k_on",
        unit="per molar per second",
        typical="1e4 - 1e7 1/(M*s)",
        formula="binding_kinetics",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Bounded above by the diffusion limit, around 1e9 1/(M*s) for "
            "proteins of this size. Most antibodies sit two to five orders of "
            "magnitude below it, so there is real headroom, but engineering "
            "usually targets k_off instead because it is easier to change."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Dissociation rate. Where affinity engineering actually happens.
    # -------------------------------------------------------------------------
    Metric(
        name="Dissociation rate constant",
        symbol="k_off",
        unit="per second",
        typical="1e-5 - 1e-2 1/s",
        formula="binding_kinetics",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A k_off of 1e-4 1/s corresponds to a residence time of roughly "
            "three hours. For a receptor-blocking molecule, residence time "
            "often predicts effect better than K_D does, because the biology "
            "responds to how long the receptor is occupied rather than to an "
            "equilibrium that is never reached in vivo."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Avidity. The reason a bivalent molecule outperforms its own monovalent
    #  affinity, and a routine source of overstated numbers.
    # -------------------------------------------------------------------------
    Metric(
        name="Avidity enhancement",
        symbol="beta",
        unit="fold, dimensionless",
        typical="10 - 1000 fold over monovalent affinity",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Two arms binding a surface with many copies of the target detach "
            "far more slowly than one arm would, because both must release "
            "simultaneously. An apparent K_D measured on a cell therefore looks "
            "far tighter than the true monovalent constant, and quoting the "
            "former as the latter is the most common way an affinity figure is "
            "inflated."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Potency in a functional assay. Related to affinity but not the same
    #  number, and the one that predicts a dose.
    # -------------------------------------------------------------------------
    Metric(
        name="Half maximal effective concentration",
        symbol="EC50",
        unit="nanomolar",
        typical="0.01 - 100 nM",
        formula="ec50_hill",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Measured in a functional assay rather than by binding. EC50 and "
            "K_D diverge whenever there is receptor reserve, signal "
            "amplification or avidity, so a potency figure is not a binding "
            "figure and cannot be substituted for one."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Drug-to-antibody ratio. A two-sided specification for conjugates.
    # -------------------------------------------------------------------------
    Metric(
        name="Drug-to-antibody ratio",
        symbol="DAR",
        unit="payload molecules per antibody",
        typical="2 - 8, most commonly 4",
        formula="drug_antibody_ratio",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Too low is under-potent. Too high aggregates, clears faster and "
            "loses the very targeting the conjugate exists for. Conventional "
            "conjugation gives a distribution rather than a single value, which "
            "is why site-specific chemistry is preferred despite its cost."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Circulating half-life. The property Fc engineering exists to tune.
    # -------------------------------------------------------------------------
    Metric(
        name="Serum half-life",
        symbol="t_half",
        unit="days",
        typical="14 - 21 days for IgG1; hours for a fragment",
        formula="elimination_half_life",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The neonatal Fc receptor rescues IgG from lysosomal degradation "
            "and recycles it, which is why a full antibody persists for weeks "
            "while a fragment lacking that stem is cleared within hours. Fc "
            "engineering can extend this to roughly three months, which is what "
            "makes single-dose seasonal prophylaxis possible."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Aggregate content. A release specification, and the main structural
    #  driver of the immunogenicity recorded in practice.CHALLENGES.
    # -------------------------------------------------------------------------
    Metric(
        name="High molecular weight aggregate",
        symbol="HMW",
        unit="per cent by size-exclusion chromatography",
        typical="< 2 - 5 % at release",
        formula="aggregate_fraction",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Aggregates present repeating epitope arrays, which is exactly the "
            "arrangement the immune system is built to respond to. This is the "
            "structural link between a manufacturing attribute and the anti-drug "
            "antibody problem."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  protein_concentration_a280 and molar_extinction are included because every
#  number above is normalised to a concentration measured that way, and an
#  extinction coefficient error propagates into all of them at once.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "dissociation_constant",
    "binding_kinetics",
    "ec50_hill",
    "drug_antibody_ratio",
    "elimination_half_life",
    "aggregate_fraction",
    "protein_concentration_a280",
    "molar_extinction",
    "serial_dilution",
)
