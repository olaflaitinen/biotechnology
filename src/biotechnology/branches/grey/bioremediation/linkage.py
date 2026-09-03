# =============================================================================
#  biotechnology.branches.grey.bioremediation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `grey.bioaugmentation` is the first edge because this record repeatedly
#  defers to it. The question of whether to add organisms is the commonest
#  question asked of a remediation contractor and the answer is usually no,
#  and that record exists to hold the evidence for the answer so this one does
#  not have to argue it four times.
#
#  `grey.phytoremediation` is the second because it is the same job with plants
#  instead of bacteria, and because the comparison is instructive rather than
#  redundant: plants reach further, take longer, tolerate less, and can
#  actually extract a metal into harvestable tissue, which is the one thing
#  microbial treatment cannot do.
#
#  `grey.biomining` is the edge a reader would not predict and should see. The
#  same organisms and the same acid-generating chemistry that recover copper
#  from low-grade ore also produce acid mine drainage, which is one of the
#  most persistent contamination problems this record has to treat. The
#  technology and the contamination are the same biology pointed in different
#  directions.
#
#  `blue.marine_natural_products` is DELIBERATELY NOT LINKED despite the
#  shoreline work in `history.py`. That record is about compounds recovered
#  from marine organisms, which is a different subject that happens to share a
#  coastline. Linking it would be association by setting, which rule 13 exists
#  to prevent.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and each is claimed on a mechanism this record actually performs.
#
#  Goal 6 is the strongest. Groundwater plume treatment and the protection of
#  abstraction zones are literally what a large part of this practice does, and
#  the drinking water pathway is what most cleanup targets are derived from.
#
#  Goal 15 is claimed on land: contaminated soil is degraded land, and
#  returning it to use is what the goal covers.
#
#  Goal 3 is claimed narrowly and honestly. Cleanup targets are calculated from
#  human exposure pathways, so reducing a soil concentration to a risk-based
#  number is a health intervention by construction rather than by aspiration.
#
#  Goal 11 is claimed because contaminated land sits inside cities, and whether
#  it is treated or fenced determines whether a neighbourhood gets housing and
#  a park or a hoarding for thirty years.
#
#  GOAL 12 IS DELIBERATELY NOT CLAIMED, which may surprise a reader. Responsible
#  production and consumption is about not creating the waste. This record deals
#  with waste that already exists, decades after the fact, and claiming a
#  prevention goal for a cleanup technology would fail the sceptical-auditor
#  test in rule 12. `grey.biowaste_treatment` claims it and is entitled to.
#
#  GOAL 14 IS ALSO NOT CLAIMED, despite the oil spill work, because the
#  overwhelming majority of this practice is terrestrial and subsurface.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on cleanup targets derived from human exposure pathways
    6,  # Water, on groundwater plume treatment and abstraction protection
    11,  # Cities, on whether urban contaminated land is treated or fenced
    15,  # Land, on returning degraded soil to use
)


# =============================================================================
#  GLOSSARY
#  Grouped: the contamination, the strategies, the limiting physics, and the
#  evidence.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- what is there ---------------------------------------------------------
    "contaminated_land",
    "groundwater_plume",
    "source_zone",
    "petroleum_hydrocarbon",
    "chlorinated_solvent",
    "polycyclic_aromatic_hydrocarbon",
    "heavy_metal",
    "conceptual_site_model",
    # -- what is done about it -------------------------------------------------
    "bioremediation",
    "monitored_natural_attenuation",
    "biostimulation",
    "bioaugmentation",
    "bioventing",
    "air_sparging",
    "land_farming",
    "biopile",
    "permeable_reactive_barrier",
    "pump_and_treat",
    # -- why it stops before the target ----------------------------------------
    "bioavailability",
    "sorption",
    "desorption",
    "sequestration",
    "mass_transfer_limitation",
    "asymptotic_endpoint",
    # -- the chemistry it runs on ----------------------------------------------
    "mineralisation",
    "cometabolism",
    "reductive_dechlorination",
    "electron_acceptor",
    "electron_donor",
    "redox_zonation",
    "denitrification",
    # -- and how anyone knows it worked ----------------------------------------
    "compound_specific_isotope_analysis",
    "functional_gene_marker",
    "microcosm_study",
    "risk_based_cleanup_target",
    "exposure_pathway",
    "plume_stability",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "bioremediation_field_review",
    "exxon_valdez_shoreline_bioremediation",
    "natural_attenuation_protocol",
    "compound_specific_isotope_analysis_guide",
    "bioavailability_contaminated_soil",
    "dehalococcoides_dechlorination",
    "deepwater_horizon_hydrocarbon_degradation",
    "pfas_biodegradation_limits",
    "remediation_cost_comparison",
)


# =============================================================================
#  RELATED
#  Six edges. The first two are the alternatives to this record, and the third
#  is the source of contamination it has to clean up.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- should organisms be added at all, which this record keeps deferring ----
    "grey.bioaugmentation",
    # -- the same job with plants, and the one thing they can do that microbes
    #    cannot, which is extract a metal into harvestable tissue ---------------
    "grey.phytoremediation",
    # -- the same acid-generating biology, pointed the other way ----------------
    "grey.biomining",
    # -- deciding whether the treatment worked, and where the plume is ----------
    "grey.environmental_biomonitoring",
    # -- the engineered-vessel version of the same degradation ------------------
    "grey.wastewater_treatment",
    # -- the degrading capabilities themselves, and where new ones come from ----
    "white.biocatalysis",
)
