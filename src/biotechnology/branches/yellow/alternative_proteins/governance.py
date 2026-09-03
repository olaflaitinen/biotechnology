# =============================================================================
#  biotechnology.branches.yellow.alternative_proteins.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record contains four sources with four different regulatory positions,
#  which is unusual and is the reason its status value is `VARIES`.
#
#      plant protein   ordinary food. Soy, pea and wheat have been eaten for
#                      millennia and require no authorisation. A burger made
#                      from them is a food product like any other.
#      fungal protein  authorised, and the authorisation is decades old.
#      insect protein  novel food, authorised species by species, each
#                      requiring its own dossier.
#      microbial and   novel food for human consumption, and a feed additive
#      gas protein     question where it goes into feed, which is where nearly
#                      all of it goes.
#
#  So the same shelf holds a product needing no approval beside one that needed
#  a species-specific authorisation, and the difference is again consumption
#  history rather than hazard.
#
#  THE SECOND THREAD IS NAMING, AND IT IS UNUSUALLY CONSEQUENTIAL HERE. Whether
#  a product may be called a burger, a sausage, milk or cheese is decided by
#  law rather than by composition, and the decisions differ between
#  jurisdictions. Dairy terms are restricted in the European Union while meat
#  terms largely are not, which is why plant-based drinks cannot be called milk
#  and plant-based burgers can be called burgers. The argument is about
#  consumer confusion and the evidence that consumers are confused is weak,
#  which this facet records rather than adjudicates.
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
#  MATURITY = ESTABLISHED, and the value deliberately reflects the whole record
#  rather than its most publicised part.
#
#  Tofu and tempeh are ancient. Textured vegetable protein dates from 1960 and
#  mycoprotein from 1985. Insect meal in aquaculture feed is authorised and
#  operating. These are established products by any reading.
#
#  The 2015 wave of extruded analogues is younger and contracted in 2023, and
#  recording the whole record as COMMERCIAL on that basis would let the most
#  covered part define a category that is largely older and steadier than it.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED, which is the honest average across four positions.
#
#  A plant protein product alone would be ROUTINE: registered food business,
#  hygiene rules, nothing more. An insect protein product alone would be
#  REGULATED: species-by-species authorisation before sale.
#
#  CONTROLLED reflects that a food business requires registration or approval
#  and that a substantial part of this record requires authorisation, without
#  claiming that every product in it does.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The characteristic unit is an extrusion line or a
#  fermentation plant. The insect route is closer to FIELD in character and is
#  a minority of the record by volume.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. FOOD is the sector. ENVIRONMENT carries the land and emissions
#  argument, which `metrics.py` records as strong against beef and weak against
#  pulses eaten directly. HEALTH is claimed with reservation and is included
#  because the record's nutritional questions are real in both directions:
#  these products can improve a diet by displacing red meat and can worsen it
#  through sodium and reduced mineral bioavailability, and a domain filter that
#  omitted health would hide both.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.FOOD,
    Domain.ENVIRONMENT,
    Domain.HEALTH,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, and this record is a clean illustration of the
#  value. Plant protein products need no authorisation, insect species each
#  need one, fungal protein has held one for decades, and gas-fermented protein
#  needs one for food and a different one for feed.
#
#  The same shelf holds products at both ends of that range.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by which of the four sources it governs.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- applies to all of it -----------------------------------------------------
    "Regulation (EC) No 178/2002 general food law and Regulation (EC) No "
    "852/2004 on hygiene, under which any of these products is a food business "
    "operation",
    "Regulation (EU) No 1169/2011 on food information, whose allergen "
    "provisions cover soy, wheat and, increasingly, other legumes, and which is "
    "why the choice between soy and pea protein is a labelling decision as much "
    "as a technical one",
    "Regulation (EC) No 1924/2006 on nutrition and health claims, which "
    "constrains what may be said about protein content and about health "
    "benefits",
    # -- what makes a product novel -----------------------------------------------
    "Regulation (EU) 2015/2283 on novel foods, under which insect species are "
    "authorised individually, gas-fermented and microbial proteins require "
    "authorisation, and plant proteins from familiar crops do not",
    "Species-specific insect authorisations, each requiring its own dossier "
    "covering composition, allergenicity and the substrate the insects were "
    "reared on",
    # -- what it may be called ------------------------------------------------------
    "Regulation (EU) No 1308/2013 on the common organisation of agricultural "
    "markets, whose reservation of dairy designations prevents plant-based "
    "drinks being called milk while meat terms remain largely available",
    "National measures restricting meat-related denominations for plant-based "
    "products, which differ between member states and have been repeatedly "
    "litigated",
    # -- feed, where most insect and microbial protein actually goes -----------------
    "Regulation (EC) No 1069/2009 on animal by-products, which governs what "
    "insects may be reared on and is the binding constraint on the waste-stream "
    "argument in this record",
    "Regulation (EC) No 999/2001 and its amendments, which govern processed "
    "animal protein in feed and under which insect meal was authorised for "
    "aquaculture",
    "Regulation (EC) No 1831/2003 on feed additives",
    # -- and where the protein came from ---------------------------------------------
    "Regulation (EU) 2023/1115 on deforestation-free products, which applies to "
    "soy and which bears directly on whether the environmental claim in this "
    "record holds for a given supply chain",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is where this record's claims are actually tested.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- proving the nutritional claim -------------------------------------------
    "FAO methodology for the digestible indispensable amino acid score, which "
    "is how protein quality is assessed properly rather than by protein "
    "content",
    "Bioavailability testing conventions for iron and zinc in plant matrices, "
    "since fortification and absorption are different questions",
    "Nutrient profiling models used by retailers and public bodies, which "
    "increasingly determine shelf placement and promotion regardless of what "
    "the law permits",
    # -- proving the environmental claim -------------------------------------------
    "ISO 14040, ISO 14044 and product environmental footprint category rules "
    "for protein products, with the comparator named, since the result differs "
    "completely between beef, chicken and pulses",
    "Deforestation-free and responsible soy certification schemes, which are "
    "how the supply chain condition on the environmental claim is actually "
    "met",
    # -- describing the product honestly --------------------------------------------
    "Processing classification frameworks including NOVA, which are contested "
    "as a guide to healthfulness and which have become a commercial fact for "
    "this record regardless",
    "Voluntary labelling conventions distinguishing plant-based, vegan and "
    "vegetarian, which are not defined in law in most jurisdictions",
    # -- running the plant ------------------------------------------------------------
    "FSSC 22000, BRCGS and IFS certification for extrusion and fermentation "
    "facilities",
    "Insect rearing hygiene and welfare guidance, the latter unsettled since "
    "insect sentience is genuinely unresolved and the numbers involved are very "
    "large",
    # -- measuring the thing that decides purchase --------------------------------------
    "Sensory evaluation protocols and trained panel methodology, which is the "
    "only rigorous handle on the attributes that determined this record's "
    "commercial history",
)
