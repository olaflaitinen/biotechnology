# =============================================================================
#  biotechnology.branches.yellow.probiotics_and_prebiotics.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record covers a field where the commercial claims and the evidence have
#  diverged more sharply than anywhere else in the branch, and the narrative
#  has to be careful in both directions. Dismissing the whole category is as
#  wrong as accepting its marketing.
#
#  WHAT THE EVIDENCE SUPPORTS is specific and strain-dependent: particular
#  organisms, at particular doses, for particular conditions. Reducing the
#  duration of infectious diarrhoea in children, reducing the incidence of
#  antibiotic-associated diarrhoea, and reducing necrotising enterocolitis in
#  preterm infants are supported by substantial trial evidence.
#
#  WHAT IT DOES NOT SUPPORT is the general proposition, sold on most shelves,
#  that consuming live bacteria improves health in a healthy adult. It is not
#  that this has been disproved; it is that the trials mostly have not been
#  done at the quality required, and the ones that have been done are
#  frequently for a different strain from the one in the product.
#
#  THE CENTRAL FACT A READER NEEDS is that PROBIOTIC EFFECTS ARE
#  STRAIN-SPECIFIC. Evidence for one strain does not transfer to another of the
#  same species, any more than one breed of dog tells you about another. Most
#  marketing, and a good deal of press coverage, treats the species name as the
#  active ingredient. It is not.
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
    "Live microorganisms and the substrates that feed them, taken to modify "
    "the gut microbial community, with strain-specific and uneven evidence."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the definitions, which are contested and matter, (b) the
#  strain specificity problem, (c) what the evidence actually supports, (d) the
#  gap between that and the market.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the definitions
    "A probiotic is conventionally defined as a live microorganism that, "
    "administered in adequate amounts, confers a health benefit on the host. "
    "The definition is doing more work than it appears: it requires the "
    "organism to be alive, the dose to be sufficient, and the benefit to be "
    "demonstrated, so a product meeting none of those is not a probiotic even "
    "if it contains bacteria. A prebiotic is a substrate selectively used by "
    "host microorganisms to confer a benefit, which chiefly means "
    "non-digestible carbohydrates that reach the colon intact and are fermented "
    "there. Synbiotics combine the two, and postbiotics are inactivated "
    "organisms or their components, a category created partly because the "
    "requirement that a probiotic be alive is commercially inconvenient. "
    # (b) strain specificity
    "The property that governs the whole field is that effects are "
    "strain-specific rather than species-specific. Two strains of the same "
    "species can differ in adhesion, in the metabolites they produce and in "
    "their effect on the host, and evidence generated for one does not "
    "transfer to another. This is why strain designations matter, why a "
    "product should name them, and why a great deal of published evidence "
    "cannot be applied to the product a consumer actually buys. "
    # (c) what the evidence supports
    "Where trials have been done properly the results are real and narrow. "
    "Specific strains reduce the duration of acute infectious diarrhoea in "
    "children, reduce the incidence of antibiotic-associated diarrhoea, and "
    "reduce necrotising enterocolitis in preterm infants, the last being the "
    "strongest evidence in the field and concerning a condition with "
    "substantial mortality. Faecal microbiota transplantation, which is the "
    "same idea taken to its logical conclusion, is highly effective against "
    "recurrent Clostridioides difficile infection and is the clearest "
    "demonstration that the gut community can be therapeutically manipulated. "
    # (d) the gap
    "The gap between that and the market is wide. Most products carry no "
    "strain designation, most claims are made for general wellbeing rather "
    "than a defined condition, and in the European Union no health claim for "
    "any probiotic has been authorised, which is why products are sold on "
    "implication rather than assertion. Colonisation is usually transient, so "
    "an effect that depends on the organism persisting generally does not "
    "outlast consumption. And the mechanism, where it is understood at all, is "
    "frequently metabolic or immunological rather than a matter of the organism "
    "taking up residence."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Your gut contains an enormous number of bacteria, and which ones they are "
    "seems to matter for health. Probiotics are live bacteria you swallow "
    "deliberately; prebiotics are the fibres that feed the ones already there. "
    "Some of this is well established. Particular bacteria, at particular "
    "doses, genuinely shorten some kinds of diarrhoea and prevent a dangerous "
    "gut condition in very premature babies. Much of what is sold, though, "
    "makes vaguer promises than the evidence supports, and one detail explains "
    "most of the confusion: the effect depends on the exact strain, not on the "
    "species. Two bacteria with the same name on the label can behave "
    "completely differently."
)

# -----------------------------------------------------------------------------
#  The garden reseeding analogy. Chosen because it carries transience, which is
#  the least understood property of the field, and because its limit is the
#  honest one: an established garden resists new planting, which is exactly why
#  colonisation usually fails.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is scattering seed on an established lawn. Some will germinate and "
    "something will change while you keep scattering. Stop, and the lawn "
    "returns to what it was, because the existing plants were not there by "
    "accident. That is the part most often left out: for most people and most "
    "products the newcomers pass through rather than settle, and the effect, "
    "where there is one, lasts about as long as the supply does."
)

WHY_IT_MATTERS = (
    "In the places the evidence is strong it is genuinely strong. Specific "
    "probiotic strains reduce necrotising enterocolitis in preterm infants, a "
    "condition that kills, and that is among the better-supported nutritional "
    "interventions in neonatal care. Faecal microbiota transplantation cures "
    "recurrent Clostridioides difficile infection at rates antibiotics do not "
    "approach, and it established beyond argument that the gut community can be "
    "manipulated therapeutically. Prebiotic fibres have effects on stool "
    "consistency, mineral absorption and satiety that are measurable and "
    "reproducible. Human milk oligosaccharides in infant formula supply "
    "compounds that shape the infant gut community and that formula previously "
    "lacked entirely. The costs of the field are mostly costs to its own "
    "credibility. Most products name no strain, so published evidence cannot "
    "be attached to them. No health claim for a probiotic has been authorised "
    "in the European Union, and products are consequently sold on implication. "
    "Colonisation is usually transient and this is rarely disclosed. Viability "
    "at the end of shelf life is frequently below what is claimed and is not "
    "routinely verified. And there are real safety questions in specific "
    "populations, since live organisms have caused bloodstream infections in "
    "immunocompromised and critically ill patients, which is a reason the "
    "casual framing of these products as harmless is wrong even where they are "
    "ineffective."
)
