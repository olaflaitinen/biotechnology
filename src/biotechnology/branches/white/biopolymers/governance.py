# =============================================================================
#  biotechnology.branches.white.biopolymers.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  In this record the STANDARDS matter more than the REGULATIONS, which is
#  unusual and worth explaining before the lists.
#
#  A word like compostable has no meaning in ordinary use. What gives it
#  meaning is a test standard that fixes the temperature, the medium, the
#  duration and the pass threshold. EN 13432 and its equivalents are therefore
#  not background documents here; they are the operative definitions, and a
#  claim made without reference to one of them is not a weaker claim but an
#  empty one.
#
#  THE TWO POINTS A READER SHOULD CARRY AWAY:
#
#  FIRST, THE CERTIFICATION NAMES AN ENVIRONMENT. Industrial composting, home
#  composting, soil and marine biodegradation are four different standards with
#  four different thresholds, and passing one implies nothing about the others.
#  Polylactic acid is certified for the first and fails the rest. Presenting an
#  industrial composting certificate as a general environmental credential is
#  the most common misuse of these documents.
#
#  SECOND, REGULATION HAS DECLINED TO TREAT COMPOSTABLE AS SPECIAL. Single-use
#  plastic restrictions did NOT exempt compostable items, on the reasoning that
#  the collection infrastructure to compost them does not generally exist. The
#  legislature reached the same conclusion this record reaches on technical
#  grounds: the constraint is infrastructure, not chemistry.
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
#  MATURITY = COMMERCIAL. Regenerated cellulose has been made for a century and
#  polylactic acid at commodity scale since 2002, which argues for
#  ESTABLISHED. But polyhydroxyalkanoates remain a niche product for cost
#  reasons, biopolymers are a low single-digit share of total polymer
#  production, and the category has not displaced its incumbent in any major
#  application. COMMERCIAL is the accurate description of a real industry that
#  is not yet a standard one.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED. Contained use permits for the production organisms,
#  registration of the polymer as a substance, and prior authorisation of the
#  monomers and additives used in food contact applications, which is where a
#  large share of this record's volume goes.
#
#  It is not ROUTINE because of that food contact thread: an article intended
#  to hold food must have every constituent on a positive list, and a novel
#  biopolymer therefore faces an approval its fossil competitor completed
#  decades ago.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. MATERIALS is the sector. ENVIRONMENT carries both the justification
#  and the substantiation burden, which in this record are unusually close
#  together.
#
#  FOOD is claimed on two distinct grounds rather than one: the feedstock is
#  frequently a food crop, and the largest single application is food
#  packaging and service ware, which brings its own authorisation regime.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.ENVIRONMENT,
    Domain.FOOD,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. The polymer requires registration as a
#  substance, food contact materials require prior authorisation of every
#  constituent, and a compostability claim requires certification against a
#  named standard before it may lawfully be made. All three are permissions
#  granted in advance.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by what each instrument governs.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- what may be sold as single use, and the decision that surprised people -
    "Directive (EU) 2019/904 on single-use plastics, which restricts certain "
    "items and DOES NOT exempt compostable plastics from those restrictions",
    "Regulation (EU) 2019/1009 on fertilising products, which governs "
    "biodegradable mulch film intended to remain in soil",
    "Packaging and packaging waste rules setting recycled content, "
    "recyclability and compostability requirements by application",
    "Restrictions on oxo-degradable plastics, adopted because fragmentation "
    "produces microplastics rather than mineralisation",
    # -- what may touch food ----------------------------------------------------
    "Regulation (EC) No 1935/2004 and Regulation (EU) No 10/2011 on food "
    "contact materials, under which every monomer and additive must appear on "
    "a positive list, an approval the incumbent polymers completed long ago",
    # -- the substance itself ---------------------------------------------------
    "Regulation (EC) No 1907/2006 REACH and Regulation (EC) No 1272/2008 CLP, "
    "which apply to a biopolymer exactly as to any other polymer",
    "Restrictions on intentionally added microplastics, relevant to fillers, "
    "fragmenting additives and abrasive particles",
    # -- what may be claimed ------------------------------------------------------
    "Directive 2005/29/EC on unfair commercial practices and the subsequent "
    "green claims instruments, under which an uncertified compostable or "
    "biodegradable claim is a regulated act rather than a marketing choice",
    "Labelling requirements distinguishing compostable from recyclable at the "
    "point of disposal, since consumer sorting is where the failure occurs",
    # -- the production organism ---------------------------------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, applicable to engineered polymer-accumulating strains",
    # -- the medical exception ------------------------------------------------------
    "Regulation (EU) 2017/745 on medical devices, under which resorbable "
    "sutures and scaffolds are regulated by their clinical function and their "
    "degradation profile is a design specification rather than an "
    "environmental property",
)


# =============================================================================
#  STANDARDS
#  These are the operative definitions in this record. Note that the first
#  four name four DIFFERENT environments, and passing one implies nothing about
#  the others.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the four environments, which are four separate questions --------------
    "EN 13432 and EN 14995 for industrial compostability, requiring "
    "mineralisation, disintegration, ecotoxicity and heavy metal criteria to be "
    "met together at composting temperature",
    "ASTM D6400 and ASTM D6868, the corresponding North American "
    "specifications",
    "Home composting certification schemes, which test at ambient temperature "
    "over a longer period and which several industrially compostable materials "
    "fail",
    "Soil and marine biodegradation standards, including EN 17033 for "
    "biodegradable mulch film, which are again separate tests with separate "
    "thresholds",
    # -- the underlying measurements -------------------------------------------
    "ISO 14855 and ISO 17556 respirometric methods, which measure evolved "
    "carbon dioxide and are what a mineralisation percentage actually reports",
    "ISO 20200 and equivalent disintegration tests, kept distinct from the "
    "above because passing one is not passing the other",
    # -- proving where the carbon came from --------------------------------------
    "ASTM D6866, EN 16640 and EN 16785 for biobased carbon content, the "
    "independent second axis",
    # -- proving the material works -----------------------------------------------
    "ISO 527 and ISO 178 for mechanical properties, ISO 11357 for thermal "
    "transitions, and ISO 15106 and ISO 15105 for barrier",
    "ISO 1133 melt flow determination, which is what a converter actually asks "
    "for before agreeing to run a new resin",
    # -- proving the environmental claim -------------------------------------------
    "ISO 14040, ISO 14044 and ISO 14067, with declared conventions for biogenic "
    "carbon and end of life, without which two published footprints are not "
    "comparable",
    # -- telling people what to do with it ------------------------------------------
    "Certification marks and on-pack disposal labelling schemes, which are the "
    "only mechanism by which a correct sorting decision reaches the person "
    "actually holding the item",
)
