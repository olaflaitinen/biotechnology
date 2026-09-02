# =============================================================================
#  biotechnology.branches.red.pharmacogenomics.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the one record in the red branch whose science was settled decades
#  ago and whose problem is entirely one of delivery. The genes are known, the
#  variants are catalogued, the prescribing guidelines are written and freely
#  published, and the tests cost less than a single day in hospital. Almost
#  none of it reaches most patients.
#
#  The public register therefore does something unusual: it spends its final
#  paragraph on implementation rather than on biology, because a reader who
#  understands the science and not the bottleneck has understood the less
#  important half.
#
#  The wine analogy is used deliberately in place of an engineering one.
#  Everybody already accepts, without being taught, that two people metabolise
#  alcohol at different rates. The whole field is that observation, made
#  measurable.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

__all__ = [
    "SUMMARY",
    "DESCRIPTION",
    "PLAIN_LANGUAGE",
    "ANALOGY",
    "WHY_IT_MATTERS",
]


# =============================================================================
#  TECHNICAL REGISTER
# =============================================================================

SUMMARY = (
    "Using inherited genetic variation to predict drug response, dose "
    "requirement and adverse-reaction risk."
)

# -----------------------------------------------------------------------------
#  Structure: (a) definition and scope boundary, (b) where the variation sits,
#  (c) how a genotype becomes a prescribing action, (d) the binding constraint.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) definition and boundary
    "Pharmacogenomics studies how inherited variation changes what a drug does "
    "to a patient and what the patient does to the drug. The boundary that "
    "matters is germline against somatic: variation inherited from a parent "
    "belongs here, while variation acquired by a tumour and used to select a "
    "targeted therapy belongs to `red.molecular_diagnostics`. "
    # (b) where the variation sits
    "Most actionable variation sits in three places: genes encoding "
    "drug-metabolising enzymes, chiefly the cytochrome P450 family and a small "
    "number of transferases; genes encoding transporters such as SLCO1B1 that "
    "govern how much drug reaches a tissue; and immune loci such as HLA, where "
    "a single allele can turn an ordinary medicine into a life-threatening "
    "hypersensitivity reaction. "
    # (c) genotype to action
    "Variation is described using star allele nomenclature, where a haplotype "
    "such as CYP2C19*2 denotes a defined set of variants with a known "
    "functional consequence. The two inherited alleles form a diplotype, which "
    "is translated into an activity score and then into a phenotype: poor, "
    "intermediate, normal, rapid or ultrarapid metaboliser. Guidelines from the "
    "Clinical Pharmacogenetics Implementation Consortium and the Dutch "
    "Pharmacogenetics Working Group map that phenotype to a prescribing action, "
    "and regulators increasingly place the mapping in the product label. "
    # (d) the binding constraint
    "The binding constraint is implementation, not discovery. A result that "
    "does not reach the prescriber inside the electronic health record, at the "
    "moment of prescribing, in a form that requires no interpretation, changes "
    "nothing at all."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Your liver breaks medicines down using a set of tiny chemical tools, and "
    "the instructions for building those tools are written in your genes. Some "
    "people inherit a fast version of a tool, some a slow one, and some none at "
    "all. A fast processor may clear a drug before it has time to work. A slow "
    "processor may build up a dangerous amount from an ordinary dose. A few "
    "people carry a version that makes their immune system attack a particular "
    "medicine outright. A single cheek swab or blood test can show which "
    "versions you carry, and the result does not change during your life, so it "
    "only needs to be done once."
)

# -----------------------------------------------------------------------------
#  The wine analogy. Its limit is visible and useful: alcohol tolerance is
#  affected by many things besides genetics, and so is drug response, which is
#  exactly why a genotype narrows a dose rather than fixing it.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Two people drink the same two glasses of wine. One is fine, the other is "
    "unwell for the evening. Nobody finds this surprising, because we all "
    "accept that bodies process alcohol at different speeds. Medicines are no "
    "different; pharmacogenomics simply measures the speed in advance instead "
    "of discovering it by accident. The comparison has a useful limit: how you "
    "handle wine also depends on your weight, what you ate and what else you "
    "have taken, and the same is true of medicines. A genetic result narrows "
    "the right dose. It does not by itself determine it."
)

WHY_IT_MATTERS = (
    "Adverse drug reactions are among the leading causes of hospital admission "
    "in high-income countries, and a substantial fraction are predictable from "
    "a handful of well-characterised genes. Screening for HLA-B*57:01 before "
    "abacavir has essentially eliminated a life-threatening hypersensitivity "
    "reaction. Screening for DPYD before fluoropyrimidine chemotherapy prevents "
    "deaths from a drug that is otherwise routine. These are not futuristic "
    "claims; they are standard of care in several European health systems "
    "today. The uncomfortable part is that the science has been settled far "
    "longer than the practice has existed. The variants were characterised in "
    "the 1980s and 1990s, the guidelines are free to read, and the test costs "
    "less than one day in a hospital bed, yet most patients in most countries "
    "are still prescribed as though everyone metabolised identically. The "
    "obstacles are electronic health records, reimbursement rules and clinical "
    "workflow, none of which is a scientific problem. There is a second "
    "problem: the reference data are drawn overwhelmingly from people of "
    "European ancestry, so the populations with the least evidence behind their "
    "results are the ones already least well served."
)
