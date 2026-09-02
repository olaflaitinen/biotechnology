# =============================================================================
#  biotechnology.branches.green.biopesticides
# -----------------------------------------------------------------------------
#  GREEN BIOTECHNOLOGY  ->  BIOPESTICIDES AND BIOLOGICAL CONTROL
#
#  IN ONE SENTENCE, FOR ANYONE
#  Using living organisms, or substances they make, to control crop pests -
#  a predator, a disease of the pest, or a natural toxin - instead of a
#  broad-spectrum synthetic chemical.
#
#  THE CENTRAL TRADE-OFF
#  Biopesticides are narrow. That is simultaneously their great advantage
#  (they spare pollinators and natural enemies) and their commercial
#  disadvantage (a product that kills one pest species has a small market and
#  still needs a full registration dossier).
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
    key="biopesticides",
    name="Biopesticides and Biological Control",
    aliases=("biocontrol", "biopesticide", "bt spray", "integrated pest management"),
    summary=(
        "Pest and disease management with living organisms or their natural "
        "products instead of broad-spectrum synthetic chemistry."
    ),
    description=(
        "Biopesticides fall into three regulatory and biological classes. "
        "Microbial biopesticides use a living organism as the active "
        "substance: Bacillus thuringiensis, whose crystal proteins are "
        "solubilised and activated only in the alkaline insect midgut, is by "
        "far the largest single product; entomopathogenic fungi such as "
        "Beauveria and Metarhizium penetrate the cuticle directly; "
        "entomopathogenic nematodes carry symbiotic bacteria into the pest; "
        "baculoviruses are extremely host-specific. Biochemical biopesticides "
        "are naturally occurring substances with a non-toxic mode of action, "
        "including sex pheromones used for mating disruption and mass "
        "trapping, plant extracts such as azadirachtin, and plant defence "
        "elicitors. Macrobial biological control releases predators and "
        "parasitoids - predatory mites, parasitic wasps, ladybirds - and is "
        "the backbone of protected-crop production in northern Europe. A "
        "fourth, newer class delivers double-stranded RNA that silences an "
        "essential gene in the target pest through RNA interference, giving "
        "species-level selectivity that no chemical can match. Because all of "
        "these are living or labile, environmental persistence is short, "
        "which improves safety and complicates efficacy."
    ),
    plain_language=(
        "Instead of spraying a chemical that kills most insects it touches, "
        "biological control uses nature's own arrangements. Some products are "
        "a bacterium that makes a protein poisonous only to caterpillars and "
        "harmless to everything else, including us. Some release the wasps or "
        "mites that already eat the pest. Some flood the air with the scent "
        "females use to attract males, so the males spend the season searching "
        "and never find one. The pest is controlled, and the bees, ladybirds "
        "and earthworms are not."
    ),
    analogy=(
        "A synthetic pesticide is a fire hose aimed at a room. Biological "
        "control is a trained sniffer dog: slower to deploy, useless against "
        "anything it was not trained for, and it does not soak everything else "
        "in the room."
    ),
    why_it_matters=(
        "Broad-spectrum insecticides have been implicated in pollinator "
        "decline and routinely destroy the natural enemies that were "
        "suppressing secondary pests, producing outbreaks worse than the "
        "original problem. Biological control avoids that trap and leaves no "
        "residue, which matters for export markets with tight maximum residue "
        "limits and for the farm workers doing the spraying. It is also the "
        "only tool that still works after a pest has evolved resistance to "
        "every registered chemical, a situation now common in horticulture."
    ),
    applications=(
        "Bacillus thuringiensis sprays against lepidopteran caterpillars",
        "Beauveria and Metarhizium against locusts, thrips and whitefly",
        "Entomopathogenic nematodes against soil-dwelling larvae",
        "Baculovirus products against codling moth and armyworm",
        "Pheromone mating disruption in orchards and vineyards",
        "Trichoderma against soil-borne fungal pathogens",
        "Augmentative release of predatory mites in glasshouses",
        "RNA interference sprays against Colorado potato beetle",
    ),
    technologies=(
        "Submerged and solid-state fermentation of microbial actives",
        "Formulation with UV protectants and adjuvants",
        "Encapsulation for shelf life and rainfastness",
        "Double-stranded RNA synthesis and stabilisation",
        "Pheromone identification and controlled-release dispensers",
        "Mass rearing of predators and parasitoids",
        "Resistance-management refuge strategies",
        "Bioassay panels for efficacy and non-target safety",
    ),
    organisms=(
        "bacillus_thuringiensis",
        "beauveria_bassiana",
        "metarhizium_anisopliae",
        "trichoderma_harzianum",
        "steinernema_feltiae",
        "apis_mellifera",
    ),
    techniques=(
        "fermentation",
        "microbial_plate_count",
        "bioassay",
        "pcr",
        "chromatography",
        "microscopy",
    ),
    challenges=(
        "Short field persistence under ultraviolet light and heat",
        "Narrow host range limiting market size per product",
        "Registration dossiers designed for synthetic chemistry",
        "Cold chain and shelf life for living products",
        "Resistance evolution to Bt in intensively treated systems",
        "Slower and more variable knockdown than conventional insecticides",
    ),
    metrics=(
        Metric(
            name="Median lethal concentration",
            symbol="LC50",
            unit="mg/L or spores/mL",
            typical="assay- and species-specific",
            formula="lc50_probit",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Median lethal time",
            symbol="LT50",
            unit="days",
            typical="3 - 10 days for fungal agents",
            formula="lt50",
            evidence=EvidenceLevel.REVIEWED,
            note="Slow kill is the usual reason growers reject a biological product.",
        ),
        Metric(
            name="Spore concentration",
            symbol="S_conc",
            unit="spores/mL or spores/g",
            typical="1e8 - 1e10",
            formula="colony_forming_units",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Field efficacy",
            symbol="Abbott%",
            unit="% mortality corrected for control",
            typical="50 - 95 %",
            formula="abbott_correction",
            evidence=EvidenceLevel.CONSENSUS,
            note="Abbott's formula corrects observed mortality for natural mortality.",
        ),
        Metric(
            name="Pre-harvest interval",
            symbol="PHI",
            unit="days",
            typical="0 - 3 days for most biologicals",
            evidence=EvidenceLevel.CONSENSUS,
        ),
    ),
    formulas=(
        "lc50_probit",
        "lt50",
        "abbott_correction",
        "colony_forming_units",
        "economic_threshold",
        "serial_dilution",
    ),
    maturity=Maturity.COMMERCIAL,
    risk_tier=RiskTier.REGULATED,
    scale=Scale.FIELD,
    domains=(Domain.FOOD, Domain.ENVIRONMENT),
    regulatory_status=RegulatoryStatus.AUTHORISED,
    regulations=(
        "EU Regulation (EC) No 1107/2009 on plant protection products",
        "EU Regulation (EU) 2022/1439 data requirements for microorganisms",
        "EU Directive 2009/128/EC on sustainable pesticide use",
        "US EPA biopesticide registration under FIFRA",
    ),
    standards=(
        "EPPO efficacy evaluation standards",
        "OECD guidance on microbial pest control agents",
        "IOBC guidelines for testing effects on beneficial organisms",
    ),
    milestones=(
        Milestone(1901, "Ishiwata isolates the bacterium later named Bacillus thuringiensis"),
        Milestone(1938, "First commercial Bt product sold in France"),
        Milestone(1960, "Integrated pest management formalised as a concept"),
        Milestone(1970, "Pheromone mating disruption demonstrated in orchards"),
        Milestone(1995, "Baculovirus products registered for major lepidopteran pests"),
        Milestone(2017, "First RNA interference based pesticide approved in the United States"),
        Milestone(2022, "EU streamlines data requirements for microbial actives"),
    ),
    sdgs=(2, 12, 15),
    glossary=(
        "biopesticide",
        "entomopathogen",
        "pheromone",
        "rna_interference",
        "integrated_pest_management",
        "economic_threshold",
        "non_target_organism",
        "cry_protein",
    ),
    references=("ishiwata1901", "lacey2015", "eppo_efficacy", "bravo2011"),
    related=(
        "green.biofertilisers",
        "green.plant_genetic_engineering",
        "white.microbial_fermentation",
        "grey.environmental_biomonitoring",
        "yellow.food_safety_biotechnology",
    ),
)
