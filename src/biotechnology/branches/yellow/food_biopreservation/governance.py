# =============================================================================
#  biotechnology.branches.yellow.food_biopreservation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The governing distinction here is one of the most consequential in food law
#  and it is almost invisible from outside:
#
#      AN ADDITIVE must be declared on the label and must be authorised by
#      name and by food category. Nisin is an additive with an E number.
#
#      A PROCESSING AID acts during production, is not present or has no
#      function in the finished food, and need not be declared.
#
#      A CULTURE added to a food is an ingredient, and is declared as such
#      without requiring additive authorisation.
#
#  The same protective effect can therefore be delivered through three
#  different legal routes with three different labelling consequences, and this
#  drives real technical choices. Producing a bacteriocin in situ with a
#  culture rather than adding a purified preparation is frequently a REGULATORY
#  decision presented as a technical one, and it is the reason
#  `practice.TECHNOLOGIES` lists both.
#
#  BACTERIOPHAGE PREPARATIONS SIT AWKWARDLY IN ALL THREE. They are neither
#  clearly an additive, nor obviously absent from the finished food, nor an
#  ingredient in any ordinary sense, and jurisdictions have classified them
#  differently. That is why this record's status is VARIES rather than
#  AUTHORISED.
#
#  A SECOND POINT: THE CLEAN LABEL PRESSURE THAT DRIVES ADOPTION WORKS AGAINST
#  THE FIELD AS OFTEN AS FOR IT. A manufacturer replacing a chemical
#  preservative to shorten an ingredient list may find the replacement is also
#  a declarable additive.
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
#  MATURITY = ESTABLISHED. Nisin has been an internationally accepted food
#  additive since 1969 and in use for longer, protective cultures have been
#  commercial since 1990, and hurdle technology has been the organising
#  framework of food preservation for nearly fifty years.
#
#  Bacteriophage preparations are newer and are a minority of the record. The
#  category as a whole is settled.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED. An additive requires authorisation by name and by
#  food category before it may be used, which is approval prior to sale and is
#  exactly what the value denotes. Nisin's permitted levels are set in
#  legislation, food category by food category.
#
#  It is not CONTROLLED, which would describe the protective culture half
#  alone, because the additive half of this record requires an authorisation
#  decision rather than a permit.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit is a food manufacturing line, and the agents
#  are applied in processing rather than in a kitchen or a field.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. FOOD is the sector. HEALTH is claimed on a specific and serious
#  ground rather than generally: this record's principal purpose is controlling
#  Listeria monocytogenes in ready-to-eat food, which has a high case fatality
#  rate and which neither cooking nor chilling addresses.
#
#  ENVIRONMENT is claimed on food waste, since a third of food produced is lost
#  and shelf life extension reduces that without asking anyone to change their
#  behaviour.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.FOOD,
    Domain.HEALTH,
    Domain.ENVIRONMENT,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, and the reason is the three-route problem in the
#  header rather than any geographic divergence.
#
#  Nisin is AUTHORISED as an additive with defined limits. A protective culture
#  is an ingredient requiring no additive authorisation. A bacteriophage
#  preparation is classified differently in different jurisdictions and
#  sometimes not clearly at all.
#
#  One protective effect, three legal routes, and the choice between them is a
#  live technical and commercial decision rather than a formality.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by the three routes and then by what must be proved.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the additive route -----------------------------------------------------
    "Regulation (EC) No 1333/2008 on food additives, under which nisin is "
    "authorised as E 234 with maximum levels set food category by food "
    "category, and lysozyme as E 1105",
    "Regulation (EU) No 231/2012 laying down specifications for food "
    "additives, which defines what a nisin preparation must be",
    "Regulation (EU) No 1169/2011 on food information, whose declaration "
    "requirements are what make the additive route commercially unattractive to "
    "a manufacturer pursuing a short ingredient list",
    # -- the culture route --------------------------------------------------------
    "General food law treatment of added cultures as ingredients rather than "
    "additives, which is why in situ bacteriocin production avoids additive "
    "authorisation and why `practice.TECHNOLOGIES` lists it separately",
    "Regulation (EU) 2015/2283 on novel foods, applicable to protective "
    "organisms without a history of use in food",
    # -- the processing aid route, and where phage sits awkwardly -------------------
    "National and regional treatment of bacteriophage preparations, classified "
    "variously as processing aids, additives or outside the framework, which is "
    "the principal reason this record's status is VARIES",
    "United States Generally Recognised As Safe determinations for phage "
    "preparations, which is the route several such products took",
    # -- what must be proved regardless of the route ---------------------------------
    "Regulation (EC) No 2073/2005 on microbiological criteria, whose "
    "ready-to-eat food provisions require that Listeria not exceed defined "
    "limits at the end of shelf life, which is the requirement this record "
    "exists to meet",
    "Regulation (EC) No 852/2004 on hygiene, under which challenge testing and "
    "shelf life validation sit within the hazard analysis",
    # -- and the pressure driving current adoption -------------------------------------
    "Nitrite and nitrate limits in cured meat under the additives regulation, "
    "whose tightening is the clearest current commercial driver of "
    "biopreservation",
    "Directive 2005/29/EC on unfair commercial practices, relevant to natural "
    "and clean label claims made for products that nonetheless contain "
    "declarable additives",
)


# =============================================================================
#  STANDARDS
#  Not law. The first entry is the one that actually decides whether a product
#  may make a safety claim.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- proving the barrier holds ----------------------------------------------
    "Challenge testing protocols for Listeria monocytogenes in ready-to-eat "
    "foods, including inoculation level, storage conditions and reasonable "
    "temperature abuse, which is the only acceptable evidence for a safety "
    "claim and which no combination of laboratory metrics replaces",
    "Shelf life validation and durability study conventions",
    "Predictive microbiology models and their documented limits, since hurdle "
    "interactions are not additive and a model extrapolated beyond its "
    "validation range is a guess",
    # -- specifying the agent ------------------------------------------------------
    "Bacteriocin activity determination in international units against a "
    "reference organism, since preparations differ in purity and a mass figure "
    "is not a specification",
    "Purity and identity specifications for nisin preparations under the "
    "additive specifications regulation",
    "Phage preparation characterisation, including genome sequencing to "
    "demonstrate the absence of lysogeny, toxin and resistance genes, which is "
    "what distinguishes a food-grade phage from an environmental isolate",
    # -- the organisms -------------------------------------------------------------
    "Qualified presumption of safety assessment for protective cultures, and "
    "screening for transferable antimicrobial resistance, which matters "
    "particularly here because the organism is added deliberately and remains "
    "alive in the food",
    "Culture collection deposit and strain authentication",
    # -- watching for the thing the field understated ----------------------------------
    "Resistance monitoring conventions for bacteriocins and phages, which are "
    "less developed than their clinical equivalents and which the 1999 nisin "
    "resistance finding should have prompted sooner",
    # -- and proving nothing else changed -----------------------------------------------
    "Sensory discrimination testing against an untreated control, since the "
    "performance requirement in this record is that the food is unchanged "
    "except in shelf life",
)
