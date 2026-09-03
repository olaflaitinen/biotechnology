# =============================================================================
#  biotechnology.branches.grey.phytoremediation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THREE SEPARATE BODIES OF LAW MEET ON ONE FIELD, AND THEY WERE NOT WRITTEN
#  WITH EACH OTHER IN MIND.
#
#      CONTAMINATED LAND LAW   sets the target and approves the plan
#      WASTE LAW               governs the harvest, which is hazardous waste
#      AGRICULTURAL LAW        governs planting, and assumes food or forestry
#
#  A phytoextraction site is simultaneously a remediation project, a hazardous
#  waste generator and a crop. The third is the awkward one: agricultural rules
#  exist to keep contaminants OUT of plants, and this practice deliberately
#  puts them in. A crop grown to accumulate cadmium is a compliant remediation
#  measure and a wholly non-compliant food crop, and the boundary between those
#  two descriptions is a fence and a management plan.
#
#  WHICH IS WHY THE REGULATION THAT MATTERS MOST HERE IS ABOUT PATHWAYS RATHER
#  THAN ABOUT PLANTS. The technique creates an exposure route that did not
#  exist: metal that was locked in soil is now in leaves, and leaves are eaten
#  by insects, by grazing animals and occasionally by people who see a green
#  field. Site control is not an administrative formality in this record. It is
#  the safety measure.
#
#  A SECOND POINT: THE CHELATE RESTRICTION IS THE CLEAREST CASE IN THE LIBRARY
#  OF A REGULATION WRITTEN AGAINST A TECHNIQUE THAT WORKED. It was restricted
#  because it succeeded at the wrong system boundary, which `history.py` sets
#  out in full.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import Domain, Maturity, RegulatoryStatus, RiskTier, Scale

__all__ = [
    "MATURITY",
    "RISK_TIER",
    "SCALE",
    "DOMAINS",
    "REGULATORY_STATUS",
    "REGULATIONS",
    "STANDARDS",
]


# =============================================================================
#  POSITION IN THE CONTROLLED VOCABULARIES
# =============================================================================

# -----------------------------------------------------------------------------
#  MATURITY = COMMERCIAL, and the value is a weighted judgement across parts of
#  the record that sit in different places.
#
#  Constructed wetlands and hydraulic control plantings are ESTABLISHED on
#  their own: decades of operation, accepted design methods, regulatory
#  acceptance. Vegetative covers over tailings are routine.
#
#  Phytoextraction is not. It is deployed at a modest number of sites, its
#  timescales are long enough to deter most projects, and nickel phytomining is
#  the only case with a settled commercial model.
#
#  COMMERCIAL is the honest weighted value. ESTABLISHED would credit extraction
#  with the containment applications' record, which is exactly the conflation
#  `practice.py` is organised to prevent.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#
#  The same tier as `grey.bioremediation` and for the same reason: the object
#  regulated is contaminated land. An authority approves the remediation plan,
#  sets the target and certifies completion.
#
#  This record adds two obligations that record does not carry. The harvest is
#  hazardous waste with its own handling and disposal regime, and the site must
#  be controlled against grazing and foraging for as long as the plants are
#  accumulating. Both are prior-approval matters embedded in the site plan.
#
#  It is not RESTRICTED. Any competent contractor may do this work; what is
#  approved is the plan.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = FIELD, and here the vocabulary term is almost literal.
#
#  The unit of work is a planted area under open sky, on a seasonal cycle, at
#  the mercy of weather. Costs, removal rates and targets are all expressed per
#  hectare.
#
#  This is also the value that carries the record's chief limitation, since a
#  field has a depth of a metre or two and everything below it is out of scope.
# -----------------------------------------------------------------------------
SCALE = Scale.FIELD

# -----------------------------------------------------------------------------
#  DOMAINS. ENVIRONMENT first and primarily.
#
#  HEALTH is included on the same basis as `grey.bioremediation`, since cleanup
#  targets are derived from human exposure pathways, and on one additional
#  basis specific to this record: the technique creates a new exposure pathway
#  by moving metal into edible tissue, which is a health matter and not merely
#  an environmental one.
#
#  MATERIALS is included for phytomining, where the harvest is smelted and the
#  metal is recovered as a product. That is a narrow part of the record and it
#  is a genuine one.
#
#  FOOD is deliberately NOT claimed, although the practice grows crops on
#  agricultural land using agricultural equipment. Nothing here enters the food
#  supply, and the governance effort goes into ensuring it does not.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENVIRONMENT,
    Domain.HEALTH,
    Domain.MATERIALS,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED.
