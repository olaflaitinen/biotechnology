# =============================================================================
#  biotechnology.branches.green.molecular_plant_breeding
# -----------------------------------------------------------------------------
#  GREEN BIOTECHNOLOGY  ->  MOLECULAR PLANT BREEDING
#
#  IN ONE SENTENCE, FOR ANYONE
#  Ordinary plant breeding, made far faster by reading a seedling's DNA to
#  predict what the adult plant will be like, instead of waiting a season to
#  find out.
#
#  WHY THIS IS THE QUIET GIANT OF GREEN BIOTECHNOLOGY
#  Genetic engineering attracts the argument; marker-assisted and genomic
#  selection deliver most of the actual yield gain. Nothing here creates a
#  genetically modified organism: the alleles being selected already exist in
#  the species. That is why the `regulatory_status` is UNREGULATED while the
#  neighbouring modules are not.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ...core.enums import (
    Domain,
    EvidenceLevel,
    Maturity,
    RegulatoryStatus,
    RiskTier,
    Scale,
)
from ...core.models import Metric, Milestone, Subtype

__all__ = ["SUBTYPE"]


SUBTYPE = Subtype(
    key="molecular_plant_breeding",
    name="Molecular Plant Breeding",
    aliases=("marker assisted selection", "genomic selection", "mas", "plant breeding"),
    summary=(
        "Accelerating conventional breeding with DNA markers and genomic "
        "prediction so that selection happens at the seedling stage."
    ),
    description=(
        "Classical breeding evaluates a plant by growing it: phenotype is "
        "observed, superior individuals are crossed, and the cycle repeats "
        "once per season. Molecular breeding replaces part of that observation "
        "with genotyping. Marker-assisted selection works where a trait is "
        "controlled by one or a few large-effect loci: a DNA marker tightly "
        "linked to the favourable allele is scored in a seedling and the "
        "unwanted individuals are discarded before they occupy field space. "
        "Marker-assisted backcrossing additionally selects against the donor "
        "genome elsewhere, recovering the recurrent parent in three "
        "generations rather than six. Most traits of economic value, however, "
        "are polygenic, and for those genomic selection is used: a training "
        "population is both genotyped and phenotyped, a statistical model "
        "estimates the effect of every marker simultaneously, and the model "
        "then predicts a genomic estimated breeding value for candidates that "
        "have never been grown. Combined with speed breeding under extended "
        "photoperiod, this compresses the breeding cycle from years to months "
        "and raises the rate of genetic gain per unit time, which is the "
        "quantity breeders actually optimise."
    ),
    plain_language=(
        "Breeding a better wheat variety used to mean planting thousands of "
        "seedlings, waiting a whole season, measuring which ones did best, and "
        "starting again. Now a tiny piece of leaf from a two-week-old seedling "
        "can be tested, and its DNA read like a form guide. The plants unlikely "
        "to perform are removed before they take up space, and only the "
        "promising ones are grown on. The plants themselves are ordinary; the "
        "speed of choosing between them is what changed."
    ),
    analogy=(
        "It is the difference between auditioning every candidate for a "
        "full season and reading their references first. The audition still "
        "happens, but only for the shortlist, so the same effort covers far "
        "more candidates."
    ),
    why_it_matters=(
        "Almost all of the yield improvement in the world's staple crops over "
        "the last thirty years came from breeding, not from transgenes, and "
        "molecular tools roughly doubled the rate at which breeders can "
        "deliver it. Because nothing foreign is introduced, the resulting "
        "varieties face no special regulatory hurdle anywhere, which makes "
        "this the most transferable technology in the green branch: national "
        "programmes and CGIAR centres use it as routinely as multinationals do."
    ),
    applications=(
        "Marker-assisted backcrossing of rust resistance into elite wheat",
        "Submergence-tolerant rice carrying the SUB1A locus",
        "Genomic selection in hybrid maize breeding programmes",
        "Pyramiding of several resistance genes into one variety",
        "Speed breeding with extended photoperiod and early seed harvest",
        "Quality trait selection for protein, oil and starch composition",
        "Purity and identity testing of commercial seed lots",
        "Pre-breeding from landraces and crop wild relatives",
    ),
    technologies=(
        "Single nucleotide polymorphism genotyping arrays",
        "Genotyping-by-sequencing and skim sequencing",
        "Quantitative trait locus mapping in biparental populations",
        "Genome-wide association studies in diversity panels",
        "Genomic prediction models such as GBLUP and Bayesian alphabet",
        "Doubled-haploid production for instant homozygosity",
        "High-throughput field phenotyping with drones and spectral imaging",
        "Environment covariates and genotype-by-environment models",
    ),
    organisms=(
        "triticum_aestivum",
        "oryza_sativa",
        "zea_mays",
        "hordeum_vulgare",
        "glycine_max",
        "solanum_tuberosum",
    ),
    techniques=(
        "pcr",
        "next_generation_sequencing",
        "microarray",
        "electrophoresis",
        "phenotyping",
    ),
    challenges=(
        "Prediction accuracy collapses across unrelated germplasm",
        "Genotype-by-environment interaction under climate variability",
        "Phenotyping, not genotyping, is now the cost bottleneck",
        "Narrow elite germplasm base in several major crops",
        "Data sharing between public and private breeding programmes",
    ),
    metrics=(
        Metric(
            name="Narrow-sense heritability",
            symbol="h2",
            unit="-",
            typical="0.1 (yield) - 0.9 (plant height)",
            formula="heritability",
            evidence=EvidenceLevel.CONSENSUS,
            note="The fraction of observed variation that is additive genetic.",
        ),
        Metric(
            name="Response to selection",
            symbol="R",
            unit="trait units per cycle",
            typical="crop- and trait-specific",
            formula="breeders_equation",
            evidence=EvidenceLevel.CONSENSUS,
            note="R = h2 * S, the breeder's equation.",
        ),
        Metric(
            name="Genetic gain per year",
            symbol="dG/t",
            unit="%/year",
            typical="0.5 - 2.5 %/year",
            formula="genetic_gain",
            evidence=EvidenceLevel.REVIEWED,
        ),
        Metric(
            name="Prediction accuracy",
            symbol="r_gy",
            unit="-",
            typical="0.3 - 0.7",
            formula="prediction_accuracy",
            evidence=EvidenceLevel.REVIEWED,
        ),
        Metric(
            name="Selection intensity",
            symbol="i",
            unit="standard deviations",
            typical="1.0 - 2.7",
            formula="selection_intensity",
            evidence=EvidenceLevel.CONSENSUS,
        ),
    ),
    formulas=(
        "heritability",
        "breeders_equation",
        "genetic_gain",
        "selection_intensity",
        "prediction_accuracy",
        "hardy_weinberg",
        "mendelian_segregation",
        "linkage_disequilibrium",
    ),
    maturity=Maturity.ESTABLISHED,
    risk_tier=RiskTier.ROUTINE,
    scale=Scale.FIELD,
    domains=(Domain.FOOD,),
    regulatory_status=RegulatoryStatus.UNREGULATED,
    regulations=(
        "UPOV Convention on the protection of new plant varieties",
        "EU Regulation (EU) 2016/2031 on plant health",
        "National seed certification and variety registration laws",
        "Nagoya Protocol where germplasm crosses borders",
    ),
    standards=(
        "UPOV DUS testing: distinctness, uniformity and stability",
        "ISTA rules for seed testing",
        "OECD seed schemes for varietal certification",
    ),
    milestones=(
        Milestone(1865, "Mendel reports the laws of inheritance"),
        Milestone(1908, "Hardy and Weinberg describe population allele equilibrium"),
        Milestone(1936, "Lush formalises the breeder's equation"),
        Milestone(1980, "Restriction fragment length polymorphism markers introduced"),
        Milestone(1996, "First large-scale marker-assisted selection programmes"),
        Milestone(2001, "Meuwissen and colleagues propose genomic selection"),
        Milestone(2006, "SUB1A submergence tolerance transferred into mega-varieties"),
        Milestone(2018, "Speed breeding protocols published for major cereals"),
    ),
    sdgs=(2, 15),
    glossary=(
        "allele",
        "marker",
        "quantitative_trait_locus",
        "heritability",
        "backcross",
        "genomic_estimated_breeding_value",
        "landrace",
        "doubled_haploid",
    ),
    references=("mendel1866", "meuwissen2001", "xu2020", "watson2018"),
    related=(
        "green.plant_genetic_engineering",
        "green.agricultural_genome_editing",
        "gold.machine_learning_in_biology",
        "gold.genomics_data_analysis",
        "purple.plant_variety_rights",
        "brown.arid_land_crops",
    ),
)
