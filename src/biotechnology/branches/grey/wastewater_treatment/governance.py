# =============================================================================
#  biotechnology.branches.grey.wastewater_treatment.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS IS THE MOST HEAVILY REGULATED PROCESS IN THIS BRANCH AND NONE OF THE
#  REGULATION IS ABOUT THE ORGANISMS.
#
#  There is no approval for the community in an aeration tank. Nobody licenses
#  the nitrifiers. What is regulated is a NUMBER AT THE OUTFALL, measured
#  continuously, reported to an authority, and enforceable with criminal
#  penalties against named individuals in several jurisdictions.
#
#      THE LAW SPECIFIES THE RESULT AND SAYS NOTHING ABOUT THE MEANS.
#
#  That is an unusual and, on the whole, well-designed arrangement. An operator
#  may achieve the consent by any process at all, which is why the technology
#  in `practice.py` is diverse and why plants differ enormously between
#  countries with similar standards.
#
#  A SECOND POINT, AND IT IS THE ONE WITH TEETH. Discharge consent breaches
#  carry personal liability for operators and managers, not merely corporate
#  fines. Very little else in this library is enforced that way, and it
#  reflects that the harm is immediate, local and attributable.
#
#  A THIRD POINT WORTH RECORDING HONESTLY. Combined sewer overflows are
#  PERMITTED discharges of untreated sewage during heavy rain. They are lawful
#  by design, not a failure of enforcement, and they exist because separating
#  storm water from foul water in an old city costs more than any regulator has
#  been willing to require.
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
#  MATURITY = ESTABLISHED, and if any record in this library is entitled to the
#  value it is this one.
#
#  The core process has run continuously since 1914, serves most of the urban
#  world, is taught as standard engineering, has published design codes, and
#  has a professional discipline built around operating it. There is no
#  argument to be made here.
#
#  That the process does not remove micropollutants does not reduce the value.
#  An established technology can have a scope, and this one's scope is carbon,
#  nutrients and pathogens.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#
#  A works operates under a discharge consent that sets numerical limits,
#  requires continuous monitoring and periodic reporting, and is enforceable.
#  Sludge destined for land carries its own authorisation. That is prior
#  approval of a specific activity with ongoing conditions.
#
#  It is not RESTRICTED. Anyone may operate a treatment works subject to
#  holding the permit and, in most jurisdictions, employing certified
#  operators. The restriction is on the discharge rather than on the actor.
#
#  As elsewhere, the tier reflects governance intensity. The organisms are
#  ordinary environmental bacteria that arrived in the sewage.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL.
#
#  This is a continuously operated plant with a design flow, unit processes,
#  instrumentation, control systems and a shift rota. It is a chemical works
#  whose reactor happens to contain an undefined community, and INDUSTRIAL is
#  what that is.
#
#  POPULATION was considered, since a works is sized by the population it
#  serves and its purpose is a population health outcome. It was rejected
#  because the unit of operation is a plant. `grey.environmental_biomonitoring`
#  carries the population-scale surveillance use of the same sewage.
#
#  FIELD would be wrong: the reactor has walls.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. Four, and each earns its place on a different mechanism.
#
#  ENVIRONMENT is the discharge: oxygen demand and nutrients reaching receiving
#  waters, which is what the consent limits exist for.
#
#  HEALTH is the founding purpose. Separating sewage from drinking water is
#  what ended cholera and typhoid as ordinary urban facts, and this is the
#  process that makes it possible at city scale.
#
#  ENERGY is claimed on a real and quantified basis in both directions:
#  aeration is a substantial share of municipal electricity demand, and
#  digester methane offsets a substantial share of the works demand. A record
#  that is both a large consumer and a generator has an energy domain.
#
#  FOOD is claimed narrowly, for biosolids and recovered struvite returning
#  nitrogen and phosphorus to agricultural soil. It is the smallest of the four
#  and it is a genuine material flow rather than an association.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENVIRONMENT,
    Domain.HEALTH,
    Domain.ENERGY,
    Domain.FOOD,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED.
