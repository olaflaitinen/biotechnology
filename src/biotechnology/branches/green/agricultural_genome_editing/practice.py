# =============================================================================
#  biotechnology.branches.green.agricultural_genome_editing.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications are grouped by EDIT CLASS rather than by crop, because the
#  class is what determines the regulatory treatment and therefore whether the
#  product can exist at all in a given country. A knockout and a cassette
#  insertion are the same laboratory afternoon and completely different legal
#  objects.
#
#  Note how many entries are knockouts. Removing a gene is far easier than
#  adding a function, so the deployed trait set is dominated by traits that
#  consist of switching something off: a browning enzyme, a susceptibility
#  gene, a horn-growth locus, an antinutrient pathway. That asymmetry shapes
#  the field more than any policy does.
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
#  Grouped by edit class, because the class decides the legal object.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- type 1 knockouts in plants: the great majority of deployed edits -----
    "Non-browning mushrooms, produced by knocking out a polyphenol oxidase "
    "gene, and the first edited organism cleared without regulation in the "
    "United States",
    "Powdery-mildew resistant wheat, by knocking out all six copies of the MLO "
    "susceptibility gene",
    "Bacterial-blight resistant rice, by editing the promoters the pathogen "
    "hijacks rather than the genes themselves",
    "Reduced-gluten wheat lines for people who cannot tolerate conventional "
    "wheat",
    "Low-acrylamide and bruise-resistant potato",
    "Waxy maize with an altered starch profile",
    # -- type 2 substitutions: copying an allele the species already has ------
    "Herbicide-tolerant oilseed rape carrying a substitution found in natural "
    "populations",
    "High-oleic soybean produced by precise base changes in fatty acid "
    "desaturase genes",
    # -- edits that add a trait rather than remove one -------------------------
    "High-GABA tomato, the first edited food sold in Japan, produced by "
    "truncating an autoinhibitory domain",
    # -- livestock ---------------------------------------------------------------
    "Hornless dairy cattle carrying the POLLED allele, avoiding painful "
    "disbudding",
    "Pigs resistant to porcine reproductive and respiratory syndrome virus, by "
    "editing the CD163 receptor the virus requires",
    "Heat-tolerant cattle carrying a slick-coat allele from tropical breeds",
    # -- research tools that reach the field indirectly -------------------------
    "Haploid inducer lines that carry editing machinery and deliver it during "
    "crossing, leaving an edited but machinery-free progeny",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by what part of the problem each solves: aim, edit, deliver, remove
#  the machinery, and prove what was done.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- aiming ---------------------------------------------------------------
    "CRISPR-Cas9, the workhorse nuclease",
    "CRISPR-Cas12a, which recognises a different sequence motif and so reaches "
    "targets Cas9 cannot",
    "Multiplexed guide RNA arrays, essential in polyploid crops where the same "
    "gene exists in three or six copies that must all be hit",
    "Guide RNA design software scoring on-target activity and predicted "
    "off-target sites",
    # ---- editing without cutting -----------------------------------------------
    "Cytosine and adenine base editors, which convert one base pair chemically "
    "and make no double-strand break",
    "Prime editors, which write a short defined sequence from an attached "
    "template",
    # ---- getting the machinery in -----------------------------------------------
    "Agrobacterium delivery followed by segregation of the transgene in later "
    "generations",
    "Ribonucleoprotein delivery into protoplasts, which introduces no DNA at "
    "any point",
    "Biolistic delivery of ribonucleoprotein into immature embryos",
    "Haploid induction mediated editing, which delivers the machinery through "
    "a cross",
    "Zygote electroporation and microinjection in livestock",
    # ---- getting a plant back ----------------------------------------------------
    "Protoplast regeneration, which is the limiting step in most species",
    "Developmental regulators that make recalcitrant genotypes regenerable",
    # ---- proving what was done -----------------------------------------------------
    "Amplicon sequencing of the target site to quantify editing outcomes",
    "Whole-genome sequencing for off-target and structural change assessment",
    "PCR screening to confirm absence of the editing construct",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "streptococcus_pyogenes",  # the source of Cas9
    "oryza_sativa",  # rice, the model and a major target crop
    "triticum_aestivum",  # bread wheat, hexaploid and therefore the hard case
    "zea_mays",  # maize, where haploid induction editing was developed
    "solanum_lycopersicum",  # tomato, the first edited food sold in Japan
    "bos_taurus",  # cattle, POLLED and slick-coat edits
    "sus_scrofa",  # pigs, CD163 disease resistance
    "agrobacterium_tumefaciens",  # still the main delivery vehicle
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "crispr_cas9",
    "plant_transformation",
    "tissue_culture",
    "protoplast_transfection",
    "next_generation_sequencing",
    "pcr",
    "electrophoresis",
    "phenotyping",
)


# =============================================================================
#  CHALLENGES
#  Two biological, then five that are legal, commercial or institutional. The
#  weighting reflects where the field actually loses time.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- biological -------------------------------------------------------------
    "The regeneration bottleneck, since an edited cell is worthless until it "
    "becomes a plant, and elite genotypes are frequently the hardest to "
    "regenerate",
    "Editing efficiency in polyploid crops such as bread wheat, where the same "
    "gene exists in three genomes and every copy must be hit before the "
    "phenotype appears",
    # -- legal --------------------------------------------------------------------
    "Regulatory divergence that fragments international trade, so the same "
    "grain is conventional in one port and unauthorised in the next",
    "Detection and traceability where no foreign DNA remains, which makes "
    "enforcement of that divergence arguably impossible and leaves every side "
    "of the argument uncomfortable",
    # -- commercial -----------------------------------------------------------------
    "Patent thickets over the editing tools themselves, so freedom to operate "
    "rather than biology decides what a small breeder may attempt",
    # -- institutional ------------------------------------------------------------
    "Public consultation processes that have run years behind deployment, so "
    "products reached markets before the conversation about them had happened",
    "An evidence base still dominated by the first decade of the technology, "
    "with little long-term field data on edited lines under commercial "
    "cultivation",
)
