# =============================================================================
#  biotechnology.branches.red.gene_therapy.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE -  maturity, risk, scale, and the rules.
# -----------------------------------------------------------------------------
#
#  WHAT LIVES HERE
#      MATURITY            how far from the bench the field has travelled
#      RISK_TIER           how much oversight the work attracts
#      SCALE               the physical size at which it is practised
#      DOMAINS             which cross-cutting sectors it serves
#      REGULATORY_STATUS   how a product class is treated by authorities
#      REGULATIONS         the specific instruments that apply
#      STANDARDS           the voluntary or technical standards that apply
#
#  THE DISTINCTION BETWEEN REGULATIONS AND STANDARDS
#  A regulation is law: breaking it is an offence, and a named authority
#  enforces it. A standard is a technical consensus document: it may be
#  referenced by a regulation, in which case compliance becomes effectively
#  mandatory, but the document itself has no independent legal force. Keeping
#  them in separate tuples matters because a reader in a third country can
#  substitute their own regulations while keeping the same standards.
#
#  WHY THESE ENUMS AND NOT FREE TEXT
#  Because these four fields are what the library is filtered on. A policy
#  analyst asking "which parts of biotechnology are at pilot scale and
#  attract national-agency oversight?" is running a query, and a query needs a
#  controlled vocabulary. See `biotechnology.core.enums` for the full
#  definitions, each of which carries a plain-language explanation of its own.
#
#  A NOTE ON JURISDICTION
#  The regulations listed lean European, because this library is written in
#  Finland and the European instruments are the ones the authors can cite
#  accurately. United States instruments are included where they are the
#  global reference point. This is a stated bias, not a hidden one, and
#  contributions adding other jurisdictions are the most welcome kind.
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
#  MATURITY = COMMERCIAL, not ESTABLISHED.
#  Products are approved and sold, so it is past PILOT. It is not ESTABLISHED
#  because fewer than twenty products exist worldwide, treatment is confined
#  to accredited centres, and no product has been observed over a patient
#  lifetime. ESTABLISHED is reserved for routine, decades-old practice.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#  A national or supranational agency must authorise the product before it may
#  be sold. It is not RESTRICTED: the materials and methods are freely
#  available to any competent laboratory, and the control point is the
#  marketing authorisation rather than access to the technology.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = BENCH.
#  This surprises people, so it is worth stating explicitly. The therapeutic
#  effect is delivered at the scale of one patient, and vector manufacture,
#  though demanding, runs in vessels measured in tens or low hundreds of
#  litres rather than cubic metres. Contrast `white.microbial_fermentation`,
#  which is INDUSTRIAL, and `red.vaccine_development`, which is POPULATION.
# -----------------------------------------------------------------------------
SCALE = Scale.BENCH

# -----------------------------------------------------------------------------
#  DOMAINS
#  Single-domain. Gene therapy serves human health and nothing else. Contrast
#  `green.agricultural_genome_editing`, which uses much of the same molecular
#  toolkit but serves FOOD and ENVIRONMENT.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.HEALTH,)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED.
#  Not VARIES: unlike genome-edited crops, every major jurisdiction agrees
#  that a gene therapy is a medicine requiring a marketing authorisation.
#  Jurisdictions differ on evidence requirements and on price, not on
#  classification.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS - instruments with legal force
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- European Union: the product itself ---------------------------------
    "EU Regulation (EC) No 1394/2007 on advanced therapy medicinal products",
    "EU Directive 2001/83/EC on medicinal products for human use",
    "EU Regulation (EC) No 726/2004 establishing the centralised procedure, "
    "under which every advanced therapy must be authorised",
    # ---- European Union: because the vector is often a GMO -------------------
    "EU Directive 2001/18/EC on the deliberate release of genetically "
    "modified organisms, which applies in parallel where the vector is a GMO",
    "EU Directive 2009/41/EC on the contained use of genetically modified "
    "micro-organisms, applying to the manufacturing site",
    # ---- European Union: the trial ------------------------------------------
    "EU Regulation (EU) No 536/2014 on clinical trials on medicinal products",
    # ---- United States -------------------------------------------------------
    "US Public Health Service Act section 351 biologics licence",
    "US FDA 21 CFR Part 1271 on human cells, tissues and cellular products",
    # ---- International -------------------------------------------------------
    "ICH E6(R2) Good Clinical Practice",
    "Council of Europe Convention on Human Rights and Biomedicine, which "
    "prohibits interventions modifying the germline",
)


# =============================================================================
#  STANDARDS - technical consensus documents
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- manufacture ---------------------------------------------------------
    "EU GMP Part IV, Guidelines on Good Manufacturing Practice specific to "
    "advanced therapy medicinal products",
    "EU GMP Annex 1 on the manufacture of sterile medicinal products",
    # ---- product quality -----------------------------------------------------
    "Ph. Eur. 5.14 gene transfer medicinal products for human use",
    "USP <1047> gene therapy product quality",
    "ICH Q5A(R2) viral safety evaluation of biotechnology products",
    # ---- materials and biobanking -------------------------------------------
    "ISO 20387 biotechnology: biobanking general requirements",
    "ISO 9001 quality management systems, for supporting operations",
)
