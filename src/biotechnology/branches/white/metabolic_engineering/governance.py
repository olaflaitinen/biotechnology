# =============================================================================
#  biotechnology.branches.white.metabolic_engineering.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is the reason `RegulatoryStatus.VARIES` exists in the
#  vocabulary, and it is worth explaining before the lists.
#
#  Metabolic engineering has NO REGULATORY REGIME OF ITS OWN. The organism is
#  handled under contained use rules, which are the same whether it makes a
#  fuel or a flavour. Everything after that is determined entirely by WHAT THE
#  PATHWAY MAKES:
#
#      a food ingredient   novel food authorisation, and the question of
#                          whether a fermentation-derived vanillin may be
#                          called natural is a legal question, not a chemical
#                          one
#      a feed additive     feed additive authorisation
#      a drug substance    GMP, and the route locked into the dossier as
#                          described in `white.biocatalysis`
#      a fuel or polymer   chemicals law and fuel quality standards
#      a cosmetic          cosmetics regulation and its own ingredient rules
#
#  The same strain technology therefore meets five different regulators
#  depending on the molecule. A reader looking for the rules that govern this
#  field will not find them in one place, and that is the finding rather than a
#  gap in this record.
#
#  A SECOND POINT: CONTAINMENT IS THE WHOLE SAFETY CASE. These organisms are
#  engineered to be poor competitors outside a fermenter, they are killed at
#  the end of the run, and they are not intended for release. That is why this
#  record sits far from `green.plant_genetic_engineering` in regulatory terms
#  despite using similar tools.
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
#  MATURITY = COMMERCIAL, and the value hides a genuine split that
#  `history.py` makes visible.
#
#  Amino acid and vitamin fermentation is established beyond argument and has
#  operated at millions of tonnes since the 1950s. But those strains were built
#  largely by mutagenesis and selection, not by the rational model-guided
#  design that defines the modern discipline. Designed pathways reached the
#  market from 2006 and have a mixed commercial record, including the
#  artemisinin case. COMMERCIAL is the honest value for the discipline as
#  practised now.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED. The vocabulary measures governance intensity. Work
#  with these organisms requires a contained use notification or consent and
#  institutional biosafety oversight, which is exactly what CONTROLLED denotes.
#
#  It is not REGULATED, because no agency approves a metabolic engineering
#  project as such. What gets approved is the resulting substance, under
#  whichever regime that substance falls into.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit of operation is a production fermenter.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. MATERIALS covers the chemicals and polymer precursors that are the
#  largest application. ENERGY covers fuels, where the economics are hardest.
#  FOOD is claimed on amino acids, vitamins, sweeteners and flavour compounds,
#  which is where the oldest and largest tonnages actually are.
#
#  HEALTH is deliberately NOT claimed despite the artemisinin case, because
#  pharmaceutical application of this technology is carried by
#  `red.pharmaceutical_biotechnology` and by `white.biocatalysis`, and claiming
#  it here would blur three records that are usefully distinct.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.ENERGY,
    Domain.FOOD,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, for the reason set out at length in the module
#  header. The technology has no status of its own; the product does, and the
#  product could be a fuel, a food ingredient, a feed additive, a polymer
#  precursor or a drug substance.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law. The first group applies always; everything after it applies
#  only if the pathway happens to make that kind of molecule.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- applies to every project in this record -------------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, which is the single instrument that governs this field "
    "regardless of what is being produced",
    "Directive 2000/54/EC on biological agents at work",
    "National contained use notification and institutional biosafety committee "
    "requirements, which determine the containment class of a given strain",
    # -- if the product goes into food ------------------------------------------
    "Regulation (EU) 2015/2283 on novel foods, under which a "
    "fermentation-derived food ingredient with no significant consumption "
    "history requires authorisation",
    "Regulation (EC) No 1334/2008 on flavourings, which decides whether a "
    "fermentation-derived flavour compound may be labelled natural, a legal "
    "distinction rather than a chemical one",
    "Regulation (EC) No 1829/2003, relevant where the product carries material "
    "from the modified organism rather than being purified away from it",
    # -- if the product goes into feed --------------------------------------------
    "Regulation (EC) No 1831/2003 on feed additives, which covers the amino "
    "acids that are this field's largest tonnage",
    # -- if the product is a chemical or a fuel -------------------------------------
    "Regulation (EC) No 1907/2006 REACH and Regulation (EC) No 1272/2008 CLP",
    "Directive 2018/2001 on renewable energy, including its sustainability and "
    "feedstock criteria, which govern whether a biofuel counts towards a target",
    # -- if the product is a medicine ------------------------------------------------
    "EudraLex Volume 4 Good Manufacturing Practice, Part II, where the strain "
    "produces a drug substance or its precursor",
    # -- where the genetic parts came from ---------------------------------------------
    "The Convention on Biological Diversity and the Nagoya Protocol, which "
    "apply to the enzymes and pathways sourced from organisms collected in "
    "another country, including where only sequence information was used",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is unusual in this library: it exists because the
#  field's own results were not reproducible, and the community wrote its own
#  reporting rules in response.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- making results mean the same thing twice ------------------------------
    "Minimum Information Required in the Annotation of Models, the community "
    "standard for reporting a metabolic model so that another group can rerun "
    "it",
    "Systems Biology Markup Language for exchanging metabolic models between "
    "tools",
    "Community conventions on reporting titre, rate and yield together with the "
    "cultivation conditions, without which the trio is not comparable between "
    "laboratories",
    "Reporting of carbon balance closure as a data quality condition, which is "
    "the fastest available check that a published result is internally "
    "consistent",
    # -- naming parts and strains consistently ----------------------------------
    "Synthetic Biology Open Language and standard part registries for "
    "describing genetic constructs unambiguously",
    "Strain deposit in a recognised culture collection under the Budapest "
    "Treaty where patent protection is sought",
    # -- how the plant is run ----------------------------------------------------
    "ISO 9001, and HACCP and FSSC 22000 where the product enters food or feed",
    "Good Manufacturing Practice for pharmaceutical intermediates",
    # -- what may be claimed ------------------------------------------------------
    "ISO 14040 and ISO 14044 life cycle assessment, required before a "
    "fermentation route may be called lower impact than the petrochemical one "
    "it replaces, since feedstock cultivation carries its own burden",
    "Greenhouse gas accounting conventions for biobased products, including "
    "how biogenic carbon is treated",
    # -- responsible practice ---------------------------------------------------------
    "Institutional and industry codes on responsible engineering of "
    "microorganisms, including screening of synthesised DNA orders, which "
    "connects this record to `dark.biosecurity`",
)
