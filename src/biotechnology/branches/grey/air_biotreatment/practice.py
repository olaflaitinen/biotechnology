# =============================================================================
#  biotechnology.branches.grey.air_biotreatment.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS ARE GROUPED BY WHO IS COMPLAINING AND ABOUT WHAT, WHICH IS THE
#  HONEST TAXONOMY FOR THIS RECORD.
#
#      ODOUR              the majority of deployment, driven by neighbours
#      SPECIFIC TOXICANT  hydrogen sulphide and ammonia, where there is a
#                         measurable reason beyond smell
#      SOLVENT VAPOUR     regulated emission limits, and where solubility
#                         starts to bite
#      METHANE            the hardest case, and the one that mostly does not
#                         work
#
#  THE METHANE GROUP IS INCLUDED AND LABELLED AS MARGINAL. Methane is very
#  poorly soluble and dilute in the streams where it appears, which is exactly
#  the combination this technique handles worst. Listing it without that
#  qualification would breach rule 6, and omitting it would leave out the
#  application readers most often ask about.
#
#  TECHNOLOGIES ARE GROUPED BY CONFIGURATION AND THEN BY WHAT KEEPS THE BED
#  ALIVE. The second group is longer, which is accurate: the engineering
#  problem here is maintenance of a living bed rather than reactor design.
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
#  By what is being complained about, from the commonest to the marginal.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # ---- ODOUR: the majority of what is actually installed ---------------------
    "Odour control at wastewater treatment works, covering inlet works, sludge "
    "handling and storage, which is the single commonest installation and is "
    "frequently a planning condition rather than an environmental one",
    "Odour control at composting and anaerobic digestion facilities, which is "
    "what allows `grey.biowaste_treatment` plants to be sited near the "
    "populations whose waste they take",
    "Rendering, fish processing and food factory exhaust treatment, where the "
    "offending compounds are amines, sulphides and aldehydes at very low "
    "concentration",
    "Intensive livestock housing ventilation treatment, which handles ammonia "
    "and odour together and is driven by both neighbour complaint and nitrogen "
    "deposition rules",
    "Landfill working face and waste transfer station air treatment",
    # ---- SPECIFIC TOXICANTS: a measurable reason beyond smell -------------------
    "Hydrogen sulphide removal from digester biogas, which is done because the "
    "gas is toxic and corrosive and destroys the engines the biogas is meant to "
    "run, so the driver is asset protection rather than emission",
    "Hydrogen sulphide treatment in sewer ventilation, which also addresses the "
    "concrete corrosion that the same chemistry causes in the pipe itself",
    "Ammonia removal from livestock and composting exhaust, which is regulated "
    "as an air quality and nitrogen deposition matter and not only as an odour",
    "Biological desulphurisation of biogas by controlled micro-aeration, which "
    "achieves the same result inside the digester headspace without a separate "
    "vessel",
    # ---- SOLVENT VAPOUR: where solubility starts to decide ---------------------
    "Treatment of alcohol, ketone and ester vapours from printing, coating and "
    "painting operations, which are soluble enough for the technique to work "
    "well",
    "Styrene and toluene removal from composites and plastics manufacturing, "
    "which sits at the boundary of what partitions adequately",
    "Volatile organic compound treatment at pharmaceutical and chemical plants "
    "where the compound is soluble and the concentration is low",
    "Soil vapour extraction off-gas treatment, which pairs this record directly "
    "with `grey.bioremediation` by treating what the remediation strips out of "
    "the ground",
    # ---- METHANE AND POORLY SOLUBLE COMPOUNDS: marginal, and labelled ----------
    "Methane oxidation in landfill biocovers, where methanotrophs in an "
    "engineered soil layer oxidise gas escaping the cap, which works at low "
    "flux and cannot handle a concentrated stream",
    "Dilute methane treatment from livestock and mine ventilation air, which is "
    "recorded as a research area rather than an established application, since "
    "methane is poorly soluble and very dilute in exactly these streams, which "
    "is the worst combination for this technique",
    "Chlorinated solvent vapour treatment, which is included with the same "
    "qualification: the compounds partition poorly and the degradation produces "
    "acid that damages the bed",
)


