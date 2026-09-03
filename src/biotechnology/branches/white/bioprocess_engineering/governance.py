# =============================================================================
#  biotechnology.branches.white.bioprocess_engineering.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record carries the strongest version of an idea that appears nowhere
#  else in the library in quite this form:
#
#      FOR A BIOLOGICAL PRODUCT, THE PROCESS IS THE PRODUCT.
#
#  A small molecule can be fully characterised. Its identity is a structure,
#  and two batches made by different routes can be shown to be the same
#  substance. A large biological molecule cannot be characterised to that
#  standard. Glycosylation patterns, charge variants, aggregation and higher
#  order structure depend on how the cells were grown and how the molecule was
#  purified, and analytical methods cannot fully enumerate what may differ.
#
#  The regulatory consequence is severe and is the defining constraint of this
#  discipline. A change to the manufacturing process is treated as a potential
#  change to the product, and must be supported by a comparability exercise
#  showing that the molecule has not been altered in any way that matters.
#  Improvements are therefore expensive to deploy, and a plant can find itself
#  running a process it knows how to better, because proving the better one
#  equivalent costs more than the improvement returns.
#
#  This is why `white.biocatalysis` records a route locked into a dossier, and
#  why this record goes further: there, the route is approved; here, the route
#  IS the definition of what is being sold.
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
#  MATURITY = ESTABLISHED. A profession since 1943, with settled transport
#  theory, standard unit operations and a validated regulatory framework.
#  Continuous processing and intensification are active areas within it, but
#  the discipline itself is not emerging in any sense.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = REGULATED, and this is one step above its two neighbouring
#  records, which are CONTROLLED. The difference is deliberate.
#
#  A national agency does not merely permit this activity; it approves the
#  specific process, inspects the facility, and must be satisfied before the
#  product may be sold. Process validation, comparability after change and
#  pre-approval inspection are agency decisions taken about the process itself.
#  That is precisely what REGULATED denotes, and it follows directly from the
#  process being the product.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.REGULATED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit of operation is a manufacturing facility.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. HEALTH is placed first because the regulatory weight, the cost
#  structure and the failure consequences described in this record are all
#  driven by biopharmaceutical manufacture. MATERIALS and FOOD cover the same
#  engineering applied where the stakes and the rules are different.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.HEALTH,
    Domain.MATERIALS,
    Domain.FOOD,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED, and here the value has an unusually literal
#  meaning. In its principal application the process itself is what an agency
#  authorises: the facility is inspected, the validation is assessed, and the
#  process description in the dossier is binding. Changing it requires
#  approval, not notification.
#
#  Note the contrast with the two neighbouring records, which are VARIES. They
#  are enabling operations whose status depends on the product. This one is
#  approved as such, because the process is the product.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by what each instrument governs.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- the process and the facility -----------------------------------------
    "EudraLex Volume 4 Good Manufacturing Practice, Parts I and II, and Annex "
    "1 on the manufacture of sterile medicinal products, which is the most "
    "demanding single document most of these facilities work to",
    "United States 21 CFR Parts 210 and 211, and Part 600 for biological "
    "products",
    "Regulation (EC) No 1234/2008 on variations, which is the instrument that "
    "makes a process improvement expensive to deploy once approved",
    # -- data and records -------------------------------------------------------
    "21 CFR Part 11 and Annex 11 on electronic records and signatures, which "
    "govern the process control and data historian systems these plants depend "
    "on",
    # -- the equipment as machinery --------------------------------------------
    "Directive 2014/68/EU on pressure equipment, for sterilisable vessels "
    "operated above atmospheric pressure",
    "Directive 2006/42/EC on machinery, and Directive 1999/92/EC on explosive "
    "atmospheres where solvents or dusts are handled",
    # -- the plant as an installation -------------------------------------------
    "Directive 2010/75/EU on industrial emissions, and national discharge "
    "consents for spent broth and process water",
    # -- the organism ------------------------------------------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, and Directive 2000/54/EC on biological agents at work",
    # -- what goes in the product ------------------------------------------------
    "Regulation (EU) 2017/745 and food contact material rules as applicable to "
    "single-use components, whose extractables and leachables must be assessed "
    "because the plastic touches the product",
)


# =============================================================================
#  STANDARDS
#  Not law, and in this record the distinction is thin: an ICH guideline is
#  formally guidance and is followed as though it were binding, because a
#  dossier that departs from it must justify the departure.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- proving the molecule did not change ------------------------------------
    "ICH Q5E on comparability of biotechnological products subject to changes "
    "in their manufacturing process, which is the document behind this "
    "record's central governance idea",
    "ICH Q6B on specifications for biotechnological products, and ICH Q5A on "
    "viral safety evaluation, under which the clearance factors in `metrics.py` "
    "are established",
    # -- designing quality in rather than testing it afterwards ------------------
    "ICH Q8 on pharmaceutical development and the design space concept",
    "ICH Q9 on quality risk management and ICH Q10 on the pharmaceutical "
    "quality system",
    "ICH Q11 on development and manufacture of drug substances",
    "ICH Q13 on continuous manufacturing, which addresses how a batch may be "
    "defined for a process that has no natural batch boundary",
    "ICH Q14 on analytical procedure development, since a process can only be "
    "controlled as well as it can be measured",
    # -- validation as a lifecycle rather than an event ---------------------------
    "Process validation guidance in three stages, from process design through "
    "performance qualification to continued verification in routine production",
    "Cleaning validation and campaign changeover expectations, which is where "
    "cross-contamination between products is actually prevented",
    # -- how the plant is built ---------------------------------------------------
    "American Society of Mechanical Engineers Bioprocessing Equipment "
    "standards for hygienic design, surface finish, drainability and "
    "weld quality",
    "ISO 14644 cleanroom classification, and ISO 13408 on aseptic processing",
    "Bio-Process Systems Alliance and pharmacopoeial guidance on extractables "
    "and leachables from single-use systems",
    # -- what may be claimed environmentally ---------------------------------------
    "ISO 14040 and ISO 14044 life cycle assessment, which is how the trade "
    "between single-use plastic waste and the water and energy of cleaning is "
    "actually settled rather than asserted",
)
