# =============================================================================
#  biotechnology.branches.yellow.probiotics_and_prebiotics.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `yellow.nutrigenomics` is the edge this record most needs, and it is a
#  warning rather than a resource.
#
#  Both fields promised personalisation on evidence that did not support it,
#  both attracted commercial products ahead of the science, and both were
#  corrected by better measurement rather than by better marketing. The 2018
#  finding that probiotic colonisation is highly individual is exactly the kind
#  of result that makes personalisation sound imminent, and this record's
#  history shows what happens when a field sells that before it can deliver it.
#
#  `green.biofertilisers` is a cross-branch edge that a reader would not
#  predict and that carries a precise parallel. Both records sell live
#  organisms by viable count, both face the problem that a count is not an
#  effect, both encounter an established resident community that resists the
#  newcomer, and both have a history of products whose label claim exceeds what
#  survives to the point of use. One is applied to soil and one to a gut, and
#  the failure modes are the same.
#
#  `red.molecular_diagnostics` supplies the sequencing that established
#  transience, which is the finding that most changed what this field can
#  honestly claim.
#
#  `yellow.food_fermentation` is the older and quieter relative: fermented
#  foods deliver live organisms without any of this record's claims, and the
#  evidence concerning them is about the food rather than about an identified
#  strain.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Two, which is the fewest of any record in this branch, and the restraint is
#  the point.
#
#  Goal 3 is claimed on the specific clinical applications where the evidence
#  is strong: necrotising enterocolitis in preterm infants, antibiotic-
#  associated diarrhoea, acute infectious diarrhoea in children, and recurrent
#  Clostridioides difficile infection. Those are real outcomes in defined
#  populations with trial evidence behind them.
#
#  It is NOT claimed for the general wellbeing market, which is most of the
#  sector by revenue and for which no health claim has been authorised in the
#  European Union.
#
#  GOALS 2 AND 12 ARE DELIBERATELY NOT CLAIMED, although a food record could
#  reach for both. Nothing here addresses food security, and nothing here
#  reduces resource use. A record whose own governance facet records that its
#  claims failed regulatory assessment should be the last in this branch to
#  claim additional goals, and claiming them would be exactly the behaviour
#  rule 12 exists to prevent.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on the specific clinical applications only
    9,  # Industry and innovation, on the manufacturing and formulation science
)


# =============================================================================
#  GLOSSARY
#  Grouped: the definitions, the community, the delivery problem, and the
#  evidence vocabulary.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the definitions, which are contested and matter -----------------------
    "probiotic",
    "prebiotic",
    "synbiotic",
    "postbiotic",
    "live_biotherapeutic_product",
    "strain_specificity",
    # -- the community it acts on ----------------------------------------------
    "gut_microbiome",
    "colonisation",
    "colonisation_resistance",
    "dysbiosis",
    "short_chain_fatty_acid",
    "faecal_microbiota_transplantation",
    "defined_consortium",
    # -- getting it there alive ------------------------------------------------
    "colony_forming_unit",
    "viability",
    "microencapsulation",
    "freeze_drying",
    "gastric_survival",
    "shelf_life",
    # -- the substrates --------------------------------------------------------
    "inulin",
    "fructo_oligosaccharide",
    "galacto_oligosaccharide",
    "human_milk_oligosaccharide",
    "resistant_starch",
    "fermentable_fibre",
    # -- the evidence vocabulary -----------------------------------------------
    "randomised_controlled_trial",
    "number_needed_to_treat",
    "surrogate_endpoint",
    "health_claim",
    "publication_bias",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "isapp_probiotic_definition",
    "isapp_prebiotic_definition",
    "efsa_probiotic_health_claims_assessment",
    "fmt_recurrent_cdi_trial",
    "probiotic_colonisation_transience_study",
    "probiotics_preterm_necrotising_enterocolitis_review",
    "antibiotic_associated_diarrhoea_meta_analysis",
    "probiotic_product_label_accuracy_survey",
    "defined_consortium_licensed_medicine",
    "human_milk_oligosaccharide_authorisation",
)


# =============================================================================
#  RELATED
#  Six edges. The first is a warning and the second is an unexpected parallel.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same overpromise, in a neighbouring field -------------------------
    "yellow.nutrigenomics",
    # -- live organisms sold by count, against a resident community ------------
    "green.biofertilisers",
    # -- live organisms delivered by food, without the claims ------------------
    "yellow.food_fermentation",
    # -- the sequencing that established transience ----------------------------
    "red.molecular_diagnostics",
    # -- where the oligosaccharides come from ----------------------------------
    "yellow.precision_fermentation",
    # -- direct-fed microbials, where efficacy data is actually required -------
    "green.veterinary_vaccines",
)
