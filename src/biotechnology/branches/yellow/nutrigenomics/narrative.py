# =============================================================================
#  biotechnology.branches.yellow.nutrigenomics.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record closes the yellow branch and it is the one where the gap between
#  claim and evidence is widest. The narrative has to be exact in both
#  directions, because the field contains real biology and a large commercial
#  layer that the biology does not support.
#
#  WHAT IS ESTABLISHED is monogenic: single genes with large effects, where a
#  variant genuinely determines what a person should eat. Phenylketonuria,
#  lactase persistence, coeliac disease risk and hereditary haemochromatosis
#  are real, mechanistically understood, and clinically actionable.
#
#  WHAT IS NOT ESTABLISHED is the polygenic promise, which is what is actually
#  sold: that a panel of common variants predicts how an individual responds to
#  fat, carbohydrate, caffeine or salt well enough to guide their diet. Effect
#  sizes for common variants are small, interactions with diet are smaller
#  still, and the largest controlled trials have found that genotype-matched
#  diets do not outperform the alternatives.
#
#  THE HONEST SUMMARY IS THAT THE FIELD'S BEST RESULTS ARE OLD AND RARE, ITS
#  MARKETING IS NEW AND COMMON, and the intervening science has largely
#  returned negative or null findings that the commercial layer has not
#  absorbed.
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
    "The interaction between diet and the genome, where monogenic effects are "
    "established and the polygenic personalisation being sold is not."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the two halves of the field, (b) what the monogenic half has
#  delivered, (c) why the polygenic half has not, (d) what has actually
#  predicted response better than genotype.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the two halves
    "Nutrigenomics covers two questions that are frequently conflated. "
    "Nutrigenetics asks how a person's genotype affects their response to food. "
    "Nutrigenomics proper asks how food affects gene expression, which is a "
    "mechanistic question about regulation rather than a predictive one about "
    "individuals. The commercial field concerns the first, and within it the "
    "distinction that matters is between monogenic effects, where one variant "
    "has a large consequence, and polygenic ones, where many variants each "
    "have a small consequence. "
    # (b) the monogenic half
    "The monogenic half is established and clinically useful. Phenylketonuria "
    "is a single-gene disorder in which dietary phenylalanine causes "
    "irreversible neurological damage, it is detected by newborn screening in "
    "most health systems, and dietary management prevents the damage entirely. "
    "Lactase persistence is a well-characterised variant determining whether an "
    "adult digests lactose. Hereditary haemochromatosis alters iron handling "
    "with direct dietary and clinical consequences. Coeliac disease risk "
    "depends on defined HLA types, and their absence effectively excludes the "
    "diagnosis. These are real gene-diet interactions with large effects, and "
    "they were understood before the field acquired its name. "
    # (c) why the polygenic half has not delivered
    "The polygenic half is what is sold and what the evidence does not "
    "support. Common variants associated with body weight, lipid response or "
    "caffeine metabolism have small individual effects, and the interaction "
    "between such a variant and a dietary component is smaller again. Detecting "
    "an interaction reliably requires far larger samples than detecting a main "
    "effect, and most published gene-diet interactions have not replicated. The "
    "largest controlled trials assigning diets by genotype have found no "
    "advantage over assigning them otherwise. "
    # (d) what did predict better
    "What has predicted individual response better than genotype is more "
    "interesting than the negative result alone. Studies measuring postprandial "
    "glucose and lipid responses have found large and reproducible differences "
    "between people eating identical meals, and that those differences are "
    "predicted substantially by the gut microbiome, by meal composition, by "
    "sleep and by physical activity, with genetics contributing modestly. "
    "Personalised nutrition is therefore a defensible idea whose best current "
    "basis is not genomic, which is an awkward finding for a field named after "
    "genomes."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "This is the study of how what you eat interacts with the genes you were "
    "born with. Some of it is completely established. A small number of people "
    "have a single gene difference that means a particular food genuinely harms "
    "them, and newborn babies are tested for one of these because catching it "
    "early prevents permanent brain damage. Whether adults can digest milk is "
    "also down to one well-understood gene. But the tests sold online promising "
    "a diet matched to your DNA are a different matter. When researchers have "
    "tested that properly, matching diets to genes has not worked better than "
    "not doing so. What does seem to predict how someone responds to a meal is "
    "their gut bacteria, their sleep and their activity, more than their genes."
)

# -----------------------------------------------------------------------------
#  The allergy analogy. Chosen because it separates a real large-effect
#  individual difference from a claimed small-effect one using an example
#  everybody already accepts, and because its limit is exactly the record's
#  argument.
# -----------------------------------------------------------------------------
ANALOGY = (
    "A severe nut allergy is a genuine instruction about what one person must "
    "not eat, and nobody doubts it. The claim being sold is that everyone "
    "carries a comparable set of instructions, subtler but equally real, "
    "waiting to be read from their DNA. The comparison is where the argument "
    "breaks: the allergy is a large effect in a few people, and what the tests "
    "report is a collection of very small effects in everyone, which is a "
    "different kind of thing and not simply a quieter version of the same one."
)

WHY_IT_MATTERS = (
    "The established part of this field prevents severe and permanent harm. "
    "Newborn screening for phenylketonuria, followed by dietary management, "
    "prevents irreversible intellectual disability, and it is among the "
    "clearest demonstrations anywhere that a gene-diet interaction can be "
    "identified and acted on. Understanding lactase persistence explains a "
    "difference in digestion across populations that was previously described "
    "as an abnormality in the majority of the world's adults. Defined HLA types "
    "make it possible to exclude coeliac disease rather than only to suspect "
    "it. The costs of the unestablished part are real too. Direct-to-consumer "
    "tests sell dietary advice on variants whose effects are small and whose "
    "interactions with diet have frequently failed to replicate, and the advice "
    "given is usually generic advice with a genetic justification attached. "
    "That is not harmless: it displaces attention from interventions that work, "
    "it risks people restricting foods on weak evidence, and it lends the "
    "authority of a genome to a recommendation that did not come from one. The "
    "field also carries a genuine privacy exposure, since a dietary test is a "
    "genetic test and the data is subject to the concerns "
    "`purple.genetic_data_privacy` sets out, frequently without the consent "
    "process a clinical test would require. And the most useful recent finding "
    "in personalised nutrition, that response is predicted better by the "
    "microbiome and by behaviour than by genotype, is one the commercial layer "
    "of this field has been slow to absorb."
)
