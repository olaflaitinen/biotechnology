# =============================================================================
#  biotechnology.branches.green
# -----------------------------------------------------------------------------
#  GREEN BIOTECHNOLOGY - agriculture, livestock and primary food production.
#
#  WHAT THIS PACKAGE DOES
#  It imports the eight subtype modules beside it and assembles `BRANCH`.
#  Branch-level material only lives here; the substance is in the modules.
#
#  ORDER OF SUBTYPES
#  Plant material first (engineering, editing, breeding, propagation), then
#  the inputs applied to the field (fertility, protection), then the animal
#  side. This mirrors how an agronomy curriculum is usually taught.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ...core.enums import Domain
from ...core.models import Branch, Milestone

from . import (
    agricultural_genome_editing,
    animal_biotechnology,
    biofertilisers,
    biopesticides,
    molecular_plant_breeding,
    plant_genetic_engineering,
    plant_tissue_culture,
    veterinary_vaccines,
)

__all__ = ["BRANCH"]


BRANCH = Branch.build(
    key="green",
    name="Green Biotechnology",
    colour="#2E7D32",
    aliases=("agriculture", "agricultural", "plant", "farming", "livestock", "agri"),
    domains=(Domain.FOOD, Domain.ENVIRONMENT),
    summary="Agriculture, livestock and crop production.",
    description=(
        "Green biotechnology applies molecular, cellular and reproductive "
        "tools to plants, farm animals and the soil ecosystem. Its objectives "
        "are to raise yield per hectare, improve nutritional quality, reduce "
        "chemical inputs, and build resilience to pests, disease and climate "
        "stress. It is the branch with the widest public visibility and the "
        "most divergent regulation between jurisdictions: the same edited "
        "plant may be an unregulated conventional variety on one side of a "
        "border and a genetically modified organism on the other."
    ),
    plain_language=(
        "Green biotechnology is biotechnology used to grow food. It covers "
        "making crops resistant to insects so they need less spraying, "
        "breeding faster by reading a seedling's DNA instead of waiting a "
        "season, growing thousands of identical disease-free plants from a "
        "single healthy one, using helpful soil microbes instead of some "
        "synthetic fertiliser, and keeping farm animals healthier through "
        "better breeding and vaccination."
    ),
    analogy=(
        "Farming has always been biotechnology - every wheat field is the "
        "result of ten thousand years of deliberate genetic modification by "
        "selection. The modern branch simply reads the instructions instead of "
        "working blind, which makes the same process faster and more precise "
        "rather than different in kind."
    ),
    why_it_matters=(
        "Roughly ten billion people will need feeding by mid-century from "
        "farmland that cannot expand without destroying what remains of the "
        "world's forests, using less water and less nitrogen, under a climate "
        "that is shifting faster than traditional variety development can "
        "follow. Every subtype in this branch is a partial answer to that "
        "arithmetic, and none of them is sufficient alone."
    ),
    origin_note=(
        "Green is the oldest of the colour labels alongside red, and entered "
        "wide use during the European debate over genetically modified food in "
        "the late 1990s. The colour refers to plants, not to environmental "
        "friendliness, a confusion the term has never quite shaken off."
    ),
    key_questions=(
        "How is yield raised without expanding farmland or nitrogen use?",
        "Should an edited plant be regulated differently from a mutagenised one?",
        "Who owns a seed, and what may a farmer do with the harvest?",
        "Can biological inputs replace a meaningful share of agrochemicals?",
        "How is genetic diversity conserved while selecting ever harder?",
    ),
    milestones=(
        Milestone(-9000, "Domestication of wheat, barley and rice begins"),
        Milestone(1866, "Mendel publishes the laws of inheritance"),
        Milestone(1953, "Structure of DNA published"),
        Milestone(1962, "Murashige and Skoog medium standardises plant tissue culture"),
        Milestone(1983, "First transgenic plants produced"),
        Milestone(1996, "Commercial planting of genetically modified crops begins"),
        Milestone(2001, "Genomic selection proposed and later transforms livestock breeding"),
        Milestone(2012, "CRISPR-Cas9 opens routine genome editing in crops and livestock"),
    ),
    sdgs=(2, 12, 13, 15),
    references=("isaaa_brief", "nasem2016", "fao_sofa"),
    subtypes=(
        plant_genetic_engineering.SUBTYPE,
        agricultural_genome_editing.SUBTYPE,
        molecular_plant_breeding.SUBTYPE,
        plant_tissue_culture.SUBTYPE,
        biofertilisers.SUBTYPE,
        biopesticides.SUBTYPE,
        animal_biotechnology.SUBTYPE,
        veterinary_vaccines.SUBTYPE,
    ),
)
