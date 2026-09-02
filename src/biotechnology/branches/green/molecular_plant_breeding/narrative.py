# =============================================================================
#  biotechnology.branches.green.molecular_plant_breeding.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the quiet giant of the green branch, and the public register is
#  written to say so plainly. Genetic engineering attracts the argument;
#  marker-assisted and genomic selection delivered most of the actual yield
#  gain of the last thirty years.
#
#  Nothing here creates a genetically modified organism. The alleles being
#  selected already exist in the species, and the only thing that changed is
#  the speed and accuracy of choosing between plants that could all have been
#  produced by a farmer with a paintbrush. That is why the regulatory status is
#  UNREGULATED while both neighbouring records are not, and it is the single
#  most useful fact a reader can take from this record.
#
#  The form-guide analogy is chosen because it captures the real change
#  precisely: the audition still happens, but only for a shortlist, so the same
#  effort covers far more candidates.
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
    "Accelerating conventional breeding with DNA markers and genomic "
    "prediction so that selection happens at the seedling stage."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what classical breeding costs, (b) marker-assisted selection
#  for simple traits, (c) genomic selection for everything else, (d) the
#  quantity the whole field actually optimises.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the problem
    "Classical breeding evaluates a plant by growing it. Phenotype is observed, "
    "superior individuals are crossed, and the cycle repeats once per season. "
    "Every wrong candidate occupies field space, water and a year. "
    # (b) marker-assisted selection
    "Molecular breeding replaces part of that observation with genotyping. "
    "Marker-assisted selection works where a trait is controlled by one or a "
    "few large-effect loci: a DNA marker tightly linked to the favourable "
    "allele is scored in a seedling, and unwanted individuals are discarded "
    "before they reach the field. Marker-assisted backcrossing additionally "
    "selects against the donor genome elsewhere, recovering the recurrent "
    "parent in three generations rather than six. "
    # (c) genomic selection
    "Most traits of economic value are polygenic, and for those genomic "
    "selection is used instead. A training population is both genotyped and "
    "phenotyped; a statistical model estimates the effect of every marker "
    "simultaneously rather than testing them one at a time; the model then "
    "predicts a genomic estimated breeding value for candidates that have "
    "never been grown. No individual marker needs to reach significance, which "
    "is what makes the method work for traits controlled by thousands of loci "
    "of tiny effect. "
    # (d) what is actually optimised
    "Combined with speed breeding under extended photoperiod, this compresses "
    "the breeding cycle from years to months. The quantity being optimised is "
    "not accuracy but genetic gain per unit time, and shortening the cycle "
    "raises it even when prediction accuracy falls, which is why breeders will "
    "trade one for the other deliberately."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Breeding a better wheat variety used to mean planting thousands of "
    "seedlings, waiting a whole season, measuring which ones did best, and "
    "starting again. Now a tiny piece of leaf from a two-week-old seedling can "
    "be tested and its DNA read like a form guide. The plants unlikely to "
    "perform are removed before they take up space, and only the promising ones "
    "are grown on. The plants themselves are entirely ordinary. Nothing has "
    "been added to them and nothing has been changed; every one of them could "
    "have been produced by a farmer with a paintbrush and enough patience. What "
    "changed is the speed of choosing between them."
)

# -----------------------------------------------------------------------------
#  The form-guide analogy. Its limit is honest and is the field's real
#  weakness: references predict poorly for a candidate unlike anyone the
#  scout has seen before, which is exactly why prediction accuracy collapses
#  across unrelated germplasm.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is the difference between auditioning every candidate for a full season "
    "and reading their references first. The audition still happens, but only "
    "for the shortlist, so the same effort covers far more candidates. The "
    "comparison has an honest limit: references are only useful if the referee "
    "has seen people like this candidate before. Predict for a plant unrelated "
    "to anything in the training set and the accuracy collapses, which is the "
    "central practical weakness of the method."
)

WHY_IT_MATTERS = (
    "Almost all of the yield improvement in the world's staple crops over the "
    "last thirty years came from breeding, not from transgenes, and molecular "
    "tools roughly doubled the rate at which breeders can deliver it. Because "
    "nothing foreign is introduced, the resulting varieties face no special "
    "regulatory hurdle anywhere in the world. That makes this the most "
    "transferable technology in the green branch: national programmes and CGIAR "
    "centres use it as routinely as multinationals do, and a genotyping service "
    "costs a few euro per sample rather than tens of millions per event. The "
    "costs are real but different in kind. Genotyping has become cheap enough "
    "that phenotyping is now the bottleneck, and measuring a thousand plots "
    "accurately is expensive and unglamorous work that funders do not like "
    "paying for. Prediction models trained on elite material perform badly on "
    "landraces and wild relatives, which risks narrowing the genetic base "
    "further at exactly the moment climate variability makes breadth most "
    "valuable. And the public and private sectors both hold data they will not "
    "share, so the largest single improvement available to the field, meaning "
    "bigger and more diverse training populations, is blocked by something "
    "that is not a scientific problem at all."
)
