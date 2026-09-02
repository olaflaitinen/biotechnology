# =============================================================================
#  biotechnology.branches.red.vaccine_development.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires that
#  setbacks appear; here that is the 1955 Cutter incident, which killed
#  children and rewrote how biological products are regulated.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the longest timeline in the taxonomy and the only one that reaches
#  an eradication. It is worth reading in full for one reason: the interval
#  from first idea to first product shortened from roughly a century to roughly
#  a year across the span of these entries, and the 2020 entry is the reason
#  every subsequent conversation about outbreak response starts from a
#  different baseline.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  BEFORE VACCINATION: DELIBERATE INFECTION
    # =========================================================================
    Milestone(
        1721,
        "Variolation against smallpox is publicised in Britain by Lady Mary "
        "Wortley Montagu",
        note=(
            "Deliberate infection with material from a mild case. It worked, "
            "and it killed roughly one in fifty of those treated, which is why "
            "the next entry mattered so much."
        ),
    ),
    # =========================================================================
    #  THE FOUNDING OBSERVATIONS
    # =========================================================================
    Milestone(
        1796,
        "Jenner demonstrates that cowpox inoculation protects against smallpox",
        note=(
            "The first use of a related but harmless organism, and the origin "
            "of the word vaccine, from the Latin for cow."
        ),
    ),
    Milestone(
        1879,
        "Pasteur produces the first attenuated bacterial vaccine, for fowl "
        "cholera",
        note=(
            "Discovered by accident, from a culture left over a summer holiday. "
            "It established attenuation as a deliberate technique rather than a "
            "lucky choice of organism."
        ),
    ),
    Milestone(
        1885,
        "Pasteur administers the first rabies post-exposure vaccine to a child",
    ),
    # =========================================================================
    #  INDUSTRIAL SCALE, AND THE DISASTER THAT SHAPED REGULATION
    # =========================================================================
    Milestone(
        1923,
        "Formalin inactivation makes diphtheria and tetanus toxoid vaccines "
        "possible",
    ),
    Milestone(
        1955,
        "Salk inactivated polio vaccine licensed, and the Cutter incident "
        "follows within weeks",
        note=(
            "Incompletely inactivated batches from one manufacturer paralysed "
            "children and killed several. The investigation produced the "
            "modern framework of batch release, lot testing and manufacturer "
            "liability under which every biological product is now made."
        ),
    ),
    Milestone(
        1963,
        "Measles vaccine licensed, later combined into MMR",
    ),
    # =========================================================================
    #  ERADICATION
    # =========================================================================
    Milestone(
        1980,
        "The World Health Assembly declares smallpox eradicated",
        note=(
            "The only human disease ever eradicated. The campaign succeeded "
            "through surveillance and ring vaccination rather than through mass "
            "coverage, which is a lesson repeatedly relearned since."
        ),
    ),
    # =========================================================================
    #  THE RECOMBINANT AND CONJUGATE ERA
    # =========================================================================
    Milestone(
        1986,
        "First recombinant vaccine approved, for hepatitis B",
        note=(
            "Produced in yeast rather than harvested from human plasma, which "
            "removed a blood-borne safety risk entirely."
        ),
    ),
    Milestone(
        1987,
        "First conjugate vaccine licensed, against Haemophilus influenzae type b",
        note=(
            "Coupling a polysaccharide to a carrier protein recruits T-cell "
            "help, which is what makes a bacterial vaccine work in infants. It "
            "removed the leading cause of childhood bacterial meningitis."
        ),
    ),
    Milestone(
        2006,
        "Human papillomavirus vaccines introduced",
        note="The first vaccines designed explicitly to prevent a cancer.",
    ),
    # =========================================================================
    #  THE NUCLEIC-ACID ERA
    # =========================================================================
    Milestone(
        2020,
        "First messenger RNA vaccines authorised for human use",
        note=(
            "Sixty-three days from the publication of the viral sequence to the "
            "first dose in a trial participant. The platform had been in "
            "development for three decades; what was new was that it worked at "
            "scale, and that regulators and manufacturers ran in parallel "
            "rather than in sequence."
        ),
    ),
    Milestone(
        2021,
        "First malaria vaccine recommended by the World Health Organization",
        note=(
            "Modest efficacy against a parasite that had defeated vaccine "
            "development for a century, in the disease that kills the most "
            "children."
        ),
    ),
    Milestone(
        2023,
        "First respiratory syncytial virus vaccines approved, decades after a "
        "1960s trial in which a candidate worsened disease",
        note=(
            "The delay was caused by that early failure. Structure-based "
            "prefusion stabilisation is what finally resolved it, which is the "
            "clearest example in this record of design rather than "
            "manufacturing solving a problem."
        ),
    ),
)
