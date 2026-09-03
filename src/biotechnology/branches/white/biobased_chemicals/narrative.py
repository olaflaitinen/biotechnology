# =============================================================================
#  biotechnology.branches.white.biobased_chemicals.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has one genuinely explanatory principle, and putting it in the
#  narrative rather than burying it in the metrics is the most useful editorial
#  decision available here.
#
#  SUGAR IS ALREADY OXYGENATED. PETROLEUM IS NOT.
#
#  Glucose has roughly one oxygen per carbon. A hydrocarbon has none. So a
#  petrochemical route to an oxygen-rich molecule such as a diacid or a diol
#  must ADD oxygen through several selective oxidation steps, each with its own
#  yield loss, catalyst and separation. A biological route to the same molecule
#  starts most of the way there. Conversely, making a pure hydrocarbon from
#  sugar means REMOVING oxygen that the feedstock is full of, which wastes
#  carbon as carbon dioxide and energy as heat.
#
#  That single asymmetry predicts, with remarkable accuracy, which biobased
#  chemicals succeeded commercially and which did not. It is why this record
#  reads more positively than `white.biofuels` while using the same feedstocks
#  and the same organisms: a fuel is a hydrocarbon, and a hydrocarbon is the
#  worst possible target for a route that begins with sugar.
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
    "Producing bulk and speciality chemicals from biological feedstocks in "
    "place of petroleum, by fermentation and catalytic upgrading."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the field and the oxygen principle, (b) the two market
#  strategies, (c) the platform chemical idea, (d) what actually decides
#  whether a molecule is made this way.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the principle
    "Biobased chemicals are the molecules of the chemical industry made from "
    "sugars, oils, residues and gases rather than from petroleum. The field's "
    "structural advantage follows from a single property of its feedstock: "
    "biomass is highly oxygenated, with roughly one oxygen per carbon in "
    "glucose, whereas petroleum has essentially none. Producing an "
    "oxygen-containing molecule such as a diacid, a diol or a hydroxy acid "
    "therefore requires several selective oxidation steps from petroleum and "
    "very few from sugar. Producing a pure hydrocarbon requires the reverse, "
    "and stripping oxygen from sugar wastes carbon as carbon dioxide. Which "
    "biobased chemicals have succeeded is largely predicted by this asymmetry. "
    # (b) the two strategies
    "Two market strategies exist and they fail differently. A drop-in product "
    "is chemically identical to its petrochemical equivalent, so it needs no "
    "requalification and can enter an existing supply chain immediately, but it "
    "competes purely on price against an incumbent with a century of "
    "optimisation and no performance premium to offer. A novel molecule offers "
    "properties the petrochemical range cannot match and must create its own "
    "market, qualify with every downstream user and wait years for adoption. "
    "The successes in this record are mostly the second kind, or the first kind "
    "where the oxygen asymmetry gave a genuine cost advantage rather than "
    "parity. "
    # (c) platform chemicals
    "Much of the field is organised around platform chemicals: a small set of "
    "building blocks from which many products can be derived, so that "
    "investment in one fermentation supports a family of downstream molecules. "
    "Published lists of priority platforms have shaped research funding for "
    "two decades. They have also proved a poor predictor of commercial "
    "outcome, because a molecule can be an excellent chemical platform and a "
    "poor business if nobody has built the downstream capacity to consume it. "
    # (d) what decides
    "What decides in practice is rarely the fermentation. It is feedstock cost "
    "against oil price, the capital intensity of a plant that must be built "
    "before any revenue exists, the separation cost of recovering a dilute "
    "product from an aqueous broth, and whether a customer will pay anything at "
    "all for the biobased attribute. The last of these is a market question "
    "rather than a technical one, and it has ended more projects than any "
    "titre."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Almost everything manufactured passes through the chemical industry: "
    "plastics, paints, solvents, detergents, fibres, adhesives, coatings. "
    "Nearly all of it currently starts from oil. Biobased chemicals make the "
    "same substances from plants, sugar or waste instead. This works better "
    "than making fuel from plants, for a reason that is easy to state: sugar "
    "already contains a lot of oxygen, and many useful chemicals need oxygen "
    "in them, whereas fuels need it removed. So biology starts closer to the "
    "chemical than to the fuel. Chemicals are also worth far more per tonne "
    "than fuel is, so a smaller amount of farmland goes much further."
)

# -----------------------------------------------------------------------------
#  The half-built analogy. It carries the oxygen principle in ordinary language
#  without requiring any chemistry, and its second half carries the reverse
#  case, which is what distinguishes this record from `white.biofuels`.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Petroleum is a pile of identical plain bricks and sugar is a pile of "
    "parts that already have fittings attached. If you want a plain wall, the "
    "bricks are better and the fittings only get in the way. If you want "
    "something with plumbing in it, the parts that already have fittings save "
    "you most of the work. Fuel is the plain wall. Most chemicals are not."
)

WHY_IT_MATTERS = (
    "The chemical industry is one of the largest industrial consumers of "
    "energy and fossil feedstock, and unlike electricity generation it cannot "
    "be decarbonised by changing the power supply, because the carbon in a "
    "plastic is the product rather than the fuel. A carbon atom that ends up in "
    "a material has to come from somewhere, and biomass, waste and carbon "
    "dioxide are the alternatives to a well. Chemicals are also a far better "
    "match for biomass than fuels are: they account for a much smaller share "
    "of petroleum use and are worth several times more per tonne, so the same "
    "hectare of land displaces a great deal more fossil carbon when it makes a "
    "chemical than when it makes a fuel. Some of the field's products are "
    "genuinely better rather than merely greener, with fibres and polymers "
    "whose properties the petrochemical range does not match. The failures are "
    "equally instructive and are recorded here rather than passed over. "
    "Succinic acid was named a priority platform chemical, attracted at least "
    "four companies and several commercial plants, and most of them had exited "
    "or failed within a decade, because the downstream demand that the platform "
    "logic assumed did not materialise. Biobased does not automatically mean "
    "lower impact either: a route that needs more energy, more land or more "
    "processing can carry a larger footprint than the petrochemical one it "
    "replaces, and only a full life cycle assessment settles it."
)
