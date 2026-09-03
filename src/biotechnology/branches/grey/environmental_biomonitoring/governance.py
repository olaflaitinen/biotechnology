# =============================================================================
#  biotechnology.branches.grey.environmental_biomonitoring.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS RECORD IS NOT MOSTLY REGULATED. IT IS MOSTLY THE THING THAT MAKES
#  REGULATION ENFORCEABLE.
#
#  Water framework legislation does not regulate biomonitoring; it REQUIRES it,
#  and defines a legal classification in its terms. A discharge consent is
#  enforced by measurements taken here. A remediation is signed off on evidence
#  produced here. The record's position in the regulatory system is that of the
#  instrument rather than the subject.
#
#      WHICH MEANS THE STANDARDS FACET CARRIES MORE WEIGHT THAN THE
#      REGULATIONS FACET, AND THAT IS THE CORRECT SHAPE FOR THIS RECORD.
#
#  A method that is not comparable between laboratories cannot support an
#  enforcement action, so the intercalibration and quality assurance work below
#  is doing legal work, not housekeeping.
#
#  THE ONE PLACE WHERE THIS RECORD IS GENUINELY THE REGULATED SUBJECT IS
#  WASTEWATER SURVEILLANCE, AND IT DESERVES ITS OWN TREATMENT.
#
#  Measuring a sewer measures people. Nobody in a catchment consented, the
#  method works precisely because it does not require consent, and it extends
#  without any technical change from disease prevalence to drug use to
#  anything else a population excretes. A small catchment can identify a
#  building. This is a genuine and unresolved governance question and the
#  record states it plainly rather than filing it under public health.
#
#  A SECOND POINT: THE ORGANISMS ARE SUBJECTS. Electrofishing, netting and
#  caged sentinel deployment involve killing or holding animals, so animal
#  welfare law applies to a monitoring programme in a way it applies to nothing
#  else in this branch.
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
#  Biotic indices have been regulatory instruments since the 1960s, ecological
#  status is a legal classification, and standardised methods, accreditation
#  schemes and intercalibration exercises all exist. That is established by any
#  reading.
#
#  Environmental DNA is younger and is already accepted in statutory survey and
#  invasive species programmes, so it does not pull the value down. The record
#  is honest in `metrics.py` about which of its methods carry weaker evidence.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED.
#
#  Monitoring itself is a low-intensity activity: sampling licences, permits to
#  handle protected species, animal welfare approval for procedures on fish,
#  and accreditation where the data will be used for enforcement. Those are
#  compliance obligations rather than prior approval of a technology.
#
#  It sits deliberately below the REGULATED tier assigned to
#  `grey.bioremediation` and `grey.wastewater_treatment`. Measuring a river
#  attracts far less governance than discharging into it, which is correct.
#
#  Wastewater surveillance of human populations is the part of this record that
#  would justify a higher tier, and it is governed by data protection and
#  research ethics regimes rather than by environmental permitting. That is
#  recorded in REGULATIONS instead of being allowed to move this value, since
#  the value describes the record as a whole.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION, and this is the only record in the grey branch to carry
#  it.
#
#  The unit assessed is not a vessel or a site. It is a water body, a
#  catchment, a coastline, or in the surveillance applications a human
#  population. Indices are defined per water body type, ecological status is
#  classified per water body, and a sewershed is a population.
#
#  FIELD would describe the act of taking a sample and would miss what is being
#  measured, which is the assemblage rather than the plot. INDUSTRIAL would be
#  plainly wrong.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. Three, and the third is unusual.
#
#  ENVIRONMENT is the substance of the record.
#
#  HEALTH is claimed on the wastewater surveillance applications, which are
#  genuinely public health instruments, and on the exposure assessment that
#  connects contaminated water to people.
#
#  INFORMATION is claimed because this record's product IS data. It generates
#  sequence archives, long time series and reference databases, and its
#  characteristic failures are informational: incomplete reference coverage,
#  bioinformatic thresholds changing a species list, and the loss of continuity
#  when a programme is interrupted. Very few records in this library have a
#  genuine claim to that domain and this one does.
#
#  GOVERNANCE was considered, since the record makes environmental law
#  enforceable. It was declined: producing evidence that regulators use is not
#  the same as being a governance activity, and `purple` holds the records for
#  which it is.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENVIRONMENT,
    Domain.HEALTH,
    Domain.INFORMATION,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = NOTIFIED.
#
#  Sampling licences are held, protected species work is permitted, laboratories
#  are accredited, and results are reported to authorities. What is not present
#  is any approval of the monitoring technique itself: a regulator specifies
#  the method to be used rather than authorising a practitioner to use it.
#
#  AUTHORISED would misdescribe that. The authorisation in this branch attaches
#  to discharging, remediating and mining, and this record is how those
#  authorisations are checked.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.NOTIFIED


