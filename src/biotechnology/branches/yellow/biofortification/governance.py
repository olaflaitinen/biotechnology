# =============================================================================
#  biotechnology.branches.yellow.biofortification.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record contains the sharpest illustration in the library of a fact
#  about agricultural regulation: THE SAME NUTRITIONAL OUTCOME FACES ENTIRELY
#  DIFFERENT REGULATION DEPENDING ON HOW IT WAS ACHIEVED.
#
#      conventional breeding   variety registration, distinctness, uniformity
#                              and stability testing, national listing. No
#                              biosafety assessment, no food safety dossier, no
#                              labelling. Released and eaten.
#      transgenic route        full biosafety assessment, food and feed
#                              approval, cultivation approval, labelling,
#                              coexistence rules, and in several cases
#                              litigation. Twenty-five years and counting.
#      genome editing          treated as conventional breeding in some
#                              jurisdictions and as transgenesis in others,
#                              which is the divergence
#                              `green.agricultural_genome_editing` records.
#
#  A zinc-biofortified wheat and a provitamin A rice address the same category
#  of deficiency in the same populations. One was released; the other has been
#  in process since 1999.
#
#  THIS RECORD DOES NOT ADJUDICATE THAT. Precaution about novel traits in the
#  food supply is defensible, and so is the observation that the process has
#  cost decades against a deficiency that blinds and kills children. Both are
#  recorded, and the reader is left with the comparison rather than a verdict,
#  on the same editorial principle `green.plant_genetic_engineering` follows.
#
#  A SECOND POINT: THE GOVERNING BODIES HERE ARE NOT FOOD REGULATORS. National
#  variety release committees, agricultural research systems and international
#  donors decide what gets bred and released, and none of them is a health
#  authority. That is why nutrition targets had to be imported into breeding
#  programmes deliberately rather than arising from them.
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
#  MATURITY = COMMERCIAL, and the value describes the conventionally bred
#  majority of the record rather than its most discussed part.
#
#  Biofortified varieties have been released across many countries since 2007,
#  have reached tens of millions of farming households, and have demonstrated
#  effects on nutritional status in efficacy trials. That is beyond PILOT.
#
#  It is not ESTABLISHED because coverage remains a fraction of the affected
#  population, the field depends on donor funding rather than on a seed market,
#  and the transgenic route has delivered essentially nothing in twenty-five
#  years.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED, and the value is driven by the route rather than by
#  the trait.
#
#  A conventionally bred variety requires official registration and listing
#  before it may be sold as seed, which is an approval prior to marketing. A
#  transgenic variety requires biosafety, food, feed and cultivation approvals.
#  Either way an authority decides before the seed reaches a farmer.
#
#  The trait itself carries no hazard: more zinc in wheat is not a risk, and
#  the governance weight comes entirely from the method and from the seed system
#  rather than from the nutrient.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION, which is unusual for a crop record and is correct here.
#
#  `green.molecular_plant_breeding` is FIELD, because its unit is a crop in a
#  field. This record's unit is a deficiency prevalence in a population: the
#  breeding target is derived from it, the efficacy trials measure it, and a
#  variety is judged by whether it changes nutritional status across a
#  population rather than by what it yields on a hectare.
#
#  FIELD would describe where the crop grows and miss what the record is for.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. HEALTH is placed first and is the primary label: this is a public
#  health intervention that happens to be delivered by agriculture, its targets
#  are set from deficiency data, and its endpoint is a biomarker of nutritional
#  status. FOOD is the delivery mechanism and the sector the work happens in.
#
#  Two domains is the honest answer. An ENVIRONMENT claim would be unearned,
#  since biofortification changes what is in a crop rather than how it is
#  grown.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.HEALTH,
    Domain.FOOD,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, and the divergence is by METHOD rather than by
