# =============================================================================
#  biotechnology.branches.grey.environmental_biomonitoring.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  EVERY OTHER RECORD IN THIS BRANCH CHANGES SOMETHING. THIS ONE FINDS OUT
#  WHETHER ANYTHING CHANGED.
#
#  It is the branch's instrument, and without it the rest of grey biotechnology
#  is a set of claims. Monitored natural attenuation is approved on the
#  strength of evidence produced here. A discharge consent is enforced on
#  numbers produced here. A remediation is signed off here.
#
#  THE CENTRAL IDEA IS THAT A CHEMICAL MEASUREMENT ANSWERS A DIFFERENT QUESTION
#  FROM A BIOLOGICAL ONE, AND BOTH QUESTIONS MATTER.
#
#      CHEMISTRY   what was present in this water, at this point, at the
#                  moment the bottle was filled
#      BIOLOGY     what the organisms living there have been exposed to since
#                  the last time anything killed them
#
#  A river receiving an illegal discharge at three in the morning shows nothing
#  in a sample taken at noon and shows a collapsed invertebrate community for
#  months. That is not a shortcoming of chemistry; it is the difference between
#  measuring a concentration and measuring an effect, and a monitoring
#  programme that does only one of them is answering half the question.
#
#  THE SECOND THING TO ESTABLISH IS WHAT ENVIRONMENTAL DNA DID AND DID NOT
#  CHANGE. It made it possible to survey what lives in a river by filtering
#  water instead of catching anything, which is a genuine transformation of
#  scale, cost and harm. It also detects material from an organism that was
#  present rather than one that is there now, it does not count individuals,
#  and it cannot tell whether they were breeding. Those limits are structural.
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
    "Using organisms and their traces to measure environmental condition, "
    "which records exposure over time where a chemical sample records a "
    "concentration at an instant."
)

# -----------------------------------------------------------------------------
#  Structure: (a) why biology is measured at all, (b) the four approaches,
#  (c) what environmental DNA changed and what it did not, (d) the reference
#  problem, which is the field's deepest difficulty.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the argument for measuring organisms rather than substances
    "Environmental biomonitoring uses living organisms, and increasingly their "
    "genetic traces, to assess the condition of water, soil, sediment and air. "
    "Its justification is that it answers a question chemistry cannot. A water "
    "sample records what was present at one point at one moment; the community "
    "living in that water records what it has been exposed to continuously "
    "since whatever last disturbed it. An intermittent discharge, a pesticide "
    "pulse after rain, or a mixture whose components are individually below "
    "their limits will be invisible to a sampling programme and visible in the "
    "invertebrates. Biology also integrates interactions that no list of "
    "concentrations captures, and it measures the thing that is actually "
    "valued, which is whether the ecosystem is functioning rather than whether "
    "a number was exceeded. "
    # (b) the four approaches
    "Four approaches are used and they answer different questions. Indicator "
    "and index methods score the community present against what would be "
    "expected, using groups whose tolerances are well characterised, and this "
    "is what most regulatory assessment of rivers consists of. Bioaccumulation "
    "monitoring measures contaminant concentrations in the tissue of organisms "
    "that concentrate them from the surrounding medium, which is how "
    "persistent substances at undetectable ambient concentrations are found. "
    "Biomarker and biosensor methods measure a physiological or molecular "
    "response, from enzyme induction in a fish to an engineered bacterium that "
    "produces a signal in the presence of a specific compound. And molecular "
    "survey methods identify what is present from genetic material, either "
    "from the organisms themselves or from the traces they shed. "
    # (c) environmental DNA, honestly
    "Environmental DNA is the development that changed the field's economics. "
    "Every organism sheds cells, mucus and waste, so a filtered water sample "
    "contains genetic material from much of what lives upstream, and "
    "sequencing it produces a species list without catching, handling or "
    "killing anything. It detects rare and cryptic species that netting misses "
    "and it detects invasive species early, which is where its practical value "
    "is greatest. Its limits are structural rather than technical. It reports "
    "that material was present, which is not the same as an organism being "
    "there now, since DNA travels downstream and persists for a period after "
    "the organism has gone. Read counts do not translate reliably into "
    "abundance, so it does not replace a census. It says nothing about age, "
    "condition or whether a population is breeding. And it is entirely "
    "dependent on reference sequence databases, so a species with no reference "
    "entry is invisible no matter how much of its DNA is in the sample. "
    # (d) the reference problem
    "That last point generalises into the field's deepest difficulty and it "
    "applies to the traditional methods as well. Every assessment is a "
    "comparison against an expectation, and the expectation has to come from "
    "somewhere. Reference sites are chosen as the least disturbed available "
    "rather than the undisturbed, because in most regions undisturbed sites do "
    "not exist. Historical baselines are patchy and were collected for other "
    "purposes. So a system judged in good condition is being compared against "
    "a standard set after most of the change had already occurred, and each "
    "generation of assessors calibrates against the world it inherited."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Instead of testing water for chemicals, you can look at what is living in "
    "it. This works because a bottle of water only tells you about the moment "
    "it was filled, while the creatures in a river have been sitting in it the "
    "whole time. If somebody dumped something at three in the morning, the "
    "water sample at noon shows nothing and the missing insects show it for "
    "months. Some species can only survive in clean water, so counting which "
    "ones are present grades the river. A newer method is remarkable: every "
    "animal sheds skin cells and waste, so you can filter a bucket of river "
    "water, read the DNA in it, and get a list of what lives upstream without "
    "catching anything at all. It finds rare and hidden species and spots "
    "invaders early. It cannot tell you how many there are, whether they are "
    "breeding, or whether they are still there rather than having passed "
    "through last week."
)

