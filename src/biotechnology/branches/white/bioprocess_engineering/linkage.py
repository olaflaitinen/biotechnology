# =============================================================================
#  biotechnology.branches.white.bioprocess_engineering.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record completes the three-way division of labour that the white branch
#  is organised around, and it is worth stating once from the last of the three
#  sides:
#
#      metabolic_engineering   builds the strain          measures the strain
#      microbial_fermentation  grows the strain           measures the culture
#      bioprocess_engineering  builds the plant           measures the process
#
#  The boundary with the middle record is drawn at a single quantity. Oxygen
#  transfer appears in both, and it is a DEMAND there and a CAPABILITY here.
#  kLa belongs to the vessel; the oxygen uptake rate belongs to the organism; a
#  process works when the first exceeds the second. In practice those are the
#  responsibility of two different engineers, which is why they are two
#  records.
#
#  `red.pharmaceutical_biotechnology` is the application that supplies this
#  record its regulatory weight, its cost structure and its worst failure. The
#  edge is not decorative: the comparability requirement described in
#  `governance.py` exists because the products in that record cannot be fully
#  characterised, and everything severe about this discipline follows from it.
#
#  `grey.wastewater_treatment` is an edge a reader might not expect and it is
#  deliberate. A fermentation plant produces a large organic effluent, and the
#  treatment of that stream is not a footnote to the process but a permit
#  condition and a capital item.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four. Goal 12 is claimed with a caveat that belongs in the data rather than
#  in a footnote: single-use plastics raised facility utilisation and created a
#  disposal stream, and which way that trade falls is settled by life cycle
#  assessment rather than by preference. Goal 9 is the primary claim, since
#  this discipline is what turns a biological discovery into something that can
#  actually be supplied.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on the manufacture and supply security of medicines
    6,  # Clean water, on process water demand and effluent treatment
    9,  # Industry and innovation, on manufacturing capability itself
    12,  # Responsible production, including the single-use trade
)


# =============================================================================
#  GLOSSARY
#  Grouped: the vessel and transport vocabulary, the scale-up vocabulary, the
#  downstream train in process order, then the words that govern whether a
#  process may be changed.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the vessel ------------------------------------------------------------
    "bioreactor",
    "impeller",
    "sparger",
    "baffle",
    "oxygen_transfer_coefficient",
    "shear_stress",
    "mixing_time",
    "residence_time",
    # -- making it bigger ------------------------------------------------------
    "scale_up",
    "scale_down_model",
    "geometric_similarity",
    "power_per_volume",
    "reynolds_number",
    "dimensional_analysis",
    "computational_fluid_dynamics",
    # -- the downstream train, in order ----------------------------------------
    "downstream_processing",
    "harvest",
    "centrifugation",
    "tangential_flow_filtration",
    "cell_disruption",
    "inclusion_body",
    "capture_chromatography",
    "polishing",
    "diafiltration",
    "viral_clearance",
    "fill_finish",
    # -- proving it stays the same ---------------------------------------------
    "process_validation",
    "comparability",
    "critical_quality_attribute",
    "critical_process_parameter",
    "design_space",
    "process_analytical_technology",
    "single_use_system",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "bioprocess_engineering_principles",
    "downstream_processing_review",
    "scale_up_criteria_review",
    "downstream_bottleneck_analysis",
    "ich_q5e_comparability",
    "single_use_systems_assessment",
    "continuous_bioprocessing_review",
    "viral_contamination_facility_case",
    "sigma_factor_centrifuge_scale_up",
    "quality_by_design_guidance",
)


# =============================================================================
#  RELATED
#  Seven edges. The first two complete the division of labour; the third is
#  where the discipline's severity comes from.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the culture whose demands this plant must meet ------------------------
    "white.microbial_fermentation",
    # -- the strain, and where its stability requirement comes from ------------
    "white.metabolic_engineering",
    # -- the application that sets the regulatory weight -----------------------
    "red.pharmaceutical_biotechnology",
    # -- reactor design for enzymatic rather than cellular processes -----------
    "white.biocatalysis",
    # -- the largest tonnage this equipment produces ---------------------------
    "white.industrial_enzymes",
    # -- what leaves the plant that is not product -----------------------------
    "grey.wastewater_treatment",
    # -- the same plant making food protein, under different rules -------------
    "yellow.precision_fermentation",
)
