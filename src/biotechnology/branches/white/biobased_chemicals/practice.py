# =============================================================================
#  biotechnology.branches.white.biobased_chemicals.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by the oxygen principle set out in `narrative.py`,
#  because that grouping is itself the record's main argument. Oxygen-rich
#  targets first, where biology begins most of the way to the product;
#  hydrocarbon targets last, where it does not. A reader who compares the
#  commercial state of the first group with the last will see the principle
#  demonstrated rather than asserted.
#
#  TECHNOLOGIES are grouped by where the value is added: the fermentation, the
#  separation that recovers a dilute product from water, and the catalysis that
#  upgrades it. The middle group is the one that surprises people. For a bulk
#  chemical, recovering the molecule from broth is frequently a larger cost
#  than making it.
#
#  A NOTE ON THE BOUNDARY. Strain construction is `white.metabolic_engineering`
#  and the vessel is `white.bioprocess_engineering`. Polymers made from these
#  building blocks are `white.biopolymers`. This record is the molecule
#  between the fermenter and the polymer plant.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = [
    "APPLICATIONS",
    "TECHNOLOGIES",
    "ORGANISMS",
    "TECHNIQUES",
    "CHALLENGES",
]


# =============================================================================
#  APPLICATIONS
#  Ordered by the oxygen principle: where biology starts closest, first.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- oxygen-rich targets, where biology has a structural advantage ---------
    "Lactic acid production by fermentation, the largest biobased platform "
    "chemical by volume and the feedstock for polylactic acid",
    "1,3-propanediol from glucose, produced commercially for a polyester fibre "
    "whose properties differ from the petrochemical alternative, which is the "
    "clearest case of a biobased route winning on performance rather than on "
    "virtue",
    "1,4-butanediol by a pathway that exists in no natural organism, a solvent "
    "and polymer intermediate previously made only from acetylene or maleic "
    "anhydride",
    "Citric, itaconic and gluconic acid, long-established fermentation products "
    "that predate the biobased label entirely",
    "2,5-furandicarboxylic acid from sugar, a potential replacement for "
    "terephthalic acid in polyesters, still scaling",
    "Bio-based monoethylene glycol for polyester bottles, produced via "
    "bio-ethanol and adopted at scale by consumer brands",
    "Glycerol derivatives including epichlorohydrin, which exploit a cheap "
    "by-product stream from biodiesel manufacture",
    "Levulinic acid, succinic acid and other platform acids proposed as "
    "building blocks, whose mixed commercial record is recorded honestly in "
    "`history.py`",
    # -- nitrogen-containing molecules, where biology is also well placed -------
    "Amino acids for feed, food and chemical use, the oldest and largest "
    "fermentation chemistry in existence",
    "Bio-based acrylamide by nitrile hydratase, which replaced a copper "
    "catalysed route and is a standing example of enzymatic substitution",
    "Fermentation-derived 1,5-pentanediamine and other polyamide monomers",
    # -- speciality and high-value products, where price is not the constraint ---
    "Fragrance and flavour molecules including vanillin, nootkatone and "
    "santalol, where a natural label and a scarce plant source make the "
    "biological route commercially comfortable",
    "Cosmetic ingredients such as squalane produced by engineered yeast, which "
    "is where several fuel programmes profitably redirected themselves",
    "Surfactants including sophorolipids and rhamnolipids, and enzymatically "
    "made sugar esters",
    "Solvents such as ethyl lactate and 2-methyltetrahydrofuran, adopted where "
    "a regulator has restricted the petrochemical alternative",
    # -- hydrocarbon targets, where the principle works against the route --------
    "Bio-ethylene by dehydration of bio-ethanol, technically simple, "
    "commercially marginal, and viable mainly where sugarcane is very cheap",
    "Bio-based aromatics from lignin, pursued for two decades and still without "
    "a large commercial process, since lignin is heterogeneous and its "
    "depolymerisation is unselective",
    "Isoprene, farnesene and terpene hydrocarbons, whose producers have "
    "generally moved upmarket into speciality applications rather than "
    "competing as commodities",
)