# =============================================================================
#  REGULATIONS
#  Binding law. The first group is law that REQUIRES this record rather than
#  constraining it.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- law that requires biomonitoring ----------------------------------------
    "The Water Framework Directive 2000/60/EC and national equivalents, which "
    "define ecological status as a legal classification in biological terms and "
    "require member states to achieve good status",
    "Marine Strategy Framework Directive 2008/56/EC descriptor monitoring, "
    "which extends the same logic to marine waters",
    "Habitats Directive 92/43/EEC and Birds Directive 2009/147/EC surveillance "
    "obligations, which require the condition of designated species and "
    "habitats to be reported periodically",
    "Discharge consent monitoring and reporting conditions, which is how the "
    "measurements in this record become enforcement evidence against the "
    "installations in the rest of this branch",
    "Remediation verification and completion certification requirements, which "
    "specify what evidence will be accepted before a site is signed off",
    # -- getting the samples lawfully --------------------------------------------
    "Sampling licences and permits to take, disturb or handle protected "
    "species, which apply to exactly the rare species a survey is designed to "
    "find",
    "Animal welfare legislation governing procedures on protected animals, "
    "including Directive 2010/63/EU, which applies to electrofishing, netting "
    "and caged sentinel deployment and makes the organisms subjects rather than "
    "instruments",
    "Access and benefit sharing obligations under the Nagoya Protocol, which "
    "apply to genetic material collected in another jurisdiction and therefore "
    "to environmental DNA sampling across borders",
    "Biosecurity and equipment disinfection requirements between sites, since a "
    "survey team moving between catchments is itself a vector",
    # -- the surveillance question, which is the real governance issue ------------
    "Data protection law applied to wastewater surveillance, including the "
    "General Data Protection Regulation, where a catchment small enough to "
    "identify a building or an institution makes an aggregate measurement "
    "personal in effect",
    "Research ethics and institutional review requirements for population-level "
    "wastewater studies, which are the only place consent is considered at all "
    "since no individual in a sewershed agreed to be measured",
    "Public health surveillance mandates and reporting obligations, which "
    "authorise disease monitoring and do not by themselves authorise the "
    "measurement of anything else a population excretes",
    "Restrictions on the secondary use of wastewater data, which is the "
    "unresolved question, since nothing technical prevents extending the method "
    "from pathogens to drug use to any other marker",
    # -- and the data itself -------------------------------------------------------
    "Environmental information access legislation, including the Aarhus "
    "Convention, which gives the public a right to the monitoring data that "
    "regulators hold",
    "Sequence data deposit requirements and database access conditions, which "
    "govern the reference resources every molecular method here depends on",
)


# =============================================================================
#  STANDARDS
#  Not law, and in this record they carry the enforcement weight. A method that
#  is not comparable between laboratories cannot support a prosecution.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- making results comparable, which is what makes them enforceable -------
    "Intercalibration exercises establishing that class boundaries mean the "
    "same thing between countries and laboratories, which is what allows a "
    "classification to be compared across a shared river basin",
    "ISO 17025 laboratory accreditation for analysis intended for enforcement "
    "use",
    "Ring test and proficiency scheme participation for taxonomic and molecular "
    "identification",
    "Reference condition derivation guidance, which is the documented basis for "
    "a judgement that `metrics.py` places first and identifies as a judgement",
    # -- taking a sample that means something ----------------------------------
    "Standardised field sampling protocols including kick sampling, "
    "electrofishing and net specification, whose comparability depends entirely "
    "on identical execution",
    "Environmental DNA sampling and filtration protocols specifying volume, "
    "pore size, preservation and field blanks, which are the largest source of "
    "between-study variation when unspecified",
    "Contamination control practice from field through laboratory, since a "
    "method sensitive enough to detect a rare species detects the previous "
    "sample as readily",
    "Survey design and statistical power conventions, including the replication "
    "needed before an absence may be reported as an absence",
    # -- turning readings into conclusions --------------------------------------
    "Bioinformatic pipeline specification including clustering and assignment "
    "thresholds, which materially change the species list produced from "
    "identical raw data and must therefore be reported",
    "Occupancy modelling conventions accounting for imperfect detection",
    "Multimetric index construction and validation guidance",
    "Reference sequence database curation standards, which are the invisible "
    "dependency of every molecular result and which rest on taxonomic work the "
    "field is losing",
    # -- and keeping the record ---------------------------------------------------
    "Long-term data archiving, versioning and custody arrangements, which are "
    "what make a time series valuable and what a funding interruption destroys "
    "retrospectively",
    "Open data and FAIR data practice for environmental sequence and monitoring "
    "records",
    "Metadata standards for sample provenance, which determine whether a result "
    "can be reinterpreted years later against a better database",
    "Ethical review practice for wastewater surveillance study design, "
    "including catchment size thresholds below which a result should not be "
    "reported",
)
