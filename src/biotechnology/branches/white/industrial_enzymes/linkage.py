# =============================================================================
#  biotechnology.branches.white.industrial_enzymes.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is the upstream neighbour of most of the white branch, and the
#  edges below are structural rather than decorative.
#
#  `white.biocatalysis` is the closest edge and the one most easily confused.
#  The division is deliberate and is worth stating: THIS record is about the
#  enzyme as a manufactured article, meaning how it is discovered, engineered,
#  fermented, formulated and sold. `white.biocatalysis` is about the enzyme as
#  a step in a synthetic route, meaning reaction engineering, solvent choice,
#  cofactor regeneration and cascades. One is the tool; the other is the use.
#  A reader interested in making enzymes belongs here, and a reader interested
#  in using them to make a molecule belongs there.
#
#  `white.microbial_fermentation` and `white.bioprocess_engineering` are how
#  the product in this record is physically manufactured. Every gram of
#  industrial enzyme is a fermentation product first.
#
#  `gold.machine_learning_in_biology` has moved from a peripheral connection to
#  a central one. Structure prediction and sequence-activity models now supply
#  candidates and propose variants, though as `history.py` records for 2021,
#  they do not yet predict activity or stability, so the screening bottleneck
#  in `practice.CHALLENGES` is unchanged.
#
#  `purple.access_benefit_sharing` is included because it binds directly here.
#  An enzyme found by sampling a hot spring or by metagenomic sequencing of
#  soil in another country is a genetic resource under the Nagoya Protocol, and
#  the obligation attaches to the sequence, not only to a physical sample.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and each is claimed on a specific documented mechanism rather than on
#  general merit.
#
#  Goal 6 deserves the note: phytase in feed reduces the phosphorus excreted by
#  pigs and poultry, and phosphorus runoff is a principal cause of algal blooms
#  and dead zones. That is a water quality claim with a measurable pathway, not
#  an environmental slogan.
# =============================================================================
SDGS: Tuple[int, ...] = (
    6,  # Clean water, on phosphorus runoff avoided and effluent load reduced
    9,  # Industry and innovation, on process substitution in manufacturing
    12,  # Responsible production, on solvent, chlorine and waste displaced
    13,  # Climate action, on the wash temperature reduction above all
)


# =============================================================================
#  GLOSSARY
#  Grouped: the kinetic vocabulary, the engineering vocabulary, the process
#  vocabulary, then the enzyme classes a reader meets in `practice.py`.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- how an enzyme is described --------------------------------------------
    "enzyme",
    "active_site",
    "substrate",
    "cofactor",
    "michaelis_constant",
    "turnover_number",
    "catalytic_efficiency",
    "specific_activity",
    "enzyme_unit",
    # -- how it is improved ----------------------------------------------------
    "directed_evolution",
    "rational_design",
    "protein_engineering",
    "thermostability",
    "ancestral_sequence_reconstruction",
    # -- how it is made and used -----------------------------------------------
    "immobilisation",
    "secretion",
    "titre",
    "fermentation",
    "metagenomics",
    "extremophile",
    # -- the classes named in practice.py --------------------------------------
    "protease",
    "amylase",
    "lipase",
    "cellulase",
    "phytase",
    # -- how the environmental claims are measured -----------------------------
    "e_factor",
    "atom_economy",
    "life_cycle_assessment",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "industrial_enzymes_market_review",
    "directed_evolution_nobel_lecture",
    "enzyme_immobilisation_review",
    "detergent_enzyme_lca",
    "phytase_feed_phosphorus_review",
    "iubmb_enzyme_nomenclature",
    "amfep_safe_handling_guidance",
    "jecfa_enzyme_specifications",
    "green_chemistry_metrics_review",
)


# =============================================================================
#  RELATED
#  Seven edges, ordered as a reader should follow them: the sibling that is
#  most often confused with this record first, then manufacture, then use.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the tool versus the use of the tool -----------------------------------
    "white.biocatalysis",
    # -- how the enzyme is physically made -------------------------------------
    "white.microbial_fermentation",
    "white.bioprocess_engineering",
    # -- engineering the host that secretes it ---------------------------------
    "white.metabolic_engineering",
    # -- the largest single unsolved cost problem, in biomass conversion -------
    "white.biofuels",
    # -- where the enzymes end up in the food chain ----------------------------
    "yellow.food_safety_biotechnology",
    # -- who owns a sequence sampled from someone else's territory -------------
    "purple.access_benefit_sharing",
)
