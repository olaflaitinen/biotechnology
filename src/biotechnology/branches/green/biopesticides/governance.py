# =============================================================================
#  biotechnology.branches.green.biopesticides.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is the clearest case in the taxonomy of a regulatory system
#  producing an outcome nobody wanted.
#
#  The modern pesticide regulatory framework was built after Silent Spring, to
#  control persistent synthetic molecules that accumulate in tissue and travel
#  through food chains. Its data requirements follow from that: metabolism
#  studies, residue trials, groundwater modelling, chronic mammalian toxicity.
#
#  Applied to a fungus that dies in sunlight within two days, most of those
#  requirements answer questions that cannot arise. A baculovirus specific to a
#  single moth species faces a dossier priced for a compound that will be
#  sprayed on a hundred million hectares. The result is that the sector is
#  dominated by a handful of organisms registered decades ago, and that many
#  effective agents are never commercialised at all.
#
#  Regulation (EU) 2022/1439 is the first serious correction, replacing the
#  synthetic-molecule data requirements with ones written for micro-organisms.
#  It appears in `history.py` as a milestone for that reason.
#
#  THE BOUNDARY WITH BIOFERTILISERS
#  The same strain is a fertilising product when sold for nutrient supply and a
#  plant protection product the moment a pest-suppression claim is made, at one
#  to two orders of magnitude more dossier cost. The line is drawn by the claim
#  on the label, not by the microbiology. See `green.biofertilisers`.
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
#  MATURITY = COMMERCIAL, and this one is genuinely arguable in both
#  directions.
#
#  Bt has been sold since 1938 and glasshouse biological control is the default
#  system in northern European protected cropping, which argues for
#  ESTABLISHED. But biopesticides remain a small single-digit percentage of the
#  global crop protection market, the trait set is narrow, and adoption in
#  broadacre field crops is limited. COMMERCIAL records the sector rather than
#  its two mature corners.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED, in deliberate contrast with
#  `green.biofertilisers`, which is CONTROLLED.
#
#  The difference is not the organism. It is that a pest-control claim triggers
#  full premarket authorisation by a national agency, with active substance
#  approval at Union level and product authorisation at Member State level.
#  Two organisms with identical biology sit in different tiers because of what
#  their labels say.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

SCALE = Scale.FIELD

# -----------------------------------------------------------------------------
#  DOMAINS
#  FOOD is the purpose. ENVIRONMENT is central rather than incidental: the
#  entire case for the category is what it does NOT kill, and non-target
#  assessment is the largest single part of the dossier.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.FOOD, Domain.ENVIRONMENT)

REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Grouped by what each governs: the substance, the product, how it is used,
#  and the organism itself where that is a separate question.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- approving the active substance --------------------------------------
    "EU Regulation (EC) No 1107/2009 concerning the placing of plant protection "
    "products on the market, under which the active substance is approved at "
    "Union level and the product is authorised by each Member State",
    "EU Regulation (EU) 2022/1439 on data requirements for micro-organisms, "
    "which replaced requirements written for synthetic molecules and is the "
    "most consequential reform to this sector's economics in decades",
    "EU Regulation (EU) 2022/1440 on the assessment and evaluation of "
    "micro-organism dossiers",
    "US EPA biopesticide registration under FIFRA, with a reduced data set and "
    "a separate Biopesticides and Pollution Prevention Division",
    # ---- what may remain on the crop -------------------------------------------
    "EU Regulation (EC) No 396/2005 on maximum residue levels, from which many "
    "microbial actives are exempt, which is the basis of their short "
    "pre-harvest intervals",
    # ---- how it must be used -----------------------------------------------------
    "EU Directive 2009/128/EC on the sustainable use of pesticides, which "
    "obliges Member States to promote integrated pest management and therefore "
    "underpins the threshold-based approach this record depends on",
    "National integrated pest management action plans",
    # ---- moving living organisms across borders ------------------------------------
    "EU Regulation (EU) 2016/2031 on plant health, which governs the "
    "introduction of macrobial agents, since importing a predator is importing "
    "a live organism into an ecosystem",
    "National regulations on the release of non-native biological control "
    "agents, which are stricter than those on microbials for good historical "
    "reasons",
    # ---- where the organism came from, and whether it is modified --------------------
    "Nagoya Protocol on Access and Benefit-sharing, engaged whenever a strain "
    "or a natural enemy is collected in another country",
    "EU Directive 2001/18/EC, applying where an agent is genetically modified, "
    "a route almost nobody has taken commercially",
    # ---- organic production ----------------------------------------------------------
    "EU Regulation (EU) 2018/848 on organic production, under which most of "
    "these products are among the few permitted interventions",
)


# =============================================================================
#  STANDARDS
#  Non-target testing sits at the top, because sparing beneficials is the
#  entire proposition and IOBC classification is what a grower actually
#  consults.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- what it must not harm -----------------------------------------------
    "IOBC guidelines for testing effects on beneficial organisms, whose "
    "four-point classification is what an integrated pest management adviser "
    "consults before recommending a product",
    "OECD Test Guidelines 213 and 214 on honeybee acute toxicity",
    "OECD guidance on the environmental risk assessment of micro-organisms",
    # ---- proving it works ------------------------------------------------------
    "EPPO PP1 series efficacy evaluation standards, including the "
    "micro-organism-specific guidance",
    "EPPO PP1/276 on principles of efficacy evaluation for low-risk products",
    "EPPO standards on resistance risk assessment and management",
    # ---- the agent itself --------------------------------------------------------
    "OECD issue papers on microbial contaminant limits in microbial pest "
    "control products",
    "ISO 17025 accreditation for the laboratories running the bioassays",
    "Strain deposit in a recognised culture collection for identity and "
    "traceability",
    # ---- releasing a live macro-organism --------------------------------------------
    "IPPC ISPM 3, guidelines for the export, shipment, import and release of "
    "biological control agents and other beneficial organisms",
    "IOBC quality control guidelines for mass-reared natural enemies, which set "
    "the fitness and fecundity a shipment must meet",
)
