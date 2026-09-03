# =============================================================================
#  biotechnology.branches.white.metabolic_engineering.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `white.biocatalysis` names this record as its genuine strategic
#  alternative, and the edge is reciprocated here with the same framing seen
#  from the other side.
#
#      biocatalysis            a few steps, outside a cell, with purified or
#                              immobilised enzymes. The engineer controls the
#                              medium, the concentrations and the temperature
#                              absolutely, and pays for every cofactor.
#
#      metabolic engineering   the whole pathway inside a living organism. The
#                              cell regenerates cofactors for nothing and
#                              repairs its own catalysts, and in exchange it
#                              grows, mutates, spends carbon on staying alive,
#                              and cannot tolerate what a bare enzyme
#                              tolerates.
#
#  There is no general answer to which is right. Long pathways with expensive
#  cofactors favour the cell; short pathways with toxic substrates, poor
#  solubility or a need for absolute control favour the isolated enzyme.
#  Recording that as an open engineering decision rather than picking a winner
#  is deliberate.
#
#  `white.bioprocess_engineering` is a hard dependency rather than a
#  neighbour. The oxygen transfer metric in this record's `metrics.py` is a
#  vessel property, not a strain property, and a strain that is excellent in a
#  shake flask can be ordinary at cubic metre scale for reasons that belong
#  entirely to that record.
#
#  `gold.genomics_data_analysis` and `gold.machine_learning_in_biology` are
#  where the design and learn halves of the cycle now live. This is one of the
#  most computational records in the white branch and the edges say so.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four. Goal 2 is claimed on a mechanism that is easy to miss: feed-grade
#  lysine and methionine let a livestock diet meet its amino acid requirement
#  with less protein crop, which frees land and grain. That is a larger and
#  better documented food-security contribution than any of the field's more
#  publicised projects.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on feed amino acids reducing the protein crop required
    7,  # Affordable clean energy, on fuels and on gas fermentation
    9,  # Industry and innovation, on replacing petrochemical routes
    12,  # Responsible production, on feedstock and waste
)


# =============================================================================
#  GLOSSARY
#  Grouped: the network vocabulary, the design and control vocabulary, the
#  performance vocabulary, then the terms specific to keeping a strain alive
#  and honest.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the network -----------------------------------------------------------
    "metabolism",
    "metabolic_pathway",
    "metabolic_flux",
    "genome_scale_metabolic_model",
    "stoichiometric_matrix",
    "precursor",
    "cofactor",
    "redox_balance",
    # -- design and control ----------------------------------------------------
    "flux_balance_analysis",
    "metabolic_control_analysis",
    "flux_control_coefficient",
    "rate_limiting_step",
    "feedback_inhibition",
    "pathway_refactoring",
    "design_build_test_learn",
    "retrobiosynthesis",
    # -- how a strain is judged ------------------------------------------------
    "titre",
    "product_yield",
    "theoretical_yield",
    "volumetric_productivity",
    "specific_growth_rate",
    # -- keeping the strain doing what it was built for ------------------------
    "growth_coupling",
    "adaptive_laboratory_evolution",
    "genetic_stability",
    "product_toxicity",
    "chassis_organism",
    "gas_fermentation",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "bailey_metabolic_engineering_1991",
    "kacser_burns_control_analysis",
    "flux_balance_analysis_primer",
    "genome_scale_model_reconstruction_protocol",
    "artemisinic_acid_yeast_paper",
    "semisynthetic_artemisinin_market_review",
    "butanediol_designed_pathway",
    "propanediol_commercial_process",
    "growth_coupled_strain_design_review",
    "gas_fermentation_commercial_review",
)


# =============================================================================
#  RELATED
#  Seven edges. The first is the strategic alternative; the second is the
#  dependency; the rest are where the products go.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same job done outside a cell --------------------------------------
    "white.biocatalysis",
    # -- the vessel, without which none of the metrics hold at scale -----------
    "white.bioprocess_engineering",
    # -- where the strain is actually run --------------------------------------
    "white.microbial_fermentation",
    # -- what the pathways are built to make -----------------------------------
    "white.biobased_chemicals",
    "white.biofuels",
    # -- the design and learn halves of the cycle ------------------------------
    "gold.machine_learning_in_biology",
    # -- fermentation-derived food ingredients and their labelling -------------
    "yellow.precision_fermentation",
)
