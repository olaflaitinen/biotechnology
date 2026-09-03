# =============================================================================
#  biotechnology.branches.yellow.cultivated_meat.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the most publicised record in the branch and among the least
#  commercially realised in the library, and the narrative has to hold both
#  facts at once without sounding like either a promotion or a debunking.
#
#  WHAT IS TRUE: the biology works. Animal cells grow in culture, differentiate
#  into muscle and fat, and the product is meat by any compositional test. Two
#  jurisdictions have approved sales. This is not a speculative technology.
#
#  WHAT IS ALSO TRUE: it is produced in kilograms rather than tonnes, at a cost
#  that no published figure has brought near commodity meat, and the
#  constraints are not ones that scale obviously solves. The medium is the
#  dominant cost and is a pharmaceutical input; the bioreactor economics are
#  those of `white.bioprocess_engineering` applied to a product worth a
#  thousandth as much per kilogram; and animal cells are shear-sensitive,
#  slow-growing and finite in their divisions unless immortalised, which is
#  itself a regulatory question.
#
#  THE HONEST FRAME IS THAT THIS RECORD DESCRIBES A DEMONSTRATED CAPABILITY
#  WITH AN UNSOLVED COST STRUCTURE. That is a real thing to be, and it is not
#  the thing the coverage describes.
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
    "Growing animal muscle and fat cells in culture to produce meat without "
    "raising or slaughtering an animal."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what the process is, (b) the four unsolved problems, (c) what
#  has actually been achieved, (d) why the scale-up is not the usual scale-up.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the process
    "Cultivated meat grows animal cells in a bioreactor and assembles them into "
    "a food. The sequence is established: a cell line is obtained from a biopsy "
    "or an existing bank, expanded in a growth medium, differentiated into "
    "muscle and fat, and either harvested as loose cells for a formed product "
    "or grown on a scaffold to approach the structure of a cut. The biology is "
    "not in doubt. Animal cell culture has been routine in laboratories for "
    "seventy years and at manufacturing scale in `red.pharmaceutical_biotechnology` "
    "for forty. "
    # (b) the four problems
    "Four problems are unsolved together, and they interact. The growth medium "
    "is the dominant cost and was developed as a pharmaceutical input, so "
    "removing its serum, replacing its recombinant growth factors with cheaper "
    "sources and recycling it are the field's central work. Cell line "
    "performance matters more than in pharmaceutical culture because the cells "
    "are the product rather than a factory for one: primary cells senesce after "
    "a limited number of divisions, and immortalised lines avoid that at the "
    "cost of a regulatory conversation about what has been done to them. "
    "Bioreactor design must handle shear-sensitive adherent cells at volumes "
    "the pharmaceutical industry never needed, since a therapeutic protein is "
    "made in grams and food is made in tonnes. And structure is a separate "
    "problem again: loose cells make a formed product, and anything resembling "
    "a steak requires scaffolding, perfusion and co-culture of at least muscle "
    "and fat. "
    # (c) what has been achieved
    "What has been achieved is real and modest. A cultivated burger was "
    "presented in 2013 at a cost that made the point rather than the product. "
    "Regulatory approval for sale followed in Singapore in 2020 and in the "
    "United States in 2023, in both cases for chicken products and at small "
    "volumes. Several jurisdictions have moved in the other direction and "
    "prohibited sale outright. Production remains at kilogram rather than tonne "
    "scale. "
    # (d) why scale-up is different here
    "The scale-up problem is not the ordinary one. In most technologies cost "
    "falls with volume because fixed costs spread and manufacturing improves. "
    "Here the dominant cost is a consumable input, the medium, whose price "
    "falls only if its composition changes, and the second cost is capital for "
    "bioreactor capacity that does not yet exist at food scale. Neither falls "
    "automatically with volume, which is the same error "
    "`yellow.precision_fermentation` made in its 2023 projections and the same "
    "shape `white.biobased_chemicals` records for succinic acid."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "This is growing meat from animal cells instead of from animals. A small "
    "sample of cells is taken once, then fed and multiplied in a tank until "
    "there is enough to eat. It is genuinely meat, not an imitation, and it has "
    "been approved for sale in a couple of places. It is also made in very "
    "small quantities and costs a great deal, because the liquid the cells are "
    "fed on was developed for medical laboratories and is expensive, and "
    "because equipment to do this at the scale of a food industry does not "
    "exist yet. The science is real. The price is the problem, and it is not "
    "the kind of problem that gets solved simply by making more."
)

# -----------------------------------------------------------------------------
#  The greenhouse analogy. Chosen because it captures the actual cost
#  structure, where the input rather than the output dominates, and because its
#  limit is the honest one: a greenhouse at least gets its light free.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is growing tomatoes in a heated greenhouse in winter. The tomatoes are "
    "real tomatoes and nobody disputes that; what decides whether the business "
    "works is the heating bill, not the horticulture. The comparison is kind in "
    "one respect and unkind in another. A greenhouse at least gets its light "
    "free, while every nutrient these cells receive has to be bought and most "
    "of it was priced for a laboratory."
)

WHY_IT_MATTERS = (
    "If it worked at scale it would address something no other record in this "
    "branch addresses: meat itself, rather than a substitute for it, produced "
    "without raising or slaughtering an animal. That removes the welfare "
    "question entirely rather than reducing it, avoids the antibiotic use and "
    "zoonotic risk that `green.veterinary_vaccines` describes, and would in "
    "principle use a fraction of the land that livestock occupies. For "
    "consumers unwilling to accept a substitute, it is the only approach that "
    "offers the product rather than an approximation, which is why it attracts "
    "attention disproportionate to its volume. The honest position is that "
    "none of that has been delivered. Production is at kilogram scale, cost per "
    "kilogram remains far above commodity meat, and the dominant cost is a "
    "medium input whose price does not fall simply with volume. The "
    "environmental case is genuinely uncertain rather than merely unproven: "
    "assessments differ on whether cultivated meat beats conventional beef, and "
    "the answer depends almost entirely on how the energy for the process is "
    "generated and on how the medium inputs are produced. Several jurisdictions "
    "have prohibited sale for reasons that are cultural and political rather "
    "than evidential, which no technical progress will resolve. And the "
    "immortalised cell lines that make continuous production practical raise a "
    "regulatory and consumer conversation the field has not had in public."
)
