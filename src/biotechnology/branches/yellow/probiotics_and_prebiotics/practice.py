# =============================================================================
#  biotechnology.branches.yellow.probiotics_and_prebiotics.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped BY STRENGTH OF EVIDENCE, from clinical use down to
#  general wellbeing, and this is the most important editorial decision in the
#  record. Rule 6 forbids listing an aspiration as an application, and in this
#  field the distinction between a demonstrated effect and a marketed claim is
#  precisely what a reader needs.
#
#  A reader who notices that the first group concerns hospitals and the last
#  concerns supermarket shelves has understood the field's principal problem.
#
#  ORGANISMS require an unusual note. The entries below are SPECIES, and the
#  record's central point is that evidence is STRAIN-specific. A species name
#  is therefore not an active ingredient, and listing species here is a
#  limitation of the schema rather than an endorsement of the practice of
#  labelling by species. Where a specific strain matters clinically the
#  applications name the effect rather than the strain, because strain
#  designations belong in a reference registry that does not yet exist.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = [
    "APPLICATIONS",
    "TECHNOLOGIES",
    "ORGANISMS",
    "TECHNIQUES",
    "CHALLENGES",
]


# =============================================================================
#  APPLICATIONS
#  By strength of evidence, strongest first. The ordering is the argument.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- clinical, with substantial trial evidence ------------------------------
    "Faecal microbiota transplantation for recurrent Clostridioides difficile "
    "infection, which is highly effective, is regulated as a medicine or a "
    "tissue in most jurisdictions, and is the clearest demonstration that the "
    "gut community can be manipulated therapeutically",
    "Specific probiotic strains to reduce necrotising enterocolitis in preterm "
    "infants, which addresses a condition with substantial mortality and is "
    "among the better-supported nutritional interventions in neonatal care",
    "Specific strains to reduce the duration of acute infectious diarrhoea in "
    "children",
    "Specific strains to reduce the incidence of antibiotic-associated "
    "diarrhoea",
    "Defined bacterial consortia developed as licensed medicines for recurrent "
    "infection, which is faecal transplantation made reproducible and "
    "manufacturable",
    # -- established and narrower ------------------------------------------------
    "Lactase-producing strains and lactose-free dairy for lactose maldigestion, "
    "where the mechanism is enzymatic and uncontroversial",
    "Prebiotic fibres including inulin, fructo-oligosaccharides and "
    "galacto-oligosaccharides for stool consistency and transit time",
    "Human milk oligosaccharides in infant formula, which supply compounds that "
    "shape the infant gut community and that formula previously lacked, and "
    "which are produced by `yellow.precision_fermentation`",
    "Resistant starch and beta-glucan for their effects on colonic fermentation "
    "and short-chain fatty acid production",
    # -- plausible, and the trials are mostly not of the required quality ---------
    "Strains investigated for irritable bowel syndrome symptoms, where results "
    "are mixed and strain-dependent",
    "Strains investigated for vaginal and urogenital health, where the "
    "rationale is strong and the trial evidence is uneven",
    "Fermented foods consumed for microbiome effects, which links to "
    "`yellow.food_fermentation` and where the evidence concerns the food rather "
    "than any identified organism",
    # -- sold widely, and the evidence does not support the claim made -------------
    "General wellbeing, immunity and digestive health products carrying no "
    "strain designation, which constitute most of the market and for which no "
    "health claim has been authorised in the European Union",
    "Probiotic cosmetics and skin products, where the mechanism is largely "
    "unestablished",
    # -- animals, where the economics are clearer ----------------------------------
    "Direct-fed microbials and prebiotics in livestock and aquaculture feed, "
    "adopted partly as an alternative to antibiotic growth promoters and "
    "measured on production outcomes rather than on health claims",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the four problems: pick it, keep it alive, get it there, prove it.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- choosing the organism ------------------------------------------------
    "Strain isolation and whole genome sequencing, which is what makes a strain "
    "designation meaningful and allows a product to be matched to published "
    "evidence",
    "Screening for adhesion, acid and bile tolerance, and antimicrobial "
    "production, which are the properties assumed to matter and are proxies "
    "rather than demonstrated mechanisms",
    "Safety assessment including antimicrobial resistance gene screening and "
    "absence of transferable resistance, which is a requirement rather than a "
    "refinement",
    "Defined consortium design, assembling several characterised organisms "
    "rather than transferring an undefined community",
    # ---- keeping it alive until it is eaten -------------------------------------
    "Freeze drying with cryoprotectants, which is how most viable counts "
    "survive to the end of shelf life",
    "Microencapsulation in alginate, protein or lipid matrices, protecting "
    "organisms through processing, storage and stomach acid",
    "Stability formulation for water activity, oxygen and temperature, since "
    "these organisms die slowly in storage and the label claim must hold at the "
    "end of shelf life rather than at manufacture",
    "Spore-forming strain selection, which sidesteps the stability problem "
    "entirely at the cost of a different safety assessment",
    # ---- getting it past the stomach ---------------------------------------------
    "Gastric-resistant delivery formats and enteric coating",
    "Dose determination, since the definition requires an adequate amount and "
    "the adequate amount is strain and outcome specific rather than a general "
    "number",
    # ---- finding out whether it did anything --------------------------------------
    "Sequencing-based community profiling before, during and after "
    "administration, which is how transience was actually established",
    "Short-chain fatty acid and metabolite measurement, which is where "
    "prebiotic effects are most reliably detected",
    "In vitro gut models and organoid systems for mechanism, which are useful "
    "for hypothesis and weak as evidence of clinical effect",
    "Randomised controlled trials with a named strain and a defined clinical "
    "endpoint, which is the only thing that settles the question and is the "
    "step most of this market has skipped",
)


