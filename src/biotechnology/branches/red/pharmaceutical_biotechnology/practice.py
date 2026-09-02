# =============================================================================
#  biotechnology.branches.red.pharmaceutical_biotechnology.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and editorial rules: see `red/gene_therapy/practice.py`.
#      APPLICATIONS must name something that exists, not something proposed.
#      CHALLENGES must include at least one non-technical entry.
#      ORGANISMS and TECHNIQUES are registry keys and are checked on commit.
#
#  SUBTYPE-SPECIFIC NOTE
#  The technology list below is organised as the process flows - upstream,
#  downstream, then the quality systems that wrap both - because that is how
#  a manufacturing site is physically laid out and how a reader touring one
#  would encounter it.
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
#  Ordered by the historical sequence in which these product classes reached
#  patients, which is also roughly the order of increasing molecular
#  complexity.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- 1982 onwards: simple recombinant proteins ----------------------------
    "Recombinant human insulin and engineered insulin analogues",
    "Recombinant human growth hormone",
    # -- 1980s-1990s: haematology and nephrology ------------------------------
    "Erythropoietin and granulocyte colony-stimulating factors",
    "Recombinant clotting factors VIII and IX for haemophilia",
    # -- 1986 onwards: antibodies --------------------------------------------
    "Therapeutic monoclonal antibodies in oncology and immunology",
    "Fusion proteins and Fc-fusion decoy receptors",
    # -- specialist and metabolic --------------------------------------------
    "Enzyme replacement therapy for lysosomal storage disorders",
    "PEGylated proteins with extended circulating half-life",
    # -- 2006 onwards: the copy market ---------------------------------------
    "Biosimilar development and formal comparability exercises",
    # -- contract manufacture -------------------------------------------------
    "Contract development and manufacturing for third-party products",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by position in the process train.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- upstream: expression hosts ----------------------------------------
    "Chinese hamster ovary (CHO) suspension cell lines",
    "Escherichia coli periplasmic secretion and inclusion-body refolding",
    "Pichia pastoris and Saccharomyces cerevisiae secretion systems",
    "Glycoengineered host lines producing defined glycoforms",
    # ---- upstream: culture --------------------------------------------------
    "Single-use stirred-tank bioreactors from 50 L to 2000 L",
    "Fed-batch, perfusion and intensified seed-train strategies",
    "Chemically defined, animal-component-free media",
    # ---- downstream ---------------------------------------------------------
    "Protein A affinity capture chromatography",
    "Ion exchange and hydrophobic interaction polishing",
    "Viral inactivation by low pH and nanofiltration",
    "Tangential flow filtration for concentration and buffer exchange",
    # ---- quality systems wrapping both --------------------------------------
    "Quality by design with defined critical quality attributes",
    "Process analytical technology and multivariate batch monitoring",
    "Extended characterisation by peptide mapping and glycan profiling",
)


# =============================================================================
#  ORGANISMS
#  Registry keys. The list is short because the industry is deliberately
#  conservative: a new expression host means a new viral safety package, and
#  almost nobody takes that on without a compelling reason.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "cricetulus_griseus",  # CHO cells, the workhorse of the industry
    "escherichia_coli",  # non-glycosylated proteins and plasmid supply
    "saccharomyces_cerevisiae",  # insulin, hepatitis B antigen
    "komagataella_phaffii",  # Pichia, for secreted peptides and enzymes
    "homo_sapiens",  # HEK293 and human cell lines for some products
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "cell_culture",
    "fermentation",
    "chromatography",
    "electrophoresis",
    "mass_spectrometry",
    "elisa",
    "pcr",
    "filtration",
)


# =============================================================================
#  CHALLENGES
#  Four technical, three structural. The structural ones are what actually
#  determine whether a patient in a given country receives the medicine.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- economic and technical, coupled --------------------------------------
    "Cost of goods dominated by upstream titre and by the price of "
    "downstream capture resin, both of which resist further improvement",
    # -- immunological ---------------------------------------------------------
    "Immunogenicity in a fraction of patients, producing anti-drug antibodies "
    "that neutralise the therapy over months to years",
    # -- product quality -------------------------------------------------------
    "Glycan heterogeneity between batches and between manufacturing sites, "
    "which is the usual sticking point in a comparability exercise",
    # -- logistics -------------------------------------------------------------
    "Cold chain requirements that limit distribution in warm climates and in "
    "settings without reliable electricity",
    # -- regulatory burden -----------------------------------------------------
    "The comparability evidence required after any process change, which "
    "discourages manufacturers from improving processes at all",
    # -- structural ------------------------------------------------------------
    "Concentration of large-scale manufacturing capacity in a small number of "
    "countries, exposed during every supply shock",
    "Biosimilar uptake that varies more with national procurement policy than "
    "with clinical evidence",
)
