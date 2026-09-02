# =============================================================================
#  biotechnology.branches.red.gene_therapy.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE -  everything that is prose.
# -----------------------------------------------------------------------------
#
#  WHY THIS IS A SEPARATE FILE
#  A subtype record mixes five very different kinds of content: prose, lists
#  of practice, numbers, dates and governance. Reviewing them together is
#  hopeless, because the people qualified to check each kind are different
#  people. A clinical geneticist should be able to open one file and check the
#  science without wading past regulation citations; a science communicator
#  should be able to rewrite the plain-language paragraph without ever seeing
#  a Python import. This package splits the record along exactly those lines,
#  and this file holds the prose.
#
#  THE TWO REGISTERS
#  Every subtype in this library is described twice, deliberately and in full.
#
#    TECHNICAL REGISTER   SUMMARY, DESCRIPTION
#        Written for a reader who already knows the vocabulary. Dense, exact,
#        no hedging, no marketing. Assumes an undergraduate life-science
#        education. This is what a researcher, a regulator or a grant
#        reviewer will read.
#
#    PUBLIC REGISTER      PLAIN_LANGUAGE, ANALOGY, WHY_IT_MATTERS
#        Written for a reader with no scientific training at all: a
#        journalist, a policy adviser, a patient, a school student, a
#        procurement officer. No unexplained term is permitted. The analogy
#        must be drawn from ordinary life and must not be misleading when
#        pushed one step further than intended.
#
#  THE EDITORIAL RULES THAT APPLY TO THIS FILE
#    1. PLAIN_LANGUAGE must contain no word that would not appear in a general
#       newspaper. "DNA", "gene", "cell" and "virus" are permitted; "vector",
#       "episomal", "transduction" and "capsid" are not.
#    2. ANALOGY must be checkable. A reader should be able to see where the
#       analogy breaks down, and the text should not depend on it not breaking.
#    3. WHY_IT_MATTERS must state both the benefit and the cost or the
#       controversy. A record that lists only upside is advertising, and this
#       library is not advertising.
#    4. DESCRIPTION states what the field does, not what it hopes to do.
#       Aspiration belongs in the challenges list in `practice.py`.
#    5. No sentence may assert a number that is not also present, with a unit
#       and an evidence grade, in `metrics.py`.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
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

# -----------------------------------------------------------------------------
#  SUMMARY
#  One sentence. It appears in every index, table, search result and command
#  line listing in the project, so it must stand alone with no context at all.
#  Hard limit in review: 200 characters.
# -----------------------------------------------------------------------------
SUMMARY = (
    "Treating disease by adding, silencing, replacing or editing genetic "
    "material inside a patient's cells."
)

# -----------------------------------------------------------------------------
#  DESCRIPTION
#  Three to eight sentences of technical exposition. The structure used here,
#  and recommended for every subtype, is:
#      (a) a definition that fixes the boundary of the field,
#      (b) the strategies or sub-approaches that exist inside that boundary,
#      (c) how the thing is actually delivered or performed in practice,
#      (d) the constraint that shapes everything else.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) definition
    "Gene therapy is the deliberate modification of nucleic acid inside a "
    "patient in order to produce a therapeutic effect. "
    # (b) the four strategies
    "Four strategies are in clinical use or late-stage development. Gene "
    "addition supplies a working copy of a gene without removing the faulty "
    "one, and is the approach used in most approved products. Gene silencing "
    "suppresses a harmful transcript with antisense oligonucleotides or short "
    "interfering RNA. Gene editing rewrites the genome in place using "
    "nuclease, base-editing or prime-editing systems. Gene regulation changes "
    "how much of an existing gene is expressed without altering its sequence. "
    # (c) delivery
    "Delivery is either in vivo, where the vector is infused or injected into "
    "the patient, or ex vivo, where cells are removed, modified in a clean "
    "room and returned. The dominant in vivo vehicle is the adeno-associated "
    "virus, chosen for low pathogenicity and long episomal persistence in "
    "post-mitotic tissue; the dominant ex vivo vehicle is the lentivirus, "
    "chosen because it integrates into the genome and is therefore inherited "
    "by every daughter cell. "
    # (d) the constraint that shapes the field
    "The binding constraint is not efficacy but delivery: getting enough "
    "vector to the right tissue, in a patient whose immune system may already "
    "recognise that vector, at a manufacturing cost that a health system can "
    "absorb."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

# -----------------------------------------------------------------------------
#  PLAIN_LANGUAGE
#  The single most important field in this library for readers outside the
#  field. Written at roughly a fourteen-year-old reading level. Every technical
#  idea is either explained in place or omitted.
# -----------------------------------------------------------------------------
PLAIN_LANGUAGE = (
    "Your body follows a set of written instructions stored in your cells, "
    "called DNA. In some illnesses one of those instructions has a mistake in "
    "it, so the body cannot make something it needs. Gene therapy puts a "
    "corrected instruction into the cells, usually by hiding it inside a "
    "harmless virus that acts as a delivery van. If it works, the body starts "
    "producing the missing part on its own, sometimes after a single "
    "treatment. The change is made only in the treated person; it is not "
    "passed on to their children."
)

# -----------------------------------------------------------------------------
#  ANALOGY
#  One everyday image. It exists to give a reader a handle, not a model, and it
#  is chosen so that its limits are visible. The factory image below breaks
#  down in a useful way: a factory manual can be reprinted at will, whereas a
#  cell's instructions can be reached only through the delivery problem
#  described in DESCRIPTION.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Imagine a factory working from a printed manual with one page smudged "
    "beyond reading, so a single component never gets made. Gene therapy does "
    "not rebuild the factory. It slips a clean copy of that one page into the "
    "manual, and the production line starts again. The hard part is not "
    "printing the page - it is getting it into every relevant manual in a "
    "building with several trillion rooms."
)

# -----------------------------------------------------------------------------
#  WHY_IT_MATTERS
#  Consequence, at the scale a non-specialist cares about, with the cost or the
#  controversy stated in the same breath as the benefit. Review rule 3 applies
#  strictly here.
# -----------------------------------------------------------------------------
WHY_IT_MATTERS = (
    "Most of the roughly seven thousand known rare diseases are caused by a "
    "fault in a single gene, and for the great majority there has never been "
    "any treatment that addresses the cause rather than the symptoms. Gene "
    "therapy is the first approach that can, in principle, treat them at the "
    "source, and in several cases a single infusion has replaced a lifetime "
    "of transfusions or injections. It also raises hard questions about price "
    "- list prices above two million euro per patient are now routine - and "
    "about equity, since the health systems with the most patients are often "
    "those least able to pay, and almost no manufacturing capacity exists "
    "outside a handful of high-income countries."
)
