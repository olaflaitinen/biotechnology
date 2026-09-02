# =============================================================================
#  biotechnology.branches.green.animal_biotechnology.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Three edges here each carry something the record cannot say alone.
#
#  `green.molecular_plant_breeding` runs the same equation, the same models and
#  in several cases the same software. Genomic selection was proposed for
#  livestock in 2001, adopted by the dairy industry from 2009, and moved into
#  crops afterwards. A reader who understands genomic prediction in cattle
#  understands it in wheat; what differs is generation interval and
#  reproductive rate, not statistics.
#
#  `red.regenerative_medicine` is a descendant rather than a neighbour. Dolly
#  established that differentiation is reversible and that an adult specialised
#  cell keeps its complete genome in usable form. Induced pluripotent stem
#  cells a decade later are the direct consequence, and cloning's scientific
#  legacy has mattered far more than cloning itself ever did commercially.
#
#  `purple.bioethics` is not a governance footnote here. This is the only
#  record in the green branch whose subject can suffer, and several of its
#  techniques exist specifically to reduce suffering while others are
#  indifferent to it. The record reports both directions and settles neither.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three. Goal 3 is claimed on antimicrobial resistance specifically: an animal
#  that cannot be infected needs no antibiotics, and veterinary antimicrobial
#  use is a substantial contributor to resistance in human medicine. Goal 13 is
#  claimed on emissions intensity, meaning emissions per unit of product, which
#  falls as output per animal and survival rise. Neither claim asserts that
#  livestock production is low-impact; both concern the impact per unit.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on output per animal and reduced mortality
    3,  # Good health and well-being, on antimicrobial use avoided
    13,  # Climate action, on emissions intensity per unit of product
)


# =============================================================================
#  GLOSSARY
#  Grouped by the three layers, then the diversity vocabulary the costs are
#  measured in.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- layer one, reproduction ---------------------------------------------
    "artificial_insemination",
    "superovulation",
    "embryo_transfer",
    "sexed_semen",
    "cryopreservation",
    # ---- layer two, prediction ------------------------------------------------
    "breeding_value",
    "selection_index",
    "generation_interval",
    "reliability",
    "progeny_test",
    # ---- layer three, alteration -----------------------------------------------
    "somatic_cell_nuclear_transfer",
    "zygote",
    "mosaicism",
    "polled",
    "intentional_genomic_alteration",
    # ---- what the gain costs -----------------------------------------------------
    "inbreeding",
    "effective_population_size",
    "correlated_response",
    # ---- why disease resistance matters beyond the herd ---------------------------
    "zoonosis",
    "antimicrobial_resistance",
)


# =============================================================================
#  REFERENCES
#  The cloning result, the paper that reframed selection, the modern
#  implementation review, and the disease resistance proof of concept.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "wilmut1997",  # Dolly, and the reversibility of differentiation
    "meuwissen2001",  # genomic selection, proposed here first
    "vanraden2020",  # how genomic selection is actually implemented
    "whitworth2016",  # PRRS-resistant pigs
)


# =============================================================================
#  RELATED
#  Seven edges. The first, fourth and last are the ones explained in the header
#  note.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the same equation, a different kingdom ------------------------------
    "green.molecular_plant_breeding",
    # ---- the other half of keeping animals healthy ---------------------------
    "green.veterinary_vaccines",
    # ---- the editing toolkit, applied to zygotes instead of seedlings --------
    "green.agricultural_genome_editing",
    # ---- what Dolly actually led to ------------------------------------------
    "red.regenerative_medicine",
    # ---- the same techniques in an aquatic species ---------------------------
    "blue.aquaculture_biotechnology",
    # ---- the alternative to farming animals at all ---------------------------
    "yellow.alternative_proteins",
    # ---- the question this record reports and does not settle ----------------
    "purple.bioethics",
)
