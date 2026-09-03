# =============================================================================
#  biotechnology.branches.yellow.precision_fermentation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Three edges do real work here and each is a comparison rather than a
#  pointer.
#
#  `yellow.food_fermentation` is the reciprocal of the comparison that record
#  makes. Same biology, opposite regulatory position, and the variable is
#  consumption history rather than hazard. Following the edge in either
#  direction teaches the same lesson about what food regulation actually
#  measures.
#
#  `white.microbial_fermentation` and `white.bioprocess_engineering` hold the
#  manufacturing problem. This record's binding constraint is cost per
#  kilogram, and the reason it binds is the downstream cost share that the
#  bioprocess record documents for therapeutic proteins. The difference is that
#  a therapeutic protein can carry that cost and a food ingredient cannot,
#  which is why food-grade purity limits matter economically rather than only
#  technically.
#
#  `yellow.alternative_proteins` is the competitor most readers conflate with
#  this record and the distinction is worth stating: a plant-based product is a
#  DESCRIPTION of an animal product and this is a COPY of one. They compete for
#  the same shelf and solve different problems, and a reader who treats them as
#  one category will misread both.
#
#  `red.pharmaceutical_biotechnology` is where the technique came from, and the
#  edge exists to keep this record honest about its own novelty.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and each is narrowed deliberately.
#
#  Goal 3 is claimed on the specific products with no practical alternative
#  source: vitamin B12 for people eating no animal products, and the human milk
#  oligosaccharides authorised for infant formula. It is not claimed on protein
#  nutrition generally, since dairy and egg protein are not in short supply
#  where this record's products are sold.
#
#  Goal 12 is claimed on displacing animal production for the functional
#  proteins, which is real and quantified in `metrics.py` with the
#  qualification that sugar feedstock is grown on farmland.
#
#  GOAL 2 IS DELIBERATELY NOT CLAIMED. Zero hunger would be an easy claim for a
#  protein technology and it does not survive the sceptical-auditor test: these
#  products are sold at a premium in wealthy markets, and a technology whose
#  cost problem is that it cannot yet match a commodity is not addressing food
#  insecurity. `yellow.biofortification` claims that goal and can support it.
#
#  GOAL 13 IS ALSO NOT CLAIMED, for the reason `metrics.py` gives: the
#  emissions figures are graded REPORTED, are mostly produced by interested
#  parties, and assume a scale not yet achieved. The direction is plausible and
#  a goal claim requires more than plausibility.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on B12 and infant formula oligosaccharides specifically
    9,  # Industry and innovation, on the manufacturing route itself
    12,  # Responsible production, on animal production displaced
)


# =============================================================================
#  GLOSSARY
#  Grouped: what the thing is, how it is made, how identity is proved, and what
#  is claimed for it.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- what it is ------------------------------------------------------------
    "precision_fermentation",
    "recombinant_protein",
    "heterologous_expression",
    "animal_free_protein",
    "novel_food",
    "substantial_equivalence",
    # -- how it is made --------------------------------------------------------
    "expression_host",
    "secretion",
    "titre",
    "fed_batch_culture",
    "downstream_processing",
    "codon_optimisation",
    "contained_use",
    # -- proving it is the same ------------------------------------------------
    "sequence_identity",
    "glycosylation",
    "post_translational_modification",
    "host_cell_protein",
    "allergenicity",
    # -- the proteins themselves -----------------------------------------------
    "beta_lactoglobulin",
    "casein",
    "ovalbumin",
    "chymosin",
    "lactoferrin",
    "human_milk_oligosaccharide",
    "heme_protein",
    # -- what is claimed -------------------------------------------------------
    "life_cycle_assessment",
    "land_use_change",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "recombinant_insulin_approval",
    "fermentation_chymosin_history",
    "novel_food_regulation_eu",
    "precision_fermentation_technoeconomic_analysis",
    "dairy_protein_fermentation_lca",
    "human_milk_oligosaccharide_authorisation",
    "heme_protein_novel_food_assessment",
    "recombinant_bst_controversy",
    "qps_microorganisms_list",
    "food_protein_functionality_review",
)


# =============================================================================
#  RELATED
#  Six edges. The first is the comparison this record exists to make.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- same biology, opposite regulatory position ----------------------------
    "yellow.food_fermentation",
    # -- a description of an animal product, against a copy of one -------------
    "yellow.alternative_proteins",
    # -- where the technique came from, forty years earlier --------------------
    "red.pharmaceutical_biotechnology",
    # -- how the protein is actually manufactured ------------------------------
    "white.microbial_fermentation",
    # -- the downstream cost that decides whether it is affordable -------------
    "white.bioprocess_engineering",
    # -- the strain engineering behind the host --------------------------------
    "white.metabolic_engineering",
)
