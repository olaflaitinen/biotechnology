# =============================================================================
#  biotechnology.branches.green.veterinary_vaccines.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks;
#  this record has two, in 2001 and 2003, and the first is the largest single
#  demonstration of what happens when trade rules discourage vaccination.
#
#  SUBTYPE-SPECIFIC NOTE
#  Veterinary vaccinology is older than human vaccinology as a deliberate
#  science. Jenner's cowpox observation in 1796 came from cattle, and Pasteur's
#  first two attenuated vaccines, in 1879 and 1881, were both veterinary. The
#  field that is now treated as an application of human vaccinology is in fact
#  where the method was invented.
#
#  The 2011 rinderpest entry deserves its length. It is the second disease of
#  any species ever eradicated, and it happened in livestock, largely
#  unnoticed outside the profession.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE METHOD WAS INVENTED HERE
    # =========================================================================
    Milestone(
        1879,
        "Pasteur produces the first deliberately attenuated vaccine, against "
        "fowl cholera",
        note=(
            "Discovered by accident, from a culture left over a summer holiday "
            "that had lost its virulence. The first vaccine in history designed "
            "rather than found, and it was a poultry vaccine."
        ),
    ),
    Milestone(
        1881,
        "Pasteur demonstrates anthrax vaccination publicly at Pouilly-le-Fort",
        note=(
            "Twenty-five vaccinated sheep survived a challenge that killed "
            "almost all twenty-five unvaccinated controls, in front of an "
            "invited audience. A veterinary experiment, and the demonstration "
            "that made vaccination credible to the public."
        ),
    ),
    # =========================================================================
    #  MASS ADMINISTRATION
    # =========================================================================
    Milestone(
        1950,
        "Live attenuated Newcastle disease vaccines are developed for mass "
        "administration",
        note=(
            "Delivery by drinking water and spray made it possible to vaccinate "
            "a flock of fifty thousand birds in an afternoon, which is the "
            "logistical problem that distinguishes this field from human "
            "vaccinology."
        ),
    ),
    Milestone(
        1960,
        "A thermostable rinderpest vaccine is developed",
        note=(
            "Protection without a cold chain, in regions where a cold chain did "
            "not exist. It is the single technical advance that made the "
            "eradication campaign possible, and it is a formulation advance "
            "rather than an immunological one."
        ),
    ),
    Milestone(
        1970,
        "In-ovo vaccination against Marek's disease is introduced",
        note=(
            "Vaccinating a chick at day eighteen of incubation, before it "
            "hatches, now automated at tens of thousands of eggs per hour."
        ),
    ),
    # =========================================================================
    #  REACHING WILDLIFE
    # =========================================================================
    Milestone(
        1978,
        "Oral rabies vaccination of wild foxes begins in Switzerland",
        note=(
            "Vaccine-laden baits distributed across the landscape, later by "
            "aircraft on defined grids. It eliminated fox rabies from western "
            "Europe, and remains the only successful large-scale vaccination of "
            "a wild population."
        ),
    ),
    # =========================================================================
    #  SOLVING THE TRADE PROBLEM
    # =========================================================================
    Milestone(
        1992,
        "DIVA marker vaccine concepts are introduced for pseudorabies",
        note=(
            "Deleting a non-essential antigen so that vaccinated animals can be "
            "distinguished serologically from infected ones. A technical "
            "solution to a trade problem, and the concept that made vaccination "
            "compatible with disease-free status."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: WHAT HAPPENS WHEN VACCINATION IS DISCOURAGED
    # =========================================================================
    Milestone(
        2001,
        "The United Kingdom foot-and-mouth disease epidemic is controlled by "
        "culling rather than vaccination",
        note=(
            "More than six million animals were killed. Vaccination was "
            "available and was not used at scale, in large part because it "
            "would have delayed the return of disease-free trading status. The "
            "episode is recorded as a setback because it demonstrated, at "
            "enormous cost and with lasting public revulsion, that a trade rule "
            "can override both economics and animal welfare. It is the strongest "
            "single argument for the DIVA technology in this record."
        ),
    ),
    Milestone(
        2003,
        "Avian influenza H7N7 in the Netherlands infects 89 people and kills a "
        "veterinarian during a poultry cull",
        note=(
            "Thirty million birds culled. A reminder recorded here because it "
            "is easy to treat poultry disease as an agricultural matter: the "
            "people at greatest risk during a zoonotic outbreak are the ones "
            "handling the animals."
        ),
    ),
    # =========================================================================
    #  ERADICATION
    # =========================================================================
    Milestone(
        2011,
        "Rinderpest is declared globally eradicated",
        note=(
            "The second disease of any species ever eradicated, after "
            "smallpox, and the only animal disease. It had caused famines "
            "across Africa and Asia for centuries; a single nineteenth-century "
            "outbreak killed an estimated ninety per cent of the cattle in "
            "sub-Saharan Africa. Achieved with a thermostable vaccine, "
            "community-based delivery by trained local vaccinators, and "
            "surveillance. It happened in livestock and passed almost unnoticed "
            "outside the profession."
        ),
    ),
    # =========================================================================
    #  THE ANTIMICROBIAL RESULT
    # =========================================================================
    Milestone(
        2006,
        "The European Union bans antibiotic growth promoters",
        note=(
            "Removed routine sub-therapeutic medication and forced the industry "
            "towards vaccination, husbandry and management as substitutes. The "
            "measurable consequence is the next entry."
        ),
    ),
    Milestone(
        2022,
        "EU veterinary antimicrobial sales are reported to have more than "
        "halved since 2011",
        note=(
            "Achieved largely through vaccination and husbandry rather than "
            "prohibition alone. The clearest quantitative demonstration that "
            "animal vaccination is a human antimicrobial resistance "
            "intervention."
        ),
    ),
)
