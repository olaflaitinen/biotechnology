# =============================================================================
#  biotechnology.branches.green.animal_biotechnology.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Every technique in this record acts on a sentient animal, and that fact
#  changes how the public register has to be written. It is not enough to
#  describe what is done and note the welfare question at the end.
#
#  Several of these technologies exist SPECIFICALLY to reduce suffering that
#  current farming imposes: removing horn growth so calves are not disbudded
#  with a hot iron, making pigs immune to a virus that kills millions a year,
#  producing hornless or heat-tolerant animals. Others raise welfare concerns
#  of their own, particularly selection pressed hard on production traits. Both
#  directions are stated, and the record links to `purple.bioethics` rather
#  than implying the question is settled.
#
#  The racehorse analogy is chosen because it isolates the actual change: the
#  animals are the same animals, and the information arrives decades earlier.
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
    "Reproductive, genomic and genetic technologies applied to livestock to "
    "improve productivity, welfare and disease resistance."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the three layers, (b) what reproduction technology does,
#  (c) what genomics changed, (d) what direct editing adds, and the constraint.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the three layers
    "Animal biotechnology operates in three layers that build on each other: "
    "reproductive technology multiplies the influence of chosen parents, "
    "genomic technology changes how those parents are chosen, and genetic "
    "technology alters the animal directly. "
    # (b) reproduction
    "Artificial insemination lets one bull sire tens of thousands of calves. "
    "Sexed semen, sorted by flow cytometry on the small DNA difference between "
    "X-bearing and Y-bearing sperm, biases the calf crop towards the productive "
    "sex. Superovulation with embryo transfer, and ovum pick-up with in vitro "
    "embryo production, do the same on the female side, where the biological "
    "ceiling is far lower. "
    # (c) genomics
    "Genomic selection, adopted by the dairy industry from 2009, estimates "
    "breeding values from tens of thousands of markers in a newborn calf rather "
    "than from the milk records of its adult daughters. That roughly halves the "
    "generation interval, and because genetic gain per year is inversely "
    "proportional to it, the annual rate of improvement nearly doubled. The "
    "statistics are the same as in `green.molecular_plant_breeding`; the "
    "biology is different only in generation time and reproductive rate. "
    # (d) direct alteration, and the constraint
    "Genetic technology alters the animal itself: somatic cell nuclear transfer "
    "produces a clone of an existing individual, and zygote editing produces "
    "defined changes such as knocking out the CD163 receptor that porcine "
    "reproductive and respiratory syndrome virus requires, or introducing the "
    "POLLED allele so cattle grow no horns. The binding constraint on that last "
    "layer is not technical. Editing a zygote is now routine; obtaining "
    "regulatory approval to sell the resulting animal, in most jurisdictions, "
    "is not."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Farmers have always bred from their best animals. The difference now is "
    "speed and precision. A DNA test on a newborn calf can predict how much "
    "milk its daughters will give, so that decision no longer waits five years. "
    "Embryos can be produced from the best cows and carried by other cows. And "
    "in a few cases a single gene can be changed: so that cattle are born "
    "without horns and never have to be painfully dehorned as calves, or so "
    "that pigs cannot catch a virus that otherwise kills millions of them every "
    "year. The animals themselves are ordinary animals. What changed is how "
    "much is known about them, and when."
)

# -----------------------------------------------------------------------------
#  The racehorse analogy. Its limit is stated and is the real one: a form
#  report is a prediction, and predicting well requires having seen animals
#  like this one before.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is the difference between judging a racehorse by watching it race for "
    "five seasons and reading a reliable form report on the day it is born. The "
    "animals are the same animals; the information arrives much earlier, so far "
    "fewer wrong turnings are taken. The comparison has a real limit. A form "
    "report is only as good as the races the scout has already seen, which is "
    "why these predictions work well within a well-recorded breed and poorly "
    "for an animal unlike anything in the reference population."
)

WHY_IT_MATTERS = (
    "Livestock account for a large share of agricultural greenhouse gas "
    "emissions and land use, and the fastest way to lower emissions per litre "
    "of milk or kilogram of meat is to raise output per animal and cut "
    "mortality. Disease resistance is the clearest case: a pig that cannot be "
    "infected needs no antibiotics, does not transmit, and does not die, which "
    "is simultaneously an economic, an animal welfare and an antimicrobial "
    "resistance argument. Hornless cattle avoid a painful procedure performed "
    "on millions of calves a year. The costs are equally concrete. Very "
    "intense selection through a small number of sires has narrowed the genetic "
    "base of the major dairy breeds to an effective population size that would "
    "concern a conservation biologist. Selecting hard for production has "
    "historically carried fertility, lameness and metabolic disease along with "
    "it, and correcting that took a deliberate change in how breeding goals are "
    "written. Somatic cell nuclear transfer remains inefficient and produces "
    "losses that are real regardless of one's position on cloning. And beneath "
    "all of it sits a question this record does not attempt to settle: these "
    "are sentient animals, some of these interventions reduce their suffering, "
    "some are indifferent to it, and public opinion distinguishes between them "
    "in ways the science does not."
)
