# =============================================================================
#  biotechnology.branches.blue.algal_biotechnology.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The edge to `white.biofuels` is reciprocal and deliberate, and it is the
#  most useful one here. That record documents the algal fuel disappointment
#  and points to this one for where algal biotechnology actually succeeded.
#  This record supplies the other half: the same organisms, ponds and
#  centrifuges that failed at fuel are profitable at pigments, and the only
#  variable is the value of what is being recovered.
#
#  A reader who follows the edge in either direction should find the same
#  constraint producing opposite outcomes, which is more instructive than
#  either record alone.
#
#  `blue.seaweed_cultivation` is the near neighbour most easily confused with
#  this record, and the boundary is drawn at the organism rather than at the
#  application. Microalgae are single cells grown in suspension, harvested by
#  separating them from water, and that harvest problem is what this record is
#  about. Macroalgae are large, are grown on lines in the sea, and are lifted
#  out by hand or by boat. The harvest constraint that governs everything here
#  does not exist there, which is why they are separate records and why the
#  economics differ so completely.
#
#  `white.bioprocess_engineering` matters more than it appears to. The
#  heterotrophic route recorded in `practice.py`, where algae are grown in the
#  dark in conventional fermenters, is how much commercial algal oil is
#  actually produced, and it belongs to that record's equipment rather than to
#  a photobioreactor.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and Goal 14 carries an argument that is easy to state badly.
#
#  Life below water is claimed on a specific and documented mechanism:
#  producing long-chain omega-3 fatty acids from the microalgae that make them
#  removes a step from a fishery that exists only to concentrate the same
#  compounds. That reduces pressure on wild stocks directly rather than by
#  aspiration.
#
#  Goal 2 is claimed on protein produced without arable land or fresh water,
#  which is real but modest in volume, and is claimed for that reason rather
#  than for the larger role sometimes projected for algal protein.
#
#  GOAL 7 IS DELIBERATELY NOT CLAIMED, despite this record containing an entire
#  energy application. Algal fuel failed twice, its energy return is reported
#  at or below unity, and claiming affordable clean energy for it would be
#  exactly the unearned credit rule 12 exists to prevent. The ENERGY domain in
#  `governance.py` records the application honestly without claiming a benefit
#  it has not delivered.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on protein grown without arable land or fresh water
    9,  # Industry and innovation, on cultivation and processing systems
    12,  # Responsible production, on wastewater and carbon dioxide coupling
    14,  # Life below water, on omega-3 supply that bypasses a fishery
)


# =============================================================================
#  GLOSSARY
#  Grouped: the organisms, how they are grown, the constraint, and what is
#  recovered.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- what they are ---------------------------------------------------------
    "microalgae",
    "cyanobacteria",
    "phytoplankton",
    "photoautotroph",
    "heterotrophic_cultivation",
    "mixotrophy",
    # -- how they are grown ----------------------------------------------------
    "photobioreactor",
    "raceway_pond",
    "areal_productivity",
    "photosynthetic_efficiency",
    "photoinhibition",
    "light_penetration",
    "nutrient_limitation",
    # -- the constraint that governs -------------------------------------------
    "culture_density",
    "harvesting",
    "dewatering",
    "flocculation",
    "centrifugation",
    "cell_disruption",
    # -- what comes out --------------------------------------------------------
    "astaxanthin",
    "beta_carotene",
    "phycocyanin",
    "long_chain_omega_3",
    "single_cell_protein",
    "biorefinery",
    # -- what can go wrong -----------------------------------------------------
    "culture_crash",
    "cyanotoxin",
    "grazer_contamination",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "aquatic_species_program_final_report",
    "algal_biofuel_technoeconomic_assessment",
    "microalgae_harvesting_review",
    "photobioreactor_design_review",
    "astaxanthin_haematococcus_production",
    "algal_omega_3_production_review",
    "spirulina_commercial_history",
    "algae_wastewater_coupling_review",
    "cyanotoxin_monitoring_guidance",
    "novel_food_algae_authorisation",
)


# =============================================================================
#  RELATED
#  Six edges. The first is the reciprocal comparison that explains both records.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same constraint producing the opposite outcome --------------------
    "white.biofuels",
    # -- macroalgae, where the harvest problem does not exist ------------------
    "blue.seaweed_cultivation",
    # -- who buys the pigment and the live feed --------------------------------
    "blue.aquaculture_biotechnology",
    # -- where heterotrophic algal oil is actually manufactured ----------------
    "white.bioprocess_engineering",
    # -- algal protein as a food ingredient ------------------------------------
    "yellow.alternative_proteins",
    # -- wastewater coupling, where the economics invert -----------------------
    "grey.wastewater_treatment",
)
