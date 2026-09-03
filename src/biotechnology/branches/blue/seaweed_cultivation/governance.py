# =============================================================================
#  biotechnology.branches.blue.seaweed_cultivation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The governance question that dominates this record is one that scarcely
#  arises anywhere else in the library:
#
#      WHO HAS THE RIGHT TO USE A PIECE OF SEA?
#
#  A terrestrial farm sits on land somebody owns, and the ownership is recorded,
#  transferable and enforceable. A seaweed farm occupies coastal water, which is
#  usually public, and which fishing, navigation, tourism, aquaculture,
#  conservation designation and in many places customary community rights all
#  have claims on. There is frequently no register, no transferable title and
#  no established procedure for deciding between competing uses.
#
#  THIS IS THE PRINCIPAL BARRIER TO EXPANSION IN EUROPE AND NORTH AMERICA, and
#  it is worth stating plainly that it is administrative rather than
#  biological. The farming itself is well understood and needs little capital.
#  What is missing is a licensing framework, and in jurisdictions that have
#  built one the sector has grown.
#
#  A SECOND THREAD: THE CROP IS A FOOD THAT CONCENTRATES ITS ENVIRONMENT.
#  Seaweed takes up whatever the water holds, so maximum levels for heavy
#  metals and arsenic, and iodine limits in several jurisdictions, are binding
#  constraints rather than formalities. Unlike most food safety questions these
#  cannot be managed by better husbandry; they are managed by choosing where
#  the farm is, or not farming there.
#
#  A THIRD, WHICH IS SPECIFIC TO ASIA AND EASY FOR A EUROPEAN ACCOUNT TO MISS:
#  most of the world's production is by smallholders under customary or
#  informal tenure, and formalising marine spatial rights can dispossess the
#  people already farming as easily as it can protect them.
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
#  MATURITY = ESTABLISHED, without qualification, and this is the value most
#  likely to surprise a reader who arrived expecting an emerging technology.
#
#  Nori has been farmed since the seventeenth century and reliably since 1949.
#  Kelp cultivation has been industrial since the 1970s. The sector produces
#  tens of millions of tonnes a year and employs very large numbers of people.
#
#  European and North American cultivation is genuinely emerging, and recording
#  the branch value from that vantage point would describe a small periphery
#  rather than the subject.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED. A licence or concession is required to occupy the
#  water, and a food business authorisation is required to sell the crop. Both
#  are permits rather than product approvals.
#
#  It is not REGULATED, because no agency approves seaweed as a product before
#  sale in the way `blue.algal_biotechnology` requires for a novel species: the
#  established food species have a long consumption history and need no novel
#  food authorisation. A newly introduced species would move this record
#  upwards, which is a useful illustration that the tier describes the activity
#  as practised rather than every possible instance of it.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = FIELD, and this is the only record in the blue branch to carry it.
#
#  The unit of operation is a cultivated area measured in hectares of sea,
#  worked seasonally, with yields quoted per hectare per year. That is farming,
#  and FIELD is the vocabulary's label for it. INDUSTRIAL would describe the
#  hydrocolloid extraction plants downstream, which are real but are not this
#  record's characteristic unit.
#
#  The contrast with `blue.algal_biotechnology` at INDUSTRIAL is deliberate and
#  informative: microalgae are grown in vessels, seaweed is grown in a place.
# -----------------------------------------------------------------------------
SCALE = Scale.FIELD

# -----------------------------------------------------------------------------
#  DOMAINS. FOOD is the primary label, covering both the crop eaten directly
#  and the hydrocolloids that appear throughout the processed food supply.
#  ENVIRONMENT covers the nutrient removal service, which is this record's most
#  defensible environmental claim, and also the habitat and spatial questions
#  that cut the other way. MATERIALS covers the extracted polysaccharides used
#  in formulation, dressings and dental impression materials.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.FOOD,
    Domain.ENVIRONMENT,
    Domain.MATERIALS,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. A farm requires a licence or concession
