# =============================================================================
#  biotechnology.branches.green.veterinary_vaccines.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has a governance feature found nowhere else in the library: a
#  body of international rules that can make the RIGHT intervention the wrong
#  decision.
#
#  The World Organisation for Animal Health sets the standards under which
#  countries recognise each other's disease status, and those standards are
#  referenced by the World Trade Organization agreement on sanitary measures.
#  For several diseases, a country that vaccinates loses its disease-free
#  status and therefore its export markets, because vaccinated animals cannot
#  be distinguished serologically from infected ones. The rational response for
#  an exporting country has often been to cull healthy animals rather than
#  vaccinate them. Six million animals were killed in the United Kingdom in
#  2001 substantially for this reason.
#
#  DIVA vaccines exist to dissolve that conflict, and the standards have been
#  progressively revised to recognise vaccination with DIVA surveillance. This
#  is therefore one of the few places in this library where a technical advance
#  was made specifically in order to change a legal rule, and where the rule
#  moved in response.
#
#  A second feature: veterinary medicines regulation is genuinely separate from
#  human medicines regulation, with its own legal basis, its own agency
#  committee and a mandatory extra question that human regulation never asks,
#  which is how long a treated animal must be withheld from the food chain.
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
#  MATURITY = ESTABLISHED. Pasteur's fowl cholera vaccine of 1879 makes this
#  the oldest deliberate vaccinology of any kind, and tens of billions of doses
#  are administered annually. Newer platforms exist within the field, but the
#  field itself is not emerging in any sense.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = MODERATE, and the reasoning is worth stating because a reader
#  might expect either extreme.
#
#  It is not LOW: live attenuated vaccines can revert or recombine, mass
#  administration removes any possibility of individual clinical judgement, and
#  residues in food-producing animals are a human exposure route. Working with
#  seed material for high-consequence pathogens such as foot-and-mouth disease
#  requires high-containment facilities.
#
#  It is not HIGH: the products are administered to animals rather than people,
#  the platforms are long-established, and the counterfactual is an untreated
#  outbreak whose risk is considerably greater.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.MODERATE

# -----------------------------------------------------------------------------
#  SCALE = POPULATION. This matches `red.vaccine_development` and for the same
#  reason: the unit of intervention is a herd, a flock or a national livestock
#  population, not an individual. It is the correct value even for a companion
#  animal vaccine, because rabies vaccination of dogs is a population measure
#  aimed at human deaths.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. AGRICULTURE is the sector, HEALTHCARE is claimed because zoonosis
#  control and antimicrobial stewardship are human health interventions
#  delivered through animals, and RESEARCH covers the surveillance and strain
#  matching that keep the products current.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.AGRICULTURE,
    Domain.HEALTHCARE,
    Domain.RESEARCH,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. Veterinary vaccines are licensed medicinal
#  products with marketing authorisations, dossiers, batch release and
#  pharmacovigilance, exactly as human vaccines are, under a separate legal
#  code.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law. Grouped by what each instrument actually controls.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the medicines code ----------------------------------------------------
    "Regulation (EU) 2019/6 on veterinary medicinal products, the legal basis "
    "for authorisation, manufacture, distribution and pharmacovigilance, "
    "deliberately separate from the human medicines code",
    "Regulation (EU) 2019/4 on medicated feed, which governs the route by which "
    "routine antibiotic medication was historically delivered",
    "United States Virus-Serum-Toxin Act, under which veterinary biologics are "
    "licensed by the Department of Agriculture rather than by the Food and Drug "
    "Administration",
    # -- what may remain in food -----------------------------------------------
    "Regulation (EC) No 470/2009 and the maximum residue limits established "
    "under it, which set the withdrawal period before a treated animal may "
    "enter the food chain",
    # -- disease control powers -------------------------------------------------
    "Regulation (EU) 2016/429, the Animal Health Law, which sets out categorised "
    "diseases and the powers to require vaccination, movement restriction or "
    "culling",
    # -- welfare ---------------------------------------------------------------
    "Directive 2010/63/EU on the protection of animals used for scientific "
    "purposes, which governs the challenge studies on which efficacy claims "
    "rest",
    "Council Regulation (EC) No 1099/2009 on the protection of animals at the "
    "time of killing, which applies to the culling that vaccination is intended "
    "to avoid",
    # -- containment -----------------------------------------------------------
    "National high-containment requirements for work with foot-and-mouth "
    "disease and other high-consequence animal pathogens, including seed virus "
    "handling",
)


# =============================================================================
#  STANDARDS
#  Not law. The first two entries are the most consequential documents in this
#  record, because trade status follows from them and trade status is what
#  decides whether vaccination is used.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the documents that decide whether vaccination is politically possible --
    "World Organisation for Animal Health Terrestrial Animal Health Code, which "
    "defines disease-free status, the conditions under which vaccination is "
    "compatible with it, and the surveillance required to demonstrate freedom",
    "World Organisation for Animal Health Manual of Diagnostic Tests and "
    "Vaccines for Terrestrial Animals, which prescribes the reference methods "
    "and potency tests",
    # -- the quality baseline --------------------------------------------------
    "European Pharmacopoeia monographs for veterinary vaccines, including batch "
    "potency and safety requirements",
    "Veterinary International Conference on Harmonisation guidelines, the "
    "veterinary counterpart of ICH",
    "Good Manufacturing Practice as applied to veterinary immunologicals",
    # -- surveillance and reporting --------------------------------------------
    "World Organisation for Animal Health WAHIS notification requirements for "
    "listed diseases",
    "European Surveillance of Veterinary Antimicrobial Consumption reporting, "
    "which produced the halving figure recorded in `history.py`",
    # -- laboratory competence -------------------------------------------------
    "ISO/IEC 17025 accreditation for the diagnostic laboratories that perform "
    "DIVA and surveillance testing",
    # -- the framing -----------------------------------------------------------
    "The tripartite One Health framework of the World Health Organization, the "
    "World Organisation for Animal Health and the Food and Agriculture "
    "Organization, under which animal vaccination is treated as a human health "
    "measure",
)
