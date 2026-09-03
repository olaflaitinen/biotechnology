# =============================================================================
#  biotechnology.branches.grey.bioremediation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE REGULATED OBJECT HERE IS NOT THE TECHNOLOGY. IT IS THE LAND.
#
#  Almost every other record in this library is governed by rules about what
#  may be done: an approval for a product, a licence for a process, a permit
#  for a release. Contaminated land regulation asks a different question first,
#  and it is a question about people rather than about biology:
#
#      WHO IS LIABLE FOR CONTAMINATION SOMEBODY ELSE CAUSED, POSSIBLY DECADES
#      AGO, AND POSSIBLY WHEN IT WAS LEGAL?
#
#  That question determines whether a site is treated at all. The choice
#  between bioremediation and excavation is made by whoever carries the
#  liability, against a deadline that is usually commercial. The microbiology
#  is downstream of it.
#
#  WHICH IS WHY THE RISK TIER IS NOT ABOUT THE ORGANISMS. The organisms used
#  are overwhelmingly indigenous and unmodified, and in monitored natural
#  attenuation nothing is added at all. The governance weight comes from the
#  contamination, the disposal of what is produced, and the injection of
#  amendments into groundwater that somebody may later drink.
#
#  A SECOND POINT WORTH RECORDING. Cleanup targets are risk-based rather than
#  absolute. A number is derived from an exposure pathway and a land use, so
#  the SAME concentration passes for an industrial site and fails for a
#  playground. This is a defensible way to regulate and it has a consequence
#  worth stating: it makes the acceptable endpoint depend on who is expected to
#  live there.
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
#  Hydrocarbon bioremediation has been routine commercial practice for over
#  thirty years, there is a competitive contractor industry, regulators publish
#  guidance on how to design and evidence it, and monitored natural attenuation
#  is an accepted regulatory outcome. That is the definition of established.
#
#  The value is assigned to the practice as a whole and not to every
#  application in it. Per- and polyfluoroalkyl substances have no biological
#  treatment at all, and the metal work is a set of partial techniques. An
#  established field can contain unsolved problems, and this one does.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#
#  An authority approves the remediation plan before work starts, sets the
#  cleanup target, and signs off completion. Injecting amendments into
#  groundwater requires a permit in most jurisdictions, and moving
#  contaminated material triggers waste law.
#
#  It is not RESTRICTED, which in this library means access is limited to
#  vetted actors. Any competent contractor may perform bioremediation; the
#  approval is of the plan rather than of the person.
#
#  Note carefully that this value reflects GOVERNANCE INTENSITY and not danger.
#  The organisms are ordinary soil bacteria already present at the site. What
#  is regulated is the contamination and the land.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = FIELD.
#
#  The unit of work is a site: a plume of a given extent in a given aquifer,
#  treated in place under weather nobody controls. That is the definition of
#  FIELD in this library.
#
#  INDUSTRIAL would be wrong even for the ex situ variants, because a biopile
#  is still an open heap of site material rather than a plant with a defined
#  throughput. POPULATION would be wrong because the endpoint is a
#  concentration in a defined volume rather than a distribution across people.
# -----------------------------------------------------------------------------
SCALE = Scale.FIELD

# -----------------------------------------------------------------------------
#  DOMAINS. ENVIRONMENT first and unarguably.
#
#  HEALTH is included because cleanup targets are derived from human exposure
#  pathways: the number a site must reach is calculated from what a person
#  would ingest, inhale or absorb, so this is a human health intervention
#  performed on soil.
#
#  MATERIALS is included narrowly, for the metal work, where a contaminant is
#  concentrated into a material that then has to be managed and occasionally
#  has value. It is the smallest of the three and is not padding: it is the
#  domain the metal applications actually sit in.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENVIRONMENT,
    Domain.HEALTH,
    Domain.MATERIALS,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED.
