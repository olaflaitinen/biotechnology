# =============================================================================
#  biotechnology.branches.red.pharmacogenomics.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two edges below carry more weight than the rest.
#
#  `purple.genetic_data_privacy` is not an optional governance footnote here.
#  A pharmacogenomic result is generated once, must persist for a lifetime to
#  be useful, and reveals information about relatives who were never asked. No
#  other test in this taxonomy has all three properties at once, and a reader
#  who studies the science without the data question has missed the part that
#  actually determines whether the practice is acceptable.
#
#  `yellow.nutrigenomics` is included because it is this record's cautionary
#  twin. The two fields ask structurally identical questions, meaning how does
#  inherited variation change the response to something ingested, and they have
#  arrived at very different evidentiary places. Pharmacogenomics has a small
#  set of variants with large, replicated, clinically actionable effects.
#  Nutrigenomics is dominated by variants with small effects and a
#  direct-to-consumer market that overstates them. Setting them side by side is
#  the clearest way to show what a defensible gene-response claim looks like.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Goal 10 is included, unusually, as a claim that this field could genuinely
#  advance it rather than merely engage it: the tests are cheap, the guidelines
#  are free, and the benefit is largest in health systems with the least
#  capacity to manage adverse reactions. The qualifier is that the reference
#  data are ancestry-skewed, so the advance is conditional on fixing that, and
#  practice.CHALLENGES says so.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Good health and well-being
    10,  # Reduced inequalities, conditionally; see the note above
)


# =============================================================================
#  GLOSSARY
#  Grouped in the order the DESCRIPTION uses them: what is inherited, how it is
#  named, what it is turned into, and what happens to the drug as a result.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- what is inherited ---------------------------------------------------
    "allele",
    "haplotype",
    "diplotype",
    "polymorphism",
    "germline",
    # ---- how it is named ------------------------------------------------------
    "star_allele",
    "genotype",
    "phenotype",
    # ---- what it is turned into ------------------------------------------------
    "activity_score",
    "metaboliser_status",
    "clinical_decision_support",
    # ---- what happens to the drug ----------------------------------------------
    "pharmacokinetics",
    "pharmacodynamics",
    "prodrug",
    "therapeutic_index",
    "adverse_drug_reaction",
)


# =============================================================================
#  REFERENCES
#  The naming of the field, the modern clinical review, the guideline
#  consortium that made it actionable, and the trial that showed panel testing
#  changes outcomes.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "vogel1959",  # the field acquires a name
    "relling2015",  # the standard modern clinical review
    "cpic_guidelines",  # the operative genotype-to-action mapping
    "swen2023",  # the multicentre panel-testing trial
)


# =============================================================================
#  RELATED
#  Seven edges, five crossing a branch boundary. The first is the sibling that
#  handles the somatic half of the same question; the last two are the ones the
#  header note explains.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- the sibling that handles acquired rather than inherited variation ---
    "red.molecular_diagnostics",
    # ---- what the result is used to prescribe ---------------------------------
    "red.pharmaceutical_biotechnology",
    # ---- the computational layer that calls and interprets the genotype -------
    "gold.genomics_data_analysis",
    "gold.multi_omics_integration",
    "gold.machine_learning_in_biology",
    # ---- the question that decides whether the practice is acceptable ---------
    "purple.genetic_data_privacy",
    # ---- the cautionary twin; see the header note -----------------------------
    "yellow.nutrigenomics",
)
