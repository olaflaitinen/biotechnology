# =============================================================================
#  biotechnology.branches.grey.biowaste_treatment.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS FACET CARRIES MORE OF THE RECORD THAN GOVERNANCE FACETS USUALLY DO,
#  BECAUSE POLICY IS WHAT BUILT THE SECTOR.
#
#  The microbiology was settled by 1930 and explains none of the growth. What
#  explains it is a landfill diversion target, a landfill tax and a renewable
#  tariff. `history.py` sets that out; here it means the regulations below are
#  not a compliance backdrop to the technology, they are its cause.
#
#      A LANDFILL TAX IS THE MOST EFFECTIVE PIECE OF PROCESS ENGINEERING IN
#      THIS RECORD.
#
#  A SECOND FEATURE WORTH NAMING. This record sits at a junction of four
#  regulatory regimes that were written separately and that a single plant must
#  satisfy simultaneously:
#
#      WASTE           what may be accepted, and when the output stops being
#                      waste
#      ANIMAL BY-PRODUCT   pathogen reduction where catering or animal material
#                      is present
#      NUTRIENT AND WATER  where and when digestate may be spread
#      ENERGY          what the gas qualifies as, and what it earns
#
#  The end-of-waste question is the sharpest of these. Digestate is legally
#  waste until a protocol says otherwise, and whether it is a product or a
#  waste changes who may handle it, where it may go and what it is worth, while
#  the material itself is unchanged.
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
#
#  Anaerobic digestion has operated at municipal and farm scale for decades,
#  there are thousands of plants, design codes and standards exist, and rural
#  household digesters have been deployed in very large numbers since the
#  1950s. Composting is older still and is entirely routine.
#
#  The sector's dependence on policy support does not reduce the value.
#  ESTABLISHED describes whether the technology works and is deployed, not
#  whether it would be built without a landfill tax. Many established
#  technologies exist because of a tax.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#
#  A plant needs an environmental permit to accept waste, an approval under
#  animal by-product rules where catering or animal material is involved, and
#  compliance with nutrient regulations at the point of spreading. Gas handling
#  carries explosion protection duties. Each is a prior approval with ongoing
#  conditions.
#
#  Note that the hazards driving this are conventional industrial ones:
#  explosive gas, pathogens, nitrate leaching. The organisms are the same
#  anaerobic community that operates in any sediment, and none of the
#  regulation is about them.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL.
#
#  The unit is a plant with a permitted throughput, a gas engine or upgrading
#  train, storage, and a control system. That is INDUSTRIAL.
#
#  The value is a weighted judgement, since the record also contains windrow
#  composting on open pads and unheated household digesters, which sit
#  elsewhere. The mass of material treated moves through permitted plants, so
#  INDUSTRIAL is the honest choice, and the household deployment is recorded in
#  `practice.py` and `history.py` rather than being allowed to move this value.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. Four, each on a distinct material or energy flow.
#
#  ENVIRONMENT is the diversion itself and the avoided landfill methane, which
#  is the largest term in the record's climate case.
#
#  ENERGY is claimed without qualification. The plant produces methane, and in
#  the upgrading case it produces a grid-quality gas. This is one of the few
#  records in the branch that is a net energy producer rather than a consumer.
#
#  FOOD is claimed for the digestate returning nitrogen and phosphorus to
#  agricultural soil, and for the farm feedstock that comes from and goes back
#  to the same land.
#
#  MATERIALS is claimed narrowly for nutrient recovery as struvite and ammonium
#  salts, where a defined product is separated rather than a bulk amendment
#  spread.
#
#  HEALTH is deliberately NOT claimed. Pathogen reduction is a condition the
#  process must satisfy, not an outcome it delivers, and claiming a health
#  domain for meeting a sanitation requirement would be the sort of padding the
#  vocabulary exists to prevent.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENVIRONMENT,
    Domain.ENERGY,
    Domain.FOOD,
    Domain.MATERIALS,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED.
