# =============================================================================
#  biotechnology.branches.grey.wastewater_treatment.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `white.microbial_fermentation` IS THE EDGE THAT TEACHES THE MOST, AND IT IS
#  A CONTRAST RATHER THAN A SIMILARITY.
#
#      white   ONE defined strain, sterile vessel, everything else excluded.
#              The organism is chosen and the conditions serve it.
#      grey    an UNDEFINED community, open vessel, continuously reseeded by
#              the influent. The conditions are chosen and they select the
#              organisms.
#
#  They are the two opposite answers to the same engineering question, and the
#  grey answer is the one operating at the larger scale by several orders of
#  magnitude. A reader who has understood only the sterile-vessel model has
#  seen the smaller half of industrial microbiology.
#
#  `grey.biowaste_treatment` is linked because anaerobic digestion sits in both
#  records and is the same process applied to different feedstock. The division
#  is that this record digests a sludge its own treatment produced, while that
#  one digests material collected separately as a waste in its own right.
#
#  `blue.algal_biotechnology` is the consequence edge. Nutrients that leave
#  this record's outfall are what feed the blooms and dead zones that record
#  describes, which is why the 1965 entry in `history.py` reads as a setback.
#
#  `dark.antimicrobial_resistance` IS DELIBERATELY INCLUDED despite pointing at
#  an unwritten branch, because a dense mixed community under continuous
#  selective pressure concentrating resistance genes is a genuine mechanism of
#  this process and not an association.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  FIVE, WHICH IS THE LONGEST TUPLE IN THIS BRANCH, AND EVERY ONE IS EARNED ON
#  A MECHANISM RATHER THAN ON AN ASPIRATION.
#
#  Goal 6 is not merely claimed here, it is largely defined by this record.
#  Target 6.3 is about halving untreated wastewater, which is this process
#  verbatim.
#
#  Goal 3 is claimed on the founding public health outcome. Separating sewage
#  from drinking water ended cholera and typhoid as ordinary urban facts, and
#  this is the process that makes it possible at city scale.
#
#  Goal 14 is claimed on oxygen depletion and eutrophication in coastal waters,
#  which is the direct and measured consequence of the discharge this record
#  controls.
#
#  Goal 11 is claimed because sanitation is a defining piece of urban
#  infrastructure and because coverage gaps fall on informal settlements.
#
#  Goal 7 is claimed on a quantified two-way basis: aeration is a substantial
#  share of municipal electricity demand, and digester methane offsets a
#  substantial share of a works' own consumption. This is the one record in the
#  branch where an energy goal is not a stretch.
#
#  GOAL 12 IS DELIBERATELY NOT CLAIMED, even though biosolids return nutrients
#  to soil and struvite is recovered. This process handles waste that has
#  already been produced; it does not reduce its production.
#  `grey.biowaste_treatment` claims that goal and is entitled to it.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on the sanitation outcome that predates antibiotics
    6,  # Water and sanitation, which target 6.3 states almost verbatim
    7,  # Energy, on aeration demand and on digester methane recovery
    11,  # Cities, on sanitation infrastructure and coverage gaps
    14,  # Oceans, on nutrient loading and coastal oxygen depletion
)


# =============================================================================
#  GLOSSARY
#  Grouped: the process, the three pollutant jobs, the solid, and the operating
#  vocabulary an engineer actually uses.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the process and its configurations ------------------------------------
    "activated_sludge",
    "trickling_filter",
    "membrane_bioreactor",
    "sequencing_batch_reactor",
    "granular_sludge",
    "upflow_anaerobic_sludge_blanket",
    "waste_stabilisation_pond",
    "primary_treatment",
    "secondary_treatment",
    "tertiary_treatment",
    # -- the three jobs --------------------------------------------------------
    "biochemical_oxygen_demand",
    "chemical_oxygen_demand",
    "nitrification",
    "denitrification",
    "anammox",
    "enhanced_biological_phosphorus_removal",
    "struvite",
    "eutrophication",
    # -- what governs which organisms are present ------------------------------
    "solids_retention_time",
    "hydraulic_retention_time",
    "mixed_liquor",
    "food_to_microorganism_ratio",
    "dissolved_oxygen",
    "anoxic_zone",
    "floc",
    "biofilm",
    # -- the solid, and what happens to it -------------------------------------
    "sludge",
    "sludge_volume_index",
    "bulking",
    "anaerobic_digestion",
    "biogas",
    "biosolids",
    "dewatering",
    # -- and what gets through -------------------------------------------------
    "micropollutant",
    "combined_sewer_overflow",
    "water_reuse",
    "discharge_consent",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "activated_sludge_centenary",
    "activated_sludge_model_series",
    "enhanced_biological_phosphorus_removal_review",
    "anammox_engineered_systems",
    "aerobic_granular_sludge_full_scale",
    "uncultured_organisms_activated_sludge",
    "wastewater_energy_balance",
    "micropollutant_removal_conventional_treatment",
    "wastewater_based_epidemiology",
    "global_sanitation_coverage",
)


# =============================================================================
#  RELATED
#  Six edges. The contrast first, because it is what makes the record legible.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the opposite answer to the same engineering question ------------------
    "white.microbial_fermentation",
    # -- the same digestion, applied to separately collected feedstock ---------
    "grey.biowaste_treatment",
    # -- what the nutrients in the discharge go on to do -----------------------
    "blue.algal_biotechnology",
    # -- the same sewage read as a population health instrument ----------------
    "grey.environmental_biomonitoring",
    # -- where seeding a reactor is uncontested, and why -----------------------
    "grey.bioaugmentation",
    # -- resistance genes concentrated rather than destroyed -------------------
    "dark.antimicrobial_resistance",
)