#  geography, which distinguishes it from most VARIES values in this library.
#
#  A conventionally bred biofortified variety is registered and sold like any
#  other variety. A transgenic one requires a full authorisation that in the
#  central case of this record has taken twenty-five years and is not complete.
#  A genome-edited one falls either side depending on jurisdiction.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by route, which is what determines everything here.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the conventional route: seed law, and nothing else ---------------------
    "National variety release and registration systems, requiring distinctness, "
    "uniformity and stability testing and value for cultivation and use trials, "
    "which is the only approval a conventionally bred biofortified variety "
    "needs",
    "Seed certification and quality control legislation, which governs whether "
    "the seed a farmer receives is what it claims to be and is frequently the "
    "practical bottleneck in the delivery systems this record depends on",
    "Plant variety protection under UPOV and national equivalents, and the "
    "farmers' rights provisions that determine whether saved seed may be "
    "replanted, which matters for crops distributed to subsistence growers",
    # -- the transgenic route: everything above plus a great deal more -----------
    "The Cartagena Protocol on Biosafety and national biosafety frameworks "
    "implementing it, which govern the transboundary movement and release of "
    "living modified organisms",
    "National biosafety authorisation for cultivation, and separate food and "
    "feed approvals, which in the central case of this record were obtained in "
    "different countries years apart",
    "Regulation (EC) No 1829/2003 and Regulation (EC) No 1830/2003 on "
    "authorisation, traceability and labelling, applicable to import into the "
    "European Union",
    "National judicial review of biosafety permits, which in 2024 revoked a "
    "cultivation approval that had been granted in 2021",
    # -- the editing route, which is unsettled ------------------------------------
    "Divergent national treatment of genome-edited crops, regulated as "
    "conventional breeding in several jurisdictions and as transgenesis in "
    "others, which is the same unresolved divergence "
    "`green.agricultural_genome_editing` records",
    # -- what may be said about the food ------------------------------------------
    "Regulation (EC) No 1924/2006 on nutrition and health claims, and national "
    "equivalents, which govern whether a biofortified crop may be marketed on "
    "its nutritional content",
    "Codex Alimentarius nutrient reference values, which define the "
    "requirements the breeding targets are calculated against",
    # -- where the germplasm came from ----------------------------------------------
    "The International Treaty on Plant Genetic Resources for Food and "
    "Agriculture, whose multilateral system governs access to the genebank "
    "collections that every conventional programme depends on",
    "The Convention on Biological Diversity and the Nagoya Protocol, for "
    "material outside the treaty's multilateral system",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what makes a nutritional claim checkable.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- setting and verifying the target --------------------------------------
    "Breeding target-setting conventions derived from deficiency prevalence, "
    "consumption data, retention and bioavailability, which is the backwards "
    "calculation that distinguishes this field from raising a content figure "
    "for its own sake",
    "Standardised micronutrient analysis protocols, including calibrated X-ray "
    "fluorescence screening against reference wet chemistry, which is what made "
    "screening thousands of breeding lines practical",
    "Retention testing through documented local preparation methods rather "
    "than through a standard laboratory procedure",
    "Bioavailability assessment conventions, from in vitro digestion through to "
    "stable isotope studies in the target population",
    # -- proving it worked --------------------------------------------------------
    "Efficacy and effectiveness trial design standards for nutritional "
    "outcomes, and CONSORT reporting, since the last link in the chain is the "
    "only one that matters and is measured least often",
    "Biomarker measurement and interpretation conventions, including adjustment "
    "for inflammation, which otherwise distorts ferritin and retinol readings "
    "in exactly the populations being studied",
    # -- getting it to farmers ------------------------------------------------------
    "Participatory variety selection protocols, which is how yield parity and "
    "farmer preference are established rather than assumed",
    "Community seed and vine multiplication practice, which is what delivered "
    "orange-fleshed sweet potato and which no formal seed system replaced",
    "Quality declared seed standards, an intermediate between certified seed "
    "and no standard at all, designed for exactly the systems this record "
    "operates in",
    # -- and the collections everything depends on -----------------------------------
    "Genebank management and characterisation standards, since conventional "
    "biofortification requires variation collected and conserved decades ago by "
    "institutions that are now underfunded",
)