#
#  A works cannot discharge without a permit specifying limits and monitoring.
#  The permit is granted before operation, varied over time, and withdrawn or
#  enforced against on breach. That is authorisation in the strict sense.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by what it controls: the discharge, the solid, the
#  intake, and the people.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the number at the outfall, which is the whole regime -------------------
    "Discharge consents and permits setting numerical limits on oxygen demand, "
    "suspended solids, ammonium, total nitrogen and total phosphorus, which "
    "specify the result and say nothing about the process used to reach it",
    "The Urban Waste Water Treatment Directive 91/271/EEC and its national "
    "equivalents, which set collection and treatment obligations by settlement "
    "size and impose stricter nutrient limits on sensitive catchments",
    "The Water Framework Directive 2000/60/EC, which sets the receiving water "
    "status that discharge limits are ultimately derived from",
    "Self-monitoring, record-keeping and reporting obligations, including "
    "continuous instrumentation where the consent requires it",
    "Personal criminal liability for operators and managers on consent breach "
    "in several jurisdictions, which is a level of enforcement almost nothing "
    "else in this library carries",
    # -- the discharges that are lawful by design ---------------------------------
    "Combined sewer overflow permits authorising the discharge of untreated "
    "sewage during heavy rainfall, which are lawful by design rather than a "
    "failure of enforcement and which reflect the cost of separating storm and "
    "foul networks in old cities",
    "Storm water and emergency overflow reporting requirements, including "
    "event duration monitoring",
    # -- what arrives at the works ------------------------------------------------
    "Trade effluent consents and pretreatment requirements, which control what "
    "industry may discharge to sewer and are the plant's protection against the "
    "toxic shock loads that kill its biomass",
    "Prohibitions on discharging listed hazardous substances to sewer, since a "
    "works cannot remove what it was not designed for and will simply pass it "
    "on",
    # -- the solid --------------------------------------------------------------------
    "The Sewage Sludge Directive 86/278/EEC and national equivalents, setting "
    "metal limits, treatment requirements and application rates for biosolids "
    "used on agricultural land",
    "Waste framework legislation classifying sludge, and the end-of-waste "
    "criteria that determine when treated biosolids cease to be waste",
    "Animal by-products and pathogen reduction requirements where biosolids are "
    "applied to grazing land or to crops entering the food chain",
    "Emission limits and permitting for sludge incineration, and the "
    "classification of the resulting ash",
    # -- where the water goes next --------------------------------------------------
    "Water reuse regulation, including Regulation (EU) 2020/741 on minimum "
    "requirements for water reuse in agricultural irrigation",
    "Drinking water quality legislation, which sets the standard that any "
    "potable reuse scheme must ultimately satisfy",
    "Bathing water and shellfish water designations, which impose pathogen "
    "limits on discharges upstream of them",
    # -- and the people running it ----------------------------------------------------
    "Operator certification and competence requirements, which in many "
    "jurisdictions are a condition of the permit itself",
    "Confined space, gas and worker safety law, since digester gas is explosive "
    "and treatment works contain the two most common causes of fatal accidents "
    "in the water industry",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is how the regulated numbers are actually measured,
#  since a consent limit is only as good as the method behind it.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- measuring the numbers the law is written in ---------------------------
    "Standard Methods for the Examination of Water and Wastewater, which "
    "define the biochemical oxygen demand procedure that discharge law is "
    "written in and without which the limit would have no meaning",
    "ISO analytical standards for chemical oxygen demand, nitrogen species, "
    "phosphorus and suspended solids",
    "Sampling and flow measurement conventions, including composite sampling, "
    "which determine whether a reported value represents the day or the moment "
    "it was taken",
    "Instrument calibration, validation and data quality practice for "
    "continuous online monitoring",
    "Laboratory accreditation to ISO 17025 for compliance analysis",
    # -- designing and simulating the plant -------------------------------------
    "Activated sludge model formulations, which are the shared mathematical "
    "description the field designs and simulates against",
    "Design codes and loading guidance for the unit processes, including the "
    "solids retention time required to sustain nitrification at a given "
    "temperature",
    "Aeration system testing and oxygen transfer efficiency determination, "
    "which is how the plant's largest energy cost is specified and verified",
    "Energy benchmarking conventions for treatment works, which is what an "
    "efficiency programme is measured against",
    # -- knowing what is in the tank ---------------------------------------------
    "Microscopic sludge examination and filament identification protocols, "
    "which remain the fastest practical diagnostic for a settling problem",
    "Sludge volume index determination methods, which are the early warning for "
    "the failure that shuts plants down",
    "Molecular community profiling conventions for mixed liquor, which "
    "identified the organisms the process had been using for eighty years "
    "without knowing it",
    "Respirometric testing for influent characterisation and toxicity "
    "screening",
    # -- running it safely and consistently ---------------------------------------
    "ISO 9001 and ISO 14001 management systems as applied by water utilities",
    "Asset management practice under ISO 55000, which is what determines "
    "whether ageing infrastructure is renewed before it underperforms",
    "Water safety plan methodology, which applies a hazard analysis approach "
    "from source to discharge and to reuse",
    "Digester gas handling and explosion protection practice, which is the "
    "safety standard with the highest consequence attached to it",
)
