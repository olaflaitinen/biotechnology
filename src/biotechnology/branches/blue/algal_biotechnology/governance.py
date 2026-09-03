# =============================================================================
#  biotechnology.branches.blue.algal_biotechnology.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record's governance turns on a fact that surprises people who arrive
#  from the fuel story: ALGAL BIOTECHNOLOGY IS PRINCIPALLY REGULATED AS FOOD.
#
#  Almost every commercially successful application in `practice.py` ends up
#  eaten, by a person or by a farmed animal. Spirulina and chlorella are food.
#  Astaxanthin is a feed additive and a supplement. Omega-3 oils go into infant
#  formula, which is among the most heavily regulated food categories that
#  exists. So the operative instruments here are novel food authorisation, feed
#  additive authorisation and food hygiene law, not environmental or industrial
#  regulation.
#
#  THE PRACTICAL CONSEQUENCE IS A BARRIER TO NEW SPECIES. The handful of algae
#  with a history of consumption can be sold; a newly isolated species with
#  better productivity requires novel food authorisation, with a safety dossier
#  and a multi-year timeline. This is why the same few organisms recur across
#  the industry despite thousands having been screened, and it is a regulatory
#  explanation for what looks like a scientific conservatism.
#
#  A SECOND THREAD THAT MATTERS: WHAT GROWS IN THE POND IS NOT ONLY WHAT WAS
#  PUT THERE. Cyanobacteria produce potent toxins, and an open pond can be
#  colonised by a toxin-producing species. Toxin monitoring is therefore a
#  routine and non-negotiable part of food-grade algal production rather than
#  an exceptional measure, and it is recorded here rather than left implicit.
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
#  MATURITY = COMMERCIAL, and the value has to span two very different
#  histories.
#
#  Spirulina has been produced commercially since 1970 and beta-carotene since
#  1985, which argues for ESTABLISHED. Against that, algal fuel failed twice,
#  most low-value applications remain uneconomic, and the industry as a whole
#  is small and concentrated in a handful of products and species.
#
#  COMMERCIAL is the accurate description: several genuinely profitable
#  products, decades old, in a field that has not become general.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED, which is a step above most cultivation records and is
#  justified by the food route rather than by any hazard of the organisms.
#
#  A national agency decides before a novel algal species may be sold as food,
#  and before an algal feed additive may be marketed. That is approval prior to
#  sale, which is what REGULATED denotes. Genetically modified strains bring
#  contained use requirements on top.
#
#  It is not RESTRICTED, since nothing here is deliberately limited by law.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit is a pond system or a photobioreactor
#  installation. FIELD would suggest agriculture on land, which misdescribes a
#  closed reactor, and the heterotrophic route recorded in `practice.py` runs
#  in conventional fermenters and is unambiguously industrial.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. FOOD is placed first and is the correct primary label for the
#  reason set out above: the successful products are eaten, and food law is
#  what actually governs them. ENERGY is retained because the fuel application
#  is a real part of this record's history and its failure is instructive
#  rather than deletable. ENVIRONMENT covers the wastewater and carbon dioxide
#  coupling, which is where the low-value applications may yet become viable.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.FOOD,
    Domain.ENERGY,
    Domain.ENVIRONMENT,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. Novel foods require authorisation, feed
#  additives require authorisation, and food colourants require listing. These
#  are prior permissions, and obtaining one is the principal barrier to
#  introducing a new species.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by which question each instrument answers. The first
#  group is the one that decides which organisms the industry uses.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- may this species be sold as food at all? ------------------------------
    "Regulation (EU) 2015/2283 on novel foods, under which an algal species "
    "without a significant history of consumption in the Union requires "
    "authorisation with a safety dossier, which is the principal reason the "
    "same few species recur across the industry",
    "Regulation (EC) No 178/2002 general food law and Regulation (EC) No "
    "852/2004 on food hygiene",
    "Regulation (EC) No 1333/2008 on food additives, for algal pigments used as "
    "colourants",
    "Regulation (EU) No 609/2013 on food for specific groups, which governs "
    "algal oils in infant formula and is among the most demanding food regimes "
    "in existence",
    "Regulation (EC) No 1924/2006 on nutrition and health claims, which "
    "constrains what may be said about a supplement regardless of what it "
    "contains",
    # -- may it be fed to animals? -----------------------------------------------
    "Regulation (EC) No 1831/2003 on feed additives, under which the "
    "pigment used in salmon farming is authorised",
    "Regulation (EC) No 767/2009 on the placing on the market of feed",
    # -- what else might be in the pond? -------------------------------------------
    "Regulation (EC) No 1881/2006 setting maximum levels for contaminants, "
    "including the cyanotoxin and heavy metal limits that open-pond production "
    "must demonstrate compliance with batch by batch",
    # -- the water, the land and the discharge --------------------------------------
    "Directive 2000/60/EC, the Water Framework Directive, and national "
    "abstraction and discharge consents, which apply to the large water volumes "
    "this record moves",
    "Directive 2010/75/EU on industrial emissions where an installation passes "
    "threshold capacity",
    "Nutrient discharge and eutrophication rules governing spent medium, since "
    "algal culture medium is by design rich in nitrogen and phosphorus",
    # -- if the strain is modified --------------------------------------------------
    "Directive 2009/41/EC on contained use, and the deliberate release regime "
    "where a modified strain would be grown in an open system, which is a "
    "substantial barrier to applying genome editing outdoors",
    # -- where the strain came from --------------------------------------------------
    "The Convention on Biological Diversity and the Nagoya Protocol, applying "
    "to strains isolated from another country's waters",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is the one that makes food-grade production
#  possible at all.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- demonstrating that what grew is safe to eat ---------------------------
    "Cyanotoxin testing protocols and limits, including microcystin, which are "
    "routine rather than exceptional in open-pond food production because an "
    "open pond can be colonised by a toxin-producing species",
    "Heavy metal and microbiological specifications for algal food and feed "
    "ingredients",
    "Species identity verification of the harvested biomass, since an open "
    "system's contents are not guaranteed by its inoculum",
    # -- running a food plant ----------------------------------------------------
    "HACCP and FSSC 22000 certification for production and processing sites",
    "Good Manufacturing Practice for supplement and ingredient manufacture",
    "Organic certification schemes where the product is sold on that basis, "
    "which impose their own constraints on nutrient sources",
    # -- knowing what you are growing ---------------------------------------------
    "Culture collection deposit and strain authentication, without which a "
    "production strain cannot be shown to be the one that was authorised",
    "Purity and stability monitoring across production cycles",
    # -- substantiating the claims --------------------------------------------------
    "ISO 14040 and ISO 14044 life cycle assessment, required before any carbon "
    "capture or environmental benefit claim, and which must account for harvest "
    "energy, nutrient production and the carbon dioxide that escaped "
    "undissolved",
    "Reporting conventions distinguishing sustained outdoor areal productivity "
    "from short-term laboratory values, which is the specific discipline the "
    "two failed fuel programmes in `history.py` lacked",
    "Water source declaration alongside water use figures, since saline, waste "
    "and fresh water have entirely different significance",
)
