# =============================================================================
#  biotechnology.branches.yellow.cultivated_meat.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `red.regenerative_medicine` is the edge that carries the most information in
#  this record, and it is not an analogy. It is the same physical constraint.
#
#  That record is organised around the oxygen diffusion limit of roughly one to
#  two hundred micrometres, beyond which tissue cannot be kept alive without a
#  vascular supply. This record hits the identical wall for the identical
#  reason, which is why formed products from loose cells are on sale and whole
#  cuts are not. Two fields with entirely different purposes, funding and
#  regulators are blocked by one number, and neither has solved it.
#
#  `yellow.alternative_proteins` and `yellow.precision_fermentation` complete
#  the spectrum by how much of the animal is retained: none, one molecule, the
#  cells themselves. Cost and regulatory burden rise in that order, and so does
#  the claim to be the thing rather than a version of it. This record is the
#  expensive end of all three.
#
#  `white.bioprocess_engineering` holds the scale-up problem, and the edge is
#  deliberate rather than routine. That record's cost structure is for a
#  product worth thousands of euro per kilogram. Applying it to one worth a few
#  euro is the whole difficulty here, and reading the two together shows why
#  inherited pharmaceutical equipment is the wrong tool rather than merely an
#  expensive one.
#
#  `purple.bioethics` is included because this record's strongest argument is
#  ethical rather than environmental: it removes the animal entirely rather
#  than reducing its suffering, which is a different claim from any other
#  record in the library makes.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and all three are claimed conditionally, which is unusual and is
#  correct for a record at PILOT maturity.
#
#  Goal 3 is the most defensible and the least discussed: a process with no
#  living animal has no enteric pathogen reservoir, needs no antibiotics and
#  presents no zoonotic risk. That is a genuine benefit of the method rather
#  than of the scale, so it holds at kilogram production as well as it would at
#  tonne production.
#
#  Goal 12 and Goal 15 are claimed CONDITIONALLY, on the technology reaching
#  scale. At present production volumes neither is delivered in any measurable
#  quantity, and `metrics.py` records genuine disagreement about whether the
#  greenhouse gas comparison favours this record at all.
#
#  GOAL 13 IS DELIBERATELY NOT CLAIMED, which for a technology usually
#  presented as a climate measure is the significant omission in this facet.
#  Published assessments disagree on whether cultivated meat beats conventional
#  beef, and the answer turns on the energy source. A goal claim requires more
#  than a disputed comparison, and claiming it would be the clearest possible
#  failure of the sceptical-auditor test in rule 12.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on zoonotic risk and antibiotic use removed by the method
    12,  # Responsible production, conditional on reaching scale
    15,  # Life on land, conditional on reaching scale
)


# =============================================================================
#  GLOSSARY
#  Grouped: the cells, the medium, the vessel, the structure, and the market.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the cells -------------------------------------------------------------
    "cultivated_meat",
    "cell_line",
    "primary_cell",
    "immortalisation",
    "replicative_senescence",
    "myoblast",
    "adipocyte",
    "differentiation",
    "suspension_adaptation",
    # -- the medium, which is the cost -----------------------------------------
    "growth_medium",
    "foetal_bovine_serum",
    "serum_free_medium",
    "growth_factor",
    "medium_recycling",
    # -- the vessel ------------------------------------------------------------
    "bioreactor",
    "perfusion_culture",
    "microcarrier",
    "shear_stress",
    "cell_density",
    "oxygen_transfer_coefficient",
    # -- the structure problem -------------------------------------------------
    "scaffold",
    "tissue_engineering",
    "vascularisation",
    "diffusion_limit",
    "co_culture",
    # -- the market ------------------------------------------------------------
    "novel_food",
    "hybrid_product",
    "cost_of_goods",
    "life_cycle_assessment",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "cultivated_meat_technoeconomic_analysis",
    "first_cultured_burger_2013",
    "serum_free_medium_cultivated_meat",
    "singapore_cultivated_chicken_approval",
    "us_cultivated_meat_joint_oversight",
    "cultivated_meat_lca_disagreement",
    "scaffold_and_structure_review",
    "immortalised_cell_lines_food_use",
    "italy_cultivated_meat_prohibition",
    "cultivated_meat_scale_up_constraints",
)


# =============================================================================
#  RELATED
#  Seven edges. The first is the same physical wall, not an analogy.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the identical diffusion limit, blocking both fields -------------------
    "red.regenerative_medicine",
    # -- the other two answers to the same question ----------------------------
    "yellow.alternative_proteins",
    "yellow.precision_fermentation",
    # -- the scale-up problem, at a thousandth of the product value ------------
    "white.bioprocess_engineering",
    # -- the incumbent, and the welfare argument this record removes -----------
    "green.animal_biotechnology",
    # -- cultivated seafood, and the wild stock argument -----------------------
    "blue.aquaculture_biotechnology",
    # -- the ethical claim, which is this record's strongest -------------------
    "purple.bioethics",
)