#
#  A remediation plan is approved before planting, the harvest disposal route
#  is specified in it, and completion is certified against the target. That is
#  prior authorisation of a specific activity at a specific place.
#
#  The transgenic variants of this record are effectively PROHIBITED in field
#  use, and that is recorded in REGULATIONS rather than in this value, because
#  the value describes the practice as it is actually carried out.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by which body of law it comes from, since the collision
#  between them is this record's governance problem.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- contaminated land law: the target and the plan --------------------------
    "Site investigation, risk assessment and remediation plan approval "
    "requirements, under which a planting scheme is approved as a remediation "
    "measure with a specified endpoint",
    "Risk-based cleanup target derivation tied to land use, which for a site "
    "expected to remain vegetated may be a different number than for one "
    "expected to carry housing",
    "Long-term monitoring and completion certification obligations, which for a "
    "decades-long extraction outlast most of the parties to the original "
    "agreement",
    "Institutional controls and land use restrictions recorded against title, "
    "which are how a site under phytostabilisation is closed with the "
    "contamination still present",
    # -- waste law: the harvest --------------------------------------------------
    "Waste framework legislation classifying contaminated harvest as waste, and "
    "as hazardous waste where the accumulated metal exceeds threshold "
    "concentrations",
    "Hazardous waste storage, transport and disposal requirements applying to "
    "biomass between harvest and destination, which is a logistics obligation "
    "on a seasonal schedule",
    "Incineration and combustion permitting where biomass volume is reduced "
    "thermally, including emission limits and ash classification, since the ash "
    "carries the metal that was in the leaves",
    "Radioactive waste rules where the accumulated contaminant is a "
    "radionuclide, which is a wholly separate and stricter regime",
    # -- agricultural and food law, which was written for the opposite purpose ------
    "Maximum contaminant levels in feed and food, which a phytoextraction crop "
    "is designed to exceed and which is why such a crop must be kept "
    "demonstrably outside those chains",
    "Sewage sludge and soil amendment legislation setting metal limits for "
    "land application, including Directive 86/278/EEC, which governs what may "
    "be added to a soil that is being cleaned",
    "Plant health and invasive species controls on the species planted, which "
    "bear on vigorous wetland and pioneer species used for their tolerance",
    "Agricultural land designation and change of use requirements, which "
    "determine whether a field may be taken out of food production for a "
    "remediation planting",
    # -- what may be added to the soil, after 2001 ---------------------------------
    "Restrictions on the use of persistent synthetic chelating agents for "
    "extraction enhancement, introduced because mobilised metal leached toward "
    "groundwater, which is the clearest case in this library of a technique "
    "restricted for succeeding at the wrong system boundary",
    "Groundwater protection legislation, including the Groundwater Directive "
    "2006/118/EC, which is the standard the leaching concern is measured "
    "against",
    # -- and the engineered route --------------------------------------------------
    "Deliberate release requirements for genetically modified plants, including "
    "Directive 2001/18/EC, which keep enhanced-uptake transgenic varieties out "
    "of field remediation",
    "Air quality regulation bearing on phytovolatilisation, which transfers a "
    "contaminant into shared air and is treated as an emission rather than as a "
    "removal",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is site control, because the technique creates the
#  exposure pathway it then has to manage.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- keeping the metal out of things that eat it ---------------------------
    "Site access, fencing and grazing exclusion practice for accumulating "
    "plantings, which is the primary safety measure of a phytoextraction "
    "project rather than an administrative formality",
    "Litter and leaf-fall management conventions, since unharvested tissue "
    "returns its metal to the soil and reverses part of the extraction",
    "Harvest timing practice tied to peak tissue concentration and to "
    "senescence, which determines whether the metal leaves the site or falls "
    "back onto it",
    "Ecological risk assessment for pollinators, invertebrates and wildlife "
    "using a site that looks like habitat and is not",
    # -- measuring what is actually being removed ------------------------------
    "Plant tissue metal analysis protocols, including digestion and "
    "inductively coupled plasma determination against certified reference "
    "material",
    "Mass balance accounting conventions requiring removal to be reported as "
    "concentration multiplied by harvested biomass rather than as a "
    "bioconcentration factor alone",
    "Sequential extraction and phytoavailability assessment of soil metal, "
    "which distinguishes what can be taken up from what is merely present",
    "Sap flow and transpiration measurement standards for hydraulic control "
    "designs, and the capture zone calculations built on them",
    # -- designing the planting ------------------------------------------------
    "Species and provenance selection guidance matching accumulation, biomass, "
    "tolerance and climate, which is the four-way trade this record turns on",
    "Establishment practice on hostile substrates, including amendment, liming "
    "and irrigation through the first seasons, which is when most plantings "
    "fail",
    "Constructed wetland design standards for mine drainage and effluent, "
    "which are the most mature design conventions in the record",
    "Evapotranspiration cover design guidance for landfill capping",
    # -- and proving it worked over a very long time ---------------------------
    "Long-term monitoring design for decade-scale projects, including data "
    "custody arrangements that survive changes of site ownership",
    "Sustainable remediation appraisal frameworks, which weigh the low energy "
    "and carbon cost of a planting against its long duration and which "
    "frequently favour this record for that reason",
)
