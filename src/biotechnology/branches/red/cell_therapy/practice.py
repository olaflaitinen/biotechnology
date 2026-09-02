# =============================================================================
#  biotechnology.branches.red.cell_therapy.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The CHALLENGES list here is unusually important. Cell therapy is the
#  subtype in this library where the gap between what is demonstrated and what
#  is deliverable is widest, and where the limiting factors are least
#  technical: vein-to-vein time, accredited-centre capacity and cost structure
#  decide more outcomes than any molecular property does.
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
#  Ordered oldest and most established first. Note that the first entry
#  predates the term "cell therapy" by half a century.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- the founding application, in routine use since the 1960s -------------
    "Allogeneic haematopoietic stem cell transplantation for leukaemia and "
    "inherited marrow failure",
    # -- the modern engineered products ---------------------------------------
    "CD19-directed CAR-T therapy for B-cell lymphoma and leukaemia",
    "BCMA-directed CAR-T therapy for multiple myeloma",
    # -- non-engineered adoptive transfer -------------------------------------
    "Tumour-infiltrating lymphocyte therapy for advanced melanoma",
    "Virus-specific T cells for post-transplant infection",
    # -- secretory rather than engrafting products ----------------------------
    "Mesenchymal stromal cells for steroid-refractory graft-versus-host disease",
    # -- replacement of a lost endocrine function -----------------------------
    "Islet cell transplantation in brittle type 1 diabetes",
    # -- in trials rather than approved ---------------------------------------
    "Induced pluripotent stem cell derived cardiomyocyte and retinal grafts",
    "Allogeneic off-the-shelf natural killer cell products",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped along the manufacturing path, because the path is the product.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- obtaining the starting material ------------------------------------
    "Leukapheresis and mononuclear cell collection",
    "Magnetic bead and column-based cell selection",
    "Cord blood and donor registry sourcing for allogeneic products",
    # ---- modification --------------------------------------------------------
    "Chimeric antigen receptor design and signalling domain selection",
    "Lentiviral and retroviral transduction of primary T cells",
    "CRISPR knockout of TCR and HLA loci for allogeneic products",
    # ---- expansion -----------------------------------------------------------
    "Serum-free expansion media with defined cytokine cocktails",
    "Closed-system automated cell processing platforms",
    "Rocking-motion and gas-permeable expansion vessels",
    # ---- release and delivery ------------------------------------------------
    "Potency assays based on cytotoxicity and cytokine release",
    "Controlled-rate freezing and vapour-phase liquid nitrogen storage",
    "Chain-of-identity and chain-of-custody tracking systems",
    # ---- the platform for the next generation --------------------------------
    "Induced pluripotent stem cell reprogramming and directed differentiation",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "homo_sapiens",  # both the source and the recipient
    "mus_musculus",  # preclinical models and the origin of early scFv domains
    "escherichia_coli",  # plasmid supply for vector manufacture
    "streptococcus_pyogenes",  # Cas9 for allogeneic gene knockouts
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "cell_culture",
    "flow_cytometry",
    "crispr_cas9",
    "elisa",
    "next_generation_sequencing",
    "cryopreservation",
    "digital_pcr",
    "apheresis",
)


# =============================================================================
#  CHALLENGES
#  Two technical, then five that are logistical, clinical-operational or
#  economic. That balance is not an accident: it reflects where the field
#  actually loses patients.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- biological ------------------------------------------------------------
    "Poor efficacy in solid tumours, where the product must traffic, "
    "penetrate and survive a hostile microenvironment rather than meet its "
    "target in the bloodstream",
    "Antigen escape, in which the tumour simply stops expressing the single "
    "marker the product was engineered to see",
    # -- safety ----------------------------------------------------------------
    "Cytokine release syndrome and immune effector cell associated "
    "neurotoxicity, both requiring intensive care capability on site",
    # -- manufacturing ---------------------------------------------------------
    "Manufacturing failure rate in heavily pre-treated patients whose T cells "
    "are exhausted before collection",
    "Potency assay design that actually predicts clinical benefit rather than "
    "merely demonstrating the cells are alive",
    # -- logistical and economic -----------------------------------------------
    "Vein-to-vein turnaround time of two to five weeks, during which the "
    "disease progresses and some patients become ineligible",
    "A cost structure that resists conventional economies of scale, because "
    "doubling output means doubling clean-room suites and operators",
    "Restriction to accredited centres, which makes access a question of "
    "postcode as much as of diagnosis",
)
