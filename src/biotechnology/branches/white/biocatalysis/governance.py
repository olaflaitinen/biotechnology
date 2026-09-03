# =============================================================================
#  biotechnology.branches.white.biocatalysis.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record's governance is unusual in the library because THE REGULATED
#  THING IS THE ROUTE, NOT THE PRODUCT. A biocatalytic step makes an ordinary
#  small molecule, chemically identical to the same molecule made any other
#  way. There is no separate approval for a molecule because an enzyme made it.
#
#  What is regulated is the MANUFACTURING PROCESS as described in the
#  marketing authorisation dossier. Under ICH Q11 the synthetic route, the
#  starting materials and the control strategy are part of what an agency
#  approves, and changing an approved step requires a variation, with data and
#  with time. This is why `practice.CHALLENGES` lists the regulatory lock as a
#  genuine constraint rather than as paperwork: the decision to go enzymatic is
#  effectively made once, before the first pivotal batch, and is then fixed for
#  the commercial life of the product. A better enzyme discovered in year six
#  is frequently not worth the variation.
#
#  A SECOND POINT, AND A PLEASANT ONE. Biocatalysis is one of the few
#  technologies in this library that makes a regulatory burden SMALLER. ICH
#  Q3D sets limits on elemental impurities, and a route that never uses a
#  rhodium, palladium or ruthenium catalyst has no such impurity to control,
#  test for or remove. Removing the metal removes the specification with it.
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
#  MATURITY = COMMERCIAL, and this is deliberately one step below
#  `white.industrial_enzymes`, which is ESTABLISHED. The difference is not an
#  oversight.
#
#  Hydrolase chemistry is established beyond argument: penicillin acylase has
#  run at tens of thousands of tonnes a year since the 1970s. But the reaction
#  classes that make the field interesting now, meaning redox chemistry,
#  transaminations, carbon-carbon bond formation and cascades, are in active
#  commercial adoption rather than settled practice, and a large majority of
#  synthetic steps in industry remain chemical. COMMERCIAL is the honest value
#  for the field as a whole.
# -----------------------------------------------------------------------------
MATURITY = Maturity.COMMERCIAL

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED. The vocabulary measures governance intensity rather
#  than danger. A permit is needed because the catalyst is produced by a
#  genetically modified microorganism under contained use, and pharmaceutical
#  application brings GMP oversight of the site.
#
#  It is not REGULATED, because no agency approves biocatalysis as such. What
#  an agency approves is a specific route inside a specific product dossier,
#  which is a property of that product rather than of this technology.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit of operation is a reactor in a chemical plant.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. MATERIALS is the sector, since this is chemical manufacturing.
#  HEALTH is claimed because pharmaceutical intermediates are where the field's
#  value is concentrated, and because the routes recorded here appear inside
#  medicines rather than beside them. ENVIRONMENT is claimed on solvent, metal
#  and waste displaced, which is measured rather than asserted through the
#  process mass intensity metric.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.HEALTH,
    Domain.ENVIRONMENT,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED, and the reasoning matters because a reader
#  could reasonably expect UNREGULATED for a manufacturing method.
#
#  The method itself needs no authorisation. But in its principal application
#  the route is written into an approved dossier, and it may not be changed
#  without an agency variation. Being unable to alter a step without permission
#  is what AUTHORISED means in practice, so the value reflects how the field
#  actually operates rather than how a synthesis textbook would classify it.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by which question each instrument answers.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- may the route be changed once approved? -------------------------------
    "Regulation (EC) No 1234/2008 on variations to marketing authorisations, "
    "which is the instrument that makes an approved synthetic route expensive "
    "to alter and therefore effectively fixed",
    "Directive 2001/83/EC and Regulation (EU) 2019/6, under which the "
    "manufacturing process forms part of the human and veterinary medicine "
    "dossiers respectively",
    # -- how must the plant operate? --------------------------------------------
    "EudraLex Volume 4 Good Manufacturing Practice, Part II, which governs "
    "manufacture of active substances and applies whether the catalytic step "
    "is enzymatic or chemical",
    "United States 21 CFR Part 211 and the corresponding active pharmaceutical "
    "ingredient expectations",
    # -- what happens in the fermenter that makes the catalyst? ------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, which applies to producing the enzyme and to whole-cell "
    "biocatalysts, and not to the isolated product",
    # -- what may be placed on the market? ----------------------------------------
    "Regulation (EC) No 1907/2006 REACH and Regulation (EC) No 1272/2008 CLP "
    "for the substances handled and produced",
    "Regulation (EC) No 1334/2008 on flavourings, which governs whether a "
    "biocatalytically produced flavour ester may be described as natural, a "
    "legal distinction rather than a chemical one",
    # -- worker and process safety -------------------------------------------------
    "Directive 2012/18/EU Seveso III for sites holding hazardous solvent "
    "inventories, a burden that a route eliminating solvent reduces directly",
    "Directive 2000/54/EC on biological agents at work, for handling the "
    "production organism",
    # -- where the enzyme's sequence came from ----------------------------------------
    "The Nagoya Protocol on access and benefit sharing, which attaches to an "
    "enzyme sourced from another country's genetic resources even when only "
    "the sequence was used",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is what actually determines practice here, and ICH
#  Q11 in particular is the document behind this record's governance note.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- what the agency approves, and therefore what is hard to change --------
    "ICH Q11 on development and manufacture of drug substances, which brings "
    "the synthetic route, the starting material justification and the control "
    "strategy into the approved dossier",
    "ICH Q7 Good Manufacturing Practice for active pharmaceutical ingredients",
    "ICH Q8 and Q9 on pharmaceutical development and quality risk management, "
    "under which the design space for an enzymatic step is defined",
    # -- the burden this technology removes --------------------------------------
    "ICH Q3D on elemental impurities, which a route that uses no metal "
    "catalyst simply does not engage, removing a specification and its testing "
    "rather than satisfying it",
    "ICH Q3C on residual solvents, which is where solvent substitution is "
    "credited",
    # -- what must be shown absent instead ----------------------------------------
    "Pharmacopoeial expectations for residual host cell protein, host cell DNA "
    "and endotoxin in material made using a biological catalyst, which is the "
    "purification burden that replaces the metal specification",
    # -- how the environmental claim is substantiated -------------------------------
    "American Chemical Society Green Chemistry Institute Pharmaceutical "
    "Roundtable process mass intensity conventions, which are how route "
    "comparisons in this field are actually reported",
    "The twelve principles of green chemistry, which supplied the field its "
    "design vocabulary in 1998",
    "ISO 14040 and ISO 14044 life cycle assessment methodology, required "
    "before a biocatalytic route may honestly be called the lower impact one, "
    "since fermenting the enzyme carries its own burden",
    # -- naming things consistently -------------------------------------------------
    "International Union of Biochemistry and Molecular Biology enzyme "
    "nomenclature and EC numbering",
)
