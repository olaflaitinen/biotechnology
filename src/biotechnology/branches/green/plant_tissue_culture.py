# =============================================================================
#  biotechnology.branches.green.plant_tissue_culture
# -----------------------------------------------------------------------------
#  GREEN BIOTECHNOLOGY  ->  PLANT TISSUE CULTURE AND MICROPROPAGATION
#
#  IN ONE SENTENCE, FOR ANYONE
#  Growing whole plants from a few cells in a sterile jar, so that thousands
#  of identical, disease-free seedlings can be produced from one good parent.
#
#  WHY IT UNDERPINS EVERYTHING ELSE IN THIS BRANCH
#  Every transgenic and every edited plant has to be regenerated from a single
#  transformed cell, and that regeneration is tissue culture. When a genotype
#  is described as "recalcitrant" and therefore un-engineerable, the failure is
#  almost always here rather than in the DNA delivery step.
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
    key="plant_tissue_culture",
    name="Plant Tissue Culture and Micropropagation",
    aliases=("micropropagation", "in vitro culture", "meristem culture", "clonal propagation"),
    summary=(
        "Regenerating whole plants from cells, tissues or organs on sterile "
        "media to mass-produce uniform, disease-free planting material."
    ),
    description=(
        "Plant tissue culture exploits totipotency: most living plant cells "
        "retain the full genetic programme needed to rebuild an entire "
        "organism. An explant - a shoot tip, a leaf disc, an anther, an "
        "immature embryo - is surface-sterilised and placed on a defined "
        "medium containing mineral salts, sucrose, vitamins and, critically, a "
        "balance of two hormone classes. A high cytokinin to auxin ratio "
        "favours shoot formation; the reverse favours roots; an intermediate "
        "ratio produces undifferentiated callus. Regeneration proceeds either "
        "by organogenesis, in which shoots and roots form successively, or by "
        "somatic embryogenesis, in which bipolar embryos form directly and can "
        "be encapsulated as synthetic seed. Meristem culture exploits the fact "
        "that the apical dome is usually virus-free because viral movement "
        "lags behind cell division, so excising a fragment under a millimetre "
        "across yields clean stock from an infected mother plant. The main "
        "quality risk is somaclonal variation: prolonged callus phases "
        "accumulate epigenetic and chromosomal change, so commercial protocols "
        "cap the number of subcultures."
    ),
    plain_language=(
        "A cutting from a houseplant will grow roots in a glass of water. "
        "Plant tissue culture is that idea taken to its limit: with the right "
        "nutrients and hormones, a piece of tissue smaller than a grain of "
        "rice can be persuaded to grow into a complete plant, and each of "
        "those plants can be divided again. Because everything is done in "
        "sealed sterile jars, the resulting plants carry none of the diseases "
        "the parent may have had, and every one of them is genetically "
        "identical to that parent."
    ),
    analogy=(
        "It is photocopying rather than reprinting. A seed is a new edition "
        "with fresh typesetting - every one slightly different. Tissue culture "
        "makes exact copies of a page you already like, and it makes them "
        "clean, without the coffee stains the original picked up."
    ),
    why_it_matters=(
        "Almost every banana eaten in the world is a clone produced this way, "
        "and the technique is what keeps virus-free potato, sugarcane, "
        "strawberry and orchid industries running. For a smallholder, "
        "certified virus-free planting material can be the difference between "
        "a normal harvest and a thirty per cent loss. It is also the quiet "
        "prerequisite for gene editing and transformation, which cannot "
        "deliver a plant without it."
    ),
    applications=(
        "Clonal propagation of banana, orchid, sugarcane and date palm",
        "Virus elimination from potato and cassava seed systems",
        "Somatic embryogenesis in conifer and oil palm forestry",
        "Anther and microspore culture for doubled haploids",
        "Embryo rescue in wide crosses that would otherwise abort",
        "In vitro germplasm conservation and slow-growth storage",
        "Production of secondary metabolites in cell suspension",
        "Regeneration step for transformation and genome editing",
    ),
    technologies=(
        "Murashige and Skoog basal medium and its derivatives",
        "Auxin to cytokinin ratio control for organogenesis",
        "Temporary immersion bioreactors for scale-up",
        "Meristem excision under stereomicroscope",
        "Synthetic seed encapsulation in calcium alginate",
        "Cryopreservation by vitrification and droplet freezing",
        "Laminar flow sterile technique and contamination indexing",
        "Acclimatisation and hardening protocols before field transfer",
    ),
    organisms=(
        "musa_acuminata",
        "solanum_tuberosum",
        "nicotiana_tabacum",
        "arabidopsis_thaliana",
        "elaeis_guineensis",
    ),
    techniques=(
        "tissue_culture",
        "cryopreservation",
        "microscopy",
        "pcr",
        "plant_transformation",
    ),
    challenges=(
        "Somaclonal variation after extended callus phases",
        "Endophytic bacterial contamination that appears only after months",
        "Genotype-dependent recalcitrance in elite cereal lines",
        "Hyperhydricity and poor survival at acclimatisation",
        "Labour cost, which dominates the economics of micropropagation",
        "Cryopreservation protocols that must be developed species by species",
    ),
    metrics=(
        Metric(
            name="Multiplication rate",
            symbol="M",
            unit="shoots per explant per cycle",
            typical="3 - 10 per 4-6 week cycle",
            formula="multiplication_rate",
            evidence=EvidenceLevel.CONSENSUS,
            note="Compounds geometrically: a rate of 5 gives 15625 plants in six cycles.",
        ),
        Metric(
            name="Regeneration frequency",
            symbol="RF",
            unit="% of explants",
            typical="10 - 90 %",
            formula="regeneration_frequency",
            evidence=EvidenceLevel.REVIEWED,
        ),
        Metric(
            name="Contamination rate",
            symbol="C_rate",
            unit="% of cultures",
            typical="< 5 % in a well-run laboratory",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Acclimatisation survival",
            symbol="S_acc",
            unit="%",
            typical="70 - 98 %",
            evidence=EvidenceLevel.REVIEWED,
            note="The step where poorly hardened plantlets are lost in bulk.",
        ),
        Metric(
            name="Auxin to cytokinin ratio",
            symbol="A:C",
            unit="-",
            typical="high for roots, low for shoots",
            formula="hormone_ratio",
            evidence=EvidenceLevel.CONSENSUS,
        ),
    ),
    formulas=(
        "multiplication_rate",
        "regeneration_frequency",
        "hormone_ratio",
        "medium_osmolality",
        "serial_dilution",
        "exponential_growth",
    ),
    maturity=Maturity.ESTABLISHED,
    risk_tier=RiskTier.ROUTINE,
    scale=Scale.INDUSTRIAL,
    domains=(Domain.FOOD, Domain.ENVIRONMENT),
    regulatory_status=RegulatoryStatus.NOTIFIED,
    regulations=(
        "EU Regulation (EU) 2016/2031 on protective measures against plant pests",
        "EU marketing directives for propagating material",
        "National phytosanitary certification for cross-border movement",
        "Nagoya Protocol for germplasm access",
    ),
    standards=(
        "EPPO certification schemes for pathogen-tested material",
        "FAO/IPGRI genebank standards for in vitro conservation",
        "ISTA and ISHS protocols for propagation material quality",
    ),
    milestones=(
        Milestone(1902, "Haberlandt proposes cell totipotency"),
        Milestone(1939, "First indefinitely growing plant callus cultures established"),
        Milestone(1957, "Skoog and Miller describe hormonal control of organogenesis"),
        Milestone(1962, "Murashige and Skoog publish their medium formulation"),
        Milestone(1974, "Commercial orchid and ornamental micropropagation industry forms"),
        Milestone(1985, "Cryopreservation of plant meristems demonstrated"),
        Milestone(2000, "Temporary immersion bioreactors reach commercial banana production"),
    ),
    sdgs=(2, 15),
    glossary=(
        "totipotency",
        "explant",
        "callus",
        "meristem",
        "somatic_embryogenesis",
        "somaclonal_variation",
        "auxin",
        "cytokinin",
    ),
    references=("murashige1962", "skoog1957", "george2008"),
    related=(
        "green.plant_genetic_engineering",
        "green.agricultural_genome_editing",
        "green.molecular_plant_breeding",
        "brown.arid_land_crops",
        "grey.biodiversity_conservation",
    ),
)
