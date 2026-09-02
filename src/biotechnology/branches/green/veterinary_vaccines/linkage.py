# =============================================================================
#  biotechnology.branches.green.veterinary_vaccines.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has the strongest cross-branch edges in the green branch, and
#  they are the point rather than a convenience.
#
#  `red.vaccine_development` shares the platforms, the formulas and most of the
#  vocabulary. The difference is not scientific: it is cost per dose,
#  administration to thousands of animals an hour, and a population rather than
#  an individual endpoint. Reading the two records side by side is the clearest
#  way to see how constraints rather than biology shape a technology.
#
#  `red.molecular_diagnostics` is a hard dependency rather than a neighbour. A
#  DIVA vaccine is useless without its companion test, and the specificity
#  requirement recorded in `metrics.py` is a diagnostics requirement, not a
#  vaccine one. The two were designed together.
#
#  `green.animal_biotechnology` is the same animals under different
#  technologies, and the two records answer the same question by different
#  routes: disease resistance can be vaccinated for or bred for.
#
#  `dark.biosecurity` is included because several of the pathogens in this
#  record are listed agents, and because a national vaccine antigen bank is
#  simultaneously an animal health measure and a preparedness asset.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and Goal 3 is the one that would surprise a reader who filed this
#  record under agriculture. It is claimed twice over: zoonoses prevented in
#  animals never reach people, and antimicrobial use avoided in animals slows
#  resistance in human medicine. The halving of EU veterinary antimicrobial
#  sales since 2011 is the evidence, and it is recorded as a metric and a
#  milestone rather than left as an assertion here.
# =============================================================================
SDGS: Tuple[int, ...] = (
    1,  # No poverty, on livestock as the principal asset of poor households
    2,  # Zero hunger, on losses to disease in food-producing animals
    3,  # Good health and well-being, on zoonoses and antimicrobial resistance
    17,  # Partnerships, on the tripartite One Health arrangement
)


# =============================================================================
#  GLOSSARY
#  Grouped: the concept unique to this field, then the population vocabulary,
#  then the delivery vocabulary that distinguishes it from human vaccinology.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- unique to this field --------------------------------------------------
    "diva_vaccine",
    "marker_vaccine",
    "autogenous_vaccine",
    "withdrawal_period",
    "disease_free_status",
    # -- the population frame --------------------------------------------------
    "zoonosis",
    "one_health",
    "antimicrobial_resistance",
    "herd_immunity",
    "reproduction_number",
    "shedding",
    "reservoir",
    "surveillance",
    # -- platforms -------------------------------------------------------------
    "attenuated_vaccine",
    "inactivated_vaccine",
    "subunit_vaccine",
    "viral_vector",
    "adjuvant",
    "reverse_vaccinology",
    # -- delivery and readout --------------------------------------------------
    "in_ovo_vaccination",
    "cold_chain",
    "thermostability",
    "seroconversion",
    "geometric_mean_titre",
)


# =============================================================================
#  REFERENCES
#  Weighted towards the standard-setting and surveillance documents, because in
#  this field those are what determine practice.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "who_terrestrial_animal_health_code",
    "woah_diagnostic_manual",
    "eu_regulation_2019_6_veterinary_medicinal_products",
    "esvac_antimicrobial_sales_report",
    "rinderpest_eradication_report",
    "one_health_tripartite_framework",
    "diva_vaccine_review",
    "fmd_2001_epidemic_inquiry",
    "oral_rabies_vaccination_europe",
    "poultry_vaccination_practice_review",
)


# =============================================================================
#  RELATED
#  Six edges. The first two are the ones a reader should follow first.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same technology under different constraints -----------------------
    "red.vaccine_development",
    # -- the companion test without which DIVA does not work -------------------
    "red.molecular_diagnostics",
    # -- the same animals, the other route to disease resistance ---------------
    "green.animal_biotechnology",
    # -- where the antigens and adjuvants are manufactured ---------------------
    "red.pharmaceutical_biotechnology",
    # -- listed agents, antigen banks and preparedness -------------------------
    "dark.biosecurity",
    # -- who decides what may be done to a sentient animal ---------------------
    "purple.bioethics",
)
