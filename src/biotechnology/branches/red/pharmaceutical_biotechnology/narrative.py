# =============================================================================
#  biotechnology.branches.red.pharmaceutical_biotechnology.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  The facet contract and the editorial rules are documented once, in full, in
#  `branches/red/gene_therapy/narrative.py`. In brief:
#
#      SUMMARY, DESCRIPTION            technical register
#      PLAIN_LANGUAGE, ANALOGY,
#      WHY_IT_MATTERS                  public register, no unexplained jargon
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the commercial anchor of the entire colour scheme, so the public
#  register carries an extra burden: a reader needs to understand not only
#  what a biologic is but why it costs what it costs. The bread analogy below
#  is chosen because it makes the process-defines-product principle - the
#  single most consequential fact in biologic regulation - obvious without
#  using the phrase.
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

SUMMARY = (
    "Discovery, production and formulation of biologic medicines made in "
    "living expression systems rather than by chemical synthesis."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what a biologic is, (b) why it cannot be synthesised,
#  (c) the production sequence, (d) the constraint that shapes regulation.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) definition
    "A biologic is a medicine whose active ingredient is produced by a living "
    "system: a recombinant protein, a monoclonal antibody, a peptide, an "
    "enzyme, a nucleic acid, or a conjugate of these. "
    # (b) why chemistry cannot do it
    "The molecule is typically a hundred to a thousand times larger than a "
    "conventional small-molecule drug and carries post-translational "
    "modifications, above all glycosylation, that no synthetic route can "
    "reproduce economically or reproducibly. "
    # (c) the production sequence
    "Production follows a fixed sequence. A gene of interest is cloned into an "
    "expression vector; a host cell line is transfected and a single "
    "high-producing clone is isolated and banked as a master and a working "
    "cell bank; the clone is expanded through seed trains into production "
    "bioreactors; the product is captured on an affinity resin, polished by "
    "one or two orthogonal chromatography steps, and formulated. Chinese "
    "hamster ovary cells dominate for glycosylated proteins, Escherichia coli "
    "for simple non-glycosylated ones, and yeast for peptides and some "
    "vaccine antigens. "
    # (d) the constraint that shapes everything downstream
    "Because the product is defined by its process as much as by its "
    "sequence, regulators treat any change to the process as a change to the "
    "medicine. That single principle is why generic copies are called "
    "biosimilars rather than generics, why a comparability exercise follows "
    "every process change, and why manufacturing capacity rather than "
    "chemistry is the barrier to entry."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Aspirin is a small, simple molecule that a chemist can build from "
    "scratch in a flask. Insulin is not: it is a folded chain of building "
    "blocks far too complicated to assemble that way. So instead of building "
    "it, we give the recipe to living cells, grow those cells in enormous "
    "stainless steel tanks, and let them do the manufacturing. Afterwards the "
    "medicine is separated out and purified until nothing of the cells "
    "remains. Almost all modern cancer and arthritis medicines are made like "
    "this."
)

# -----------------------------------------------------------------------------
#  The bread analogy is load-bearing. It is chosen because everyone already
#  accepts, without being told, that two bakeries following the same recipe
#  produce different bread - which is exactly the principle behind biosimilar
#  regulation.
# -----------------------------------------------------------------------------
ANALOGY = (
    "You cannot carve a loaf of bread out of a block of wood, however sharp "
    "your knife. You have to let yeast make it. Biologic medicines are the "
    "same: the product is grown rather than machined. And as with bread, the "
    "recipe alone is not enough - the temperature, the timing and the "
    "particular strain of yeast all end up in the result, which is why a copy "
    "made in a different factory is never quite identical and has to be "
    "tested rather than assumed equivalent."
)

WHY_IT_MATTERS = (
    "Biologics changed the prognosis of rheumatoid arthritis, several "
    "cancers and a long list of autoimmune conditions from managed decline to "
    "something close to normal life. They are also the most expensive class "
    "of medicine ever made, and about half of all pharmaceutical spending in "
    "high-income health systems now goes to them. That is why biosimilar "
    "competition matters so much: when a biosimilar enters a European market "
    "the price of the reference product typically falls by a quarter to a "
    "half within two years, which is often the difference between a health "
    "system funding a treatment for everyone who needs it and rationing it."
)
