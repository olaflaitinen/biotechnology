# =============================================================================
#  biotechnology.branches.white.biopolymers.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by the two-axis classification from `narrative.py`
#  rather than by industry, and this is the most consequential editorial
#  decision in the record. A reader who sees bio-polyethylene listed under
#  DURABLE and polylactic acid under INDUSTRIALLY COMPOSTABLE has already
#  learned the distinction that the rest of the subject depends on, without
#  being told it twice.
#
#  Each group states the end-of-life condition explicitly, because a list of
#  biopolymer applications that omits where each one is supposed to go would
#  reproduce exactly the confusion this record exists to correct.
#
#  TECHNOLOGIES follow the three production routes, then the two things that
#  decide whether the material is usable at all: processing on existing
#  equipment, and property modification. A biopolymer that cannot run on the
#  converter's existing extruder is not a product.
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
#  Grouped by the two axes. End-of-life stated for every group.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- BIOBASED AND DURABLE: recyclable, not compostable ---------------------
    "Bio-based polyethylene from sugarcane ethanol, chemically identical to the "
    "fossil polymer, recycled in the existing stream and not compostable in any "
    "environment",
    "Partly bio-based polyethylene terephthalate for beverage bottles, using "
    "bio-derived monoethylene glycol, recycled as ordinary PET",
    "Bio-based polyamides from castor oil, used in automotive and textile "
    "applications for performance as much as for origin",
    "Polytrimethylene terephthalate fibre from bio-based propanediol, adopted "
    "because its elastic recovery differs from the petrochemical alternative",
    "Bio-based polyurethanes and epoxy resins using vegetable oil polyols",
    # -- BIOBASED AND INDUSTRIALLY COMPOSTABLE ---------------------------------
    "Polylactic acid in food service ware, rigid packaging and fibre, "
    "compostable in industrial conditions and persistent in soil, home compost "
    "and seawater",
    "Starch-based and starch-blend films for caddy liners and carrier bags, "
    "where compostability is the point because the item is food-contaminated",
    "Regenerated cellulose film and fibre, among the oldest materials in this "
    "record and biodegradable in a range of environments",
    "Agricultural mulch film designed to be tilled into soil, one of the few "
    "applications where soil biodegradability rather than compostability is the "
    "requirement",
    # -- BIOBASED AND BROADLY BIODEGRADABLE, INCLUDING MARINE -------------------
    "Polyhydroxyalkanoates for packaging, coatings and single-use items, which "
    "degrade in ambient soil and marine conditions because environmental "
    "organisms already carry the depolymerases",
    "Polyhydroxyalkanoate coatings on paper, which replace the thin "
    "polyethylene layer that makes coated paper cups difficult to recycle",
    # -- FOSSIL AND COMPOSTABLE: the quadrant people forget ---------------------
    "Polybutylene adipate terephthalate and polycaprolactone, certified "
    "compostable and manufactured from petroleum, usually blended with starch "
    "or polylactic acid to make those materials tough enough to use",
    # -- MEDICAL, WHERE DEGRADATION IS THE ENTIRE FUNCTION ----------------------
    "Resorbable sutures, screws and scaffolds from polylactic and polyglycolic "
    "acid, where controlled degradation inside the body is the product feature "
    "and the timescale is engineered deliberately",
    "Hydrogels and drug delivery matrices from alginate, chitosan and "
    "hyaluronic acid",
    # -- NOT A PLASTIC AT ALL ----------------------------------------------------
    "Bacterial cellulose for wound dressings, membranes and food applications",
    "Xanthan, gellan and other microbial polysaccharides used as thickeners and "
    "rheology modifiers rather than as structural materials",
)