# =============================================================================
#  TECHNOLOGIES
#  Where the value is added, and where the cost actually is.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- making the molecule ---------------------------------------------------
    "Fermentation of engineered strains to the target molecule or its immediate "
    "precursor, drawing on `white.metabolic_engineering`",
    "Enzymatic conversion of a biobased intermediate, drawing on "
    "`white.biocatalysis`",
    "Whole-cell biotransformation of a purchased substrate, which avoids "
    "building the pathway from sugar when the substrate is cheap",
    "Gas fermentation of carbon monoxide and carbon dioxide, which supplies "
    "acetate and ethanol as chemical feedstock rather than as fuel",
    # ---- getting it out of the water, which is where the money goes -------------
    "Reactive extraction and back-extraction for organic acids, which must "
    "handle a product that is ionised at the pH the organism prefers",
    "Electrodialysis and bipolar membrane processes for acid recovery, avoiding "
    "the salt waste that neutralisation produces",
    "Crystallisation and antisolvent precipitation, the cheapest recovery route "
    "when the product will cooperate",
    "Simulated moving bed chromatography for separations that a column cannot "
    "do economically in batch",
    "In situ product removal, which relieves inhibition and raises effective "
    "titre simultaneously",
    "Azeotropic and extractive distillation for alcohols and solvents",
    # ---- upgrading it chemically ------------------------------------------------
    "Catalytic hydrogenation and hydrogenolysis of biobased acids and sugars to "
    "diols, which is where chemistry and biology are combined rather than "
    "opposed",
    "Dehydration chemistry converting sugars to furans, and alcohols to "
    "olefins",
    "Oxidation and esterification steps that finish a fermentation product into "
    "a saleable specification",
    "Lignin depolymerisation by catalytic, reductive or oxidative routes, still "
    "the field's least solved problem",
    # ---- proving what it is and what it saved -----------------------------------
    "Radiocarbon determination of biobased carbon content, which distinguishes "
    "recently fixed carbon from fossil carbon in a finished product",
    "Techno-economic analysis and minimum selling price modelling, which is how "
    "a project is killed or funded long before a plant exists",
    "Life cycle assessment against the incumbent petrochemical route, without "
    "which the biobased claim is unsupported",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "escherichia_coli",  # diols, acids, and most engineered pathways
    "saccharomyces_cerevisiae",  # terpenes and speciality molecules, acid tolerant
    "corynebacterium_glutamicum",  # amino acids and diamines
    "aspergillus_niger",  # citric and organic acids, tolerant of low pH
    "yarrowia_lipolytica",  # lipid-derived and oleochemical routes
    "clostridium_autoethanogenum",  # gas fermentation to acetate and ethanol
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "chromatography",
    "distillation",
    "crystallisation",
    "catalysis",
    "gas_chromatography",
    "life_cycle_assessment",
    "process_modelling",
)


# =============================================================================
#  CHALLENGES
#  The first three end more projects than any biological limit.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the market, not the science -------------------------------------------
    "Competing on price against a petrochemical incumbent with a century of "
    "optimisation, depreciated assets and enormous scale, where a technically "
    "excellent process can still be commercially worthless",
    "Exposure to the oil price, since the competitiveness of a biobased route "
    "is set by a commodity nobody in the field controls and can reverse within "
    "a year",
    "Willingness to pay for the biobased attribute, which is frequently zero "
    "outside consumer-facing products, and which is a market question that no "
    "amount of process improvement answers",
    # -- the platform assumption that failed -------------------------------------
    "The platform chemical fallacy, in which a molecule is an excellent "
    "chemical building block and a poor business because the downstream "
    "capacity to consume it was never built",
    # -- where the cost actually is ------------------------------------------------
    "Separation of a dilute product from an aqueous broth, which for a bulk "
    "chemical often exceeds the cost of making it",
    "Salt waste from neutralising an organic acid fermentation, which is a real "
    "and unglamorous environmental burden of the route",
    "Product toxicity and low pH tolerance, which cap titre and therefore make "
    "the separation problem worse",
    # -- capital ---------------------------------------------------------------------
    "Capital intensity, since a plant must be financed and built before any "
    "revenue exists and cannot be scaled incrementally the way a chemical "
    "process line sometimes can",
    "Feedstock price volatility and its competition with food, real but an "
    "order of magnitude smaller than for fuels because the volumes are smaller "
    "and the values higher",
    # -- the target that fights back --------------------------------------------------
    "Removing oxygen to reach hydrocarbon targets, which wastes carbon as "
    "carbon dioxide and is the structural reason bio-based olefins and "
    "aromatics have struggled",
    "Lignin heterogeneity and unselective depolymerisation, which has kept "
    "biobased aromatics unsolved for two decades",
    # -- proving the claim ---------------------------------------------------------------
    "Substantiating an environmental claim, since biobased is not automatically "
    "lower impact and a route needing more energy, land or processing can be "
    "worse than what it replaces",
)
