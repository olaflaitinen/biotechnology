# =============================================================================
#  biotechnology.branches.green.agricultural_genome_editing.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the reference case for REGULATORY_STATUS = VARIES in this library.
#  The same plant, carrying the same four-base deletion, indistinguishable by
#  any laboratory test from a spontaneous mutant, is:
#
#      a genetically modified organism      in the European Union
#      a conventional variety               in Japan, Argentina, Brazil, the
#                                           United States and England
#      unclassified                         in most of the rest of the world
#
#  Three positions are defensible and are held by serious people.
#
#  PROCESS-BASED, as in the European Union: what matters is how the organism
#  was made, because the technique is the only thing a regulator can verify
#  before the fact and because novelty of method is a reasonable trigger for
#  scrutiny.
#
#  PRODUCT-BASED, as in Canada and Argentina: what matters is what the organism
#  IS, because a plant that could have arisen by conventional means presents
#  conventional risks regardless of how it actually arose.
#
#  NOVELTY-BASED, as in Japan and the 2023 EU proposal: what matters is whether
#  foreign DNA remains, as a workable proxy for the two positions above.
#
#  This facet records all three and adjudicates none of them. That restraint is
#  the point: a taxonomy that picked a side here would be advocacy, and
#  GOVERNANCE.md forbids it.
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
#  MATURITY = COMMERCIAL.
#  Products are on sale: a tomato in Japan, a soybean oil in the United States,
#  mushrooms cleared for market. It is not ESTABLISHED because deployment is
#  confined to a handful of jurisdictions and a handful of products, and the
#  regulatory position in most of the world is unresolved rather than settled.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED, not REGULATED, and this is the deliberate contrast
#  with `green.plant_genetic_engineering`.
#
#  In the jurisdictions where most edited products have reached market, the
#  requirement is notification or a determination of scope rather than a full
#  premarket authorisation. In the European Union it is currently REGULATED,
#  which is precisely the divergence this record documents. CONTROLLED records
#  the modal treatment across jurisdictions; the VARIES status below records
#  that the mode is not universal.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

SCALE = Scale.FIELD

DOMAINS: Tuple[Domain, ...] = (Domain.FOOD, Domain.ENVIRONMENT)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES. See the header note. This is the clearest
#  instance of the value anywhere in the taxonomy.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Grouped by the three regulatory philosophies, so that a reader can see that
#  the disagreement is principled rather than arbitrary.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- process-based: the technique determines the treatment ---------------
    "EU Directive 2001/18/EC on the deliberate release of genetically modified "
    "organisms, written in 2001 and therefore before this technology existed",
    "Court of Justice of the EU Case C-528/16, judgment of 25 July 2018, which "
    "held that organisms obtained by directed mutagenesis fall within the "
    "Directive because the mutagenesis exemption covers only techniques with a "
    "long safety record of use",
    "EU proposal of July 2023 on plants obtained by certain new genomic "
    "techniques, which would create a separate category for edits achievable "
    "by conventional breeding",
    "New Zealand Hazardous Substances and New Organisms Act, applied on a "
    "similarly process-based reading",
    # ---- product-based: what the organism is determines the treatment --------
    "Canadian Plants with Novel Traits regime, which assesses the trait rather "
    "than the technique and so captures some conventionally bred varieties the "
    "EU regime does not",
    "Argentina Resolution 173/2015, the first framework written for these "
    "techniques, asking case by case whether a novel combination of genetic "
    "material is present",
    "Brazil CTNBio Normative Resolution 16/2018, following a comparable "
    "case-by-case approach",
    # ---- novelty-based: presence of foreign DNA as the operative test --------
    "Japan notification pathway under the Cartagena Act, requiring notification "
    "but no premarket approval where no foreign DNA remains",
    "US SECURE rule, 7 CFR Part 340, exempting modifications that could have "
    "been achieved by conventional breeding",
    "England Genetic Technology (Precision Breeding) Act 2023, separating "
    "precision-bred organisms from the retained GMO regime",
    # ---- the layer that applies regardless ------------------------------------
    "Cartagena Protocol on Biosafety, which governs transboundary movement and "
    "under which parties reach different conclusions about whether an edited "
    "organism is a living modified organism at all",
    "EU Regulation (EU) 2016/2031 on plant health, and national variety "
    "registration and seed marketing law, which apply to any new variety "
    "however it was bred",
)


# =============================================================================
#  STANDARDS
#  The detection problem sits at the top, because it is what makes the
#  divergence above so difficult to enforce.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- the detection problem ------------------------------------------------
    "ISO 21569 and ISO 21570 GMO detection methods, which rely on a unique "
    "inserted sequence and therefore cannot identify a type 1 edit that leaves "
    "no such sequence behind",
    "European Network of GMO Laboratories reports on the detectability of "
    "products of new genomic techniques, which conclude that an edit "
    "indistinguishable from a natural mutation cannot be identified as edited "
    "without prior knowledge of the event",
    # ---- assessing the product -------------------------------------------------
    "OECD consensus documents on new plant breeding techniques",
    "OECD consensus documents on the biology of individual crop species, which "
    "define the conventional counterpart every comparative assessment needs",
    "Codex Alimentarius principles for the risk analysis of foods derived from "
    "modern biotechnology",
    "EFSA opinions on the applicability of existing guidance to plants obtained "
    "by targeted mutagenesis and cisgenesis",
    # ---- characterising the edit -------------------------------------------------
    "Whole-genome sequencing based off-target assessment protocols",
    "Amplicon sequencing conventions for reporting editing outcomes",
    # ---- the variety, once it exists ----------------------------------------------
    "UPOV distinctness, uniformity and stability testing, which applies to an "
    "edited variety exactly as to any other",
    "ISTA rules for seed testing",
)
