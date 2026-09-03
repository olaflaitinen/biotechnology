# =============================================================================
#  biotechnology.branches.white.cell_free_biomanufacturing.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record contains the most interesting governance finding in the white
#  branch, and it is a GAP rather than a rule.
#
#  THE REACTION CONTAINS NOTHING ALIVE, SO THE FRAMEWORKS DO NOT APPLY TO IT.
#  Contained use, deliberate release and the whole apparatus of genetically
#  modified organism law are written around a LIVING modified organism capable
#  of replication and transfer. A tube of extract and DNA is none of those
#  things. It cannot grow, cannot persist in an environment, and cannot pass
#  anything to a wild population. So the reaction itself falls outside rules
#  that govern every other record in this branch, which is why cell-free kits
#  can be used in a classroom that could not host a contained use facility.
#
#  THIS IS NOT A LOOPHOLE AND IT IS NOT A SAFETY GUARANTEE. It is an accurate
#  regulatory consequence of a genuine physical difference, and it moves the
#  control point rather than removing it. A cell-free system is PROGRAMMED WITH
#  NUCLEIC ACID, so what determines what it can produce is the DNA supplied to
#  it. Screening synthesised DNA orders therefore does work here that
#  organism-based controls do for the rest of the branch, and that is where the
#  oversight has to sit.
#
#  ONE QUALIFICATION MATTERS AND IS EASY TO MISS. The extract is made from
#  cells, frequently engineered ones, grown conventionally. Contained use rules
#  apply in full to producing the reagent even though they do not apply to
#  using it. The technology sits downstream of the regime rather than outside
#  it.
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
#  MATURITY = PILOT, and this is the only record in the white branch below
#  COMMERCIAL. The value is deliberate and the split behind it should be stated.
#
#  As a RESEARCH REAGENT the technology is entirely established: kits are sold
#  in volume, the method is a century old, and it was the instrument of two
#  foundational discoveries. As a MANUFACTURING PLATFORM it remains at
#  demonstration scale, in tens to hundreds of litres, with few products on the
#  market.
#
#  This record is about manufacturing, so PILOT is the honest value. Recording
#  it as COMMERCIAL because reagent kits sell well would repeat exactly the
#  overstatement that `history.py` documents as this field's characteristic
#  failing.
# -----------------------------------------------------------------------------
MATURITY = Maturity.PILOT

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED, and the reasoning is more interesting than the
#  value.
#
#  The REACTION would arguably be ROUTINE: nothing in it is alive, it cannot
#  replicate or escape, and it is used in classrooms. But the EXTRACT must be
#  manufactured from cultured cells that are frequently engineered, and that
#  production step requires the same contained use permit as anything else in
#  this branch.
#
#  CONTROLLED reflects the activity as actually practised, which includes
#  making the reagent. A reader interested only in using a purchased extract
#  should understand that the tier they face is lower than the one recorded
#  here, and that the difference is the point.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = BENCH. This is the only record in the white branch not at INDUSTRIAL
#  scale, and the value is a substantive claim rather than an oversight.
#
#  The characteristic unit of this technology is a reaction of microlitres to
#  litres, and its largest demonstrations reach tens to hundreds of litres
#  against the hundreds of cubic metres routine in
#  `white.microbial_fermentation`. Its most distinctive application, a
#  freeze-dried reaction on a paper disc, is smaller still. Recording BENCH is
#  what makes the contrast with the rest of the branch legible.
# -----------------------------------------------------------------------------
SCALE = Scale.BENCH

# -----------------------------------------------------------------------------
#  DOMAINS. HEALTH covers on-demand biologics and the field diagnostics that
#  are this record's strongest application. MATERIALS covers protein and enzyme
#  production and the prototyping that supports the rest of the branch.
#
#  SECURITY is claimed on two distinct grounds rather than as a gesture:
#  field-deployable detection of outbreak pathogens is a preparedness
#  capability, and the governance gap described above makes DNA synthesis
#  screening the operative control point, which is a security question rather
#  than a safety one.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.HEALTH,
    Domain.MATERIALS,
    Domain.SECURITY,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = VARIES. The technique has no status of its own. A
#  research reagent is essentially unregulated, a diagnostic is a medical
#  device, an on-demand biologic is a medicine manufactured under GMP, and an
#  educational kit is a consumer product. The same tube meets four different
#  regimes depending on what is being asked of it.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.VARIES


# =============================================================================
#  REGULATIONS
#  Binding law. Note which instruments are ABSENT: the deliberate release
#  regime does not appear, and its absence is the record's governance finding.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- what applies to making the reagent, not to using it -------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, which applies in full to culturing the cells that the "
    "extract is made from and not to the cell-free reaction itself",
    "Directive 2000/54/EC on biological agents at work, for the same production "
    "step",
    # -- what applies to the product, which depends entirely on the product -----
    "Regulation (EU) 2017/746 on in vitro diagnostic medical devices, under "
    "which a cell-free sensor intended to inform a clinical decision is a "
    "regulated device",
    "EudraLex Volume 4 Good Manufacturing Practice, where the reaction produces "
    "a medicinal product, including at the point of care",
    "Regulation (EC) No 1907/2006 REACH for reagent components placed on the "
    "market as chemicals",
    # -- what applies because the system is programmed by DNA --------------------
    "Export control and dual-use regulations applying to genetic sequences of "
    "concern rather than to organisms, which is where oversight of this "
    "technology necessarily sits",
    "National biosecurity provisions on the possession and synthesis of listed "
    "agent sequences, which apply to the template even though nothing in the "
    "reaction is alive",
    # -- what applies where it is deployed ---------------------------------------
    "Requirements for diagnostics used outside a laboratory setting, including "
    "instructions, interpretation and result reporting, which govern the "
    "record's most distinctive application",
    "Clinical trial and ethics approval where field diagnostics are evaluated "
    "on human samples",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is the one this record most needs and least has.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the standards the field is missing ------------------------------------
    "Reporting conventions for extract preparation, composition and "
    "batch-to-batch performance, which are not yet consistently applied and "
    "whose absence is the largest obstacle to regulated use of these systems",
    "Reference materials and positive controls allowing yields to be compared "
    "between laboratories, without which a published titre is not a "
    "reproducible claim",
    # -- describing the instruction unambiguously --------------------------------
    "Synthetic Biology Open Language and standard part registries for "
    "describing the genetic template",
    "Minimum information conventions for reporting synthetic circuits and their "
    "performance",
    # -- screening the instruction ------------------------------------------------
    "International Gene Synthesis Consortium screening protocols for "
    "synthesised DNA orders, which are voluntary and are the operative control "
    "on what a cell-free system can be asked to produce",
    "Institutional review of sequences of concern, applied to templates rather "
    "than to organisms",
    # -- making the product acceptable ---------------------------------------------
    "ISO 13485 and IEC 62304 where a cell-free diagnostic is developed as a "
    "device",
    "ISO 15189 and point-of-care testing guidance for results generated outside "
    "a laboratory",
    "Good Manufacturing Practice expectations for reagents used in the "
    "manufacture of a medicinal product",
    # -- storage and transport ------------------------------------------------------
    "Stability testing conventions for lyophilised biological reagents, which "
    "are what substantiate the ambient shelf life claim in `metrics.py`",
)
