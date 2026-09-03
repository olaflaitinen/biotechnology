# =============================================================================
#  biotechnology.branches.yellow.precision_fermentation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by HOW LONG THE PRODUCT HAS BEEN ON THE MARKET,
#  oldest first, because that ordering is the record's principal argument. The
#  first group has been eaten for decades without controversy, and the last is
#  the one that generates the coverage. Presenting them by product category
#  would hide the fact that this is a mature technology being applied to a new
#  target rather than a new technology.
#
#  A reader who notices that most cheese has been made with a
#  fermentation-derived enzyme since the 1980s, and that this is listed in the
#  same record as the products described as revolutionary, has understood the
#  record.
#
#  ORGANISMS are production hosts, and the note on each says what it is chosen
#  for, since the choice between a bacterium, a yeast and a filamentous fungus
#  is determined by whether the protein needs to be secreted and whether it
#  needs post-translational modification.
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
#  By time on the market, oldest first. The ordering is the argument.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- on the market for decades, unremarked ----------------------------------
    "Chymosin for cheesemaking, produced by fermentation since 1988 and used in "
    "the great majority of cheese made in several countries, which is the "
    "largest and least controversial precision fermentation product in "
    "existence",
    "Vitamin B2 and vitamin B12 by fermentation, which for B12 is the only "
    "practical source for people eating no animal products",
    "Amino acids and vitamins for food and feed fortification, produced this "
    "way at very large scale and rarely described by this name",
    "Food enzymes across baking, dairy and starch processing, which belong "
    "technically to `white.industrial_enzymes` and are made by the same "
    "process as everything else in this record",
    # -- on the market recently, and widely eaten without the label ---------------
    "Heme protein produced by yeast, used to give plant-based meat its colour "
    "and flavour, which is the most widely eaten product in this record that "
    "consumers do not associate with it",
    "Human milk oligosaccharides for infant formula, supplying compounds that "
    "have no other practical source at scale",
    "Sweet-tasting proteins such as brazzein and thaumatin as sugar "
    "alternatives, where the plant source is scarce and geographically "
    "restricted",
    "Fermentation-derived flavour and fragrance compounds including vanillin, "
    "which reduce dependence on scarce plant material",
    # -- reaching the market now, and generating the coverage ----------------------
    "Beta-lactoglobulin and other whey proteins for dairy applications, "
    "approved and sold in several jurisdictions",
    "Caseins, which are harder than whey because they function in a food as an "
    "assembled micelle rather than as an isolated protein",
    "Ovalbumin and other egg proteins for baking and emulsification",
    "Collagen and gelatin produced without animals, for food and for the "
    "materials applications in `blue.marine_biomaterials`",
    "Lactoferrin and other minor milk proteins, where the animal source yields "
    "very little and the fermentation route competes on availability rather "
    "than only on price",
    # -- fats, which are a different problem entirely -------------------------------
    "Fermentation-derived fats and oils, including cocoa butter and dairy fat "
    "equivalents, which are made by whole-cell metabolic engineering rather "
    "than by expressing a single protein and belong here only loosely",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the four questions, and the third is where the cost problem is.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- choosing and building the producer -----------------------------------
    "Host selection between bacterial, yeast and filamentous fungal systems, "
    "decided by whether the protein must be secreted and whether it requires "
    "post-translational modification",
    "Gene design and codon optimisation for the chosen host",
    "Secretion signal and promoter engineering to raise secreted titre, which "
    "is usually a larger commercial lever than any change to the protein",
    "Strain development by classical and genomic methods, drawing on "
    "`white.metabolic_engineering`",
    # ---- making it ------------------------------------------------------------
    "Fed-batch fermentation on sugar feedstock, on the terms "
    "`white.microbial_fermentation` sets out including the overflow metabolism "
    "constraint",
    "Food-grade host and medium selection, since a host with a history of safe "
    "use in food shortens the regulatory path considerably",
    "Scale-up to production volumes, where the cost target is set by an "
    "agricultural commodity rather than by a pharmaceutical",
    # ---- getting it out, which is where the cost sits ----------------------------
    "Downstream recovery and purification, which for a food protein must reach "
    "a cost per kilogram that a pharmaceutical process never has to consider",
    "Removal of host cell protein, DNA and endotoxin to food-grade "
    "specifications, which are less stringent than pharmaceutical ones and are "
    "not absent",
    "Spray drying and formulation into an ingredient a food manufacturer can "
    "actually use",
    # ---- proving it is what it claims to be ---------------------------------------
    "Identity confirmation against the animal protein by mass spectrometry and "
    "sequencing, which is the basis of the substantial equivalence argument",
    "Glycosylation and folding characterisation, since sequence identity does "
    "not guarantee identical behaviour in a food",
    "Functional testing in the actual food matrix, covering gelation, foaming, "
    "emulsification and heat stability, because a protein that is chemically "
    "right and functionally wrong is not an ingredient",
    "Allergenicity assessment, which for an identical protein confirms rather "
    "than removes the allergen status",
)


