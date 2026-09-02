# =============================================================================
#  biotechnology.branches.red.vaccine_development.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two things make this record's governance unusual.
#
#  First, SCALE is POPULATION rather than BENCH or INDUSTRIAL. A vaccine is the
#  only medicine in this taxonomy whose therapeutic unit is a population: its
#  effect on the person who receives it is only part of the point, and the
#  calculation that justifies a national programme is epidemiological rather
#  than clinical.
#
#  Second, WHO prequalification appears under STANDARDS rather than
#  REGULATIONS, and is arguably the most consequential entry in either list. It
#  has no legal force anywhere. It nonetheless determines which products United
#  Nations agencies may purchase, which in practice decides what is available
#  across much of the world. It is the clearest example in this library of a
#  voluntary standard functioning as a market gate.
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
#  Two centuries old, delivered in billions of doses a year, and the subject of
#  routine national programmes almost everywhere. Individual platforms within
#  it are newer, but the practice is not.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#  A marketing authorisation is required, and unusually the release of each
#  individual batch is separately tested and certified by an official control
#  laboratory. That extra step exists because of the 1955 Cutter incident
#  recorded in history.py.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION.
#  The only red-branch record with this value. See the header note.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS
#  HEALTH is obvious. SECURITY is included because vaccine capacity is treated
#  as national infrastructure and because medical countermeasures are the
#  defensive core of `dark.biodefence_countermeasures`.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.HEALTH, Domain.SECURITY)

REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- European Union: the product -----------------------------------------
    "EU Directive 2001/83/EC on medicinal products for human use",
    "EU Regulation (EC) No 726/2004 centralised authorisation procedure",
    "EU Regulation (EU) 2022/2371 on serious cross-border threats to health",
    # ---- European Union: the batch -------------------------------------------
    "EU Official Control Authority Batch Release, required for every batch of "
    "every vaccine before it may be placed on the market",
    # ---- European Union: the trial -------------------------------------------
    "EU Regulation (EU) No 536/2014 on clinical trials",
    "ICH E11(R1) clinical investigation of medicinal products in paediatric "
    "populations",
    # ---- United States -------------------------------------------------------
    "US Public Health Service Act section 351 biologics licence",
    "US National Childhood Vaccine Injury Act 1986, which created a no-fault "
    "compensation scheme in order to keep manufacturers in the market",
    # ---- International -------------------------------------------------------
    "International Health Regulations (2005)",
    "National immunisation acts and school-entry requirements, which vary "
    "widely and are the point at which vaccination becomes a civil liberties "
    "question rather than a medical one",
)


# =============================================================================
#  STANDARDS
#  WHO prequalification is listed first deliberately. See the header note.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- the de facto global market gate --------------------------------------
    "WHO prequalification, which has no legal force and nonetheless determines "
    "what United Nations agencies may purchase",
    # ---- technical guidance ----------------------------------------------------
    "WHO Technical Report Series guidelines on vaccine quality, safety and "
    "efficacy",
    "WHO Vaccine Vial Monitor specification, a heat-sensitive label that tells "
    "a health worker whether a dose is still viable",
    # ---- compendial -------------------------------------------------------------
    "Ph. Eur. general monograph 0153 on vaccines for human use",
    "USP general chapters on biological products",
    # ---- manufacture -------------------------------------------------------------
    "EU GMP Annex 1 manufacture of sterile medicinal products",
    "EU GMP Annex 2 biological medicinal products",
    "ISO 13408 aseptic processing of health care products",
    # ---- cold chain -------------------------------------------------------------
    "WHO Performance, Quality and Safety prequalification for cold chain "
    "equipment",
    "ISO 21973 general requirements for transportation of biological material",
)
