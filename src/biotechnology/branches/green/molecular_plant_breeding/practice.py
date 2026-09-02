# =============================================================================
#  biotechnology.branches.green.molecular_plant_breeding.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications list is grouped by the GENETIC ARCHITECTURE of the trait,
#  because that is what decides which method applies. A trait controlled by one
#  large-effect locus is a marker-assisted selection problem; a trait
#  controlled by thousands of small ones is a genomic selection problem; and
#  applying the wrong method to either wastes a decade.
#
#  Note that the entries in the first group are almost all disease resistance
#  and stress tolerance, while the second group is almost all yield and
#  quality. That is not a coincidence: resistance genes tend to be single and
#  large, and yield is the sum of everything the plant does.
#
#  Editorial rule 6 is easy to satisfy here, because these varieties are grown
#  on tens of millions of hectares and are named in national variety registers.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = [
    "APPLICATIONS",
    "TECHNOLOGIES",
    "ORGANISMS",
    "TECHNIQUES",
    "CHALLENGES",
]


# =============================================================================
#  APPLICATIONS
#  Grouped by genetic architecture, which decides the method.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- few large-effect loci: marker-assisted selection ----------------------
    "Marker-assisted backcrossing of rust resistance genes into elite wheat",
    "Submergence-tolerant rice carrying the SUB1A locus, which survives two "
    "weeks under floodwater and is now grown by millions of smallholders",
    "Pyramiding several bacterial blight resistance genes into one rice variety, "
    "which is impossible to select for by phenotype because one gene masks "
    "another",
    "Downy mildew and virus resistance in vegetable crops",
    "Male sterility and restorer systems for hybrid seed production",
    # -- thousands of small-effect loci: genomic selection ---------------------
    "Genomic selection in hybrid maize breeding programmes",
    "Genomic prediction of grain yield and quality in wheat and barley",
    "Genomic selection in perennial and tree crops, where a single generation "
    "can take a decade and the saving is correspondingly larger",
    # -- traits that are expensive or destructive to measure --------------------
    "Selection for baking and malting quality, which conventionally requires "
    "destroying a sample and running a full process test",
    "Selection for root architecture, which cannot be measured without digging "
    "the plant up",
    # -- speed rather than accuracy ---------------------------------------------
    "Speed breeding under extended photoperiod, delivering up to six "
    "generations a year in wheat instead of one or two",
    "Doubled-haploid production, reaching complete homozygosity in one step "
    "rather than six generations of selfing",
    # -- widening rather than narrowing the base ---------------------------------
    "Pre-breeding from landraces and crop wild relatives, using markers to "
    "track a useful allele through the linkage drag that surrounds it",
    "Purity and identity verification of commercial seed lots",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped along the workflow: genotype, find the associations, build the
#  model, measure the plants, and shorten the cycle.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- genotyping ----------------------------------------------------------
    "Single nucleotide polymorphism genotyping arrays",
    "Genotyping-by-sequencing and skim sequencing, which cost less per sample "
    "and give a different set of markers each time",
    "Targeted amplicon panels for a defined set of known loci",
    "Imputation from a low-density panel to a high-density reference",
    # ---- finding the associations ----------------------------------------------
    "Quantitative trait locus mapping in biparental populations",
    "Genome-wide association studies in diversity panels",
    "Haplotype-based analysis, which uses linked blocks rather than single "
    "markers",
    # ---- building the model -----------------------------------------------------
    "Genomic best linear unbiased prediction and the Bayesian alphabet",
    "Machine-learning predictors for non-additive effects",
    "Multi-environment models incorporating weather and soil covariates, which "
    "is how genotype-by-environment interaction is handled rather than ignored",
    # ---- measuring the plants ----------------------------------------------------
    "High-throughput field phenotyping with drones and multispectral imaging",
    "Automated glasshouse imaging platforms",
    "Near-infrared spectroscopy for grain composition without destroying the "
    "sample",
    # ---- shortening the cycle -----------------------------------------------------
    "Speed breeding under extended photoperiod and early seed harvest",
    "Doubled-haploid production by anther culture or haploid inducer lines",
    "Off-season nurseries in a counter-seasonal location",
)


# =============================================================================
#  ORGANISMS
#  All crops. This record uses no production host and no source organism for a
#  tool, which distinguishes it from every other subtype in the green branch.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "triticum_aestivum",  # bread wheat, hexaploid and the hardest case
    "oryza_sativa",  # rice, where SUB1A is the standard success story
    "zea_mays",  # maize, where genomic selection was adopted first
    "hordeum_vulgare",  # barley
    "glycine_max",  # soybean
    "solanum_tuberosum",  # potato, autotetraploid and therefore awkward
    "musa_acuminata",  # banana, where conventional breeding is nearly impossible
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "pcr",
    "next_generation_sequencing",
    "microarray",
    "electrophoresis",
    "phenotyping",
    "tissue_culture",
    "spectroscopy",
)


# =============================================================================
#  CHALLENGES
#  Three technical, then four that are economic, institutional or strategic.
#  The last is the one that would cost least to fix and is furthest from being
#  fixed.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the central technical weakness ----------------------------------------
    "Prediction accuracy collapses across unrelated germplasm, because a model "
    "trained on elite material has never seen anything like a landrace and "
    "cannot extrapolate to it",
    "Genotype-by-environment interaction under climate variability, where the "
    "best variety in one season is not the best in the next and the training "
    "data describe a climate that is receding",
    "Non-additive effects, meaning dominance and epistasis, which most "
    "prediction models handle badly or not at all",
    # -- the cost has moved --------------------------------------------------------
    "Phenotyping, not genotyping, is now the bottleneck. Reading DNA costs a few "
    "euro; measuring a thousand plots accurately costs far more and attracts far "
    "less funding",
    # -- strategic ------------------------------------------------------------------
    "A narrow elite germplasm base in several major crops, which molecular "
    "selection can reinforce by making it easier to select within what is "
    "already there than to bring in something new",
    # -- institutional ---------------------------------------------------------------
    "Data sharing between public and private breeding programmes, where the "
    "single largest available improvement, meaning larger and more diverse "
    "training populations, is blocked by commercial confidentiality rather than "
    "by any scientific difficulty",
    "Capacity, since the method needs a statistician and a data pipeline as much "
    "as a breeder, and national programmes often have the field sites and not "
    "the analysts",
)
