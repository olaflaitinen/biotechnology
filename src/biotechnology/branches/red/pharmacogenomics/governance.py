# =============================================================================
#  biotechnology.branches.red.pharmacogenomics.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is governed by three regimes that were written for different
#  purposes and were never reconciled with each other.
#
#    THE DEVICE REGIME governs the test as a product placed on the market.
#    THE MEDICINES REGIME governs the drug label that tells a prescriber what
#    to do with the result.
#    THE DATA PROTECTION REGIME governs the result itself, which is genetic
#    data about a person and, unusually, about their untested relatives too.
#
#  A genotype has properties no other clinical measurement has: it never
#  changes, so it need only be generated once and should therefore persist for
#  a lifetime; and it is partially shared with parents, siblings and children
#  who never consented to anything. Article 9 of the GDPR treats it as a
#  special category for exactly that reason.
#
#  The CPIC guidelines appear under STANDARDS and are, in practice, the
#  operative document. They have no legal force in any jurisdiction. Health
#  systems implement them anyway, because they are the only freely available,
#  regularly updated, genotype-to-action mapping that exists.
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
#  MATURITY = COMMERCIAL, not ESTABLISHED.
#  A judgement call, and the most arguable one in this record. The science has
#  been settled for decades and several tests are standard of care, which
#  argues for ESTABLISHED. But most patients in most countries are still
#  prescribed without any pharmacogenomic input at all, and a practice that
#  reaches a minority of its eligible population is not routine. COMMERCIAL
#  records the deployment rather than the knowledge.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION.
#  Unusual for a test. It is set this way because the modern form of the
#  practice is pre-emptive panel testing of everyone at first contact with a
#  health system, which is a population-level programme rather than a
#  patient-level investigation. Reactive single-gene testing alone would be
#  BENCH.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS
#  HEALTH is the purpose. INFORMATION is not decoration: the deliverable is a
#  data object that must persist for a lifetime, move between record systems,
#  and fire a decision support rule decades after it was generated. The
#  bottleneck in practice.CHALLENGES is an information one.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.HEALTH, Domain.INFORMATION)

REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Grouped by the three unreconciled regimes described in the header.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- the test as a device -------------------------------------------------
    "EU Regulation (EU) 2017/746 on in vitro diagnostic medical devices, under "
    "which a companion diagnostic is class C",
    "US FDA premarket review of companion diagnostics, and enforcement "
    "discretion over direct-to-consumer pharmacogenomic reports",
    "US Clinical Laboratory Improvement Amendments certification of the "
    "performing laboratory",
    # ---- the drug label -------------------------------------------------------
    "EU Directive 2001/83/EC, under which pharmacogenomic information is placed "
    "in the summary of product characteristics",
    "EMA Guideline on the use of pharmacogenetic methodologies in the "
    "pharmacokinetic evaluation of medicinal products",
    "US FDA Table of Pharmacogenetic Associations and pharmacogenomic "
    "biomarker labelling",
    "ICH E15 definitions for genomic biomarkers and sample coding categories",
    # ---- the result as personal data --------------------------------------------
    "GDPR Article 9, which classes genetic data as a special category requiring "
    "an explicit legal basis",
    "GDPR Article 22 on decisions based solely on automated processing, which "
    "reaches an automated dose recommendation",
    "Council of Europe Convention on Human Rights and Biomedicine, Article 12, "
    "restricting predictive genetic testing to health purposes",
    "National genetic non-discrimination provisions governing insurance and "
    "employment, which vary sharply between countries",
)


# =============================================================================
#  STANDARDS
#  CPIC is listed first because it is the operative document, notwithstanding
#  having no legal force anywhere.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- what to do with a result ---------------------------------------------
    "CPIC clinical practice guidelines, freely published, regularly updated, "
    "and the de facto genotype-to-action mapping used worldwide",
    "Dutch Pharmacogenetics Working Group recommendations, the other major "
    "guideline set, which occasionally differs from CPIC and says so",
    # ---- naming the variants ----------------------------------------------------
    "PharmVar star allele nomenclature, the reference definition of what each "
    "allele designation means",
    "Human Genome Variation Society sequence variant nomenclature",
    # ---- carrying the result ------------------------------------------------------
    "HL7 FHIR Genomics implementation guide, which is how a result survives a "
    "change of records system",
    "ISO 20428 health informatics, structure of genomic sequencing report data",
    # ---- laboratory quality ---------------------------------------------------------
    "ISO 15189 medical laboratories, requirements for quality and competence",
    "Pharmacogenetics external quality assessment schemes",
    "ACMG technical standards for pharmacogenomic testing",
)
