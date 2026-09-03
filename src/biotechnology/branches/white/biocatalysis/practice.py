# =============================================================================
#  biotechnology.branches.white.biocatalysis.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by REACTION CLASS rather than by industry, which is
#  the reverse of `white.industrial_enzymes`. The reason is that a chemist
#  chooses a biocatalytic step by asking what bond needs to be formed, not by
#  asking what sector the product is sold into. Hydrolases come first because
#  they need no cofactor and are therefore where almost every organisation
#  starts.
#
#  TECHNOLOGIES are grouped by the four questions a process chemist actually
#  faces in order: what medium, how is the cofactor paid for, how is the
#  catalyst held, and how are steps combined.
#
#  A NOTE ON WHAT IS ABSENT. Enzyme discovery and enzyme engineering are NOT
#  listed here, although they are obviously used. They belong to
#  `white.industrial_enzymes`, and duplicating them would blur the boundary
#  that both records exist to keep clear.
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
#  Grouped by reaction class, easiest to deploy first.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- hydrolases: no cofactor, so this is where everyone begins -------------
    "Enzymatic production of 6-aminopenicillanic acid with penicillin acylase, "
    "which replaced a route requiring dichloromethane and sub-zero operation "
    "and now runs at tens of thousands of tonnes a year",
    "Lipase-catalysed kinetic resolution of racemic alcohols, amines and "
    "esters, the most widely used single technique in the field",
    "Nitrilase and nitrile hydratase routes to acrylamide and to chiral acids, "
    "where the chemical alternative requires copper catalysis",
    "Esterase and protease steps in peptide and semi-synthetic antibiotic "
    "manufacture, including selective deprotection without touching the rest "
    "of the molecule",
    # -- oxidoreductases: stereocentres, at the price of a cofactor ------------
    "Ketoreductase reduction of prochiral ketones to single-enantiomer "
    "alcohols, used in statin side chain manufacture",
    "Alcohol dehydrogenase and ene reductase steps that set stereocentres "
    "which chemical hydrogenation sets poorly or not at all",
    "Cytochrome P450 and monooxygenase hydroxylation at unactivated carbon "
    "positions, a transformation conventional chemistry performs badly",
    "Steroid hydroxylation by whole fungal cells, the oldest industrial "
    "biocatalytic oxidation and still in use",
    # -- transaminases: chiral amines, which are everywhere in medicines -------
    "Transaminase installation of chiral amine centres, replacing "
    "metal-catalysed asymmetric hydrogenation and its high-pressure equipment",
    "Imine reductase and reductive aminase routes to secondary amines",
    # -- forming carbon skeletons ----------------------------------------------
    "Aldolase and other lyase steps that form carbon-carbon bonds with control "
    "of two stereocentres at once",
    "Engineered carbene and nitrene transferases performing cyclopropanation "
    "and carbon-hydrogen amination, reactions with no natural counterpart",
    "Glycosyltransferase and glycosidase routes to defined oligosaccharides, "
    "including human milk oligosaccharides",
    # -- combining steps --------------------------------------------------------
    "Multi-enzyme cascades that build a complex molecule in one vessel without "
    "isolating intermediates or using protecting groups",
    "Chemoenzymatic routes in which enzymatic and conventional steps alternate, "
    "which is how most real processes are actually built",
    # -- outside pharmaceuticals ------------------------------------------------
    "Enzymatic interesterification of fats and oils, which replaced chemical "
    "interesterification and partial hydrogenation in food manufacture",
    "Biodiesel transesterification by immobilised lipase, avoiding the soap "
    "formation of alkali-catalysed routes",
    "Enzymatic synthesis of flavour and fragrance esters that may be labelled "
    "natural, a legal rather than chemical distinction",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the four questions a process chemist faces, in order.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- what does the reaction run in? --------------------------------------
    "Two-phase aqueous and organic systems, where substrate and product sit in "
    "the organic phase and the enzyme stays in the water",
    "Water-miscible cosolvent systems, traded against the loss of activity that "
    "cosolvent almost always causes",
    "Neat substrate operation with minimal water, which raises volumetric "
    "productivity and removes most of the solvent inventory",
    "Deep eutectic and ionic liquid media for substrates that dissolve in "
    "nothing conventional",
    # ---- who pays for the cofactor? -------------------------------------------
    "In situ cofactor regeneration with a coupled glucose dehydrogenase or "
    "formate dehydrogenase, which is what makes any nicotinamide-dependent "
    "process affordable",
    "Substrate-coupled regeneration using a sacrificial cosubstrate such as "
    "isopropanol, simpler but limited by the equilibrium",
    "Photochemical and electrochemical regeneration, promising and not yet "
    "routine at manufacturing scale",
    # ---- how is the catalyst held? ---------------------------------------------
    "Immobilisation on resin, silica or as cross-linked enzyme aggregates, "
    "which makes the catalyst recoverable and is often what decides economics",
    "Whole-cell biocatalysis, which supplies cofactor regeneration free from "
    "the cell's own metabolism at the cost of a permeability barrier and side "
    "reactions",
    "Packed-bed and continuous-flow reactors, where an immobilised enzyme runs "
    "for months and space-time yield rises sharply",
    # ---- how are the steps combined? --------------------------------------------
    "One-pot cascade design, in which several enzymes operate simultaneously "
    "and an unfavourable equilibrium is pulled by the next step consuming the "
    "product",
    "In situ product removal by extraction, resin adsorption or distillation, "
    "the standard answer to product inhibition",
    "Biocatalytic retrosynthesis software that proposes enzymatic "
    "disconnections alongside chemical ones",
    "Compartmentalisation of incompatible steps in flow, so that reactions "
    "which cannot share a vessel can still share a route",
)


