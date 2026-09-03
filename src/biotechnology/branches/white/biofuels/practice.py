# =============================================================================
#  biotechnology.branches.white.biofuels.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by generation, which is the field's own
#  organisation, and each group carries an honest note about its commercial
#  state. That is unusual for this facet and it is deliberate: a list of
#  biofuel applications that does not distinguish what operates at scale from
#  what was announced and abandoned would misinform a reader more than it
#  informed them.
#
#  TECHNOLOGIES follow the lignocellulosic conversion train in order,
#  pretreatment then hydrolysis then fermentation then recovery, because that
#  sequence is where the second generation's difficulty actually lives and
#  because each step creates the problem the next one must solve.
#
#  A NOTE ON ENZYME AND STRAIN WORK. Cellulase production belongs to
#  `white.industrial_enzymes` and xylose-fermenting strain construction to
#  `white.metabolic_engineering`. They appear here only as the requirements
#  this record imposes on those two.
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
#  By generation, with the commercial state stated rather than implied.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- first generation: large, mature, contested ----------------------------
    "Sugarcane ethanol, produced at very large scale for decades and the "
    "clearest case of a favourable energy return in the field",
    "Maize and wheat starch ethanol, the largest volume by production and the "
    "subject of a long unresolved argument about its net energy and emissions",
    "Biodiesel by transesterification of vegetable oils, mature and limited by "
    "the same feedstock competition",
    "Molasses and beet ethanol as regional variants of the same process",
    # -- waste and residues: modest, real, and quietly successful ----------------
    "Hydrotreated esters and fatty acids from used cooking oil and rendered "
    "animal fats, which is currently the principal route to sustainable "
    "aviation fuel and is constrained by feedstock availability rather than by "
    "technology",
    "Biogas and upgraded biomethane from anaerobic digestion of manure, sewage "
    "sludge and food waste, which converts a disposal cost into an energy "
    "supply and is the least disputed application in this record",
    # -- second generation: technically demonstrated, commercially unproven -------
    "Lignocellulosic ethanol from straw, bagasse, corn stover and energy "
    "grasses, demonstrated at commercial scale and then largely withdrawn, as "
    "recorded in `history.py`",
    "Lignin valorisation into materials and chemicals, pursued because "
    "lignocellulosic fuel economics do not close on the fuel alone",
    "Consolidated bioprocessing, in which one organism both secretes the "
    "enzymes and ferments the sugars, which would remove the enzyme cost "
    "entirely and remains a research objective",
    # -- gas and one-carbon feedstocks ------------------------------------------
    "Gas fermentation of steel mill and refinery off-gas to ethanol, "
    "commercially operating and notable for using a feedstock that competes "
    "with nothing",
    "Syngas fermentation from gasified biomass and waste",
    # -- third generation: heavily funded, largely redirected ---------------------
    "Algal lipid and hydrocarbon production, which absorbed substantial "
    "investment in the late 2000s and mostly redirected towards higher value "
    "products, as `blue.algal_biotechnology` records",
    # -- fourth generation and beyond ---------------------------------------------
    "Electrofuels and carbon dioxide derived fuels using renewable electricity, "
    "where the biological step is optional and the economics are set by "
    "electricity price",
    "Biobutanol and isobutanol as higher energy density alternatives to "
    "ethanol that avoid the blend limit",
    "Farnesane and other terpene-derived drop-in fuels, produced by engineered "
    "strains and generally viable only where a specialty market pays more than "
    "a fuel market would",
)


