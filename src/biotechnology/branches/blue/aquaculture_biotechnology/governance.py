# =============================================================================
#  biotechnology.branches.blue.aquaculture_biotechnology.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Four separate legal systems meet on a single fish farm, which is more than
#  any other record in this library has to reconcile.
#
#      ANIMAL WELFARE LAW     applies to a sentient animal, and applies badly.
#                             Most welfare legislation was written for
#                             terrestrial livestock, and provisions on
#                             transport, handling and slaughter frequently do
#                             not fit a fish or do not mention one. The
#                             evidence on fish sentience has strengthened
#                             considerably and the law has not kept pace.
#      MEDICINES LAW          governs vaccines and treatments, including the
#                             withdrawal period before a treated animal may be
#                             eaten.
#      FOOD LAW               governs the product, its contaminants and its
#                             labelling.
#      ENVIRONMENTAL LAW      governs the site, the discharge, the escapes and
#                             the effect on wild populations, and this is where
#                             the contested decisions are actually made.
#
#  THE FIFTH THREAD IS THE ONE THAT DECIDES WHAT GETS DEPLOYED. Genome editing
#  for disease resistance has been demonstrated in farmed species and is held
#  up by regulatory classification rather than by any technical difficulty. The
#  genetically modified salmon approved in 2015 took roughly two decades of
#  review for work completed in the early 1990s. Whatever one concludes about
#  those products, the timeline is a statement about the system.
#
#  A SIXTH POINT WORTH RECORDING: SOME OF THE MOST EFFECTIVE CONTROL IS NOT
#  LAW AT ALL. Sea lice thresholds, area management agreements, synchronised
#  fallowing and certification schemes do more to govern day-to-day practice
#  than statute does, because the problems are regional and no single operator
#  can solve them alone.
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
#  MATURITY = ESTABLISHED. Aquaculture supplies about half the fish eaten
#  worldwide and overtook capture fisheries in 2014. Breeding programmes have
#  run since 1971, vaccination since the late 1980s, and genomic selection is
#  standard.
#
#  Individual technologies within the record are far less settled, particularly
#  genome editing and land-based recirculating production, and those are
#  recorded as such in `history.py` rather than by lowering the branch value.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED. A national agency decides before a farm may operate,
#  before a veterinary medicine may be used, and before a novel or modified
#  animal may enter the food chain. Site consent, welfare inspection, disease
#  notification and discharge authorisation are all agency decisions taken in
#  advance.
#
#  It is not RESTRICTED, since nothing here is deliberately limited in the way
#  that value denotes, though the genome editing position comes closer to it in
#  practice than the tier suggests.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION, and the choice needs explaining because FIELD would look
#  natural for a farm.
#
#  The decisions that matter in this record are taken at the level of a water
#  body rather than a site. Sea lice thresholds exist to protect wild salmon
#  migrating past a farm. Fallowing and biosecurity zoning are synchronised
#  across every farm in an area because a parasite does not respect a licence
#  boundary. Escape is consequential because of what it does to a wild
#  population's genetics.
#
#  The unit of both the risk and its management is a population, farmed and
#  wild together, which is precisely what this value denotes.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. FOOD is the sector. ENVIRONMENT is claimed because the escape,
#  effluent, parasite and habitat questions are environmental ones and are
#  where the sector's licence to operate is actually contested. HEALTH is
#  claimed on the antimicrobial stewardship argument, which is a human health
#  benefit delivered through animals, on the same reasoning
#  `green.veterinary_vaccines` uses.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.FOOD,
    Domain.ENVIRONMENT,
    Domain.HEALTH,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. A farm operates under a licence, veterinary
#  medicines are authorised products, and a modified animal requires approval
#  before it may be sold as food. All are prior permissions.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by the four systems described above.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the animal as a sentient creature -------------------------------------
    "Council Directive 98/58/EC on the protection of animals kept for farming "
    "purposes, which applies to farmed fish and was written with terrestrial "
    "livestock in view",
    "Council Regulation (EC) No 1099/2009 on the protection of animals at the "
    "time of killing, whose species-specific provisions largely do not address "
    "fish",
    "Directive 2010/63/EU on animals used for scientific purposes, which covers "
    "the research underlying this record",
    # -- the animal as a patient -------------------------------------------------
    "Regulation (EU) 2019/6 on veterinary medicinal products, and Regulation "
    "(EC) No 470/2009 with the maximum residue limits and withdrawal periods "
    "that follow from it",
    "Regulation (EU) 2016/429, the Animal Health Law, and Directive "
    "2006/88/EC before it, governing listed aquatic diseases, notification and "
    "movement controls",
    # -- the animal as food -------------------------------------------------------
    "Regulation (EC) No 853/2004 laying down specific hygiene rules for food of "
    "animal origin",
    "Regulation (EC) No 1881/2006 on contaminant levels, and Regulation (EU) No "
    "1379/2013 on consumer information, under which farmed and wild product "
    "must be distinguished",
    "Regulation (EC) No 1829/2003 and Regulation (EC) No 1830/2003, under which "
    "a genetically modified animal requires authorisation and labelling",
    # -- the farm as a place in the environment -------------------------------------
    "Directive 2000/60/EC and Directive 2008/56/EC on water and marine "
    "environmental status, which constrain discharge and stocking in a water "
    "body",
    "Directive 2014/89/EU on maritime spatial planning, and national "
    "aquaculture licensing regimes",
    "Directive 92/43/EEC and Directive 2009/147/EC, requiring appropriate "
    "assessment where a farm affects a designated site",
    "Regulation (EU) No 1143/2014 on invasive alien species, and national "
    "requirements on escape reporting and containment",
    "Regulation (EC) No 1069/2009 on animal by-products, governing mortalities "
    "and processing waste",
)


# =============================================================================
#  STANDARDS
#  Not law, and in this record several of them govern practice more effectively
#  than statute does, because the problems are regional.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the regional coordination that statute does not achieve ---------------
    "Area management agreements and coordinated fallowing across all farms in a "
    "water body, which is how sea lice and disease are actually controlled, "
    "since a parasite does not respect a licence boundary",
    "Sea lice threshold and reporting schemes, which function as binding "
    "operating limits whether or not they sit in legislation",
    "Biosecurity protocols for movement of stock, equipment and personnel "
    "between sites",
    # -- animal health and disease reporting -------------------------------------
    "World Organisation for Animal Health Aquatic Animal Health Code and the "
    "corresponding diagnostic manual, which define listed diseases and the "
    "conditions for trade",
    "Vaccine potency and safety requirements under the European Pharmacopoeia "
    "for veterinary immunologicals",
    # -- welfare, where the standards run ahead of the law ------------------------
    "Species-specific welfare guidance covering stocking density, handling, "
    "delousing procedure and stunning before slaughter, which is more detailed "
    "and more current than the legislation it supplements",
    "Operational welfare indicator frameworks, which give measurable proxies "
    "for a question that stocking density alone answers poorly",
    # -- certification, which is what the market actually enforces -----------------
    "Aquaculture certification schemes covering feed sourcing, escape "
    "prevention, antibiotic use, welfare and social criteria",
    "Marine ingredient certification for feed, which is how the fish-in "
    "fish-out question is addressed commercially rather than legally",
    "Chain of custody certification distinguishing farmed from wild product",
    # -- breeding and genetics ------------------------------------------------------
    "Breeding programme conventions on pedigree recording and on maintaining "
    "effective population size, which matter because these populations were "
    "founded from small numbers of wild individuals",
    "Genetic assignment methods for tracing escapees to a farm of origin, which "
    "is what makes escape provisions enforceable",
)
