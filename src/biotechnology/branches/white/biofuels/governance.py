# =============================================================================
#  biotechnology.branches.white.biofuels.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record's governance is unlike anything else in the library, and the
#  difference is worth stating plainly before the lists.
#
#  EVERYWHERE ELSE, REGULATION PERMITS OR RESTRICTS. HERE, REGULATION CREATES
#  THE MARKET. A biofuel is chemically a fuel and competes with a cheaper
#  fossil equivalent. What makes it saleable at a viable price is a blending
#  mandate, a renewable target or a tradable certificate, all of which exist
#  only because a legislature created them. Withdraw the policy and most of
#  this industry does not merely shrink, it has no reason to exist.
#
#  THE CONSEQUENCE IS THAT A CALCULATION BECOMES A LEGAL FACT. Whether a
#  consignment counts towards a target depends on its computed carbon
#  intensity, and that computation depends on system boundary, co-product
#  allocation and the land use change model prescribed by the regulator. Two
#  defensible methodologies give different answers for the same physical fuel.
#  Regulators resolve this by mandating one methodology, which converts a
#  contested scientific estimate into an administrative determination.
#
#  A THIRD FEATURE: THE SUPPLY CHAIN IS AUDITED, NOT THE PRODUCT. The molecules
#  in a litre of ethanol carry no evidence of how the crop was grown. So
#  compliance is demonstrated through chain of custody certification and mass
#  balance bookkeeping rather than through analysis of the fuel, which makes
#  this one of the few records where the governance mechanism is auditing
#  rather than testing.
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
#  MATURITY = COMMERCIAL, and the single value conceals a split that this
#  record is careful to make visible elsewhere.
#
#  First generation ethanol and biodiesel are established beyond argument, at
#  enormous scale, for decades. Second generation lignocellulosic fuel was
#  demonstrated commercially and then largely withdrawn. Algal fuel did not
#  arrive. Averaging those into one value is unavoidable given the vocabulary,
#  and COMMERCIAL is the honest average: real production, real revenue, and no
#  settled position for the technologies that were supposed to succeed the
#  first generation.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED. A national or supranational authority determines,
#  before the product may be sold as renewable, whether it qualifies: its
#  feedstock eligibility, its certified chain of custody and its computed
#  carbon intensity are all assessed by an agency or an approved scheme acting
#  under one.
#
#  Note that the tier reflects governance intensity rather than hazard. The
#  physical risks of a fuel plant are the ordinary risks of flammable liquid
#  handling; the governance is heavy because the product's value depends on a
#  regulatory determination.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit is a conversion plant, though this record is
#  unusual in that its decisive constraints, land and feedstock logistics, are
#  agricultural rather than industrial.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. ENERGY is the sector. ENVIRONMENT is claimed because the entire
#  justification and the entire critique are environmental, and because the
#  carbon intensity determination is what makes the product saleable.
#
#  FOOD is claimed deliberately and would be an error to omit. The competition
#  for land, water and fertiliser is not a side effect of this record; it is
#  its defining controversy, and a domain filter that returned biofuels for
#  ENERGY but not for FOOD would hide the thing a reader most needs to see.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENERGY,
    Domain.ENVIRONMENT,
    Domain.FOOD,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. A fuel must meet a specification to be sold
#  at all, and must additionally be certified against sustainability criteria
#  to be sold as renewable. Both are prior permissions rather than subsequent
#  oversight.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law. The first group is the one that creates the market rather than
#  merely constraining it.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the instruments that make the industry exist --------------------------
    "Directive (EU) 2018/2001 on the promotion of energy from renewable "
    "sources, with its transport target, its cap on crop-based fuels, its "
    "sustainability criteria and its treatment of high indirect land use "
    "change risk feedstocks",
    "The United States Renewable Fuel Standard and its volumetric mandates, "
    "including the repeatedly revised cellulosic obligation described in "
    "`history.py`",
    "Low carbon fuel standards that price a fuel by its computed carbon "
    "intensity rather than by its volume",
    "Directive 98/70/EC on fuel quality and its greenhouse gas reduction "
    "obligation on suppliers",
    # -- what may be counted, and from where ------------------------------------
    "Sustainability and greenhouse gas saving criteria, including the "
    "prohibition on feedstock from land with high carbon stock or high "
    "biodiversity value",
    "Rules on wastes and residues, and on the double counting that "
    "distinguishes them from crop feedstocks",
    "Regulation (EU) 2023/2405 and comparable instruments mandating "
    "sustainable aviation fuel uptake",
    # -- the plant as an installation --------------------------------------------
    "Directive 2010/75/EU on industrial emissions, and discharge consents for "
    "stillage and process effluent, which for ethanol production is a large "
    "stream",
    "Directive 2012/18/EU Seveso III and Directive 1999/92/EC, since these "
    "plants hold substantial inventories of flammable liquid",
    # -- the organisms and the enzymes --------------------------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, which applies to the engineered pentose-fermenting strains "
    "this record depends on",
    # -- taxation, which is frequently the real policy instrument -------------------
    "Excise duty differentials and tax exemptions for renewable fuels, which in "
    "several jurisdictions have moved more volume than any mandate",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is unusually consequential here: a certification
#  scheme decides whether a consignment is renewable, which decides its price.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- auditing the supply chain, because the fuel cannot be tested for it ----
    "Voluntary certification schemes recognised for demonstrating compliance "
    "with sustainability criteria, which audit the chain of custody from field "
    "to fuel",
    "Mass balance chain of custody methodology, the bookkeeping convention that "
    "allows certified and uncertified material to share infrastructure without "
    "the claim being lost",
    "Roundtable on Sustainable Biomaterials and comparable scheme criteria "
    "covering land rights, labour and biodiversity alongside carbon",
    # -- how the carbon number is computed ---------------------------------------
    "Prescribed life cycle methodologies and default values, which fix system "
    "boundary and co-product allocation so that two suppliers are computing "
    "the same quantity",
    "ISO 14040, ISO 14044 and ISO 14067 as the underlying assessment "
    "methodology",
    "CORSIA eligibility criteria and default life cycle values for aviation "
    "fuel",
    # -- whether the fuel is fit to burn ------------------------------------------
    "EN 15376 and ASTM D4806 for ethanol as a blending component",
    "EN 14214 and ASTM D6751 for fatty acid methyl ester biodiesel",
    "ASTM D7566 for aviation turbine fuel containing synthesised hydrocarbons, "
    "which is what makes a drop-in fuel usable in an existing aircraft",
    "EN 16723 and comparable specifications for biomethane injected into the "
    "gas grid",
    # -- measuring what it was made from -------------------------------------------
    "Radiocarbon-based biobased content determination, one of the few "
    "properties of the finished fuel that can be verified analytically rather "
    "than by audit",
)
