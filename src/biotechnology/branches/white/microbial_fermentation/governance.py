# =============================================================================
#  biotechnology.branches.white.microbial_fermentation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Three governance threads run through this record, and the third explains
#  something the technical facets cannot.
#
#  THE SITE IS REGULATED, NOT ONLY THE PRODUCT. A production fermentation plant
#  is a large industrial installation. It holds pressure vessels, consumes
#  water and energy continuously, discharges a substantial organic effluent in
#  the spent broth, and in the European Union a plant above a threshold
#  capacity requires a permit under the Industrial Emissions Directive with
#  conditions set by reference to best available techniques. This is a genuine
#  regulatory burden that most accounts of biotechnology omit entirely, because
#  it belongs to process industry rather than to biology.
#
#  THE ORGANISM IS REGULATED WHEREVER IT IS MODIFIED. Contained use rules apply
#  identically whether the vessel makes a fuel or a medicine.
#
#  AND BATCH IS A LEGAL CONCEPT, NOT ONLY AN OPERATING CHOICE. This is the
#  point that explains the anomaly recorded in `narrative.py` and `history.py`.
#  A regulated product is released, traced, recalled and rejected by batch. A
#  process that runs continuously for months has no natural batch boundary, so
#  a continuous manufacturer must define one artificially and defend it. That
#  regulatory friction, on top of contamination risk and genetic drift, is a
#  substantial part of why the theoretically superior mode of operation is
#  rarely the one chosen.
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
#  MATURITY = ESTABLISHED, without qualification. Industrial since 1916,
#  recognisably modern since 1943, and the route by which most products in this
#  branch and much of the red branch physically reach the world. Newer feedstock
#  and operating strategies exist within it; the operation itself is settled.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED. Governance intensity rather than danger. A permit is
#  required on two independent grounds: contained use of the organism where it
#  is modified, and an environmental permit for the installation itself above a
#  threshold capacity. Either alone would place this record above ROUTINE.
#
#  It is not REGULATED, because no agency approves a fermentation as such. What
#  is approved is the substance produced, under whichever regime applies to it.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The defining unit is a production vessel of tens to
#  hundreds of cubic metres and the plant around it.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. This record claims three because it genuinely serves three, and
#  that breadth is its defining feature: the same vessel design makes an
#  antibiotic, a feed amino acid and a polymer precursor.
#
#  HEALTH covers antibiotics and recombinant therapeutic proteins. FOOD covers
#  amino acids, vitamins, yeasts and the animal-free proteins. MATERIALS covers
#  the chemicals, acids and polymer feedstocks.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.HEALTH,
    Domain.FOOD,
    Domain.MATERIALS,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, for the same structural reason as
#  `white.metabolic_engineering`: this is an enabling operation rather than a
#  product, and the status of what leaves the vessel depends entirely on what
#  it is. The two records share the value because they share the property, and
#  saying so is more useful than varying the answer for the sake of variety.
#
#  The difference between them is that this record ALSO carries a site-level
#  authorisation that has nothing to do with the product: the environmental
#  permit for the installation.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by what each instrument actually governs. The first
#  group is the one most accounts of biotechnology leave out.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the plant as an industrial installation -------------------------------
    "Directive 2010/75/EU on industrial emissions, under which a fermentation "
    "installation above a threshold capacity requires a permit with conditions "
    "set by reference to best available techniques",
    "Directive 2000/60/EC, the Water Framework Directive, and national "
    "discharge consents governing spent broth and process effluent",
    "Directive 2014/68/EU on pressure equipment, which applies to sterilisable "
    "vessels operated above atmospheric pressure",
    "Directive 1999/92/EC on explosive atmospheres, relevant to solvent "
    "recovery, dust handling and gas fermentation feedstocks",
    # -- the organism -----------------------------------------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, which governs the strain regardless of the product",
    "Directive 2000/54/EC on biological agents at work, including the "
    "classification of the production organism",
    # -- what leaves the vessel, which depends on what it is ----------------------
    "EudraLex Volume 4 Good Manufacturing Practice, Parts I and II, where the "
    "product is a medicine or an active substance",
    "Regulation (EC) No 852/2004 on the hygiene of foodstuffs and Regulation "
    "(EU) 2015/2283 on novel foods, where the product enters the food chain",
    "Regulation (EC) No 1831/2003 on feed additives, which covers the amino "
    "acids and enzymes that constitute much of this record's tonnage",
    "Regulation (EC) No 1907/2006 REACH, where the product is a chemical",
    # -- the people in the plant ---------------------------------------------------
    "Directive 89/391/EEC on safety and health at work, including confined "
    "space entry and the asphyxiation hazard from carbon dioxide accumulation "
    "in and around large fermenters",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what actually determines whether a batch is
#  accepted.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- proving that nothing else grew ----------------------------------------
    "Pharmacopoeial sterility test methods and the sterility assurance level "
    "convention, under which sterility is demonstrated to a probability rather "
    "than asserted absolutely",
    "Bacterial endotoxin testing for products from Gram-negative hosts, a "
    "requirement that follows from the choice of production organism",
    "Culture identity and purity verification at every stage of the seed train",
    # -- keeping the strain the same over decades --------------------------------
    "Master and working cell bank conventions, including characterisation, "
    "storage and the limit on passage number, which is how a strain stays the "
    "same organism across a product's commercial life",
    "Strain deposit in a recognised culture collection under the Budapest "
    "Treaty where patent protection is sought",
    # -- how the plant is designed and run ----------------------------------------
    "American Society of Mechanical Engineers Bioprocessing Equipment "
    "standards for hygienic design, surface finish and drainability",
    "ISO 14159 on hygiene requirements for machinery, and hygienic design "
    "guidance from the European Hygienic Engineering and Design Group",
    "ICH Q7 for active pharmaceutical ingredients and ICH Q8, Q9 and Q10 for "
    "pharmaceutical development, risk management and quality systems",
    "Process analytical technology and continuous manufacturing guidance, "
    "including how a batch may be defined for a process that does not "
    "naturally have one",
    # -- food, feed and environmental claims ---------------------------------------
    "HACCP and FSSC 22000 certification where the product enters food or feed",
    "ISO 14040 and ISO 14044 life cycle assessment, required to substantiate "
    "any claim that a fermentation route is lower impact, since feedstock "
    "cultivation, sterilisation energy, aeration power and spent broth all "
    "count against it",
)
