# =============================================================================
#  biotechnology.branches.green.biofertilisers
# -----------------------------------------------------------------------------
#  GREEN BIOTECHNOLOGY  ->  BIOFERTILISERS AND PLANT-GROWTH-PROMOTING MICROBES
#
#  IN ONE SENTENCE, FOR ANYONE
#  Some soil microbes pull nitrogen out of the air or unlock phosphate the
#  plant cannot reach, and feed it to the roots. Biofertilisers are those
#  microbes, packaged and applied deliberately.
#
#  THE NUMBER THAT FRAMES THIS MODULE
#  Manufacturing synthetic nitrogen fertiliser by the Haber-Bosch process
#  consumes on the order of one to two per cent of global primary energy and
#  supplies the nitrogen in roughly half the protein eaten by humanity. Any
#  biological substitution therefore matters at planetary scale even if it
#  replaces only part of the load.
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
    key="biofertilisers",
    name="Biofertilisers and Plant-Growth-Promoting Microbes",
    aliases=("biofertilizer", "inoculant", "rhizobium", "pgpr", "mycorrhiza"),
    summary=(
        "Living microbial inoculants that fix nitrogen, solubilise phosphate "
        "or stimulate root growth, substituting for part of the synthetic "
        "fertiliser load."
    ),
    description=(
        "Biofertilisers are formulated preparations of living microorganisms "
        "applied to seed, root or soil in order to improve nutrient "
        "availability. Four functional groups dominate. Symbiotic nitrogen "
        "fixers, chiefly Rhizobium and Bradyrhizobium, form root nodules on "
        "legumes and reduce atmospheric dinitrogen to ammonia using the "
        "nitrogenase enzyme complex, an oxygen-sensitive reaction protected "
        "inside the nodule by leghaemoglobin. Free-living and associative "
        "fixers such as Azotobacter and Azospirillum fix at lower rates "
        "without nodulation. Phosphate-solubilising bacteria and fungi secrete "
        "organic acids and phosphatases that release phosphorus bound to "
        "calcium, iron or aluminium and otherwise unavailable to roots. "
        "Arbuscular mycorrhizal fungi colonise root cortical cells and extend "
        "hyphae far beyond the depletion zone, functioning as an extension of "
        "the root system in exchange for photosynthate. A fifth, looser "
        "category - plant-growth-promoting rhizobacteria - acts through "
        "hormone production, siderophore-mediated iron acquisition and "
        "suppression of pathogens rather than through nutrient supply as such."
    ),
    plain_language=(
        "Air is nearly four-fifths nitrogen, and plants need nitrogen, but "
        "they cannot use it straight from the air. Certain bacteria can. If "
        "those bacteria live in little swellings on a bean plant's roots, they "
        "capture nitrogen from the air and hand it to the plant, and the plant "
        "feeds them sugar in return. Other microbes act like a spade, "
        "unlocking nutrients already in the soil that are chemically stuck. "
        "Biofertilisers are these helpful microbes, grown in a factory and "
        "added to the seed or the soil on purpose."
    ),
    analogy=(
        "Fertiliser is delivering groceries to the door. A biofertiliser is "
        "installing a tenant in the basement who grows food and shares it, "
        "and who keeps doing so all season without another delivery. The "
        "catch is that tenants are alive: they can arrive dead, refuse to "
        "settle in, or be outcompeted by whoever already lives there."
    ),
    why_it_matters=(
        "Synthetic nitrogen fertiliser is energy-intensive to make, expensive "
        "to buy and, when it runs off, the primary cause of eutrophication in "
        "rivers and coastal seas. Biological fixation in a well-nodulated "
        "legume crop can supply the equivalent of one to three hundred "
        "kilograms of nitrogen per hectare per year at essentially no "
        "emissions cost. For farmers facing volatile fertiliser prices, a "
        "few euro of inoculant against a hundred euro of urea is an obvious "
        "trade - when the product actually works, which is the honest "
        "qualifier this whole sector lives with."
    ),
    applications=(
        "Rhizobium seed inoculation of soybean, chickpea and groundnut",
        "Arbuscular mycorrhizal inoculation of orchards and vineyards",
        "Phosphate-solubilising bacteria in phosphorus-fixing soils",
        "Azospirillum inoculation of cereals and grasses",
        "Consortium products combining fixers, solubilisers and biocontrol",
        "Biofertiliser use in organic and low-input farming systems",
        "Restoration of degraded land through microbial reintroduction",
        "Seed coating and pelleting for mechanised sowing",
    ),
    technologies=(
        "Carrier-based formulation in peat, vermiculite or biochar",
        "Liquid and freeze-dried inoculant formulations",
        "Strain selection for competitiveness against native populations",
        "Rhizosphere microbiome profiling by amplicon sequencing",
        "nif and nod gene characterisation",
        "On-seed polymer coating and osmoprotectants",
        "Viability and shelf-life testing by plate count",
        "Nitrogen isotope dilution to quantify fixation in the field",
    ),
    organisms=(
        "rhizobium_leguminosarum",
        "bradyrhizobium_japonicum",
        "azospirillum_brasilense",
        "azotobacter_chroococcum",
        "rhizophagus_irregularis",
        "bacillus_subtilis",
        "glycine_max",
    ),
    techniques=(
        "fermentation",
        "microbial_plate_count",
        "amplicon_sequencing",
        "pcr",
        "microscopy",
        "isotope_analysis",
    ),
    challenges=(
        "Field results far less consistent than glasshouse results",
        "Survival of live cells through storage, heat and seed treatment chemicals",
        "Competition from established native soil populations",
        "Quality control in markets where unregulated products are common",
        "Difficulty proving efficacy claims to a regulatory standard",
        "Nitrogen fixation still confined largely to legumes",
    ),
    metrics=(
        Metric(
            name="Viable cell count",
            symbol="CFU/g",
            unit="colony forming units per gram",
            typical="1e8 - 1e9 CFU/g at manufacture",
            formula="colony_forming_units",
            evidence=EvidenceLevel.CONSENSUS,
            note="Most national standards set a minimum at point of sale, not manufacture.",
        ),
        Metric(
            name="Biological nitrogen fixation",
            symbol="BNF",
            unit="kg N/ha/year",
            typical="30 - 300 kg N/ha/year in legumes",
            formula="nitrogen_fixation_rate",
            evidence=EvidenceLevel.REVIEWED,
        ),
        Metric(
            name="Nodule number and mass",
            symbol="N_nod",
            unit="nodules per plant",
            typical="10 - 100 per plant",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Mycorrhizal colonisation",
            symbol="M%",
            unit="% root length colonised",
            typical="20 - 80 %",
            formula="root_colonisation",
            evidence=EvidenceLevel.CONSENSUS,
        ),
        Metric(
            name="Nitrogen use efficiency",
            symbol="NUE",
            unit="kg yield per kg N applied",
            typical="20 - 60 kg/kg",
            formula="nutrient_use_efficiency",
            evidence=EvidenceLevel.REVIEWED,
        ),
    ),
    formulas=(
        "colony_forming_units",
        "nitrogen_fixation_rate",
        "nutrient_use_efficiency",
        "root_colonisation",
        "serial_dilution",
        "exponential_growth",
    ),
    maturity=Maturity.COMMERCIAL,
    risk_tier=RiskTier.CONTROLLED,
    scale=Scale.FIELD,
    domains=(Domain.FOOD, Domain.ENVIRONMENT),
    regulatory_status=RegulatoryStatus.AUTHORISED,
    regulations=(
        "EU Regulation (EU) 2019/1009 on fertilising products",
        "EU Regulation (EC) No 834/2007 and 2018/848 on organic production",
        "National biofertiliser quality and registration standards",
        "Cartagena Protocol where a strain is genetically modified",
    ),
    standards=(
        "FAO guidelines on the use of biofertilisers",
        "Bureau of Indian Standards specifications for carrier-based inoculants",
        "ISO 11063 soil DNA extraction for community analysis",
    ),
    milestones=(
        Milestone(1888, "Beijerinck isolates the root nodule bacterium"),
        Milestone(1895, "First commercial legume inoculant sold as Nitragin"),
        Milestone(1913, "Haber-Bosch process industrialises synthetic nitrogen"),
        Milestone(1960, "Nitrogenase enzyme complex characterised"),
        Milestone(1975, "Arbuscular mycorrhizal inoculum produced commercially"),
        Milestone(2005, "Rhizosphere microbiome sequencing becomes routine"),
        Milestone(2019, "EU fertilising products regulation creates a single market category"),
    ),
    sdgs=(2, 12, 15),
    glossary=(
        "nitrogen_fixation",
        "rhizosphere",
        "nodule",
        "mycorrhiza",
        "inoculant",
        "siderophore",
        "symbiosis",
        "eutrophication",
    ),
    references=("beijerinck1888", "vessey2003", "smith2008", "fao_biofertiliser"),
    related=(
        "green.biopesticides",
        "brown.soil_microbiome_restoration",
        "grey.bioaugmentation",
        "grey.biodiversity_conservation",
        "blue.seaweed_biotechnology",
    ),
)
