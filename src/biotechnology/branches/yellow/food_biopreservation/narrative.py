# =============================================================================
#  biotechnology.branches.yellow.food_biopreservation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record separates from `yellow.food_fermentation` on intent, and the
#  distinction is real rather than administrative.
#
#      food_fermentation      the microbes TRANSFORM the food. Preservation is
#                             one of four things happening, and the product is
#                             different from what went in.
#      food_biopreservation   the microbes or their products PROTECT the food
#                             and are meant to change nothing else. A
#                             biopreserved ham is still a ham.
#
#  That is why a bacteriocin can be added to a food that is not fermented at
#  all, and why the performance requirement here is that nothing perceptible
#  happens except that the food lasts longer.
#
#  THE FIELD'S DEFINING PROBLEM IS THE HURDLE. No biopreservative is
#  sufficient alone. Nisin does not touch Gram-negative bacteria, protective
#  cultures need time and temperature, and bacteriophage products act on one
#  species. Each is a partial barrier, and they work because several partial
#  barriers combine into one that pathogens cannot cross. A record that
#  presented any of them as a replacement for refrigeration or for a kill step
#  would be describing a marketing claim rather than a practice.
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
    "Using microorganisms, their antimicrobial products and bacteriophages to "
    "extend shelf life and control pathogens without changing the food."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what it is and how it differs from fermentation, (b) the four
#  approaches, (c) why hurdle technology is the correct frame, (d) the
#  constraints, which include resistance.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the distinction
    "Food biopreservation controls spoilage and pathogens using biological "
    "agents rather than heat, chemical preservatives or irradiation. It is "
    "distinguished from fermentation by intent: a fermented food is "
    "deliberately transformed, whereas a biopreserved food is meant to be "
    "unchanged except in how long it lasts. That requirement is strict. A "
    "protective culture that acidifies a product perceptibly has failed even if "
    "the product is safe, which is why the organisms used are selected for "
    "producing antimicrobials without producing flavour. "
    # (b) the four approaches
    "Four approaches are used. Protective cultures are live organisms added to "
    "outcompete spoilage and pathogenic species by consuming nutrients, "
    "occupying surfaces and producing inhibitors. Bacteriocins are ribosomally "
    "synthesised antimicrobial peptides, of which nisin is the oldest and most "
    "widely permitted, added as purified preparations or produced in situ by a "
    "culture. Bacteriophages are viruses that infect one bacterial species and "
    "leave everything else untouched, which is both their advantage and their "
    "limitation. And antimicrobial enzymes, chiefly lysozyme and the "
    "lactoperoxidase system, act on bacterial structures directly. "
    # (c) the hurdle frame
    "None of these is sufficient alone, and treating any of them as a "
    "standalone preservative misdescribes the field. Nisin is highly effective "
    "against Gram-positive organisms including Listeria and Clostridium, and "
    "has essentially no effect on Gram-negative bacteria because their outer "
    "membrane excludes it. Protective cultures need time and a temperature at "
    "which they are active. Phage products act on a single species and select "
    "for resistance. Each is a partial barrier, and biopreservation works "
    "because several partial barriers combine with pH, water activity, salt, "
    "chilling and packaging into a hurdle set that no organism crosses. "
    # (d) the constraints
    "The constraints follow from that. Efficacy is matrix-dependent, because a "
    "peptide binds to fat and protein and a culture behaves differently in a "
    "solid than in a liquid, so a result in broth predicts little about a "
    "sausage. Resistance develops to bacteriocins and to phages, and the "
    "field's honest position is that these are antimicrobials subject to the "
    "same evolutionary pressure as any other. Regulatory status differs "
    "sharply between jurisdictions and between agents, with nisin permitted for "
    "decades and phage preparations treated variously as processing aids, "
    "additives or neither. And the clean label appeal that drives commercial "
    "interest is in tension with the fact that several of these agents are, in "
    "regulatory terms, additives that must be declared."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "This is using harmless microbes, or the substances they make, to stop "
    "food going off or making people ill. It is different from fermentation, "
    "where the microbes deliberately change the food into something else: here "
    "the aim is that nothing noticeable happens except that the food keeps for "
    "longer. Some of these agents are very old, and one has been permitted in "
    "food for over sixty years. None of them works on its own. They are one "
    "barrier among several, alongside keeping food cold, salty or acidic, and "
    "it is the combination that stops bacteria rather than any single part of "
    "it."
)

# -----------------------------------------------------------------------------
#  The locks analogy. Chosen because hurdle technology is the record's central
#  idea and is genuinely hard to convey otherwise, and because its stated limit
#  carries the resistance problem: locks do not adapt and bacteria do.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is fitting several ordinary locks rather than one exceptional one. No "
    "single one would stop a determined intruder, and the combination does, "
    "because getting past all of them at once is a different problem from "
    "getting past any of them. The comparison has one important flaw. A lock "
    "stays as good as it was; a bacterium that meets the same barrier "
    "repeatedly can adapt to it, which is why resistance appears in this record "
    "and not in a locksmith's catalogue."
)

WHY_IT_MATTERS = (
    "Roughly a third of food produced is lost or wasted, and a substantial part "
    "of that is spoilage. Extending shelf life is therefore a resource measure "
    "as much as a commercial one, and it is one of the few interventions that "
    "reduces waste without asking anyone to change their behaviour. "
    "Biopreservation also addresses a specific and serious risk: Listeria "
    "monocytogenes grows at refrigeration temperature, contaminates "
    "ready-to-eat foods after cooking rather than before, and kills a "
    "significant proportion of those it makes seriously ill. Nisin and "
    "protective cultures are among the few tools that act on it in the finished "
    "product. The approach also lets manufacturers reduce nitrite in cured meat "
    "and chemical preservatives elsewhere, which is a genuine improvement and "
    "the reason commercial interest exists. The limits are real. These agents "
    "are narrow: nisin does nothing to Gram-negative organisms, and a phage "
    "preparation acts on one species while a food may carry several. Efficacy "
    "in a laboratory medium predicts efficacy in a food poorly, because fat and "
    "protein bind peptides and a solid matrix restricts diffusion. Resistance "
    "develops, and the field has been slower than it should be to say so "
    "plainly. And the clean label positioning is partly illusory, since several "
    "of these agents are additives with E numbers that must be declared."
)
