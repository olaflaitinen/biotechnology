# =============================================================================
#  biotechnology.branches.green.animal_biotechnology
# -----------------------------------------------------------------------------
#  GREEN BIOTECHNOLOGY  ->  ANIMAL BIOTECHNOLOGY
#
#  IN ONE SENTENCE, FOR ANYONE
#  Applying reproductive and genetic technology to farm animals so that fewer
#  animals produce more food, get sick less often and suffer less.
#
#  AN ETHICAL NOTE THAT BELONGS IN THE DATA, NOT A FOOTNOTE
#  Every technique here acts on a sentient animal, and several of them - horn
#  removal, tail docking avoidance, disease resistance - exist specifically to
#  reduce suffering that current farming imposes. Others raise welfare
#  concerns of their own. This record reports both directions, and links to
#  `purple.bioethics` rather than pretending the question is settled.
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
    key="animal_biotechnology",
    name="Animal Biotechnology",
    aliases=("livestock genomics", "animal breeding", "reproductive technology"),
    summary=(
        "Reproductive, genomic and genetic technologies applied to livestock "
        "to improve productivity, welfare and disease resistance."
    ),
    description=(
        "Animal biotechnology combines three layers. Reproductive technology "
        "multiplies the influence of superior parents: artificial insemination "
        "lets one bull sire tens of thousands of calves, sexed semen biases "
        "the calf crop towards the productive sex, and superovulation with "
        "embryo transfer or ovum pick-up with in vitro production does the "
        "same on the female side. Genomic technology changes how those parents "
        "are chosen: genomic selection, adopted by the dairy industry from "
        "2009 onwards, estimates breeding values from tens of thousands of "
        "markers in a calf rather than from the milk records of its adult "
        "daughters, roughly halving the generation interval and thereby nearly "
        "doubling the annual rate of genetic gain. Genetic technology alters "
        "the animal directly: somatic cell nuclear transfer produces clones of "
        "an existing individual, and zygote editing produces defined changes "
        "such as knocking out the CD163 receptor that porcine reproductive and "
        "respiratory syndrome virus requires, or introducing the POLLED allele "
        "so that cattle grow no horns. Transgenic animals also serve as "
        "bioreactors, secreting recombinant proteins into milk or egg white."
    ),
    plain_language=(
        "Farmers have always bred from their best animals. The difference now "
        "is speed and precision. A DNA test on a newborn calf can predict how "
        "much milk its daughters will give, so the decision no longer waits "
        "five years. Embryos can be produced from the best cows and carried by "
        "others. And in a few cases a single gene can be changed - for "
        "instance so that cattle are born without horns and never have to be "
        "painfully dehorned, or so that pigs cannot catch a virus that "
        "otherwise kills millions of them each year."
    ),
    analogy=(
        "It is the difference between judging a racehorse by watching it race "
        "for five seasons and reading a reliable form report on the day it is "
        "born. The animals are the same animals; the information arrives much "
        "earlier, so far fewer wrong turnings are taken."
    ),
    why_it_matters=(
        "Livestock account for a large share of agricultural greenhouse gas "
        "emissions and land use, and the fastest way to lower emissions per "
        "litre of milk or kilogram of meat is to raise output per animal and "
        "cut mortality. Disease resistance is the clearest case: a pig that "
        "cannot be infected does not need antibiotics, does not transmit, and "
        "does not die, which is simultaneously an economic, an animal welfare "
        "and an antimicrobial resistance argument. The counterweights are "
        "genetic diversity loss from very narrow sire selection, and unresolved "
        "public disagreement about editing sentient animals at all."
    ),
    applications=(
        "Genomic selection in dairy cattle and pigs",
        "Artificial insemination and sexed semen",
        "Ovum pick-up with in vitro embryo production",
        "PRRS-resistant pigs through CD163 knockout",
        "POLLED cattle that grow no horns",
        "Transgenic animals producing therapeutic proteins in milk",
        "Cloning of elite breeding animals and of endangered breeds",
        "Genomic management of inbreeding in small populations",
    ),
    technologies=(
        "Single nucleotide polymorphism chips for livestock species",
        "Genomic estimated breeding value pipelines",
        "Flow-cytometric sperm sexing",
        "Superovulation, embryo flushing and transfer",
        "Somatic cell nuclear transfer",
        "CRISPR editing of zygotes and of primordial germ cells",
        "Cryopreservation of semen, oocytes and embryos",
        "Sensor-based phenotyping of feed intake and health",
    ),
    organisms=(
        "bos_taurus",
        "sus_scrofa",
        "gallus_gallus",
        "ovis_aries",
        "salmo_salar",
    ),
    techniques=(
        "next_generation_sequencing",
        "microarray",
        "crispr_cas9",
        "cryopreservation",
        "flow_cytometry",
        "pcr",
    ),
    challenges=(
        "Loss of genetic diversity through intense sire selection",
        "Welfare consequences of selecting hard for production traits",
        "Low efficiency and high loss rates in somatic cell nuclear transfer",
        "Regulatory uncertainty for edited food animals",
        "Public acceptance of any genetic intervention in animals",
        "Concentration of genetics in very few multinational suppliers",
    ),
    metrics=(
        Metric(
            name="Genomic estimated breeding value",
            symbol="GEBV",
            unit="trait units",
            typical="expressed as deviation from a base population",
            formula="genomic_breeding_value",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Generation interval",
            symbol="L",
            unit="years",
            typical="1.5 - 2 years in genomic dairy schemes, 5+ historically",
            formula="generation_interval",
            evidence=EvidenceLevel.CONSENSUS,
            note="Halving L roughly doubles annual genetic gain, all else equal.",
        ),
        Metric(
            name="Rate of inbreeding per generation",
            symbol="dF",
            unit="-",
            typical="< 0.01 recommended",
            formula="inbreeding_rate",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Effective population size",
            symbol="Ne",
            unit="animals",
            typical="50 - 150 in commercial dairy breeds",
            formula="effective_population_size",
            evidence=EvidenceLevel.REVIEWED,
        ),
        Metric(
            name="Conception rate",
            symbol="CR",
            unit="%",
            typical="30 - 60 % per insemination",
            evidence=EvidenceLevel.REVIEWED,
        ),
    ),
    formulas=(
        "genomic_breeding_value",
        "generation_interval",
        "genetic_gain",
        "inbreeding_rate",
        "effective_population_size",
        "heritability",
        "breeders_equation",
    ),
    maturity=Maturity.COMMERCIAL,
    risk_tier=RiskTier.REGULATED,
    scale=Scale.FIELD,
    domains=(Domain.FOOD,),
    regulatory_status=RegulatoryStatus.VARIES,
    regulations=(
        "EU Regulation (EU) 2016/1012 on animal breeding",
        "EU Directive 2010/63/EU on animals used for scientific purposes",
        "EU Regulation (EC) No 1099/2009 on protection of animals at killing",
        "US FDA guidance on intentional genomic alterations in animals",
    ),
    standards=(
        "ICAR guidelines for animal recording and evaluation",
        "Interbull international genetic evaluation standards",
        "OIE terrestrial animal health code",
    ),
    milestones=(
        Milestone(1780, "Spallanzani reports the first artificial insemination of a dog"),
        Milestone(1951, "Successful embryo transfer in cattle"),
        Milestone(1985, "First transgenic livestock produced"),
        Milestone(1996, "Dolly the sheep cloned from an adult somatic cell"),
        Milestone(2009, "Genomic selection adopted across the dairy industry"),
        Milestone(2016, "PRRS-resistant pigs produced by gene editing"),
        Milestone(2020, "First edited food animal approved for sale in the United States"),
    ),
    sdgs=(2, 3),
    glossary=(
        "breeding_value",
        "generation_interval",
        "inbreeding",
        "effective_population_size",
        "somatic_cell_nuclear_transfer",
        "zygote",
        "polled",
        "zoonosis",
    ),
    references=("wilmut1997", "meuwissen2001", "vanraden2020", "whitworth2016"),
    related=(
        "green.veterinary_vaccines",
        "green.agricultural_genome_editing",
        "green.molecular_plant_breeding",
        "blue.aquaculture_biotechnology",
        "purple.bioethics",
        "yellow.alternative_proteins",
    ),
)
