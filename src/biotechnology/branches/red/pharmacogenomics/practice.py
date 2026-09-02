# =============================================================================
#  biotechnology.branches.red.pharmacogenomics.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications below are grouped by the KIND of harm each prevents, not by
#  therapeutic area, because that is the distinction that decides whether a
#  test is worth doing. Preventing a catastrophic idiosyncratic reaction, as in
#  the HLA group, is a different proposition from optimising a dose, and the
#  evidence bar for each is different too.
#
#  The technologies list is short by the standards of this library. That is
#  honest: genotyping a known panel of variants is a solved problem, and almost
#  all of the difficulty has moved into the last group, which is software and
#  workflow rather than laboratory work.
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
#  Grouped by the kind of harm prevented, because that decides the evidence
#  bar and the economics.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- preventing a catastrophic immune reaction -----------------------------
    "HLA-B*57:01 screening before abacavir, which has essentially eliminated a "
    "life-threatening hypersensitivity syndrome",
    "HLA-B*15:02 screening before carbamazepine in populations where the allele "
    "is common",
    "HLA-B*58:01 screening before allopurinol",
    # -- preventing lethal toxicity from a normal dose --------------------------
    "DPYD screening before fluorouracil and capecitabine chemotherapy",
    "TPMT and NUDT15 screening before thiopurine therapy",
    "UGT1A1 genotyping before irinotecan",
    # -- preventing treatment failure --------------------------------------------
    "CYP2C19-guided antiplatelet therapy in acute coronary syndrome, where a "
    "poor metaboliser does not activate clopidogrel",
    "CYP2D6-guided use of codeine and tramadol, which are prodrugs and are "
    "therefore ineffective in poor metabolisers and dangerous in ultrarapid "
    "ones",
    # -- optimising a dose ---------------------------------------------------------
    "CYP2D6 and CYP2C19-guided dosing of antidepressants",
    "CYP2D6-guided use of tamoxifen",
    "SLCO1B1 genotyping and statin-associated muscle symptom risk",
    "VKORC1 and CYP2C9 informed warfarin dosing algorithms",
    # -- doing it once, in advance ---------------------------------------------------
    "Pre-emptive panel testing at first contact with a health system, so that "
    "the result is already present when any future prescription is written",
)


# =============================================================================
#  TECHNOLOGIES
#  Short by design. The laboratory problem is solved; the difficulty is in the
#  last group.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- generating the genotype ---------------------------------------------
    "Targeted genotyping arrays covering pharmacogene star alleles",
    "Long-read sequencing to resolve CYP2D6 copy number, hybrid genes and "
    "structural rearrangements that short reads cannot phase",
    "Extraction from saliva or buccal swab, avoiding a blood draw",
    # ---- turning a genotype into a phenotype -----------------------------------
    "Star-allele calling software with curated allele definition tables",
    "Diplotype-to-activity-score translation, then activity score to phenotype",
    "Population allele frequency reference databases",
    # ---- turning a phenotype into an action ------------------------------------
    "Clinical decision support fired at the moment of prescribing rather than "
    "reported to a file",
    "Structured storage of the result so that it survives a change of care "
    "provider or of records system",
    "Therapeutic drug monitoring as an orthogonal check where the stakes are "
    "high",
)


# =============================================================================
#  ORGANISMS
#  One. This is the only subtype in the red branch that studies no organism
#  other than the patient: there is no production host, no model system and no
#  source organism for a tool.
# =============================================================================
ORGANISMS: Tuple[str, ...] = ("homo_sapiens",)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "pcr",
    "next_generation_sequencing",
    "microarray",
    "mass_spectrometry",
    "digital_pcr",
)


# =============================================================================
#  CHALLENGES
#  One technical, then six that are structural, economic or ethical. That
#  weighting is the point of the record.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the one genuinely technical problem left ------------------------------
    "Structural variation in CYP2D6, including gene deletions, duplications "
    "and hybrid genes, which short-read sequencing cannot resolve and which "
    "affects one of the most clinically important genes in the panel",
    # -- the evidence base is uneven --------------------------------------------
    "Allele frequencies and clinical evidence drawn overwhelmingly from people "
    "of European ancestry, so the populations least well served by existing "
    "medicine are also those with the weakest evidence behind their results",
    # -- workflow ----------------------------------------------------------------
    "Getting the result in front of the prescriber at the moment of decision, "
    "which is an electronic health record problem rather than a genetic one",
    "Alert fatigue, where a decision support system that fires too often is "
    "switched off entirely and takes the useful alerts with it",
    # -- economics ----------------------------------------------------------------
    "Reimbursement designed for reactive testing of one gene against one drug, "
    "rather than for pre-emptive panel testing whose benefit accrues over "
    "decades and to a different budget",
    # -- persistence ---------------------------------------------------------------
    "Result portability over a lifetime, across providers, systems and "
    "countries, for data that never changes and should therefore never need "
    "regenerating",
    # -- the market ----------------------------------------------------------------
    "Direct-to-consumer reports that outrun the underlying evidence, offering "
    "actionable-sounding conclusions from variants with no established clinical "
    "consequence",
)
