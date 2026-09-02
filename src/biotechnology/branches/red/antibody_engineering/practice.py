# =============================================================================
#  biotechnology.branches.red.antibody_engineering.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The technologies are grouped along the design loop rather than by chemistry:
#  find a binder, select the good ones, make it human, tune what the tail does,
#  attach a payload, and check it can actually be manufactured. That last step,
#  developability, is where most candidates die, and it is routinely omitted
#  from descriptions of the field because it is unglamorous.
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
#  Ordered by the format each represents, from the plain molecule outward to
#  the formats that no longer look like an antibody at all.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- the plain molecule, blocking or neutralising --------------------------
    "Checkpoint inhibitor antibodies that release a suppressed immune response "
    "against a tumour",
    "Anti-TNF and anti-interleukin antibodies in autoimmune disease",
    "PCSK9 inhibitors that lower circulating cholesterol",
    "CGRP-pathway antibodies for migraine prevention",
    # -- neutralising an external threat ----------------------------------------
    "Long-acting neutralising antibodies for respiratory syncytial virus "
    "prophylaxis in infants",
    "Antivenoms and antitoxins produced as defined recombinant molecules",
    # -- the antibody as a delivery address --------------------------------------
    "Antibody-drug conjugates delivering a cytotoxic payload to a tumour cell",
    "Radioimmunoconjugates for imaging and for targeted radiotherapy",
    # -- two grips at once --------------------------------------------------------
    "Bispecific T-cell engagers that force a synapse between a tumour cell and "
    "a T cell",
    "Bispecific antibodies that replace the function of a missing clotting "
    "factor",
    # -- fragments and single domains ----------------------------------------------
    "Antibody fragments small enough for intravitreal injection into the eye",
    "Nanobody-based imaging agents and intracellular binders",
    # -- outside the clinic ---------------------------------------------------------
    "Diagnostic and research antibodies underpinning most immunoassays",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped along the design loop. The last group is where most candidates die.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- find a binder -------------------------------------------------------
    "Phage display of synthetic and immune libraries",
    "Yeast surface display with fluorescence-activated sorting",
    "Ribosome and mRNA display for libraries beyond cellular transformation "
    "limits",
    "Single B-cell cloning from convalescent or immunised donors",
    "Transgenic mice carrying human immunoglobulin loci",
    "Camelid immunisation for single-domain heavy-chain antibodies",
    # ---- select and improve ---------------------------------------------------
    "Iterative panning with increasing stringency",
    "Affinity maturation by error-prone PCR or targeted library design",
    "Deep mutational scanning of the binding interface",
    # ---- make it human ---------------------------------------------------------
    "Complementarity-determining region grafting onto human frameworks",
    "Germlining to revert non-essential residues to the closest human sequence",
    # ---- tune what the tail does ------------------------------------------------
    "Fc engineering for neonatal Fc receptor binding and extended half-life",
    "Afucosylation to increase antibody-dependent cellular cytotoxicity",
    "Effector-silent Fc variants where recruitment would be harmful",
    # ---- attach a payload --------------------------------------------------------
    "Site-specific conjugation chemistry with defined attachment points",
    "Cleavable and non-cleavable linker design",
    # ---- check it can be made -----------------------------------------------------
    "In silico developability and immunogenicity prediction",
    "High-concentration viscosity and aggregation screening",
    "Forced degradation studies for oxidation, deamidation and isomerisation",
)


# =============================================================================
#  ORGANISMS
#  Unusually long, because this field borrows from more species than any other
#  in the red branch: a camel for the single-domain format, a mouse for the
#  hybridoma, a phage for the display, and a hamster to manufacture the result.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "homo_sapiens",  # the donor of fully human sequences, and the patient
    "mus_musculus",  # hybridomas, and transgenic human-locus strains
    "camelus_dromedarius",  # heavy-chain-only antibodies, the nanobody source
    "escherichia_coli",  # phage display host and fragment expression
    "saccharomyces_cerevisiae",  # yeast surface display
    "cricetulus_griseus",  # CHO cells, where the finished molecule is made
    "oryctolagus_cuniculus",  # rabbit antibodies, favoured for affinity
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "chromatography",
    "flow_cytometry",
    "elisa",
    "surface_plasmon_resonance",
    "mass_spectrometry",
    "x_ray_crystallography",
    "cryo_electron_microscopy",
    "cell_culture",
    "next_generation_sequencing",
)


# =============================================================================
#  CHALLENGES
#  The first three are the delivery constraint named in the description. The
#  last four are commercial and structural.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- delivery, the binding constraint --------------------------------------
    "Poor penetration into solid tumours, where a large molecule must cross a "
    "leaky vasculature and diffuse through dense stroma against raised "
    "interstitial pressure",
    "Almost no transfer across the blood-brain barrier, which excludes most "
    "neurological targets without an active transport strategy",
    "Injection only, since a protein of this size is digested if swallowed, "
    "which limits use in conditions where daily oral dosing is the standard",
    # -- physical chemistry ------------------------------------------------------
    "Aggregation and viscosity at the high concentrations needed to deliver a "
    "large dose in a small subcutaneous volume",
    # -- immunology ---------------------------------------------------------------
    "Anti-drug antibodies that neutralise the therapeutic over months to years, "
    "which is difficult to predict from sequence alone",
    "Cytokine release with agonist and T-cell-engaging formats, requiring "
    "step-up dosing and inpatient monitoring",
    # -- commercial and structural -------------------------------------------------
    "Crowded intellectual property around popular targets, where dozens of "
    "molecules chase the same antigen while neglected targets attract none",
    "Cost of goods for chronic indications, which keeps annual treatment in the "
    "tens of thousands of euro and confines many products to wealthy health "
    "systems",
)
