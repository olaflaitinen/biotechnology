# =============================================================================
#  biotechnology.branches.yellow.cultivated_meat.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS in this record require care, because rule 6 forbids listing an
#  aspiration as an application. Most of what is written about cultivated meat
#  describes products that do not exist.
#
#  THE LIST IS THEREFORE ORDERED BY WHAT HAS ACTUALLY BEEN DONE. The first
#  group has been sold to the public somewhere. The second has been produced
#  and demonstrated but not sold. The third is where the field's effort goes
#  and where nothing has yet been achieved at any scale, and it is labelled as
#  such rather than presented alongside the others.
#
#  A reader who notices that the first group is short and concerns formed
#  products rather than cuts of meat has understood the state of the field.
#
#  ORGANISMS are the species whose cells are cultured, and the note on each
#  says why it was chosen, which is usually cell line availability or
#  regulatory path rather than culinary importance.
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
#  Ordered by what has actually been done. Group three is labelled honestly.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- sold to the public somewhere -------------------------------------------
    "Cultivated chicken sold in Singapore following approval in 2020, in small "
    "volumes and in formed rather than whole-cut products",
    "Cultivated chicken approved for sale in the United States in 2023 and "
    "offered through restaurants at limited scale",
    "Cultivated pet food, which reached market in some jurisdictions ahead of "
    "human food because the regulatory path is shorter and the consumer "
    "acceptance question does not arise in the same form",
    # -- produced and demonstrated, not sold ------------------------------------
    "Cultivated beef in formed products, demonstrated publicly since 2013 and "
    "not commercially available",
    "Hybrid products combining cultivated animal fat with plant protein, which "
    "use the cultivated component for flavour rather than for bulk and are the "
    "most plausible near-term route to market",
    "Cultivated fat as an ingredient, which is technically easier than muscle "
    "because adipocytes require no alignment and because fat carries much of "
    "what is recognised as meat flavour",
    "Cultivated seafood, including finfish and crustacean cells, where the "
    "argument connects to the wild stock pressure in "
    "`blue.aquaculture_biotechnology`",
    # -- the objective, and nothing has been achieved at scale --------------------
    "Structured whole cuts requiring scaffolding, vascularisation and "
    "co-culture of muscle, fat and connective tissue, which remains the "
    "field's stated objective and has not been produced at any commercial "
    "scale",
    "Production at tonne rather than kilogram scale, which no facility has yet "
    "demonstrated and which the cost structure in `metrics.py` explains",
    "Price parity with commodity meat, which no published figure has "
    "approached and which is the condition on every environmental and welfare "
    "argument made for the field",
    # -- the parts that are genuinely working ------------------------------------
    "Food-grade growth medium development, which is where most of the field's "
    "technical progress has actually occurred and where the cost reductions "
    "have been real",
    "Cell line banking and characterisation for food use, which is "
    "infrastructure the field did not have and now does",
)


# =============================================================================
#  TECHNOLOGIES
#  The four unsolved problems, in the order they dominate cost.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- the medium, which is the dominant cost --------------------------------
    "Serum-free medium formulation, which removed the foetal bovine serum that "
    "made the whole proposition incoherent, since a meat alternative cannot "
    "depend on a slaughterhouse product",
    "Food-grade replacement of pharmaceutical-grade medium components, which is "
    "the largest single cost reduction available and is a purity specification "
    "question rather than a biological one",
    "Recombinant growth factor production by microbial fermentation, which "
    "links this record directly to `yellow.precision_fermentation` and is where "
    "the remaining medium cost concentrates",
    "Medium recycling and perfusion, recovering unconsumed components rather "
    "than discarding spent medium",
    "Plant hydrolysate and low-cost nutrient sources as partial replacements",
    # ---- the cells, which are the product rather than the factory ---------------
    "Cell line establishment from biopsy, and banking under food-appropriate "
    "conditions",
    "Immortalisation or selection of spontaneously immortalised lines, which "
    "makes continuous production practical and raises a regulatory and "
    "consumer question the field has not had in public",
    "Adaptation to suspension growth, which removes the need for a surface and "
    "is the single change that would most simplify scale-up",
    "Differentiation control into myotubes and adipocytes, since undifferentiated "
    "cells are biomass rather than meat",
    # ---- the vessel, at a scale nobody has built --------------------------------
    "Stirred tank and perfusion bioreactor design for shear-sensitive animal "
    "cells at food volumes, which is `white.bioprocess_engineering` applied to "
    "a product worth a thousandth as much per kilogram",
    "Microcarrier culture, including edible microcarriers that need not be "
    "removed from the product",
    "Oxygen transfer and metabolite removal at high cell density, where lactate "
    "and ammonia accumulation limit the achievable density",
    # ---- the structure, which is a separate problem again -------------------------
    "Edible scaffolds from plant protein, alginate or decellularised material, "
    "which give cells something to align on",
    "Co-culture of muscle, fat and connective tissue, since a cut of meat is "
    "several tissues rather than one",
    "Perfusion and vascularisation approaches for thick constructs, which is "
    "the same diffusion limit `red.regenerative_medicine` records and the same "
    "unsolved problem",
    "Three-dimensional printing and fibre alignment for whole-cut structure",
)


