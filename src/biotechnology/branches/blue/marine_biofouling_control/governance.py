# =============================================================================
#  biotechnology.branches.blue.marine_biofouling_control.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is governed by an unusual combination: a dedicated international
#  convention prohibiting a specific technology, plus ordinary biocide
#  authorisation, plus a body of guidance that is not law and shapes practice
#  more than either.
#
#  THE CONVENTION IS THE UNUSUAL PART. There are very few instruments in this
#  library whose purpose is to prohibit a named technology globally. The
#  International Convention on the Control of Harmful Anti-fouling Systems on
#  Ships exists because tributyltin was a problem that no single state could
#  address: a ship coated in one jurisdiction pollutes another's harbours, so a
#  national ban moves the problem rather than solving it. Global shipping
#  required a global instrument.
#
#  THE ORDINARY PART IS THAT AN ANTIFOULING BIOCIDE IS A BIOCIDE. Copper and
#  the booster biocides go through the same authorisation as any other biocidal
#  product, with efficacy data, environmental fate modelling and a risk
#  assessment comparing predicted environmental concentration against predicted
#  no effect concentration. That comparison is the pair of metrics this record
#  places at its centre.
#
#  THE PART THAT IS NOT LAW AND MATTERS MOST FOR THE SECOND OBJECTIVE:
#  biofouling management for invasive species control is largely guidance
#  rather than binding requirement in most jurisdictions, and it addresses a
#  different problem from fuel efficiency. A record that treated them as one
#  would misdescribe both the technology and its regulation.
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
#  MATURITY = ESTABLISHED. Antifouling coatings are applied to essentially
#  every commercial vessel afloat, the industry is old and large, and copper
#  sheathing dates from 1761.
#
#  The biological approaches within the record, meaning quorum sensing
#  inhibition, enzymatic coatings and natural product antifoulants, are
#  genuinely emerging and are recorded as such in `practice.py` rather than by
#  lowering the value for the whole field.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED. A biocidal antifouling product requires authorisation
#  before it may be placed on the market, its active substances must be
#  approved, and a specific class of these products is prohibited outright by
#  international convention. Ships are surveyed and certified for compliance.
#
#  RESTRICTED is worth considering, since tributyltin is genuinely prohibited
#  rather than merely controlled. REGULATED is the better fit for the field as
#  a whole: what is restricted is one withdrawn technology, while the current
#  ones are authorised subject to assessment.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit is a coating applied to vessels and structures
#  at commercial scale, formulated and manufactured industrially.
#
#  A case could be made for POPULATION, since the harm this record's history
#  turns on was to mollusc populations across whole coastlines, and since the
#  invasive species objective concerns populations moving between ports. That
#  is the consequence rather than the unit of operation, and it is recorded in
#  the metrics instead.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. MATERIALS is the sector: these are coatings and surfaces.
#  ENVIRONMENT is claimed twice over and is the heart of the record, covering
#  both the harm biocides have done and the emissions avoided by a smooth hull.
#  ENERGY is claimed because the fuel consequence across the world fleet is the
#  principal economic and climate justification for the whole field, and a
#  domain filter that returned only MATERIALS would hide why this record
#  matters.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.ENVIRONMENT,
    Domain.ENERGY,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. Biocidal products require prior
#  authorisation and their active substances require approval. The prohibition
#  of organotin coatings sits alongside that as a specific exclusion rather
#  than as the general status of the field.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by what each instrument governs.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the instrument that exists because of this record's history -----------
    "The International Convention on the Control of Harmful Anti-fouling "
    "Systems on Ships, which prohibits organotin coatings globally and requires "
    "certification and survey of compliance, adopted because a national ban on "
    "a coating applied to internationally trading ships moves the problem "
    "rather than solving it",
    "Regulation (EC) No 782/2003, which implements that prohibition within the "
    "Union",
    # -- an antifouling biocide is a biocide -------------------------------------
    "Regulation (EU) No 528/2012 on biocidal products, under which antifouling "
    "products are product type 21, active substances require approval and "
    "products require authorisation with efficacy and environmental risk data",
    "Regulation (EC) No 1907/2006 REACH and Regulation (EC) No 1272/2008 CLP "
    "for the substances themselves",
    # -- what may be released into the water --------------------------------------
    "Directive 2000/60/EC and Directive 2008/56/EC, under which tributyltin "
    "compounds are priority hazardous substances and copper is assessed against "
    "environmental quality standards",
    "National and port authority rules on in-water hull cleaning, which "
    "commonly require capture of removed material because cleaning releases "
    "both organisms and biocide into the harbour",
    "Discharge consents and sediment quality requirements in marinas and "
    "enclosed harbours, where accumulation rather than concentration is the "
    "concern",
    # -- the other objective: organisms rather than chemicals ----------------------
    "The Ballast Water Management Convention, which addresses the other major "
    "vector for marine invasions and is binding where the biofouling "
    "instruments are guidance",
    "Regulation (EU) No 1143/2014 on invasive alien species, and national "
    "biofouling requirements where these exist as binding rules rather than as "
    "recommendations",
    # -- the people applying it ----------------------------------------------------
    "Occupational exposure and waste legislation covering coating application "
    "and removal in shipyards, including collection of blasted coating residue",
)


# =============================================================================
#  STANDARDS
#  Not law, and the first group governs the invasive species objective almost
#  entirely, since binding rules for it are the exception.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the guidance that does the work of law ---------------------------------
    "International Maritime Organization guidelines for the control and "
    "management of ships' biofouling to minimise the transfer of invasive "
    "aquatic species, which shape practice while remaining recommendatory in "
    "most jurisdictions",
    "Biofouling management plans and record books, which are how those "
    "guidelines are actually implemented on a vessel",
    "Niche area inspection protocols, which matter because sea chests and "
    "thrusters carry the transferable organisms while the open hull carries the "
    "drag penalty",
    # -- testing whether a coating works ------------------------------------------
    "ASTM D6990 and related standards for assessing fouling on static "
    "immersion panels, which is slow and remains necessary because laboratory "
    "assays predict field performance poorly",
    "Standard settlement assay protocols for barnacle cyprids and algal spores, "
    "useful for ranking candidates rather than for claiming performance",
    "Hull roughness and performance monitoring conventions, which is how the "
    "fuel benefit is demonstrated in service rather than modelled",
    # -- assessing what it does to everything else ---------------------------------
    "OECD ecotoxicity test guidelines across trophic levels, from which the "
    "predicted no effect concentration in `metrics.py` is derived",
    "Environmental emission scenario documents for antifouling products, which "
    "fix how the predicted environmental concentration is modelled so that two "
    "products are assessed comparably",
    "Leaching rate determination methods, since the release rate a product is "
    "authorised against must be measured by an agreed procedure",
    # -- applying and removing it ----------------------------------------------------
    "ISO 12944 and marine coating application standards for surface "
    "preparation and application",
    "In-water cleaning and capture standards, which are what make maintenance "
    "acceptable rather than a discharge",
)
