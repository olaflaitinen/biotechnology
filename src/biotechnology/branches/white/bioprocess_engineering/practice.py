# =============================================================================
#  biotechnology.branches.white.bioprocess_engineering.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by unit operation IN PROCESS ORDER, from the vessel
#  to the vial, rather than by industry. That ordering is the point of the
#  record: a reader should be able to follow a molecule from broth to product
#  and see how many operations stand between the two, because that count is
#  what the yield arithmetic acts on.
#
#  Note how few entries concern the fermenter and how many concern what happens
#  afterwards. That proportion is roughly the proportion of the cost, and it is
#  the opposite of how the subject is usually described.
#
#  TECHNOLOGIES are grouped by the four questions the discipline answers: how
#  to make it bigger, how to know what is happening, how to make the plant
#  flexible, and how to prove it does the same thing every time.
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
#  Unit operations in process order. Count how many come after the vessel.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- the vessel -------------------------------------------------------------
    "Stirred tank bioreactor design, including impeller selection, baffling and "
    "sparger geometry for the oxygen demand the culture will make",
    "Airlift, bubble column and wave-mixed reactors for shear-sensitive "
    "cultures where a stirred impeller does damage",
    "Heat removal design, since a large aerobic fermentation is a substantial "
    "heat source and cooling area does not grow with volume",
    "Photobioreactor design for phototrophic cultures, where light penetration "
    "replaces oxygen transfer as the limiting transport problem",
    # -- getting the cells out of the way ---------------------------------------
    "Harvest by disc-stack centrifugation, depth filtration or tangential flow "
    "filtration, chosen by particle size, fragility and viscosity",
    "Cell disruption by high pressure homogenisation or bead milling, required "
    "whenever the product was not secreted and the reason secretion hosts are "
    "preferred",
    "Inclusion body recovery, solubilisation and refolding, a route with "
    "characteristically poor and hard-won yields",
    # -- capturing the product ---------------------------------------------------
    "Capture chromatography, including affinity capture, which in a single step "
    "removes the great majority of impurities and dominates therapeutic protein "
    "processing",
    "Polishing chromatography by ion exchange, hydrophobic interaction or "
    "mixed mode, to remove aggregates and product-related variants",
    "Continuous and simulated moving bed chromatography, which uses resin far "
    "more efficiently than a batch column",
    # -- the steps nobody photographs ---------------------------------------------
    "Ultrafiltration and diafiltration for concentration and buffer exchange, "
    "which consume most of the buffer volume in a facility",
    "Buffer preparation, hold and in-line dilution, which frequently sizes the "
    "plant more than the bioreactor does",
    "Viral clearance by low pH inactivation and nanofiltration, with the "
    "clearance capacity of each step validated independently",
    # -- finishing --------------------------------------------------------------
    "Formulation, sterile filtration and aseptic fill-finish",
    "Lyophilisation cycle design for products that are not stable in solution",
    "Single-use assembly design, including the extractables and leachables "
    "assessment that plastic contact requires",
    # -- and the leftovers -------------------------------------------------------
    "Spent broth, biomass and process water treatment, which is a large waste "
    "stream and a permit condition rather than an afterthought",
)


