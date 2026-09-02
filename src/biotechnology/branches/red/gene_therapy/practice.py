# =============================================================================
#  biotechnology.branches.red.gene_therapy.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE -  what is actually done, with what, and what
#                              stops it working.
# -----------------------------------------------------------------------------
#
#  WHAT LIVES HERE
#      APPLICATIONS   concrete uses, preferably ones that exist rather than
#                     ones that are proposed
#      TECHNOLOGIES   the enabling methods and platforms
#      ORGANISMS      keys into biotechnology.organisms - the biological
#                     systems used as tools or as subjects
#      TECHNIQUES     keys into biotechnology.techniques - the bench methods
#      CHALLENGES     the honest list of what does not work yet
#
#  THE APPLICATIONS RULE
#  An entry in APPLICATIONS must name something a reader could go and look up:
#  an approved product class, a completed trial, a deployed programme. "Could
#  be used for neurodegeneration" is not an application; it is a hope, and
#  hopes belong in CHALLENGES phrased as the obstacle that stands in the way.
#  This rule is what keeps the library from drifting into press-release prose.
#
#  THE CHALLENGES RULE
#  Every subtype must list at least four challenges, and at least one of them
#  must be non-technical - cost, access, regulation, acceptance or capacity.
#  A field described only by its technical obstacles is being described by its
#  own practitioners, and that is a biased sample.
#
#  CROSS-REFERENCE KEYS
#  ORGANISMS and TECHNIQUES are not free text. Each string must resolve in the
#  corresponding registry, and `tests/test_integrity.py` fails the build if one
#  does not. That is what allows the documentation generator to turn every one
#  of them into a working link.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
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
#  Ordered roughly by how established each use is, most established first.
#  Every entry below corresponds to at least one authorised product or one
#  completed registrational trial as of the 2026 data freeze.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- ocular: the first approved in vivo AAV therapy anywhere -------------
    "Adeno-associated virus therapy for inherited retinal dystrophy",
    # -- haemoglobinopathies: the largest patient populations addressed ------
    "Lentiviral gene addition for beta-thalassaemia and sickle cell disease",
    # -- immunodeficiency: where the field began clinically ------------------
    "Ex vivo correction of severe combined immunodeficiency",
    # -- neuromuscular: antisense rather than viral delivery -----------------
    "Antisense oligonucleotides for spinal muscular atrophy",
    # -- cardiometabolic: the first in vivo base-editing programmes ----------
    "In vivo base editing to lower lipoprotein cholesterol",
    # -- oncology: engineered viruses as the therapeutic agent ---------------
    "Oncolytic viruses engineered to replicate in and lyse tumour cells",
    # -- muscular dystrophy: dose-limited by vector requirement --------------
    "AAV micro-dystrophin transfer in Duchenne muscular dystrophy",
    # -- RNA interference: durable knockdown without genome change -----------
    "RNA interference therapeutics for hereditary transthyretin amyloidosis",
    # -- haemophilia: single infusion replacing prophylactic factor ----------
    "AAV factor VIII and factor IX transfer in haemophilia",
)


# =============================================================================
#  TECHNOLOGIES
#  The platform methods. Grouped by function in the comments so that a reader
#  can see the shape of the toolbox rather than a flat list.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- delivery vehicles -------------------------------------------------
    "Adeno-associated virus (AAV) capsid serotypes and engineered variants",
    "Third-generation self-inactivating lentiviral vectors",
    "Lipid nanoparticle encapsulation of messenger and guide RNA",
    "Non-viral transposon systems such as Sleeping Beauty and piggyBac",
    # ---- editing chemistry -------------------------------------------------
    "CRISPR-Cas9 nuclease editing with homology-directed repair",
    "Cytosine and adenine base editors that make no double-strand break",
    "Prime editing with a reverse-transcriptase-fused nickase",
    # ---- expression control ------------------------------------------------
    "Tissue-specific and inducible promoter cassettes",
    "Codon optimisation and intron inclusion for expression strength",
    # ---- manufacture -------------------------------------------------------
    "Suspension HEK293 triple-transfection vector production",
    "Sf9 baculovirus expression for large-scale AAV manufacture",
    "Affinity and ion-exchange purification with full-empty capsid separation",
)


# =============================================================================
#  ORGANISMS
#  Keys into `biotechnology.organisms`. These are the biological systems that
#  appear in the workflow, whether as the subject (the patient), as the source
#  of a tool (the virus), or as a production host.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "homo_sapiens",  # the subject, and the source of the target cells
    "escherichia_coli",  # plasmid production for vector manufacture
    "saccharomyces_cerevisiae",  # historical source of expression elements
    "streptococcus_pyogenes",  # origin of the Cas9 nuclease
    "spodoptera_frugiperda",  # Sf9 cells for baculovirus AAV production
)


# =============================================================================
#  TECHNIQUES
#  Keys into `biotechnology.techniques`. These are bench methods a laboratory
#  would need to be competent in to work on this subtype at all.
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "crispr_cas9",
    "pcr",
    "next_generation_sequencing",
    "flow_cytometry",
    "cell_culture",
    "elisa",
    "chromatography",
    "digital_pcr",
)


# =============================================================================
#  CHALLENGES
#  What genuinely limits the field. Note the mixture required by the challenges
#  rule: the first four are technical, the last three are economic, structural
#  and geopolitical. All seven are load-bearing.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- immunological -------------------------------------------------------
    "Pre-existing neutralising antibodies exclude a large share of patients "
    "from adeno-associated virus therapy, and there is no accepted way to "
    "redose someone who has been treated once",
    # -- safety --------------------------------------------------------------
    "Insertional mutagenesis risk with integrating vectors, demonstrated in "
    "early trials and still a lifelong monitoring obligation",
    "Off-target editing and unintended large deletions or chromosomal "
    "rearrangements that short-read sequencing can miss",
    # -- durability ----------------------------------------------------------
    "Durability of expression in dividing tissue is measured in years rather "
    "than decades, and no product has yet been observed over a full lifespan",
    # -- economic ------------------------------------------------------------
    "Manufacturing yield and cost of goods at commercial scale, which set the "
    "floor under prices that already exceed two million euro per patient",
    # -- structural ----------------------------------------------------------
    "Payer and reimbursement models built for chronic dosing rather than for "
    "a single curative administration",
    # -- geopolitical --------------------------------------------------------
    "Almost no manufacturing or administration capacity outside a small "
    "number of high-income countries, so eligibility is decided by geography",
)
