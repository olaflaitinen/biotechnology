# =============================================================================
#  biotechnology.branches.grey.biodiversity_conservation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE HARDEST THING TO GET RIGHT IN THIS RECORD IS THE RELATIONSHIP BETWEEN
#  WHAT THE TECHNOLOGY CAN DO AND WHAT THE PROBLEM ACTUALLY IS.
#
#      SPECIES ARE LOST BECAUSE HABITAT IS DESTROYED.
#      NO BIOTECHNOLOGY ADDRESSES HABITAT DESTRUCTION.
#
#  Everything in this record is downstream of that. Biobanking, assisted
#  reproduction, genetic rescue and genome sequencing are genuinely useful and
#  they operate on populations that are already small because their habitat is
#  already gone. A record that presented them as a solution to biodiversity
#  loss would be describing a different problem from the one that exists.
#
#  THIS IS NOT A REASON TO DISMISS THE FIELD, AND THE RECORD DOES NOT. Genetic
#  rescue has demonstrably recovered populations from inbreeding depression.
#  Sequencing has revealed that some conservation units were wrongly defined,
#  which changed what was protected. Environmental DNA has made surveying
#  affordable. Biobanks preserve options that would otherwise close
#  permanently. These are real contributions to a problem that biotechnology
#  did not create and cannot solve alone.
#
#  THE SECOND THING THIS RECORD MUST HANDLE CAREFULLY IS DE-EXTINCTION, WHICH
#  RECEIVES ATTENTION OUT OF ALL PROPORTION TO ITS CONTRIBUTION.
#
#  No extinct species has been restored. What is technically conceivable is an
#  engineered proxy: an existing species edited to carry some traits of a lost
#  one. The serious objection is not technical. It is that a credible promise
#  of reversal weakens the case for prevention, and conservation biologists
#  have made that argument themselves rather than having it made about them.
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
    "Applying genetic and reproductive technologies to conserving species, "
    "which manages the consequences of habitat loss rather than its cause."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the framing, stated first because everything depends on it,
#  (b) what the tools actually do, (c) genetic rescue, which is the clearest
#  success and carries a real risk, (d) de-extinction, in proportion.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the framing
    "Conservation biotechnology applies genetic, reproductive and molecular "
    "methods to the preservation of species and populations. Its position has "
    "to be stated before its content: species are lost principally because "
    "habitat is destroyed, fragmented and degraded, and no technology in this "
    "record addresses that. What these methods do is manage the consequences. "
    "They work on populations that are already small, already isolated and "
    "already losing genetic variation, and they are useful precisely because "
    "such populations are now common. Treating them as a response to "
    "biodiversity loss rather than as a response to its aftermath misstates "
    "both what they achieve and what the problem is. "
    # (b) what the tools do
    "Four capabilities do most of the work. Population genomics establishes "
    "how much variation remains, how populations are related, and where the "
    "barriers between them lie, which has repeatedly shown that conservation "
    "units were defined wrongly and that resources were being spent "
    "protecting a boundary that did not exist. Molecular survey, principally "
    "environmental DNA, makes it possible to establish presence and "
    "distribution without capture, which is treated in "
    "`grey.environmental_biomonitoring` and has transformed what a survey "
    "costs. Biobanking preserves gametes, embryos, tissue and cell lines "
    "against a future in which the living material is gone, which is the only "
    "intervention here that cannot be repeated later if it is not done now. "
    "And assisted reproduction, including artificial insemination and embryo "
    "transfer, moves genetic material between animals that cannot or will not "
    "breed with each other, which matters most for species held in small "
    "numbers across distant institutions. "
    # (c) genetic rescue, the clearest success and its risk
    "Genetic rescue is the field's clearest demonstrated success and it is "
    "also where the field is least comfortable. Introducing individuals from "
    "another population into one suffering inbreeding depression has produced "
    "measurable recovery in fitness and population size in documented cases. "
    "The reservation is genuine: the introduced animals bring genes adapted to "
    "somewhere else, and the resulting population is no longer the one that "
    "was there. Where the two populations are sufficiently different the cross "
    "can perform worse than either parent, and deciding when the risk of doing "
    "nothing exceeds the risk of intervening is a judgement about which "
    "population is worth preserving rather than a calculation. "
    # (d) de-extinction, kept in proportion
    "De-extinction occupies a share of public attention that its contribution "
    "does not support. No extinct species has been restored, and what is "
    "conceivable is an engineered proxy: an existing species altered to carry "
    "traits of a lost one, released into an ecosystem that has changed since "
    "the original disappeared. The most serious objection is not technical. It "
    "is that a credible promise of reversal reduces the perceived cost of "
    "loss, and it has been made most forcefully by conservation biologists "
    "concerned that their own field's funding and political case rests on "
    "extinction being permanent."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Species are disappearing mainly because the places they live are being "
    "destroyed, and no laboratory technique fixes that. What these techniques "
    "can do is help the populations that are already too small. Reading an "
    "animal's DNA shows how much variation is left and whether two groups "
    "thought to be separate species really are, which has changed what gets "
    "protected. Frozen stores of eggs, sperm and cells keep options open for "
    "later. Moving a few animals from one population into another that has "
    "become inbred has genuinely revived populations that were failing, though "
    "it makes them slightly different from what was there before. Bringing "
    "extinct animals back is not something anyone has done; what might be "
    "possible is editing a living species to resemble a lost one. The "
    "strongest argument against it comes from conservationists themselves, who "
    "point out that if people believe extinction can be undone, they will care "
    "less about preventing it."
)

