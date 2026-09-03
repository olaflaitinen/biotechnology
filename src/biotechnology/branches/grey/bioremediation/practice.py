# =============================================================================
#  biotechnology.branches.grey.bioremediation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped BY CONTAMINANT CLASS, because the contaminant
#  determines whether biology is even the right tool. The groups run from what
#  works well, through what works with difficulty, to what cannot be destroyed
#  at all, and that ordering is the record's main argument made visible.
#
#  The metals group is deliberately last and is deliberately labelled. Every
#  entry in it changes where a metal is or what form it takes, and none of them
#  removes it from existence. Presenting those beside hydrocarbon degradation
#  without that distinction would repeat the misconception the record exists to
#  correct.
#
#  TECHNOLOGIES are grouped by HOW MUCH IS ADDED, from nothing upwards, which
#  is also roughly the order of increasing cost and decreasing likelihood of
#  success. The first group contains one entry and it is an approved
#  intervention.
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
#  By contaminant class, from what works to what cannot be destroyed.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- petroleum hydrocarbons: the commonest, and the best suited -------------
    "Treatment of petroleum hydrocarbon contamination at fuel stations, depots "
    "and refineries, which is the commonest contamination by a wide margin and "
    "the application biology handles best",
    "Land farming and biopiling of excavated hydrocarbon-contaminated soil, "
    "where the material is spread or heaped and aerated deliberately",
    "In situ aerobic treatment of hydrocarbon plumes in groundwater by air "
    "sparging and oxygen release",
    "Shoreline treatment after oil spills by nutrient addition, which is where "
    "the field's public reputation was made and where the evidence is stronger "
    "than for most applications",
    # -- chlorinated solvents: works, and can make things worse first ------------
    "Reductive dechlorination of trichloroethene and tetrachloroethene in "
    "groundwater, using organisms that use the solvent as an electron acceptor "
    "rather than as food",
    "Sequential anaerobic and aerobic treatment, since the intermediates of "
    "anaerobic dechlorination require oxygen to be finished off",
    "Permeable reactive barriers containing an electron donor, treating a plume "
    "as it flows through rather than treating the whole aquifer",
    # -- nitrogen and nutrients: an entirely different chemistry ------------------
    "Denitrification of nitrate-contaminated groundwater, converting nitrate to "
    "nitrogen gas, which is one of the few cases where a contaminant leaves as "
    "a harmless gas",
    "Treatment of ammonium and nutrient plumes beneath agricultural and landfill "
    "sites",
    # -- the difficult organics ---------------------------------------------------
    "Polycyclic aromatic hydrocarbon treatment at gasworks and coking sites, "
    "which is slow because the larger compounds are poorly soluble and strongly "
    "sorbed",
    "Explosives and energetic compound treatment at former munitions sites",
    "Pesticide and herbicide residue treatment in soil",
    "Treatment of per- and polyfluoroalkyl substances, which is included "
    "honestly as an area of research rather than an application, since the "
    "carbon-fluorine bond resists biological attack and no established "
    "biological treatment exists",
    # -- metals: NOT destruction, and labelled as such ----------------------------
    "Biosorption and bioaccumulation of metals into biomass, which CONCENTRATES "
    "the metal into material that must then be disposed of",
    "Microbially mediated reduction of chromium and uranium to less soluble "
    "oxidation states, which IMMOBILISES the metal in place rather than "
    "removing it",
    "Sulphate reduction precipitating metals as sulphides, used in mine water "
    "treatment and leaving a metal-bearing sludge",
    "Mercury volatilisation, which is technically possible and moves the "
    "contaminant to the atmosphere, and which is recorded here as a "
    "demonstration of why relocation is not remediation",
)


