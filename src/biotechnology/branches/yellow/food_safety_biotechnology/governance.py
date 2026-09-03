# =============================================================================
#  biotechnology.branches.yellow.food_safety_biotechnology.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record's governance has a feature found nowhere else in the library:
#  THE METHOD ITSELF IS REGULATED, NOT ONLY THE RESULT.
#
#  For most of this library an analytical method is a technical choice. Here,
#  a result that carries legal consequence must be produced by a method
#  validated against a reference standard, in an accredited laboratory, on the
#  matrix concerned. A better method that has not been through that process
#  cannot be used to release a product or to justify a recall, however good it
#  is.
#
#  That is why method validation appears in STANDARDS with more weight than
#  usual, and why the adoption of any new technique in this record is slower
#  than its performance would suggest.
#
#  THE SECOND FEATURE IS THAT A RESULT CREATES A LEGAL DUTY. Under general food
#  law an operator who has reason to believe food is unsafe must withdraw it
#  and inform the authorities. There is no discretion to investigate quietly.
#  A positive result is therefore not information to be weighed but a trigger,
#  which is why the false positive cost asymmetry recorded in `metrics.py` is
#  commercial rather than academic, and why confirmation before action matters
#  so much.
#
#  A THIRD: the microbiological criteria are not pass marks. They are
#  verification that a process is under control, and a food meeting them is not
#  thereby safe. That distinction is stated in the legislation and is widely
#  misread.
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
#  MATURITY = ESTABLISHED. Molecular pathogen detection has been routine since
#  the late 1990s, the regulatory framework is mature, accreditation is
#  universal, and routine genomic surveillance has been operating for a decade.
#
#  Metagenomic and portable methods are newer and are a minority of practice.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED, and the reason is the method rather than the hazard.
#
#  A laboratory producing results with legal consequence requires accreditation,
#  the methods require validation against reference standards, and official
#  control laboratories are designated by authorities. Approval precedes use,
#  which is what the value denotes.
#
#  This is a case where the tier reflects governance intensity rather than any
#  danger in the activity: analysing food for pathogens is ordinary laboratory
#  work at containment level 2, and the weight comes from the consequences of
#  the answer.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION, and the choice is deliberate over INDUSTRIAL.
#
#  Product testing happens in a plant, which would suggest INDUSTRIAL. But the
#  activity this record is actually about is surveillance across a food supply
#  and a population: outbreak detection links cases across countries, national
#  monitoring programmes sample entire commodity streams, and the genomic
#  cluster analysis that transformed the field is a population method.
#
#  Recording INDUSTRIAL would describe the sampling point and miss the system.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. HEALTH is placed first because foodborne illness is the hazard and
#  outbreak investigation is public health work. FOOD is the sector.
#  INFORMATION is claimed deliberately: the field's largest recent advance is a
#  sequence database and a cluster definition, its outputs are data rather than
#  substances, and its unresolved problems are interpretive.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.HEALTH,
    Domain.FOOD,
    Domain.INFORMATION,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED, applied to the METHOD rather than to a
#  product, which is unusual and is the point.
#
#  Nothing here is placed on a market. What requires prior approval is the
#  analytical method used to generate a legally consequential result, and the
#  accreditation of the laboratory producing it. A method not validated for the
#  matrix cannot be used for official control however well it performs.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by what each instrument requires.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- what a result obliges you to do ---------------------------------------
    "Regulation (EC) No 178/2002 general food law, whose withdrawal and "
    "notification duties turn a positive result into a legal obligation rather "
    "than information to be weighed, and which establishes the Rapid Alert "
    "System for Food and Feed",
    "Regulation (EC) No 2073/2005 on microbiological criteria for foodstuffs, "
    "which sets food safety criteria and process hygiene criteria, and which "
    "states that meeting a criterion verifies control rather than "
    "demonstrating safety",
    "Regulation (EC) No 852/2004 on hygiene, under which testing sits inside "
    "hazard analysis rather than replacing it",
    # -- who may produce a result that counts ------------------------------------
    "Regulation (EU) 2017/625 on official controls, which designates official "
    "laboratories, requires accreditation and establishes the reference "
    "laboratory network that arbitrates method disputes",
    "Method validation requirements against reference standards, without which "
    "a result cannot be used for official control however good the method",
    # -- the specific hazards -----------------------------------------------------
    "Regulation (EC) No 1881/2006 setting maximum levels for contaminants "
    "including mycotoxins and marine biotoxins, with the tightest limits on "
    "food for infants",
    "Regulation (EU) No 1169/2011 on food information, whose Annex II fixes the "
    "allergens that must be declared and therefore what must be detectable",
    "Implementing rules on gluten-free labelling, which set the twenty "
    "milligrams per kilogram threshold that makes the claim measurable",
    # -- authenticity, which is enforced under different law -----------------------
    "Regulation (EU) 2017/625 provisions on fraudulent and deceptive practices, "
    "which brought food fraud explicitly within official control",
    "Regulation (EU) No 1151/2012 on quality schemes, whose protected "
    "designations are enforced partly by the origin testing in this record",
    # -- and the data ---------------------------------------------------------------
    "Regulation (EU) 2016/679, applicable where clinical isolate sequences from "
    "identified patients are shared across borders for outbreak investigation, "
    "which is a genuine tension between surveillance and data protection",
)


# =============================================================================
#  STANDARDS
#  Not law, and in this record they carry unusual weight because the method
#  itself must be approved.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the methods that count -------------------------------------------------
    "ISO 6579 for Salmonella, ISO 11290 for Listeria monocytogenes and the "
    "related horizontal methods, which are the reference methods alternatives "
    "must be validated against",
    "ISO 16140 for method validation and verification, which is the standard "
    "that decides whether a rapid method may substitute for a reference one",
    "AOAC and equivalent certification schemes for commercial test kits",
    # -- the laboratory ----------------------------------------------------------
    "ISO/IEC 17025 accreditation, without which a result carries no official "
    "weight regardless of its accuracy",
    "Proficiency testing and interlaboratory comparison schemes, which is how a "
    "laboratory demonstrates that its results agree with everyone else's",
    "Measurement uncertainty estimation and reporting, which matters because a "
    "result close to a legal limit is a decision about uncertainty rather than "
    "about a number",
    # -- sampling, which the standards address better than the field does ----------
    "Codex Alimentarius sampling plans and the two-class and three-class "
    "attribute plans, which define what a negative result actually means",
    "Environmental monitoring programme design, which samples the problem "
    "rather than the product and which the 2022 recognition in `history.py` "
    "pushed to the centre",
    # -- comparing genomes -------------------------------------------------------
    "Core genome multilocus sequence typing schemes and agreed cluster "
    "thresholds, which make sequences comparable between laboratories and "
    "countries",
    "Sequence data sharing conventions and public repositories, which are what "
    "make cross-border outbreak detection possible and which run into the data "
    "protection tension noted above",
    # -- and the frameworks around them -------------------------------------------
    "Codex Alimentarius general principles of food hygiene and HACCP",
    "GFSI-recognised certification schemes including FSSC 22000, BRCGS and IFS, "
    "which impose testing requirements beyond the legal minimum and are what a "
    "retailer actually audits against",
)
