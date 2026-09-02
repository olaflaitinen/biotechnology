# =============================================================================
#  biotechnology.branches.red.cell_therapy.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Cell therapy is governed by two overlapping legal regimes that were written
#  for different purposes and have never been fully reconciled. Tissue and
#  cell law (Directive 2004/23/EC) governs donation, procurement and testing
#  of the starting material; medicines law (Regulation 1394/2007) governs the
#  finished product. A hospital that collects cells is a tissue establishment;
#  the same hospital, once it manipulates them, becomes a manufacturer. Where
#  the line falls decides whether an academic centre may treat its own
#  patients, which is the most consequential regulatory question in the field.
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
#  MATURITY = COMMERCIAL.
#  A judgement call, because the branch spans two eras. Haematopoietic stem
#  cell transplantation alone would be ESTABLISHED: it is fifty years old and
#  performed tens of thousands of times a year. Engineered cell products are
#  COMMERCIAL: approved and sold, but fewer than a dozen exist and delivery is
#  confined to accredited centres. The lower of the two is recorded, because
#  the record describes the modern engineered field.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#  Marketing authorisation is required, the manufacturing site is licensed,
#  and in the European Union the treating centre must additionally be
#  qualified by the marketing authorisation holder.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = BENCH.
#  An autologous batch occupies a single culture vessel. This is the smallest
#  manufacturing scale of any approved medicine in existence, and it is the
#  root cause of the cost problem recorded in practice.CHALLENGES.
# -----------------------------------------------------------------------------
SCALE = Scale.BENCH

DOMAINS: Tuple[Domain, ...] = (Domain.HEALTH,)

REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Note the two-regime structure described in the header: the first group
#  governs the finished medicine, the second the human starting material.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- the finished medicine ----------------------------------------------
    "EU Regulation (EC) No 1394/2007 on advanced therapy medicinal products",
    "EU Directive 2001/83/EC on medicinal products for human use",
    "EU Regulation (EC) No 726/2004 centralised authorisation procedure",
    # ---- the human starting material -----------------------------------------
    "EU Directive 2004/23/EC on standards of quality and safety for human "
    "tissues and cells",
    "EU Directive 2006/17/EC on donation, procurement and testing",
    "EU Directive 2006/86/EC on traceability and serious adverse reactions",
    # ---- where the cells are gene-modified -----------------------------------
    "EU Directive 2009/41/EC on contained use of genetically modified "
    "micro-organisms",
    # ---- United States -------------------------------------------------------
    "US FDA 21 CFR Part 1271, the risk-based HCT/P framework",
    "US Public Health Service Act section 351 for more-than-minimally "
    "manipulated products",
    # ---- clinical ------------------------------------------------------------
    "EU Regulation (EU) No 536/2014 on clinical trials",
    "ICH E6(R2) Good Clinical Practice",
)


# =============================================================================
#  STANDARDS
#  JACIE and FACT accreditation deserve particular attention: they are
#  voluntary professional standards that in practice determine which hospitals
#  may deliver these products at all, which makes them a more effective access
#  control than most of the legislation above.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- centre accreditation, the real gatekeeper --------------------------
    "JACIE standards for haematopoietic cell therapy in Europe",
    "FACT standards for cellular therapy in North America",
    # ---- manufacture ---------------------------------------------------------
    "EU GMP Part IV for advanced therapy medicinal products",
    "EU GMP Annex 1 manufacture of sterile medicinal products",
    "ISO 14644 cleanrooms and controlled environments",
    # ---- material handling ---------------------------------------------------
    "ISO 20387 biotechnology: biobanking general requirements",
    "ISO 21973 general requirements for transportation of cells for "
    "therapeutic use",
    # ---- product characterisation --------------------------------------------
    "Ph. Eur. 5.14 and general chapters on cell-based preparations",
    "USP <1046> cellular and tissue-based products",
)
