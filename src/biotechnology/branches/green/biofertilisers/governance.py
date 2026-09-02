# =============================================================================
#  biotechnology.branches.green.biofertilisers.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The governance question here is unusual and worth stating precisely: for
#  most of this field's history the problem was not that regulation was too
#  strict but that there was effectively none.
#
#  A living microbial product sits awkwardly between three regimes. It is not a
#  fertiliser, because it supplies no nutrient itself. It is not a plant
#  protection product, unless it also suppresses a pathogen, at which point it
#  becomes one and the dossier cost multiplies. It is not a feed or a food. For
#  a century that gap meant a bag of peat could be sold as an inoculant with
#  nothing living in it and no authority whose job it was to check.
#
#  EU Regulation (EU) 2019/1009 closed that gap in Europe by creating a defined
#  product function category with composition and labelling requirements. That
#  is why this record is NOTIFIED rather than UNREGULATED, and why the entry
#  appears in `history.py` as a milestone rather than as background.
#
#  THE BOUNDARY THAT CHANGES THE COST
#  A strain sold for nutrient supply is a fertilising product. The same strain
#  sold with a claim that it suppresses a soil pathogen is a plant protection
#  product under Regulation (EC) No 1107/2009, with a dossier one to two orders
#  of magnitude more expensive. Manufacturers therefore word claims carefully,
#  and the boundary with `green.biopesticides` is drawn by the claim rather
#  than by the biology.
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
#  A judgement call, and an arguable one. Legume inoculation alone would be
#  ESTABLISHED without hesitation: it has been sold since 1895 and is routine
#  across soybean production worldwide. But the wider category, meaning
#  phosphate solubilisers, associative fixers and consortium biostimulants, has
#  inconsistent field performance and a quality record that has repeatedly
#  failed independent testing. COMMERCIAL records the category rather than its
#  single mature member.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED.
#  Placing a microbial fertilising product on the market requires conformity
#  assessment and, for most categories, a notified body. It is not REGULATED in
#  the sense used for a medicine or a GMO: there is no premarket authorisation
#  of each product by a national agency, and the control is on composition and
#  labelling rather than on a risk assessment of the organism.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

SCALE = Scale.FIELD

# -----------------------------------------------------------------------------
#  DOMAINS
#  FOOD is the purpose. ENVIRONMENT is not decoration: substituting for
#  synthetic nitrogen is an emissions and eutrophication question before it is
#  an agronomic one, and the strongest argument for the whole category is
#  environmental rather than yield-based.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.FOOD, Domain.ENVIRONMENT)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED in the European Union since 2019, in the
#  sense that a product must meet a defined category specification and carry
#  CE marking before it may be placed on the market. Elsewhere the position
#  ranges from national registration to nothing at all, and the honest summary
#  is that enforcement is the variable rather than the law.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Grouped by what each governs: the product, the claim, the organism, and the
#  soil it goes into.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- the product ---------------------------------------------------------
    "EU Regulation (EU) 2019/1009 laying down rules on the making available on "
    "the market of EU fertilising products, which created product function "
    "category 6, microbial plant biostimulants, and for the first time set "
    "composition and labelling requirements for a living inoculant",
    "EU Regulation (EU) 2019/1009 Annex II, which lists the microbial genera "
    "permitted in that category and thereby determines what may be sold at all",
    "National biofertiliser registration and quality standards, which predate "
    "the EU regime and remain the operative control in most of the world",
    # ---- the claim ------------------------------------------------------------
    "EU Regulation (EC) No 1107/2009 on plant protection products, which "
    "applies the moment a product claims to suppress a pest or pathogen and "
    "raises the dossier cost by one to two orders of magnitude",
    "EU Regulation (EU) 2022/1439 on data requirements for micro-organisms, "
    "which lowered that barrier somewhat for microbial actives",
    # ---- the organism -----------------------------------------------------------
    "EU Directive 2001/18/EC and Regulation (EC) No 1829/2003, which apply "
    "where an inoculant strain is genetically modified, a route almost nobody "
    "has taken commercially precisely because of the cost",
    "EU Directive 2009/41/EC on contained use, applying to the fermentation "
    "stage for a modified strain",
    # ---- where the organism came from ---------------------------------------------
    "Nagoya Protocol on Access and Benefit-sharing, engaged whenever a strain "
    "is isolated from soil collected in another country, which is how almost "
    "every commercial strain originated",
    # ---- the farming system ----------------------------------------------------------
    "EU Regulation (EU) 2018/848 on organic production, under which "
    "biofertilisers are among the few permitted nutrient interventions",
    "EU Directive 91/676/EEC, the Nitrates Directive, which limits nitrogen "
    "application in vulnerable zones and is a substantial part of the economic "
    "case for biological fixation",
)


# =============================================================================
#  STANDARDS
#  Quality specifications first, because a century of failure to meet them is
#  the defining fact of this record's commercial history.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- proving the product is alive ----------------------------------------
    "Bureau of Indian Standards specifications for carrier-based and liquid "
    "inoculants, among the oldest and most detailed national quality standards "
    "for this product class",
    "Brazilian MAPA inoculant standards, which set minimum viable counts and "
    "contamination limits for a market where soybean inoculation is universal",
    "ISO 27205 and related methods for enumeration of viable microorganisms in "
    "inoculant products",
    "Accelerated shelf-life testing protocols, which are what connect a "
    "manufacture-date count to a point-of-sale count",
    # ---- proving it does something ---------------------------------------------
    "EPPO efficacy evaluation standards, applied where a biostimulant claim is "
    "made",
    "FAO guidelines on the use of biofertilisers",
    "Isotope-based protocols for quantifying biological nitrogen fixation, from "
    "the IAEA and FAO joint programme",
    # ---- characterising strain and soil ------------------------------------------
    "ISO 11063 soil quality, DNA extraction from soil for community analysis",
    "ISO 10381 soil sampling standards",
    "World Data Centre for Microorganisms deposit requirements for strain "
    "identity and traceability",
)
