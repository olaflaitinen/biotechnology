# =============================================================================
#  biotechnology.branches.green.molecular_plant_breeding.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The most instructive edge here points outside the green branch entirely.
#
#  `green.animal_biotechnology` uses the same equation, the same models and in
#  several cases the same software as this record. Genomic selection was
#  proposed for livestock in 2001, adopted by the dairy industry from 2009, and
#  moved into crops afterwards. A reader who understands genomic prediction in
#  wheat understands it in cattle, and the differences that remain are about
#  generation interval and reproductive rate rather than about statistics.
#
#  That shared-method edge is the kind this taxonomy exists to surface: two
#  records in the same branch, describing different kingdoms, running the same
#  mathematics.
#
#  The edge to `gold.machine_learning_in_biology` matters for a different
#  reason. Genomic prediction was doing high-dimensional regression with more
#  predictors than observations two decades before that became fashionable
#  elsewhere, and the field solved the problem with shrinkage and Bayesian
#  priors rather than with deep networks.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Two, both claimed on strong evidence. Goal 2 is the most defensible claim in
#  the green branch: almost all staple crop yield improvement of the last three
#  decades came from breeding, and molecular tools roughly doubled its rate.
#  Goal 15 is claimed cautiously and in both directions, because the same
#  methods that let a breeder mine a landrace also make it easier to keep
#  selecting within an already narrow elite pool.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on realised yield gain in staple crops
    15,  # Life on land, engaged in both directions; see the note above
)


# =============================================================================
#  GLOSSARY
#  Grouped as the DESCRIPTION uses them: what is inherited, what is measured,
#  what is predicted, and how the cycle is shortened.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- what is inherited ---------------------------------------------------
    "allele",
    "haplotype",
    "quantitative_trait_locus",
    "linkage_disequilibrium",
    "additive_genetic_variance",
    # ---- what is measured ------------------------------------------------------
    "marker",
    "genotype",
    "phenotype",
    "heritability",
    "genotype_by_environment_interaction",
    # ---- what is predicted -------------------------------------------------------
    "genomic_estimated_breeding_value",
    "training_population",
    "prediction_accuracy",
    "selection_intensity",
    # ---- how the cycle is shortened -------------------------------------------------
    "backcross",
    "doubled_haploid",
    "generation_interval",
    "landrace",
    "linkage_drag",
)


# =============================================================================
#  REFERENCES
#  The founding law, the paper that reframed the field, the standard modern
#  review, and the protocol that attacked the generation interval.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "mendel1866",  # the founding law
    "meuwissen2001",  # genomic selection, the single most important paper here
    "xu2020",  # the standard modern review across livestock and plants
    "watson2018",  # speed breeding
)


# =============================================================================
#  RELATED
#  Seven edges. The first is the shared-method edge described in the header
#  note and is the most instructive one in the record.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the same equation, a different kingdom ------------------------------
    "green.animal_biotechnology",
    # ---- what an engineered or edited event is crossed into -------------------
    "green.plant_genetic_engineering",
    "green.agricultural_genome_editing",
    # ---- how a doubled haploid or a rescued embryo is actually produced -------
    "green.plant_tissue_culture",
    # ---- where the varieties are headed as the climate moves ------------------
    "brown.arid_land_crops",
    # ---- the statistics and the sequence analysis behind the prediction -------
    "gold.machine_learning_in_biology",
    "gold.genomics_data_analysis",
)
