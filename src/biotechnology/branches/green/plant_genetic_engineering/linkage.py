# =============================================================================
#  biotechnology.branches.green.plant_genetic_engineering.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Three edges below are load-bearing rather than decorative.
#
#  `green.plant_tissue_culture` is a PREREQUISITE, not a neighbour. Every
#  transgenic plant that has ever existed was regenerated from a single
#  transformed cell in a sterile jar. When a genotype is described as
#  impossible to engineer, the failure is almost always regeneration rather
#  than DNA delivery. A reader who skips that record will misattribute the
#  field's main laboratory bottleneck.
#
#  `green.agricultural_genome_editing` is the successor technology and the
#  contrast that makes this record legible. Same laboratory, same people, same
#  crops; a completely different regulatory position in most of the world,
#  because editing usually leaves no foreign DNA. Reading the two side by side
#  shows how much of what is attributed to the technology is actually
#  attributable to the law.
#
#  `red.gene_therapy` is included deliberately. The molecular operation is the
#  same operation. The governance, the public reaction and the cost structure
#  are entirely different, and the comparison is one of the most instructive in
#  the whole taxonomy.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and the first is claimed carefully. This technology has demonstrably
#  reduced insecticide exposure and protected yield under pest pressure, which
#  serves goal 2. It has not, so far, reached the crops eaten by the most
#  food-insecure populations, for the cost reasons in governance.py. Both halves
#  are recorded in narrative.WHY_IT_MATTERS, and the goal is claimed on the
#  evidence that exists rather than on the aspiration.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on protected yield and reduced crop loss
    12,  # Responsible consumption and production, on reduced insecticide use
    15,  # Life on land, engaged in both directions: less spraying, but gene
    #     flow and resistant weeds are real costs. practice.CHALLENGES says so.
)


# =============================================================================
#  GLOSSARY
#  Grouped as a reader meets them: what is inserted, how it gets in, what comes
#  out, and the vocabulary of the argument about it.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- what is inserted ----------------------------------------------------
    "transgene",
    "promoter",
    "terminator",
    "selectable_marker",
    "cry_protein",
    # ---- how it gets in -------------------------------------------------------
    "t_dna",
    "ti_plasmid",
    "biolistics",
    "transformation",
    # ---- what comes out --------------------------------------------------------
    "event",
    "copy_number",
    "gene_silencing",
    "backcross",
    # ---- the vocabulary of the argument -----------------------------------------
    "gmo",
    "substantial_equivalence",
    "coexistence",
    "adventitious_presence",
    "gene_flow",
    "refuge",
)


# =============================================================================
#  REFERENCES
#  The founding demonstration, the humanitarian proof of concept, the largest
#  independent evidence review, and the annual deployment survey.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "fraley1983",  # first transgenic plants
    "ye2000",  # Golden Rice prototype
    "nasem2016",  # the National Academies evidence review
    "isaaa_brief",  # the annual global deployment survey
)


# =============================================================================
#  RELATED
#  Eight edges. Three are explained in the header note; the rest connect this
#  record to the breeding, propagation and legal machinery it depends on.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the prerequisite, not a neighbour ------------------------------------
    "green.plant_tissue_culture",
    # ---- the successor technology, and the contrast that explains this one ----
    "green.agricultural_genome_editing",
    # ---- what an event is crossed into once it exists -------------------------
    "green.molecular_plant_breeding",
    # ---- the trait most commercial events actually carry ----------------------
    "green.biopesticides",
    # ---- the same molecular operation, a different world -----------------------
    "red.gene_therapy",
    # ---- where drought and salinity traits are headed --------------------------
    "brown.drought_tolerance_engineering",
    # ---- who owns the event, and who owns the tool used to make it ------------
    "purple.biotechnology_patents",
    # ---- the law that decides whether it may exist at all ----------------------
    "purple.biosafety_law",
)
