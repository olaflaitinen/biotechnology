# =============================================================================
#  biotechnology.branches.yellow
# -----------------------------------------------------------------------------
#  YELLOW BIOTECHNOLOGY - food production, fermentation and nutrition.
#
#  WHAT THIS PACKAGE DOES
#  It imports the nine subtype packages beside it and assembles `BRANCH`.
#  Branch-level material only lives here; the substance is in the packages.
#
#  ORDER OF SUBTYPES
#  The order runs from transforming food, through replacing parts of it, to
#  protecting it and finally to what it does inside a person:
#
#      1. transform it   food_fermentation, precision_fermentation
#      2. replace it     alternative_proteins, cultivated_meat
#      3. live in it     probiotics_and_prebiotics
#      4. protect it     food_biopreservation, food_safety_biotechnology
#      5. improve it     biofortification, nutrigenomics
#
#  THE FACT THAT SEPARATES THIS BRANCH FROM EVERY OTHER
#
#      PEOPLE EAT THIS, VOLUNTARILY, EVERY DAY.
#
#  A patient consents to a medicine because they are ill. A farmer buys a seed
#  because it yields. Nobody is obliged to eat anything, so in this branch
#  ACCEPTANCE IS A FIRST-CLASS ENGINEERING CONSTRAINT rather than a
#  communications problem to be solved after the science. A product that is
#  safe, cheap, nutritious and unappealing does not exist commercially, and the
#  history in these records contains several of them.
#
#  That is also why the regulatory burden here is unusually heavy for products
#  that are, in risk terms, unremarkable. Novel food authorisation exists
#  because a population's entire diet is not a place to run an uncontrolled
#  experiment, and it applies with equal weight to a protein that has been
#  eaten for centuries somewhere else.
#
#  THE OLDEST BRANCH, AND IT IS NOT CLOSE
#  Fermented beverages are documented from roughly nine thousand years ago,
#  which is older than writing and probably older than settled agriculture in
#  some regions. Bread, cheese, beer, wine, soy sauce, kimchi and yoghurt are
#  all yellow biotechnology, practised for millennia before anyone knew a
#  microorganism existed. Most of the records here describe science catching up
#  with a craft rather than inventing one.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ...core.enums import Domain
from ...core.models import Branch, Milestone

from . import (
    alternative_proteins,
    biofortification,
    cultivated_meat,
    food_biopreservation,
    food_fermentation,
    food_safety_biotechnology,
    nutrigenomics,
    precision_fermentation,
    probiotics_and_prebiotics,
)

__all__ = ["BRANCH"]