#
#  A permit is required before waste may be accepted, and separate approval
#  before digestate may be spread. Both are granted in advance and carry
#  conditions.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by the four regimes a single plant must satisfy. The
#  first group is the one that caused the sector to exist.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the policy that created the sector -------------------------------------
    "The Landfill Directive 1999/31/EC and equivalent national regimes, whose "
    "binding targets for diverting biodegradable waste from landfill gave "
    "organic waste a disposal cost and thereby created the economic basis for "
    "this record",
    "Landfill taxes and gate fee structures, which set the avoided disposal "
    "cost that most plants earn more from than they earn from the gas",
    "The Waste Framework Directive 2008/98/EC, including the waste hierarchy "
    "which places prevention above recovery, so a well-run digester does not "
    "justify producing the material",
    "Mandatory separate collection requirements for biowaste, which determine "
    "feedstock quality and therefore plant performance more reliably than any "
    "process variable",
    # -- when the output stops being waste ---------------------------------------
    "End-of-waste criteria and quality protocols for digestate and compost, "
    "which determine whether the output is a product or a waste and thereby "
    "change who may handle it, where it may go and what it is worth, without "
    "the material changing at all",
    "Environmental permitting for waste treatment operations, setting permitted "
    "throughput, accepted waste codes and emission conditions",
    "Fertilising products regulation, including Regulation (EU) 2019/1009, "
    "which sets the route by which digestate may be placed on the market as a "
    "fertilising product across a single market",
    # -- pathogens, where animal material is involved ------------------------------
    "Animal by-products regulation, including Regulation (EC) No 1069/2009, "
    "which imposes pasteurisation time and temperature requirements on catering "
    "waste and animal material before or after digestion",
    "Restrictions on feeding and on land application where treated material may "
    "contact livestock, which are disease control measures rather than "
    "environmental ones",
    # -- where the digestate may go, and when ---------------------------------------
    "The Nitrates Directive 91/676/EEC and national action programmes, which "
    "set closed periods and application limits for nitrogen, and whose closed "
    "periods fall when storage is fullest",
    "Groundwater and surface water protection requirements applying to storage "
    "and spreading, including buffer distances from watercourses",
    "Metal and physical contaminant limits for material applied to agricultural "
    "land, which are what the 2018 protocol tightening addressed",
    "Storage capacity requirements sized to the closed periods above, which are "
    "a substantial part of a plant's capital cost and are frequently "
    "underestimated",
    # -- the gas, as an energy product and as a hazard --------------------------------
    "Renewable energy support schemes and feed-in tariffs, restructured in "
    "several jurisdictions after crop-fed digestion was found to be displacing "
    "food production",
    "Gas quality specifications and grid injection requirements for upgraded "
    "biomethane",
    "Explosion protection and hazardous area requirements, including the ATEX "
    "framework, since digester gas is explosive and gas handling is where the "
    "serious accidents occur",
    "Industrial emissions and air quality requirements covering ammonia and "
    "odour, which are the objections neighbours raise and the reason siting is "
    "contentious",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what separates a real yield from a proposal
#  figure.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- knowing what a feedstock will actually give ---------------------------
    "Biomethane potential assay protocols, including inoculum standardisation "
    "and the reporting conventions that keep the result legible as a ceiling "
    "rather than as a prediction",
    "Volatile solids and moisture determination methods, since yields quoted "
    "per wet tonne are not comparable between feedstocks",
    "Feedstock characterisation and acceptance criteria, which is how a plant "
    "protects itself from a delivery it cannot digest",
    # -- running the vessel without losing it ----------------------------------
    "Volatile fatty acid and alkalinity determination methods, which underpin "
    "the ratio that gives warning before pH moves",
    "Process monitoring and control conventions on gas composition, "
    "temperature and loading rate",
    "Commissioning and inoculation practice, which is the uncontested case of "
    "seeding discussed in `grey.bioaugmentation`, since a new vessel has no "
    "incumbent community",
    "Anaerobic digestion process modelling conventions, which are the shared "
    "description the field designs against",
    # -- the quality of what comes out -----------------------------------------
    "PAS 110 and equivalent digestate quality specifications, and the compost "
    "quality schemes alongside them, which set limits on physical contaminants "
    "and stability",
    "Compost stability and maturity testing, including respiration and "
    "self-heating methods, which distinguish a finished product from one that "
    "will continue reacting in a heap",
    "Nutrient analysis and application planning conventions, which is how a "
    "spreading rate is derived from crop demand rather than from what is in "
    "storage",
    "Sampling protocols for physical contaminants, which is the measurable "
    "consequence of collection policy",
    # -- and proving the climate claim -----------------------------------------
    "Methane leakage measurement and quantification protocols, which are the "
    "difference between a measured climate benefit and an assumed one",
    "Life cycle assessment conventions under ISO 14040 and ISO 14044, applied "
    "with landfill rather than with nothing as the counterfactual",
    "Greenhouse gas accounting practice for waste treatment, including the "
    "global warming potential horizon chosen, which materially changes how "
    "methane leakage is weighed",
    "Gas safety, storage and flare practice, which is where the record's most "
    "serious physical hazards sit",
)
