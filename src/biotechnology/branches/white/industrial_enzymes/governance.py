# =============================================================================
#  biotechnology.branches.white.industrial_enzymes.governance
# -----------------------------------------------------------------------------
#  FACET 5 OF 6:  GOVERNANCE
#
#  Contract, and the regulations-versus-standards distinction:
#  `red/gene_therapy/governance.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The governance of this record turns on a distinction that decides almost
#  everything and that most readers have never met.
#
#  THE ENZYME IS REGULATED AS A CHEMICAL, NOT AS AN ORGANISM. An industrial
#  enzyme is a purified protein. The genetically modified microorganism that
#  produced it is contained in the fermenter, killed, and removed during
#  downstream processing, and it does not appear in the product. Consequently
#  the enzyme falls under chemicals law, food additive law and occupational
#  health law, and NOT under the deliberate release regime that governs
#  `green.plant_genetic_engineering`. The contained use of the production
#  organism is regulated separately, at the factory.
#
#  This is why fermentation-produced chymosin entered the food supply in 1988
#  with almost none of the opposition later directed at genetically modified
#  crops. The public distinction between a modified organism in a field and a
#  purified protein in a drum turned out to be legally as well as
#  psychologically real.
#
#  THE OCCUPATIONAL THREAD IS NOT A FORMALITY. Enzymes are respiratory
#  sensitisers, the 1969 episode recorded in `history.py` was serious, and the
#  exposure limits and encapsulation practice below are the direct consequence.
#  They are listed before the food law for that reason.
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
#  MATURITY = ESTABLISHED. Commercial since 1913, recombinant since the 1980s,
#  a multi-billion euro market with several hundred products in routine use.
#  Individual enzyme classes within the field are still emerging; the field is
#  not.
# -----------------------------------------------------------------------------
MATURITY = Maturity.ESTABLISHED

# -----------------------------------------------------------------------------
#  RISK_TIER = CONTROLLED, and the choice needs explaining because a reader
#  could argue for either neighbouring value.
#
#  The vocabulary measures GOVERNANCE INTENSITY rather than danger. CONTROLLED
#  means a permit or licence is needed, and that is universally true here: the
#  production organism is a genetically modified microorganism handled under a
#  contained use authorisation, whatever the enzyme is later used for.
#
#  It is not ROUTINE, because of that permit and because enzymes are potent
#  respiratory sensitisers whose handling is subject to occupational controls
#  well beyond ordinary factory practice. The 1969 episode in `history.py` is
#  the reason.
#
#  It is not REGULATED, even though food and feed grades genuinely do require
#  agency authorisation before sale, because that applies to a subset rather
#  than to the class. That fact is carried by REGULATORY_STATUS below instead
#  of by inflating this tier.
# -----------------------------------------------------------------------------
RISK_TIER = RiskTier.CONTROLLED

# -----------------------------------------------------------------------------
#  SCALE = INDUSTRIAL. The unit of operation is a fermenter of tens to hundreds
#  of cubic metres feeding a process line, which is exactly what this value
#  denotes.
# -----------------------------------------------------------------------------
SCALE = Scale.INDUSTRIAL

# -----------------------------------------------------------------------------
#  DOMAINS. MATERIALS is the sector, since the vocabulary's industrial label
#  covers chemicals, fibres and process stock, which is what these catalysts
#  are sold into. FOOD is claimed because baking, dairy, starch and juice
#  processing are among the largest applications and bring their own legal
#  regime. ENVIRONMENT is claimed for the displaced chlorine, solvent and
#  phosphorus documented in `narrative.WHY_IT_MATTERS`.
# -----------------------------------------------------------------------------
DOMAINS: Tuple[Domain, ...] = (
    Domain.MATERIALS,
    Domain.FOOD,
    Domain.ENVIRONMENT,
)

# -----------------------------------------------------------------------------
#  REGULATORY_STATUS = AUTHORISED. Food enzymes require authorisation and are
#  entered on a positive list; feed additives require authorisation; the
#  substances themselves are registered under chemicals law. This is a
#  permissioned market, not an unregulated one.
# -----------------------------------------------------------------------------
REGULATORY_STATUS = RegulatoryStatus.AUTHORISED


