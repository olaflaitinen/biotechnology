# =============================================================================
#  biotechnology.branches.white.biopolymers.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two of these edges do work that this record cannot do alone, and one of them
#  is the most important cross-branch link in the white branch.
#
#  `grey.bioremediation` is that link. This record can say that a material
#  mineralises at a given rate under a named test. What it cannot say is what
#  happens in an actual environment, where the organisms present, the
#  temperature, the oxygen availability and the residence time are all
#  different from a standardised vessel. The gap between a laboratory
#  respirometry result and a hedgerow is exactly the gap that
#  `grey.bioremediation` studies for every other material, and a reader
#  interested in whether biodegradation claims hold outside the test should
#  follow it.
#
#  `white.biobased_chemicals` is directly upstream and the boundary is
#  polymerisation. Lactic acid belongs there and polylactic acid belongs here.
#  The stereochemistry link is real rather than nominal: the ratio of lactic
#  acid isomers coming out of the fermentation sets the crystallinity, and
#  therefore the heat resistance, of the finished polymer.
#
#  `red.regenerative_medicine` is included because resorbable polymers are the
#  one application where degradation is the ENTIRE function rather than an
#  end-of-life property, and where the timescale is engineered deliberately
#  against tissue healing rather than against a compost cycle. It is a useful
#  corrective to reading degradation as inherently environmental.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and Goal 14 requires a note because it is the one most likely to be
#  claimed carelessly.
#
#  Life below water is claimed ONLY for the polymers that genuinely mineralise
#  in marine conditions, which in practice means the polyhydroxyalkanoates.
#  Claiming it for industrially compostable materials would be exactly the
#  error this record was written to correct, since those persist in seawater.
#  The distinction is recorded here rather than left to a reader's charity.
# =============================================================================
SDGS: Tuple[int, ...] = (
    9,  # Industry and innovation, on feedstock substitution in materials
    12,  # Responsible production, the primary and best-supported claim
    13,  # Climate action, subject to a benchmarked life cycle assessment
    14,  # Life below water, for genuinely marine-degradable polymers only
)


# =============================================================================
#  GLOSSARY
#  Grouped: the two axes and their vocabulary, the materials, the properties
#  that decide usability, then end of life.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the distinction the record exists to make -----------------------------
    "biopolymer",
    "bioplastic",
    "biobased_content",
    "biodegradation",
    "compostable",
    "industrial_composting",
    "home_composting",
    "marine_biodegradation",
    "mineralisation",
    "disintegration",
    "oxo_degradable",
    "microplastic",
    # -- the materials ---------------------------------------------------------
    "polylactic_acid",
    "polyhydroxyalkanoate",
    "thermoplastic_starch",
    "regenerated_cellulose",
    "bacterial_cellulose",
    "chitosan",
    "alginate",
    "drop_in_polymer",
    # -- whether it can be made and used ---------------------------------------
    "polymerisation",
    "ring_opening_polymerisation",
    "molecular_weight",
    "glass_transition_temperature",
    "crystallinity",
    "barrier_property",
    "compatibilisation",
    "extrusion",
    # -- where it goes afterwards ----------------------------------------------
    "mechanical_recycling",
    "chemical_recycling",
    "end_of_life",
    "life_cycle_assessment",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "en_13432_compostability",
    "astm_d6866_biobased_carbon",
    "polylactic_acid_review",
    "polyhydroxyalkanoate_production_review",
    "biopolymer_lca_comparison",
    "oxo_degradable_plastics_assessment",
    "single_use_plastics_directive",
    "marine_biodegradation_review",
    "biopol_commercial_history",
    "chemical_recycling_polyester_review",
)


# =============================================================================
#  RELATED
#  Six edges. The first is upstream, the second is the reality check.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the monomers, and where the boundary is drawn -------------------------
    "white.biobased_chemicals",
    # -- whether degradation claims hold outside a standardised test -----------
    "grey.bioremediation",
    # -- who accumulates the polymer inside the cell ---------------------------
    "white.metabolic_engineering",
    # -- fermentation and the extraction that dominates PHA cost ---------------
    "white.microbial_fermentation",
    # -- feedstock, and the land question it brings ----------------------------
    "green.plant_genetic_engineering",
    # -- where degradation is the function rather than the disposal ------------
    "red.regenerative_medicine",
)
