# =============================================================================
#  biotechnology.branches.yellow.precision_fermentation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This facet exists to make one comparison, and it is the sharpest in the
#  branch.
#
#      yellow.food_fermentation        UNREGULATED
#      yellow.precision_fermentation   AUTHORISED
#
#  Same underlying biology: microorganisms making food. The difference is not
#  hazard, not risk assessment, not evidence. It is CONSUMPTION HISTORY. A food
#  eaten for centuries is exempt from the novel food regime; a molecule
#  identical to one eaten for millennia, made a different way, is not.
#
#  That is defensible. A population's entire diet is not a place for
#  uncontrolled experiment, and requiring evidence before a new thing is eaten
#  widely is a reasonable rule. But the consequence should be stated plainly:
#  the regime measures FAMILIARITY rather than danger, and its practical effect
#  is a barrier to entry that favours companies able to fund parallel dossiers
#  in several jurisdictions.
#
#  A SECOND POINT THAT DECIDES DOSSIERS. The organism is contained, killed and
#  removed, so the product is not a genetically modified food in most
#  jurisdictions and does not carry GMO labelling. It IS produced using a
#  genetically modified microorganism, which some jurisdictions require to be
#  disclosed and others do not, and which some retailers require regardless.
#  That distinction, between a modified organism in the product and one in the
#  process, is the same one `white.industrial_enzymes` turns on.
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
#  MATURITY = COMMERCIAL, and the value has to span an awkward range.
#
#  The technique is ESTABLISHED beyond argument: insulin since 1982, chymosin
#  since 1988, vitamins and amino acids at very large scale for decades. If the
#  record were about the method, ESTABLISHED would be right.
#
#  It is about the application to bulk food proteins, which reached the market
#  from 2020, is sold in a limited set of jurisdictions and applications, and
#  whose cost projections were revised downwards in 2023. COMMERCIAL is the
#  honest value for that.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED. A national or supranational authority decides before
#  the product may be sold, on a full novel food dossier covering
#  characterisation, production process, exposure and allergenicity. That is
#  approval prior to sale, which is what the value denotes.
#
#  The contained use permit for the production organism sits underneath, and
#  would alone place the record at CONTROLLED. The novel food authorisation is
#  what lifts it.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit is a production fermenter and its downstream
#  train, on the terms `white.bioprocess_engineering` sets out.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. FOOD is the sector. HEALTH is claimed on the products with no
#  practical alternative source, specifically vitamin B12 for people eating no
#  animal products and the human milk oligosaccharides authorised for infant
#  formula. ENVIRONMENT carries the land and emissions argument, which
#  `metrics.py` records as real, smaller than claimed, and demonstrable only by
#  life cycle assessment against a named benchmark.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.FOOD,
    Domain.HEALTH,
    Domain.ENVIRONMENT,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. Novel food authorisation is required before
#  sale, food enzyme and additive routes require listing, and infant formula
#  ingredients require their own approval. Every route to market is a prior
#  permission.
#
#  The contrast with `yellow.food_fermentation` at UNREGULATED is the point of
#  this facet and is set out in the header.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law. The first group is what makes this record AUTHORISED.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the instrument that defines this record's position --------------------
    "Regulation (EU) 2015/2283 on novel foods, which requires authorisation "
    "for any food without significant consumption history in the Union and "
    "which applies in full to a molecule identical to one eaten for millennia",
    "EFSA guidance on the information required for a novel food application, "
    "covering identity, production process, compositional analysis, exposure "
    "and allergenicity",
    "United States Generally Recognised As Safe notification, and the "
    "equivalent routes in other jurisdictions, whose divergent timelines are "
    "recorded as a challenge in this record",
    # -- the organism in the process, not in the product -------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, which governs production and not the purified product",
    "Regulation (EC) No 1829/2003 and Regulation (EC) No 1830/2003, whose "
    "labelling obligations attach where modified material is present in the "
    "product rather than only in the process",
    # -- the other routes to market ----------------------------------------------
    "Regulation (EC) No 1332/2008 on food enzymes, the route by which chymosin "
    "and the food enzymes in this record are authorised",
    "Regulation (EC) No 1333/2008 on food additives, relevant to colour and "
    "functional applications",
    "Regulation (EU) No 609/2013 on food for specific groups, under which the "
    "human milk oligosaccharides for infant formula are approved, in one of the "
    "most demanding food categories that exists",
    # -- what must be declared ------------------------------------------------------
    "Regulation (EU) No 1169/2011 on food information, whose allergen "
    "provisions apply unchanged to an identical protein, which is the point "
    "this record insists on",
    "Compositional and naming rules restricting the use of terms such as milk "
    "and cheese, which are decided by law rather than by molecular composition",
    # -- and the ordinary food law underneath ----------------------------------------
    "Regulation (EC) No 178/2002 and Regulation (EC) No 852/2004 on general "
    "food law and hygiene",
    "Regulation (EC) No 1881/2006 on contaminants, applied to the fermentation "
    "product and its feedstock",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is how identity is actually demonstrated.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- proving it is the same molecule ----------------------------------------
    "Analytical characterisation conventions for recombinant proteins, "
    "including mass spectrometric confirmation of sequence and determination "
    "of the glycosylation profile, which is where identity most often diverges",
    "Reference material comparison against the animal-derived protein, which is "
    "the only meaningful basis for a substantial equivalence argument",
    "Host cell protein and DNA residue limits to food-grade specifications, "
    "less stringent than pharmaceutical limits and not absent",
    # -- proving it works as food -------------------------------------------------
    "Functional testing protocols for gelation, foaming, emulsification and "
    "heat stability, benchmarked against the ingredient being replaced rather "
    "than against a specification",
    "Sensory evaluation by trained panel, since a functionally correct "
    "ingredient that tastes wrong is not a product",
    # -- the production organism -------------------------------------------------
    "Qualified presumption of safety assessment and inventories of "
    "microorganisms with a documented history of safe use in food, which "
    "shorten the regulatory path considerably when the host qualifies",
    "Culture collection deposit and strain characterisation, including the "
    "absence of antimicrobial resistance markers and of toxin production",
    # -- running the plant --------------------------------------------------------
    "HACCP, FSSC 22000 and Good Manufacturing Practice for food ingredient "
    "production",
    "Kosher, halal and vegan certification schemes, which for this record are "
    "commercially significant because the animal-free claim is central to the "
    "proposition and the certifications are what make it credible",
    # -- substantiating the environmental claim -------------------------------------
    "ISO 14040 and ISO 14044 life cycle assessment against a named dairy or egg "
    "benchmark, with feedstock cultivation counted, which is what converts the "
    "land and emissions claims in `metrics.py` from assertion into evidence",
    "Conventions on declaring assumed production scale in a life cycle "
    "assessment, since most published figures for this record assume a scale "
    "not yet achieved",
)
