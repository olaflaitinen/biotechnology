# =============================================================================
#  biotechnology.branches.yellow.food_safety_biotechnology.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The change this record documents is not a better test. It is a change in
#  WHEN THE ANSWER ARRIVES, and that is what converted food safety from an
#  investigation into a control.
#
#      culture-based    two to five days for a result. A chilled product with a
#                       ten-day shelf life has been eaten before the laboratory
#                       reports, so the test tells you what went wrong.
#      molecular        hours. The result arrives while the batch is still on
#                       the site, so the test tells you what to do.
#
#  Nothing about the pathogen changed. The interval did, and the interval is
#  the whole subject.
#
#  A SECOND THEME RUNS THROUGH THE RECORD AND IS EASY TO MISS: much of what is
#  called food safety work is actually FOOD FRAUD work. Species substitution,
#  origin misdeclaration and adulteration are economic crimes rather than
#  hygiene failures, they are detected by the same molecular methods, and one
#  of them, the 2008 melamine adulteration, killed infants. Authenticity and
#  safety are not separable in practice.
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
    "Molecular detection of pathogens, toxins, allergens and adulteration in "
    "food, and the genomic tracing of outbreaks to their source."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the timing change and why it matters, (b) what is detected,
#  (c) genomic epidemiology, which is the second transformation, (d) the
#  constraints, which are sampling and interpretation rather than sensitivity.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the timing change
    "Food safety biotechnology applies molecular and immunological methods to "
    "determining what is in food and where it came from. Its defining "
    "achievement is not sensitivity but speed. Culture-based detection requires "
    "an organism to grow, which takes days, and for a chilled product with a "
    "short shelf life the result arrives after the food has been eaten. "
    "Molecular detection returns an answer in hours, while the batch is still "
    "under the producer's control. That single change converted testing from a "
    "record of what happened into a decision about what to release, and "
    "everything else in this record follows from it. "
    # (b) what is detected
    "Four things are looked for. Pathogens, chiefly Salmonella, Listeria "
    "monocytogenes, Campylobacter and Shiga toxin-producing Escherichia coli, "
    "are detected by nucleic acid amplification after a short enrichment, "
    "since even molecular methods need enough target to find. Toxins including "
    "mycotoxins, marine biotoxins and bacterial toxins are measured by "
    "immunoassay and mass spectrometry, and matter because a toxin survives the "
    "heat that kills the organism producing it. Allergens are quantified by "
    "immunoassay and increasingly by mass spectrometry, and their control is a "
    "labelling and cleaning problem as much as a detection one. Authenticity "
    "testing determines whether a food is what it claims to be, by species, by "
    "origin and by composition. "
    # (c) genomic epidemiology
    "Whole genome sequencing produced the second transformation. Comparing "
    "isolates at single-nucleotide resolution links cases separated by time and "
    "geography that no previous method could connect, which turned outbreak "
    "investigation from a matter of interviewing patients about what they ate "
    "into a matter of matching genomes between a clinical case and a food "
    "sample. Routine sequencing of isolates by public health laboratories "
    "detects clusters that were previously invisible, including small outbreaks "
    "spread across countries. "
    # (d) the constraints
    "The constraints are not analytical. Sampling dominates: a pathogen is "
    "distributed unevenly through a batch, so a negative result on a few "
    "hundred grams says less about a lorry-load than the precision of the "
    "method suggests. Molecular methods detect nucleic acid rather than viable "
    "organisms, so a positive may reflect a dead cell, which matters after a "
    "kill step. And the sensitivity of genomic surveillance creates its own "
    "problem: a cluster of three cases in three countries is now detectable and "
    "must be interpreted, which is a demand on epidemiological judgement rather "
    "than on laboratory capacity."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "This is testing food to find out whether it contains something dangerous, "
    "and working out where a contaminated batch came from. The important change "
    "was not that the tests got better at finding things. It was that they got "
    "faster. The old method meant growing bacteria in a laboratory, which takes "
    "days, by which time a fresh product has already been sold and eaten. The "
    "new methods give an answer in hours, while the food is still in the "
    "factory, so a problem can be stopped instead of investigated. The same "
    "techniques also show whether food is what it claims to be, which turns out "
    "to matter for safety as well as for honesty."
)

# -----------------------------------------------------------------------------
#  The smoke alarm analogy. Chosen because the record's point is timing rather
#  than capability, and because its stated limit carries the sampling problem,
#  which is the field's actual constraint.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is the difference between a smoke alarm and a fire report. Both tell "
    "you a fire happened; only one tells you while you can still do something. "
    "The comparison understates one difficulty. A smoke alarm sits in the room "
    "with the smoke, and a food test examines a few hundred grams taken from a "
    "consignment of many tonnes, so a clear result means the sample was clean "
    "rather than the lorry."
)

WHY_IT_MATTERS = (
    "Foodborne illness affects a very large number of people every year and "
    "kills a substantial number of them, most of whom are children, elderly or "
    "immunocompromised. Rapid detection stops contaminated product before it "
    "ships, which prevents illness rather than documenting it. Genomic "
    "surveillance has repeatedly identified outbreaks that no one had noticed "
    "were outbreaks, because the cases were few, far apart and separately "
    "unremarkable, and linking them located contaminated sites that would "
    "otherwise have continued producing. Allergen detection is what makes a "
    "may-contain declaration something other than a guess, and for a person "
    "with a severe allergy the difference is not academic. Authenticity testing "
    "addresses a category of harm that food safety frameworks were not designed "
    "for, and the 2008 melamine adulteration, which killed infants and injured "
    "many thousands, was an economic crime detected as a safety failure. The "
    "costs are worth stating precisely. Sampling remains the weak point and no "
    "improvement in analytical sensitivity addresses it. Molecular methods "
    "detect nucleic acid rather than live organisms, which produces positives "
    "that mean nothing after a kill step and consequent product loss. Testing "
    "capacity is very unevenly distributed, so the countries exporting food are "
    "frequently not the ones able to test it, and a system that relies on "
    "importing-country testing pushes cost and risk in a direction that is "
    "not obviously fair. And genomic surveillance identifies clusters faster "
    "than public health systems can always act on them, which converts a "
    "laboratory advance into a resourcing problem."
)
