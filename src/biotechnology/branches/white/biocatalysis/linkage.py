# =============================================================================
#  biotechnology.branches.white.biocatalysis.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `white.industrial_enzymes` is the reciprocal of the edge declared in that
#  record, and the division is worth restating from this side. That record
#  supplies the catalyst and measures it: k_cat, K_M, secreted titre, cost per
#  kilogram of enzyme. This record consumes the catalyst and measures the
#  process: substrate loading, cofactor turnover, process mass intensity. A
#  reader who follows the edge in either direction should find the other half
#  of the same subject rather than a repetition of this one.
#
#  `red.pharmaceutical_biotechnology` is where the value of this record is
#  realised. The routes here mostly exist to make drug substances, and the
#  governance lock described in `governance.py` is a pharmaceutical dossier
#  constraint rather than a chemical one.
#
#  `white.metabolic_engineering` is the deeper alternative and the more
#  interesting edge. Biocatalysis performs one or a few steps outside a cell
#  with purified or immobilised enzymes; metabolic engineering puts the whole
#  pathway inside a living organism and lets it feed itself. The choice between
#  them is a real engineering decision with no general answer: the cell
#  regenerates its own cofactors for nothing, and it also grows, mutates,
#  diverts carbon to biomass, and cannot tolerate what a bare enzyme tolerates.
#
#  `gold.machine_learning_in_biology` is where the 2022 milestone points, and
#  the linkage is recorded with the caution that entry carries.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, each on a specific documented mechanism.
#
#  Goal 3 is claimed on manufacturing cost rather than on discovery: shorter
#  routes with higher yields make medicines cheaper to produce, and the
#  6-aminopenicillanic acid process is the clearest instance, since it
#  underpins the semi-synthetic penicillins.
#
#  Goal 12 is the central claim and it is measurable. Solvent, heavy metal
#  catalyst and protecting group waste avoided are all captured by the process
#  mass intensity metric rather than asserted.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on the manufacturing cost of medicines
    9,  # Industry and innovation, on route redesign in chemical manufacture
    12,  # Responsible production, on solvent, metal and waste avoided
)


# =============================================================================
#  GLOSSARY
#  Grouped: the handedness vocabulary the record is organised around, then the
#  reaction classes, then the process engineering terms.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- handedness, which is what the record is about -------------------------
    "chirality",
    "enantiomer",
    "racemate",
    "enantiomeric_excess",
    "kinetic_resolution",
    "dynamic_kinetic_resolution",
    "stereoselectivity",
    "prochiral",
    # -- the reaction classes --------------------------------------------------
    "hydrolase",
    "lipase",
    "ketoreductase",
    "transaminase",
    "oxidoreductase",
    "aldolase",
    "cytochrome_p450",
    # -- making the process work -----------------------------------------------
    "cofactor",
    "cofactor_regeneration",
    "whole_cell_biocatalysis",
    "immobilisation",
    "two_phase_system",
    "in_situ_product_removal",
    "cascade_reaction",
    "chemoenzymatic_synthesis",
    "retrosynthesis",
    "protecting_group",
    # -- how the route is judged -----------------------------------------------
    "process_mass_intensity",
    "e_factor",
    "atom_economy",
    "space_time_yield",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "sitagliptin_transaminase_process",
    "biocatalysis_in_pharmaceutical_manufacture_review",
    "penicillin_acylase_process_history",
    "green_chemistry_twelve_principles",
    "ich_q11_drug_substance",
    "acs_gci_pmi_conventions",
    "cofactor_regeneration_review",
    "enzymes_in_organic_solvents_review",
    "new_to_nature_carbene_transferase",
    "islatravir_enzymatic_cascade",
)


# =============================================================================
#  RELATED
#  Six edges. The first is the sibling this record is defined against; the
#  third is the genuine strategic alternative.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- who supplies and measures the catalyst --------------------------------
    "white.industrial_enzymes",
    # -- where these routes are actually used ----------------------------------
    "red.pharmaceutical_biotechnology",
    # -- the alternative: put the pathway in a living cell instead -------------
    "white.metabolic_engineering",
    # -- reactor design, scale-up and the flow systems in practice.py ----------
    "white.bioprocess_engineering",
    # -- biobased feedstock for the substrates themselves ----------------------
    "white.biobased_chemicals",
    # -- enzyme selection and variant proposal, with the 2022 caution ----------
    "gold.machine_learning_in_biology",
)
