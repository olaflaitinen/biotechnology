# =============================================================================
#  biotechnology.branches.white
# -----------------------------------------------------------------------------
#  WHITE BIOTECHNOLOGY - industrial processes, materials, fuels and chemicals.
#
#  WHAT THIS PACKAGE DOES
#  It imports the nine subtype packages beside it and assembles `BRANCH`.
#  Branch-level material only lives here; the substance is in the packages.
#
#  ORDER OF SUBTYPES
#  The order follows the production chain, because that is how the field is
#  actually taught and how a plant is actually built:
#
#      1. the catalyst      industrial_enzymes, biocatalysis
#      2. the organism      metabolic_engineering
#      3. the process       microbial_fermentation, bioprocess_engineering
#      4. the products      biofuels, biobased_chemicals, biopolymers
#      5. the alternative   cell_free_biomanufacturing, which removes the cell
#
#  Reading them in this order takes a reader from a single protein to a
#  finished tonne of material. Reading them alphabetically does not.
#
#  WHY THE COLOUR IS ALMOST WHITE
#  The colour token below is a very light grey rather than pure white, because
#  a pure white swatch is invisible against a white page. This is the only
#  branch in the library where `Branch.prefers_dark_text` returns True, and
#  `core/models.py` documents that method with this branch as its example.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ...core.enums import Domain
from ...core.models import Branch, Milestone

from . import (
    biobased_chemicals,
    biocatalysis,
    biofuels,
    biopolymers,
    bioprocess_engineering,
    cell_free_biomanufacturing,
    industrial_enzymes,
    metabolic_engineering,
    microbial_fermentation,
)

__all__ = ["BRANCH"]


