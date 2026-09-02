# =============================================================================
#  biotechnology.branches.green.agricultural_genome_editing.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two edges below are the most instructive pair in the taxonomy, and they
#  should be followed together.
#
#  `green.plant_genetic_engineering` is the same laboratory, the same people
#  and the same crops, with a completely different regulatory position in most
#  of the world. Reading the two records side by side isolates how much of what
#  is attributed to a technology is actually attributable to the law that
#  governs it.
#
#  `red.gene_therapy` is the same molecular operation on a human being. A
#  CRISPR edit to correct a haemoglobin gene and a CRISPR edit to remove a
#  browning enzyme are the same chemistry with the same tool. One is celebrated
#  and reimbursed at over a million euro per patient; the other is contested and
#  in several jurisdictions prohibited. Nothing in the biology explains that
#  difference, and following the edge is the fastest way to see it.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three. Goal 2 is claimed more confidently here than in
#  `green.plant_genetic_engineering`, because the collapse in cost and timeline
#  genuinely does open crop improvement to minor crops and public-sector
#  breeders, which is the barrier that kept transgenic technology away from the
#  most food-insecure regions. It is claimed on that mechanism, not on
#  deployment, which is still thin.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on access to improvement rather than on yield gains
    13,  # Climate action, on the speed of adapting varieties to shifting
    #     conditions, which is where the timeline advantage matters most
    15,  # Life on land, engaged in both directions: fewer inputs, and open
    #     questions about gene flow and about editing wild relatives
)


# =============================================================================
#  GLOSSARY
#  Grouped as the DESCRIPTION uses them: the tool, what the cell does with the
#  break, what is left behind, and the vocabulary the policy argument runs in.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- the tool ------------------------------------------------------------
    "crispr",
    "guide_rna",
    "nuclease",
    "protospacer_adjacent_motif",
    "base_editing",
    "prime_editing",
    # ---- what the cell does with it -------------------------------------------
    "non_homologous_end_joining",
    "homology_directed_repair",
    "indel",
    "knockout",
    # ---- what is left behind ---------------------------------------------------
    "off_target_effect",
    "protoplast",
    "ribonucleoprotein",
    "segregation",
    # ---- the vocabulary of the policy argument ----------------------------------
    "site_directed_nuclease",
    "cisgenesis",
    "mutagenesis",
    "somaclonal_variation",
)


# =============================================================================
#  REFERENCES
#  The enabling paper, the first regulatory answer reported as news, the
#  livestock proof of concept, and the standard review of agricultural
#  applications.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "jinek2012",  # programmable RNA-guided endonuclease
    "waltz2016",  # the mushroom cleared without regulation
    "whitworth2016",  # PRRS-resistant pigs
    "zhu2020",  # the standard review of CRISPR in agriculture
    "cjeu2018",  # the judgment that split the world in two
)


# =============================================================================
#  RELATED
#  Eight edges. The first and the fifth are the instructive pair described in
#  the header note.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the predecessor, and the contrast that explains this record ----------
    "green.plant_genetic_engineering",
    # ---- what an edited line is crossed into, and how it is selected ----------
    "green.molecular_plant_breeding",
    # ---- the prerequisite nobody mentions until it fails ----------------------
    "green.plant_tissue_culture",
    # ---- editing applied to farm animals rather than to crops -----------------
    "green.animal_biotechnology",
    # ---- the same operation on a human being ----------------------------------
    "red.gene_therapy",
    # ---- where edited drought and salinity traits are headed ------------------
    "brown.drought_tolerance_engineering",
    # ---- the law that decides whether the product may exist -------------------
    "purple.biosafety_law",
    # ---- the patent thicket that decides who may attempt it -------------------
    "purple.biotechnology_patents",
)