# =============================================================================
#  TECHNOLOGIES
#  By how much is added, from nothing upwards.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- add nothing, and prove it is working ----------------------------------
    "Monitored natural attenuation, in which indigenous degradation is "
    "documented as faster than plume migration, with the lines of evidence "
    "specified: falling concentrations, matching geochemical footprints, and "
    "confirmed degrader populations",
    # ---- add what is missing, which is usually an electron acceptor -------------
    "Oxygen delivery by air sparging, bioventing, oxygen release compounds or "
    "hydrogen peroxide, which is the commonest biostimulation because oxygen is "
    "what aerobic degradation runs out of first",
    "Electron donor addition for reductive processes, including lactate, "
    "emulsified vegetable oil and hydrogen release compounds",
    "Nutrient addition of nitrogen and phosphorus, which is what the shoreline "
    "work did and which is unnecessary in most soils where nutrients are not "
    "limiting",
    "pH and redox adjustment to bring conditions into the range the degrading "
    "organisms need",
    # ---- add access, which is the real problem ----------------------------------
    "Surfactant and cosolvent flushing to mobilise sorbed contaminant, which "
    "attacks bioavailability directly and risks spreading the plume",
    "Thermal enhancement, which raises both desorption and metabolic rate and "
    "is the point at which a biological treatment starts to cost like a "
    "physical one",
    "Soil mixing and tilling in ex situ treatment, which is simply making the "
    "contaminant reachable",
    # ---- add organisms, which usually fails --------------------------------------
    "Bioaugmentation with characterised degrading cultures, which succeeds in "
    "the specific case of dechlorinating consortia where the capability is "
    "genuinely absent, and generally fails otherwise for the reasons "
    "`grey.bioaugmentation` sets out",
    # ---- move it into a vessel ----------------------------------------------------
    "Slurry bioreactors and engineered ex situ systems, which give control at "
    "the cost of excavation, so the material has been dug up anyway",
    "Permeable reactive barriers, which treat the flow rather than the aquifer",
    # ---- find out whether it is working -------------------------------------------
    "Compound-specific isotope analysis, which distinguishes destruction from "
    "dilution because degradation leaves an isotopic signature and dilution "
    "does not, and which is the single most useful line of evidence in the "
    "field",
    "Molecular biological tools quantifying degrader genes and organisms, "
    "linking this record to `red.molecular_diagnostics`",
    "Microcosm testing on site material to establish whether degradation "
    "occurs at all before committing to a design",
)


# =============================================================================
#  ORGANISMS
#  Each entry notes what it degrades, since capability is the reason for
#  inclusion.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "pseudomonas_putida",  # broad hydrocarbon and aromatic degradation
    "alcanivorax_borkumensis",  # marine alkane specialist, blooms after oil spills
    "dehalococcoides_mccartyi",  # the only genus completing dechlorination to ethene
    "rhodococcus_erythropolis",  # persistent, degrades a wide range, survives stress
    "mycobacterium_vanbaalenii",  # polycyclic aromatic hydrocarbon degradation
    "geobacter_metallireducens",  # metal reduction, immobilising rather than removing
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "microcosm_testing",
    "gas_chromatography",
    "mass_spectrometry",
    "isotope_ratio_analysis",
    "qpcr",
    "metagenomics",
    "groundwater_sampling",
    "process_modelling",
)


# =============================================================================
#  CHALLENGES
#  Bioavailability first, because it is the limit that is usually
#  misattributed.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the limit that is not microbiological ---------------------------------
    "Bioavailability, since contaminants sorbed to organic matter and diffused "
    "into intraparticle pores are unreachable, which means most persistent "
    "contamination is degradable in a flask and not in the ground",
    "Asymptotic behaviour, where treatment proceeds rapidly and then stalls "
    "well above the target concentration as the accessible fraction is "
    "exhausted, so the last portion of a cleanup is disproportionately hard",
    "Site heterogeneity, since a low-permeability lens holds contaminant that "
    "no injected amendment reaches and releases it slowly for years afterwards",
    # -- what biology cannot do at all --------------------------------------------
    "Metals, which no organism destroys, so every metal application relocates, "
    "concentrates or immobilises and none removes",
    "Compounds resisting biological attack, including per- and polyfluoroalkyl "
    "substances, where the carbon-fluorine bond is the obstacle and no "
    "established biological treatment exists",
    # -- when treatment makes things worse -----------------------------------------
    "Accumulation of toxic intermediates, notably vinyl chloride from "
    "incomplete dechlorination, which is more hazardous than the parent "
    "compound and which means a stalled treatment can leave a site worse than "
    "untreated",
    "Contaminant mobilisation by surfactants or by changed redox conditions, "
    "which can spread a plume that was stable",
    # -- the conditions the organisms need ------------------------------------------
    "Oxygen limitation, which is what aerobic degradation runs out of first and "
    "which is expensive to supply through a soil matrix",
    "Toxicity of the contamination to the degrading organisms at high "
    "concentration, so the most contaminated zone is frequently the least "
    "biologically active",
    "Temperature dependence, which in temperate and cold climates halves "
    "process rates in winter and lengthens an already slow treatment",
    # -- and the constraints that are not technical ------------------------------------
    "Timescale against regulatory deadlines and property transactions, which is "
    "why physical methods are chosen on sites where biology would have worked",
    "Demonstrating that concentrations fell through destruction rather than "
    "dilution, which requires isotope or molecular evidence that many "
    "monitoring programmes do not collect",
)
