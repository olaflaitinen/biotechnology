# =============================================================================
#  biotechnology.branches.red
# -----------------------------------------------------------------------------
#  RED BIOTECHNOLOGY - medicine, health care and pharmaceuticals.
#
#  WHAT THIS PACKAGE DOES
#  It imports the eight subtype modules that sit beside it and assembles them
#  into a single `BRANCH` object. All of the descriptive weight lives in the
#  subtype modules; this file holds only branch-level material - the identity
#  of the colour, its history, and the questions the field is trying to answer.
#
#  THE ORDER OF `subtypes` BELOW IS THE PUBLISHED ORDER
#  It runs roughly from the manufacture of a medicine, through the newer
#  cell- and gene-based modalities, to the diagnostic and personalisation
#  layers that decide who should receive what. It is a narrative order, not an
#  alphabetical one, because the first thing most readers do is read the list
#  top to bottom.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ...core.enums import Domain
from ...core.models import Branch, Milestone

# -- the eight subtype modules -------------------------------------------------
from . import (
    antibody_engineering,
    cell_therapy,
    gene_therapy,
    molecular_diagnostics,
    pharmaceutical_biotechnology,
    pharmacogenomics,
    regenerative_medicine,
    vaccine_development,
)

__all__ = ["BRANCH"]


BRANCH = Branch.build(
    key="red",
    name="Red Biotechnology",
    # Deep clinical red. Chosen for contrast against the green and blue
    # branches at the same lightness, so that colour-coded figures remain
    # readable for the most common forms of colour vision deficiency.
    colour="#C62828",
    aliases=("medical", "medicine", "health", "pharma", "pharmaceutical", "clinical"),
    domains=(Domain.HEALTH,),
    # -------------------------------------------------------------------------
    #  Technical register
    # -------------------------------------------------------------------------
    summary="Medicine, health care and pharmaceutical applications.",
    description=(
        "Red biotechnology covers every biotechnological application aimed at "
        "human health. It spans the discovery and manufacture of biologic "
        "medicines, the engineering of genes and cells into therapies, the "
        "design and production of vaccines, the molecular diagnosis of disease, "
        "and the tailoring of treatment to an individual patient. It is the "
        "most heavily regulated branch of the field and by a wide margin the "
        "largest in commercial terms. It is also the branch where the gap "
        "between technical possibility and equitable access is widest, which "
        "is why almost every subtype here cross-references the ethical and "
        "regulatory material in the purple branch."
    ),
    # -------------------------------------------------------------------------
    #  Plain-language register
    # -------------------------------------------------------------------------
    plain_language=(
        "Red biotechnology is biotechnology used on people, to keep them well "
        "or to make them better. It includes medicines grown in living cells "
        "instead of mixed in a chemical plant, vaccines, treatments that "
        "correct faulty genes, therapies made from living cells, and the tests "
        "that tell a doctor exactly what is wrong and which treatment will "
        "work. The colour red was chosen simply because it is the colour of "
        "blood, and the name stuck."
    ),
    analogy=(
        "If ordinary medicine is a workshop full of hand tools, red "
        "biotechnology is the part of the workshop where the tools are alive. "
        "The materials grow, repair themselves and occasionally behave in ways "
        "the manual did not predict, which is both the promise and the reason "
        "for the paperwork."
    ),
    why_it_matters=(
        "Roughly half of the best-selling medicines in the world are now made "
        "by living cells rather than by chemical synthesis. Diseases that were "
        "uniformly fatal within living memory - several childhood leukaemias, "
        "haemophilia, some inherited blindness - now have treatments that "
        "address their cause. At the same time, prices in the hundreds of "
        "thousands or millions of euro per patient have made access, not "
        "invention, the central policy question of the branch."
    ),
    origin_note=(
        "The red/green contrast entered European policy language in the late "
        "1990s, when public debate about genetically modified food ran hot and "
        "the medical sector wanted its work considered separately. The other "
        "colours were added afterwards, by analogy."
    ),
    key_questions=(
        "Can a therapy that costs two million euro per patient ever be funded at scale?",
        "How long does a single-dose gene therapy actually last?",
        "What evidence should be required before a living medicine is approved?",
        "Who owns and who may read a person's genome?",
        "How is manufacturing capacity distributed beyond a handful of countries?",
    ),
    milestones=(
        Milestone(1922, "Insulin first used to treat a patient with diabetes"),
        Milestone(1953, "Structure of DNA published"),
        Milestone(1973, "Recombinant DNA technology demonstrated"),
        Milestone(1975, "Monoclonal antibodies produced by hybridoma"),
        Milestone(1982, "First recombinant medicine approved"),
        Milestone(2003, "Human Genome Project completed"),
        Milestone(2017, "First gene therapy and first CAR-T product approved in the United States"),
        Milestone(2020, "Messenger RNA vaccines deployed at population scale"),
    ),
    sdgs=(3, 9, 10),
    references=("walsh2018", "high2019", "plotkin2020"),
    # -------------------------------------------------------------------------
    #  The eight subtypes, in published order
    # -------------------------------------------------------------------------
    subtypes=(
        pharmaceutical_biotechnology.SUBTYPE,
        antibody_engineering.SUBTYPE,
        vaccine_development.SUBTYPE,
        gene_therapy.SUBTYPE,
        cell_therapy.SUBTYPE,
        regenerative_medicine.SUBTYPE,
        molecular_diagnostics.SUBTYPE,
        pharmacogenomics.SUBTYPE,
    ),
)
