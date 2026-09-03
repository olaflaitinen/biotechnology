# =============================================================================
#  biotechnology.branches.blue.marine_natural_products.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record carries the constraint named in the blue branch header, and it
#  is stated in both registers because everything else follows from it.
#
#      THE PROBLEM IS NEVER DISCOVERY. THE PROBLEM IS SUPPLY.
#
#  Marine invertebrates make interesting molecules in vanishing quantities.
#  One anticancer compound required roughly a tonne of tunicate for a gram of
#  material. Another needed many tonnes of a bryozoan for a few grams. A third
#  came from a sponge at similar ratios. No marine-derived medicine has ever
#  reached a market by harvesting its source organism, and every one that
#  succeeded did so by synthesis, semisynthesis, fermentation of the symbiont
#  that actually makes the compound, or a simplified analogue.
#
#  THE SECOND IDEA IS WHY THE CHEMISTRY IS INTERESTING AT ALL. A sponge cannot
#  run away and cannot hide. Its defence is chemical, released into an ocean
#  that dilutes it immediately, so anything that works must work at very low
#  concentration. That is precisely the property a drug needs, and it is why
#  the sea has produced pharmacology out of all proportion to how little of it
#  has been sampled.
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
    "Discovery and development of pharmacologically active compounds from "
    "marine organisms, where supply rather than discovery is the constraint."
)

# -----------------------------------------------------------------------------
#  Structure: (a) why marine chemistry is distinctive, (b) the supply problem,
#  (c) the four routes out of it, (d) what has actually reached patients.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) why the chemistry is different
    "Marine natural products are secondary metabolites from marine organisms "
    "investigated for pharmacological activity. Two features distinguish them "
    "from their terrestrial counterparts. The first is structural: marine "
    "chemistry uses halogens far more freely than terrestrial chemistry, "
    "because seawater supplies bromine and chlorine in abundance, and it "
    "occupies regions of chemical space that plant and soil chemistry does not "
    "reach. The second is potency. A sessile animal defends itself by "
    "releasing compounds into water that disperses them at once, so selection "
    "favours molecules active at very low concentration, which is the same "
    "property that makes a molecule a plausible drug. "
    # (b) the supply problem
    "The field's defining difficulty follows immediately. These compounds are "
    "produced in minute quantities by animals that grow slowly, cannot be "
    "farmed, and in several cases are protected. Quantities sufficient for "
    "preclinical work have required tonnes of biomass for grams of material, "
    "and quantities sufficient for a market are simply unobtainable by "
    "collection. A promising compound with no supply route is not a candidate; "
    "it is a publication. "
    # (c) the four routes out
    "Four routes exist and each has produced a marketed medicine or come "
    "close. Total synthesis works where the molecule is tractable and fails "
    "where it is not. Semisynthesis starts from a related compound available "
    "by fermentation and converts it, which is how the tunicate-derived "
    "anticancer agent is actually manufactured. Analogue design keeps the "
    "pharmacophore and discards the synthetically difficult remainder, which is "
    "how a sponge macrolide became a marketed drug. And heterologous expression "
    "of the biosynthetic gene cluster addresses the fact, established "
    "repeatedly, that the animal often does not make the compound at all: a "
    "microbial symbiont does. "
    # (d) what actually reached patients
    "The clinical record is small, real, and worth stating precisely rather "
    "than in the aggregate. Marine-derived agents in use include a treatment "
    "for severe chronic pain derived from cone snail venom, given intrathecally "
    "because the peptide does not survive any other route; several anticancer "
    "agents including one from a tunicate and one designed from a sponge "
    "macrolide; and a cytotoxic payload of marine origin used in antibody drug "
    "conjugates. Early antiviral and anticancer nucleosides were developed from "
    "sponge chemistry in the 1950s and 1960s. That is a short list from a very "
    "large search, which is the honest description of the field."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Animals fixed to the seabed cannot run away, so they defend themselves "
    "with chemistry. Because the sea washes everything away immediately, those "
    "chemicals have to be powerful in tiny amounts, which is exactly what a "
    "medicine needs to be. Several real drugs have come from this: a painkiller "
    "from the venom of a sea snail for people nothing else helps, and cancer "
    "treatments found in a sea squirt and a sponge. The difficulty is almost "
    "never finding something. It is getting enough of it. These animals make "
    "the interesting substance in vanishingly small quantities, grow slowly, "
    "and cannot be farmed, so collecting your way to a medicine is impossible."
)

# -----------------------------------------------------------------------------
#  The recipe analogy. It carries the supply problem, which is the harder half
#  of the record, and its stated limit is the useful part: the cook can at
#  least go to another shop, and the chemist frequently cannot.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is finding a superb recipe that calls for an ingredient sold by one "
    "shop, in one town, a spoonful at a time. The recipe is not the hard part "
    "and never was. The comparison flatters the situation, though, because a "
    "cook can eventually find another supplier, and here there is often no "
    "other supplier at all: the only way forward is to work out how the "
    "ingredient is made and make it yourself."
)

WHY_IT_MATTERS = (
    "This field has produced medicines that exist for no other reason. A "
    "peptide from cone snail venom treats severe chronic pain in patients who "
    "respond to nothing else, and it works because it blocks a channel that no "
    "terrestrial chemistry had provided a tool for. Anticancer agents derived "
    "from a Caribbean tunicate and designed from a sponge macrolide are in "
    "clinical use. A marine-derived cytotoxin is the warhead in several "
    "antibody drug conjugates, which means marine chemistry is present in "
    "modern targeted cancer therapy without being visible in its name. The "
    "costs are substantial and are not only financial. Early bioprospecting "
    "damaged the reefs and beds it sampled, sometimes severely, and collection "
    "at the scale preclinical work required was not sustainable by any "
    "definition. The economics are unattractive: a decade of chemistry may end "
    "in a molecule that cannot be supplied, so pharmaceutical companies largely "
    "withdrew from marine discovery despite the success rate per compound being "
    "high. And the benefits have accrued unevenly, since the organisms were "
    "frequently collected in tropical waters and the resulting medicines are "
    "priced for wealthy health systems, which is the practical shape of the "
    "access and benefit sharing argument rather than its abstract form."
)