# =============================================================================
#  TECHNOLOGIES
#  The three routes, then what makes the material actually usable.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- route one: polymerise a biobased monomer -----------------------------
    "Ring-opening polymerisation of lactide to polylactic acid, which is how "
    "high molecular weight is reached where direct condensation stalls",
    "Polycondensation of biobased diacids and diols into polyesters and "
    "polyamides",
    "Stereochemical control of the lactide feed, since the ratio of the two "
    "lactic acid isomers sets crystallinity and therefore heat resistance",
    # ---- route two: let the organism make the polymer --------------------------
    "Fermentative accumulation of polyhydroxyalkanoate granules inside bacterial "
    "cells, which are storage material rather than a secreted product",
    "Copolymer composition control by feeding different carbon sources, which "
    "tunes brittleness and melting point across a wide range",
    "Mixed culture accumulation on waste streams and volatile fatty acids, "
    "which avoids the sterile sugar feedstock that dominates the cost",
    "Polymer recovery by solvent extraction or by digesting the cell around the "
    "granule, which is the step that has kept this material expensive",
    # ---- route three: modify a polymer that already exists ----------------------
    "Regeneration and derivatisation of cellulose into film, fibre and esters",
    "Thermoplastic starch production by plasticising starch so it can be "
    "extruded at all",
    "Extraction and modification of chitin, alginate and other structural "
    "biopolymers",
    # ---- making it processable on existing machinery ----------------------------
    "Melt processing on conventional extrusion, injection moulding and film "
    "lines, which is a hard requirement rather than a convenience since "
    "converters will not re-equip for a new material",
    "Drying and hydrolysis control during processing, because polyesters "
    "degrade in the melt if moisture is present",
    "Nucleation and annealing to raise crystallinity and therefore heat "
    "resistance",
    # ---- making it perform ------------------------------------------------------
    "Blending and compatibilisation, which is how brittle biopolymers are made "
    "tough and why fossil compostable polyesters appear in biobased products",
    "Plasticisers, impact modifiers and mineral fillers",
    "Barrier coatings and multilayer structures for oxygen and moisture, which "
    "is where biopolymers most often fall short of the incumbent",
    "Chemical recycling back to monomer, which for a polyester is a genuine "
    "alternative to composting and is increasingly preferred to it",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "cupriavidus_necator",  # the classic PHA accumulator, storage to high cell fraction
    "escherichia_coli",  # engineered PHA and monomer production, easier to lyse
    "lactobacillus_delbrueckii",  # lactic acid for the polylactic acid route
    "komagataeibacter_xylinus",  # bacterial cellulose of very high purity
    "xanthomonas_campestris",  # xanthan gum, a secreted polysaccharide
    "zea_mays",  # maize starch, the feedstock for starch blends and much PLA
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "polymerisation",
    "extrusion",
    "gel_permeation_chromatography",
    "differential_scanning_calorimetry",
    "mechanical_testing",
    "respirometry",
    "life_cycle_assessment",
)


# =============================================================================
#  CHALLENGES
#  The first is not a materials problem at all, and putting it first is the
#  honest ordering.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the constraint that is not chemistry ----------------------------------
    "Absence of collection and industrial composting infrastructure, which is "
    "the binding constraint on compostable materials and cannot be solved by "
    "any improvement to the polymer",
    "Contamination of recycling streams by compostable items that visually "
    "resemble conventional plastic, so that in the wrong place a compostable "
    "package is worse than the one it replaced",
    # -- the language problem ---------------------------------------------------
    "Conflation of biobased with biodegradable in procurement, labelling and "
    "public understanding, which causes materials to be chosen for properties "
    "they do not have",
    "Conflation of disintegration with biodegradation, since a material that "
    "breaks into small fragments has not mineralised and fragmentation is how "
    "microplastics are produced",
    # -- performance ------------------------------------------------------------
    "Oxygen and moisture barrier performance below that of the incumbent "
    "polymers, which restricts shelf life and therefore application",
    "Heat resistance, since polylactic acid softens near temperatures a hot "
    "drink reaches without deliberate crystallinity control",
    "Brittleness requiring blending, which is why fossil-derived compostable "
    "polyesters are present in many nominally biobased products",
    "Melt processing sensitivity to moisture, which degrades molecular weight "
    "during extrusion",
    # -- cost --------------------------------------------------------------------
    "Cost per tonne above the fossil incumbent, whose plants are depreciated "
    "and whose scale is very much larger",
    "Polymer recovery cost for intracellular polyhydroxyalkanoates, which is "
    "the single largest reason a material with excellent environmental "
    "credentials remains a niche product",
    # -- the claim ----------------------------------------------------------------
    "Substantiating the environmental claim, since a biobased polymer with "
    "agricultural feedstock can carry a larger land, water and eutrophication "
    "burden than the fossil polymer it replaces",
    "End-of-life accounting, where composting recovers no material value and "
    "mechanical or chemical recycling may be environmentally preferable to "
    "biodegradation for a durable item",
)
