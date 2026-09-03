# =============================================================================
#  biotechnology.branches.grey.bioaugmentation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS RECORD HAS A REGULATORY GAP AT ITS CENTRE, AND THE GAP IS THE MOST
#  IMPORTANT THING IN THE FACET.
#
#      SAFETY IS REGULATED. EFFICACY IS NOT.
#
#  A microbial product sold for waste treatment must generally be safe: the
#  organisms must not be pathogens, the release must not introduce a harmful
#  non-indigenous species, and the material must be handled properly. Those
#  requirements exist and are enforced.
#
#  Whether the product does anything is, in most jurisdictions, an advertising
#  question rather than an approval question. There is no efficacy dossier, no
#  controlled trial requirement, and no equivalent of the marketing
#  authorisation that `red.antibody_engineering` cannot be sold without. A
#  product that reliably does nothing can be lawfully sold indefinitely,
#  provided it is not dangerous and its claims are not demonstrably false.
#
#  That asymmetry, and not any hazard, is why this record's governance matters.
#  It is the same structure `yellow.probiotics_and_prebiotics` describes for
#  supplements and `green.biofertilisers` for soil inoculants, and the
#  consequence is the same: the burden of evidence falls on the buyer.
#
#  A SECOND POINT. Because the regulated hazard is small, the RISK TIER here is
#  LOWER than in `grey.bioremediation`, which is initially counterintuitive.
#  The tier measures governance intensity, and adding ordinary non-pathogenic
#  bacteria attracts less of it than excavating contaminated land does.
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
#  MATURITY = COMMERCIAL, and the value needs its reasoning stated because a
#  reader could argue for either neighbour.
#
#  ESTABLISHED would be wrong. An established practice is one whose benefit is
#  agreed, and the central proposition here fails controlled comparison in most
#  applications. A large market is not the same thing as an established
#  technique.
#
#  PILOT would also be wrong, and would understate the record. Digester seeding
#  is a century-old routine, plant reseeding after a toxic shock is standard,
#  and dechlorinating consortia are a mature commercial service with reproduced
#  evidence behind them.
#
#  COMMERCIAL is the honest value: products are sold at scale, some of them
#  work, and the field has not converged on which.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED.
#
#  Requirements exist and they are modest. The organisms must not be pathogens,
#  non-indigenous species are controlled, and release into groundwater usually
#  needs the same injection permit any amendment needs. That is a notification
#  and compliance regime rather than a prior approval of the product itself.
#
#  It is deliberately LOWER than the REGULATED tier assigned to
#  `grey.bioremediation`, which will look odd to a reader who assumes tiers
#  track danger. They do not. They track governance intensity. Excavating
#  contaminated soil triggers liability law, waste law and a formal remediation
#  plan approval; pouring non-pathogenic bacteria into a grease trap triggers a
#  product safety regime and very little else.
#
#  Genetically modified degraders would sit far higher, which is why they are
#  not deployed. That is recorded in REGULATIONS rather than in this value,
#  because the value describes what the practice actually is.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = FIELD.
#
#  The unit is an open environment into which organisms are released: a site, a
#  lagoon, a soil, a plume. That the practice usually fails at this scale is
#  the record's content and does not change where it is attempted.
#
#  INDUSTRIAL would describe the digester and bioreactor seeding cases, which
#  are a real part of the record but not the majority of it, and choosing it
#  would misdescribe the contested applications this record exists to examine.
# -----------------------------------------------------------------------------
SCALE = Scale.FIELD

# -----------------------------------------------------------------------------
#  DOMAINS. ENVIRONMENT is the whole of it in substance.
#
#  GOVERNANCE is included for a specific and non-decorative reason: the
#  defining problem in this record is a regulatory gap between safety approval
#  and efficacy evidence, and that gap is a governance object rather than a
#  technical one. This is one of the few records in the library where the
#  domain is claimed for the absence of a rule rather than the presence of one.
#
#  HEALTH is deliberately NOT claimed. The gut parallel in
#  `yellow.probiotics_and_prebiotics` is an analogy, not a shared application,
#  and claiming a health domain on the strength of an analogy is exactly the
#  padding the domain vocabulary exists to prevent.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENVIRONMENT,
    Domain.GOVERNANCE,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = NOTIFIED.
