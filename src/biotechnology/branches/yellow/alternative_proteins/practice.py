# =============================================================================
#  biotechnology.branches.yellow.alternative_proteins.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped BY PROTEIN SOURCE, because the four sources have
#  different economics, different regulatory positions and different acceptance
#  problems, and grouping by product type would suggest they are
#  interchangeable inputs. They are not: a fungal protein arrives fibrous and a
#  pea protein has to be made fibrous, which is the difference between a
#  fermentation and an extrusion business.
#
#  TECHNOLOGIES are grouped by the four things that have to be right at once
#  for a product to be bought twice: structure, flavour, fat and nutrition. The
#  structure group is the largest because it is where the engineering is, and
#  the nutrition group is the smallest because, as `narrative.py` argues,
#  nutrition was never the hard part.
#
#  ORGANISMS include the crop species, which is unusual for this facet and is
#  correct here: the protein source is an agricultural commodity and the choice
#  between soy and pea is driven by allergen labelling and by regional
#  supply rather than by protein chemistry.
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
#  By protein source, since the four have different economics and acceptance.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- plant protein: the largest, the cheapest, the most contested -----------
    "Extruded plant protein burgers, mince and pieces from soy, pea and wheat "
    "gluten, which is the category that grew rapidly to 2019 and then "
    "contracted",
    "High-moisture extrudates approaching whole-muscle structure, which is the "
    "technical frontier of plant protein texturisation",
    "Plant-based dairy analogues from soy, oat, almond and pea, a category that "
    "has grown steadily and quietly while meat analogues struggled, largely "
    "because milk is easier to imitate than muscle",
    "Traditional plant protein foods including tofu, tempeh and seitan, which "
    "predate the sector by centuries and which are neither ultra-processed nor "
    "expensive",
    "Pulse and legume protein isolates as ingredients in conventional food "
    "manufacture, which is the largest volume use and attracts none of the "
    "attention",
    # -- fungal protein: fibrous by nature, and forty years old ------------------
    "Mycoprotein from filamentous fungal fermentation, sold since 1985, whose "
    "hyphal structure gives fibrousness without extrusion",
    "Fermented fungal biomass products including tempeh-style and "
    "koji-fermented preparations",
    "Mycelium grown on solid substrate into whole-cut structures, which "
    "approaches whole-muscle texture by a route entirely different from "
    "extrusion",
    # -- insect protein: efficient, and blocked by acceptance --------------------
    "Insect meal in aquaculture and poultry feed, which is where nearly all "
    "insect protein actually goes and where no consumer acceptance question "
    "arises",
    "Insect protein for human food, authorised for several species in Europe "
    "and constrained by acceptance rather than by regulation or by cost",
    "Insect rearing on food-industry side streams, which converts a waste "
    "stream into feed protein and is the strongest environmental case in this "
    "record",
    # -- microbial and gas-derived protein ----------------------------------------
    "Single cell protein from bacteria and yeast for animal feed, produced at "
    "scale and mostly invisible to consumers",
    "Gas-fermented protein from carbon dioxide, hydrogen or methane, which "
    "requires no farmland at all and which is the most land-efficient protein "
    "in this record",
    "Algal protein, which belongs to `blue.algal_biotechnology` for its "
    "production and appears here as an ingredient",
)