# =============================================================================
#  ORGANISMS
#  Species, and the record's point is that species are not the active
#  ingredient. See the module header.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "lacticaseibacillus_rhamnosus",  # the most trialled species; strains differ widely
    "bifidobacterium_longum",  # dominant in the infant gut, and a common product species
    "lactobacillus_acidophilus",  # widely sold, and frequently without a strain name
    "saccharomyces_boulardii",  # a yeast, and unaffected by antibacterial treatment
    "akkermansia_muciniphila",  # mucin-degrading, studied for metabolic effects
    "bacillus_subtilis",  # spore-forming, which solves the stability problem
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "cell_culture",
    "next_generation_sequencing",
    "metagenomics",
    "freeze_drying",
    "microencapsulation",
    "randomised_controlled_trial",
    "mass_spectrometry",
    "flow_cytometry",
)


# =============================================================================
#  CHALLENGES
#  The evidence problems first, because they are what the field is judged on.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the problem that invalidates most of the market ------------------------
    "Strain specificity, since evidence generated for one strain does not "
    "transfer to another of the same species, and most products name no strain "
    "at all, which means published evidence cannot be attached to what a "
    "consumer buys",
    "Absence of any authorised health claim for a probiotic in the European "
    "Union, so products are sold on implication rather than on assertion, which "
    "is a regulatory finding about the evidence rather than about the rules",
    "Trial quality, where much of the literature uses small samples, "
    "surrogate endpoints and heterogeneous populations, so meta-analysis "
    "combines studies that are not measuring the same thing",
    # -- the biology that limits what is possible --------------------------------
    "Transient colonisation, since introduced organisms generally do not "
    "establish and the effect lasts about as long as the administration, which "
    "is rarely disclosed",
    "Individual variation in response, which is large and is why an effect "
    "demonstrated across a population may be absent in a given person",
    "Poorly understood mechanisms, which are frequently metabolic or "
    "immunological rather than a matter of the organism taking up residence, so "
    "the intuitive account most consumers hold is wrong",
    # -- keeping the product honest ------------------------------------------------
    "Viability at the end of shelf life, which is frequently below the label "
    "claim and is not routinely verified by anyone",
    "Survival through gastric acid and bile, which reduces the delivered dose "
    "by an amount that is rarely measured in the product as sold",
    "Identity verification, since products have been found to contain "
    "organisms other than those declared",
    # -- safety, which the casual framing gets wrong ----------------------------------
    "Bloodstream infection in immunocompromised and critically ill patients, "
    "which has occurred with live organisms and is the reason these products "
    "are not harmless merely because they are frequently ineffective",
    "Antimicrobial resistance gene transfer from a live organism to the "
    "resident community, which is why resistance screening is a requirement",
    # -- and the therapeutic end of the record ---------------------------------------
    "Donor screening, standardisation and long-term follow-up for faecal "
    "microbiota transplantation, where an undefined community is transferred "
    "between people and the transferred material cannot be fully characterised",
)
