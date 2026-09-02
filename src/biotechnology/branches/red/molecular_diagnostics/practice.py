# =============================================================================
#  biotechnology.branches.red.molecular_diagnostics.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The technologies below are grouped by what they are good at rather than by
#  chemistry, because that is the axis on which a laboratory actually chooses.
#  Sensitivity, absolute quantification, speed without instruments, and breadth
#  are four different problems, and no single platform is best at more than two
#  of them.
#
#  The challenges list leads with interpretation rather than with detection,
#  which reflects the binding constraint named in narrative.DESCRIPTION.
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
#  Ordered by how routine each has become, most routine first.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- infectious disease, the highest-volume use ---------------------------
    "Reverse-transcription PCR detection of respiratory and gastrointestinal "
    "viruses",
    "Rapid detection of antimicrobial resistance genes directly from a sample",
    "Blood-borne virus screening of donated blood",
    # -- oncology --------------------------------------------------------------
    "Companion diagnostics that select a targeted cancer therapy",
    "Liquid biopsy for circulating tumour DNA and minimal residual disease",
    "Cervical screening by human papillomavirus testing rather than cytology",
    # -- inherited and prenatal -------------------------------------------------
    "Non-invasive prenatal testing from cell-free DNA in maternal plasma",
    "Newborn screening panels for treatable inherited disorders",
    "Exome and genome sequencing for undiagnosed rare disease",
    # -- unknown cause -----------------------------------------------------------
    "Metagenomic sequencing for infection of unknown origin",
    # -- outside a laboratory -----------------------------------------------------
    "Point-of-care isothermal testing in clinics without laboratory hardware",
    "Self-administered tests taken at home",
    # -- public health -------------------------------------------------------------
    "Wastewater surveillance for community-level pathogen circulation",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the problem each is best at, which is how a laboratory chooses.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- best at sensitivity and throughput ---------------------------------
    "Quantitative real-time PCR with hydrolysis probes",
    "Multiplex panels detecting twenty or more targets in one reaction",
    # ---- best at absolute quantification --------------------------------------
    "Droplet and chip-based digital PCR, counted against a Poisson model",
    # ---- best at working without instruments -----------------------------------
    "Loop-mediated isothermal amplification and recombinase polymerase "
    "amplification",
    "Lateral flow immunoassay strips",
    "CRISPR-Cas12 and Cas13 collateral-cleavage reporters",
    # ---- best at breadth --------------------------------------------------------
    "Targeted next-generation sequencing panels with unique molecular "
    "identifiers",
    "Untargeted shotgun metagenomic sequencing",
    "Nanopore sequencing for long reads at the point of need",
    # ---- what makes any of them usable -------------------------------------------
    "Automated nucleic acid extraction platforms",
    "Sample-to-answer cartridge systems with no manual pipetting",
    "Internal amplification controls that detect inhibition",
    "Bioinformatic variant calling and clinical interpretation pipelines",
    "Curated variant databases with expert classification panels",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "homo_sapiens",  # the patient, and the target in genetic testing
    "thermus_aquaticus",  # source of the thermostable polymerase
    "escherichia_coli",  # enzyme production and control material
    "mycobacterium_tuberculosis",  # the pathogen that drove point-of-care design
    "streptococcus_pyogenes",  # Cas9, and Cas12 relatives, for detection
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "pcr",
    "digital_pcr",
    "next_generation_sequencing",
    "crispr_cas9",
    "elisa",
    "electrophoresis",
    "microscopy",
    "mass_spectrometry",
)


# =============================================================================
#  CHALLENGES
#  Interpretation first, because that is the binding constraint. Then the
#  laboratory problems, then the structural ones.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- interpretation ---------------------------------------------------------
    "Distinguishing infection from colonisation, since a sensitive test finds "
    "organisms that are present but not causing the illness",
    "Variants of uncertain significance in clinical sequencing, which are "
    "found faster than expert panels can classify them",
    "Detecting fragments of a pathogen for weeks after it has stopped being "
    "infectious, which makes a positive result hard to act on",
    # -- laboratory --------------------------------------------------------------
    "Contamination and false positives, an inherent risk of any method that "
    "amplifies a single molecule into a visible signal",
    "Inhibitors in clinical material, particularly stool and blood, which can "
    "produce a false negative that looks exactly like a true one",
    # -- structural ---------------------------------------------------------------
    "Reference ranges and variant databases skewed towards European ancestry, "
    "so a benign variant common in an under-represented population is more "
    "likely to be misclassified as pathogenic",
    "Reimbursement pathways that lag years behind the technology, so a test "
    "that works is not a test that is paid for",
    "The regulatory transition from laboratory-developed tests to certified "
    "devices, which improves oversight and simultaneously removes rare-disease "
    "assays that no manufacturer will ever certify",
)