# -----------------------------------------------------------------------------
#  The library analogy carries the two things the record needs: that these
#  tools preserve and repair rather than create, and that the loss they
#  address is a loss of the building rather than of individual volumes.
# -----------------------------------------------------------------------------
ANALOGY = (
    "These are the techniques of a conservation workshop in a library: "
    "repairing damaged bindings, copying fragile pages, cataloguing what "
    "survives and keeping a duplicate somewhere safe. All of it is skilled and "
    "necessary work. None of it addresses the fact that the building is being "
    "demolished around them, and a workshop that let anyone believe otherwise "
    "would be doing harm along with its good."
)

WHY_IT_MATTERS = (
    "Extinction is irreversible, which is what distinguishes this record from "
    "every other in the branch: a contaminated aquifer can be treated in "
    "twenty years, and a lost species cannot be recovered in any. That makes "
    "the interventions here worth doing even where their reach is modest. "
    "Genetic rescue has documented recoveries behind it. Genomic analysis has "
    "redirected conservation effort by showing that units were wrongly "
    "defined, which is a cheap intervention with a large effect. Biobanking is "
    "the one action in this record that cannot be deferred, since material not "
    "collected while a population exists cannot be collected afterwards. "
    "Environmental DNA has reduced the cost and the harm of finding out what "
    "is still present. "
    "The limits are structural and should not be softened. Habitat loss, "
    "fragmentation, invasive species, overexploitation and climate change "
    "drive extinction, and nothing in this record touches any of them. The "
    "methods are expensive per species and are applied overwhelmingly to large "
    "vertebrates that attract funding, while most biodiversity is invertebrate, "
    "fungal and microbial and most of it has never been described. Assisted "
    "reproduction has succeeded in a small number of species and fails in most "
    "because the reproductive biology is unknown. Biobanks depend on "
    "institutional continuity measured in centuries and on funding measured in "
    "grant cycles. Genetic rescue changes the population it saves. Reference "
    "databases and expertise are concentrated in wealthy countries while "
    "biodiversity is concentrated elsewhere, and the resulting flow of genetic "
    "material out of species-rich countries is the reason access and benefit "
    "sharing law exists and is taken seriously. And the deepest problem is one "
    "of attention rather than of technique: work that photographs well "
    "attracts support disproportionately, and a promise that extinction might "
    "be reversible is the most photogenic thing in the field."
)
