# =============================================================================
#  biotechnology.branches.grey.air_biotreatment.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS IS THE ONLY RECORD IN THE LIBRARY WHOSE PRINCIPAL COMPLIANCE STANDARD
#  IS ENFORCED THROUGH A HUMAN SENSE.
#
#  Almost everything else here is regulated against an instrumental limit. Air
#  biotreatment is regulated substantially against odour, and odour is measured
#  by presenting diluted samples to a trained panel and recording the dilution
#  at which half of them can just detect it. That procedure is standardised,
#  reproducible and written into permits, and its unit is a person.
#
#      THE OBJECTIVE IS NOT A HEALTH THRESHOLD. IT IS AN ANNOYANCE THRESHOLD.
#
#  That distinction has to be stated plainly rather than smoothed over. Odour
#  limits protect amenity, which is a legitimate object of regulation and is
#  not the same as protecting health. A plant may be fully compliant and still
#  be a real nuisance to the nearest household, and the record says so.
#
#  A SECOND POINT. THE REGULATION THAT MATTERS MOST HERE IS PLANNING
#  REGULATION. Odour is usually a condition attached to permission to operate
#  in a particular place. That means the binding constraint arrives before the
#  plant is built and is decided by a local authority weighing neighbours
#  against infrastructure, which is why this record determines where a great
#  deal of `grey.wastewater_treatment` and `grey.biowaste_treatment` can
#  physically be.
#
#  A THIRD: the treatment generates its own emission. Bioaerosols from organic
#  packing are an exposure question in their own right, so the abatement plant
#  is itself a regulated source.
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
#  MATURITY = ESTABLISHED.
#
#  Soil beds have been used since the 1920s, engineered biofilters since the
#  1970s, and biotrickling filters are the default answer for hydrogen sulphide
#  at wastewater and biogas installations. There are design guidelines, a
#  supplier industry, and a standardised compliance method.
#
#  The unsolved part of the record, which is poorly soluble compounds, does not
#  reduce the value: it is a boundary of scope rather than an immaturity, and
#  `history.py` records that the boundary is chemical rather than developmental.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED, and it is the lowest tier in this branch after
#  `grey.bioaugmentation`.
#
#  A biofilter is normally a condition within somebody else's permit rather
#  than a separately permitted activity. The parent installation holds the
#  environmental permit and the abatement plant is how it meets a limit in it.
#  Emission limits, monitoring obligations and planning conditions apply, and
#  no prior approval of the abatement technology itself is required.
#
#  It is not REGULATED because the authorisation attaches to the emitting
#  installation rather than to this process. The record is honest that it is
#  usually a component and not a facility.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL.
#
#  The unit is a bed sized to a design air flow, sitting on a plant, with a
#  fan, humidifier and irrigation system. It is process equipment.
#
#  FIELD was considered for the landfill biocover application, where an
#  engineered soil layer sits under open sky across a whole site. That is a
#  genuine part of the record and it is a minority of it, so it is recorded in
#  `practice.py` rather than being allowed to move this value.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. Two, and the record is better for not claiming more.
#
#  ENVIRONMENT is the emission itself: odour, ammonia, sulphide and volatile
#  organic compounds leaving a stack.
#
#  HEALTH is claimed on the specific toxicants rather than on odour. Hydrogen
#  sulphide is acutely toxic, ammonia is an irritant and a deposition problem,
#  and several treated solvents have occupational limits. The odour work is
#  amenity rather than health, which is exactly why HEALTH is claimed on the
#  narrower basis and not on the bulk of the deployment.
#
#  ENERGY IS DELIBERATELY NOT CLAIMED even though the technique's chief
#  advantage is that it uses far less energy than thermal oxidation. Using less
#  energy than an alternative is not an energy application. Claiming it would
#  be exactly the padding the vocabulary exists to prevent, and it would sit
#  badly beside `grey.biowaste_treatment`, which claims the domain because it
#  produces a fuel.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENVIRONMENT,
    Domain.HEALTH,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = NOTIFIED.
#
#  The abatement plant is declared as the means by which the parent
#  installation meets its emission and planning conditions, and it is then
#  monitored against those conditions. No authority approves the biofilter
#  itself.
#
#  AUTHORISED would misdescribe this, since it would imply an approval of the
#  technology. What is authorised is the installation, and this record is one
#  of the things that installation does to keep its authorisation.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.NOTIFIED


