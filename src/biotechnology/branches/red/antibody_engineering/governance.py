# =============================================================================
#  biotechnology.branches.red.antibody_engineering.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Three things distinguish the governance of this record from its neighbours.
#
#  First, ANIMAL USE. Almost no other red-branch subtype depends on immunising
#  a live animal as a routine production step. Directive 2010/63/EU is
#  therefore a first-order constraint here rather than a background one, and
#  display technologies are adopted partly because they replace immunisation
#  entirely, which is a Three Rs argument as much as a technical one.
#
#  Second, NAMING. The WHO International Nonproprietary Name scheme is listed
#  under STANDARDS and is unusually consequential: the suffix in a name such as
#  "-mab" or "-tug" encodes the format and the source, so the generic name of
#  an antibody is itself a machine-readable classification. The scheme was
#  revised in 2021 because the old suffixes had run out of descriptive room.
#
#  Third, FIRST-IN-HUMAN DESIGN. The 2006 TGN1412 trial recorded in history.py
#  produced binding European guidance that applies to this modality more
#  directly than to any other, and it is cited below as a regulation rather
#  than as a standard because it conditions authorisation of the trial itself.
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
#  Roughly a hundred and fifty approved products, four decades of clinical use,
#  and a design workflow taught as routine industrial practice. Individual
#  formats inside the record are newer: a bispecific T-cell engager alone would
#  be COMMERCIAL, and an intracellular nanobody would be RESEARCH. The value
#  records the discipline, not its newest corner.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = BENCH.
#  This is a design discipline. The library, the panning and the
#  characterisation all happen in millilitres. Manufacture of the resulting
#  molecule is INDUSTRIAL, and lives in `red.pharmaceutical_biotechnology`.
#  Keeping the two separate is the whole reason both records exist.
# -----------------------------------------------------------------------------
SCALE = Scale.BENCH

DOMAINS: Tuple[Domain, ...] = (Domain.HEALTH,)

REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Grouped by what each governs: the medicine, the trial, or the animals used
#  to make it.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- the medicine --------------------------------------------------------
    "EU Directive 2001/83/EC on medicinal products for human use",
    "EU Regulation (EC) No 726/2004 centralised authorisation procedure, "
    "mandatory for all biotechnology-derived medicines",
    "US Public Health Service Act section 351 biologics licence",
    "US Biologics Price Competition and Innovation Act 2009, under which "
    "antibody biosimilars are authorised",
    # ---- the trial -----------------------------------------------------------
    "EU Regulation (EU) No 536/2014 on clinical trials",
    "EMA Guideline on strategies to identify and mitigate risks for "
    "first-in-human and early clinical trials, EMEA/CHMP/SWP/28367/07 Rev 1, "
    "written in direct response to the 2006 TGN1412 incident",
    "ICH S6(R1) preclinical safety evaluation of biotechnology-derived "
    "pharmaceuticals, which sets the species-relevance requirement",
    # ---- the animals ----------------------------------------------------------
    "EU Directive 2010/63/EU on the protection of animals used for scientific "
    "purposes, a first-order constraint here because immunisation is a routine "
    "production step",
    "EU Directive 2010/63/EU Article 4, the Three Rs, which is the formal basis "
    "for preferring display technologies over immunisation where either would "
    "work",
    # ---- the product specification ----------------------------------------------
    "ICH Q6B specifications for biotechnological and biological products",
)


# =============================================================================
#  STANDARDS
#  The naming scheme is listed first because it is the one a reader will meet
#  before any of the others, in every product name they have ever seen.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- naming, which is itself a classification -----------------------------
    "WHO International Nonproprietary Name scheme for monoclonal antibodies, "
    "revised in 2021 to replace the single -mab stem with -tug, -bart, -mig "
    "and -ment, encoding format rather than species of origin",
    # ---- numbering and structural description ---------------------------------
    "IMGT unique numbering for immunoglobulin and T-cell receptor variable "
    "domains",
    "Kabat and Chothia numbering schemes, still in parallel use, which is a "
    "routine source of confusion when comparing two papers",
    # ---- comparability and change control ---------------------------------------
    "ICH Q5E comparability of products subject to changes in manufacturing",
    "EMA Guideline on similar biological medicinal products containing "
    "monoclonal antibodies",
    # ---- measurement -------------------------------------------------------------
    "WHO International Standards for biological reference preparations, "
    "without which titres from different laboratories are not comparable",
    "ISO 20395 requirements for evaluating the performance of quantification "
    "methods for nucleic acid target sequences",
    # ---- manufacture ---------------------------------------------------------------
    "EU GMP Annex 2 biological medicinal products",
    "ICH Q11 development and manufacture of drug substances",
)
