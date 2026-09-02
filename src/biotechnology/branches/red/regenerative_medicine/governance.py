# =============================================================================
#  biotechnology.branches.red.regenerative_medicine.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record sits at a regulatory junction that exists nowhere else in the
#  taxonomy. A tissue-engineered construct is simultaneously:
#
#      a MEDICINE, because it contains living cells intended to act
#      pharmacologically or to regenerate tissue;
#      a MEDICAL DEVICE, because it contains a scaffold that acts by physical
#      means;
#      a HUMAN TISSUE, because the starting material came out of a person.
#
#  Three regimes, three competent authorities, three sets of quality
#  expectations, and a classification decision that changes which applies. In
#  the European Union a combined product falls under Regulation 1394/2007 with
#  the device component assessed against the essential requirements of the
#  medical device rules, which is a genuinely awkward hybrid.
#
#  THE MINIMAL MANIPULATION QUESTION
#  The most consequential regulatory line in this field is the boundary between
#  a transplanted tissue and a manufactured medicine. Fat removed and reinjected
#  is a tissue transplant. Fat removed, enzymatically digested, expanded in
#  culture and reinjected is a medicine requiring authorisation. Almost the
#  entire unregulated clinic sector recorded in `practice.CHALLENGES` operates
#  by claiming to be on the tissue side of that line.
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
#  MATURITY = PILOT, and this is the lowest value in the red branch.
#  The judgement is deliberate and arguable. Cultured epidermal autografts have
#  treated patients since 1981, which taken alone would be ESTABLISHED. But the
#  field as it describes itself, meaning engineered replacement tissue, is at
#  demonstration scale: a handful of authorised products, small series, and
#  nothing thick. PILOT records what the discipline is doing now rather than
#  the one thing it solved forty years ago.
# -----------------------------------------------------------------------------
MATURITY = Maturity.PILOT

RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = BENCH.
#  A construct is made for one patient, in a vessel measured in millilitres,
#  and is often shaped to that patient's anatomy. There is no batch.
# -----------------------------------------------------------------------------
SCALE = Scale.BENCH

# -----------------------------------------------------------------------------
#  DOMAINS
#  HEALTH is the purpose. MATERIALS is not decoration: the scaffold is a
#  designed material, its stiffness and degradation rate are materials
#  properties, and the failures recorded in metrics.py are materials failures.
#  This is the only red-branch record that carries it.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.HEALTH, Domain.MATERIALS)

REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Grouped by which of the three regimes each belongs to. The junction between
#  them is the subject of the header note.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- as a medicine -------------------------------------------------------
    "EU Regulation (EC) No 1394/2007 on advanced therapy medicinal products, "
    "which defines the tissue-engineered product category",
    "EU Directive 2001/83/EC on medicinal products for human use",
    "EU Regulation (EC) No 726/2004 centralised authorisation procedure",
    "EU hospital exemption under Regulation 1394/2007 Article 28, permitting "
    "non-routine preparation for an individual patient under national "
    "authorisation, which is both a genuine clinical need and the widest gap in "
    "the regime",
    # ---- as a device ----------------------------------------------------------
    "EU Regulation (EU) 2017/745 on medical devices, applied to the scaffold "
    "component of a combined product",
    # ---- as human tissue -------------------------------------------------------
    "EU Directive 2004/23/EC on standards of quality and safety for human "
    "tissues and cells",
    "EU Directive 2006/17/EC on donation, procurement and testing",
    "EU Directive 2006/86/EC on traceability and adverse reaction reporting",
    # ---- the United States, where the same line is drawn differently -----------
    "US FDA 21 CFR Part 1271, and the more-than-minimal-manipulation and "
    "homologous-use criteria that decide whether a product is a tissue or a "
    "regulated medicine",
    "US Public Health Service Act section 351, applying where those criteria "
    "are exceeded",
    # ---- the trial --------------------------------------------------------------
    "EU Regulation (EU) No 536/2014 on clinical trials",
)


# =============================================================================
#  STANDARDS
#  Unusually materials-heavy, because the scaffold is evaluated as a material
#  before it is evaluated as a treatment.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- the material ---------------------------------------------------------
    "ISO 10993 series, biological evaluation of medical devices, which governs "
    "whether a scaffold is tolerated at all",
    "ASTM F2150 standard guide for characterisation of scaffolds used in "
    "tissue-engineered medical products",
    "ASTM F2451 assessment of tissue-engineered cartilage products",
    "ISO 13485 medical devices, quality management systems",
    # ---- the cells ------------------------------------------------------------
    "ISO 20387 biotechnology, biobanking general requirements",
    "ISO 24603 requirements for human and mouse pluripotent stem cells",
    "International Society for Stem Cell Research guidelines for stem cell "
    "research and clinical translation, which explicitly address unproven "
    "commercial offerings",
    # ---- the finished product ---------------------------------------------------
    "EU GMP Part IV for advanced therapy medicinal products",
    "EU GMP Annex 1 manufacture of sterile medicinal products",
    "Ph. Eur. 5.14 and general chapters on cell-based preparations",
    "USP <1046> cellular and tissue-based products",
    # ---- transport -------------------------------------------------------------
    "ISO 21973 general requirements for transportation of cells for therapeutic "
    "use",
)
