# =============================================================================
#  biotechnology.branches.white.industrial_enzymes.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by industry, in descending order of market volume,
#  because that ordering carries information: detergents and animal feed are
#  where the tonnes are, while pharmaceutical biocatalysis is where the value
#  per kilogram is. A reader who assumes the medical application is the biggest
#  one has the field backwards.
#
#  Each entry names the enzyme class where it is informative, because a reader
#  who learns that a protease digests protein and a lipase digests fat can then
#  predict most of this list without memorising it.
#
#  ORGANISMS are the production hosts rather than the sources. That distinction
#  matters: an enzyme discovered in a deep-sea vent archaeon is manufactured in
#  Bacillus, because Bacillus secretes protein into the broth and grows on
#  cheap medium. The source organism is a sequence; the host is the factory.
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
#  Ordered by market volume, largest first.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- detergents, the largest market by volume -------------------------------
    "Laundry and dishwashing detergents, where proteases, lipases, amylases "
    "and cellulases together allow effective washing at 30 degrees rather than "
    "60 and therefore about a third of the electricity",
    "Cellulases in detergent that remove the microfibrils responsible for "
    "greying and pilling, which is why enzyme-washed cotton keeps its colour",
    # -- animal feed ------------------------------------------------------------
    "Phytase in pig and poultry feed, which releases phosphorus bound in plant "
    "phytate so that less mined phosphate is added and less phosphorus is "
    "excreted into watercourses",
    "Xylanases and beta-glucanases in feed, which break down cereal fibre that "
    "monogastric animals cannot digest",
    # -- starch and sweeteners ---------------------------------------------------
    "Alpha-amylase and glucoamylase in starch liquefaction and saccharification, "
    "the first stage of nearly every fermentation feedstock",
    "Glucose isomerase in the production of high fructose syrups, one of the "
    "earliest and largest immobilised enzyme processes",
    # -- baking ------------------------------------------------------------------
    "Amylases, xylanases and lipases in baking, which control dough handling, "
    "loaf volume and staling rate",
    "Asparaginase in baking and frying, which reduces acrylamide formation, a "
    "process contaminant, without changing the recipe",
    # -- dairy --------------------------------------------------------------------
    "Chymosin produced by fermentation for cheesemaking, which replaced calf "
    "rennet and was among the first recombinant products in the food chain",
    "Lactase in dairy processing for lactose-free milk",
    # -- textiles and leather ------------------------------------------------------
    "Amylases in textile desizing and cellulases in denim finishing, which "
    "replaced pumice stone abrasion",
    "Proteases in leather bating, replacing part of the sulphide chemistry",
    # -- pulp and paper --------------------------------------------------------------
    "Xylanase pre-bleaching of pulp, which reduces the chlorine-based bleaching "
    "chemistry required for the same brightness",
    # -- fuel and chemicals ------------------------------------------------------------
    "Cellulase and hemicellulase cocktails for lignocellulosic ethanol, where "
    "enzyme cost per litre remains a principal barrier",
    # -- highest value per kilogram, smallest volume ---------------------------------
    "Enzymatic steps in pharmaceutical manufacture, including transaminases, "
    "ketoreductases and nitrilases, which replace multi-step chemical routes "
    "and eliminate solvent",
    "Analytical and diagnostic enzymes, including glucose oxidase in blood "
    "glucose strips and the polymerases underlying `red.molecular_diagnostics`",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the four questions in order: what enzyme, made better how, made
#  how, and used how.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- finding a starting point ---------------------------------------------
    "Screening of culture collections and extremophile isolates from hot "
    "springs, alkaline lakes, polar water and deep-sea vents",
    "Metagenomic library construction from environmental DNA, which reaches the "
    "large majority of organisms that cannot be cultured",
    "Sequence-based mining and structure prediction, which now supply "
    "candidates without any isolation step at all",
    # ---- making it better -----------------------------------------------------
    "Directed evolution by iterative mutagenesis and screening, which requires "
    "no mechanistic understanding and is the reason the field advanced faster "
    "than protein theory did",
    "Rational and semi-rational design using structural information to target "
    "specific residues",
    "Ancestral sequence reconstruction, which frequently yields more thermostable "
    "variants than any modern homologue",
    "Consensus design, which substitutes the most common residue at each "
    "position across a family",
    "Computational design and machine learning models trained on variant "
    "activity data, linking this record to `gold.machine_learning_in_biology`",
    # ---- making it in quantity -------------------------------------------------
    "Submerged fed-batch fermentation of secreting hosts at tens to hundreds of "
    "cubic metres",
    "Signal peptide and promoter engineering to raise secreted titre, which is "
    "usually a larger commercial lever than raising specific activity",
    "Downstream recovery by filtration, ultrafiltration and formulation into "
    "liquid, granulate or spray-dried product",
    # ---- using it well ----------------------------------------------------------
    "Immobilisation by adsorption, covalent attachment, entrapment or "
    "cross-linked enzyme aggregates, which makes the catalyst recoverable and "
    "reusable and is often what makes a process economic",
    "Granulation and coating for detergent products, which is also a worker "
    "safety measure against inhaled enzyme dust",
    "Enzyme cocktail formulation, where several activities are balanced against "
    "one substrate, as in cellulase blends for biomass",
)


# =============================================================================
#  ORGANISMS
#  Production hosts, not sources. See the note in the module header.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "bacillus_subtilis",  # the workhorse secreting host for bacterial enzymes
    "aspergillus_niger",  # the fungal counterpart, high secretion, long history
    "trichoderma_reesei",  # unmatched cellulase secretion, hence biomass enzymes
    "escherichia_coli",  # expression, cloning and most engineering work
    "saccharomyces_cerevisiae",  # display libraries and some secreted products
    "thermus_aquaticus",  # the canonical thermostable source organism
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "chromatography",
    "directed_evolution",
    "protein_expression",
    "x_ray_crystallography",
    "mass_spectrometry",
    "high_throughput_screening",
    "bioassay",
)


# =============================================================================
#  CHALLENGES
#  The first is the one that dominates practice and is routinely
#  underestimated: stability, not activity, is what usually decides a process.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the constraint that actually binds --------------------------------------
    "Operational stability rather than initial activity, because cost per "
    "kilogram of product depends on total turnovers before the catalyst dies, "
    "and a fast enzyme with a short life is worth less than a slow durable one",
    # -- the mismatch with industrial conditions ----------------------------------
    "Tolerance of the conditions industry would prefer to use, meaning organic "
    "solvents, extremes of pH, high substrate loading and high temperature",
    "Inhibition by the product itself, which caps conversion and forces either "
    "product removal in situ or dilute operation",
    # -- the discovery bottleneck ---------------------------------------------------
    "Screening throughput, since a directed evolution campaign is limited by "
    "how many variants can be assayed rather than by how many can be made",
    # -- economics ------------------------------------------------------------------
    "Enzyme cost per litre of product in low-margin applications, which is the "
    "principal unresolved barrier for lignocellulosic biofuel",
    # -- the cofactor problem ---------------------------------------------------------
    "Cofactor dependence in oxidoreductases, where the cofactor costs more than "
    "the product unless it is regenerated in situ",
    # -- safety --------------------------------------------------------------------------
    "Respiratory sensitisation from inhaled enzyme dust, a genuine occupational "
    "hazard that caused serious harm in the detergent industry in the 1960s and "
    "is the reason granulation is standard rather than optional",
    # -- what a customer is allowed to say -------------------------------------------------
    "Regulatory and labelling divergence for enzymes in food between "
    "jurisdictions, including whether a processing aid must be declared",
)
