# =============================================================================
#  biotechnology.branches.white.biobased_chemicals.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The governing fact here is one that newcomers to the field consistently get
#  wrong, and it is worth stating before anything else.
#
#  A BIOBASED CHEMICAL IS REGULATED AS A CHEMICAL. THERE IS NO CONCESSION FOR
#  BEING BIOLOGICAL.
#
#  If a biobased route produces a molecule identical to the petrochemical one,
#  it is the same substance, with the same registration, the same
#  classification, the same hazard labelling and the same exposure limits. The
#  origin of the carbon changes nothing about the toxicology. And a NOVEL
#  biobased molecule is in a worse position than the incumbent rather than a
#  better one: it has no existing registration, so it must be registered from
#  scratch with its own toxicological dossier, at a cost that falls entirely on
#  a new entrant competing with an established product that was registered
#  decades ago.
#
#  This asymmetry is a real barrier and is rarely mentioned in enthusiastic
#  accounts of the bioeconomy. The regulatory system is not hostile to biobased
#  chemistry; it is simply indifferent to it, and indifference favours the
#  incumbent.
#
#  THE SECOND FEATURE IS THAT THE CLAIM IS NOW REGULATED EVEN WHERE THE
#  MOLECULE IS NOT. Rules against unsubstantiated environmental marketing mean
#  that calling a product biobased or renewable without evidence is itself a
#  regulated act. That is why radiocarbon content and life cycle assessment
#  appear in STANDARDS below as evidentiary requirements rather than as
#  marketing support.
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
#  MATURITY = COMMERCIAL. Citric acid, lactic acid and the amino acids are
#  established beyond argument and have been for decades. The designed-pathway
#  products of the last twenty years are genuinely commercial, at modest scale,
#  with a mixed survival record. ESTABLISHED would overstate the position of
#  everything after 2004; PILOT would insult everything before it.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED. A permit is required for contained use of the
#  production organism, and the substance itself requires registration before
#  it may be placed on the market in commercial quantity.
#
#  It is not REGULATED, because for most of these products no agency assesses
#  the process or approves the product individually before sale; registration
#  is a filing obligation with a dossier rather than an approval decision of the
#  kind that governs `white.bioprocess_engineering`.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. MATERIALS is the sector: chemicals, fibres, solvents and polymer
#  precursors are exactly what that label denotes. ENVIRONMENT carries the
#  justification and the substantiation burden.
#
#  FOOD is claimed for the same reason as in `white.biofuels`, and with an
#  important difference stated in the data rather than hidden: the feedstock
#  competition is real but roughly an order of magnitude smaller, because
#  chemicals are a much smaller share of petroleum use and are worth several
#  times more per tonne. The same hectare goes very much further here.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.ENVIRONMENT,
    Domain.FOOD,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. A substance must be registered before it may
#  be placed on the market above threshold quantities, and food contact,
#  cosmetic and biocidal applications each require their own prior
#  authorisation. This is a permissioned market, and being biobased grants no
#  exemption from any of it.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law. The first group applies identically to the petrochemical
#  equivalent, which is the point.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the substance, with no concession for its origin ----------------------
    "Regulation (EC) No 1907/2006 REACH, under which a novel biobased molecule "
    "must be registered from scratch with its own toxicological dossier while "
    "the incumbent it competes with was registered long ago",
    "Regulation (EC) No 1272/2008 CLP on classification, labelling and "
    "packaging, which depends on the molecule and not on where its carbon came "
    "from",
    "Regulation (EU) No 528/2012 on biocidal products, and Regulation (EC) No "
    "1223/2009 on cosmetic products, where the application requires its own "
    "authorisation",
    "Regulation (EC) No 1935/2004 and Regulation (EU) No 10/2011 on materials "
    "intended to come into contact with food",
    # -- the claim ---------------------------------------------------------------
    "Directive 2005/29/EC on unfair commercial practices and the subsequent "
    "instruments on substantiating environmental claims, which make an "
    "unevidenced biobased or renewable claim a regulated act",
    # -- the organism ------------------------------------------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, and Directive 2000/54/EC on biological agents at work",
    # -- the plant ----------------------------------------------------------------
    "Directive 2010/75/EU on industrial emissions, with discharge consents "
    "covering the salt and organic load that acid fermentation recovery "
    "produces",
    "Directive 2012/18/EU Seveso III where solvent or reagent inventories pass "
    "threshold quantities",
    # -- what the feedstock was ----------------------------------------------------
    "Sustainability criteria for biomass feedstock where a product claims "
    "renewable content or benefits from a support scheme",
    "The Nagoya Protocol, where the producing organism or its pathway derives "
    "from another country's genetic resources",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group exists because the biobased claim needs evidence,
#  and it is the one place where this record has an advantage over
#  `white.biofuels`: the property can be measured on the product itself.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- proving the claim, analytically ---------------------------------------
    "ASTM D6866 and EN 16640 for determining biobased carbon content by "
    "radiocarbon analysis, which verifies the claim on the finished product "
    "rather than by auditing the supply chain",
    "EN 16785 for determining the biobased content of products, including "
    "those containing both biobased and fossil carbon",
    "EN 16575 and the associated terminology standards, which fix what the word "
    "biobased may be taken to mean",
    # -- proving the environmental benefit -------------------------------------
    "ISO 14040, ISO 14044 and ISO 14067, and the product environmental "
    "footprint category rules, which fix system boundaries so that two "
    "producers compute a comparable number",
    "Conventions on the accounting treatment of biogenic carbon and of "
    "end-of-life, which materially change the result and must therefore be "
    "declared",
    # -- procurement and market access -------------------------------------------
    "Public procurement schemes with minimum biobased content requirements, "
    "which have moved more volume in some markets than any environmental "
    "argument",
    "Certification schemes for biobased products and for the mass balance "
    "attribution of certified feedstock through shared infrastructure",
    # -- making the product usable ------------------------------------------------
    "Product specification standards for purity, colour and trace impurities, "
    "which a drop-in molecule must meet exactly, since a customer's process was "
    "tuned to the incumbent's impurity profile rather than to the ideal one",
    "Pharmacopoeial and food-grade specifications where the chemical enters "
    "those supply chains",
    # -- responsible practice ------------------------------------------------------
    "Responsible Care and industry codes on process safety and product "
    "stewardship, which apply to this sector on the same terms as to the "
    "petrochemical one",
)