# =============================================================================
#  ORGANISMS
#  Hosts, and what each is chosen for.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "komagataella_phaffii",  # Pichia; high secreted titre, the dominant host here
    "trichoderma_reesei",  # unmatched secretion capacity, used for chymosin
    "saccharomyces_cerevisiae",  # food-grade history shortens the regulatory path
    "aspergillus_niger",  # filamentous, long food use, high secretion
    "escherichia_coli",  # fastest and cannot glycosylate, so limited here
    "bacillus_subtilis",  # secreting bacterial host with a food-safe record
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "protein_expression",
    "chromatography",
    "mass_spectrometry",
    "spray_drying",
    "functional_testing",
    "immunoassay",
    "life_cycle_assessment",
)


# =============================================================================
#  CHALLENGES
#  Cost first, because it is the only one that has stopped products.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the constraint that decides everything --------------------------------
    "Cost per kilogram against an agricultural commodity, where the comparison "
    "is with a heavily scaled and frequently subsidised industry, and where a "
    "pharmaceutical cost structure is two orders of magnitude too expensive",
    "Downstream processing cost, which for a food ingredient cannot carry the "
    "purification burden that `white.bioprocess_engineering` records as normal "
    "for a therapeutic protein",
    "Capital intensity of fermentation capacity at food volumes, and the "
    "shortage of suitable contract manufacturing capacity",
    # -- identity does not guarantee function -----------------------------------
    "Functionality in a real food matrix, since gelation, foaming and "
    "emulsification depend on folding, glycosylation and accompanying minor "
    "components as well as on sequence",
    "Reproducing assembled structures such as the casein micelle, which is not "
    "a protein but an arrangement of several with calcium and phosphate",
    # -- the regulatory position -------------------------------------------------
    "Full novel food authorisation for a molecule identical to one eaten for "
    "millennia, which is defensible caution and a real barrier to entry that "
    "favours incumbents",
    "Divergent approval timelines and requirements between jurisdictions, so a "
    "product on sale in one market may be years from another",
    "Labelling and naming disputes, including whether a product may be called "
    "milk or cheese, which are decided by law rather than by composition",
    # -- what the product inherits -------------------------------------------------
    "Unchanged allergen status, since an identical protein provokes an "
    "identical response, which must be declared and which limits the market a "
    "product can address",
    # -- the environmental claim needs checking --------------------------------------
    "Sugar feedstock grown on farmland, so the land saving is real and smaller "
    "than commonly claimed, and demonstrable only by full life cycle "
    "assessment against a named dairy or egg benchmark",
    # -- and what people will accept ---------------------------------------------------
    "Consumer acceptance of a genetically modified organism in the production "
    "chain, which chymosin achieved and which newer products cannot assume, "
    "since the objection is frequently to the process rather than to the "
    "molecule",
)
