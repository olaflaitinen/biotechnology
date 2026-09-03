# =============================================================================
#  biotechnology.branches.blue.marine_natural_products.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record sits under two complete regulatory systems that were designed
#  independently and meet only here, and the collision is the interesting part.
#
#  MEDICINES LAW governs what the compound becomes. From the moment a marine
#  extract is developed towards a therapy it is a medicinal product like any
#  other, with the same trials, the same dossier and the same manufacturing
#  requirements. Nothing about marine origin earns any concession, and nothing
#  about it should.
#
#  BIODIVERSITY AND LAW OF THE SEA GOVERN WHERE IT CAME FROM. Access requires
#  the consent of the state whose waters were sampled, benefit sharing
#  obligations attach to the sample and to the sequence derived from it,
#  protected species and protected areas have their own regimes, and for the
#  high seas there was no rule at all until 2023.
#
#  THE COLLISION IS TEMPORAL. A medicine takes fifteen to twenty-five years
#  from collection to approval, which is longer than the interval over which
#  the access rules themselves changed. Material collected lawfully in 1985 was
#  collected before the Convention on Biological Diversity existed; material
#  collected in 2005 predates the Nagoya Protocol; material from the high seas
#  predates the 2023 agreement. A company developing a compound today may hold
#  a library assembled under three successive legal regimes, none applied
#  retroactively and none providing a clean answer.
#
#  That is not a hypothetical difficulty. It is the practical reason several
#  programmes were abandoned, and it is recorded here rather than in a footnote.
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
#  MATURITY = COMMERCIAL, and the value needs its qualification stated.
#
#  Marketed medicines exist, in several therapeutic areas, some approved for
#  more than a decade and one for more than fifty years. That is beyond PILOT
#  by any reading.
#
#  It is not ESTABLISHED, because the pipeline that produced them is not
#  functioning. Large pharmaceutical companies withdrew from natural product
#  discovery in the 1990s and did not return, the supply problem defeats most
#  candidates before development, and the number of marine-derived approvals
#  remains in single figures. A field with real products and a broken pathway
#  to more of them is COMMERCIAL.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED. A national agency decides before the product may be
#  sold, which is the definition. The compounds are medicines, assessed and
#  authorised as medicines.
#
#  Note that the collection end of the same activity would sit at CONTROLLED,
#  matching `blue.marine_genomics`, since it turns on permits rather than
#  approvals. The tier records the activity at its most demanding point.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = BENCH, which is unusual for a record with marketed products and is
#  deliberate.
#
#  The characteristic unit of this discipline is milligrams. Structures are
#  elucidated on sub-milligram quantities, screens run on microlitres, and the
#  entire supply problem exists precisely BECAUSE the scale never rises. Once a
#  compound is manufactured at tonnage it has become a pharmaceutical
#  manufacturing question and belongs to `red.pharmaceutical_biotechnology`,
#  not here.
#
#  Recording INDUSTRIAL would describe the destination rather than the
#  discipline, and would hide the constraint the record is built around.
# -----------------------------------------------------------------------------
SCALE = Scale.BENCH

# -----------------------------------------------------------------------------
#  DOMAINS. HEALTH is the sector without argument. ENVIRONMENT is claimed not
#  as a benefit but because the activity acts on habitats: collection damages
#  what it samples, and the access regime is an environmental instrument rather
#  than a health one. INFORMATION is claimed for the chemical libraries,
#  structural databases and genome-mining catalogues, which outlive most of the
#  programmes that generated them and are the field's most durable output.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.HEALTH,
    Domain.ENVIRONMENT,
    Domain.INFORMATION,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. The products are authorised medicines. The
#  collection activity upstream is NOTIFIED in character, as
#  `blue.marine_genomics` records, but the status of a record should reflect
#  what it ultimately places on a market.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by which of the two systems it belongs to. The grouping
#  is the point of this facet.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- system one: what the compound becomes ---------------------------------
    "Directive 2001/83/EC and Regulation (EC) No 726/2004, under which a "
    "marine-derived compound is a medicinal product with no concession for its "
    "origin",
    "Regulation (EU) No 536/2014 on clinical trials",
    "EudraLex Volume 4 Good Manufacturing Practice, Part II, for the active "
    "substance however it is finally supplied",
    "Regulation (EC) No 141/2000 on orphan medicinal products, which is the "
    "practical route to market for several compounds in this record given "
    "small indications",
    "ICH Q3D on elemental impurities and ICH Q3C on residual solvents, which "
    "bear on semisynthetic and total synthesis routes",
    # -- system two: where it came from ------------------------------------------
    "The Convention on Biological Diversity and the Nagoya Protocol, under "
    "which access requires prior informed consent and mutually agreed terms, "
    "and benefit sharing attaches to the sequence as well as the sample",
    "Regulation (EU) No 511/2014, imposing due diligence and record-keeping on "
    "users within the Union",
    "The United Nations Convention on the Law of the Sea, which determines "
    "whose consent is needed and where",
    "The 2023 Agreement on marine biological diversity of areas beyond "
    "national jurisdiction, which addresses high seas genetic resources "
    "prospectively and not retroactively",
    # -- what may be collected at all ---------------------------------------------
    "CITES, and national protected species and marine protected area "
    "legislation, which restrict collection of several organisms of interest",
    "Deep sea and vulnerable marine ecosystem protection measures, which "
    "constrain the habitats that have proved most chemically productive",
    # -- moving material across borders ---------------------------------------------
    "Biosecurity and phytosanitary controls on transporting biological samples "
    "between jurisdictions",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group exists because this field's characteristic error is
#  publishing a compound that was already known, or a structure that is wrong.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- not describing the same molecule twice --------------------------------
    "Dereplication practice against natural product databases before "
    "structure elucidation is undertaken, which is what separates discovery "
    "from rediscovery",
    "Journal requirements for full spectroscopic characterisation and for "
    "deposition of raw spectra, adopted after repeated structural revisions of "
    "published marine compounds",
    "Absolute configuration determination conventions, since a reported "
    "structure with the wrong stereochemistry sends a synthetic programme after "
    "a molecule that does not exist",
    # -- being able to say what the source was -----------------------------------
    "Voucher specimen deposition in a recognised collection, without which the "
    "source organism cannot be reidentified and a result cannot be reproduced",
    "Taxonomic verification by a specialist, since misidentification of the "
    "source invalidates the ecological and biosynthetic reasoning built on it",
    # -- making the pharmacology comparable ---------------------------------------
    "Assay reporting conventions covering cell line, incubation time and serum "
    "conditions, without which the potency figures in `metrics.py` cannot be "
    "compared between publications",
    "Reference standard and purity reporting for material used in biological "
    "testing",
    # -- collecting responsibly ----------------------------------------------------
    "Codes of practice on sampling intensity and habitat impact, which the "
    "screening programmes of the 1970s and 1980s did not have",
    "Institutional access and benefit sharing policies, including the treatment "
    "of legacy collections assembled under earlier legal regimes",
    "Research partnership norms against helicopter science, under which "
    "scientists from the sampled region are co-investigators rather than a "
    "collection service",
)
