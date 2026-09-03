# =============================================================================
#  biotechnology.branches.blue.marine_biofouling_control.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record closes the blue branch, and its edges point back into the branch
#  in an unusual direction: it consumes what the other records produce, and it
#  is the only one that treats marine organisms as the adversary.
#
#  `blue.marine_natural_products` supplies the natural antifoulants, and
#  supplies its constraint along with them. The chemistry that keeps a sessile
#  organism clean is exactly the chemistry this record wants, and it occurs in
#  the same vanishing quantities. The furanone result of 1996 is the clearest
#  case: a red alga that stays notably clean, a compound identified, and the
#  same supply question immediately.
#
#  `green.biopesticides` is the edge a reader is least likely to expect and the
#  most instructive. Both records describe a field that used broad-spectrum
#  toxicity, discovered the non-target consequences, and moved towards
#  specificity. Both have a signature banned compound. Both replaced killing
#  with interference in a behaviour. The parallel is close enough that the
#  arguments transfer, and it suggests the pattern is a property of using
#  poisons in an open system rather than of either field.
#
#  `blue.marine_biomaterials` is the reciprocal of the mussel adhesive edge.
#  That record studies byssal attachment in order to copy it; this one studies
#  it in order to prevent it. The same protein chemistry read in opposite
#  directions, which is a genuine curiosity of the branch.
#
#  `blue.aquaculture_biotechnology` is the application where a biocide cannot
#  be used at all, because the animals are inside the structure being
#  protected.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and two of them are unusual enough to justify.
#
#  Goal 13 is claimed on a mechanism most readers would not associate with
#  climate policy: a smooth hull burns less fuel, most world trade moves by
#  sea, and the aggregate emissions difference across the fleet is large. This
#  is a climate technology filed under marine paint.
#
#  Goal 14 is claimed in BOTH directions and the record has earned neither
#  half easily. Modern non-biocidal coatings reduce the chemical burden on
#  coastal water, and biofouling management limits the transport of invasive
#  species between ports. Against that stands the tributyltin history, in which
#  this same field devastated mollusc populations for decades. The claim is
#  made on present practice with that history recorded rather than omitted.
#
#  GOAL 3 IS DELIBERATELY NOT CLAIMED, although reduced shipping emissions have
#  air quality benefits. The connection runs through too many steps to survive
#  the sceptical-auditor test in rule 12.
# =============================================================================
SDGS: Tuple[int, ...] = (
    9,  # Industry and innovation, on shipping efficiency and coatings
    12,  # Responsible production, on the move away from broad-spectrum biocides
    13,  # Climate action, on fleet-wide fuel consumption
    14,  # Life below water, on chemical burden and invasive species transport
)


# =============================================================================
#  GLOSSARY
#  Grouped: the process, the chemical era, the alternatives, and how it is
#  judged.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the process -----------------------------------------------------------
    "biofouling",
    "conditioning_film",
    "biofilm",
    "settlement",
    "larval_settlement_cue",
    "macrofouling",
    "calcareous_fouling",
    # -- the chemical era ------------------------------------------------------
    "antifouling_coating",
    "biocide",
    "tributyltin",
    "imposex",
    "self_polishing_copolymer",
    "leaching_rate",
    "booster_biocide",
    # -- the alternatives ------------------------------------------------------
    "foul_release_coating",
    "surface_free_energy",
    "microtopography",
    "quorum_sensing",
    "quorum_quenching",
    "hull_grooming",
    # -- how it is judged ------------------------------------------------------
    "frictional_resistance",
    "hull_roughness",
    "predicted_environmental_concentration",
    "predicted_no_effect_concentration",
    "ecotoxicity",
    "invasive_species_vector",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "biofouling_and_ship_resistance_review",
    "tributyltin_imposex_evidence",
    "afs_convention",
    "foul_release_coating_review",
    "shark_skin_microtopography_antifouling",
    "quorum_sensing_inhibition_furanones",
    "copper_antifouling_environmental_assessment",
    "imo_biofouling_guidelines",
    "in_water_cleaning_capture_review",
    "natural_product_antifoulants_review",
)


# =============================================================================
#  RELATED
#  Six edges. The second is the cross-branch parallel worth following.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- supplies the natural antifoulants, and the supply problem with them ---
    "blue.marine_natural_products",
    # -- the same pattern in agriculture: broad toxicity to specificity --------
    "green.biopesticides",
    # -- mussel adhesion, studied to copy it there and to prevent it here ------
    "blue.marine_biomaterials",
    # -- where a biocide cannot be used because the animals are inside ---------
    "blue.aquaculture_biotechnology",
    # -- the organisms doing the fouling, and how they are detected ------------
    "blue.marine_genomics",
    # -- membrane fouling, the same problem in a different system --------------
    "grey.wastewater_treatment",
)