#
#  This is the value that carries the record's central point. A product is
#  registered or notified, its organisms are checked against pathogen lists,
#  and it goes on sale. Nobody assesses whether it works.
#
#  AUTHORISED would be wrong and would mislead badly, because it implies an
#  authority evaluated the product and permitted it on the merits. That is what
#  happens in `red.antibody_engineering` and it is not what happens here.
#
#  UNREGULATED would also be wrong: pathogen restrictions and non-indigenous
#  species controls are real and enforced.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.NOTIFIED


# =============================================================================
#  REGULATIONS
#  Binding law. Note how much of it is about safety and how little about
#  whether the product does anything.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- what the product may contain -------------------------------------------
    "Microbial product registration and notification requirements, under which "
    "the organisms are checked against pathogen and risk group classifications "
    "before sale",
    "Biological agent classification schemes, including European Union "
    "Directive 2000/54/EC on exposure to biological agents at work, which set "
    "the containment expectations for handling the cultures",
    "Restrictions on the release of non-indigenous species, which bear on "
    "cultures isolated in one region and sold into another",
    "Product labelling requirements covering composition, viable count and "
    "handling, which is where a buyer can check what was supposed to be in the "
    "container",
    # -- the gap, stated as the law that does not exist ---------------------------
    "Absence of a pre-market efficacy assessment in most jurisdictions, so a "
    "product must be safe and need not be shown to work, which is the "
    "structural feature this record turns on",
    "General consumer protection and misleading advertising law, which is the "
    "only route by which an ineffective product is challenged and which "
    "requires a claim to be demonstrably false rather than merely unsupported",
    # -- releasing anything into the ground -----------------------------------------
    "Underground injection permitting, which applies to a culture introduced "
    "into an aquifer exactly as it applies to any other amendment",
    "Groundwater protection legislation, including the Groundwater Directive "
    "2006/118/EC, which governs what may be introduced into a body of water "
    "somebody may later abstract from",
    "Remediation plan approval, under which an augmentation step is approved as "
    "part of the site plan rather than as a product in its own right",
    # -- and the route that is effectively closed --------------------------------------
    "Deliberate release requirements for genetically modified organisms, "
    "including European Union Directive 2001/18/EC, which in practice preclude "
    "engineered degraders from field remediation",
    "Contained use requirements applying to engineered strains in bioreactors, "
    "which is where such organisms are actually used",
    "Access and benefit sharing obligations under the Nagoya Protocol, "
    "applicable where a commercial culture was derived from material collected "
    "in another country",
)


# =============================================================================
#  STANDARDS
#  Not law, and in this record they are carrying the weight the law does not.
#  The first group is the trial design that would settle the question.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- how to find out whether it works ---------------------------------------
    "Controlled field trial design conventions requiring an unaugmented control "
    "plot, replication and randomisation, which is the only design capable of "
    "producing this record's first metric",
    "Statistical power and sample size determination for field comparisons, "
    "since site heterogeneity is large enough that an underpowered trial finds "
    "nothing whether or not anything happened",
    "Reporting conventions for negative and null results, which matter more in "
    "this field than in most because the failures are what the evidence base "
    "consists of",
    "Microcosm treatability study protocols using site material, which are the "
    "affordable proxy for a field trial and are honest about being a proxy",
    # -- deciding whether the site is even a candidate -----------------------------
    "Pre-application molecular screening guidance, establishing whether the "
    "relevant organisms and functional genes are already present, which is the "
    "practical form of this record's central distinction",
    "Quantitative tracking conventions for introduced strains, distinguishing a "
    "population that established from one that was detected on the day it was "
    "applied",
    # -- what should be in the container -------------------------------------------
    "Culture collection deposit and characterisation practice, which is what "
    "separates a defined consortium from an undefined mixture",
    "Viable count determination and shelf-life testing methods",
    "Cold chain and storage practice, since the count on the label is not the "
    "count that arrives",
    "Quality management systems for culture production, including ISO 9001 "
    "where a producer has adopted it",
    # -- and the specific practice that works ---------------------------------------
    "Dechlorinating consortium application protocols, including electron donor "
    "co-delivery and post-application monitoring to ethene, which is the one "
    "application in this record with a settled method",
    "Digester and activated sludge seeding practice, which is a century old, "
    "uncontested, and works because there is no incumbent community to "
    "displace",
)
