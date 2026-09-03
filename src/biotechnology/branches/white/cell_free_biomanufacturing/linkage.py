# =============================================================================
#  biotechnology.branches.white.cell_free_biomanufacturing.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record closes the white branch, and its edges are best read as the
#  completed set of answers to one question: WHAT CARRIES OUT THE CHEMISTRY?
#
#      microbial_fermentation   a living organism, growing, in a large vessel
#      metabolic_engineering    a living organism, redesigned
#      biocatalysis             purified enzymes, chosen and assembled by hand
#      cell_free                extracted machinery, programmed with DNA
#
#  The boundary with `white.biocatalysis` is the sharpest and most useful. Both
#  work outside a cell. The difference is how the system is specified: a
#  biocatalytic reaction is defined by which enzymes were put in the vessel, a
#  cell-free reaction by which template was added. Add new DNA to a cell-free
#  system and it makes something new; a biocatalytic system requires a
#  different protein.
#
#  `red.molecular_diagnostics` is a genuine dependency rather than a
#  neighbouring topic. The paper-based sensors that are this record's strongest
#  application are diagnostics, and the sensitivity that makes them clinically
#  useful comes from isothermal amplification described in that record, not
#  from the cell-free readout.
#
#  `dark.biosecurity` is included because `governance.py` establishes that the
#  control point for this technology is DNA synthesis screening rather than
#  organism containment. That is a biosecurity mechanism, and the edge records
#  a real dependency rather than a caution.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and Goal 3 is the strongest claim any record in this branch makes
#  about direct human benefit.
#
#  A freeze-dried reaction on a paper disc needs no cold chain, no mains power
#  and no laboratory, so a specific molecular diagnosis becomes possible where
#  a molecular laboratory will never exist. That is not an aspiration; it has
#  been demonstrated in the field against outbreak pathogens, and it is
#  recorded in `history.py` with a date.
#
#  Goal 4 is claimed unusually and deliberately: because nothing in the
#  reaction is alive, protein expression can be taught in an ordinary classroom
#  that could not host a containment facility. It is a small claim and it is a
#  real one.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on diagnostics where no laboratory exists
    4,  # Quality education, on teaching without a containment facility
    9,  # Industry and innovation, on prototyping speed for the whole branch
)


# =============================================================================
#  GLOSSARY
#  Grouped: the systems, what drives them, how they are used, and what the
#  absence of a cell changes.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the systems -----------------------------------------------------------
    "cell_free_protein_synthesis",
    "cell_extract",
    "reconstituted_translation_system",
    "cell_lysate",
    "in_vitro_transcription_translation",
    "linear_template",
    # -- what drives the reaction ----------------------------------------------
    "energy_regeneration",
    "cofactor",
    "ribosome",
    "translation",
    "transcription",
    # -- how it is used --------------------------------------------------------
    "continuous_exchange_reaction",
    "lyophilisation",
    "toehold_switch",
    "biosensor",
    "isothermal_amplification",
    "point_of_care_testing",
    "design_build_test_learn",
    # -- what the absence of a cell makes possible -----------------------------
    "non_standard_amino_acid",
    "membrane_protein",
    "glycosylation",
    "redox_potential",
    "protein_folding",
    "on_demand_manufacturing",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "buchner_cell_free_fermentation",
    "nirenberg_matthaei_genetic_code",
    "pure_system_reconstituted_translation",
    "cell_free_energy_regeneration_review",
    "paper_based_cell_free_sensors",
    "field_deployable_zika_sensor",
    "cell_free_prototyping_review",
    "cell_free_glycoprotein_synthesis",
    "on_demand_biologics_review",
    "dna_synthesis_screening_framework",
)


# =============================================================================
#  RELATED
#  Six edges. The first completes the branch's set of answers to what carries
#  out the chemistry.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same work outside a cell, specified differently -------------------
    "white.biocatalysis",
    # -- the living alternative this record is defined against -----------------
    "white.metabolic_engineering",
    # -- where the extract itself has to be grown ------------------------------
    "white.microbial_fermentation",
    # -- the sensors, and where their sensitivity comes from -------------------
    "red.molecular_diagnostics",
    # -- on-demand manufacture of a medicine from a stored template ------------
    "red.pharmaceutical_biotechnology",
    # -- screening the DNA, since that is where the control point moved --------
    "dark.biosecurity",
)
