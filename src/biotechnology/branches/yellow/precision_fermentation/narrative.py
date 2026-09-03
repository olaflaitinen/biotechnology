# =============================================================================
#  biotechnology.branches.yellow.precision_fermentation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record must say clearly what it is NOT, because the term is used
#  loosely and the looseness matters commercially.
#
#  PRECISION FERMENTATION IS NOT A NEW TECHNOLOGY. It is the manufacture of a
#  specific protein by an engineered microorganism, which is exactly what
#  `white.microbial_fermentation` has done for insulin since 1982 and for
#  chymosin since 1988. The technique is forty years old and thoroughly
#  routine.
#
#  WHAT IS NEW IS THE TARGET AND THE ARGUMENT. Making a milk protein rather
#  than a medicine changes nothing technically and everything commercially: the
#  product must compete with an agricultural commodity on price rather than
#  with a patented drug on efficacy, which is a completely different economic
#  problem. Insulin at a few grams per patient per year tolerates a
#  manufacturing cost that dairy protein at millions of tonnes does not.
#
#  THE THIRD THING TO SAY EARLY IS THE ONE THE FIELD FINDS AWKWARD. The protein
#  is identical to the animal one, which is the entire selling proposition, and
#  it is therefore an allergen in exactly the same way. Whey protein made by a
#  fungus will still cause a milk allergy, and no amount of describing it as
#  animal-free changes that.
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
    "Producing specific animal proteins and other defined food molecules by "
    "engineered microorganisms rather than by animals."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what it is and why it is not new, (b) what actually changed,
#  (c) the products and where they stand, (d) the constraints, which are
#  economic and regulatory rather than technical.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) not new
    "Precision fermentation produces a defined molecule, usually a protein, by "
    "an engineered microorganism grown in a fermenter. The technique is not "
    "new. Recombinant human insulin has been made this way since 1982 and "
    "chymosin for cheesemaking since 1988, and the great majority of cheese "
    "produced in several countries has been made with fermentation-derived "
    "chymosin for decades without controversy or much public awareness. What "
    "the term names is a shift in target rather than in method. "
    # (b) what changed
    "The shift matters commercially rather than technically. A pharmaceutical "
    "protein is required in grams per patient and competes on efficacy against "
    "a patented alternative, so a manufacturing cost of hundreds of euro per "
    "gram is unremarkable. A dairy protein is required in millions of tonnes "
    "and competes on price against an agricultural commodity produced by an "
    "industry with enormous scale and, in many countries, subsidy. The "
    "engineering problem is therefore not making the protein, which is solved, "
    "but making it at a cost per kilogram that a food ingredient can bear, "
    "which is the problem `white.bioprocess_engineering` describes in general "
    "and which bites hardest here. "
    # (c) the products
    "The products divide into three. Dairy proteins, chiefly beta-lactoglobulin "
    "and casein, are furthest advanced and have reached the market in several "
    "jurisdictions. Egg proteins including ovalbumin follow. And a wider set of "
    "molecules is produced the same way without attracting the same label: "
    "vitamins, flavour compounds, sweetener proteins, human milk "
    "oligosaccharides for infant formula, and the heme protein used to give "
    "plant-based meat its character. The last of these is the most widely eaten "
    "precision fermentation product that most consumers have never heard "
    "described as one. "
    # (d) the constraints
    "Three constraints govern. Cost per kilogram must approach that of an "
    "agricultural commodity, which requires titres and downstream efficiency "
    "that only some products have reached. Regulatory approval is required in "
    "full, because the product has no history of consumption even where the "
    "identical animal protein does, which is the position "
    "`yellow.food_fermentation` contrasts with. And functionality is not "
    "guaranteed by identity: a protein with the correct sequence may not "
    "behave in a food matrix as the animal protein does, because "
    "glycosylation, folding and the accompanying minor components all "
    "contribute to how a real ingredient performs."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "This is making the proteins that are in milk or eggs without using an "
    "animal. A microbe is given the instructions for the protein, grown in a "
    "tank, and the protein is collected. The result is the same molecule, not "
    "an imitation, so it behaves in cooking the way the real thing does. It is "
    "also not new: the enzyme used to make most cheese has been produced this "
    "way since the 1980s, and so has the insulin that people with diabetes use. "
    "One thing is worth knowing plainly. Because the protein is genuinely the "
    "same, it causes the same allergies. Milk protein made without a cow will "
    "still affect someone allergic to milk."
)

# -----------------------------------------------------------------------------
#  The printing analogy. Chosen because it carries identity rather than
#  imitation, which is the record's central claim, and because its limit is the
#  honest one: a copy that is genuinely identical inherits everything about the
#  original, including the parts nobody wanted.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is printing a document rather than describing it. A plant-based "
    "substitute is a description, however good, and this is the same text on "
    "different paper. The limit of the comparison is worth stating: an "
    "identical copy inherits everything, so if the original was difficult for "
    "somebody to read, the copy is too. A milk protein made without a cow is "
    "still a milk protein to an immune system."
)

WHY_IT_MATTERS = (
    "Dairy and egg production occupy a great deal of land, water and feed, and "
    "producing the functional proteins directly removes the animal from that "
    "part of the supply. The proteins behave as the originals do, so a cheese "
    "or a mayonnaise can be made rather than approximated, which is the "
    "difference between substitution and replacement. Human milk "
    "oligosaccharides for infant formula and vitamin B12 for people eating no "
    "animal products are cases where fermentation supplies something that has "
    "no practical alternative source. And the technology is genuinely mature: "
    "most cheese in several countries has been made with a "
    "fermentation-derived enzyme for over thirty years. The costs deserve equal "
    "clarity. Cost per kilogram remains the binding problem for the bulk "
    "proteins, and the comparison is against a heavily scaled and often "
    "subsidised agricultural commodity. The feedstock is sugar, which is grown "
    "on farmland, so the land saving is real and smaller than the marketing "
    "suggests, and only a full life cycle assessment settles it. Regulatory "
    "approval is slow and expensive, and it applies in full to a molecule "
    "identical to one people have eaten for millennia, which is defensible as "
    "caution and is a genuine barrier to entry that favours incumbents. And "
    "the allergen position is unchanged, which is not a marketing "
    "inconvenience but a labelling requirement and a safety fact."
)
