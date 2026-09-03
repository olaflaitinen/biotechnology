# =============================================================================
#  biotechnology.branches.blue
# -----------------------------------------------------------------------------
#  BLUE BIOTECHNOLOGY - marine and aquatic organisms, and the sea as a resource.
#
#  WHAT THIS PACKAGE DOES
#  It imports the eight subtype packages beside it and assembles `BRANCH`.
#  Branch-level material only lives here; the substance is in the packages.
#
#  ORDER OF SUBTYPES
#  The order follows what a practitioner actually does, from reading the sea to
#  protecting what is put into it:
#
#      1. read it        marine_genomics
#      2. find molecules marine_natural_products, marine_enzymes
#      3. grow it        algal_biotechnology, seaweed_cultivation,
#                        aquaculture_biotechnology
#      4. build with it  marine_biomaterials
#      5. defend against it  marine_biofouling_control
#
#  The last is not an afterthought. Everything humans put in the sea is
#  colonised within hours, and preventing that is a large industry in its own
#  right.
#
#  THE TWO FACTS THAT SHAPE THE WHOLE BRANCH
#
#  FIRST, MARINE CHEMISTRY IS POTENT BECAUSE WATER DILUTES. A sessile animal
#  defending itself on a reef releases its chemistry into an ocean that
#  immediately disperses it. Anything that works at all must work at very low
#  concentration. That is the same property a drug needs, and it is why the sea
#  has produced pharmacologically active molecules far out of proportion to how
#  little of it has been sampled.
#
#  SECOND, SUPPLY IS THE BRANCH'S SIGNATURE CONSTRAINT. The interesting
#  molecules are made in vanishing quantities by animals that cannot be farmed.
#  One anticancer compound required roughly a tonne of tunicate for a gram of
#  material; another needed many tonnes of a bryozoan for a few grams. No blue
#  biotechnology product has ever reached a market by harvesting its source
#  organism. Every success arrived by synthesis, semisynthesis, fermentation of
#  the symbiont that actually makes the compound, or an analogue. A reader who
#  takes one idea from this branch should take that one.
#
#  THE GOVERNANCE PROBLEM THAT BELONGS TO NO OTHER BRANCH
#  Roughly two thirds of the ocean lies beyond any national jurisdiction, so
#  for most of the sea there was until recently no legal answer to the question
#  of who owns a gene sequenced from it. The 2023 agreement on marine
#  biological diversity of areas beyond national jurisdiction is the first
#  instrument to address that directly, and every governance facet in this
#  branch has to engage with it.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ...core.enums import Domain
from ...core.models import Branch, Milestone

from . import (
    algal_biotechnology,
    aquaculture_biotechnology,
    marine_biofouling_control,
    marine_biomaterials,
    marine_enzymes,
    marine_genomics,
    marine_natural_products,
    seaweed_cultivation,
)

__all__ = ["BRANCH"]


