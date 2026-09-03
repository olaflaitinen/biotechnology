# =============================================================================
#  biotechnology.branches.white.microbial_fermentation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The technical register carries the one counterintuitive fact that organises
#  this whole record: FEEDING A CULTURE FASTER USUALLY PRODUCES LESS.
#
#  Above a critical feed rate a cell switches to overflow metabolism and
#  excretes acetate or ethanol instead of making more biomass or product. The
#  sugar is consumed, the by-product accumulates, it inhibits growth, and the
#  fermentation performs worse than if it had been fed more slowly. Nearly
#  every industrial fermentation is run fed-batch specifically to stay below
#  that threshold, and a reader who understands only this will understand why
#  the industry is shaped the way it is.
#
#  The stove analogy is chosen because it is the everyday system in which
#  adding fuel faster than the air supply produces smoke rather than heat,
#  which is exactly what overflow metabolism is.
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
    "Cultivating microorganisms at industrial scale under controlled and "
    "usually sterile conditions, so that a strain performs in a vessel what it "
    "was engineered to do."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what the operation is and its boundary with the next record,
#  (b) the modes and why fed-batch dominates, (c) the two things that decide
#  whether a campaign succeeds, (d) why continuous operation is rare despite
#  being better on paper.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the operation and its boundary
    "Microbial fermentation is the cultivation step: growing a defined strain "
    "from a preserved vial to a production vessel of tens or hundreds of cubic "
    "metres, feeding it, keeping everything else out, and holding the "
    "conditions that make it produce. It is distinguished from bioprocess "
    "engineering, which designs the equipment and carries the product through "
    "recovery and purification afterwards. This record is about what the "
    "culture does; that one is about what the plant does. "
    # (b) the modes, and why one dominates
    "Four modes are used. Batch is the simplest and is limited by the "
    "inhibition that follows from putting all the substrate in at once. "
    "Fed-batch supplies substrate gradually and dominates industrial practice, "
    "for a reason that is not obvious: above a critical feed rate most "
    "organisms switch to overflow metabolism, excreting acetate or ethanol "
    "rather than converting carbon to product, so feeding faster lowers output. "
    "Controlling the feed to hold specific growth rate below that threshold is "
    "the central operating decision of the field. Continuous culture holds a "
    "steady state indefinitely by matching dilution rate to growth rate. "
    "Solid-state fermentation grows organisms on a moist solid substrate with "
    "little free water, which suits filamentous fungi and some enzyme "
    "production. "
    # (c) what decides success
    "Two things decide whether a campaign succeeds, and neither is the strain. "
    "The first is sterility. A production vessel is a rich, warm, well-mixed "
    "nutrient broth, which is to say an excellent growth medium for whatever "
    "arrives first, and a contaminant with a shorter doubling time will "
    "outgrow the production organism within hours. Sterilisation of the vessel, "
    "the medium, the air and every addition is therefore not a precaution but "
    "the process itself. The second is oxygen. Aerobic fermentation consumes "
    "oxygen far faster than it dissolves, oxygen transfer does not improve with "
    "vessel size, and in most large aerobic processes the real ceiling on "
    "productivity is set by the vessel rather than by the organism. "
    # (d) the honest anomaly
    "Continuous culture is more productive per unit of capital and is used "
    "very little. The reasons are practical rather than theoretical: a long "
    "run gives contamination more opportunities, selection favours any mutant "
    "that stops making the product, and a regulated product is defined by "
    "batch, which a process without batches does not naturally provide. This "
    "record treats that gap between the theoretically better option and the "
    "commonly chosen one as a finding rather than an embarrassment."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Fermentation is growing microbes on purpose, in a tank, to make "
    "something. It is how penicillin is made, how vitamins and food "
    "ingredients are made, and how most of the enzymes and biological "
    "medicines in use today are made. The engineering is mostly about three "
    "unglamorous problems. Keeping everything else out, because a tank of warm "
    "nutrient broth is exactly what every other microbe in the world would "
    "like. Getting enough air in, because a dense culture uses oxygen far "
    "faster than it can dissolve. And feeding at the right speed, because "
    "feeding a culture too fast makes it waste the food rather than grow "
    "faster."
)

# -----------------------------------------------------------------------------
#  The stove analogy. The point of it is the third sentence: fuel added faster
#  than the air supply gives smoke rather than heat, which is precisely what
#  overflow metabolism is. The sterility half of the record is carried by the
#  final sentence.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is tending a stove rather than filling a tank. A tank simply takes "
    "whatever you pour into it. A stove has an air supply, and fuel piled on "
    "faster than the air can support it does not burn hotter, it smoulders and "
    "makes smoke. So the skill is in matching the feed to the draught, "
    "continuously, for days. And the fire is in a room where every other spark "
    "in the neighbourhood would happily take over, so the door stays shut."
)

WHY_IT_MATTERS = (
    "Almost every product in this branch reaches the world through a "
    "fermenter. Antibiotics, insulin and most therapeutic proteins, the "
    "industrial enzymes in detergent and feed, the amino acids and vitamins "
    "that go into animal nutrition, citric acid, and the newer proteins made "
    "without animals all depend on this one operation. It is also where a great "
    "deal of a plant's cost sits: sterilisation consumes energy and time, "
    "aeration and agitation consume power continuously, and a contaminated "
    "batch is a complete loss of everything that went into it, including the "
    "days it occupied the vessel. Two structural limits deserve stating "
    "plainly. Oxygen transfer does not scale with volume, so a strain that "
    "performs beautifully in a shake flask can disappoint in a large vessel for "
    "reasons that have nothing to do with its biology. And feedstock, usually "
    "sugar or starch, competes with food and land, which is why gas and "
    "one-carbon feedstocks are being pursued despite being harder. The oldest "
    "cautionary tale in the field is a warning about the second of those: a "
    "single cell protein process that worked technically and was defeated by "
    "the price of soy."
)
