# =============================================================================
#  biotechnology.branches.green.agricultural_genome_editing
# -----------------------------------------------------------------------------
#  GREEN BIOTECHNOLOGY  ->  AGRICULTURAL GENOME EDITING
#
#  IN ONE SENTENCE, FOR ANYONE
#  Instead of adding a gene from another species, genome editing rewrites a
#  few letters of the crop's own DNA - the same kind of change that happens
#  naturally, but aimed at a chosen spot.
#
#  THE REGULATORY FAULT LINE
#  This subtype is the clearest example in the whole taxonomy of law lagging
#  behind biology. A plant carrying a four-base deletion made by CRISPR is
#  legally a GMO in the European Union and legally conventional in Japan,
#  Argentina and the United States, even though no laboratory test can tell it
#  apart from a spontaneous mutant. The `regulatory_status` field is therefore
#  VARIES, and the reason is recorded here rather than buried in a footnote.
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
    key="agricultural_genome_editing",
    name="Agricultural Genome Editing",
    aliases=("crispr crops", "gene editing crops", "new genomic techniques", "ngt"),
    # -------------------------------------------------------------------------
    #  Technical register
    # -------------------------------------------------------------------------
    summary=(
        "Making targeted, often transgene-free edits in crop and livestock "
        "genomes rather than inserting foreign genes."
    ),
    description=(
        "Genome editing introduces a double-strand break, a nick or a chemical "
        "conversion at a chosen genomic position and lets the cell's own repair "
        "machinery produce the change. Three classes of edit are distinguished "
        "in the policy literature and increasingly in law. A site-directed "
        "nuclease type 1 edit is a small insertion or deletion produced by "
        "error-prone non-homologous end joining, typically knocking a gene out. "
        "Type 2 uses a short repair template to make a precise substitution, "
        "often copying an allele that already exists elsewhere in the species. "
        "Type 3 inserts a whole cassette and is, biologically and legally, "
        "transgenesis. Delivery to plants may use Agrobacterium, in which case "
        "the editing machinery is segregated away in later generations, or "
        "ribonucleoprotein complexes delivered directly into protoplasts, which "
        "leaves no foreign DNA at any stage. Base editors convert one base pair "
        "into another without a double-strand break; prime editors write short "
        "sequences from an attached template. In livestock, editing is applied "
        "in zygotes, and the most advanced applications are disease resistance "
        "and welfare traits such as removing horn growth."
    ),
    # -------------------------------------------------------------------------
    #  Plain-language register
    # -------------------------------------------------------------------------
    plain_language=(
        "All plants and animals accumulate small random changes in their DNA "
        "over generations; that is where the variety in every crop originally "
        "came from. Plant breeders have deliberately increased that randomness "
        "for a century using chemicals and radiation, then selected the useful "
        "results. Genome editing does the same kind of thing but aims: it makes "
        "one small change at one chosen place, usually switching off a gene "
        "that was causing a problem. In most cases nothing from another species "
        "remains in the final plant."
    ),
    analogy=(
        "Older breeding methods were a spelling change made by shaking the "
        "whole book until a letter fell out somewhere. Genome editing is using "
        "the find-and-replace function on one word you have already identified. "
        "The finished book reads the same either way; the difference is how "
        "many other pages were disturbed on the way."
    ),
    why_it_matters=(
        "Editing collapses the cost and the timeline of crop improvement. A "
        "trait that took a decade of backcrossing can be produced in two "
        "generations, and because no foreign gene is present the product may "
        "escape the regulatory burden that made conventional GM viable only "
        "for four global commodity crops. That opens improvement to minor "
        "crops, to public-sector breeders and to national programmes - which "
        "is precisely why the divergent regulatory treatment matters so much "
        "for who benefits."
    ),
    # -------------------------------------------------------------------------
    #  Practice
    # -------------------------------------------------------------------------
    applications=(
        "Non-browning mushrooms and long-shelf-life tomatoes",
        "Reduced-gluten wheat lines for coeliac-tolerant products",
        "Powdery-mildew resistant wheat via MLO knockout",
        "Bacterial-blight resistant rice",
        "High-GABA tomato marketed in Japan",
        "Hornless dairy cattle avoiding painful disbudding",
        "PRRS-virus-resistant pigs",
        "Low-acrylamide and bruise-resistant potato",
    ),
    technologies=(
        "CRISPR-Cas9 and CRISPR-Cas12a nucleases",
        "Cytosine and adenine base editors",
        "Prime editing with engineered reverse transcriptase",
        "Ribonucleoprotein delivery into protoplasts",
        "Haploid induction mediated editing",
        "Transgene segregation in later generations",
        "Whole-genome sequencing for off-target assessment",
        "Multiplexed guide RNA arrays for polyploid species",
    ),
    organisms=(
        "oryza_sativa",
        "triticum_aestivum",
        "zea_mays",
        "solanum_lycopersicum",
        "bos_taurus",
        "sus_scrofa",
        "streptococcus_pyogenes",
    ),
    techniques=(
        "crispr_cas9",
        "plant_transformation",
        "tissue_culture",
        "next_generation_sequencing",
        "pcr",
        "protoplast_transfection",
    ),
    challenges=(
        "Regulatory divergence fragmenting international trade",
        "Detection and traceability when no foreign DNA remains",
        "Editing efficiency in polyploid crops such as bread wheat",
        "Regeneration bottleneck in elite but recalcitrant genotypes",
        "Patent thickets over the editing tools themselves",
        "Public consultation processes that lag behind deployment",
    ),
    # -------------------------------------------------------------------------
    #  Quantitative hooks
    # -------------------------------------------------------------------------
    metrics=(
        Metric(
            name="Editing efficiency",
            symbol="indel%",
            unit="% of alleles edited",
            typical="5 - 90 %",
            formula="editing_efficiency",
            evidence=EvidenceLevel.REVIEWED,
        ),
        Metric(
            name="Off-target rate",
            symbol="OT",
            unit="events/genome",
            typical="0 - 5 detectable sites",
            formula="off_target_rate",
            evidence=EvidenceLevel.REVIEWED,
            note=(
                "Usually far below the mutational load created by the tissue "
                "culture step that accompanies it."
            ),
        ),
        Metric(
            name="Guide RNA on-target score",
            symbol="S_guide",
            unit="-",
            typical="0 - 1, design threshold about 0.6",
            formula="guide_rna_score",
            evidence=EvidenceLevel.REPORTED,
        ),
        Metric(
            name="Generations to a clean line",
            symbol="G_clean",
            unit="generations",
            typical="1 - 3",
            evidence=EvidenceLevel.CONSENSUS,
            note="How long segregating the editing machinery away actually takes.",
        ),
        Metric(
            name="Transgene-free recovery rate",
            symbol="TFR",
            unit="%",
            typical="10 - 50 % of edited lines",
            evidence=EvidenceLevel.REVIEWED,
        ),
    ),
    formulas=(
        "editing_efficiency",
        "off_target_rate",
        "guide_rna_score",
        "mendelian_segregation",
        "melting_temperature",
        "relative_yield",
    ),
    # -------------------------------------------------------------------------
    #  Context
    # -------------------------------------------------------------------------
    maturity=Maturity.COMMERCIAL,
    risk_tier=RiskTier.CONTROLLED,
    scale=Scale.FIELD,
    domains=(Domain.FOOD, Domain.ENVIRONMENT),
    regulatory_status=RegulatoryStatus.VARIES,
    regulations=(
        "Court of Justice of the EU C-528/16 (2018) classifying mutagenesis products",
        "EU proposal on plants obtained by new genomic techniques (2023)",
        "US SECURE rule exempting certain edits from regulation",
        "Japan notification pathway for edits without foreign DNA",
        "Argentina Resolution 173/2015, the first NGT-specific framework",
    ),
    standards=(
        "OECD consensus documents on new plant breeding techniques",
        "ISO 21569 series for GMO detection",
        "Codex Alimentarius principles for food safety assessment",
    ),
    milestones=(
        Milestone(1996, "Zinc finger nucleases demonstrated as programmable cutters"),
        Milestone(2011, "TALEN editing applied to rice disease resistance"),
        Milestone(2012, "CRISPR-Cas9 described as a programmable DNA endonuclease"),
        Milestone(2016, "Non-browning mushroom cleared without regulation in the US"),
        Milestone(2018, "CJEU rules edited plants fall under EU GMO law"),
        Milestone(2021, "High-GABA tomato goes on sale in Japan"),
        Milestone(2023, "European Commission proposes a separate NGT category"),
    ),
    sdgs=(2, 13, 15),
    glossary=(
        "crispr",
        "guide_rna",
        "non_homologous_end_joining",
        "homology_directed_repair",
        "base_editing",
        "off_target_effect",
        "protoplast",
        "site_directed_nuclease",
    ),
    references=("jinek2012", "waltz2016", "cjeu2018", "zhu2020"),
    related=(
        "green.plant_genetic_engineering",
        "green.molecular_plant_breeding",
        "green.animal_biotechnology",
        "red.gene_therapy",
        "purple.biosafety_law",
        "purple.plant_variety_rights",
    ),
)
