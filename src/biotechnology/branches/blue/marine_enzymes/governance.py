# =============================================================================
#  biotechnology.branches.blue.marine_enzymes.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is where the branch's access and benefit sharing problem is at
#  its sharpest, and the reason is specific rather than general.
#
#  IN THIS RECORD, THE PRODUCT IS THE SEQUENCE.
#
#  For `blue.marine_natural_products` the useful thing is a molecule, and a
#  molecule has to be made, which leaves a manufacturing trail. For this record
#  the useful thing is a gene. Once it is read it can be synthesised anywhere,
#  expressed in a conventional host, and sold as a protein with no further
#  reference to the organism, the water, or the country the sample came from.
#  Nothing physical crosses a border.
#
#  That is precisely the situation the digital sequence information debate
#  exists about, and it is why this record's obligations attach to information
#  rather than to material. A researcher who never touches a marine sample can
#  still hold an obligation towards the jurisdiction the sequence came from.
#
#  THE SECOND POINT IS THAT THE PRODUCT ITSELF IS ORDINARY. An enzyme is
#  regulated as a chemical and, in food or feed, requires authorisation, on
#  exactly the terms `white.industrial_enzymes` sets out. Marine origin earns
#  no concession and creates no additional product requirement. The whole
#  governance difference lies upstream of the fermenter.
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
#  MATURITY = COMMERCIAL. Marine enzymes are sold: a deep-sea polymerase is in
#  most molecular biology laboratories, heat-labile enzymes are catalogue
#  products, and cold-active enzymes are in detergent and food processing.
#
#  It is not ESTABLISHED, which `white.industrial_enzymes` carries, because
#  marine enzymes remain a small share of the industrial enzyme market and the
#  discovery pipeline is constrained by the expression problem recorded in
#  `metrics.py`. Real products, narrow footprint.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED. Two independent grounds, and either alone would be
#  sufficient.
#
#  The production organism is a genetically modified microorganism under
#  contained use, since the enzyme is almost always expressed heterologously
#  rather than purified from its marine source. And collection requires the
#  permissions set out in `blue.marine_genomics`, which apply whether the
#  sample is sought for its sequence or its chemistry.
#
#  The enzymes themselves present ordinary laboratory hazards, with the
#  sensitisation caveat that `white.industrial_enzymes` records for the class.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL, which differs from `blue.marine_natural_products` at
#  BENCH and the difference is the whole point of the comparison.
#
#  An enzyme is a gene. Once the sequence is known the protein is manufactured
#  by fermentation at ordinary industrial scale, so this record has no supply
#  problem at all. That is why it has products and the natural products record
#  has a constraint.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. MATERIALS covers the industrial and processing applications, which
#  is the largest use by volume. FOOD covers the chill-temperature processing
#  and dairy applications that are the clearest commercial case for cold
#  activity. INFORMATION is claimed deliberately and is the unusual one: the
#  field's principal output is sequence, its principal discovery method is
#  database mining, and its principal legal problem is about information rather
#  than material.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.FOOD,
    Domain.INFORMATION,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED, matching `white.industrial_enzymes`, since
#  the product faces the same regime: food enzymes require authorisation and a
#  positive listing, feed enzymes require authorisation, and the substance is
#  registered under chemicals law. Marine origin changes none of it.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped so that the upstream and downstream halves are
#  distinguishable, because they are governed by different systems.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- upstream: where the sequence came from, which is this record's problem -
    "The Convention on Biological Diversity and the Nagoya Protocol, whose "
    "obligations attach to the sequence and not only to a physical sample, "
    "which is decisive here because nothing physical need ever cross a border",
    "Regulation (EU) No 511/2014, imposing due diligence and record-keeping on "
    "users of genetic resources within the Union",
    "The 2023 Agreement on marine biological diversity of areas beyond "
    "national jurisdiction, including its provisions on digital sequence "
    "information",
    "The United Nations Convention on the Law of the Sea, under which marine "
    "scientific research in another state's waters requires consent",
    "National marine collection permits and protected area conditions",
    # -- midstream: making the protein ------------------------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, which governs the expression host rather than the enzyme",
    "Directive 2000/54/EC on biological agents at work",
    # -- downstream: the product, on ordinary terms -------------------------------
    "Regulation (EC) No 1332/2008 on food enzymes and the Union list "
    "authorisation procedure",
    "Regulation (EC) No 1831/2003 on feed additives",
    "Regulation (EC) No 1907/2006 REACH and Regulation (EC) No 1272/2008 CLP",
    "Regulation (EC) No 648/2004 on detergents, for the cold-wash applications",
    "Occupational exposure requirements for enzyme dust as a respiratory "
    "sensitiser, which apply to marine enzymes exactly as to any other",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what makes a claim of cold adaptation checkable
#  rather than rhetorical.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- making the central claim verifiable -----------------------------------
    "Reporting conventions requiring activity to be stated at a defined "
    "temperature against a mesophilic comparator, without which a claim of cold "
    "adaptation cannot be distinguished from a claim of cold provenance",
    "Declaration of assay duration alongside an optimum temperature, since for "
    "an unstable enzyme a shorter assay moves the apparent optimum upwards",
    "Declaration of the criteria used for inactivation, since partial or "
    "reversible loss of activity does not deliver the property the product is "
    "sold for",
    # -- naming and measuring things consistently --------------------------------
    "International Union of Biochemistry and Molecular Biology enzyme "
    "nomenclature and EC numbering",
    "Supplier-declared assay conditions for the activity unit, on the same "
    "terms `white.industrial_enzymes` records",
    # -- purity and manufacture ---------------------------------------------------
    "Joint FAO/WHO Expert Committee on Food Additives specifications for enzyme "
    "preparations, and Food Chemicals Codex monographs for food grades",
    "Good Manufacturing Practice and HACCP or FSSC 22000 certification for the "
    "production site",
    "Association of Manufacturers and Formulators of Enzyme Products guidance "
    "on safe handling and encapsulation",
    # -- depositing what was found -------------------------------------------------
    "Sequence deposition in the international nucleotide databases, which in "
    "this field is simultaneously good scientific practice and the act that "
    "makes a genetic resource globally available, a tension the benefit sharing "
    "instruments have not fully resolved",
    "Strain and clone deposit in a recognised culture collection under the "
    "Budapest Treaty where patent protection is sought",
    # -- doing the sampling fairly ---------------------------------------------------
    "Research partnership norms under which scientists from the sampled region "
    "are co-investigators, which for a sequence-based product is the only "
    "benefit sharing that occurs before commercialisation",
)