# =============================================================================
#  ORGANISMS
#  Why each species, which is usually about cell lines rather than cuisine.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "gallus_gallus",  # chicken; the approved products, and immortal lines exist
    "bos_taurus",  # beef; the 2013 demonstration and the largest welfare argument
    "sus_scrofa",  # pig; well-characterised cell lines from agricultural research
    "coturnix_japonica",  # quail; a research model with convenient cell biology
    "danio_rerio",  # zebrafish; the cell biology model behind cultivated seafood
    "escherichia_coli",  # produces the recombinant growth factors the medium needs
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "cell_culture",
    "bioreactor_cultivation",
    "tissue_engineering",
    "flow_cytometry",
    "immunostaining",
    "mass_spectrometry",
    "sensory_analysis",
    "life_cycle_assessment",
)


# =============================================================================
#  CHALLENGES
#  Cost first, and the note explains why volume does not fix it.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the cost structure, which is the whole difficulty ----------------------
    "Growth medium cost, which dominates the cost of goods and which falls only "
    "if the composition changes, since it is a consumable input rather than a "
    "fixed cost that volume spreads",
    "A scale-up curve that does not behave like the ones the projections were "
    "borrowed from, because the two dominant costs are a purchased consumable "
    "and capital for capacity that does not exist, neither of which falls "
    "automatically with production volume",
    "Capital cost of food-scale animal cell bioreactor capacity, which has "
    "never been built and for which the pharmaceutical industry's equipment is "
    "sized for grams rather than tonnes",
    # -- the biology that resists -------------------------------------------------
    "Shear sensitivity of animal cells, which limits agitation and therefore "
    "oxygen transfer, in direct tension with the cell densities the economics "
    "require",
    "Replicative senescence in primary cells, and the regulatory and consumer "
    "questions raised by the immortalised lines that avoid it",
    "Metabolite accumulation, particularly lactate and ammonia, which caps "
    "achievable cell density independently of nutrient supply",
    "Contamination risk in an open-ended culture with no antibiotic use and no "
    "terminal sterilisation of the product",
    # -- structure, which is a different problem ------------------------------------
    "Diffusion limits in thick constructs, which is the same hundred to two "
    "hundred micrometre oxygen limit `red.regenerative_medicine` is organised "
    "around and which no cultivated meat process has solved either",
    "Co-culture of multiple tissue types at different differentiation rates",
    # -- proving the environmental claim -----------------------------------------------
    "Genuine uncertainty in the life cycle assessment, where published results "
    "differ on whether cultivated meat beats conventional beef and the answer "
    "depends chiefly on the energy source and on how medium inputs are "
    "produced",
    # -- and the constraints that are not technical ------------------------------------
    "Outright prohibition of sale in several jurisdictions on cultural and "
    "political grounds, which no technical progress addresses",
    "Consumer acceptance of a product grown from cells, which surveys measure "
    "inconsistently and which no approved market has yet tested at scale",
    "Naming and labelling disputes, including whether the product may be called "
    "meat, which are being decided by legislatures rather than by composition",
)
