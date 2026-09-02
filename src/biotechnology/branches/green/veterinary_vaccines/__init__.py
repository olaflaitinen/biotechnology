# =============================================================================
#  biotechnology.branches.green.veterinary_vaccines
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  GREEN BIOTECHNOLOGY  ->  VETERINARY VACCINES
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Vaccinating animals, which keeps food supplies stable, stops diseases before
#  they reach people, and is one of the largest single reductions in antibiotic
#  use ever achieved.
#
#  WHY THIS RECORD SITS IN THE GREEN BRANCH AND NOT THE RED ONE
#  The classification is by SECTOR, not by technique. Every platform in this
#  record also appears in `red.vaccine_development`: attenuated, inactivated,
#  subunit, vectored, virus-like particle. What differs is the constraint set,
#  and the constraints are agricultural.
#
#      cost           cents per dose, not euro per dose
#      administration thousands of animals an hour, so drinking water, spray,
#                     in-ovo and immersion rather than individual injection
#      endpoint       transmission across a herd, not protection of one patient
#      extra question how long before the animal may enter the food chain
#
#  Reading this record beside `red.vaccine_development` is the clearest
#  demonstration in the library that constraints, not biology, shape a
#  technology.
#
#  THE FIELD WHERE VACCINOLOGY WAS INVENTED
#  Pasteur's first two deliberately attenuated vaccines, in 1879 and 1881, were
#  both veterinary: fowl cholera and anthrax. The public demonstration at
#  Pouilly-le-Fort that made vaccination credible to the world was performed on
#  sheep. A field now often treated as an application of human vaccinology is
#  where the method actually came from.
#
#  THE ONE REQUIREMENT WITH NO HUMAN EQUIVALENT
#  A country with disease-free trading status loses it if its animals test
#  positive, and a conventional vaccine makes vaccinated animals
#  indistinguishable from infected ones. DIVA vaccines, meaning differentiating
#  infected from vaccinated animals, delete a non-essential antigen from the
#  vaccine strain and test for antibodies against it. Vaccinated animals lack
#  that response; infected animals have it.
#
#  This is a technical solution to a LEGAL problem, and it is one of the few
#  places in this library where an advance was engineered specifically to
#  change a trade rule, and where the rule then moved.
#
#  THE SETBACK THAT EXPLAINS WHY DIVA MATTERS
#  In 2001 the United Kingdom controlled foot-and-mouth disease by killing more
#  than six million animals. Vaccine existed. It was not used at scale largely
#  because vaccinating would have delayed the return of disease-free trading
#  status. That episode is recorded in `history.py` as a setback because it
#  showed, at enormous cost, that a trade rule can override both economics and
#  animal welfare.
#
#  THE RESULT MOST READERS DO NOT KNOW
#  Rinderpest was declared eradicated in 2011. It is the second disease of any
#  species ever eradicated, after smallpox, and the only animal one. It had
#  caused famines across Africa and Asia for centuries. It was achieved with a
#  thermostable vaccine, local vaccinators and surveillance, and it passed
#  almost unnoticed outside the profession.
#
#  THE ANTIMICROBIAL ARGUMENT, STATED PLAINLY
#  An animal that does not become ill needs no antibiotic. EU veterinary
#  antimicrobial sales have more than halved since 2011, achieved largely
#  through vaccination and husbandry rather than prohibition. That is why this
#  record claims SDG 3, and the claim rests on the DDDvet metric and the 2022
#  milestone rather than on assertion.
#
#  WHY THE FIELD IS UNDERFUNDED
#  Much of the benefit is a public good captured by people who did not pay for
#  it: the neighbour whose herd is not infected, the population that never sees
#  the zoonosis, the patient whose antibiotic still works. The smoke detector
#  analogy in `narrative.py` was chosen for exactly this reason.
#
#  PACKAGE LAYOUT
#      narrative.py    the One Health framing and the smoke detector analogy
#      practice.py     applications grouped by WHO IS PROTECTED, because that
#                      decides who pays and therefore what exists
#      metrics.py      nine metrics, led by the population endpoint; cost per
#                      dose is included as a technical constraint, not an
#                      afterthought
#      history.py      1879 to 2022, including two setbacks and one eradication
#      governance.py   the trade standards that can make vaccination the wrong
#                      decision, and the DIVA answer to them
#      linkage.py      the edges to red.vaccine_development and
#                      red.molecular_diagnostics, which are the ones to follow
#
#  The full facet contract is documented in
#  `branches/red/gene_therapy/__init__.py` and is identical for all eighty-five
#  subtype packages in this library.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ....core.models import Subtype

from . import governance, history, linkage, metrics, narrative, practice

__all__ = ["SUBTYPE"]


# =============================================================================
#  IDENTITY
# =============================================================================
KEY = "veterinary_vaccines"

NAME = "Veterinary Vaccines and Animal Health"

# "one health" is included deliberately. It is not a synonym in the strict
# sense, but it is the term under which most of this record's public health
# value is discussed and funded, and a reader searching for it should arrive
# here. "livestock vaccination" and "animal health biotechnology" are what
# practitioners and industry respectively call the field.
ALIASES = (
    "animal vaccines",
    "livestock vaccination",
    "veterinary biologics",
    "animal health biotechnology",
    "one health",
    "zoonosis control",
)


# =============================================================================
#  ASSEMBLY
# =============================================================================
SUBTYPE = Subtype(
    # -- identity --------------------------------------------------------------
    key=KEY,
    name=NAME,
    aliases=ALIASES,
    # -- narrative.py ----------------------------------------------------------
    summary=narrative.SUMMARY,
    description=narrative.DESCRIPTION,
    plain_language=narrative.PLAIN_LANGUAGE,
    analogy=narrative.ANALOGY,
    why_it_matters=narrative.WHY_IT_MATTERS,
    # -- practice.py -----------------------------------------------------------
    applications=practice.APPLICATIONS,
    technologies=practice.TECHNOLOGIES,
    organisms=practice.ORGANISMS,
    techniques=practice.TECHNIQUES,
    challenges=practice.CHALLENGES,
    # -- metrics.py ------------------------------------------------------------
    metrics=metrics.METRICS,
    formulas=metrics.FORMULAS,
    # -- history.py ------------------------------------------------------------
    milestones=history.MILESTONES,
    # -- governance.py ---------------------------------------------------------
    maturity=governance.MATURITY,
    risk_tier=governance.RISK_TIER,
    scale=governance.SCALE,
    domains=governance.DOMAINS,
    regulatory_status=governance.REGULATORY_STATUS,
    regulations=governance.REGULATIONS,
    standards=governance.STANDARDS,
    # -- linkage.py ------------------------------------------------------------
    sdgs=linkage.SDGS,
    glossary=linkage.GLOSSARY,
    references=linkage.REFERENCES,
    related=linkage.RELATED,
)
