# =============================================================================
#  biotechnology.branches.blue.marine_enzymes.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The edge to `white.industrial_enzymes` is the one that most needs stating,
#  because a reader could reasonably ask why this record exists at all.
#
#      white.industrial_enzymes   the enzyme as a manufactured article,
#                                 measured by durability. Total turnover
#                                 number first, because a fast enzyme with a
#                                 short life is the worse product.
#
#      blue.marine_enzymes        the enzyme as an ADAPTATION, measured by what
#                                 the marine constraint bought. Heat-lability
#                                 appears as a FEATURE rather than a defect.
#
#  The same physical quantity, thermal stability, is a virtue in one record and
#  a product specification in the opposite direction in the other. Nothing
#  about the enzymology differs. The application decides which end of the scale
#  is wanted, and that is why both records are needed and why each states the
#  boundary from its own side.
#
#  `blue.marine_genomics` is a hard dependency. Since most producing organisms
#  cannot be cultured, sequence mining is how candidates are found, and this
#  record inherits that one's reference database poverty and sampling bias
#  along with its catalogues.
#
#  `blue.marine_natural_products` is the instructive contrast rather than a
#  neighbour. Both search the same organisms. One has products and no supply
#  problem because an enzyme is a gene; the other has a supply problem because
#  a molecule has to be made. Reading the two together explains more about the
#  branch than either does alone.
#
#  `white.biocatalysis` is where a marine enzyme becomes a synthetic step, and
#  `blue.seaweed_cultivation` is where the polysaccharide-degrading enzymes in
#  this record are actually applied at tonnage.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and Goal 13 is the one carrying real weight.
#
#  Climate action is claimed on a specific mechanism rather than in general:
#  enzymes that work at low temperature let a process run without being heated,
#  and heating is the dominant energy cost in laundry, in textile processing
#  and in much food manufacture. It is the same argument
#  `white.industrial_enzymes` makes for detergent enzymes, and marine
#  psychrophiles are one of the sources that make the lower temperature
#  achievable.
#
#  GOAL 14 IS DELIBERATELY NOT CLAIMED. This record takes sequences from the
#  ocean and returns nothing to it. Unlike `blue.marine_natural_products`,
#  which can at least argue that its history pushed the field towards
#  sustainable sourcing, there is no benefit to marine life here. Claiming life
#  below water because the enzyme came from the sea would be exactly the
#  unearned credit rule 12 exists to prevent.
# =============================================================================
SDGS: Tuple[int, ...] = (
    9,  # Industry and innovation, on process substitution
    12,  # Responsible production, on steps and reagents removed
    13,  # Climate action, on processes that no longer need heating
)


# =============================================================================
#  GLOSSARY
#  Grouped: the adaptations, the enzymology, how they are found, and how they
#  are made.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the adaptations that justify the record -------------------------------
    "psychrophile",
    "thermophile",
    "hyperthermophile",
    "piezophile",
    "halophile",
    "extremophile",
    "cold_adaptation",
    "heat_labile",
    # -- the enzymology --------------------------------------------------------
    "enzyme",
    "activation_energy",
    "melting_temperature",
    "thermal_denaturation",
    "turnover_number",
    "catalytic_efficiency",
    "conformational_flexibility",
    # -- the marine-specific activities ----------------------------------------
    "dna_polymerase",
    "proofreading_activity",
    "alkaline_phosphatase",
    "agarase",
    "alginate_lyase",
    "chitinase",
    "haloperoxidase",
    "antifreeze_protein",
    # -- finding and making them -----------------------------------------------
    "functional_metagenomics",
    "heterologous_expression",
    "inclusion_body",
    "codon_optimisation",
    "directed_evolution",
    "digital_sequence_information",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "cold_adapted_enzymes_review",
    "psychrophilic_enzyme_structure_function",
    "deep_sea_polymerase_fidelity",
    "functional_metagenomics_enzyme_discovery",
    "extremozymes_industrial_review",
    "halophilic_enzyme_review",
    "piezophile_enzymology_review",
    "marine_polysaccharide_degrading_enzymes",
    "nagoya_protocol",
    "bbnj_agreement",
)


# =============================================================================
#  RELATED
#  Six edges. The first is the record this one is defined against.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same object measured for the opposite property --------------------
    "white.industrial_enzymes",
    # -- how candidates are found, since the producers will not grow -----------
    "blue.marine_genomics",
    # -- the instructive contrast: a gene has no supply problem ----------------
    "blue.marine_natural_products",
    # -- where a marine enzyme becomes a synthetic step ------------------------
    "white.biocatalysis",
    # -- where the polysaccharide enzymes are applied at tonnage ---------------
    "blue.seaweed_cultivation",
    # -- obligations that attach to information rather than material -----------
    "purple.access_benefit_sharing",
)
