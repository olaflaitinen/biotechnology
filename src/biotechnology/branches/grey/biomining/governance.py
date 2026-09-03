# =============================================================================
#  biotechnology.branches.grey.biomining.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE GOVERNING PROBLEM HERE IS THAT THE LIABILITY OUTLASTS EVERY INSTITUTION
#  THAT COULD BEAR IT.
#
#  Acid generation from sulphide material is self-sustaining and continues for
#  centuries. No mining company lasts that long. Neither does a bond, an
#  insurance policy, or in many cases the regulatory agency that issued the
#  permit. So the central instrument in this facet is not an emission limit; it
#  is FINANCIAL ASSURANCE: money set aside at the start against an obligation
#  nobody present will be alive to discharge.
#
#      THE REGULATION IS AN ATTEMPT TO BIND A CENTURY-SCALE PROBLEM WITH
#      DECADE-SCALE INSTITUTIONS, AND IT IS ROUTINELY UNDERFUNDED.
#
#  That is stated plainly rather than softened, because the historic record of
#  abandoned acid-generating sites transferred to public ownership is the
#  evidence, and it is extensive.
#
#  A SECOND POINT. NONE OF THIS IS BIOTECHNOLOGY REGULATION. The organisms are
#  indigenous, unmodified and already present in the ore. What is regulated is
#  mining, water and closure. A reader looking for biosafety provisions will
#  find none, and that absence is correct.
#
#  A THIRD, SPECIFIC TO GOLD. Biooxidation of arsenopyrite mobilises arsenic,
#  and the biooxidised residue feeds a cyanide circuit. So a gold operation
#  carries two of the most heavily regulated substances in industrial practice
#  as a direct consequence of using this technique.
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
#
#  Heap bioleaching produces a substantial share of world copper, biooxidation
#  is the standard pretreatment for refractory gold, and both have operated
#  commercially for decades with design codes, contractors and a supplier
#  industry. The practice is older still if the pre-microbiological heap
#  leaching in `history.py` is counted.
#
#  The 1998 setback and the confinement of the economics to a few metals do not
#  reduce the value. A scope is not an immaturity.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED.
#
#  A mining permit, a water abstraction and discharge permit, a closure plan and
#  financial assurance are all required before operation, and the closure
#  obligation persists after it. Gold operations additionally carry cyanide and
#  arsenic controls.
#
#  RESTRICTED was considered and rejected. Access is not limited to vetted
#  actors: any competent operator may apply. The intensity is high and the
#  gate is a permit rather than a person.
#
#  Note again that this tier reflects governance intensity rather than the
#  organisms, which are indigenous, unmodified and already in the rock.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL.
#
#  Heaps are measured in millions of tonnes on engineered lined pads, with
#  irrigation systems, solution ponds, aeration and recovery circuits, operated
#  continuously for years. Stirred tank biooxidation is a conventional process
#  plant.
#
#  FIELD was considered because a heap sits under open sky and is subject to
#  weather. It was rejected: the pad is engineered, lined and drained, and the
#  solution is collected. The distinction from `grey.phytoremediation`, which is
#  FIELD, is precisely that there is a liner.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. Three.
#
#  MATERIALS is placed first and is the primary label. This record produces
#  copper, gold, nickel and cobalt, which is a materials output in the plainest
#  sense and is what distinguishes it from every other record in this branch.
#
#  ENVIRONMENT is claimed in both directions and honestly. The technique avoids
#  the sulphur dioxide emission of smelting and recovers metal from material
#  already excavated; and it is the acid mine drainage reaction, so containment
#  failure and closure are environmental matters of the first order.
#
#  ENERGY is claimed narrowly, because operating at ambient temperature instead
#  of in a furnace is a large difference in energy per unit of metal and
#  because the record's commercial case rests partly on it.
#
#  HEALTH IS DELIBERATELY NOT CLAIMED, although arsenic and cyanide appear in
#  `REGULATIONS`. Those are hazards the operation must control, not health
#  outcomes it delivers, and the distinction is the one
#  `grey.biowaste_treatment` applies to pathogen reduction.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.ENVIRONMENT,
    Domain.ENERGY,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED.
