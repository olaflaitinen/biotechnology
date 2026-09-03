# =============================================================================
#  biotechnology.branches.grey.biowaste_treatment.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `grey.wastewater_treatment` is first because the two records share a
#  process. Anaerobic digestion is the same four-stage community in both, and
#  the division between them is the feedstock rather than the technology:
#
#      wastewater  digests a sludge its own treatment produced
#      biowaste    digests material collected separately as a waste in its own
#                  right
#
#  Splitting them by feedstock rather than by process is a deliberate editorial
#  choice, because a reader looking for anaerobic digestion should find it in
#  the record about the material they have, not in a shared process record that
#  would belong to neither.
#
#  `white.biofuels` is the contrast edge, and it is the one that teaches most.
#  That record makes fuel from crops and residues grown or collected for the
#  purpose; this one makes fuel from material somebody was paying to get rid
#  of. The 2012 setback in `history.py` is precisely what happened when a
#  waste-treatment incentive was claimed by a crop-fed operation, which is to
#  say when this record's economics were applied to that record's feedstock.
#
#  `green.biofertilisers` binds through the digestate, which is where this
#  record's output physically goes.
#
#  `white.biopolymers` is DELIBERATELY NOT LINKED despite polyhydroxyalkanoate
#  recovery being technically possible from these streams. That is a research
#  route rather than a deployed application here, and rule 6 keeps aspirations
#  out of the edges as well as out of the applications.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Five, and this is the record in the branch with the strongest claim to goal
#  12, which most of its siblings deliberately decline.
#
#  Goal 12 is claimed properly here. Responsible production and consumption is
#  about material cycles, and this record closes one: organic material becomes
#  energy and a soil amendment rather than a landfill mass. Note that the
#  record's own `narrative.py` states that prevention beats treatment, which is
#  the waste hierarchy, and claiming the goal for recovery rather than for
#  prevention is the honest version of the claim.
#
#  Goal 13 is claimed on the largest term in the climate case, which is avoided
#  landfill methane rather than displaced fossil energy. It is claimed with the
#  qualification that leakage from the plant erodes it and is rarely measured.
#
#  Goal 7 is claimed because the plant is a net energy producer, and upgraded
#  biomethane is a grid-quality gas rather than a site-bound fuel.
#
#  Goal 2 is claimed narrowly, through digestate returning nitrogen and
#  phosphorus to agricultural soil at a time when phosphate rock is a finite
#  imported resource.
#
#  Goal 11 is claimed on municipal waste management, which is where most of the
#  feedstock is collected and where the diversion targets bite.
#
#  GOAL 6 IS DELIBERATELY NOT CLAIMED, although the sibling record claims it
#  strongly. This process treats a solid, and the water protection here appears
#  as a constraint on spreading rather than as an outcome delivered.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Food, on digestate returning nitrogen and phosphorus to soil
    7,  # Energy, on methane recovery and biomethane grid injection
    11,  # Cities, on municipal organic waste diversion
    12,  # Responsible consumption, on closing an organic material cycle
    13,  # Climate, on avoided landfill methane, net of plant leakage
)


# =============================================================================
#  GLOSSARY
#  Grouped: the two routes, the four-stage biology, the failure modes, and the
#  products.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the routes ------------------------------------------------------------
    "anaerobic_digestion",
    "composting",
    "in_vessel_composting",
    "windrow",
    "mechanical_biological_treatment",
    "co_digestion",
    "mesophilic",
    "thermophilic",
    "landfill_gas",
    # -- the four-stage biology ------------------------------------------------
    "hydrolysis",
    "acidogenesis",
    "acetogenesis",
    "methanogenesis",
    "methanogen",
    "archaea",
    "syntrophy",
    "volatile_solids",
    # -- how it goes wrong -----------------------------------------------------
    "organic_loading_rate",
    "volatile_fatty_acids",
    "alkalinity",
    "acidification",
    "ammonia_inhibition",
    "foaming",
    # -- and what comes out ----------------------------------------------------
    "biogas",
    "biomethane",
    "biogas_upgrading",
    "digestate",
    "compost",
    "gate_fee",
    "end_of_waste",
    "waste_hierarchy",
    "methane_leakage",
    "global_warming_potential",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "anaerobic_digestion_process_review",
    "biomethane_potential_protocol",
    "digestate_quality_protocol",
    "landfill_diversion_climate_assessment",
    "biogas_methane_leakage_measurement",
    "crop_fed_digestion_land_use",
    "digestate_plastic_contamination",
    "composting_process_review",
    "household_digester_deployment",
)


# =============================================================================
#  RELATED
#  Six edges. The shared process first, then the contrast, then where the
#  outputs go.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same digestion, on a sludge the plant produced itself -------------
    "grey.wastewater_treatment",
    # -- fuel from purpose-grown material, and the incentive that collided -----
    "white.biofuels",
    # -- where the digestate physically goes -----------------------------------
    "green.biofertilisers",
    # -- treating the odour and the gaseous emissions of these facilities ------
    "grey.air_biotreatment",
    # -- the uncontested case of seeding a vessel with no incumbent ------------
    "grey.bioaugmentation",
    # -- the microbial conversion of biomass, engineered rather than accepted --
    "white.microbial_fermentation",
)