# =============================================================================
#  TECHNOLOGIES
#  The three configurations, then everything that keeps a living bed working.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- the three configurations ----------------------------------------------
    "Biofilters on organic packing such as compost, bark, peat or wood chip, "
    "where the biofilm grows on the packing itself and there is no separate "
    "liquid phase to manage, which is the simplest and cheapest arrangement",
    "Biotrickling filters on inert packing with recirculated liquid, which "
    "permits pH and nutrient control and washes out acidic products, and is "
    "therefore what sulphide treatment generally uses",
    "Bioscrubbers, which absorb the contaminant into liquid in one vessel and "
    "degrade it in a separate bioreactor, giving the most control at the "
    "highest cost",
    "Membrane and two-phase partitioning bioreactors, which introduce an "
    "additional phase to improve the transfer of poorly soluble compounds and "
    "are the main line of attack on this record's central limitation",
    # ---- getting the contaminant into the water --------------------------------
    "Packing material selection for surface area, void fraction and water "
    "retention, which sets both the transfer area and the pressure drop the "
    "fan must overcome",
    "Structured and engineered media, which resist the compaction and "
    "channelling that eventually ruins an organic bed",
    "Gas distribution design, since a bed with a preferential path treats only "
    "the fraction of air that goes the long way",
    "Humidification of the incoming air, which is not optional: an unhumidified "
    "stream dries the bed out from the inlet end and the biofilm dies there "
    "first",
    # ---- keeping the bed alive ---------------------------------------------------
    "Irrigation and moisture control, which is the commonest cause of both "
    "success and failure and is what most operator attention goes to",
    "pH control and neutralisation, required wherever sulphur or chlorine "
    "compounds are degraded, since the products are acids that will kill the "
    "biofilm that made them",
    "Nutrient dosing of nitrogen and phosphorus in the recirculating liquid, "
    "which the air stream itself does not supply",
    "Backwashing and biomass control, since excess growth blocks the void space "
    "and raises the pressure drop until the fan cannot deliver the flow",
    "Media replacement scheduling for organic packings, which compact and "
    "degrade over a few years and are a recurring capital cost that proposals "
    "commonly omit",
    "Startup and reacclimation practice after a shutdown, since a bed recovers "
    "over weeks rather than hours and a maintenance outage has an odour "
    "consequence afterwards",
    # ---- finding out whether it worked --------------------------------------------
    "Dynamic olfactometry with trained human panels, which is the reference "
    "method for odour and is the acceptance criterion that actually matters",
    "Electronic nose and continuous sulphide instrumentation, which give a "
    "signal between panel assessments",
    "Inlet and outlet speciation by gas chromatography and mass spectrometry, "
    "which distinguishes what was removed from what was merely diluted",
)


# =============================================================================
#  ORGANISMS
#  Selected by what the bed conditions favour, not supplied.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "thiobacillus_thioparus",  # sulphide oxidation, and it acidifies its own bed
    "acidithiobacillus_thiooxidans",  # takes over once the bed has turned acid
    "nitrosomonas_europaea",  # ammonia oxidation in the same beds
    "methylococcus_capsulatus",  # methanotroph, the landfill biocover case
    "pseudomonas_putida",  # solvent vapour degradation
    "rhodococcus_erythropolis",  # tolerates drying and shock better than most
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "olfactometry",
    "gas_chromatography",
    "mass_spectrometry",
    "online_sensing",
    "microcosm_testing",
    "qpcr",
    "process_modelling",
    "microscopy",
)


# =============================================================================
#  CHALLENGES
#  Solubility first, because it is the boundary of the technique rather than a
#  difficulty within it.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the boundary of the technique -----------------------------------------
    "Poor solubility, which places compounds outside the method rather than "
    "making them slow within it, since a contaminant that will not partition "
    "into the water film is never presented to the organisms at all",
    "Very short gas residence times, measured in seconds, which leaves little "
    "opportunity for a slowly partitioning compound to transfer",
    "Low and variable inlet concentration, which can be insufficient to sustain "
    "the biomass that a subsequent peak load requires",
    # -- keeping a living bed alive ---------------------------------------------
    "Drying of the bed, which kills the biofilm from the inlet end and is the "
    "commonest operational failure, and which is why incoming air must be "
    "humidified",
    "Acidification from sulphur and chlorine compound degradation, where the "
    "products destroy the community that produced them unless they are washed "
    "out",
    "Compaction and channelling in organic packings, which lets air bypass most "
    "of the bed while the instrumentation still reports flow",
    "Excess biomass growth blocking void space and raising pressure drop until "
    "the fan can no longer deliver the design flow",
    "Slow recovery after shutdown or shock loading, over weeks rather than "
    "hours, so a maintenance outage produces an odour problem after it ends",
    # -- the size and the recurring cost -----------------------------------------
    "Footprint, since seconds of residence at high flow is still a large "
    "volume, and land adjacent to a treatment works is rarely available",
    "Media replacement every few years for organic packings, which is a "
    "recurring cost routinely omitted from comparisons against thermal "
    "treatment",
    "Fan power against pressure drop, which is the whole of the running cost "
    "and rises as the bed ages",
    # -- and judging whether it worked ---------------------------------------------
    "Odour measurement resting on human detection thresholds, which vary "
    "between people, are not health-based, and mean a compliant plant can still "
    "be a genuine nuisance to the nearest resident",
    "Compounds offensive far below instrumental detection limits, so a plant "
    "can satisfy every chemical specification and fail a panel",
    "Distinguishing removal from dilution where treated and untreated streams "
    "combine before the stack",
    "Bioaerosol emission from the beds themselves, particularly from organic "
    "packings, which is a treatment introducing its own emission",
)
