# =============================================================================
#  biotechnology.branches.green.plant_genetic_engineering.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the most consequential governance facet in the taxonomy, because it
#  is the one where the regulation, rather than the science, determines what
#  exists.
#
#  Two structural features are worth stating before the lists.
#
#  PROCESS VERSUS PRODUCT. The European Union regulates by PROCESS: an organism
#  is a GMO because of how it was made, regardless of what it is. Canada
#  regulates by PRODUCT: a plant with a novel trait is assessed on the trait,
#  regardless of how it arose, so a mutagenised variety and a transgenic one
#  face the same scrutiny if they present the same novelty. These two
#  philosophies produce different answers about identical plants, and almost
#  every international dispute in this field traces back to them.
#
#  THE COST IS THE POLICY. The dossier requirements below are not incidental
#  detail; they are the binding constraint named in `narrative.DESCRIPTION`.
#  Tens of millions of euro per event means the technology is available only to
#  organisations that can spend it, on crops that can repay it. Any discussion
#  of who benefits from this field is a discussion about this list.
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
#  Three decades of commercial cultivation across roughly two hundred million
#  hectares annually, in around thirty countries. The trait set is narrow and
#  has barely changed, but narrowness is not immaturity: it is the predictable
#  output of the cost structure recorded below.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#  Authorisation is required before cultivation, before import, and separately
#  before use in food and in feed. A single event can therefore need several
#  independent approvals in the same jurisdiction, and asynchronous approval
#  between trading partners is itself a recurring trade problem.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = FIELD.
#  The unit is a hectare. Everything in `metrics.py` that matters is measured
#  across a field season under real pest pressure, which is exactly why the
#  yield figure cannot be quoted as a property of the technology.
# -----------------------------------------------------------------------------
SCALE = Scale.FIELD

DOMAINS: Tuple[Domain, ...] = (Domain.FOOD, Domain.ENVIRONMENT)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, and this is the clearest case of that value in
#  the library. The same event is routinely cultivated in the Americas, imported
#  but not grown in Europe, and prohibited elsewhere. The organism does not
#  change; the answer does.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Grouped by what each controls: release into the environment, entry into the
#  food chain, movement across borders, and ownership.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- releasing it into the environment -----------------------------------
    "EU Directive 2001/18/EC on the deliberate release into the environment of "
    "genetically modified organisms, the process-based instrument that defines "
    "a GMO by the technique used to make it",
    "EU Directive (EU) 2015/412, which allows a Member State to prohibit "
    "cultivation of an EU-authorised event on its own territory for non-safety "
    "reasons",
    "EU Directive 2009/41/EC on contained use, which governs the laboratory and "
    "glasshouse stages",
    # ---- letting it into the food chain ---------------------------------------
    "EU Regulation (EC) No 1829/2003 on genetically modified food and feed",
    "EU Regulation (EC) No 1830/2003 on traceability and labelling, which "
    "imposes the 0.9 per cent adventitious presence threshold",
    # ---- moving it across borders ----------------------------------------------
    "Cartagena Protocol on Biosafety to the Convention on Biological Diversity, "
    "and the advance informed agreement procedure it establishes",
    "Nagoya-Kuala Lumpur Supplementary Protocol on Liability and Redress",
    "National biosafety laws implementing the Cartagena Protocol, which is why "
    "most countries have a framework even where no event has ever been approved",
    # ---- the alternative philosophy ---------------------------------------------
    "US coordinated framework, under which USDA APHIS, EPA and FDA each assess "
    "a different aspect of the same plant under pre-existing statutes",
    "Canadian Plants with Novel Traits regime, which regulates by product "
    "rather than by process and therefore captures some conventionally bred "
    "varieties that the EU regime does not",
    # ---- who owns it ---------------------------------------------------------------
    "Patent law over transgenic events and enabling techniques, which interacts "
    "with plant variety rights and is covered in "
    "`purple.biotechnology_patents`",
)


# =============================================================================
#  STANDARDS
#  Codex is listed first because it is the internationally agreed basis for
#  food safety assessment, and because it introduced the comparative approach
#  that every national regime now uses in some form.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- assessing whether it is safe to eat ---------------------------------
    "Codex Alimentarius Guideline CAC/GL 45-2003 for the conduct of food safety "
    "assessment of foods derived from recombinant-DNA plants",
    "Codex Principles CAC/GL 44-2003 for the risk analysis of foods derived "
    "from modern biotechnology",
    "EFSA Guidance for risk assessment of food and feed from genetically "
    "modified plants",
    # ---- the comparator ---------------------------------------------------------
    "OECD consensus documents on the biology and composition of individual crop "
    "species, which define what a conventional counterpart looks like and are "
    "therefore the baseline every comparative assessment rests on",
    # ---- detecting and tracing it ------------------------------------------------
    "ISO 21569 horizontal methods for molecular biomarker analysis, qualitative "
    "nucleic acid based methods for GMO detection",
    "ISO 21570 quantitative nucleic acid based methods",
    "European Union Reference Laboratory validated event-specific detection "
    "methods, one per authorised event",
    # ---- managing resistance -------------------------------------------------------
    "Insect Resistance Management plans imposed as conditions of authorisation, "
    "which convert the evolutionary calculation in `metrics.py` into an "
    "enforceable refuge requirement",
    # ---- seed quality ---------------------------------------------------------------
    "OECD seed schemes for varietal certification",
    "ISTA rules for seed testing and purity determination",
)
