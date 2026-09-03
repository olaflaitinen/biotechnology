# =============================================================================
#  biotechnology.branches.white.metabolic_engineering.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by how well established the product class is, from
#  the amino acid fermentations that have run since the 1950s to the pathways
#  still looking for a market. That ordering is itself information: a reader
#  who assumes this is a young field is looking at the wrong end of the list.
#  Monosodium glutamate has been made by engineered bacterial fermentation for
#  longer than the discipline has had a name.
#
#  TECHNOLOGIES follow the design, build, test, learn cycle in order, and the
#  grouping is meant to show where the bottleneck now sits. Building a pathway
#  is largely automated. Measuring what the cell then does with it is not. That
#  asymmetry is the single most important thing about how the field currently
#  works.
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
#  Ordered from the longest established to the least settled.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- the oldest and by far the largest -------------------------------------
    "Glutamate and lysine production by Corynebacterium glutamicum, which has "
    "run at industrial scale since the late 1950s and now supplies millions of "
    "tonnes of feed amino acid a year",
    "Threonine, tryptophan and methionine fermentation, which reduce the "
    "protein crop that livestock diets would otherwise require",
    "Vitamin B2, B12 and vitamin C intermediate production, which displaced "
    "multi-step chemical syntheses",
    "Citric, lactic, succinic and itaconic acid production from sugar",
    # -- polymers, where designed pathways proved themselves --------------------
    "1,3-propanediol for polymer manufacture, produced by an engineered "
    "Escherichia coli from glucose in place of a petrochemical route",
    "1,4-butanediol by a pathway assembled from parts and present in no natural "
    "organism, which is the clearest demonstration that metabolism can be "
    "designed rather than only optimised",
    "Lactic acid for polylactic acid, linking this record directly to "
    "`white.biopolymers`",
    # -- pharmaceutical precursors, including the cautionary case ---------------
    "Artemisinic acid in engineered yeast as a precursor to the antimalarial "
    "artemisinin, a technical success and a commercial disappointment recorded "
    "honestly in `history.py`",
    "Precursors for opioid, steroid and terpenoid drug substances, shortening "
    "routes that begin from a plant extract",
    "Isoprenoid and polyketide scaffolds for medicinal chemistry",
    # -- flavour, fragrance and food ingredients --------------------------------
    "Fermentation-derived vanillin, nootkatone, valencene and steviol "
    "glycosides, which reduce dependence on scarce or seasonal plant sources",
    "Human milk oligosaccharides for infant formula, produced by engineered "
    "bacteria rather than isolated from milk",
    "Heme protein for plant-based meat analogues, which sits at the boundary "
    "with `yellow.alternative_proteins`",
    # -- fuels, where the economics are hardest ----------------------------------
    "Farnesene, isobutanol and fatty acid derived fuels and lubricant "
    "precursors, viable where the product commands a specialty price and "
    "difficult where it competes with bulk fuel",
    # -- feedstock at the frontier -------------------------------------------------
    "Gas fermentation of carbon monoxide and carbon dioxide by acetogens, which "
    "converts industrial off-gas into ethanol and acetone",
    "Methanol and formate as one-carbon feedstocks for organisms engineered to "
    "grow on them, which decouples production from agricultural land",
)


