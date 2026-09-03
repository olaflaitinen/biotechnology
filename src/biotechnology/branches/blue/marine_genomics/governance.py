# =============================================================================
#  biotechnology.branches.blue.marine_genomics.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record carries the governance problem that defines the blue branch, and
#  it is worth stating in full because no other branch in this library has
#  anything comparable.
#
#  WHERE THE SAMPLE COMES FROM DETERMINES EVERYTHING, AND THREE ZONES APPLY.
#
#      inside a state's waters      the Nagoya Protocol applies. Prior informed
#                                   consent and mutually agreed terms are
#                                   required, and the obligation attaches to
#                                   the SEQUENCE and not only to the physical
#                                   sample.
#
#      the deep seabed              administered as the common heritage of
#                                   mankind through the International Seabed
#                                   Authority, a regime built for minerals that
#                                   fits genetic resources awkwardly.
#
#      the high seas water column   until 2023, essentially nothing. Two thirds
#                                   of the ocean, and no answer to who may
#                                   sample it, publish the sequence or patent
#                                   what it encodes.
#
#  THE 2023 AGREEMENT ON MARINE BIOLOGICAL DIVERSITY BEYOND NATIONAL
#  JURISDICTION is the first instrument to address that third zone directly. It
#  covers marine genetic resources including digital sequence information, and
#  it establishes notification and benefit-sharing arrangements. It is recent,
#  its implementation is unsettled, and it does not retroactively resolve the
#  status of the very large collections assembled during the decades when no
#  rule existed.
#
#  A SECOND FEATURE THAT MATTERS PRACTICALLY: DIGITAL SEQUENCE INFORMATION IS
#  THE CONTESTED CATEGORY. A physical sample can be tracked. A sequence can be
#  published, downloaded and used anywhere, which is exactly what open science
#  norms require and exactly what makes benefit sharing hard to enforce. This
#  record does not resolve that tension and does not pretend it is resolved.
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
#  MATURITY = ESTABLISHED. Culture-independent marine sequencing has been
#  routine since the 1990s, the surveys are global and standardised, and
#  environmental DNA is in regulatory use for invasive species monitoring.
#  Individual applications within it are newer; the method is not.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED, and the permit in question is unlike any other in
#  this library. It is not a biosafety permit: seawater and its DNA present
#  ordinary laboratory hazards and nothing more.
#
#  What requires permission is COLLECTION. Marine scientific research in
#  another state's waters requires that state's consent under the law of the
#  sea; sampling in a protected area requires a permit; access to genetic
#  resources requires prior informed consent under the Nagoya Protocol; and
#  work on protected species requires its own authorisation. A researcher who
#  needs four permissions before a bottle enters the water is not operating at
#  ROUTINE.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION. The unit of study is a community, a water mass or a
#  species across its range, rather than an organism or a vessel. This is the
#  same value `red.vaccine_development` carries and for the same structural
#  reason: the question being asked is about a population rather than an
#  individual.
#
#  BENCH would describe where the sequencing happens and would misdescribe what
#  is being measured. FIELD is closer and still wrong, since an ocean basin is
#  not a field site.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. INFORMATION is placed first and is the correct primary label: the
#  output of this record is data, databases and reference libraries rather than
#  a substance. ENVIRONMENT covers the monitoring and conservation
#  applications. HEALTH is claimed because the catalogues this field produces
#  are the search space for the medicines in `blue.marine_natural_products`,
#  and a domain filter that missed that connection would hide the field's
#  largest downstream consequence.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.INFORMATION,
    Domain.ENVIRONMENT,
    Domain.HEALTH,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = NOTIFIED. This is a deliberate choice over AUTHORISED
#  and it needs justifying.
#
#  No agency approves a marine genomics study as a product. What the
#  instruments below require is that the state whose waters are sampled is
#  informed and consents, that the resource holder gives prior informed
#  consent, and, under the 2023 agreement, that activities in areas beyond
#  national jurisdiction are notified. That pattern of prior notification and
#  consent rather than product approval is exactly what NOTIFIED denotes.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.NOTIFIED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by which zone of the ocean it governs. That grouping is
#  the point of this facet.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- which law applies at all, and where ------------------------------------
    "The United Nations Convention on the Law of the Sea, which defines the "
    "zones and under whose Part XIII marine scientific research in another "
    "state's waters requires that state's consent",
    # -- beyond national jurisdiction, the gap and its closing --------------------
    "The 2023 Agreement on marine biological diversity of areas beyond "
    "national jurisdiction, the first instrument to address marine genetic "
    "resources from the high seas, including digital sequence information",
    "International Seabed Authority rules for activities on the deep seabed, a "
    "regime designed for minerals and applied to a biological question",
    # -- inside national waters --------------------------------------------------
    "The Convention on Biological Diversity and the Nagoya Protocol on access "
    "and benefit sharing, under which prior informed consent and mutually "
    "agreed terms are required and the obligation follows the sequence rather "
    "than only the sample",
    "Regulation (EU) No 511/2014, which implements the Nagoya Protocol for "
    "users within the Union and imposes due diligence and record-keeping",
    "National marine scientific research permit requirements and territorial "
    "sea access conditions",
    # -- what may be collected, and from where -----------------------------------
    "Marine protected area legislation and site-specific sampling permits",
    "CITES and national protected species legislation, where the organism "
    "sampled is itself protected",
    "Ballast water management requirements, relevant where environmental DNA is "
    "used for compliance monitoring",
    # -- moving samples across borders --------------------------------------------
    "Biosecurity and phytosanitary import rules for transporting biological "
    "samples between jurisdictions",
    # -- what the data is ----------------------------------------------------------
    "Regulation (EU) 2016/679, applicable in the narrow but real case where "
    "human sequence is recovered incidentally from an environmental sample",
)


# =============================================================================
#  STANDARDS
#  Not law. In this field they carry unusual weight, because a survey that
#  cannot be compared with another survey has answered a question about one
#  bottle of water.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- making two surveys comparable -----------------------------------------
    "Minimum Information about any Sequence and the related genomic standards, "
    "which fix what must be reported alongside a sequence for it to be reusable",
    "Standardised sampling and filtration protocols from the major ocean "
    "sampling programmes, without which depth, volume and filter pore size vary "
    "enough to change the answer",
    "Environmental DNA reporting guidelines covering replication, controls and "
    "the distinction between detection and abundance",
    # -- naming things consistently ----------------------------------------------
    "Reference barcode library conventions, since environmental DNA can detect "
    "only what a library can name",
    "Taxonomic nomenclature conventions for lineages known only from sequence, "
    "which are still contested since the codes were written for organisms that "
    "could be deposited as specimens",
    # -- depositing the data -----------------------------------------------------
    "International Nucleotide Sequence Database Collaboration deposition "
    "requirements, which are what makes re-analysis cheaper than resampling",
    "FAIR data principles, which in this field have unusual force because "
    "collection cost so far exceeds analysis cost",
    # -- doing the science fairly --------------------------------------------------
    "Research collaboration norms against helicopter science, under which "
    "scientists from the sampled region are partners rather than a logistics "
    "arrangement, and which the 2023 agreement's capacity-building provisions "
    "are intended to reinforce",
    "Institutional codes on sampling impact, particularly for slow-growing "
    "deep-sea communities that will not recover within a human lifetime",
    # -- laboratory quality --------------------------------------------------------
    "ISO/IEC 17025 accreditation where environmental DNA results are used for "
    "regulatory decisions rather than for research",
)
