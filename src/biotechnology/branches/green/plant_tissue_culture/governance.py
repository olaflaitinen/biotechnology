# =============================================================================
#  biotechnology.branches.green.plant_tissue_culture.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Nothing regulates the technique. Growing a plant from a piece of another
#  plant triggers no biosafety regime anywhere, because no novel organism is
#  created and the product is genetically identical to material already in the
#  field.
#
#  What governs this record is PLANT HEALTH LAW, and it governs it more tightly
#  than any other subtype in the green branch. The reason is the compounding
#  arithmetic in `metrics.py`: one infected mother plant multiplied eight times
#  at a rate of five is nearly four hundred thousand infected plants,
#  distributed nationally, in under two years. A pathogen that would have
#  spread slowly by conventional propagation is instead delivered everywhere at
#  once.
#
#  That is why REGULATORY_STATUS is NOTIFIED rather than UNREGULATED. The
#  technique is free; moving its output across a border is not. Certification
#  schemes, phytosanitary certificates and pathogen indexing are the operative
#  controls, and they attach to the plants rather than to the method.
#
#  The second governance thread is ACCESS. Micropropagating a landrace or a
#  wild relative collected in another country engages the Nagoya Protocol, and
#  an in vitro genebank holding accessions from dozens of countries is holding
#  dozens of separate legal relationships.
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
#  Commercial since the 1970s, and the basis of the global banana, orchid,
#  potato and sugarcane planting material trades. The medium formulation in
#  daily use was published in 1962.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = ROUTINE.
#  Ordinary laboratory work under standard safety rules. No permit, no
#  committee, no containment question. The only hazard of note is the
#  sterilising agents.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.ROUTINE

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL.
#  Deliberate, and the only ROUTINE plus INDUSTRIAL combination in the green
#  branch. A commercial micropropagation laboratory produces tens of millions
#  of plantlets a year in a facility that is a factory in everything but name,
#  while remaining an ordinary laboratory in regulatory terms.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS
#  FOOD is the main purpose. ENVIRONMENT is included because in vitro
#  conservation and cryopreservation of crop wild relatives and endangered
#  species is a substantial and growing use, covered further in
#  `grey.biodiversity_conservation`.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (Domain.FOOD, Domain.ENVIRONMENT)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = NOTIFIED.
#  The technique needs no authorisation. The output cannot cross a border
#  without a phytosanitary certificate, and cannot be sold as certified
#  planting material without registration and pathogen indexing. The control
#  attaches to the plants, not to the method.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.NOTIFIED


# =============================================================================
#  REGULATIONS
#  Plant health first, because that is what actually binds. Then access to the
#  germplasm, then what may be sold.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # ---- plant health, the operative constraint ------------------------------
    "EU Regulation (EU) 2016/2031 on protective measures against pests of "
    "plants, under which plants for planting are the highest-risk category "
    "precisely because propagation multiplies any infection",
    "EU Regulation (EU) 2017/625 on official controls, governing inspection at "
    "the point of entry",
    "International Plant Protection Convention and the phytosanitary "
    "certificate regime, which is why material cannot simply be posted between "
    "countries",
    "National quarantine requirements for imported in vitro material, which in "
    "several countries mandate post-entry growing-on under observation",
    # ---- where the germplasm came from ----------------------------------------
    "Nagoya Protocol on Access and Benefit-sharing, engaged whenever a landrace "
    "or wild relative collected elsewhere is propagated",
    "EU Regulation (EU) No 511/2014 implementing Nagoya user compliance",
    "International Treaty on Plant Genetic Resources for Food and Agriculture, "
    "and its standard material transfer agreement, which is the route most crop "
    "germplasm actually moves by",
    # ---- what may be sold -------------------------------------------------------
    "EU marketing directives for propagating material of fruit, vegetable and "
    "ornamental plants",
    "National seed and planting material certification schemes, which set the "
    "pathogen indexing a batch must pass",
    # ---- where the technique is applied to a modified plant ---------------------
    "EU Directive 2009/41/EC on contained use, which applies to the culture "
    "step only where the material being regenerated is genetically modified",
)


# =============================================================================
#  STANDARDS
#  Certification schemes are listed first, because in practice they are what a
#  commercial laboratory is audited against.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # ---- certifying that the material is clean -------------------------------
    "EPPO certification schemes for pathogen-tested planting material, which "
    "define the indexing a nuclear stock plant must pass",
    "EPPO diagnostic protocols for regulated pests, PM 7 series",
    "National virus-tested stock schemes, such as those operated for potato, "
    "fruit and strawberry",
    # ---- conserving it -----------------------------------------------------------
    "FAO Genebank Standards for Plant Genetic Resources for Food and "
    "Agriculture, including the in vitro and cryopreservation sections",
    "Bioversity International and CGIAR technical guidelines for in vitro "
    "conservation and cryopreservation",
    # ---- describing it -----------------------------------------------------------
    "Multi-Crop Passport Descriptors for germplasm accessions",
    "FAO and Bioversity crop descriptor lists",
    # ---- running the laboratory ----------------------------------------------------
    "ISO 9001 quality management, commonly held by commercial micropropagation "
    "laboratories",
    "Good practice guidance on aseptic technique and contamination indexing "
    "from national horticultural research bodies",
    # ---- checking the copies are copies -----------------------------------------------
    "Molecular marker and methylation-based genetic fidelity testing protocols, "
    "adopted after the oil palm mantled-fruit episode showed that a "
    "sequence-identical clone can still be defective",
)
