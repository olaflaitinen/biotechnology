# =============================================================================
#  biotechnology.branches.yellow.cultivated_meat.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record's governance is the most divergent in the library, and the
#  divergence is not about risk assessment.
#
#      approved for sale        Singapore from 2020, the United States from
#                               2023, in both cases for chicken at small volume
#      prohibited outright      Italy from 2023 and several jurisdictions
#                               since, in most cases before any such product
#                               was available there
#      undetermined             the European Union, where no application has
#                               completed the novel food process
#
#  A product lawful in one country, banned in another and unassessed in a third
#  is not unusual in itself. What is unusual is that THE PROHIBITIONS PRECEDED
#  THE PRODUCTS. Bans were enacted where nothing was on sale, on grounds
#  concerning food heritage, cultural identity and agricultural livelihoods
#  rather than safety.
#
#  That is a legitimate thing for a legislature to weigh and it is worth being
#  precise about what it is: a decision that this food should not exist in that
#  market, taken independently of any evidence about the food. No technical
#  progress addresses it, and a record that filed it under regulatory hurdles
#  would misdescribe it.
#
#  A SECOND POINT: THE PRODUCT FALLS BETWEEN FRAMEWORKS. It is produced by a
#  cell culture process resembling pharmaceutical manufacture and sold as a
#  meat product. In the United States that produced a joint arrangement between
#  two agencies. Elsewhere it is handled under novel food rules written for
#  ingredients rather than for a process that manufactures a whole tissue.
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
#  MATURITY = PILOT, and this is the second record in the library to carry it
#  after `white.cell_free_biomanufacturing`. The reasoning must be exact,
#  because both higher and lower values are defensible in the coverage.
#
#  It is not RESEARCH or EMERGING: products have been approved by regulators
#  and sold to the public in two jurisdictions. That is beyond demonstration.
#
#  It is not COMMERCIAL: production is at kilogram rather than tonne scale,
#  availability is limited to a few restaurants, no facility operates at
#  industrial volume, and cost per kilogram is nowhere near the market it
#  addresses. A handful of approved sales at demonstration volume is a pilot.
#
#  PILOT is the honest value and it will change when a facility operates at
#  tonne scale, not when another approval is granted.
# -----------------------------------------------------------------------------
MATURITY = Maturity.PILOT

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED. Every jurisdiction that permits this product requires
#  agency approval before sale, on a full dossier covering the cell line, the
#  medium, the process and the product. Several jurisdictions have gone beyond
#  approval requirements to prohibition.
#
#  RESTRICTED is worth considering given the outright bans, and it is not the
#  right value: the vocabulary defines RESTRICTED as access to materials or
#  methods being deliberately limited by law, which is a technology control.
#  What exists here is a market prohibition on a product, which is a stronger
#  form of regulation rather than a different kind.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = PILOT, matching the maturity value and for the same reason. The
#  characteristic unit today is a demonstration facility producing kilograms.
#  INDUSTRIAL would describe an objective rather than a practice, and would put
#  this record on the same footing as `white.microbial_fermentation`, which
#  operates at hundreds of cubic metres.
# -----------------------------------------------------------------------------
SCALE = Scale.PILOT

# -----------------------------------------------------------------------------
#  DOMAINS. FOOD is the sector. ENVIRONMENT is claimed because the land and
#  emissions argument is the field's principal justification, with the genuine
#  uncertainty `metrics.py` records rather than a claimed benefit. HEALTH is
#  claimed on the antimicrobial and zoonotic argument: a process with no living
#  animal has no enteric pathogen reservoir and needs no antibiotics, which is
#  the same stewardship reasoning `green.veterinary_vaccines` uses.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.FOOD,
    Domain.ENVIRONMENT,
    Domain.HEALTH,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, and no record in the library has a stronger
