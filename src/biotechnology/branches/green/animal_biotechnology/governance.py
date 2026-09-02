# =============================================================================
#  biotechnology.branches.green.animal_biotechnology.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Three governance threads run through this record, and only one of them
#  exists anywhere else in the green branch.
#
#  ANIMAL WELFARE LAW applies throughout, to every layer, whether or not any
#  genetic technology is involved. Superovulation, embryo transfer and surgical
#  procedures are regulated as procedures on sentient animals. This is the only
#  record in the branch where the subject of the technology can suffer, and the
#  legal framework reflects that from the first layer onward.
#
#  ANIMAL BREEDING LAW governs the second layer, and is unusual: Regulation
#  (EU) 2016/1012 regulates breed societies, herd books and the publication of
#  breeding values rather than any product. There is no authorisation to obtain
#  and no dossier to file, because a genomic breeding value is a statistical
#  estimate rather than a thing placed on the market.
#
#  MEDICINES LAW governs the third layer. In the United States an intentional
#  genomic alteration in an animal is regulated as a new animal drug, which
#  sounds odd and follows from statute: the alteration is treated as an article
#  intended to affect the structure or function of the body. That framing
#  determines the evidence required and much of the nine-year timeline recorded
#  in `history.py`.
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
#  MATURITY = COMMERCIAL, and the three layers pull in different directions.
#  Artificial insemination is ESTABLISHED beyond argument, and genomic
#  selection has been standard dairy practice since 2009. Editing has produced
#  a handful of approvals in a handful of countries. COMMERCIAL is the honest
#  aggregate: the record as a whole is deployed and sold, and its newest layer
#  is not routine anywhere.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#  Driven by the third layer and by welfare law rather than by the first two.
#  A genomic breeding value needs no authorisation; an edited animal needs a
#  marketing decision from a national agency, and any procedure on a live
#  animal needs authorisation under welfare legislation.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

SCALE = Scale.FIELD

# -----------------------------------------------------------------------------
#  DOMAINS
#  FOOD is the purpose. HEALTH is included on two distinct grounds: disease
#  resistance removes a reason to use antibiotics, which is an antimicrobial
#  resistance argument, and transgenic bioreactor animals produce human
#  therapeutics. Both are substantive rather than incidental.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.FOOD, Domain.HEALTH)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES.
#  The first two layers are unregulated as products almost everywhere. The
#  third ranges from approved for sale in the United States, through pending in
#  several jurisdictions, to effectively prohibited in the European Union,
#  where an edited animal falls under GMO law. Same animal, different answers,
#  exactly as in `green.agricultural_genome_editing`.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Grouped by the three threads in the header note, plus the trade layer.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- welfare, which applies to every layer -------------------------------
    "EU Directive 98/58/EC concerning the protection of animals kept for "
    "farming purposes",
    "EU Directive 2010/63/EU on the protection of animals used for scientific "
    "purposes, which governs the research stage of every technique here",
    "EU Regulation (EC) No 1099/2009 on the protection of animals at the time "
    "of killing",
    "EU Regulation (EU) 2016/429, the Animal Health Law",
    "National provisions on disbudding, castration and other routine "
    "procedures, which are the specific practices some edits in this record are "
    "designed to make unnecessary",
    # ---- breeding, which regulates the institutions not the product ----------
    "EU Regulation (EU) 2016/1012 on zootechnical and genealogical conditions "
    "for breeding, trade and entry of purebred breeding animals, which "
    "regulates breed societies, herd books and the publication of breeding "
    "values rather than any authorised product",
    "National herd book and breeding programme approvals",
    # ---- the third layer --------------------------------------------------------
    "US FDA guidance on intentional genomic alterations in animals, under which "
    "the alteration is regulated as a new animal drug",
    "EU Directive 2001/18/EC and Regulation (EC) No 1829/2003, under which an "
    "edited animal is a genetically modified organism and its products require "
    "authorisation",
    "Cartagena Protocol on Biosafety, governing transboundary movement of "
    "living modified animals",
    "National cloning provisions, several of which restrict food from clones or "
    "require labelling",
    # ---- moving animals and germplasm -------------------------------------------------
    "WOAH Terrestrial Animal Health Code, including the chapters on collection "
    "and processing of semen and embryos",
    "EU Regulation (EU) 2020/692 on entry into the Union of animals and "
    "germinal products",
    "Nagoya Protocol and the FAO Global Plan of Action for Animal Genetic "
    "Resources, where breeds and germplasm cross borders",
)


# =============================================================================
#  STANDARDS
#  ICAR and Interbull are listed first, because they are what actually makes a
#  breeding value in one country comparable with one in another.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- making the numbers comparable ---------------------------------------
    "ICAR guidelines for performance recording, which define how milk yield, "
    "weight and health events must be recorded to be usable in an evaluation",
    "Interbull international genetic evaluation standards, which convert "
    "national breeding values onto a common scale and are the reason a bull "
    "ranked in one country can be bought in another",
    "ISO 24631 series on radio frequency identification of animals, which is "
    "how an animal is tied to its own record",
    # ---- handling germplasm ----------------------------------------------------
    "International Embryo Technology Society manual for sanitary handling and "
    "processing of embryos",
    "Certified Semen Services standards for bull stud health and semen quality",
    # ---- welfare assessment ------------------------------------------------------
    "Welfare Quality assessment protocols for cattle, pigs and poultry",
    "AWIN welfare assessment protocols",
    # ---- conserving diversity -------------------------------------------------------
    "FAO Guidelines on cryoconservation of animal genetic resources",
    "FAO Domestic Animal Diversity Information System reporting, which is how "
    "the effective population size figures in `metrics.py` are tracked",
    # ---- characterising an edited animal ------------------------------------------
    "Whole-genome sequencing based characterisation of edited founders, "
    "expected rather than encouraged since the 2019 episode recorded in "
    "`history.py`",
)
