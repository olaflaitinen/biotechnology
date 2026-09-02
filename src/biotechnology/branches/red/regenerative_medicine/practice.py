# =============================================================================
#  biotechnology.branches.red.regenerative_medicine.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications list is ordered by TISSUE THICKNESS, which sounds arbitrary
#  and is in fact the organising principle of the entire field. Everything at
#  the top of the list is thin enough to survive on diffusion and has been in
#  hospitals for years. Everything at the bottom needs a blood supply and is in
#  trials or in a laboratory. Nothing in between is missing because of cell
#  biology.
#
#  Editorial rule 6 was applied strictly here, because this is a field with a
#  long history of announcements that did not become treatments. Every entry
#  names something that has treated patients or has completed a registrational
#  trial. Proposals are in CHALLENGES, phrased as obstacles.
#
#  TECHNOLOGIES is grouped by which of the three components it serves, so that
#  the three-legged structure from the description stays visible.
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
#  Ordered by thickness, which is the same as ordering by how long ago each
#  reached patients. See the header note.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- thin enough to live on diffusion: in hospitals since the 1980s -------
    "Cultured epidermal autografts for extensive burns",
    "Limbal stem cell grafts for corneal surface restoration after chemical "
    "injury",
    "Autologous chondrocyte implantation for cartilage defects",
    # -- acellular or slowly recellularised scaffolds --------------------------
    "Decellularised heart valve and vascular grafts",
    "Scaffold-guided bone regeneration in maxillofacial and dental surgery",
    "Acellular dermal matrices in reconstructive surgery",
    # -- cells without an engineered structure ---------------------------------
    "Autologous chondrocyte and keratinocyte suspensions applied as sprays",
    # -- thicker constructs, in trials ------------------------------------------
    "Bioprinted skin and cartilage constructs in clinical trials",
    "Engineered airway and urethral segments in small series",
    # -- not implanted at all: the fastest-growing use --------------------------
    "Patient-derived organoids for drug response prediction",
    "Organoid disease models for inherited disorders",
    "Organ-on-a-chip systems accepted in some regulatory submissions in place "
    "of animal data",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by which leg of the three-legged stool each serves, plus the fourth
#  group that exists solely to attack the diffusion limit.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- the cells -----------------------------------------------------------
    "Induced pluripotent stem cell reprogramming and directed differentiation",
    "Primary cell expansion from a small biopsy",
    "Mesenchymal stromal cell isolation and expansion",
    # ---- the scaffold ---------------------------------------------------------
    "Decellularisation with detergents and perfusion, retaining native "
    "architecture",
    "Electrospun nanofibre scaffolds",
    "Hydrogels with independently tunable stiffness and degradation rate",
    "Synthetic degradable polyesters with controlled resorption",
    # ---- the signals ----------------------------------------------------------
    "Growth-factor controlled release from the scaffold itself",
    "Immobilised peptide motifs presenting adhesion cues",
    "Perfusion and mechanical-conditioning bioreactors that load tissue while "
    "it matures",
    "Substrate stiffness as a differentiation cue in its own right",
    # ---- attacking the diffusion limit -----------------------------------------
    "Extrusion, inkjet and laser-assisted three-dimensional bioprinting",
    "Sacrificial ink strategies that leave perfusable channels behind",
    "Prevascularisation by co-culture with endothelial cells",
    "Microfluidic organ-on-a-chip devices, which sidestep the limit by staying "
    "thin",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "homo_sapiens",  # the patient, the cell source and the target anatomy
    "sus_scrofa",  # porcine tissue is the main decellularised matrix source
    "bos_taurus",  # bovine collagen, the most used natural scaffold polymer
    "rattus_norvegicus",  # the standard preclinical implantation model
    "mus_musculus",  # immunodeficient strains for human tissue constructs
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "cell_culture",
    "microscopy",
    "electron_microscopy",
    "immunohistochemistry",
    "flow_cytometry",
    "cryopreservation",
    "mechanical_testing",
    "next_generation_sequencing",
)


# =============================================================================
#  CHALLENGES
#  The first is the binding constraint. The last two are not technical at all,
#  and the final one is a patient-safety problem rather than a research one.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the physical limit ----------------------------------------------------
    "Vascularisation of constructs thicker than about two hundred micrometres, "
    "which is a diffusion limit rather than a biological one and cannot be "
    "engineered around without building plumbing",
    # -- integration -----------------------------------------------------------
    "Innervation and functional integration with host tissue, since a graft "
    "that survives but is not wired in restores structure without function",
    "Matching scaffold degradation rate to the rate at which the patient "
    "deposits their own matrix, where too fast collapses and too slow blocks",
    # -- manufacturing ---------------------------------------------------------
    "Scale-up and reproducibility of constructs that are shaped for one "
    "patient's anatomy and cannot be made to inventory",
    "Potency assays for a product whose intended effect is structural, where "
    "there is often no measurable activity to release against",
    # -- safety -----------------------------------------------------------------
    "Teratoma risk from residual undifferentiated pluripotent cells, which "
    "requires a purification step sensitive enough to detect a rare cell in "
    "millions",
    # -- economics ---------------------------------------------------------------
    "Reimbursement for a one-off structural repair whose benefit accrues over "
    "decades, assessed by systems built for recurring treatment",
    # -- patient safety, and not a research problem ------------------------------
    "Unproven stem cell clinics operating outside regulation, which have "
    "permanently blinded and in some cases killed patients, and which trade on "
    "the credibility of the legitimate field",
)
