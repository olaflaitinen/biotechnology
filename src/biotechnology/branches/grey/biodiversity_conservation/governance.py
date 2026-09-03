# =============================================================================
#  biotechnology.branches.grey.biodiversity_conservation.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS RECORD IS GOVERNED BY MORE INTERNATIONAL LAW THAN ANYTHING ELSE IN THE
#  BRANCH, AND ALMOST NONE OF IT WAS WRITTEN WITH BIOTECHNOLOGY IN MIND.
#
#  Species protection, trade control and access to genetic resources are
#  treaty matters, negotiated between states over decades, and they apply to
#  this record because it moves biological material across borders. A
#  researcher taking a tissue sample from a threatened animal in another
#  country is operating inside three separate treaty regimes before any
#  laboratory work begins.
#
#      THE FRICTION IS NOT ACCIDENTAL. IT IS THE POINT.
#
#  Access and benefit sharing law exists because genetic material flowed for a
#  century out of species-rich countries into institutions in wealthy ones,
#  and the resulting knowledge and value stayed where it landed. This record
#  sits directly in that history: the expertise, the sequencing capacity and
#  the biobanks are concentrated in exactly the countries that are not
#  biodiverse. The permitting burden that researchers experience as an obstacle
#  is a deliberate correction, and the record says so rather than treating it
#  as red tape.
#
#  A SECOND POINT. THE HARDEST GOVERNANCE QUESTION HERE HAS NO REGIME AT ALL.
#  A gene drive is designed to spread through a wild population, which means it
#  does not respect a property boundary or a national one. Deliberate release
#  law was written for organisms that stay where they are put. No instrument
#  yet answers the question of who may consent to a release whose effects do
#  not stop at the border of the jurisdiction that authorised it.
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
#  MATURITY = COMMERCIAL, and the value needs its reasoning because the record
#  spans a wide range.
#
#  Population genomics, forensic identification and biobanking are routine,
#  institutionalised and used in statutory decisions. Genetic rescue has
#  documented successes and is applied deliberately. Those parts are mature.
#
#  Assisted reproduction works in a small number of species. Cloning and
#  interspecies surrogacy are demonstrations. Gene drives have never been
#  released and de-extinction has not occurred.
#
#  ESTABLISHED would credit the whole record with the maturity of its
#  analytical half. COMMERCIAL is the honest weighted value, with the
#  understanding that "commercial" here means routinely delivered by
#  institutions rather than sold: the field is funded by governments,
#  foundations and zoos rather than by a market.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = RESTRICTED, and this is the ONLY record in the grey branch to
#  carry the highest tier.
#
#  The justification is specific. Work on protected species is limited to
#  permitted persons and institutions: a licence names who may take, hold,
#  transport or perform procedures on the animal, and possessing the material
#  without it is an offence. Trade in listed species is restricted by treaty
#  with criminal enforcement. Access to genetic resources requires prior
#  informed consent from a source country. That is access limited to vetted
#  actors, which is exactly what RESTRICTED denotes in this library.
#
#  Note carefully what this tier is NOT about. The techniques are ordinary
#  molecular biology, no more hazardous than `red.molecular_diagnostics`. The
#  restriction attaches to the SUBJECT: an animal a treaty protects, and a
#  genetic resource another country owns.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.RESTRICTED

# -----------------------------------------------------------------------------
#  SCALE = POPULATION.
#
#  The unit of concern is a population: its effective size, its variation, its
#  connectivity, its trajectory. Every metric in `metrics.py` is a population
#  parameter, and interventions are judged by whether a population persisted.
#
#  This is the second POPULATION record in the branch, alongside
#  `grey.environmental_biomonitoring`, and the two are the branch's outward
#  facing pair for that reason.
# -----------------------------------------------------------------------------
SCALE = Scale.POPULATION

# -----------------------------------------------------------------------------
#  DOMAINS. Three.
#
#  ENVIRONMENT is the substance of the record.
#
#  GOVERNANCE is claimed on a stronger basis than in most records that claim
#  it. This work is conducted inside a dense treaty framework, its central
#  practical constraint is permitting rather than technique, and its most
#  significant unsolved problem, the release of a self-spreading genetic
#  element, is a governance problem with no technical component.
#
#  INFORMATION is claimed because sequence archives, reference genomes and
#  studbooks are the durable products of this field, and because a genome
#  archived is a form of preservation that outlives the material.
#
#  HEALTH IS DELIBERATELY NOT CLAIMED despite the pathogen surveillance
#  applications. Those exist to protect wildlife populations, which is the
#  ENVIRONMENT claim already made, and stretching them into a human health
#  domain would be exactly the padding rule 12 guards against.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.ENVIRONMENT,
    Domain.GOVERNANCE,
    Domain.INFORMATION,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED.