#  before it may occupy the water, and a food business requires authorisation
#  before it may sell. Both are prior permissions, and obtaining the first is
#  the specific obstacle that has limited expansion outside Asia.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by question. The first group is the one that decides
#  whether a farm can exist at all.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- may a farm occupy this water? -----------------------------------------
    "Directive 2014/89/EU on maritime spatial planning, which requires member "
    "states to plan the allocation of sea space between competing uses and is "
    "the instrument through which cultivation sites are actually made available",
    "National marine licensing and concession regimes for aquaculture "
    "installations, whose absence or slowness is the principal barrier to "
    "expansion outside Asia",
    "Navigation and safety requirements for structures in coastal water, "
    "including marking and reporting",
    "Customary and community tenure arrangements over coastal water, which "
    "govern much of world production and which formal licensing can displace as "
    "easily as it can secure",
    # -- what does the farm do to the place? -------------------------------------
    "Directive 92/43/EEC and Directive 2009/147/EC, under which a farm in or "
    "near a designated site requires appropriate assessment",
    "Directive 2008/56/EC, the Marine Strategy Framework Directive, and "
    "Directive 2000/60/EC, under which nutrient removal is a recognised benefit "
    "and habitat alteration a recognised impact",
    "Environmental impact assessment requirements above threshold farm sizes",
    "Regulation (EU) No 1143/2014 on invasive alien species, relevant where a "
    "cultivated species is grown outside its native range",
    # -- may the crop be sold as food? --------------------------------------------
    "Regulation (EC) No 178/2002 and Regulation (EC) No 852/2004 on food law "
    "and hygiene, under which a farm is a food business",
    "Regulation (EC) No 1881/2006 setting maximum levels for contaminants, "
    "including the cadmium, lead and arsenic limits that decide where a farm "
    "may be sited",
    "National iodine limits and labelling requirements for seaweed foods, which "
    "constrain how much of the product may be eaten",
    "Regulation (EU) 2015/2283 on novel foods, which does not apply to the "
    "established species and does apply to any new one",
    # -- feed, agriculture and additives ---------------------------------------------
    "Regulation (EC) No 1831/2003 on feed additives, relevant to the methane "
    "reduction application",
    "Regulation (EU) 2019/1009 on fertilising products, under which seaweed "
    "biostimulants are placed on the market",
    "Regulation (EC) No 1333/2008 on food additives, under which agar, "
    "carrageenan and alginate are authorised",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is where the sector's biological risk is actually
#  managed, and it is the least developed part of its governance.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- managing the risk that actually destroys crops ------------------------
    "Biosecurity protocols for the movement of seed stock and planting "
    "material between sites and regions, which is how disease and epiphyte "
    "outbreaks travel",
    "Gametophyte banking and culture collection deposit, which preserve genetic "
    "material that decades of vegetative propagation have narrowed and which "
    "are the practical answer to the vulnerability in `history.py`",
    "Health certification and inspection of hatchery-produced seed",
    # -- proving the crop is safe to eat ----------------------------------------
    "Contaminant monitoring programmes covering cadmium, lead, mercury and "
    "arsenic, with arsenic speciation rather than total arsenic, since the "
    "organic forms that dominate in seaweed are far less toxic",
    "Iodine testing and processing methods for reducing it, which are part of "
    "the food chain rather than an optional refinement",
    "HACCP and food business hygiene certification for drying and processing",
    # -- product specifications ---------------------------------------------------
    "Joint FAO/WHO Expert Committee on Food Additives specifications for agar, "
    "carrageenan and alginate, and the corresponding pharmacopoeial monographs",
    "Gel strength, viscosity and sulphate content specifications, which are what "
    "a hydrocolloid buyer actually purchases against",
    # -- certifying the farm ------------------------------------------------------
    "Aquaculture certification schemes covering seaweed, including social "
    "criteria, which matter here because much of world production is by "
    "smallholders with weak bargaining positions",
    "Organic certification for seaweed, which imposes constraints on site and "
    "handling rather than on inputs, since the crop receives none",
    # -- substantiating the claims -------------------------------------------------
    "ISO 14040 and ISO 14044 life cycle assessment, and greenhouse gas "
    "accounting conventions that distinguish carbon fixed from carbon durably "
    "stored, which is the distinction the sequestration claims in "
    "`practice.APPLICATIONS` turn on",
)