# -----------------------------------------------------------------------------
#  The two analogies map exactly onto the record's two central ideas: the
#  snapshot against the record, and the trace against the sighting.
# -----------------------------------------------------------------------------
ANALOGY = (
    "A chemical sample is a photograph and a biological survey is a diary. The "
    "photograph is exact about one instant and silent about the night before; "
    "the diary is vaguer about any particular hour and tells you how the month "
    "went. Environmental DNA is a third thing again: footprints rather than a "
    "sighting. They prove something passed, they do not prove it is still "
    "there, and they will not tell you how many walked or whether any of them "
    "stayed."
)

WHY_IT_MATTERS = (
    "This is the record that makes the rest of the branch accountable. "
    "Monitored natural attenuation is only defensible because degradation can "
    "be demonstrated rather than asserted. Discharge consents are enforceable "
    "because the receiving water is assessed. A remediation is signed off "
    "against measurements. Remove this record and grey biotechnology becomes a "
    "set of claims about invisible processes. "
    "The practical gains are real. Biological indices detect intermittent and "
    "mixture effects that no realistic sampling programme catches. "
    "Bioaccumulation monitoring finds persistent substances at ambient "
    "concentrations below detection. Environmental DNA has reduced the cost and "
    "the harm of surveying: a filtered water sample replaces netting, "
    "trapping and electrofishing, which means more sites can be covered, more "
    "often, without killing the animals being counted, and it detects invasive "
    "species early enough for a response to be possible. "
    "The limits deserve equal prominence. A biological index tells you "
    "something is wrong and rarely what, so it complements chemistry rather "
    "than replacing it. Environmental DNA reports presence of material rather "
    "than presence of an organism, gives no reliable abundance, and is blind "
    "to any species absent from a reference database, which biases results "
    "toward well-studied regions and well-studied taxa. Taxonomic expertise "
    "for traditional identification is declining faster than molecular methods "
    "are replacing it, and the reference databases those methods depend on "
    "were built by the same expertise. Long-term monitoring programmes are "
    "cut first in a budget round and their value is entirely in their "
    "continuity, so a five-year gap devalues thirty years of prior data. And "
    "shifting baselines are the quiet structural problem: each assessment "
    "generation calibrates against the least disturbed sites available to it, "
    "so systems can be certified as in good condition while the standard "
    "itself moves."
)
