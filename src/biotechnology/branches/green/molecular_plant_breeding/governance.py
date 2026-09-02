# =============================================================================
#  biotechnology.branches.green.molecular_plant_breeding.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the only record in the green branch with REGULATORY_STATUS =
#  UNREGULATED, and the reason is worth stating precisely because it is the
#  most useful single fact in the record.
#
#  Nothing here creates a novel organism. The alleles being selected already
#  exist in the species and could be combined by any breeder with a paintbrush
#  and enough seasons. Markers change only the speed and accuracy of choosing
#  between plants. No biosafety regime anywhere in the world is triggered by
#  making a decision faster.
#
#  What DOES govern this record is a completely different body of law:
#  intellectual property in varieties, seed marketing and certification, plant
#  health, and access to the genetic resources that breeding starts from. That
#  last one matters more here than in any neighbouring record, because
#  pre-breeding from landraces and crop wild relatives means using material
#  that came from somewhere, and the Nagoya Protocol governs what is owed to
#  wherever that was.
#
#  The other structural fact: the UPOV system was designed for morphologically
#  distinguishable varieties, and molecular markers can now distinguish
#  varieties that are visually identical. Whether a marker difference makes a
#  variety legally distinct is genuinely unsettled, and the essentially derived
#  variety concept exists to stop the answer being exploited.
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
#  Marker-assisted selection has been routine for nearly thirty years and
#  genomic selection is standard commercial practice in the major cereals. The
#  varieties produced this way are the ones most of the world eats.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = ROUTINE.
#  The only record in the green branch at this tier. There is no permit, no
#  committee and no authorisation, because there is no novel organism and no
#  containment question. A genotyping laboratory is an ordinary laboratory.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.ROUTINE

SCALE = Scale.FIELD

# -----------------------------------------------------------------------------
#  DOMAINS
#  FOOD is the purpose. INFORMATION is included deliberately: the deliverable
#  of a modern breeding programme is a prediction model and a curated dataset
#  as much as it is a seed lot, and `practice.CHALLENGES` names data sharing as
#  the largest available improvement to the field.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.FOOD, Domain.INFORMATION)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = UNREGULATED.
#  See the header note. No product-specific approval is required anywhere for a
#  variety produced by marker-assisted or genomic selection, which is the
#  cleanest contrast in the taxonomy with the two records either side of it.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.UNREGULATED


# =============================================================================
#  REGULATIONS
#  None of these govern the technique. They govern the variety, the seed and
#  the germplasm it was built from.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- who owns the variety ------------------------------------------------
    "UPOV Convention 1991 on the protection of new varieties of plants, and the "
    "breeder's exemption permitting a protected variety to be used as a parent",
    "EU Regulation (EC) No 2100/94 on Community plant variety rights",
    "Farmers' privilege provisions on farm-saved seed, which differ sharply "
    "between jurisdictions and are the most contested part of the regime",
    # ---- what may be sold as seed ----------------------------------------------
    "EU marketing directives for cereal, vegetable and fodder seed, and the "
    "national variety catalogues they establish",
    "National variety registration requiring value for cultivation and use "
    "testing in several jurisdictions",
    # ---- keeping pests out ------------------------------------------------------
    "EU Regulation (EU) 2016/2031 on protective measures against plant pests, "
    "which governs movement of breeding material across borders",
    # ---- where the germplasm came from --------------------------------------------
    "Nagoya Protocol on Access and Benefit-sharing, which applies whenever "
    "breeding starts from material collected in another country and is the "
    "reason pre-breeding from landraces carries paperwork",
    "EU Regulation (EU) No 511/2014 implementing Nagoya user compliance",
    "International Treaty on Plant Genetic Resources for Food and Agriculture, "
    "whose multilateral system and standard material transfer agreement is the "
    "route most crop breeding actually uses",
    # ---- the data ---------------------------------------------------------------
    "GDPR, where phenotype and genotype data are linked to identifiable farmers "
    "or growers in participatory breeding programmes",
)


# =============================================================================
#  STANDARDS
#  UPOV DUS testing is listed first because it is where the molecular question
#  in the header note actually bites.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- proving a variety is a variety ---------------------------------------
    "UPOV distinctness, uniformity and stability testing, designed for "
    "morphological characters and now confronted by markers that can "
    "distinguish visually identical varieties",
    "UPOV guidance on essentially derived varieties, which exists to prevent a "
    "cosmetic change being used to escape another breeder's rights",
    "UPOV TGP/15 guidance on the use of biochemical and molecular markers in "
    "DUS examination",
    # ---- proving the seed is what it says --------------------------------------
    "ISTA International Rules for Seed Testing",
    "OECD seed schemes for varietal certification in international trade",
    "Molecular variety identification protocols for purity and identity",
    # ---- describing the material -------------------------------------------------
    "FAO and Bioversity crop descriptor lists, which standardise how a trait is "
    "recorded so that two programmes can pool data",
    "Multi-Crop Passport Descriptors for germplasm accessions",
    "MIAPPE, minimum information about a plant phenotyping experiment, which is "
    "what makes a phenotype dataset reusable rather than merely archived",
    # ---- genebanks ----------------------------------------------------------------
    "FAO Genebank Standards for Plant Genetic Resources for Food and "
    "Agriculture",
)