#
#  Permits are granted in advance and name the holder, the species, the
#  procedure and the material. Export, import and access to genetic resources
#  each require separate prior authorisation. Nothing here proceeds on
#  notification.
#
#  For the gene drive and de-extinction proposals the honest status would be
#  that no framework yet exists, which is recorded in REGULATIONS rather than
#  in this value, since the value describes the practice as it is conducted.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by treaty regime. Access and benefit sharing is placed
#  first because it is the one this record most often collides with and the
#  one whose purpose is most often misread as bureaucracy.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- who owns genetic material, and who benefits from it --------------------
    "The Convention on Biological Diversity, which established that states have "
    "sovereign rights over their genetic resources and thereby ended the "
    "assumption that biological material collected abroad was free to use",
    "The Nagoya Protocol on access and benefit sharing, requiring prior "
    "informed consent from the source country and mutually agreed terms for the "
    "use of genetic resources and associated traditional knowledge",
    "National access and benefit sharing legislation implementing the above, "
    "which is what a researcher actually applies under and which varies "
    "substantially between countries",
    "Digital sequence information provisions under negotiation, which address "
    "whether a published genome sequence carries the same obligations as the "
    "physical sample it came from, and which matter because sequencing has made "
    "the physical sample optional",
    "Traditional knowledge protection provisions, which apply where a species "
    "or its use was documented by a community before any researcher arrived",
    # -- what may be taken, held and moved --------------------------------------
    "CITES, which restricts international trade in listed species and applies "
    "to tissue, gametes and derivatives as well as to whole animals",
    "National endangered species legislation, which limits taking, possessing "
    "and performing procedures on listed species to permitted persons and makes "
    "unpermitted possession an offence",
    "The Habitats Directive 92/43/EEC and Birds Directive 2009/147/EC, which "
    "impose strict protection and surveillance obligations in the European "
    "Union",
    "Import, export and phytosanitary controls on biological material, and "
    "veterinary certification for animal tissue and germplasm",
    "Biosecurity requirements governing movement of organisms between regions, "
    "including quarantine for translocated animals",
    # -- the animals as subjects ---------------------------------------------------
    "Animal welfare legislation governing procedures on protected animals, "
    "including Directive 2010/63/EU, which applies to capture, anaesthesia, "
    "biopsy and assisted reproduction",
    "Ethical review requirements for procedures on wild animals, which are "
    "separate from and additional to the conservation permits above",
    # -- releasing anything modified -------------------------------------------------
    "Deliberate release requirements for genetically modified organisms, "
    "including Directive 2001/18/EC, which is the framework the blight-resistant "
    "chestnut is being assessed under and which was written for organisms that "
    "stay where they are put",
    "The Cartagena Protocol on Biosafety, governing transboundary movement of "
    "living modified organisms",
    "Absence of any adequate framework for self-propagating genetic elements, "
    "since a gene drive is designed to spread and no instrument answers who may "
    "consent to a release whose effects do not stop at the authorising "
    "jurisdiction's border",
    # -- and the decisions about what to protect ---------------------------------------
    "Listing and conservation status assessment procedures, which determine what "
    "receives protection and which now rest substantially on the genetic unit "
    "definitions this record produces",
    "Reintroduction and translocation authorisation, which is required before "
    "any genetic rescue or assisted relocation proceeds",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what turns a genetic result into a management
#  decision, which is where this field does its real work.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- turning genetics into decisions ----------------------------------------
    "IUCN Red List categories and criteria, which are the shared framework for "
    "assessing extinction risk and are increasingly informed by effective "
    "population size rather than by headcount alone",
    "IUCN guidelines for reintroductions and conservation translocations, which "
    "are the reference for whether a genetic rescue or an assisted relocation "
    "is defensible",
    "Conservation unit and evolutionarily significant unit delineation "
    "conventions, which decide what is being protected and which molecular data "
    "has repeatedly revised",
    "Population viability analysis conventions, which combine demographic and "
    "genetic parameters into a projection that a management decision can be "
    "argued over",
    "Genetic management guidance for captive populations, including target "
    "retention of genetic diversity over a stated horizon",
    # -- keeping material, and keeping it usable --------------------------------
    "Biobank operating standards covering sample provenance, redundancy, "
    "distributed duplicate storage and long-term custody arrangements",
    "Cryopreservation protocol validation and post-thaw viability testing, "
    "since material stored without a viable protocol is a sample rather than an "
    "option",
    "Cell line authentication and contamination testing, which matters more "
    "here than elsewhere because the source animal may no longer exist to "
    "resample",
    "Studbook and pedigree management conventions integrating molecular "
    "relatedness across institutions",
    # -- making the data usable by anyone else -----------------------------------
    "Reference genome assembly and annotation standards, including the quality "
    "criteria adopted by coordinated sequencing initiatives",
    "Sequence data deposit, metadata and FAIR data practice, which determines "
    "whether a dataset can be reinterpreted decades later",
    "Sample and specimen voucher standards linking genetic data to a physical "
    "specimen, which is the connection molecular results depend on and that "
    "reference databases are built from",
    "Forensic genetics validation and chain of custody practice for wildlife "
    "trade casework, which must meet evidential rather than research standards",
    # -- and doing the work fairly ------------------------------------------------
    "Equitable research partnership and capacity building practice, which is "
    "the practical counterpart to the access and benefit sharing law above and "
    "the difference between compliance and collaboration",
    "Data sovereignty and community consent frameworks for genetic work on "
    "species of cultural significance",
    "Responsible communication guidance for de-extinction and gene drive "
    "research, which exists because overstatement in this field has a specific "
    "cost: it weakens the case for prevention",
)