# =============================================================================
#  TECHNOLOGIES
#  The four things that must be right at once. Structure is the largest group.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- structure, which is the actual engineering ---------------------------
    "High-moisture extrusion, in which protein is hydrated, heated, sheared and "
    "cooled in a long die so that molecules align into anisotropic fibres, "
    "which is the core technology of the sector",
    "Low-moisture extrusion producing textured vegetable protein, the older and "
    "cheaper process behind most mince-style products",
    "Shear cell and Couette cell processing, which achieves alignment by "
    "controlled shear rather than by a die",
    "Electrospinning and wet spinning of protein fibres, which gives fine "
    "control at a scale that is not yet commercial",
    "Three-dimensional printing of layered structures for whole-cut analogues",
    "Fungal fermentation and mycelium cultivation, which produce a fibrous "
    "structure biologically and therefore skip this entire group",
    # ---- flavour, which decides repeat purchase --------------------------------
    "Maillard reaction precursor systems that generate meat-like flavour during "
    "cooking rather than adding it beforehand",
    "Heme and other iron-binding proteins from `yellow.precision_fermentation`, "
    "which supply the specific note plant protein lacks",
    "Off-flavour masking and removal, since pea and soy protein carry beany and "
    "bitter notes that are the first thing a consumer notices",
    "Enzymatic and fermentative treatment of protein isolates to improve "
    "flavour and reduce antinutritional factors",
    # ---- fat, which carries much of what people call meat flavour ---------------
    "Fat structuring by oleogels, emulsion gels and encapsulation, so that fat "
    "renders during cooking as animal fat does rather than melting out at once",
    "Fermentation-derived and cultivated fats, which link this record to "
    "`yellow.cultivated_meat`",
    # ---- nutrition, which was never the hard part -------------------------------
    "Protein blending to complete the amino acid profile, since a single plant "
    "source is usually limiting in one essential amino acid",
    "Fortification with vitamin B12, iron and zinc, which is necessary because "
    "the animal product being replaced supplied them in absorbable form",
    "Antinutritional factor reduction, including the phytate that binds the "
    "iron and zinc just added",
)


# =============================================================================
#  ORGANISMS
#  Crop species included deliberately, since the protein source is an
#  agricultural commodity.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "glycine_max",  # soy; the cheapest and best-functioning protein, and an allergen
    "pisum_sativum",  # pea; chosen largely because it is not a labelled allergen
    "triticum_aestivum",  # wheat gluten; excellent texture, unusable for coeliacs
    "fusarium_venenatum",  # the mycoprotein fungus, fibrous without extrusion
    "hermetia_illucens",  # black soldier fly; converts side streams into feed protein
    "tenebrio_molitor",  # mealworm; the first insect authorised as a novel food in the EU
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "extrusion",
    "fermentation",
    "protein_isolation",
    "sensory_analysis",
    "mechanical_testing",
    "gas_chromatography",
    "life_cycle_assessment",
    "consumer_testing",
)


# =============================================================================
#  CHALLENGES
#  Repeat purchase first, because it is what actually contracted the sector.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- what decides whether the category survives -----------------------------
    "Repeat purchase, which depends on taste and price and which the sector "
    "demonstrated between 2019 and 2023 is not predicted by trial rates, since "
    "a category can achieve wide trial and contract anyway",
    "Price parity with commodity meat, unreached for most products, against a "
    "competitor that is inexpensive partly because it is supported",
    # -- the engineering that is genuinely hard -----------------------------------
    "Reproducing anisotropic whole-muscle structure from globular plant "
    "proteins, which is a materials problem and the reason extrusion dominates "
    "the technology list",
    "Fat behaviour during cooking, since much of what is recognised as meat "
    "flavour is released from rendering fat rather than from the protein",
    "Off-flavours in pea and soy protein isolates, which are the first thing a "
    "consumer notices and the last thing a specification records",
    # -- the reputational problem the sector did not expect -------------------------
    "Classification as ultra-processed, which placed these products in a "
    "category consumers were being advised to avoid, and which is a fair "
    "description of how the texture is achieved rather than a misunderstanding "
    "to be corrected",
    "Sodium and saturated fat content in formulations designed to match meat's "
    "sensory profile, which undermines the health positioning",
    # -- nutrition, which is easy to get wrong even though it is not the hard part --
    "Incomplete amino acid profiles from single plant sources, requiring "
    "blending",
    "Iron, zinc and vitamin B12 bioavailability, since fortification adds the "
    "nutrient and the plant matrix reduces its absorption",
    "Allergen management, since soy, wheat and increasingly pea are labelled "
    "allergens and the choice between them is a labelling decision as much as "
    "a technical one",
    # -- the environmental claim needs its comparator ---------------------------------
    "Substantiating the environmental case against a named benchmark, since soy "
    "and pea protein carry their own land and water demands and the argument is "
    "comparative rather than absolute",
    # -- and one that has no technical answer ------------------------------------------
    "Consumer acceptance of insect protein in Western markets, which is not a "
    "safety, cost or regulatory problem and which most producers have answered "
    "by selling into animal feed instead",
)