#
#  A remediation plan is submitted, approved, executed and signed off. That is
#  a prior authorisation of a specific activity at a specific place, which is
#  what AUTHORISED denotes.
#
#  VARIES was considered, because targets and liability regimes differ
#  substantially between jurisdictions. It was rejected: the differences are in
#  the numbers and in who pays, not in whether authorisation is required. It is
#  required everywhere that regulates contaminated land at all.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law. The liability group is first because it decides whether
#  anything happens at all.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- who pays, which decides whether a site is treated ----------------------
    "Contaminated land liability regimes assigning responsibility to polluters "
    "and in their absence to current owners, which determines whether a site is "
    "remediated or fenced and is therefore the most consequential law in this "
    "record",
    "Retroactive and strict liability provisions, under which a party may be "
    "responsible for contamination that was lawful when it was created",
    "Prospective purchaser and innocent landowner provisions, which limit "
    "liability for a buyer who investigated properly and which are what make "
    "contaminated sites transactable at all",
    "Environmental liability directives establishing prevention and remedying "
    "duties for operators, including the European Union Directive 2004/35/EC",
    # -- the site process itself ------------------------------------------------
    "Site investigation, risk assessment and remediation plan approval "
    "requirements, under which an authority sets the cleanup target and "
    "approves the method before work begins",
    "Risk-based cleanup target derivation tied to land use and exposure "
    "pathway, so the acceptable endpoint for an industrial site differs from "
    "that for housing or a school",
    "Completion certification and residual monitoring obligations, which for a "
    "monitored natural attenuation site continue for years after the "
    "remediation itself is finished",
    "Institutional controls and land use restrictions recorded against title, "
    "which are how a site is closed with contamination still present",
    # -- the water underneath ----------------------------------------------------
    "Groundwater protection legislation, including the Groundwater Directive "
    "2006/118/EC and the Water Framework Directive 2000/60/EC, which set the "
    "standards a treated aquifer is judged against",
    "Underground injection control and permitting for the introduction of "
    "amendments, nutrients or electron donors into an aquifer",
    "Drinking water abstraction protection zones, which frequently prohibit "
    "the very injections that would treat a plume beneath them",
    # -- the material that is moved or produced -----------------------------------
    "Waste framework legislation governing excavated contaminated soil, "
    "including its classification as hazardous waste and the point at which "
    "treated material ceases to be waste",
    "Hazardous waste disposal and transfrontier shipment rules, which apply to "
    "the concentrated metal-bearing biomass and sludges the metal applications "
    "produce",
    # -- the organisms, which is the shortest group in this facet -----------------
    "Deliberate release requirements for genetically modified organisms, which "
    "in practice exclude engineered degraders from field use and are part of "
    "the reason the 1980 patented organism was never deployed",
    "Biosafety and import controls on non-indigenous microbial cultures used "
    "for augmentation",
    # -- and what may be claimed ---------------------------------------------------
    "Consumer and environmental claim rules applied to remediation products, "
    "under which a vendor culture sold on unsubstantiated performance claims is "
    "an advertising matter as well as a technical one",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what turns a falling concentration into
#  evidence, which is where this field lost its credibility and regained it.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- proving degradation rather than dilution -------------------------------
    "Multiple lines of evidence protocols for monitored natural attenuation, "
    "requiring concentration trends, geochemical footprints and degrader "
    "presence together rather than any one alone",
    "Compound-specific isotope analysis method standards, which are what "
    "distinguish destruction from dilution and are the strongest single line of "
    "evidence available",
    "Molecular biological tool application guidance for quantifying degrader "
    "organisms and functional genes in site samples",
    "Microcosm and treatability study design conventions, establishing whether "
    "degradation occurs at all before a design is committed to",
    # -- measuring the site honestly ----------------------------------------------
    "Groundwater and soil sampling standards, including low-flow purging, which "
    "materially changes the concentrations reported from the same well",
    "ISO 18400 series soil sampling standards and equivalent national guidance",
    "Bioavailability assessment conventions using mild extraction or passive "
    "sampling rather than total extraction, which is the difference between "
    "what is present and what is treatable",
    "Data quality objectives and statistical design for demonstrating that a "
    "target has been met rather than that one sample happened to pass",
    # -- designing and predicting ---------------------------------------------------
    "Conceptual site model development conventions, which force the source, "
    "pathway and receptor to be stated before a treatment is chosen",
    "Fate and transport model application guidance, and the calibration "
    "practice that keeps a model a prediction rather than an illustration",
    "Remedial option appraisal and sustainable remediation frameworks, which "
    "weigh the carbon and energy cost of the remedy against the harm it "
    "removes, and which frequently favour biology for exactly that reason",
    # -- and the professional practice around it ------------------------------------
    "Phase I and Phase II environmental site assessment standards, which are "
    "the due diligence a purchaser relies on and the basis of the innocent "
    "landowner protections above",
    "Contractor competence and accreditation schemes for remediation practice",
    "Worker protection practice for excavation and handling of contaminated "
    "material, which is the exposure risk a remediation project actually "
    "creates",
)