# =============================================================================
#  TECHNOLOGIES
#  The design, build, test, learn cycle in order. Note where the automation is
#  and where it is not.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- DESIGN: deciding what to change --------------------------------------
    "Genome-scale metabolic models, which represent every known reaction in an "
    "organism as a stoichiometric matrix",
    "Flux balance analysis and its variants, which predict the flux "
    "distribution that maximises an objective subject to stoichiometry and "
    "uptake constraints",
    "Metabolic control analysis, which quantifies how much control each enzyme "
    "actually exerts and is the formal answer to the rate-limiting step "
    "assumption",
    "Elementary mode and pathway enumeration for finding routes that do not "
    "exist in any single organism",
    "Retrobiosynthesis software that proposes enzymatic routes to a target "
    "compound, the biological counterpart of chemical retrosynthesis",
    # ---- BUILD: making the change, and this part is now cheap ------------------
    "Multiplexed genome editing and recombineering, which introduce many "
    "changes in one round",
    "Promoter, ribosome binding site and copy number libraries for tuning "
    "expression across a pathway rather than maximising any single enzyme",
    "Pathway refactoring, in which native regulation is stripped out and "
    "replaced with parts that behave predictably",
    "Enzyme scaffolding and compartmentalisation, which hold sequential "
    "enzymes close together or confine a toxic intermediate",
    # ---- TEST: this is where the bottleneck now sits ----------------------------
    "Carbon-13 metabolic flux analysis, which measures internal fluxes from "
    "labelling patterns rather than inferring them, and is the only direct "
    "measurement of what the cell is actually doing",
    "Biosensors and transcription factor based reporters that couple product "
    "concentration to a fluorescent or growth signal, converting a slow assay "
    "into a sortable one",
    "Growth-coupled selection, in which the strain is designed so that making "
    "the product is necessary for growth, which turns evolution from an "
    "adversary into a collaborator",
    "Adaptive laboratory evolution for tolerance to the product, the solvent or "
    "the feedstock",
    # ---- LEARN: closing the loop ------------------------------------------------
    "Automated design, build, test and learn foundries operating at hundreds of "
    "strains per cycle",
    "Machine learning on strain performance data to propose the next round, "
    "linking to `gold.machine_learning_in_biology`",
)


# =============================================================================
#  ORGANISMS
#  Each entry names why that chassis rather than another.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "escherichia_coli",  # fastest to engineer, best characterised, poor at low pH
    "saccharomyces_cerevisiae",  # tolerant, food-grade, has organelles to exploit
    "corynebacterium_glutamicum",  # the amino acid workhorse, secretes readily
    "yarrowia_lipolytica",  # lipid and oleochemical routes, high acetyl-CoA flux
    "bacillus_subtilis",  # secretion, and a long food-safe regulatory record
    "clostridium_autoethanogenum",  # gas fermentation from carbon monoxide
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "genome_editing",
    "dna_assembly",
    "fermentation",
    "mass_spectrometry",
    "next_generation_sequencing",
    "flux_analysis",
    "high_throughput_screening",
    "process_modelling",
)


# =============================================================================
#  CHALLENGES
#  The first two are limits no engineering passes. The third is the one that
#  most often defeats a strain that worked perfectly in the laboratory.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the absolute limits ---------------------------------------------------
    "Stoichiometric yield ceilings, since carbon, redox and energy balances set "
    "a maximum product per unit of feedstock that no amount of engineering can "
    "exceed, and the useful question is what fraction of it a strain achieves",
    "Redox and energy imbalance in a designed pathway, where a route that "
    "works on paper consumes cofactors the cell cannot supply at that rate",
    # -- the one that kills strains at scale ------------------------------------
    "Genetic instability under production conditions, because a strain that "
    "diverts carbon from growth is outcompeted by any mutant that stops doing "
    "so, and a production fermentation lasts many generations",
    # -- the cell fights back ----------------------------------------------------
    "Product toxicity, which caps titre for alcohols, acids and solvents long "
    "before the pathway runs out of capacity",
    "Native regulation that resists the change, since the cell evolved feedback "
    "control specifically to prevent overproduction of its own metabolites",
    "Competing branch pathways that divert intermediates, where deleting them "
    "often impairs growth because they were there for a reason",
    # -- where the field's time actually goes -------------------------------------
    "Measurement rather than construction, since building a strain is now "
    "cheap and automated while determining what it does internally is slow, "
    "which makes the test step the rate-limiting one for the discipline itself",
    "The gap between a shake flask and a production fermenter, where oxygen "
    "transfer, mixing and gradients change the answer, as recorded in "
    "`white.bioprocess_engineering`",
    # -- what the process runs on --------------------------------------------------
    "Feedstock cost and its competition with food and land use, which is "
    "frequently the difference between a working strain and a viable business",
)
