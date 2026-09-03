# =============================================================================
#  biotechnology.branches.white.biofuels.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Three of these edges exist because this record's central problems are not
#  solvable inside it.
#
#  `white.industrial_enzymes` holds the cellulase cost that has kept the second
#  generation uncompetitive. The same number appears in both records with a
#  different meaning: there it is a market price constrained by what customers
#  will pay, here it is an operating cost that decides whether a plant runs.
#  Neither record can resolve it alone, which is the honest position.
#
#  `white.metabolic_engineering` holds the pentose-fermenting and
#  inhibitor-tolerant strains. Hydrolysis releases xylose that the standard
#  ethanol yeast ignores, and pretreatment generates compounds that poison it.
#  Both are strain problems stated as fuel requirements.
#
#  `green.plant_genetic_engineering` is where the feedstock itself is designed,
#  including reduced-lignin varieties intended to make pretreatment cheaper.
#  It is also the record that shares this one's editorial posture towards a
#  contested public argument.
#
#  `blue.algal_biotechnology` is included with a specific purpose. This record
#  documents the algal fuel disappointment; that record documents where algal
#  biotechnology actually succeeded. A reader who takes only the failure from
#  here would be misled, and the edge exists to prevent it.
#
#  `grey.wastewater_treatment` carries anaerobic digestion, which is the least
#  disputed application in this record and belongs as much to waste management
#  as to energy.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and the omissions are as deliberate as the inclusions.
#
#  Goal 7 and Goal 13 are the claims this record can support, and both are
#  qualified by feedstock: they hold clearly for wastes, residues and
#  sugarcane, and are contested for crop-based fuels whose land use change
#  penalty may reverse them.
#
#  GOAL 2 IS DELIBERATELY NOT CLAIMED. Where a biofuel touches food security it
#  is usually as a competitor for land and water rather than a contributor, and
#  claiming zero hunger here would be exactly the kind of unearned credit that
#  `red/gene_therapy/linkage.py` warns against. The FOOD domain in
#  `governance.py` records the relationship truthfully instead, as a
#  competition rather than a benefit.
# =============================================================================
SDGS: Tuple[int, ...] = (
    7,  # Affordable and clean energy, most defensibly for wastes and residues
    12,  # Responsible production, on residue and waste valorisation
    13,  # Climate action, subject to the carbon intensity determination
)


# =============================================================================
#  GLOSSARY
#  Grouped: the fuels and generations, the conversion train, then the
#  assessment vocabulary that decides whether any of it counts.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- what is being made ----------------------------------------------------
    "bioethanol",
    "biodiesel",
    "biobutanol",
    "biomethane",
    "drop_in_fuel",
    "sustainable_aviation_fuel",
    "first_generation_biofuel",
    "second_generation_biofuel",
    # -- the feedstock and its resistance --------------------------------------
    "lignocellulose",
    "cellulose",
    "hemicellulose",
    "lignin",
    "recalcitrance",
    "pentose",
    "energy_crop",
    "agricultural_residue",
    # -- the conversion train --------------------------------------------------
    "pretreatment",
    "enzymatic_hydrolysis",
    "saccharification",
    "fermentation_inhibitor",
    "consolidated_bioprocessing",
    "anaerobic_digestion",
    "transesterification",
    "hydrotreating",
    "gasification",
    # -- whether it counts -----------------------------------------------------
    "energy_return_on_investment",
    "carbon_intensity",
    "indirect_land_use_change",
    "life_cycle_assessment",
    "mass_balance_chain_of_custody",
    "blend_wall",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "iea_bioenergy_outlook",
    "indirect_land_use_change_analysis",
    "corn_ethanol_energy_balance_debate",
    "sugarcane_ethanol_assessment",
    "cellulosic_ethanol_commercial_review",
    "algal_biofuel_technoeconomic_assessment",
    "eu_renewable_energy_directive_ii",
    "renewable_fuel_standard_analysis",
    "sustainable_aviation_fuel_review",
    "pretreatment_technologies_review",
)


# =============================================================================
#  RELATED
#  Seven edges. The first three hold problems this record cannot solve alone.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the cost that decides the second generation ---------------------------
    "white.industrial_enzymes",
    # -- the strains that must ferment a sugar they evolved to ignore ----------
    "white.metabolic_engineering",
    # -- where the feedstock itself is designed --------------------------------
    "green.plant_genetic_engineering",
    # -- the plant that converts it --------------------------------------------
    "white.bioprocess_engineering",
    # -- the same feedstocks routed to higher value products -------------------
    "white.biobased_chemicals",
    # -- where algal biotechnology actually succeeded --------------------------
    "blue.algal_biotechnology",
    # -- anaerobic digestion as waste management -------------------------------
    "grey.wastewater_treatment",
)
