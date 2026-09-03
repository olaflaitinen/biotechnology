# =============================================================================
#  biotechnology.branches.blue.marine_biomaterials.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The most useful edge here is the contrast with `blue.marine_natural_products`,
#  because the two records sit at opposite ends of the same branch problem.
#
#      marine_natural_products   a gram per tonne, from animals that cannot be
#                                farmed. SUPPLY is the constraint, and
#                                SCALE = BENCH.
#      marine_biomaterials       waste from industries already landing it by
#                                the tonne. VARIABILITY is the constraint, and
#                                SCALE = INDUSTRIAL.
#
#  Both are marine, both are extracted from organisms, and the constraints are
#  opposite. A reader who has taken the branch's supply argument from the other
#  record needs this one to see that the argument is about scarcity of a
#  metabolite rather than about the sea.
#
#  `white.biopolymers` is the edge that most needs stating for a reader
#  interested in materials. That record is about polymers as a class, with its
#  two-axis biobased and biodegradable framing; this one is about a specific
#  marine source with a specific variability problem. Alginate and chitosan are
#  biobased and biodegradable polymers and would sit comfortably in that
#  record's quadrant table, and what is not transferable is the raw material
#  question, which is entirely this record's own.
#
#  `blue.seaweed_cultivation` and `blue.aquaculture_biotechnology` are the
#  suppliers, and the relationship is unusual: this record consumes what those
#  two discard. `grey.wastewater_treatment` is included for the same reason
#  from the other direction, since valorising a waste stream is the alternative
#  to treating it.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four. Goal 12 is the primary claim and the strongest in the branch.
#
#  Responsible production is claimed on a mechanism that is unusually direct:
#  the raw materials of this record are streams that industries were paying to
#  dispose of. Shell, skin and scale become products rather than waste. That is
#  circularity in the literal sense rather than as a framing.
#
#  Goal 3 is claimed on the medical applications, which are specific and in
#  clinical use rather than proposed.
#
#  GOAL 14 IS CLAIMED NARROWLY AND WITH ONE HISTORICAL QUALIFICATION. Using
#  by-products reduces waste entering coastal waters, which is a genuine
#  benefit. But this record also contains an application, coral bone graft,
#  that damaged reefs until it was replaced by synthesis. The claim is made on
#  present practice and the history is recorded rather than forgotten.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on wound care, haemostasis and bone graft in clinical use
    9,  # Industry and innovation, on materials with no synthetic equivalent
    12,  # Responsible production, on by-product valorisation, the primary claim
    14,  # Life below water, on waste diverted, with the coral history noted
)


# =============================================================================
#  GLOSSARY
#  Grouped: the materials, the parameters that define which material you have,
#  what is made from them, and the structural half.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the materials ---------------------------------------------------------
    "alginate",
    "agarose",
    "carrageenan",
    "fucoidan",
    "chitin",
    "chitosan",
    "marine_collagen",
    "gelatin",
    "biosilica",
    "nacre",
    # -- which material do you actually have -----------------------------------
    "degree_of_deacetylation",
    "uronic_acid_ratio",
    "sulphation_pattern",
    "molecular_weight_distribution",
    "dispersity",
    "reference_material",
    # -- what is made from them ------------------------------------------------
    "hydrogel",
    "crosslinking",
    "cell_encapsulation",
    "scaffold",
    "haemostatic_agent",
    "bioink",
    "excipient",
    "electrospinning",
    # -- the structural half ---------------------------------------------------
    "biomineralisation",
    "biomimetics",
    "hierarchical_structure",
    "fracture_toughness",
    "wet_adhesion",
    "byssus",
    # -- where it comes from ---------------------------------------------------
    "animal_by_product",
    "valorisation",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "marine_biomaterials_review",
    "chitosan_properties_and_applications",
    "alginate_biomedical_review",
    "marine_collagen_review",
    "coral_bone_graft_substitute_history",
    "mussel_adhesive_catechol_chemistry",
    "nacre_structure_toughness",
    "marine_biomaterial_standardisation_gap",
    "seafood_waste_valorisation_review",
    "iso_10993_biological_evaluation",
)


# =============================================================================
#  RELATED
#  Six edges. The first is the contrast that explains the branch.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the opposite constraint at the other end of the same branch -----------
    "blue.marine_natural_products",
    # -- the seaweed these polysaccharides come from ---------------------------
    "blue.seaweed_cultivation",
    # -- polymers as a class, with the biobased and biodegradable framing ------
    "white.biopolymers",
    # -- where the shell and skin waste originates -----------------------------
    "blue.aquaculture_biotechnology",
    # -- scaffolds, encapsulation and the clinical applications ----------------
    "red.regenerative_medicine",
    # -- valorising a waste stream as the alternative to treating it -----------
    "grey.wastewater_treatment",
)
