# =============================================================================
#  biotechnology.branches.yellow.nutrigenomics.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record contains a regulatory gap rather than a regulatory regime, and
#  naming it precisely is the most useful thing this facet can do.
#
#      A CLINICAL GENETIC TEST is an in vitro diagnostic medical device. It
#      requires conformity assessment, clinical evidence, professional
#      interpretation and a defined care pathway.
#
#      A CONSUMER TEST SOLD FOR "WELLNESS" OR DIETARY PURPOSES has frequently
#      been placed outside that framework, on the argument that it makes no
#      medical claim. The same genotyping, on the same variants, with no
#      clinical oversight and no requirement to demonstrate that the advice
#      given follows from the result.
#
#  The European in vitro diagnostic regulation narrowed that gap considerably
#  by bringing more genetic tests within scope regardless of the claim made,
#  and the position still differs between jurisdictions and the enforcement
#  record is uneven.
#
#  THE SECOND POINT: WHAT IS ACTUALLY REGULATED IS THE CLAIM. As in
#  `yellow.probiotics_and_prebiotics`, a health claim requires authorisation
#  and none of the relevant ones have any, so products are sold on implication.
#  A test may report a genotype accurately and attach dietary advice that no
#  authority has assessed, because reporting a genotype and giving advice are
#  governed separately.
#
#  A THIRD, WHICH IS THE MOST CONSEQUENTIAL: THE DATA OUTLIVES THE PRODUCT. A
#  genome does not change, cannot be reissued, and identifies relatives who
#  never consented. That is why this facet's regulations include data
#  protection at all, and why `linkage.py` treats
#  `purple.genetic_data_privacy` as binding.
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
#  MATURITY = EMERGING, and this is the lowest value in the yellow branch. The
#  reasoning has to be careful, because part of this record is sixty years old.
#
#  The monogenic applications are ESTABLISHED beyond argument: newborn
#  screening has run at population scale since 1963. But those are clinical
#  genetics, and they are recorded here because they are gene-diet
#  interactions rather than because this field produced them.
#
#  What the record is actually about, the proposition that genotype can guide
#  ordinary dietary choices, has not been demonstrated. The trials are null,
#  the interactions do not replicate, and the most promising work in
#  personalised nutrition has moved away from genotype. A field selling a
#  capability it has not established is EMERGING, whatever its market size.
# -----------------------------------------------------------------------------
MATURITY = Maturity.EMERGING

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED, and the value reflects where the record's activity
#  legally sits rather than where much of it has operated in practice.
#
#  A genetic test is an in vitro diagnostic device requiring conformity
#  assessment, and clinical genetic testing requires professional oversight and
#  informed consent. The consumer wellness route has frequently avoided that,
#  which is the gap described in the header rather than a different tier.
#
#  Recording CONTROLLED would describe the gap as though it were the rule.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION, which is the correct value for two independent reasons.
#
#  The established applications are population screening programmes. And the
#  unestablished ones fail precisely because a population-level association
#  does not transfer to an individual: the effect sizes in `metrics.py` are
#  population statistics being sold as personal instructions.
#
#  Recording BENCH or FIELD would miss both.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. HEALTH is the primary label: the established applications are
#  clinical, the data is health data, and the harms are health harms. FOOD is
#  the subject matter. INFORMATION is claimed deliberately, because the product
#  of this record is data about a person that outlives any product, cannot be
#  reissued, and identifies relatives who never consented.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.HEALTH,
    Domain.FOOD,
    Domain.INFORMATION,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES, and the divergence is between the two halves of
#  the record rather than between countries.
#
#  A clinical genetic test is an authorised medical device with clinical
#  evidence requirements. A consumer dietary test has frequently been sold
#  outside that framework on the argument that it makes no medical claim, and
#  the position differs by jurisdiction and has been changing.
#
#  One technology, two regulatory worlds, and the boundary between them is a
#  marketing decision about what the test claims to be for.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by which half of the record it governs.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the test as a device ---------------------------------------------------
    "Regulation (EU) 2017/746 on in vitro diagnostic medical devices, which "
    "brought many genetic tests within scope regardless of the claim made and "
    "which narrowed the wellness exemption considerably",
    "Requirements for genetic counselling and informed consent attached to "
    "predictive genetic testing in several member states, which apply to the "
    "clinical route and frequently not to the consumer one",
    "United States regulation of laboratory developed tests and of "
    "direct-to-consumer genetic health risk reports, whose scope has been "
    "contested and repeatedly revised",
    # -- what may be claimed ------------------------------------------------------
    "Regulation (EC) No 1924/2006 on nutrition and health claims, under which "
    "the dietary claims attached to these tests have no authorisation, so "
    "products are sold on implication in the same way "
    "`yellow.probiotics_and_prebiotics` records",
    "Directive 2005/29/EC on unfair commercial practices, which is the "
    "instrument actually used against overstated personalisation claims",
    # -- the data, which outlives the product -------------------------------------
    "Regulation (EU) 2016/679, under which genetic data is a special category "
    "requiring explicit consent and heightened protection, and which applies "
    "whether the test was sold as clinical or as wellness",
    "National genetic non-discrimination provisions restricting the use of "
    "genetic information in insurance and employment, which vary widely and are "
    "absent in many jurisdictions",
    "Cross-border data transfer rules, which matter because consumer genomics "
    "is concentrated in a small number of companies operating internationally",
    # -- the laboratory ------------------------------------------------------------
    "Accreditation requirements for genetic testing laboratories, which govern "
    "whether a reported genotype is accurate and say nothing about whether the "
    "advice attached to it follows from it",
    # -- the research half -----------------------------------------------------------
    "Regulation (EU) No 536/2014 on clinical trials and equivalent frameworks, "
    "which govern the dietary intervention studies this record's claims should "
    "rest on",
    "Research ethics approval and biobank governance for the cohorts the field "
    "depends on",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what the field's own methodological failures
#  call for and what it has adopted unevenly.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- what would have prevented the replication problem ----------------------
    "Preregistration of analysis plans and replication in independent cohorts, "
    "which is the practice whose absence produced the interaction literature "
    "that did not survive testing",
    "Reporting guidelines for genetic association and gene-environment "
    "interaction studies, including explicit power calculation for the "
    "interaction rather than for the main effect",
    "CONSORT reporting for dietary intervention trials, and registration before "
    "enrolment",
    # -- interpreting a variant honestly -------------------------------------------
    "ACMG and equivalent variant classification frameworks, which distinguish "
    "pathogenic variants from those of uncertain significance and which "
    "consumer reports frequently do not apply",
    "Conventions requiring polygenic scores to be reported with the ancestry "
    "they were derived in and their performance in the population being tested",
    "Requirements to report effect sizes alongside associations, since an "
    "association reported without its magnitude conveys the existence of an "
    "effect and not its irrelevance",
    # -- the data ---------------------------------------------------------------------
    "ISO 15189 accreditation for medical laboratories",
    "Consent, retention, secondary use and deletion conventions for consumer "
    "genetic data, which are set by contract rather than by standard and which "
    "have changed with corporate ownership",
    # -- and the practice the evidence supports ----------------------------------------
    "Dietary guideline development conventions, which is what the established "
    "evidence actually supports and which this record's commercial layer "
    "positions itself against",
    "Multi-modal personalisation reporting, covering microbiome, behavioural "
    "and continuous monitoring inputs alongside any genetic ones, which is "
    "where the defensible version of personalised nutrition now sits",
)