# =============================================================================
#  ORGANISMS
#  Whole-cell hosts and the classic source organisms for the reaction classes
#  above.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "escherichia_coli",  # the standard whole-cell biocatalyst chassis
    "saccharomyces_cerevisiae",  # reductions, and a food-grade whole-cell option
    "candida_antarctica",  # source of the most used industrial lipase
    "rhodococcus_rhodochrous",  # nitrile hydratase, acrylamide manufacture
    "aspergillus_niger",  # hydrolases and whole-cell transformations
    "pseudomonas_putida",  # oxidative biocatalysis and solvent tolerance
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "directed_evolution",
    "protein_expression",
    "chromatography",
    "mass_spectrometry",
    "nuclear_magnetic_resonance",
    "high_throughput_screening",
    "flow_chemistry",
    "process_modelling",
)


# =============================================================================
#  CHALLENGES
#  The first three are the ones that actually kill routes, in the order a
#  project usually meets them.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the medium ------------------------------------------------------------
    "Substrate solubility, since enzymes work in water and most organic "
    "substrates do not dissolve in it, which caps substrate loading and "
    "therefore volumetric productivity",
    # -- the cofactor -----------------------------------------------------------
    "Cofactor cost, which exceeds product value unless the cofactor turns over "
    "thousands of times, making cofactor total turnover rather than enzyme "
    "turnover the governing economic figure",
    # -- the equilibrium and the product ----------------------------------------
    "Unfavourable equilibria in transaminase and other transfer reactions, "
    "which must be pulled by removing or consuming the product rather than by "
    "adding more catalyst",
    "Product and substrate inhibition, which caps conversion and forces either "
    "in situ product removal or dilute operation",
    # -- the starting point -----------------------------------------------------
    "Absence of any natural enzyme for a wanted transformation, which leaves "
    "directed evolution with nothing to start from and is the principal reason "
    "some disconnections remain chemical",
    # -- the development cost ---------------------------------------------------
    "Development time for a bespoke enzyme measured in months against a "
    "chemical catalyst that can be bought from a catalogue, which is decisive "
    "on short project timelines",
    # -- the regulatory lock ----------------------------------------------------
    "The cost of changing a route once it is in a regulatory dossier, which "
    "means the choice between enzymatic and chemical is effectively made once, "
    "early, and then fixed for the product's commercial life",
    # -- what remains in the product ---------------------------------------------
    "Residual protein, host cell DNA and endotoxin specifications for material "
    "made by a biocatalytic step, which is a purification burden a metal "
    "catalyst does not impose in the same form",
    # -- comparing honestly -------------------------------------------------------
    "Comparison against the chemical alternative on a full life cycle basis "
    "rather than on solvent volume alone, since fermenting the enzyme and "
    "growing its feedstock carry their own burden",
)
