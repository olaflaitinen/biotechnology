# =============================================================================
#  biotechnology.branches.red.molecular_diagnostics.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Almost every public misunderstanding of testing is a misunderstanding of one
#  thing: that a test which is right ninety-nine times out of a hundred can
#  still be wrong most of the times it says yes, when the thing being looked
#  for is rare. That is not a flaw in the test; it is arithmetic.
#
#  The public register below therefore does two things most descriptions of
#  diagnostics do not. It explains amplification before it explains accuracy,
#  because a reader who thinks a test simply looks at a sample will not
#  understand contamination. And WHY_IT_MATTERS states the prevalence problem
#  explicitly rather than leaving it to `metrics.py`, because it is the single
#  fact a non-specialist most needs and least often gets.
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
    "Detecting disease, pathogens and genetic variation by reading nucleic "
    "acids and proteins rather than by culture or morphology."
)

# -----------------------------------------------------------------------------
#  Structure: (a) definition, (b) the amplification family, (c) the sequencing
#  family, (d) the binding constraint.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) definition
    "Molecular diagnostics identifies a specific nucleic acid or protein "
    "sequence in a clinical specimen, rather than inferring it from how an "
    "organism grows or how a cell looks. "
    # (b) amplification
    "Nucleic-acid amplification, of which the polymerase chain reaction is the "
    "archetype, doubles a target region each cycle so that a handful of "
    "starting copies becomes a detectable signal within about forty cycles. "
    "Quantitative PCR reads fluorescence in real time and reports a "
    "quantification cycle that is inversely proportional to the logarithm of "
    "the starting copy number. Digital PCR partitions the reaction into "
    "thousands of droplets and counts positives against a Poisson model, giving "
    "absolute quantification without a standard curve. Isothermal methods such "
    "as loop-mediated amplification remove the need for thermal cycling and "
    "therefore for laboratory hardware. "
    # (c) sequencing
    "Sequencing-based diagnostics moves from asking about one target to reading "
    "many: targeted panels for oncology, exome and genome sequencing for rare "
    "disease, and untargeted metagenomics for infection of unknown cause. "
    "CRISPR-based detection couples a programmable nuclease to a reporter and "
    "has pushed instrument-free sensitivity into the attomolar range. "
    # (d) the binding constraint
    "The binding constraint is interpretation, not detection. Modern assays "
    "find things reliably; deciding whether a detected sequence explains a "
    "patient's illness, or is colonisation, contamination or an incidental "
    "variant of unknown consequence, is where the difficulty now sits."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Every living thing, including every germ, carries its own genetic text. A "
    "molecular test looks for one specific sentence from that text in a swab, a "
    "drop of blood or a sample of saliva. Because there is usually far too "
    "little to see, the machine first makes millions of copies of that sentence "
    "if it is present, and then detects the copies. If nothing was there to "
    "copy, nothing appears. That copying is what makes these tests so sensitive, "
    "and it is also why a laboratory has to be scrupulous: a single stray "
    "fragment from a previous sample would be copied just as faithfully."
)

# -----------------------------------------------------------------------------
#  The library analogy. Its limit is deliberately visible: a photocopier does
#  not care whether the sentence it copied was the one you were looking for or
#  a near-identical one, which is exactly the specificity problem.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is a search-and-photocopy operation. You suspect one particular "
    "sentence is hidden somewhere in a library. Rather than reading every book, "
    "you use a machine that finds that exact sentence and photocopies it over "
    "and over until the stack is tall enough to see from the door. No sentence, "
    "no stack. The weakness of the comparison is the useful part: the machine "
    "cannot tell a sentence from one that is almost identical, which is why a "
    "test designed for one virus can sometimes be fooled by its close relative."
)

WHY_IT_MATTERS = (
    "Culture-based microbiology takes one to five days; a molecular test takes "
    "one to four hours. That difference decides whether a patient with sepsis "
    "gets the right antibiotic on day zero or on day three. In cancer care the "
    "same technology decides which targeted therapy a tumour will respond to, "
    "turning a statistical guess into a match. In an outbreak it is the only "
    "thing that can say what is spreading while there is still time to act. "
    "The cost is a kind of certainty these tests cannot deliver and are "
    "routinely assumed to: when a disease is rare, most positive results from "
    "even a very accurate test are false, because there are so many more "
    "healthy people to be wrong about. Screening a whole population with a "
    "good test can therefore cause more anxiety and more unnecessary follow-up "
    "than it prevents illness, which is why screening programmes are argued "
    "about rather than simply rolled out."
)
