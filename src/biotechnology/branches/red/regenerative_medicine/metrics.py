# =============================================================================
#  biotechnology.branches.red.regenerative_medicine.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  These metrics come from materials science as much as from biology, which is
#  unusual for the red branch and is the point: a tissue construct fails as a
#  material long before it fails as a biological object.
#
#  Two entries deserve attention before the rest.
#
#  The OXYGEN DIFFUSION LIMIT is the only metric in this library that is a hard
#  physical bound rather than a typical range. It does not improve with better
#  cells, better media or better technique. Every construct thicker than it
#  either carries plumbing or dies in the middle, and the entire structure of
#  `practice.APPLICATIONS` follows from that number.
#
#  YOUNG MODULUS is listed because stiffness is not merely a mechanical
#  requirement to be matched, it is a differentiation signal. Identical stem
#  cells become bone on a stiff substrate and nerve on a soft one, so getting
#  the number wrong produces the wrong tissue rather than merely a floppy one.
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
    #  The hard physical bound. Not a typical range; a limit.
    # -------------------------------------------------------------------------
    Metric(
        name="Oxygen diffusion limit",
        symbol="L_O2",
        unit="micrometres from the nearest capillary",
        typical="100 - 200 um",
        formula="oxygen_diffusion_limit",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The single hardest constraint in the field, and the only physical "
            "bound in this library rather than a conditional range. It does not "
            "improve with better cells or better media. Every construct thicker "
            "than this must carry a perfusable network or it necroses centrally, "
            "which is why thin tissues reached patients decades ago and thick "
            "ones have not."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Stiffness. A mechanical requirement and a differentiation signal at once.
    # -------------------------------------------------------------------------
    Metric(
        name="Young modulus of the construct",
        symbol="E",
        unit="pascals, spanning ten orders of magnitude across tissues",
        typical="0.5 kPa for brain to 20 GPa for cortical bone",
        formula="young_modulus",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Matching native stiffness is not only a mechanical requirement. "
            "Substrate stiffness directs stem cell fate: identical cells "
            "differentiate towards bone on a hard substrate and towards neural "
            "lineages on a soft one. A scaffold with the wrong modulus produces "
            "the wrong tissue, not merely a weak one."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Porosity. Governs both nutrient transport and cell infiltration.
    # -------------------------------------------------------------------------
    Metric(
        name="Scaffold porosity",
        symbol="phi",
        unit="void volume fraction, dimensionless",
        typical="0.6 - 0.9",
        formula="scaffold_porosity",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Below roughly 0.6 the interior is starved and cells cannot "
            "migrate in. Above roughly 0.9 the scaffold has too little material "
            "to bear load. Pore interconnectivity matters as much as the "
            "fraction, since isolated voids contribute nothing to transport."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Pore size. A separate parameter from porosity, and tissue-specific.
    # -------------------------------------------------------------------------
    Metric(
        name="Mean pore diameter",
        symbol="d_pore",
        unit="micrometres",
        typical="100 - 500 um for bone, 20 - 125 um for skin",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Too small excludes cells and vessels; too large reduces the "
            "surface available for attachment. The optimum is tissue-specific "
            "and is one of the few scaffold parameters with well-replicated "
            "values."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Seeding density. How many cells go in at the start.
    # -------------------------------------------------------------------------
    Metric(
        name="Cell seeding density",
        symbol="rho_seed",
        unit="cells per cubic centimetre of scaffold",
        typical="1e6 - 1e8 cells/cm^3",
        formula="seeding_density",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Constrained at the top end by the same diffusion limit: seeding "
            "more cells than the construct can supply with oxygen produces a "
            "necrotic core faster, not a denser tissue."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Residual DNA. The accepted release criterion for a decellularised
    #  matrix, and a rare example of a threshold the field agrees on.
    # -------------------------------------------------------------------------
    Metric(
        name="Residual double-stranded DNA",
        symbol="dsDNA",
        unit="nanograms per milligram dry weight",
        typical="< 50 ng/mg",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The conventional threshold below which a matrix is judged "
            "acellular, alongside no visible nuclei on staining and fragments "
            "under about two hundred base pairs. Residual cellular material is "
            "the main driver of an adverse host response to a decellularised "
            "graft."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Degradation rate. Must be matched to deposition, not minimised.
    # -------------------------------------------------------------------------
    Metric(
        name="Scaffold degradation half-life",
        symbol="t_deg",
        unit="weeks",
        typical="2 weeks for skin to 24 months for bone",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Matched to the rate at which the patient deposits their own "
            "matrix. Faster and the construct collapses before it is replaced; "
            "slower and the retained material blocks remodelling and provokes "
            "chronic inflammation."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Viability. The routine readout, and the one that reveals the necrotic
    #  core.
    # -------------------------------------------------------------------------
    Metric(
        name="Construct cell viability",
        symbol="V",
        unit="per cent viable cells",
        typical="> 80 % at release, measured through the depth",
        formula="cell_viability",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Depth-resolved measurement matters more than the bulk figure. A "
            "construct with a dead core and a living surface can report "
            "acceptable average viability while being functionally useless."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  fick_diffusion is the relationship from which the oxygen limit falls out,
#  and is included so that a reader can see where the two hundred micrometres
#  comes from rather than taking it on trust.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "oxygen_diffusion_limit",
    "fick_diffusion",
    "young_modulus",
    "scaffold_porosity",
    "seeding_density",
    "cell_viability",
    "population_doubling_level",
    "doubling_time",
)
