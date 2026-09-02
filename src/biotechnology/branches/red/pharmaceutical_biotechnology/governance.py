# =============================================================================
#  biotechnology.branches.red.pharmaceutical_biotechnology.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the distinction between REGULATIONS (law) and STANDARDS
#  (technical consensus): see `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This subtype has the densest regulatory apparatus in the entire taxonomy,
#  because it is the oldest commercial application of biotechnology and the
#  rules have had four decades to accumulate. The ICH quality guidelines
#  listed under STANDARDS are formally voluntary but are incorporated by
#  reference into the law of every major market, which is the clearest example
#  in this library of a standard that is a regulation in everything but name.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
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
#  Four decades old, hundreds of approved products, thousands of tonnes of
#  installed bioreactor capacity, and taught as routine industrial practice.
#  This is the reference point against which every other MATURITY value in the
#  red branch should be judged.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#  A marketing authorisation from a national or supranational agency is
#  required before sale, and the manufacturing site itself is separately
#  licensed and inspected.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL.
#  Production bioreactors run at 2000 L and multiples thereof, in purpose-built
#  plants costing hundreds of millions of euro. Contrast `red.gene_therapy`,
#  which uses the same molecular biology at BENCH scale.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

DOMAINS: Tuple[Domain, ...] = (Domain.HEALTH,)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED.
#  Universal across jurisdictions. Divergence is about evidence standards for
#  biosimilars and about price, never about whether authorisation is needed.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS - instruments with legal force
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- European Union: the medicine ---------------------------------------
    "EU Directive 2001/83/EC on the Community code relating to medicinal "
    "products for human use",
    "EU Regulation (EC) No 726/2004 establishing the European Medicines "
    "Agency and the centralised authorisation procedure, mandatory for all "
    "biotechnology-derived medicines",
    # ---- European Union: the site and the trial -----------------------------
    "EU Directive 2003/94/EC on good manufacturing practice",
    "EU Regulation (EU) No 536/2014 on clinical trials",
    "EU Directive 2009/41/EC on contained use of genetically modified "
    "micro-organisms, which covers the production strain",
    # ---- United States -------------------------------------------------------
    "US Public Health Service Act section 351 biologics licence application",
    "US Biologics Price Competition and Innovation Act 2009, creating the "
    "biosimilar pathway",
    "US 21 CFR Parts 210 and 211 current good manufacturing practice",
    # ---- International harmonisation with legal effect -----------------------
    "ICH Q5A-Q5E incorporated into EU and US law by reference",
)


# =============================================================================
#  STANDARDS - technical consensus documents
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- sterile and biological manufacture ---------------------------------
    "EU GMP Annex 1 manufacture of sterile medicinal products",
    "EU GMP Annex 2 manufacture of biological active substances and medicinal "
    "products for human use",
    "ISO 13408 aseptic processing of health care products",
    "ISO 14644 cleanrooms and associated controlled environments",
    # ---- product quality and lifecycle --------------------------------------
    "ICH Q8(R2) pharmaceutical development, introducing quality by design",
    "ICH Q9 quality risk management",
    "ICH Q10 pharmaceutical quality system",
    "ICH Q11 development and manufacture of drug substances",
    "ICH Q12 lifecycle management of post-approval changes",
    # ---- compendial ----------------------------------------------------------
    "Ph. Eur. and USP monographs for biotechnological products",
    "EMA and FDA guidelines on similar biological medicinal products",
)