BRANCH = Branch.build(
    key="blue",
    name="Blue Biotechnology",
    colour="#1565C0",
    aliases=(
        "marine",
        "marine biotechnology",
        "aquatic",
        "ocean",
        "blue economy",
        "marine bioprospecting",
    ),
    domains=(Domain.HEALTH, Domain.FOOD, Domain.MATERIALS),
    summary="Marine and aquatic organisms as sources of medicines, materials, "
    "enzymes and food.",
    description=(
        "Blue biotechnology applies molecular and cultivation techniques to "
        "marine and aquatic organisms. Its scientific case rests on novelty: "
        "several animal phyla exist only in the sea, marine habitats include "
        "conditions found nowhere on land, and the resulting chemistry and "
        "enzymology have no terrestrial equivalent. Its commercial case is "
        "harder, and the constraint is almost always supply rather than "
        "discovery. Interesting molecules are produced in minute quantities by "
        "organisms that cannot be farmed, so a compound that works in a "
        "laboratory may be unobtainable at the scale a medicine requires. "
        "Every marine-derived drug in clinical use reached the market by "
        "synthesis, semisynthesis, fermentation of a symbiont, or as a "
        "simplified analogue, and none by harvesting. The branch also carries a "
        "legal problem that belongs to no other colour: most of the ocean lies "
        "outside any national jurisdiction, so ownership of a sequence taken "
        "from it was unresolved until very recently."
    ),
    plain_language=(
        "Blue biotechnology is using life from the sea. The oceans hold kinds "
        "of animal that exist nowhere on land, and creatures living in places "
        "that would kill anything else: boiling water at volcanic vents, "
        "freezing water under polar ice, crushing pressure in the deep. Because "
        "these organisms had to solve different problems, they make chemicals "
        "and enzymes we would never have invented. Some are already medicines. "
        "Others clean up oil, keep food fresh, or make ice cream smooth. The "
        "hard part is rarely finding something useful. It is getting enough of "
        "it, because you cannot farm a deep-sea sponge."
    ),
    analogy=(
        "The sea is not a larger version of the land. It is a different "
        "library, in a language that developed separately, and most of it has "
        "never been read. That is why the small fraction anyone has looked at "
        "has produced so much: not because the sea is generous, but because it "
        "is unfamiliar."
    ),
    why_it_matters=(
        "The ocean covers most of the planet and holds most of its living "
        "space, and it is by far the least sampled part of the biosphere. "
        "Several important medicines came from it, including a pain treatment "
        "derived from a cone snail toxin for patients who respond to nothing "
        "else, and cancer treatments whose chemistry was found in a sea squirt "
        "and a sponge. The green fluorescent protein that made modern cell "
        "biology visible came from a jellyfish. Seaweed farming feeds millions "
        "and needs no land, no fresh water and no fertiliser. The costs are "
        "equally real. Bioprospecting has damaged the habitats it sampled. "
        "Aquaculture has spread disease to wild populations and depends on "
        "fishmeal drawn from stocks that are themselves under pressure. And "
        "the governance question of who owns a gene taken from the high seas, "
        "where no state has jurisdiction, went unanswered for decades while "
        "sequences were collected and patented."
    ),
    origin_note=(
        "Blue entered the colour scheme in European marine science policy in "
        "the early 2000s, later than red and green, and is sometimes used more "
        "narrowly than here to mean marine bioprospecting alone. This library "
        "takes the wider reading, covering aquaculture, algae and marine "
        "materials as well, because the narrower one leaves those with no "
        "colour at all."
    ),
    key_questions=(
        "Who owns a gene sequenced from water that belongs to no country?",
        "How is a molecule supplied at scale when its source cannot be farmed?",
        "Can aquaculture grow without drawing more from wild fish stocks?",
        "What does sampling cost the habitat it samples?",
        "Which marine capability has no terrestrial substitute at all?",
    ),
    milestones=(
        Milestone(1951, "Unusual nucleosides isolated from a Caribbean sponge "
                        "provide the template for the first antiviral and "
                        "anticancer drugs of marine origin"),
        Milestone(1962, "Green fluorescent protein is isolated from a "
                        "jellyfish"),
        Milestone(1969, "Cytarabine, developed from marine sponge nucleoside "
                        "chemistry, is approved for leukaemia"),
        Milestone(1977, "Hydrothermal vent ecosystems are discovered, and with "
                        "them communities independent of sunlight"),
        Milestone(1991, "A thermostable polymerase from a deep-sea "
                        "hyperthermophile enters routine laboratory use"),
        Milestone(2004, "Ziconotide, derived from a cone snail venom peptide, "
                        "is approved for severe chronic pain"),
        Milestone(2007, "Trabectedin, from a Caribbean tunicate and supplied by "
                        "semisynthesis, is approved in Europe"),
        Milestone(2023, "An international agreement on marine biological "
                        "diversity beyond national jurisdiction addresses "
                        "marine genetic resources for the first time"),
    ),
    sdgs=(2, 3, 9, 14),
    references=(
        "marine_natural_products_review",
        "bbnj_agreement",
        "fao_aquaculture_report",
    ),
    subtypes=(
        # -- read it -----------------------------------------------------------
        marine_genomics.SUBTYPE,
        # -- find molecules and catalysts --------------------------------------
        marine_natural_products.SUBTYPE,
        marine_enzymes.SUBTYPE,
        # -- grow it -----------------------------------------------------------
        algal_biotechnology.SUBTYPE,
        seaweed_cultivation.SUBTYPE,
        aquaculture_biotechnology.SUBTYPE,
        # -- build with it -----------------------------------------------------
        marine_biomaterials.SUBTYPE,
        # -- defend against it -------------------------------------------------
        marine_biofouling_control.SUBTYPE,
    ),
)