# =============================================================================
#  REGULATIONS
#  Binding law, grouped by which question each instrument answers.
# =============================================================================
REGULATIONS: Tuple[str, ...] = (
    # -- may a worker be exposed to it? ----------------------------------------
    "Directive 2004/37/EC and national occupational exposure frameworks as "
    "applied to enzyme dust, which is classified as a respiratory sensitiser "
    "and is the reason granulated rather than powdered product is standard",
    "Directive 2000/54/EC on biological agents at work, which covers handling "
    "of the production organism in the plant",
    # -- may it enter food? -----------------------------------------------------
    "Regulation (EC) No 1332/2008 on food enzymes, which establishes the Union "
    "list and the authorisation procedure",
    "Regulation (EC) No 1829/2003, which governs the position where the enzyme "
    "is produced by a genetically modified microorganism, and under which a "
    "purified enzyme carrying no viable organism or recombinant DNA is treated "
    "differently from a modified organism itself",
    "United States Generally Recognised As Safe notification and food contact "
    "notification procedures for food-processing enzymes",
    # -- may it enter feed? -------------------------------------------------------
    "Regulation (EC) No 1831/2003 on additives for use in animal nutrition, "
    "under which phytase and the feed carbohydrases are authorised",
    # -- may it be placed on the market at all? -------------------------------------
    "Regulation (EC) No 1907/2006 REACH, under which enzyme preparations are "
    "registered as substances, and Regulation (EC) No 1272/2008 CLP, under "
    "which they are classified and labelled",
    "Regulation (EC) No 648/2004 on detergents, which governs the largest "
    "single application by volume",
    # -- what happens in the fermenter -----------------------------------------------
    "Directive 2009/41/EC on the contained use of genetically modified "
    "microorganisms, which regulates the production step rather than the "
    "product",
    # -- where the sequence came from ------------------------------------------------
    "The Nagoya Protocol on access and benefit sharing, which applies directly "
    "to enzymes discovered by bioprospecting or from metagenomic sampling in "
    "another country",
)


# =============================================================================
#  STANDARDS
#  Not law. The first group is the safety practice that the 1969 episode
#  produced, and it is placed first deliberately.
# =============================================================================
STANDARDS: Tuple[str, ...] = (
    # -- the practice that followed the setback --------------------------------
    "Association of Manufacturers and Formulators of Enzyme Products guidance "
    "on safe handling, encapsulation and airborne enzyme monitoring, which is "
    "the industry's own answer to the 1969 sensitisation episode",
    "Occupational exposure guidance values for airborne enzyme protein, "
    "expressed in nanograms per cubic metre rather than milligrams, which "
    "indicates how potent a sensitiser this class is",
    # -- purity and identity ----------------------------------------------------
    "Joint FAO/WHO Expert Committee on Food Additives specifications for enzyme "
    "preparations, which set the purity and contaminant limits",
    "Food Chemicals Codex monographs for food-grade enzyme preparations",
    # -- how activity is measured -----------------------------------------------
    "International Union of Biochemistry and Molecular Biology enzyme "
    "nomenclature and EC numbering, which is what makes two suppliers' products "
    "comparable at all",
    "Supplier-declared assay conditions for the activity unit, since a unit is "
    "meaningful only alongside the pH, temperature and substrate at which it "
    "was measured, as noted in `metrics.py`",
    # -- how it is made -----------------------------------------------------------
    "ISO 9001 and, for food and feed grades, HACCP and FSSC 22000 "
    "certification of the manufacturing site",
    "Good Manufacturing Practice for enzymes intended for pharmaceutical "
    "synthesis",
    # -- what may be claimed for it -------------------------------------------------
    "ISO 14040 and ISO 14044 life cycle assessment methodology, which is how "
    "the wash temperature and solvent displacement claims in this record are "
    "substantiated rather than asserted",
    "Green chemistry metric reporting conventions for E factor and atom "
    "economy",
)
