# =============================================================================
#  biotechnology.branches.blue.marine_biomaterials.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record escapes the constraint that governs the rest of the blue branch,
#  and saying so early is the most useful thing the narrative can do.
#
#  `blue.marine_natural_products` is defined by supply: a gram of compound per
#  tonne of animal, from creatures that cannot be farmed. THIS RECORD HAS THE
#  OPPOSITE PROBLEM. Its principal raw materials are WASTE. Crustacean shells
#  from the seafood industry, fish skins and scales from filleting, and seaweed
#  from an industry already producing tens of millions of tonnes. The materials
#  are abundant, cheap and currently discarded at cost.
#
#  So the difficulty here is not obtaining the material. It is that the
#  material is VARIABLE. A polymer extracted from an animal differs between
#  species, seasons, individuals and processing batches, and a medical device
#  or a pharmaceutical excipient requires consistency that a wild-caught raw
#  material does not naturally provide. Characterisation and standardisation,
#  not supply, are what this field spends its effort on.
#
#  THE SECOND IDEA IS THAT THE BEST MARINE MATERIALS ARE STRUCTURES RATHER THAN
#  SUBSTANCES. Nacre, sponge silica and mussel adhesive are interesting for how
#  they are ARRANGED, and copying an arrangement is a harder and more
#  interesting problem than extracting a compound.
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
    "Structural materials from marine organisms, chiefly polysaccharides, "
    "collagens and mineralised composites, mostly recovered from waste."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the material classes and where they come from, (b) why waste
#  origin inverts the branch's usual problem, (c) the variability constraint
#  that replaces it, (d) the structural materials, which are the harder and
#  more interesting half.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the classes
    "Marine biomaterials are structural materials derived from marine "
    "organisms. Four classes carry the field. Polysaccharides from seaweed, "
    "meaning alginate, agarose, carrageenan and fucoidan, gel and thicken and "
    "form hydrogels under mild conditions. Chitin and its deacetylated "
    "derivative chitosan come from crustacean shells and are among the most "
    "abundant polymers on Earth after cellulose. Marine collagens and gelatins "
    "come from fish skin, scales and jellyfish. And mineralised composites, "
    "including coral skeleton, nacre and sponge biosilica, are inorganic "
    "structures built by organisms at ambient temperature. "
    # (b) the inversion
    "Where the rest of this branch is constrained by supply, this record is "
    "constrained by nothing of the kind, because its raw materials are waste. "
    "Crustacean shell is a disposal cost for the shellfish industry, fish skin "
    "and scale are by-products of filleting, and seaweed is farmed at tens of "
    "millions of tonnes for other purposes. The material is abundant, cheap and "
    "already being landed, which places this record in an unusually strong "
    "position within its branch and links it directly to waste valorisation. "
    # (c) the constraint that replaces supply
    "What limits the field instead is variability. A polymer extracted from an "
    "organism differs by species, by season, by individual and by processing "
    "batch, in molecular weight, in degree of deacetylation for chitosan, in "
    "the ratio of the two uronic acid blocks for alginate, and in sulphation "
    "for carrageenan and fucoidan. Those parameters determine gelation, "
    "mechanical properties and biological activity. A medical device or a "
    "pharmaceutical excipient requires batch-to-batch consistency that a "
    "wild-derived raw material does not naturally provide, so characterisation, "
    "specification and standardisation absorb most of the field's effort, and "
    "the absence of agreed standards is the most common reason a promising "
    "material does not reach a regulated application. "
    # (d) the structural half
    "The mineralised and adhesive materials are a different proposition. Nacre "
    "is calcium carbonate and a small fraction of protein arranged in layers, "
    "and it is orders of magnitude tougher than the mineral alone; sponge "
    "biosilica is formed at seawater temperature where industrial silica "
    "requires high heat; mussel adhesive proteins bond to wet surfaces, which "
    "synthetic adhesives do poorly. In each case the interest is in the "
    "arrangement rather than the composition, so the useful work is biomimetic "
    "rather than extractive: understanding the structure and reproducing it "
    "synthetically, since harvesting the organism is neither scalable nor "
    "acceptable."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "The sea makes materials that are difficult to copy. Seaweed gives "
    "substances that turn liquids into gels, and they are in wound dressings, "
    "in the mould a dentist takes of your teeth, and in a great deal of food. "
    "Crab and prawn shells, which the seafood industry pays to throw away, "
    "yield a material used to stop bleeding and to make fibres and coatings. "
    "Fish skin gives collagen. And mussels stick to wet rock in breaking waves, "
    "which is something no glue we make does well. Most of the raw material is "
    "waste, so the problem is not getting hold of it. The problem is that no "
    "two batches of a natural material are quite the same, and a medical "
    "product has to be."
)

# -----------------------------------------------------------------------------
#  The reclaimed timber analogy. Chosen because it carries both halves at once:
#  the material is abundant and free, and its variability is exactly what makes
#  it hard to use in an application that demands consistency.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is building with reclaimed timber. The wood is abundant, cheap and "
    "already there, which is the whole appeal, and every plank is a different "
    "age, density and moisture content. For a garden fence that hardly matters. "
    "For anything that has to be certified, every plank has to be measured "
    "first, and the measuring costs more than the timber ever did."
)

WHY_IT_MATTERS = (
    "These materials do things that synthetic ones do badly. Alginate forms a "
    "gel on contact with the calcium in wound fluid, which is why alginate "
    "dressings conform to a wound and lift off without tearing new tissue. "
    "Chitosan stops bleeding by a mechanism that does not depend on the "
    "patient's own clotting, which matters for trauma care and for patients on "
    "anticoagulants. Coral skeleton has a pore structure close enough to human "
    "cancellous bone to be used as a graft substitute. Agarose underpins "
    "molecular biology. Marine collagen avoids the mammalian sourcing that "
    "raises both disease and religious objections. And nearly all of it starts "
    "as waste that somebody was paying to dispose of, which makes this one of "
    "the clearest cases of valorisation in the library. The limits are real. "
    "Batch variability is severe enough to block regulated applications, and "
    "the standards that would fix it are largely absent. Marine collagen has "
    "lower thermal stability than mammalian collagen, which restricts where it "
    "can be used. Shellfish-derived materials carry an allergen question that "
    "is unresolved in the literature and treated conservatively in practice. "
    "Extraction of chitin is chemically harsh and generates its own waste "
    "stream, so the environmental case is not automatic. And coral harvesting "
    "for bone graft is unacceptable at any scale that would matter, which is "
    "why the synthetic route replaced it."
)
