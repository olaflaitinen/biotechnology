# =============================================================================
#  biotechnology.branches.green.biofertilisers.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The first edge is the one a reader should follow immediately, because the
#  boundary between the two records is drawn by law rather than by biology.
#
#  `green.biopesticides` and this record cover overlapping organisms doing
#  overlapping things. A Bacillus strain that promotes root growth is a
#  biofertiliser; the same strain sold with a claim that it suppresses a soil
#  pathogen becomes a plant protection product, with a dossier one to two
#  orders of magnitude more expensive. Manufacturers word claims to stay on the
#  cheaper side of that line, so the split between these two records reflects a
#  regulatory boundary that the microbiology does not respect.
#
#  The second edge worth naming is `grey.bioaugmentation`. Adding selected
#  organisms to install a capability a resident community lacks is the same
#  operation whether the goal is nitrogen in a field or hydrocarbon degradation
#  in contaminated soil, and it fails for the same reason in both: the
#  incumbents were there first and are adapted to that place.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, all claimed on the substitution argument rather than on yield.
#  Goal 12 is the strongest: displacing part of an industrial process that
#  consumes one to two per cent of global primary energy is a responsible
#  production claim on its own terms. Goal 15 is claimed on reduced nutrient
#  runoff, which is the main pathway by which agriculture damages freshwater
#  and coastal ecosystems.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on nutrient supply where fertiliser is unaffordable
    12,  # Responsible consumption and production, on displaced Haber-Bosch load
    15,  # Life on land, on reduced runoff and eutrophication
)


# =============================================================================
#  GLOSSARY
#  Grouped as the DESCRIPTION uses them: the partnership, the chemistry, the
#  place it happens, and the product.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- the partnership -----------------------------------------------------
    "symbiosis",
    "nodule",
    "mycorrhiza",
    "obligate_symbiont",
    "host_specificity",
    # ---- the chemistry --------------------------------------------------------
    "nitrogen_fixation",
    "nitrogenase",
    "leghaemoglobin",
    "phosphate_solubilisation",
    "siderophore",
    # ---- where it happens -------------------------------------------------------
    "rhizosphere",
    "root_exudate",
    "depletion_zone",
    "colonisation",
    # ---- the product -------------------------------------------------------------
    "inoculant",
    "carrier",
    "colony_forming_unit",
    "biostimulant",
    # ---- what it is meant to prevent -----------------------------------------------
    "eutrophication",
)


# =============================================================================
#  REFERENCES
#  The isolation that made a product possible, the standard review of
#  growth-promoting rhizobacteria, the reference work on mycorrhizal symbiosis,
#  and the practical guidance.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "beijerinck1888",  # isolation of the root nodule bacterium
    "vessey2003",  # the standard review of plant growth promoting rhizobacteria
    "smith2008",  # the reference work on mycorrhizal symbiosis
    "fao_biofertiliser",  # practical guidance for use
)


# =============================================================================
#  RELATED
#  Seven edges. The first is a regulatory boundary rather than a biological
#  one; the second is the same operation in a different branch.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the record separated from this one by a claim, not by biology -------
    "green.biopesticides",
    # ---- the same operation, different goal, same failure mode ---------------
    "grey.bioaugmentation",
    # ---- rebuilding soil biology rather than supplementing it ----------------
    "brown.soil_microbiome_restoration",
    # ---- how the strains are grown at scale ----------------------------------
    "white.microbial_fermentation",
    # ---- the crop varieties the symbiosis has to work with -------------------
    "green.molecular_plant_breeding",
    # ---- what the runoff does downstream -------------------------------------
    "grey.wastewater_treatment",
    # ---- where the strains were collected from -------------------------------
    "purple.access_benefit_sharing",
)
