# =============================================================================
#  biotechnology.branches.blue.marine_biomaterials.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has a governance shape found nowhere else in the library,
#  because its raw material arrives from the wrong direction.
#
#      THE RAW MATERIAL IS AN ANIMAL BY-PRODUCT, AND IT IS REGULATED AS ONE.
#
#  Crustacean shell and fish skin are not raw materials in law. They are animal
#  by-products, governed by rules written to prevent disease transmission and
#  to keep unfit material out of the food and feed chains. Those rules
#  determine what may be collected, how it must be transported, what
#  documentation follows it, and which category of by-product may be used for
#  what purpose. A material intended for a medical device must be traceable
#  back to a species and a consignment, and a fish market does not issue that
#  paperwork by default.
#
#  This is the practical reason a material that is abundant and effectively
#  free is nonetheless difficult to bring into a regulated application, and it
#  is a separate obstacle from the variability problem recorded in `metrics.py`.
#
#  THE SECOND FEATURE IS THAT THE SAME MOLECULE MEETS FOUR REGIMES. Chitosan is
#  a medical device when it is a haemostatic dressing, a food additive when it
#  clarifies a drink, a fertilising product when it is a biostimulant, and a
#  registered chemical when it is a flocculant. One substance, four
#  authorisations, four sets of specifications, and a manufacturer must decide
#  early which one it is making for.
#
#  A THIRD, WHICH IS SPECIFIC AND UNRESOLVED: shellfish allergen labelling.
#  Purified chitosan should not carry the tropomyosin responsible for shellfish
#  allergy, and practice is nonetheless conservative because the evidence is
#  incomplete. The residual protein metric in `metrics.py` is how that argument
#  is actually made.
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
#  MATURITY = COMMERCIAL, and the value spans an unusually wide range.
#
#  Agar has been industrial since the nineteenth century, alginate dressings
#  since 1983 and chitosan haemostats since 2003, which is ESTABLISHED for
#  those products. Against that, the standardisation failure recorded in
#  `history.py` still keeps many materials out of regulated use, and the
#  biomimetic structural materials are largely at laboratory scale.
#
#  COMMERCIAL is the honest average: several long-established products and a
#  field that has not converted most of its promise.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED. A national agency or notified body decides before an
#  implantable or wound-contact material may be placed on the market, and the
#  animal by-product rules require prior approval of the collection and
#  processing establishments themselves.
#
#  Note that the same polymer sold as an industrial flocculant would sit at
#  ROUTINE. The tier records the activity at its most demanding point, which is
#  the medical application that the field's effort is directed at.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit is an extraction and processing plant handling
#  waste streams in tonnage. The biomimetic materials sit at BENCH and are a
#  minority of the record by volume, which is stated in `practice.py` rather
#  than by splitting the value.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. MATERIALS is the sector. HEALTH is claimed because the medical
#  applications are where the value and nearly all the regulatory burden sit.
#  ENVIRONMENT is claimed on waste valorisation, with the qualification
#  recorded in `practice.CHALLENGES` that conventional chitin extraction is
#  chemically harsh and generates its own effluent, so the environmental case
#  is demonstrated rather than assumed.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.HEALTH,
    Domain.ENVIRONMENT,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. Medical devices require conformity
#  assessment, food additives require listing, fertilising products require
#  compliance with their regulation, and the by-product establishments require
#  approval. Every route into a market is a prior permission.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law. The first group is the one that surprises people and the one
#  that governs whether the raw material can be used at all.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the raw material is a by-product, not a raw material -------------------
    "Regulation (EC) No 1069/2009 on animal by-products and Regulation (EU) No "
    "142/2011 implementing it, which categorise shell, skin and offcuts, "
    "require approval of collecting and processing establishments, and "
    "determine which category may be used for which purpose",
    "Traceability requirements under Regulation (EC) No 178/2002, which for a "
    "device-grade material means tracing a consignment back to a species and a "
    "landing that a fish market does not document by default",
    "Regulation (EC) No 853/2004, where the by-product stream originates in a "
    "food business",
    # -- the material as a medical product ---------------------------------------
    "Regulation (EU) 2017/745 on medical devices, under which wound dressings, "
    "haemostats, bone graft substitutes and dental impression materials are "
    "classified and assessed, with implantable and resorbable materials in the "
    "highest classes",
    "Regulation (EU) 2017/746 on in vitro diagnostic medical devices, where the "
    "material is part of a diagnostic system",
    "Pharmacopoeial requirements where the polymer is a pharmaceutical "
    "excipient rather than a device component",
    # -- the same molecule, other markets ------------------------------------------
    "Regulation (EC) No 1333/2008 on food additives, under which alginate, "
    "agar and carrageenan are authorised",
    "Regulation (EU) 2019/1009 on fertilising products, covering chitosan and "
    "seaweed extract biostimulants",
    "Regulation (EC) No 1907/2006 REACH, for industrial grades placed on the "
    "market as chemicals",
    "Regulation (EC) No 1223/2009 on cosmetic products, for the collagen and "
    "extract applications",
    # -- what must be declared -------------------------------------------------------
    "Regulation (EU) No 1169/2011 on food information, whose allergen "
    "provisions cover crustacean-derived ingredients and are the origin of the "
    "unresolved labelling position on purified chitosan",
    # -- where the organism came from ------------------------------------------------
    "The Convention on Biological Diversity and the Nagoya Protocol, applicable "
    "to materials from organisms collected in another country's waters, and "
    "CITES where the source species is protected",
)


# =============================================================================
#  STANDARDS
#  Not law, and in this record their ABSENCE is the principal finding rather
#  than their content.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the standards that exist -----------------------------------------------
    "ISO 10993 series on the biological evaluation of medical devices, which is "
    "how a marine-derived material demonstrates biocompatibility",
    "ISO 13485 quality management for medical device manufacture",
    "Pharmacopoeial monographs for alginate, agar and carrageenan, which exist "
    "and which specify far less than a device manufacturer needs",
    "Joint FAO/WHO Expert Committee on Food Additives specifications for the "
    "food-grade polysaccharides",
    # -- the standards that are missing, which is the point ---------------------
    "Absence of agreed reference materials and specifications for degree of "
    "deacetylation, uronic acid ratio, sulphation pattern and molecular weight "
    "distribution, which `history.py` records as the principal barrier to "
    "regulated use and which two decades of review articles have identified "
    "without resolving",
    "Absence of harmonised analytical methods, so two laboratories reporting a "
    "degree of deacetylation may not be measuring it the same way",
    "Reporting conventions requiring the compositional parameters to accompany "
    "any performance figure, without which a published result is not "
    "reproducible",
    # -- purity and process --------------------------------------------------------
    "Endotoxin testing to pharmacopoeial methods, and residual protein limits, "
    "which is what separates a medical grade from an industrial one and is also "
    "how the allergen argument is evidenced",
    "Good Manufacturing Practice for device and excipient manufacture",
    # -- provenance -----------------------------------------------------------------
    "Species identification of the source material by molecular methods, since "
    "a mixed by-product stream is not a defined raw material",
    "Sustainability certification of the fishery or farm the by-product "
    "originates from, which is increasingly required by purchasers even where "
    "no regulation demands it",
)