BRANCH = Branch.build(
    key="yellow",
    name="Yellow Biotechnology",
    colour="#F9A825",
    aliases=(
        "food",
        "food biotechnology",
        "nutrition",
        "fermentation",
        "food science",
        "agrifood",
    ),
    # FOOD is the sector. HEALTH covers nutrition, safety and the gut
    # microbiome work. ENVIRONMENT is claimed on land use: livestock occupies
    # most agricultural land for a minority of calories, and the protein
    # records in this branch address that directly.
    domains=(Domain.FOOD, Domain.HEALTH, Domain.ENVIRONMENT),
    summary="Food production, fermentation, nutrition and the safety of what "
    "people eat.",
    description=(
        "Yellow biotechnology applies microbiology, enzymology and genetics to "
        "food: how it is made, what it is made of, how long it lasts, whether "
        "it is safe, and what it does once eaten. It is the oldest branch by a "
        "wide margin, since fermentation was practised for thousands of years "
        "before microorganisms were known to exist, and much of its modern "
        "content is science explaining and then improving a craft rather than "
        "replacing it. Its newer work is more disruptive: proteins made by "
        "fermentation rather than by animals, meat grown from cells, and "
        "detection methods that turned food safety from an outbreak "
        "investigation into a supply chain control. What unites the branch is "
        "a constraint no other colour carries in the same form. Its products "
        "are eaten voluntarily, so consumer acceptance decides commercial "
        "outcomes independently of safety, cost or nutrition, and the "
        "regulatory framework reflects a justified caution about changing what "
        "an entire population consumes."
    ),
    plain_language=(
        "Yellow biotechnology is the science of food. Some of it is very old: "
        "bread, cheese, beer, yoghurt, soy sauce and kimchi are all made by "
        "microbes, and people were doing that for thousands of years before "
        "anyone knew microbes existed. Some of it is very new: making the same "
        "proteins that are in milk without a cow, growing meat from cells "
        "instead of animals, and testing a whole factory's output for "
        "contamination in hours instead of days. And some of it is about you "
        "rather than the food: which bacteria live in your gut, and why the "
        "same diet suits one person and not another."
    ),
    analogy=(
        "Most of this branch is a cook explaining what they were already doing. "
        "The bread rose long before anyone could name the yeast, and knowing "
        "the name did not make the bread. What it made possible was doing it "
        "the same way twice, at scale, without losing a batch, which is a "
        "smaller-sounding achievement and a much larger one."
    ),
    why_it_matters=(
        "Food is the largest thing humans do to the planet and the only "
        "biotechnology everyone participates in daily. Fermentation preserves "
        "food without refrigeration, which still matters to a great many "
        "people. Molecular detection turned food safety from an investigation "
        "conducted after people fell ill into a control exercised before "
        "product ships. Biofortified staple crops address deficiencies that "
        "affect billions and that supplementation has never reached everyone. "
        "And the newer protein technologies address the fact that livestock "
        "occupies most agricultural land while supplying a minority of "
        "calories. The costs are equally specific. Consumer acceptance is a "
        "genuine constraint rather than an obstacle to be educated away, and "
        "several technically excellent products have failed on it. Novel food "
        "authorisation is slow and expensive, which favours incumbents and "
        "delays products whose benefit is real. The most publicised "
        "achievements of the branch, cultivated meat above all, remain far "
        "from the cost and scale their coverage implies. And nutrition science "
        "is genuinely difficult: the field has repeatedly promised "
        "personalisation on evidence that did not support it, which is "
        "recorded in these pages rather than passed over."
    ),
    origin_note=(
        "Yellow is the least stable of the ten colour labels. In the scheme "
        "this library follows it denotes food and nutrition, and in a "
        "substantial body of other literature it denotes INSECT "
        "biotechnology, with food sometimes assigned to green or orange "
        "instead. The collision is real and unresolved, and a reader arriving "
        "from a source using the other convention should know that this "
        "library takes the food reading, which is the more common one in "
        "European usage."
    ),
    key_questions=(
        "When is a food novel enough to need authorisation before sale?",
        "Should a protein be labelled by what it is or by how it was made?",
        "Can protein be supplied without the land livestock currently uses?",
        "What does the evidence actually support about personalised nutrition?",
        "Who decides whether a traditional fermented food may be industrialised?",
    ),
    milestones=(
        Milestone(-7000, "Fermented beverages are produced, predating writing "
                         "and much of settled agriculture"),
        Milestone(1857, "Pasteur establishes that fermentation is caused by "
                        "living microorganisms"),
        Milestone(1881, "Pure culture technique makes defined starter cultures "
                        "possible"),
        Milestone(1907, "Lactic acid bacteria are proposed as beneficial to "
                        "health, the origin of the probiotic idea"),
        Milestone(1990, "Fermentation-produced chymosin becomes the first "
                        "recombinant enzyme widely accepted in the food chain"),
        Milestone(1997, "Novel food authorisation is established in European "
                        "law, making prior approval the rule for unfamiliar "
                        "foods"),
        Milestone(2013, "The first cultivated meat burger is presented "
                        "publicly"),
        Milestone(2020, "Precision fermentation dairy proteins reach the "
                        "market without an animal in the process"),
    ),
    sdgs=(2, 3, 12, 13),
    references=(
        "fao_food_systems_report",
        "novel_food_regulation_eu",
        "fermented_foods_review",
    ),
    subtypes=(
        # -- transform it ------------------------------------------------------
        food_fermentation.SUBTYPE,
        precision_fermentation.SUBTYPE,
        # -- replace it --------------------------------------------------------
        alternative_proteins.SUBTYPE,
        cultivated_meat.SUBTYPE,
        # -- live in it --------------------------------------------------------
        probiotics_and_prebiotics.SUBTYPE,
        # -- protect it --------------------------------------------------------
        food_biopreservation.SUBTYPE,
        food_safety_biotechnology.SUBTYPE,
        # -- improve it --------------------------------------------------------
        biofortification.SUBTYPE,
        nutrigenomics.SUBTYPE,
    ),
)