# =============================================================================
#  TECHNOLOGIES
#  The lignocellulosic train in order. Each step creates the next step's
#  problem, and the notes say how.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- breaking the plant cell wall open ------------------------------------
    "Dilute acid, steam explosion and hydrothermal pretreatment, which disrupt "
    "the lignin barrier and in doing so generate the furans and organic acids "
    "that inhibit the fermentation two steps later",
    "Alkaline and organosolv pretreatment, which preserve more of the lignin "
    "for valorisation at higher reagent cost",
    "Ionic liquid and deep eutectic solvent pretreatment, effective and so far "
    "too expensive at fuel scale",
    "Mechanical size reduction, which is unglamorous and a substantial part of "
    "the parasitic energy load",
    # ---- turning polymer into sugar --------------------------------------------
    "Cellulase and hemicellulase cocktails, whose cost per litre of fuel has "
    "remained the principal unresolved barrier for this route",
    "Simultaneous saccharification and fermentation, which removes the sugar as "
    "it is released and thereby relieves the product inhibition of the enzymes",
    "Consolidated bioprocessing by an organism that secretes the enzymes and "
    "ferments the sugars itself",
    # ---- fermenting sugars the organism was not built for ------------------------
    "Engineered pentose-fermenting yeast, since hydrolysis releases xylose "
    "alongside glucose and the standard ethanol yeast does not use it",
    "Inhibitor-tolerant strains selected or evolved against the pretreatment "
    "products, which is why adaptive evolution appears in a fuel process",
    "Thermophilic and anaerobic fermentation, which reduces cooling and "
    "contamination control cost in a margin-critical process",
    # ---- getting the fuel out and making it usable --------------------------------
    "Distillation and molecular sieve dehydration, the largest single energy "
    "consumer in ethanol production and the reason low titre is fatal here "
    "rather than merely undesirable",
    "In situ product removal by gas stripping or pervaporation for butanol, "
    "where product toxicity caps titre far lower than for ethanol",
    "Transesterification and hydrotreating to produce esters and drop-in "
    "hydrocarbons that meet existing fuel specifications",
    "Anaerobic digestion and biogas upgrading to pipeline-quality biomethane",
    # ---- proving what it saved ----------------------------------------------------
    "Life cycle assessment and carbon intensity modelling, including indirect "
    "land use change, which is not an accounting exercise here but the "
    "determinant of whether the fuel may be sold as renewable at all",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "saccharomyces_cerevisiae",  # the ethanol organism, engineered for xylose
    "zymomonas_mobilis",  # higher ethanol yield per cell, narrow substrate range
    "clostridium_acetobutylicum",  # butanol, limited by its own product toxicity
    "clostridium_autoethanogenum",  # gas fermentation from carbon monoxide
    "trichoderma_reesei",  # the source of industrial cellulase cocktails
    "chlamydomonas_reinhardtii",  # the algal model organism for lipid routes
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "distillation",
    "enzymatic_hydrolysis",
    "gas_chromatography",
    "calorimetry",
    "life_cycle_assessment",
    "process_modelling",
    "adaptive_evolution",
)


# =============================================================================
#  CHALLENGES
#  The first is economic rather than technical, and stating it first is the
#  honest ordering for this record.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the one that decides everything ---------------------------------------
    "Competing as a low-value high-volume commodity against a fossil incumbent "
    "with a century of cost optimisation, which means a technically successful "
    "process can still be commercially worthless",
    # -- the biology that resists ------------------------------------------------
    "Lignocellulose recalcitrance, since plant cell walls evolved specifically "
    "to resist microbial degradation and every pretreatment is an attempt to "
    "defeat that evolution at acceptable energy cost",
    "Inhibitors generated by pretreatment, which poison the fermentation that "
    "the pretreatment exists to enable",
    "Enzyme cost per litre of fuel, the principal unresolved barrier to "
    "cellulosic ethanol and the reason consolidated bioprocessing is pursued",
    "Pentose utilisation, since a large fraction of the available sugar is "
    "xylose and the standard ethanol organism ignores it",
    # -- the physics that limits ---------------------------------------------------
    "The stoichiometric ceiling of 0.51 grams of ethanol per gram of glucose, "
    "which means roughly half the feedstock mass leaves as carbon dioxide "
    "before any process inefficiency is counted",
    "Product toxicity, which caps butanol titre far below ethanol and makes in "
    "situ removal a requirement rather than an optimisation",
    "Distillation energy at low titre, which can consume a large share of the "
    "fuel's own energy content",
    # -- the land ------------------------------------------------------------------
    "Feedstock competition with food for land, water and fertiliser, which is "
    "the field's defining controversy and is not resolved by any technical "
    "improvement to the conversion step",
    "Indirect land use change, real in principle, contested in magnitude, and "
    "capable of reversing the apparent benefit of a crop-based fuel",
    "Feedstock collection logistics, since residues are bulky, low in density "
    "and seasonal, which caps the economic radius of a plant",
    # -- the market and the policy --------------------------------------------------
    "The ethanol blend limit in existing vehicle fleets, which caps demand "
    "independently of supply and is why drop-in fuels are pursued",
    "Policy instability and mandates set beyond what the technology could "
    "deliver, which drew investment into capacity that then had no market",
)
