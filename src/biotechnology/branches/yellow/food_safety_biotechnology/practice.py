# =============================================================================
#  biotechnology.branches.yellow.food_safety_biotechnology.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by WHAT IS BEING LOOKED FOR, because the four
#  targets require different methods, answer to different regulations and fail
#  in different ways. A pathogen must be found before release; an allergen must
#  be quantified against a threshold; a toxin survives the process that killed
#  the organism; and an authenticity question is about a claim rather than a
#  hazard.
#
#  The authenticity group is placed alongside the others rather than as an
#  appendix, because the 2008 melamine adulteration killed infants and was
#  detected as a safety failure. Treating food fraud as a separate and lesser
#  subject is a mistake this facet declines to repeat.
#
#  ORGANISMS are the targets, as in `yellow.food_biopreservation`, and the note
#  on each says what makes it difficult rather than what it is.
#
#  A NOTE ON WHAT IS ABSENT. The methods themselves belong to
#  `red.molecular_diagnostics`. What is specific here is the matrix, the
#  sampling problem and the regulatory consequence of a result.
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
#  By what is being looked for. Authenticity sits alongside, not after.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- pathogens, where speed is the whole point ------------------------------
    "Rapid detection of Salmonella, Listeria monocytogenes, Campylobacter and "
    "Shiga toxin-producing Escherichia coli by nucleic acid amplification after "
    "short enrichment, returning a result while the batch is still on site",
    "Environmental monitoring of processing surfaces and drains, which finds "
    "the resident contamination that will eventually reach product and is more "
    "informative than testing the product itself",
    "Verification of kill steps and of hygiene controls as part of hazard "
    "analysis, which is what the results are actually used for",
    "Testing of ready-to-eat foods against the end-of-shelf-life criteria that "
    "`yellow.food_biopreservation` exists to meet",
    # -- outbreak tracing, which is the second transformation --------------------
    "Whole genome sequencing of clinical and food isolates to link cases that "
    "no other method connects, including small clusters spread across countries "
    "and across months",
    "Source attribution tracing a clinical isolate back to a production site, "
    "which converts an outbreak investigation from interviewing patients into "
    "matching genomes",
    "Routine sequencing of isolates by public health laboratories, which "
    "detects outbreaks nobody had noticed were outbreaks",
    # -- toxins, which survive what kills the organism -----------------------------
    "Mycotoxin measurement in cereals, nuts, spices and dried fruit, where the "
    "toxin persists long after the fungus that produced it has gone",
    "Marine biotoxin monitoring in shellfish, which is a public health "
    "surveillance programme rather than a product test and which closes "
    "harvesting areas",
    "Detection of heat-stable bacterial toxins, which survive cooking and are "
    "therefore not addressed by any kill step",
    # -- allergens, where the answer is a number against a threshold ---------------
    "Quantification of milk, egg, peanut, tree nut, gluten and other regulated "
    "allergens in product and on cleaned equipment",
    "Cleaning validation between production runs, which is where allergen "
    "control is actually exercised and where a precautionary label is either "
    "justified or avoided",
    "Gluten-free verification against the defined threshold, which is one of "
    "the few allergen claims with a numerical legal definition",
    # -- authenticity, which is not a lesser subject -------------------------------
    "Species identification in meat and fish products, which detects "
    "substitution that is economic in motive and can be a safety and a "
    "religious dietary matter in effect",
    "Geographical origin determination by stable isotope and elemental "
    "profiling, which supports protected designations and detects "
    "misdeclaration",
    "Detection of adulteration in high-value commodities including honey, olive "
    "oil, spices and infant formula, the last of which is where adulteration "
    "has killed",
    "Verification of organic, halal, kosher and free-from claims, where the "
    "declaration is unverifiable by inspection alone",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by where the sample is when the answer arrives, which is the
