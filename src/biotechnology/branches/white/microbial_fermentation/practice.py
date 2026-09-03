# =============================================================================
#  biotechnology.branches.white.microbial_fermentation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by product class, and the grouping is meant to make
#  one point: this operation is the common ancestor of most of the library. The
#  same vessel design makes an antibiotic, an industrial enzyme, a feed amino
#  acid and a therapeutic protein. Very few subtypes here are upstream of so
#  many others.
#
#  TECHNOLOGIES are grouped by the four operational problems in the order a
#  plant meets them: get the culture up to volume, keep everything else out,
#  feed it correctly, and know what is happening inside a vessel you cannot see
#  into. The last group is smaller than it should be, and that is the honest
#  state of the field rather than an omission.
#
#  A NOTE ON WHAT IS ABSENT. Reactor design, mass transfer correlations,
#  scale-up rules and everything downstream of the harvest belong to
#  `white.bioprocess_engineering`. Strain construction belongs to
#  `white.metabolic_engineering`. This record is the cultivation itself.
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
#  Grouped by product class. Note how many other records depend on this one.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- medicines --------------------------------------------------------------
    "Antibiotic production by filamentous fungi and actinomycetes, the process "
    "that created the modern fermentation industry",
    "Recombinant therapeutic protein production, including insulin and the "
    "microbial share of the biologics in `red.pharmaceutical_biotechnology`",
    "Vaccine antigen and viral vector production in microbial hosts",
    # -- the enzymes that the rest of the branch uses ---------------------------
    "Industrial enzyme manufacture by secreting Bacillus, Aspergillus and "
    "Trichoderma hosts, which is how every product in "
    "`white.industrial_enzymes` is physically made",
    # -- feed and food ingredients -----------------------------------------------
    "Amino acid production for animal feed at millions of tonnes a year, the "
    "largest tonnage in this record",
    "Vitamin and organic acid production, including citric acid, which is "
    "among the oldest large-scale fermentations still running",
    "Precision fermentation of dairy and egg proteins without animals, which "
    "is where this record meets `yellow.precision_fermentation`",
    "Yeast, probiotic and starter culture production, where the cells "
    "themselves are the product rather than something they secrete",
    # -- chemicals and fuels -----------------------------------------------------
    "Bulk chemical and polymer precursor fermentation, including lactic acid "
    "and the diols in `white.biobased_chemicals`",
    "Ethanol and advanced biofuel production, the largest fermentation by "
    "volume anywhere in the world",
    # -- growing on solids rather than in liquid ---------------------------------
    "Solid-state fermentation for fungal enzyme production and for substrate "
    "upgrading, which uses little free water and suits filamentous growth",
    # -- feedstocks that do not come from a field ----------------------------------
    "Gas fermentation of carbon monoxide and carbon dioxide by acetogens, "
    "which removes the competition with food and land",
    "Methanotroph and methylotroph cultivation on methane or methanol, "
    "including single cell protein",
)


# =============================================================================
#  TECHNOLOGIES
#  The four operational problems, in the order a plant meets them.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- getting from a vial to a production vessel ---------------------------
    "The seed train, a staged sequence of vessels each roughly ten times the "
    "last, which takes a culture from a preserved vial to production volume "
    "without ever diluting the inoculum too far",
    "Master and working cell bank systems, so that every campaign starts from "
    "genetically identical material rather than from a strain that has been "
    "passaged for years",
    "Cryopreservation and lyophilisation of production strains",
    # ---- keeping everything else out ------------------------------------------
    "Steam-in-place and clean-in-place systems, which sterilise a vessel and "
    "its pipework without dismantling it",
    "Continuous medium sterilisation, which heats briefly at high temperature "
    "and preserves nutrients that batch sterilisation destroys",
    "Sterile filtration of process air and of heat-sensitive feed components",
    "Aseptic transfer, sampling and addition design, since most contamination "
    "enters through an operation rather than through a wall",
    "Non-sterile or contamination-resistant fermentation using extreme pH, "
    "thermophiles or a substrate only the production organism can use, which "
    "removes the largest single cost in low-value processes",
    # ---- feeding it correctly, which is the central skill -----------------------
    "Fed-batch feeding strategies designed to hold specific growth rate below "
    "the threshold at which overflow metabolism begins",
    "Feedback control on dissolved oxygen, pH, or the respiratory quotient, so "
    "that the culture's own signals set the feed rate",
    "Complex media from molasses, corn steep liquor and other by-products, "
    "traded against defined media that cost more and behave reproducibly",
    "Induction strategy design, including the decision to separate a growth "
    "phase from a production phase",
    "Antifoam addition and foam control, an unglamorous necessity that "
    "nonetheless changes oxygen transfer",
    # ---- knowing what is happening inside --------------------------------------
    "Off-gas analysis for oxygen uptake, carbon dioxide evolution and "
    "respiratory quotient, which is the only continuous non-invasive window "
    "into a running culture",
    "In-line probes for dissolved oxygen, pH, temperature, pressure and optical "
    "density",
    "Process analytical technology and soft sensors that infer biomass and "
    "product from measurable signals",
    "Contamination detection by microscopy, plating and rapid molecular "
    "methods, where hours of delay decide whether a batch can be saved",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "escherichia_coli",  # fastest, highest titres, and prone to acetate overflow
    "saccharomyces_cerevisiae",  # robust, food-grade, ethanol overflow instead
    "aspergillus_niger",  # citric acid and enzymes, filamentous and viscous
    "corynebacterium_glutamicum",  # the amino acid workhorse
    "streptomyces_coelicolor",  # the antibiotic-producing actinomycetes
    "bacillus_subtilis",  # secretion, and a long food-safe record
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "cell_culture",
    "sterilisation",
    "chromatography",
    "mass_spectrometry",
    "bioassay",
    "process_modelling",
    "flux_analysis",
)


# =============================================================================
#  CHALLENGES
#  The first two are the ones that actually lose batches and money.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- what loses a batch outright -------------------------------------------
    "Contamination, which destroys not only the product but the days of vessel "
    "occupancy that produced it, and which a faster-growing organism can cause "
    "within hours of entry",
    "Bacteriophage infection in bacterial processes, which spreads through a "
    "plant and can idle it for weeks, and against which sterility alone is not "
    "protection",
    # -- what limits the good batches -------------------------------------------
    "Oxygen transfer, which does not improve with vessel size and is the true "
    "ceiling on most large aerobic processes regardless of the strain",
    "Overflow metabolism above a critical feed rate, which turns extra "
    "substrate into inhibitory acetate or ethanol rather than into product",
    "Heat removal, since a large aerobic fermentation is a substantial heat "
    "source and cooling surface does not scale with volume either",
    # -- what changes over a long run ---------------------------------------------
    "Genetic drift and reversion over the generations of a seed train and "
    "production run, which is the operational face of the stability metric in "
    "`white.metabolic_engineering`",
    "Foaming, shear damage to filamentous and fragile organisms, and the "
    "rising viscosity of a dense fungal culture, all of which degrade mixing "
    "and transfer as the run proceeds",
    # -- what the process runs on --------------------------------------------------
    "Feedstock cost and its competition with food and land, which for a bulk "
    "product is frequently the whole economic question",
    "Water and energy consumption, since sterilisation, aeration, agitation "
    "and cooling are continuous demands rather than one-off ones",
    # -- what is left afterwards ---------------------------------------------------
    "Spent broth and biomass disposal, which is a large waste stream that a "
    "life cycle assessment must count against the process",
)