BRANCH = Branch.build(
    key="white",
    name="White Biotechnology",
    # A very light grey. See the note above on why this is not #FFFFFF.
    colour="#ECEFF1",
    aliases=(
        "industrial",
        "industrial biotechnology",
        "bioprocessing",
        "biomanufacturing",
        "bioeconomy",
        "grey industrial",
    ),
    domains=(Domain.INDUSTRY, Domain.ENERGY, Domain.ENVIRONMENT),
    summary="Industrial processes, biofuels, biomaterials and biobased chemicals.",
    description=(
        "White biotechnology uses enzymes and whole cells as manufacturing "
        "equipment, in place of the high temperatures, high pressures, "
        "organic solvents and rare-metal catalysts of conventional chemical "
        "processing. A biological catalyst works in water, near room "
        "temperature and near neutral pH, and it is selective enough that it "
        "usually produces one product rather than a mixture requiring "
        "separation. Those three properties are the whole economic case for "
        "the branch: less energy, less solvent, fewer purification steps. "
        "Its scope runs from a single purified enzyme in a washing powder, "
        "through engineered strains producing amino acids and vitamins at "
        "hundreds of thousands of tonnes a year, to fuels and polymers made "
        "from plant material rather than petroleum. The branch competes "
        "directly with a mature petrochemical industry that has had a century "
        "to optimise its costs, and that competition, rather than any "
        "biological limit, is what decides which biobased processes exist."
    ),
    plain_language=(
        "White biotechnology is using living things, or parts of them, as "
        "factory machinery. The enzymes in washing powder that let clothes "
        "come clean at 30 degrees instead of 60 are the everyday example, and "
        "they save an enormous amount of electricity. The same idea makes "
        "vitamins, plastics that come from plants rather than oil, fuel from "
        "crop waste, and many of the ingredients in medicines. The appeal is "
        "simple: living things build complicated molecules in warm water, "
        "while a chemical plant usually needs great heat, high pressure and "
        "solvents that have to be disposed of afterwards."
    ),
    analogy=(
        "A chemical plant is a sledgehammer and a biological process is a "
        "locksmith. The sledgehammer is faster and works on anything, but it "
        "breaks things you wanted to keep and leaves a mess to clear up. The "
        "locksmith opens exactly the one lock, quietly, at room temperature, "
        "and leaves the rest of the door intact. The catch is that the "
        "locksmith has to be trained for each new lock, which is why a "
        "biological process is usually slower to develop and cheaper to run."
    ),
    why_it_matters=(
        "Industry accounts for a large share of global energy use and "
        "greenhouse gas emissions, and most industrial chemistry is still "
        "built on petroleum feedstocks. White biotechnology is the main route "
        "by which chemical manufacturing can use plant material and waste "
        "streams instead, and by which processes can run at ambient "
        "conditions rather than at several hundred degrees. Detergent enzymes "
        "alone are estimated to avoid a substantial quantity of emissions "
        "every year simply by allowing lower wash temperatures. The honest "
        "counterweight is that biobased is not automatically better: a "
        "biopolymer that requires farmland, fertiliser and irrigation can "
        "carry a larger footprint than the petroleum plastic it replaces, "
        "and only a full life cycle assessment settles the question. This "
        "branch records that tension in its metrics rather than assuming the "
        "answer."
    ),
    origin_note=(
        "White entered use alongside red and green in European bioeconomy "
        "policy writing in the late 1990s, chosen for industry by analogy "
        "with the white coats of a process laboratory rather than for any "
        "property of the processes themselves. It is the least intuitive of "
        "the ten colour labels, and in some older literature industrial "
        "biotechnology is called grey, which now denotes environmental "
        "biotechnology instead. That collision is why `grey industrial` "
        "appears in this branch's aliases."
    ),
    key_questions=(
        "When does a biological process actually beat a chemical one on cost?",
        "Is a biobased product genuinely lower impact, or only lower carbon "
        "at the point of use?",
        "How is a process that works in a two-litre flask made to work in a "
        "two-hundred-cubic-metre vessel?",
        "Should feedstock come from food crops, from residues, or from carbon "
        "dioxide directly?",
        "What happens to a biodegradable material that is never actually "
        "composted?",
    ),
    milestones=(
        Milestone(1833, "Payen and Persoz isolate diastase, the first enzyme "
                        "preparation obtained from a living source"),
        Milestone(1897, "Buchner shows that cell-free yeast extract still "
                        "ferments sugar, separating biochemistry from vitalism"),
        Milestone(1916, "Weizmann develops acetone-butanol fermentation, the "
                        "first large industrial fermentation process"),
        Milestone(1941, "Submerged deep-tank fermentation is developed for "
                        "penicillin and becomes the template for the industry"),
        Milestone(1974, "Bacterial proteases become standard in laundry "
                        "detergents, the largest enzyme market by volume"),
        Milestone(1993, "Directed evolution is demonstrated, allowing enzymes "
                        "to be improved without understanding their mechanism"),
        Milestone(2004, "The United States Department of Energy publishes its "
                        "list of top value-added chemicals from biomass, which "
                        "sets the field's product agenda for two decades"),
        Milestone(2018, "The Nobel Prize in Chemistry is awarded for directed "
                        "evolution of enzymes and phage display"),
    ),
    sdgs=(7, 9, 12, 13),
    references=(
        "oecd_bioeconomy_2030",
        "doe_top_value_added_chemicals",
        "industrial_biotechnology_review",
    ),
    subtypes=(
        # -- the catalyst ------------------------------------------------------
        industrial_enzymes.SUBTYPE,
        biocatalysis.SUBTYPE,
        # -- the organism ------------------------------------------------------
        metabolic_engineering.SUBTYPE,
        # -- the process -------------------------------------------------------
        microbial_fermentation.SUBTYPE,
        bioprocess_engineering.SUBTYPE,
        # -- the products ------------------------------------------------------
        biofuels.SUBTYPE,
        biobased_chemicals.SUBTYPE,
        biopolymers.SUBTYPE,
        # -- doing it without a cell ------------------------------------------
        cell_free_biomanufacturing.SUBTYPE,
    ),
)
