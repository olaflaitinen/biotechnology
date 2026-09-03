# =============================================================================
#  biotechnology.branches.white.biopolymers.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record exists to correct one confusion, and the correction is placed in
#  the first sentences of both registers because almost everything else in the
#  subject depends on it.
#
#  BIOBASED AND BIODEGRADABLE ARE INDEPENDENT PROPERTIES. One describes where
#  the carbon came from. The other describes what happens at the end. All four
#  combinations exist and are manufactured at scale:
#
#                          biodegradable        not biodegradable
#      biobased            PLA, PHA, starch     bio-PE, bio-PET
#      fossil              PBAT, PCL            conventional plastics
#
#  A bio-based polyethylene bottle is chemically identical to a fossil one and
#  persists exactly as long. A compostable film may be made entirely from
#  petroleum. Treating the two words as synonyms is the single most common
#  error in public discussion of this subject, and it leads directly to the
#  second error, which is thinking "biodegradable" means something on its own.
#
#  IT DOES NOT. Biodegradation is a rate, in a stated environment, at a stated
#  temperature. A polymer certified for industrial composting at 58 degrees
#  behaves like an ordinary plastic in a hedgerow, a landfill or the sea.
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
    "Polymers produced from biological feedstocks or by living organisms, "
    "including both durable biobased plastics and compostable materials."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the two independent axes, (b) the three routes to a
#  biopolymer, (c) why biodegradation is a rate rather than a property,
#  (d) the constraint that is not chemical at all.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the two axes
    "Biopolymers are conventionally discussed as one category and are properly "
    "described by two independent axes. Biobased content states what fraction "
    "of the carbon was recently fixed rather than extracted, and is measurable "
    "on the finished article by radiocarbon. Biodegradability states whether, "
    "and how quickly, microorganisms will mineralise the material to carbon "
    "dioxide, water and biomass under specified conditions. Neither implies the "
    "other. Bio-based polyethylene is fully biobased and as persistent as any "
    "plastic; several certified compostable polyesters are made entirely from "
    "fossil feedstock. "
    # (b) the routes
    "Three routes produce them. The first polymerises a biobased monomer, as "
    "polylactic acid is made from fermented lactic acid, which places this "
    "record immediately downstream of `white.biobased_chemicals`. The second "
    "harvests a polymer the organism makes itself: polyhydroxyalkanoates are "
    "carbon storage granules accumulated inside bacterial cells, so the "
    "polymerisation is biological and the difficulty moves to extraction. The "
    "third modifies a natural polymer that already exists, as with regenerated "
    "cellulose, starch blends, chitosan and alginate. "
    # (c) biodegradation is a rate
    "Biodegradation is not a property of a material but a rate in an "
    "environment. Polylactic acid requires the sustained temperature and "
    "humidity of industrial composting to hydrolyse at a useful rate; in soil, "
    "in home compost or in seawater it persists for a long time. "
    "Polyhydroxyalkanoates degrade in ambient and marine conditions because "
    "they are natural bacterial products and environmental organisms already "
    "possess the depolymerases. A claim of biodegradability that does not name "
    "the environment, the temperature and the timeframe conveys no information. "
    # (d) the real constraint
    "The binding constraint on compostable materials is not polymer chemistry. "
    "It is collection. A material certified for industrial composting requires "
    "an industrial composter that will accept it, and where that "
    "infrastructure is absent the article behaves as ordinary plastic while "
    "also contaminating the recycling stream it visually resembles. In such "
    "places a compostable package can be worse than the conventional one it "
    "replaced, which is a waste management conclusion rather than a materials "
    "science one."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "There are two different things people mean by a green plastic, and mixing "
    "them up causes most of the confusion. The first is what it is MADE FROM: "
    "plants instead of oil. The second is what happens to it AFTERWARDS: "
    "whether living things can break it down. These are separate. You can have "
    "a plastic made entirely from sugarcane that lasts for centuries, and a "
    "plastic made entirely from oil that composts in weeks. Both are sold "
    "today. And breaking down is not a yes or no answer either: most "
    "compostable packaging needs a large heated industrial composter, and in an "
    "ordinary bin, a field or the sea it behaves much like any other plastic."
)

# -----------------------------------------------------------------------------
#  The firewood analogy. Chosen because it carries the environment-dependence
#  of biodegradation, which is the harder of the two ideas, in a way that
#  requires no chemistry and cannot be misread as an argument against the
#  materials themselves.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Saying a plastic is biodegradable is like saying a log is burnable. It is "
    "true, and it tells you nothing about whether it will burn in the "
    "conditions you actually have. A log burns in a hot stove with a good "
    "draught. The same log in a damp field does not burn at all; it just sits "
    "there for years. The honest question is never whether a material can "
    "break down, but whether it will break down where it is actually going to "
    "end up."
)

WHY_IT_MATTERS = (
    "Plastics are among the largest single uses of fossil carbon that cannot be "
    "addressed by cleaning up electricity, because the carbon in a polymer is "
    "the product rather than the fuel. Biobased polymers move that carbon from "
    "a well to a field, and because it stays in the material rather than being "
    "burned, the displacement is durable. Compostable materials solve a "
    "genuinely different problem: not the feedstock, but the items that cannot "
    "practically be recycled because they are contaminated with food, such as "
    "caddy liners, agricultural mulch films and food service ware. Those are "
    "real applications with real benefits. The costs and the failures are "
    "equally real and this record does not soften them. Oxo-degradable "
    "additives were marketed for years as making plastic degradable and were "
    "eventually restricted because they fragment material into microplastics "
    "rather than mineralising it. Compostable packaging without industrial "
    "composting access contaminates recycling streams and reaches landfill "
    "anyway. And most biopolymers cost more, perform less well in barrier or "
    "heat resistance, and compete against a fossil incumbent whose plants are "
    "long since paid for. A biobased polymer is also not automatically lower "
    "impact: agricultural feedstock carries land, water and fertiliser burdens "
    "that only a full life cycle assessment can weigh against the fossil route "
    "it replaces."
)