# =============================================================================
#  REGULATIONS
#  Binding law. The planning group is first because it is what actually decides
#  whether a facility exists in a given place.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- planning, which is the binding constraint ------------------------------
    "Planning permission conditions requiring odour abatement, which are "
    "typically the reason a plant is installed and which are imposed before "
    "construction by an authority weighing neighbours against infrastructure",
    "Odour management plan requirements attached to permits at waste, "
    "composting and wastewater facilities, which specify complaint procedures "
    "as well as abatement",
    "Statutory nuisance provisions, under which persistent odour is actionable "
    "independently of whether an emission limit was met",
    "Separation distance and buffer zone requirements between odour-generating "
    "facilities and residential areas",
    # -- the emission limits themselves ------------------------------------------
    "The Industrial Emissions Directive 2010/75/EU and equivalent regimes, "
    "which set permit conditions and require best available techniques for the "
    "installations this record serves",
    "Best available techniques reference documents for waste treatment, which "
    "name biological air treatment as an accepted technique and describe the "
    "performance expected of it",
    "National air quality legislation setting limits for ammonia, hydrogen "
    "sulphide and volatile organic compounds",
    "Solvent emissions requirements for coating, printing and cleaning "
    "operations, which are what drive the solvent vapour applications",
    # -- the specific pollutants ---------------------------------------------------
    "Ammonia emission ceilings and nitrogen deposition rules under the National "
    "Emission Ceilings Directive 2016/2284 and habitats protection, which apply "
    "to livestock housing and composting",
    "Occupational exposure limits for hydrogen sulphide, ammonia and solvent "
    "vapours, which govern the workplace inside the fenceline rather than the "
    "emission beyond it",
    "Gas quality requirements for biogas use, which are why sulphide removal is "
    "performed to protect engines as well as to satisfy an emission limit",
    # -- the emission the treatment itself creates -------------------------------------
    "Bioaerosol assessment requirements at composting and waste facilities, "
    "which apply to the abatement media themselves and make the treatment plant "
    "a regulated source in its own right",
    "Waste classification and disposal requirements for spent biofilter media, "
    "which is a waste stream generated every few years by an installation whose "
    "purpose is emission control",
    # -- and the general duty --------------------------------------------------------
    "General duty of care and environmental permitting compliance obligations, "
    "including monitoring, record keeping and reporting against the conditions "
    "above",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is the measurement, because the entire compliance
#  regime rests on it.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- measuring an annoyance reproducibly ------------------------------------
    "EN 13725 dynamic olfactometry, which defines the odour unit through a "
    "standardised procedure with trained panels and is what allowed odour to be "
    "written into permits as a number at all",
    "Panel selection, screening and calibration practice against reference "
    "gases, which is what makes a human measurement reproducible between "
    "laboratories",
    "Odour sampling conventions for stacks and area sources, including bag "
    "material selection, since several relevant compounds are lost to the "
    "sample container itself",
    "Hedonic tone and annoyance assessment methods, which capture the fact that "
    "equal odour concentrations from different sources produce very different "
    "complaint rates",
    "Dispersion modelling conventions for odour impact assessment, which is how "
    "a stack concentration is translated into an expected exposure at a "
    "dwelling",
    # -- designing and sizing the bed --------------------------------------------
    "Empty bed residence time and elimination capacity reporting conventions, "
    "which are what make performance figures comparable between installations",
    "Packing material specification for surface area, void fraction, water "
    "retention and structural durability",
    "Air humidification and pretreatment design guidance, which addresses the "
    "commonest cause of bed failure",
    "Pressure drop measurement and fan sizing practice, since fan power is the "
    "whole of the running cost",
    # -- keeping it working ------------------------------------------------------
    "Moisture, pH and nutrient monitoring practice for operating beds",
    "Startup, acclimation and post-shutdown recovery procedures, which matter "
    "because a bed recovers over weeks and an outage has an odour consequence "
    "after it ends",
    "Media replacement and disposal scheduling for organic packings, which is a "
    "recurring cost commonly omitted from comparisons with thermal treatment",
    # -- and verifying the chemistry as well as the smell ------------------------
    "Speciated inlet and outlet analysis by gas chromatography and mass "
    "spectrometry, which distinguishes genuine removal from dilution where "
    "streams combine before the stack",
    "Continuous instrumentation calibration practice for sulphide and volatile "
    "organic compound monitors",
    "Bioaerosol sampling and enumeration methods, which apply to the treatment "
    "media as a source",
)
