# =============================================================================
#  biotechnology.branches.yellow.food_fermentation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record's governance is unusual in a way that is easy to miss: it is
#  regulated almost entirely by PROCESS CONTROL rather than by product
#  approval, and the reason is history.
#
#  Traditional fermented foods have a long history of safe consumption, so they
#  are not novel foods and require no authorisation. A cheese, a soy sauce or a
#  kimchi may be made and sold without anyone approving it. What the law
#  requires instead is that the producer identify the hazards, establish the
#  critical points where they are controlled, monitor those points and keep the
#  records. In this record the critical control point is usually a pH value and
#  the time taken to reach it, which is why `metrics.py` treats acidification
#  as a safety barrier rather than a process parameter.
#
#  THE CONSEQUENCE IS A SHARP AND SOMETIMES ODD BOUNDARY. The same organism in
#  the same food is unregulated when it has been used for centuries and
#  requires novel food authorisation when it has not. A traditional fermented
#  product from one region may be freely sold there and be a novel food in
#  another, which is a statement about consumption history rather than about
#  safety.
#
#  A THIRD THREAD BELONGS HERE AND NOWHERE ELSE IN THE LIBRARY: GEOGRAPHICAL
#  INDICATION LAW. Names such as those protecting particular cheeses and cured
#  meats restrict who may use them, and they increasingly collide with
#  standardised commercial cultures, since a rule protecting a place cannot
#  easily say whether the organisms are part of what it protects.
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
#  MATURITY = ESTABLISHED, and no record in this library has a stronger claim
#  to the value. The practice is roughly nine thousand years old, the industry
#  is enormous, and the science has been settled for over a century.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED, and the choice is worth explaining because both
#  neighbouring values are arguable.
#
#  It is not ROUTINE: a food business requires registration or approval, and an
#  establishment handling products of animal origin requires approval with an
#  identification mark before it may sell. Fermented meat and raw milk products
#  carry tighter controls than their apparent simplicity suggests, because the
#  safety barrier is a pH curve rather than a kill step.
#
#  It is not REGULATED: no agency approves a traditional fermented food before
#  sale. The obligation is to control the process and keep the records, which
#  is a permit-and-verify regime rather than an approval one.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The characteristic unit is a production plant, from a
#  dairy to a brewery. The record covers practices that also occur in a kitchen,
#  and a vocabulary that recorded that would describe the craft rather than the
#  industry this branch is about.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. FOOD is the sector without argument. HEALTH is claimed on two
#  specific and documented mechanisms rather than on general wholesomeness: the
#  detoxification of cassava, which makes a staple safe for hundreds of
#  millions of people, and the phytate reduction that improves iron and zinc
#  absorption from cereals and legumes.
#
#  INDUSTRY is not available in the vocabulary; MATERIALS would be wrong, since
#  nothing here is a material. Two domains is the honest answer.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.FOOD,
    Domain.HEALTH,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = UNREGULATED, and this is the only record in the library
#  so far to carry it, so the reasoning must be exact.
#
#  It does NOT mean the activity is unsupervised. Food hygiene law applies in
#  full, establishments are registered or approved, and hazard analysis is
#  mandatory. What it means is that THE PRODUCT ITSELF REQUIRES NO PRIOR
#  AUTHORISATION. A traditional fermented food may be made and sold without any
#  agency approving it, because its consumption history exempts it from the
#  novel food regime.
#
#  The contrast with `yellow.precision_fermentation`, which is AUTHORISED for
#  the same underlying biology, is the sharpest illustration in this branch of
#  how much of food regulation turns on familiarity rather than on hazard.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.UNREGULATED


# =============================================================================
#  REGULATIONS
#  Binding law. Note that none of the first group approves a product; they all
#  require the producer to control a process.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- control the process, keep the records ---------------------------------
    "Regulation (EC) No 178/2002 general food law, establishing traceability "
    "and the obligation to withdraw unsafe food",
    "Regulation (EC) No 852/2004 on the hygiene of foodstuffs, which requires "
    "hazard analysis and critical control points, and under which the "
    "acidification curve in `metrics.py` is typically the critical control "
    "point itself",
    "Regulation (EC) No 853/2004 laying down specific hygiene rules for food of "
    "animal origin, under which dairy and meat establishments require approval "
    "and an identification mark",
    "Regulation (EC) No 2073/2005 on microbiological criteria, which sets the "
    "pathogen and indicator limits a fermented product must meet",
    # -- what may be in it -------------------------------------------------------
    "Regulation (EC) No 1333/2008 on food additives, relevant to nitrite in "
    "cured fermented meats, where the additive is part of the safety barrier "
    "rather than a cosmetic ingredient",
    "Regulation (EC) No 1881/2006 on contaminants, covering the mycotoxins and "
    "biogenic amines that a poorly controlled fermentation can generate",
    "Regulation (EU) No 1169/2011 on food information, whose allergen "
    "provisions cover milk, soy, cereals and fish across this record",
    # -- when a fermented food is NOT exempt ---------------------------------------
    "Regulation (EU) 2015/2283 on novel foods, which does not apply to foods "
    "with a significant history of consumption in the Union and does apply to a "
    "traditional product from elsewhere, which is a distinction about "
    "familiarity rather than about safety",
    "Regulation (EC) No 1829/2003, where a genetically modified organism is "
    "used in production, as with fermentation-produced chymosin",
    # -- who may call it what -------------------------------------------------------
    "Regulation (EU) No 1151/2012 on quality schemes, establishing protected "
    "designation of origin and protected geographical indication, which "
    "restrict traditional names and increasingly collide with standardised "
    "commercial cultures",
    # -- alcohol, which is its own body of law ---------------------------------------
    "Excise, labelling and compositional rules for beer, wine and spirits, "
    "which are extensive, national and largely outside the scope of food law "
    "proper",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what a producer actually works to.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- running the process safely ---------------------------------------------
    "Codex Alimentarius general principles of food hygiene and the HACCP "
    "system, which is the framework the hygiene regulation implements",
    "Codex standards for fermented milks, cheese and named fermented products, "
    "which define composition and permitted processes",
    "FSSC 22000, BRCGS and IFS certification schemes, which are what a retailer "
    "requires regardless of what the law requires",
    # -- knowing the organisms are what they are ---------------------------------
    "Qualified presumption of safety assessment for microorganisms used in food "
    "production, which is how a starter organism is judged acceptable without a "
    "product authorisation",
    "Culture collection deposit and strain identification to species level, "
    "since a starter is sold as a defined organism and must be one",
    "Inventories of microbial species with a documented history of safe use in "
    "food, which function as the practical reference for what may be used",
    # -- measuring the barrier ----------------------------------------------------
    "Standard methods for pH, water activity and titratable acidity, which are "
    "the measurements the critical control points are expressed in",
    "Challenge testing and predictive microbiology protocols, which is how a "
    "producer demonstrates that a hurdle combination actually controls a "
    "pathogen rather than assuming it",
    # -- describing what is there --------------------------------------------------
    "Reporting conventions for microbial community composition in fermented "
    "foods, which are still developing and which matter because most "
    "traditional products were characterised only recently",
    # -- and the questions the standards do not answer -------------------------------
    "Authenticity and traditional speciality conventions, which attempt to say "
    "what makes a named food that food, and which have no settled position on "
    "whether the organisms are part of the answer",
)