#  record's organising idea.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- getting a usable sample, which is the actual bottleneck ---------------
    "Statistically designed sampling plans, which determine what a negative "
    "result means and which no analytical improvement substitutes for",
    "Enrichment culture before molecular detection, still necessary because "
    "even sensitive methods require enough target and because it also "
    "distinguishes viable organisms from residual nucleic acid",
    "Sample preparation from difficult matrices, since fat, protein and "
    "polyphenols inhibit amplification and food is an unhelpful matrix in ways "
    "a clinical sample is not",
    # ---- the laboratory ---------------------------------------------------------
    "Real-time and digital PCR for pathogen detection and quantification",
    "Immunoassay formats including ELISA and lateral flow for toxins and "
    "allergens",
    "Mass spectrometry for mycotoxins, allergen peptides and adulterants, which "
    "is the reference method where an immunoassay result is disputed",
    "Whole genome sequencing and core genome multilocus typing for isolate "
    "comparison, which is what makes outbreak linkage possible",
    "Metagenomic and 16S profiling of production environments",
    # ---- moving the answer to where the food is --------------------------------
    "Isothermal amplification methods that need no thermal cycler and therefore "
    "no laboratory",
    "Portable sequencing for on-site typing, which shortens the interval "
    "between a result and a decision",
    "Biosensors and lateral flow devices usable by a production operator rather "
    "than an analyst",
    "Freeze-dried cell-free sensors from `white.cell_free_biomanufacturing`, "
    "which put a specific molecular test where there is no laboratory at all",
    # ---- knowing what the result means -------------------------------------------
    "Reference databases and cluster definitions for genomic comparison, "
    "without which a sequence difference cannot be called a match",
    "Blockchain and digital traceability systems, which record where a "
    "consignment went and are only as good as the data entered into them",
    "Predictive modelling linking a detection to a risk decision, since a "
    "positive result requires a proportionate response rather than an automatic "
    "one",
)


# =============================================================================
#  ORGANISMS
#  The targets, and what makes each difficult.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "listeria_monocytogenes",  # grows cold, contaminates after cooking, high fatality
    "salmonella_enterica",  # very low infectious dose in some foods, many serovars
    "campylobacter_jejuni",  # the commonest cause, fragile, and hard to culture
    "escherichia_coli",  # the Shiga toxin producers, where the toxin is the hazard
    "aspergillus_flavus",  # produces aflatoxin, which outlasts the fungus entirely
    "norovirus",  # a major cause, not culturable routinely, detected only molecularly
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "pcr",
    "next_generation_sequencing",
    "immunoassay",
    "mass_spectrometry",
    "isothermal_amplification",
    "cell_culture",
    "bioinformatics",
    "isotope_ratio_analysis",
)


# =============================================================================
#  CHALLENGES
#  Sampling first, because no analytical advance addresses it.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the constraint that method improvement cannot touch --------------------
    "Sampling, since a pathogen is distributed unevenly through a batch and a "
    "negative result on a few hundred grams says far less about a consignment "
    "than the precision of the method implies, which is a statistical limit "
    "rather than an analytical one",
    "Low prevalence combined with severe consequence, which means the tests "
    "that matter most are the ones almost always negative, and a system judged "
    "on its negatives is hard to keep sharp",
    # -- what a molecular positive actually means ---------------------------------
    "Detection of nucleic acid rather than viable organisms, so a positive after "
    "a kill step may reflect dead cells and cause avoidable product loss",
    "Matrix inhibition, since fat, protein and polyphenols interfere with "
    "amplification and food is a far less cooperative sample than blood",
    "Interpretation of a genomic cluster, since sequences that are close are "
    "not necessarily epidemiologically linked and a difference threshold is a "
    "convention rather than a fact",
    # -- what happens after a positive ---------------------------------------------
    "Proportionate response to a detection, where the alternatives are an "
    "expensive recall and an unacceptable risk and the evidence is frequently "
    "incomplete",
    "Public health capacity to act on clusters that surveillance now detects "
    "faster than investigators can follow, which turns a laboratory advance "
    "into a resourcing problem",
    # -- who can afford to test ------------------------------------------------------
    "Very uneven distribution of testing capacity, so the countries exporting "
    "food are frequently not those able to test it, and a system relying on "
    "importing-country testing pushes cost and risk in a direction that is not "
    "obviously fair",
    "Cost per test at the frequency that meaningful sampling requires, which "
    "is a constraint on small producers rather than on large ones",
    # -- the targets that resist -------------------------------------------------------
    "Viruses including norovirus, which cause a large share of foodborne "
    "illness, cannot be cultured routinely, and are therefore detected only as "
    "nucleic acid with all the viability ambiguity that carries",
    "Allergen quantification variability between methods, since immunoassays "
    "respond differently to processed proteins and a result depends on the kit "
    "as well as on the food",
    "Adulterants designed to defeat the test, as melamine was chosen "
    "specifically to raise apparent protein content, which makes authenticity "
    "testing an adversarial rather than an analytical problem",
)