#
#  Mining and water permits are granted before operation, with conditions, and
#  a closure plan is approved as part of them. That is prior authorisation of a
#  specific activity at a specific place.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law. Closure and financial assurance come first, because that is
#  where the record's real governance problem sits.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the obligation that outlasts everyone ----------------------------------
    "Mine closure and rehabilitation plan approval as a condition of the "
    "operating permit, covering neutralisation, capping and long-term drainage "
    "management of residual heaps",
    "Financial assurance and reclamation bonding requirements, which set aside "
    "money at the start against an acid generation obligation that persists for "
    "centuries, and which are the central instrument of this facet",
    "Post-closure monitoring and treatment obligations, which continue after "
    "the operation ends and frequently after the operating company does",
    "Liability transfer and orphan site provisions, which determine what "
    "happens when a company fails before its closure obligation is discharged, "
    "and whose historic record is extensive",
    # -- the waste and the water --------------------------------------------------
    "The Extractive Waste Directive 2006/21/EC and equivalent regimes, which "
    "govern the management of waste rock, tailings and heap residues and "
    "require characterisation of acid generation potential",
    "Water abstraction licensing, which in arid regions puts a heap leaching "
    "operation in direct competition with agricultural and community supply",
    "Discharge permits and receiving water standards for seepage and process "
    "solution, including the Water Framework Directive 2000/60/EC",
    "Groundwater protection requirements, which are the governing constraint on "
    "in situ leaching where there is no pad and no liner at all",
    "Pad liner design, leak detection and containment standards, which are "
    "what separate this technique from the pollution it is chemically identical "
    "to",
    # -- the two substances a gold operation acquires ------------------------------
    "Arsenic emission, disposal and stabilisation requirements, which arise "
    "directly from arsenopyrite oxidation and which govern refractory gold "
    "operations",
    "Cyanide management regulation and the International Cyanide Management "
    "Code, which apply to the circuit that biooxidation exists to feed",
    "Hazardous substance transport, storage and reporting obligations for both "
    "of the above",
    # -- the site and the people --------------------------------------------------
    "Environmental and social impact assessment requirements preceding a mining "
    "permit, including cumulative effects on water availability",
    "Free prior and informed consent obligations under ILO Convention 169 and "
    "national equivalents where operations affect indigenous territories",
    "Mine safety legislation, and occupational exposure controls for acid mist, "
    "arsenic and cyanide",
    "Air quality regulation, which is the comparison that favours this record, "
    "since the sulphur dioxide limits that constrain smelting do not arise here",
    # -- and what is absent -------------------------------------------------------
    "Absence of biosafety or contained use requirements, since the organisms "
    "are indigenous, unmodified and already present in the ore, which is why a "
    "reader will find no biotechnology regulation in this record",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group predicts what the material will do after closure,
#  which is the question the whole facet turns on.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- predicting the century-scale behaviour --------------------------------
    "Acid base accounting and net acid generation test methods, which establish "
    "before mining begins whether residual material will generate acid "
    "indefinitely",
    "Kinetic humidity cell and field barrel test protocols, which measure the "
    "rate of that generation rather than only its potential",
    "Geochemical characterisation and block modelling of acid generation "
    "potential across a deposit, which is how waste rock is segregated during "
    "operation rather than after it",
    "Long-term drainage prediction and closure design guidance, including cover "
    "system performance assessment",
    # -- knowing whether the ore will leach at all ------------------------------
    "Column and crib leach test protocols, and the reporting conventions that "
    "keep a column result legible as an upper bound rather than a projection, "
    "which is what the 1998 setback in `history.py` turned on",
    "Mineralogical characterisation including automated mineralogy, which "
    "identifies the passivation and liberation behaviour a solution assay "
    "cannot see",
    "Metallurgical accounting and reconciliation standards, which distinguish "
    "metal leached from metal reporting to the recovery circuit",
    # -- running the heap ---------------------------------------------------------
    "Heap construction, agglomeration and stacking practice, which determines "
    "whether solution and air reach the whole pile or channel through part of "
    "it",
    "Solution chemistry monitoring conventions for acidity, iron speciation and "
    "dissolved metals",
    "Aeration system design guidance for heap bases, which addresses the "
    "process's usual rate limitation",
    "Inoculum preparation and adaptation practice, which is one of the "
    "legitimate augmentation cases discussed in `grey.bioaugmentation`, since "
    "freshly stacked ore has no established community",
    # -- reporting it to people who are not in the room ---------------------------
    "Mineral resource and reserve reporting codes such as JORC and NI 43-101, "
    "which govern how recovery assumptions may be presented to investors and "
    "which exist because of shortfalls of the kind recorded for 1998",
    "Global Industry Standard on Tailings Management, and equivalent facility "
    "governance frameworks",
    "Life cycle assessment conventions under ISO 14040 and ISO 14044, applied "
    "with smelting as the comparison and with closure emissions included, since "
    "omitting the post-closure term flatters the result substantially",
    "Sustainability and responsible sourcing assurance schemes for produced "
    "metal, which is where a downstream purchaser encounters this record",
)
