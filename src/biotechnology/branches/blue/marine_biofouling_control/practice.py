# =============================================================================
#  biotechnology.branches.blue.marine_biofouling_control.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by WHAT IS BEING PROTECTED, because the requirement
#  differs completely between them and a single antifouling solution for all of
#  them does not exist. A ship moves and can use release coatings; an
#  aquaculture net is around live animals and cannot use a biocide; a sensor is
#  small, expensive and cannot be cleaned in place.
#
#  TECHNOLOGIES are grouped by MECHANISM, in the order the field moved through
#  them: kill it, make it slide off, make it unable to grip, and stop it
#  settling in the first place. That ordering is also a chronology, and it
#  shows the field moving from broad toxicity towards specificity, which is the
#  same direction `green.biopesticides` records for agriculture.
#
#  ORGANISMS are the foulers rather than the resource, which makes this the
#  only record in the branch where the entries are adversaries. The note on
#  each says what stage of the sequence it belongs to.
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
#  By what is being protected, because the requirement differs completely.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- ships, where the fuel consequence is -----------------------------------
    "Hull coatings for commercial shipping, which are among the most "
    "consequential surface treatments in the world for fuel consumption and "
    "emissions given how much trade moves by sea",
    "Coatings for vessels that spend long periods stationary, where "
    "foul-release systems perform poorly and the requirement is genuinely "
    "different",
    "In-water hull cleaning and grooming with capture of the removed material, "
    "which is regulated because cleaning releases both organisms and coating "
    "biocide into a harbour",
    "Niche area protection for sea chests, thrusters and propeller shafts, "
    "which foul heavily and are difficult to reach",
    # -- aquaculture, where a biocide is not an option ---------------------------
    "Net and cage antifouling in aquaculture, where fouling restricts the water "
    "exchange that farmed fish depend on and therefore becomes a welfare and "
    "disease question",
    "Copper-free net treatments, required because the animals are inside the "
    "structure being protected",
    "Mechanical and robotic net cleaning in situ, which avoids chemistry and "
    "disturbs the stock",
    # -- industrial water systems ------------------------------------------------
    "Seawater intake, condenser and heat exchanger protection in power stations "
    "and desalination plants, where fouling reduces heat transfer and "
    "throughput",
    "Pipeline, riser and offshore structure protection, where fouling adds mass "
    "and hydrodynamic load rather than only drag",
    # -- instruments, which cannot be cleaned -------------------------------------
    "Antifouling for oceanographic sensors and moored instruments, which are "
    "expensive, small and inaccessible, and where a fouled optical window "
    "produces plausible wrong data rather than obvious failure",
    "Protection of membranes in desalination and water treatment, which links "
    "this record to `grey.wastewater_treatment`",
    # -- biosecurity, which is a different objective entirely ---------------------
    "Hull biofouling management as invasive species control, where the "
    "objective is preventing transport of organisms between ports rather than "
    "saving fuel, and where the two objectives usually but not always align",
)