# =============================================================================
#  TECHNOLOGIES
#  The four questions the discipline answers.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- how do we make it bigger without breaking it? -----------------------
    "Scale-up on constant power per unit volume, the most common default, "
    "which preserves turbulence intensity and lets tip speed rise",
    "Scale-up on constant impeller tip speed, chosen for shear-sensitive "
    "cultures at the cost of mixing and transfer",
    "Scale-up on constant oxygen transfer coefficient, chosen where the process "
    "is transfer-limited rather than shear-limited",
    "Computational fluid dynamics and scale-down models that reproduce the "
    "gradients of a large vessel in a small one, so that an organism can be "
    "tested against the insult before the plant is built",
    "Dimensional analysis and the use of Reynolds, Froude and power numbers to "
    "reason about regimes rather than about specific vessels",
    # ---- how do we know what is happening inside? -----------------------------
    "Process analytical technology, including in-line spectroscopy for "
    "concentration and quality attributes",
    "Off-gas analysis and soft sensors that infer biomass and metabolic state "
    "from what can actually be measured",
    "Digital twins and mechanistic process models used for control and for "
    "predicting the consequence of a deviation",
    "Multivariate data analysis across batches to detect drift before it "
    "becomes a failure",
    # ---- how do we make the plant flexible? ------------------------------------
    "Single-use bioreactors, bags, tubing and connectors, which remove cleaning "
    "and sterilisation between campaigns at the cost of a plastic waste stream",
    "Modular and ballroom facility design, which allows several products in one "
    "building without dedicated suites",
    "Continuous and intensified processing, including perfusion culture and "
    "connected downstream trains that remove hold tanks",
    "Process intensification by higher cell density and smaller vessels, which "
    "reduces facility footprint rather than improving the biology",
    # ---- how do we prove it does the same thing every time? ---------------------
    "Quality by design, with critical quality attributes linked to critical "
    "process parameters and a defined design space",
    "Process validation across its three stages, from design through "
    "qualification to continued verification in routine production",
    "Cleaning validation and campaign changeover control, which is where "
    "cross-contamination between products is actually prevented",
)


# =============================================================================
#  ORGANISMS
#  Listed by the transport and mechanical demand each imposes on the equipment,
#  which is how this record sees an organism.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "escherichia_coli",  # high oxygen demand, robust to shear, product often internal
    "saccharomyces_cerevisiae",  # tolerant, high density, easy to separate
    "aspergillus_niger",  # filamentous, viscous, mixing and transfer degrade with growth
    "cricetulus_griseus",  # CHO cells, shear-sensitive, the therapeutic protein workhorse
    "streptomyces_coelicolor",  # filamentous, long campaigns, antibiotic production
    "chlorella_vulgaris",  # phototrophic, light rather than oxygen is the limit
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "fermentation",
    "cell_culture",
    "chromatography",
    "filtration",
    "centrifugation",
    "process_modelling",
    "mass_spectrometry",
    "sterilisation",
)


# =============================================================================
#  CHALLENGES
#  The first two are the record's organising facts, stated as challenges.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the paradox -----------------------------------------------------------
    "The mutual incompatibility of scale-up criteria, since power per volume, "
    "tip speed, oxygen transfer and mixing time cannot be held constant "
    "together, so every scale-up sacrifices something and the engineer must "
    "know which insult the organism tolerates least",
    # -- the arithmetic --------------------------------------------------------
    "Multiplicative yield loss across a purification train, where ten steps at "
    "ninety per cent deliver thirty-five per cent overall, which makes removing "
    "a step worth more than improving one",
    # -- what large vessels actually do to cells --------------------------------
    "Gradients in dissolved oxygen, substrate and pH within a large vessel, so "
    "that cells cycle through conditions the laboratory never presented and "
    "respond metabolically to the transit rather than to the average",
    "Shear damage and interfacial damage at the bubble surface, which limits "
    "how hard a fragile culture may be mixed and aerated",
    # -- where the cost is --------------------------------------------------------
    "Downstream cost dominance, since purification typically exceeds "
    "cultivation in the cost of goods for a biological product",
    "Buffer volume and storage, which routinely sizes a facility more than the "
    "bioreactor does and is the least discussed constraint in the field",
    "Chromatography resin cost, capacity and lifetime, which for affinity "
    "capture is a major consumable rather than a fixed asset",
    # -- the historical mistake ----------------------------------------------------
    "The imbalance created by improving upstream titre without matching "
    "downstream capacity, which the industry demonstrated at scale and which "
    "left existing facilities unable to process what new cell lines produced",
    # -- proving sameness ----------------------------------------------------------
    "Comparability after any process change, since for a biological product the "
    "process defines the molecule and a change must be shown not to have "
    "altered it",
    "Contamination and its consequences in a single-source facility, where an "
    "engineering failure becomes a shortage of a medicine that has no "
    "substitute",
    # -- the cost of flexibility -----------------------------------------------------
    "The waste and supply chain consequences of single-use plastics, which "
    "trade cleaning validation and water use for a disposal stream and a "
    "dependence on specific suppliers",
)
