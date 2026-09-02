# =============================================================================
#  biotechnology.branches.green.veterinary_vaccines
# -----------------------------------------------------------------------------
#  GREEN BIOTECHNOLOGY  ->  VETERINARY VACCINES AND ANIMAL HEALTH
#
#  IN ONE SENTENCE, FOR ANYONE
#  Vaccinating farm animals, which protects the animals, protects the food
#  supply, and - because most new human diseases come from animals - protects
#  people too.
#
#  ONE HEALTH
#  This module is the clearest instance in the taxonomy of the One Health
#  principle: human, animal and environmental health are one system. Roughly
#  three-quarters of emerging human infectious diseases originate in animals,
#  so an outbreak stopped in a poultry shed is an outbreak that never reaches a
#  hospital.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ...core.enums import (
    Domain,
    EvidenceLevel,
    Maturity,
    RegulatoryStatus,
    RiskTier,
    Scale,
)
from ...core.models import Metric, Milestone, Subtype

__all__ = ["SUBTYPE"]


SUBTYPE = Subtype(
    key="veterinary_vaccines",
    name="Veterinary Vaccines and Animal Health",
    aliases=("animal vaccines", "veterinary biologics", "one health", "zoonosis control"),
    summary=(
        "Vaccines, diagnostics and therapeutics for farm and companion "
        "animals, central to controlling zoonoses and reducing antibiotic use."
    ),
    description=(
        "Veterinary vaccinology shares its platform technologies with human "
        "vaccinology but operates under different constraints. Cost per dose "
        "must be measured in cents, not euro; administration must work on "
        "thousands of animals per hour, which favours drinking water, spray, "
        "in-ovo and needle-free routes; and the endpoint is often herd-level "
        "transmission control rather than individual protection. A distinctive "
        "requirement is DIVA capability - differentiating infected from "
        "vaccinated animals - achieved by deleting a non-essential antigen "
        "from the vaccine strain and testing for antibodies against it, so that "
        "a country can vaccinate without losing its disease-free trade status. "
        "Marker vaccines, vectored constructs using herpesvirus of turkeys as "
        "a backbone, and autogenous vaccines made from an isolate taken on the "
        "affected farm are all in routine use. Beyond vaccines, the field "
        "covers herd-level molecular diagnostics, alternatives to antibiotic "
        "growth promoters, and the antimicrobial stewardship programmes that "
        "have cut veterinary antibiotic sales sharply across Europe since 2011."
    ),
    plain_language=(
        "Farm animals are vaccinated for the same reason children are: it is "
        "cheaper and kinder to prevent an illness than to treat it. There are "
        "two extra reasons on a farm. First, a sick herd is a food supply "
        "problem, not just an animal problem. Second, many human diseases - "
        "including most new ones - start in animals, so stopping an infection "
        "in a poultry shed can stop it ever reaching people. Vaccinating "
        "animals also means fewer antibiotics are used, which slows the rise "
        "of drug-resistant bacteria that affect us all."
    ),
    analogy=(
        "It is fitting smoke detectors in every flat of a building rather than "
        "only in your own. The fire that never starts next door is the one that "
        "never spreads to you."
    ),
    why_it_matters=(
        "Rinderpest, a cattle disease that caused famines across Africa and "
        "Asia for centuries, was eradicated in 2011 by vaccination - only the "
        "second disease of any species ever eradicated. Avian influenza "
        "control in poultry is the front line against a virus with pandemic "
        "potential in humans. And veterinary antimicrobial use, which in some "
        "countries once exceeded human use by weight, has fallen by more than "
        "half in the European Union largely because vaccination and husbandry "
        "replaced routine medication."
    ),
    applications=(
        "Foot-and-mouth disease vaccination and emergency banks",
        "Avian influenza vaccination and control programmes",
        "Classical swine fever and PRRS control",
        "Rabies control through oral vaccination of wildlife",
        "Newcastle disease vaccination by drinking water and spray",
        "Autogenous vaccines against farm-specific isolates",
        "Fish vaccines delivered by immersion or injection in aquaculture",
        "Anthelmintic resistance management and parasite vaccines",
    ),
    technologies=(
        "Marker and DIVA vaccine design by antigen deletion",
        "Herpesvirus of turkeys vectored constructs",
        "Inactivated oil-adjuvanted emulsions",
        "In-ovo vaccination at day eighteen of incubation",
        "Reverse vaccinology from pathogen genomes",
        "Oral bait vaccine formulation for wildlife",
        "Herd-level pooled PCR surveillance",
        "Thermostable formulation for cold-chain-free delivery",
    ),
    organisms=(
        "gallus_gallus",
        "bos_taurus",
        "sus_scrofa",
        "salmo_salar",
        "escherichia_coli",
    ),
    techniques=(
        "cell_culture",
        "elisa",
        "pcr",
        "next_generation_sequencing",
        "chromatography",
        "bioassay",
    ),
    challenges=(
        "Extreme price sensitivity per dose",
        "Antigenic variability in foot-and-mouth disease and influenza",
        "Trade rules that penalise vaccination against some diseases",
        "Delivery to extensive and smallholder systems without cold chain",
        "Wildlife reservoirs that vaccination cannot reach",
        "Fragmented regulatory approval across national markets",
    ),
    metrics=(
        Metric(
            name="Vaccine efficacy in the herd",
            symbol="VE",
            unit="%",
            typical="60 - 95 %",
            formula="vaccine_efficacy",
            evidence=EvidenceLevel.REVIEWED,
        ),
        Metric(
            name="Reproduction number under vaccination",
            symbol="R_v",
            unit="-",
            typical="target below 1",
            formula="basic_reproduction_number",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Serological titre",
            symbol="log2 HI",
            unit="log2 haemagglutination inhibition",
            typical="protective threshold about 4-5 log2",
            formula="geometric_mean_titre",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Vaccination coverage",
            symbol="V_cov",
            unit="% of herd or flock",
            typical="> 80 % for transmission control",
            formula="herd_immunity_threshold",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Defined daily dose animal",
            symbol="DDDvet",
            unit="mg/PCU",
            typical="antimicrobial use benchmark",
            evidence=EvidenceLevel.REVIEWED,
            note="The standard European metric for veterinary antibiotic consumption.",
        ),
    ),
    formulas=(
        "vaccine_efficacy",
        "basic_reproduction_number",
        "herd_immunity_threshold",
        "geometric_mean_titre",
        "prevalence_estimation",
        "sensitivity_specificity",
    ),
    maturity=Maturity.ESTABLISHED,
    risk_tier=RiskTier.REGULATED,
    scale=Scale.POPULATION,
    domains=(Domain.FOOD, Domain.HEALTH, Domain.SECURITY),
    regulatory_status=RegulatoryStatus.AUTHORISED,
    regulations=(
        "EU Regulation (EU) 2019/6 on veterinary medicinal products",
        "EU Regulation (EU) 2016/429 the Animal Health Law",
        "WOAH terrestrial and aquatic animal health codes",
        "EU Regulation (EU) 2019/4 on medicated feed",
    ),
    standards=(
        "WOAH Manual of Diagnostic Tests and Vaccines",
        "Ph. Eur. monographs for veterinary vaccines",
        "VICH guidelines for veterinary product registration",
    ),
    milestones=(
        Milestone(1879, "Pasteur produces the first attenuated bacterial vaccine, for fowl cholera"),
        Milestone(1881, "Pasteur demonstrates anthrax vaccination in sheep"),
        Milestone(1960, "Thermostable rinderpest vaccine developed"),
        Milestone(1978, "Oral rabies vaccination of wild foxes begins in Europe"),
        Milestone(1992, "First DIVA marker vaccine concepts introduced"),
        Milestone(2011, "Rinderpest declared globally eradicated"),
        Milestone(2022, "EU veterinary antimicrobial sales fall by more than half from 2011"),
    ),
    sdgs=(2, 3, 12),
    glossary=(
        "zoonosis",
        "one_health",
        "diva_vaccine",
        "attenuation",
        "herd_immunity",
        "antimicrobial_resistance",
        "seroprevalence",
        "notifiable_disease",
    ),
    references=("pasteur1881", "woah_manual", "ema_esvac", "roeder2013"),
    related=(
        "green.animal_biotechnology",
        "red.vaccine_development",
        "blue.aquaculture_biotechnology",
        "dark.biosurveillance",
        "grey.environmental_biomonitoring",
        "yellow.food_safety_biotechnology",
    ),
)
