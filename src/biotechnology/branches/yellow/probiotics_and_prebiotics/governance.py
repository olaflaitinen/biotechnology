# =============================================================================
#  biotechnology.branches.yellow.probiotics_and_prebiotics.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record contains the clearest case in the library of REGULATION OF A
#  CLAIM RATHER THAN OF A PRODUCT, and the distinction is the whole of its
#  governance.
#
#  The products are, with few exceptions, ordinary foods or supplements. The
#  organisms have a documented history of safe use, the substrates are common
#  fibres, and neither requires authorisation to sell. What is regulated is
#  WHAT MAY BE SAID.
#
#  In the European Union no health claim for any probiotic has been authorised,
#  and because the word probiotic itself implies a health benefit, several
#  member states restrict the word on labels. A category that may be sold
#  freely and may not be described is an unusual regulatory position and it
#  produces the marketing by implication that this record records as a
#  challenge.
#
#  THE SECOND POINT IS THAT THE SAME BIOLOGY SPANS FOUR REGIMES. A yoghurt is a
#  food. A capsule is a food supplement. A defined consortium for recurrent
#  infection is a licensed medicine with trial evidence. Faecal microbiota
#  transplantation is regulated as a medicine, a tissue or under a bespoke
#  framework depending on the jurisdiction, and the classification is contested.
#
#  The evidence bar rises steeply across those four, and so does the strength
#  of the demonstrated effect. That correlation is the most useful thing this
#  facet can point out.
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
#  MATURITY = COMMERCIAL. The market is large, long-established and global, and
#  fermented dairy products carrying live cultures have been sold for over a
#  century.
#
#  It is not ESTABLISHED, and the reason is unusual: the products are
#  established and the science underlying most of their claims is not. A
#  category where no health claim has been authorised in a major jurisdiction
#  has not settled, whatever its sales.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED, which is the honest position across a record whose
#  parts differ sharply.
#
#  A probiotic yoghurt alone would be ROUTINE. A licensed bacterial consortium
#  or a faecal transplant would be REGULATED, with full clinical evidence and
#  agency approval. Donor screening for transplantation is closer to tissue
#  regulation than to food law.
#
#  CONTROLLED reflects that food business registration applies throughout, that
#  the production organisms must satisfy safety assessment before use, and that
#  a substantial part of the record sits under medicines law.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION, and the choice is deliberate over INDUSTRIAL.
#
#  The manufacturing is industrial and unremarkable. What this record is
#  actually about is an intervention in a person's microbial community, and the
#  questions that decide it are population questions: does the effect hold
#  across individuals, what is the number needed to treat, how much does
#  response vary between people.
#
#  The 2018 finding that colonisation is highly individual is a population
#  finding, and recording INDUSTRIAL would describe the factory rather than the
#  subject.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. HEALTH is placed first and is the correct primary label: the entire
#  proposition is a health claim, the strongest evidence is clinical, and the
#  regulatory action concerns what may be said about health. FOOD is the sector
#  most of the products are sold in. Two domains is the honest answer, since
#  nothing here is a material, an environmental intervention or an information
#  product.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.HEALTH,
    Domain.FOOD,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, across the four regimes named in the header.
#
#  A yoghurt requires no authorisation. A supplement requires notification in
#  many member states. A licensed consortium is an authorised medicine. Faecal
#  transplantation is classified differently in different jurisdictions and the
#  classification is actively contested.
#
#  The same underlying intervention spans from unregulated to fully authorised,
#  and the evidence bar rises with it.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by the four regimes. Note that the first group governs
#  speech rather than substance.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- what may be SAID, which is what is actually regulated -----------------
    "Regulation (EC) No 1924/2006 on nutrition and health claims, under which "
    "no probiotic health claim has been authorised in the European Union and "
    "which is therefore the operative instrument for this entire record",
    "National restrictions on the use of the word probiotic on labels, adopted "
    "in several member states because the term itself implies an unauthorised "
    "health benefit, and differing between them",
    "Directive 2005/29/EC on unfair commercial practices, which governs "
    "implied claims where explicit ones are unavailable",
    # -- the food and supplement route -------------------------------------------
    "Regulation (EC) No 178/2002 and Regulation (EC) No 852/2004 on general "
    "food law and hygiene",
    "Directive 2002/46/EC on food supplements, which is how most capsule and "
    "sachet products reach the market and which requires notification rather "
    "than authorisation in most member states",
    "Regulation (EU) 2015/2283 on novel foods, applicable to organisms without "
    "a history of consumption, which is the route the next-generation gut "
    "strains must take",
    "Regulation (EU) No 609/2013 on food for specific groups, covering infant "
    "formula and the oligosaccharides added to it",
    # -- the medicines route, where the evidence is strongest ----------------------
    "Directive 2001/83/EC and Regulation (EC) No 726/2004, under which defined "
    "bacterial consortia for recurrent infection are authorised as medicinal "
    "products with the clinical evidence that implies",
    "Regulation (EU) No 536/2014 on clinical trials, governing the studies "
    "this record's stronger claims depend on",
    # -- faecal transplantation, which fits nowhere cleanly -------------------------
    "Directive 2004/23/EC on tissues and cells, applied to faecal microbiota "
    "transplantation in some jurisdictions and not in others, where it is "
    "instead treated as a medicinal product or under a bespoke framework",
    "Donor screening and traceability requirements for transplantation, which "
    "are closer to blood and tissue regulation than to anything else in this "
    "branch",
    # -- the animal side ------------------------------------------------------------
    "Regulation (EC) No 1831/2003 on feed additives, under which direct-fed "
    "microbials are authorised with efficacy data, which is a stricter "
    "requirement than the human food route imposes",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what would fix the record's central problem and
#  is largely voluntary.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the standards that would make evidence attachable to products ---------
    "Conventions requiring full genus, species and strain designation on the "
    "label, without which published evidence cannot be attached to a product, "
    "and which remain voluntary in most markets",
    "Whole genome sequence deposition for commercial strains, which makes a "
    "strain designation verifiable rather than declarative",
    "Reporting conventions requiring the strain, the dose and the endpoint "
    "together, since a result reported without all three is not usable by "
    "anyone else",
    # -- proving the organism is safe to use --------------------------------------
    "Qualified presumption of safety assessment and inventories of "
    "microorganisms with a documented history of safe use in food",
    "Antimicrobial resistance gene screening and demonstration that resistance "
    "is not transferable, which is a requirement rather than good practice "
    "given that a live organism joins a community",
    "Culture collection deposit under the Budapest Treaty where patent "
    "protection is sought",
    # -- proving the product contains what it claims -------------------------------
    "Viability determination methods and end-of-shelf-life count declaration, "
    "which is the specification that matters and is frequently not verified",
    "Identity verification of the organisms actually present, following "
    "published surveys finding products containing undeclared species",
    # -- running the trials properly ------------------------------------------------
    "CONSORT reporting for randomised trials and PRISMA for systematic reviews, "
    "which in this field would prevent much of the meta-analysis that combines "
    "studies of different strains as though they were the same intervention",
    "Registration of trials before they begin, which addresses the publication "
    "bias a field with commercial sponsorship is particularly exposed to",
    # -- the transplantation end -----------------------------------------------------
    "Donor screening panels, stool banking conventions and long-term recipient "
    "follow-up, which are the practical governance of an intervention "
    "transferring an uncharacterised community between people",
)