# =============================================================================
#  TECHNOLOGIES
#  By mechanism, in the order the field moved through them.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- kill it: the era that ended -------------------------------------------
    "Self-polishing copolymer coatings releasing a biocide at a controlled rate "
    "as the outer layer erodes, the technology that carried tributyltin and now "
    "carries copper",
    "Copper oxide and copper thiocyanate coatings, effective, widely used and "
    "under regulatory pressure for accumulation in enclosed harbours",
    "Organic booster biocides used alongside copper to cover the organisms "
    "copper does not, each with its own environmental assessment",
    # ---- make it slide off ------------------------------------------------------
    "Silicone and fluoropolymer foul-release coatings, which use very low "
    "surface energy so that organisms attach weakly and are removed by the "
    "vessel's own motion",
    "Amphiphilic and hydrogel-like surfaces that resist both protein adsorption "
    "and organism attachment",
    "Slippery liquid-infused surfaces, effective in the laboratory and limited "
    "by the durability of the infused liquid",
    # ---- make it unable to grip --------------------------------------------------
    "Biomimetic microtopography copying the riblet patterns of shark skin, "
    "which deter settlement mechanically rather than chemically",
    "Surface texturing at the scale of the settling larva, which is a different "
    "scale for a barnacle cyprid than for a diatom, so one texture does not "
    "deter both",
    # ---- stop it settling: the current frontier -----------------------------------
    "Quorum sensing inhibition, disrupting the bacterial signalling that "
    "coordinates biofilm formation, which attacks the first stage rather than "
    "the visible one",
    "Enzymatic coatings that degrade the adhesive proteins and the "
    "extracellular matrix organisms use to attach",
    "Natural product antifoulants drawn from the chemistry sessile marine "
    "organisms use to stay clean, which face the supply constraint recorded in "
    "`blue.marine_natural_products`",
    "Settlement cue interference, exploiting the fact that many larvae settle "
    "in response to specific chemical or microbial signals rather than at "
    "random",
    # ---- and the non-chemical options ---------------------------------------------
    "Proactive grooming, cleaning lightly and often so that fouling never "
    "establishes, which requires no biocide and requires access",
    "Ultraviolet illumination of sensor windows and small surfaces",
    "Copper alloy and physically resistant materials for structures where "
    "coating is impractical",
)


# =============================================================================
#  ORGANISMS
#  The foulers, in the order they arrive. This is the only record in the branch
#  where the organisms are adversaries.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "pseudoalteromonas_haloplanktis",  # early biofilm former; conditions the surface
    "navicula_perminuta",  # diatom, the slime stage that follows the bacteria
    "amphibalanus_amphitrite",  # barnacle; the standard test organism for settlement
    "mytilus_edulis",  # mussel; attaches by byssus, the adhesive studied elsewhere
    "hydroides_elegans",  # tubeworm; settles in response to a bacterial biofilm cue
    "ulva_linza",  # green alga; spore settlement is a standard assay
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "settlement_assay",
    "field_immersion_testing",
    "electron_microscopy",
    "surface_characterisation",
    "ecotoxicity_testing",
    "chromatography",
    "environmental_monitoring",
    "hydrodynamic_testing",
)


# =============================================================================
#  CHALLENGES
#  The first is the field's permanent condition: every solution has been
#  withdrawn or has a limitation that keeps it partial.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the pattern the field cannot escape -----------------------------------
    "Successive withdrawal of effective biocides, since tributyltin was banned "
    "and copper is under pressure for weaker versions of the same reason, which "
    "means an effective solution should be assumed to have a regulatory "
    "lifetime rather than a permanent one",
    "Absence of any single solution across use cases, because a ship that moves "
    "and a net around live fish and a moored sensor have requirements that no "
    "one technology meets",
    # -- what the alternatives cannot do ----------------------------------------
    "Foul-release coatings requiring vessel motion, so they perform poorly for "
    "stationary and slow vessels and for anything moored",
    "Durability of textured and liquid-infused surfaces over the years a hull "
    "coating must survive, which is where laboratory performance and service "
    "performance diverge most sharply",
    "Supply of natural product antifoulants, which meets the same constraint "
    "that governs `blue.marine_natural_products` and for the same reason",
    "Mechanical damage and coating repair, since any surface that works by its "
    "physical properties fails locally where it is scratched",
    # -- testing the thing is hard ------------------------------------------------
    "Poor correlation between laboratory settlement assays and multi-year field "
    "performance, which is why static immersion panels and full-scale trials "
    "remain necessary and slow",
    "Seasonal, geographic and species variation in fouling pressure, so a "
    "coating validated in one region may perform differently in another",
    # -- the environmental accounting is not simple ---------------------------------
    "Environmental assessment of booster biocides and of released coating "
    "particles, including microplastic from eroding self-polishing coatings, "
    "which is a newer concern than the biocide itself",
    "In-water cleaning releasing both accumulated organisms and coating biocide "
    "into a harbour, which turns maintenance into a regulated discharge",
    # -- two objectives that are not the same ---------------------------------------
    "Divergence between the fuel objective and the biosecurity objective, since "
    "a coating that keeps a hull smooth enough to be efficient may still carry "
    "enough organisms in niche areas to transport species between ports",
)
