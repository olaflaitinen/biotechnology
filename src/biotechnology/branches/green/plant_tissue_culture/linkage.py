# =============================================================================
#  biotechnology.branches.green.plant_tissue_culture.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The first two edges are the reason this record exists in the taxonomy at
#  all, and the direction of dependency matters.
#
#  `green.plant_genetic_engineering` and `green.agricultural_genome_editing`
#  DEPEND ON this record. Neither can produce a plant without it. When a
#  genotype is described as impossible to engineer, the failure is almost never
#  DNA delivery; it is that nobody can persuade that variety to regenerate.
#  Both of those records point back here, and this is the only place in the
#  green branch where the dependency runs in a single clear direction.
#
#  The edge to `red.regenerative_medicine` is worth following for the contrast
#  rather than the similarity. Both fields grow tissue from cells on a defined
#  medium with controlled signals. Plant cells retain totipotency and will
#  rebuild an entire organism; animal cells lost that capacity, which is why
#  one record produces whole banana plants by the million and the other cannot
#  yet produce a liver.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Two, both defensible on delivered outcomes rather than on aspiration.
#  Goal 2 rests on clean-seed programmes for cassava, sweet potato, potato and
#  banana, which are among the clearest food security interventions in this
#  branch. Goal 15 rests on in vitro genebanks and cryopreservation for species
#  whose seed cannot be dried and frozen, and is qualified in both directions:
#  the same technique that conserves rare genotypes also replaces thousands of
#  local varieties with one when applied commercially.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on disease-free planting material for staple root crops
    15,  # Life on land, on conservation, and qualified as above
)


# =============================================================================
#  GLOSSARY
#  Grouped as the DESCRIPTION uses them: the property, the ingredients, the
#  routes out, and what goes wrong.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- the property being exploited ----------------------------------------
    "totipotency",
    "explant",
    "meristem",
    # ---- what is in the jar ----------------------------------------------------
    "auxin",
    "cytokinin",
    "basal_medium",
    "aseptic_technique",
    # ---- routes from cell to plant ----------------------------------------------
    "callus",
    "organogenesis",
    "somatic_embryogenesis",
    "protoplast",
    "synthetic_seed",
    # ---- what goes wrong ---------------------------------------------------------
    "somaclonal_variation",
    "hyperhydricity",
    "endophyte",
    "acclimatisation",
    # ---- storing it -----------------------------------------------------------------
    "cryopreservation",
    "vitrification",
)


# =============================================================================
#  REFERENCES
#  The relationship that made it a technique, the medium everyone still uses,
#  and the standard reference work.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "skoog1957",  # hormonal control of organogenesis
    "murashige1962",  # the medium, still the default sixty years later
    "george2008",  # the standard reference work on plant propagation in vitro
)


# =============================================================================
#  RELATED
#  Seven edges. The first two depend on this record rather than merely relating
#  to it, and the fifth is a contrast rather than a similarity.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- records that cannot function without this one -----------------------
    "green.plant_genetic_engineering",
    "green.agricultural_genome_editing",
    # ---- where doubled haploids and rescued embryos feed a breeding programme -
    "green.molecular_plant_breeding",
    # ---- propagating the varieties bred for dry and saline land ---------------
    "brown.arid_land_crops",
    # ---- the same idea in an organism that lost totipotency -------------------
    "red.regenerative_medicine",
    # ---- in vitro genebanks and cryopreservation of wild relatives ------------
    "grey.biodiversity_conservation",
    # ---- who owns the germplasm being propagated ------------------------------
    "purple.access_benefit_sharing",
)