#  claim to it. The same product is authorised in one jurisdiction, prohibited
#  in another and unassessed in a third, and the prohibitions were enacted
#  before the product was available.
#
#  AUTHORISED would describe Singapore and the United States and would conceal
#  the bans. PROHIBITED would describe Italy and conceal the approvals. VARIES
#  is the only value that reports the situation.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by the three positions described in the header.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- where it is permitted ---------------------------------------------------
    "Singapore Food Agency novel food framework, under which the first "
    "approval anywhere was granted in 2020",
    "United States joint oversight between the Food and Drug Administration "
    "and the Food Safety and Inspection Service, the first agency assessing "
    "cell collection and culture and the second the harvest, processing and "
    "labelling, which is how a product falling between frameworks was actually "
    "handled",
    "Regulation (EU) 2015/2283 on novel foods, which is the route in the "
    "European Union and which no application has yet completed",
    # -- where it is prohibited ----------------------------------------------------
    "National prohibitions on the production and sale of cultivated meat, "
    "enacted in Italy in 2023 and in comparable form in several other "
    "jurisdictions, in most cases before any such product was available for "
    "sale there",
    "Naming and denomination restrictions preventing the use of meat terms for "
    "cultivated products, which in several places accompany or substitute for "
    "prohibition",
    # -- what applies wherever it is made ------------------------------------------
    "Regulation (EC) No 178/2002 and Regulation (EC) No 852/2004 on general "
    "food law and hygiene",
    "Regulation (EC) No 853/2004 on food of animal origin, whose applicability "
    "to a product from cells rather than from a carcass is not straightforward "
    "and is part of why the product falls between frameworks",
    "Regulation (EU) No 1169/2011 on food information, including allergen "
    "declaration and the naming question",
    # -- the inputs, which are where the cost and the scrutiny are ------------------
    "Feed and food ingredient rules applying to growth medium components, since "
    "the medium is an input to a food and its components must be food-grade",
    "Directive 2009/41/EC on contained use, where genetically modified "
    "microorganisms produce the recombinant growth factors the medium requires",
    "Directive 2010/63/EU on animals used for scientific purposes, applicable "
    "to the biopsy from which a cell line is established",
)


# =============================================================================
#  STANDARDS
#  Not law, and this record has fewer than most because the standards do not
#  yet exist. That absence is the finding.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- inherited from pharmaceutical cell culture ------------------------------
    "Cell bank characterisation conventions from pharmaceutical manufacture, "
    "covering identity, purity, stability and freedom from adventitious agents, "
    "which this record inherited wholesale",
    "Good Manufacturing Practice concepts for cell culture, applied at a cost "
    "structure they were never designed for",
    "Adventitious agent and mycoplasma testing, which is routine in "
    "pharmaceutical culture and non-negotiable here",
    # -- what the field has had to invent ----------------------------------------
    "Food-grade specifications for growth medium components, which did not "
    "exist because no previous application needed a cell culture medium at food "
    "purity and food price",
    "Characterisation expectations for immortalised cell lines used in food, "
    "which are still being established and which are the least settled area of "
    "the record's governance",
    # -- describing the product --------------------------------------------------
    "Compositional and nutritional characterisation against the conventional "
    "meat the product represents",
    "Allergen assessment, which for an animal cell product is expected to "
    "mirror the conventional meat, on the same reasoning "
    "`yellow.precision_fermentation` records for identical proteins",
    # -- substantiating the environmental claim ------------------------------------
    "ISO 14040 and ISO 14044 life cycle assessment with the energy source and "
    "the medium input production route declared, since `metrics.py` records "
    "that the result depends chiefly on those two assumptions and published "
    "studies disagree because of them",
    # -- and the standards that do not exist yet ------------------------------------
    "Absence of agreed terminology, so cultivated, cultured, cell-based and "
    "lab-grown are used interchangeably in scientific literature and are "
    "treated as materially different in regulation and marketing",
    "Absence of accepted scale-up and validation conventions for food-scale "
    "animal cell culture, which is unsurprising since no facility has operated "
    "at that scale",
)
