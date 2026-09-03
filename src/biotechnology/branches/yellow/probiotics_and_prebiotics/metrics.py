# =============================================================================
#  biotechnology.branches.yellow.probiotics_and_prebiotics.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS THE ONE THE WHOLE FIELD IS SOLD ON AND IT IS THE ONE
#  THAT PROVES LEAST.
#
#  Colony forming units per dose is on almost every package. It is a count of
#  live organisms and it is not an outcome, in exactly the sense
#  `green.biofertilisers` insists on for its own products and
#  `white.microbial_fermentation` for starter cultures. A high count with no
#  demonstrated effect is a well-populated tube.
#
#  It is placed first BECAUSE it is what consumers see, and its note is where
#  the correction belongs. The metrics that matter follow: whether the strain
#  is identified at all, whether the organisms survive to be eaten, whether
#  they survive the stomach, and whether anything measurable happened.
#
#  A NOTE ON WHY CLINICAL METRICS APPEAR HERE AT ALL. This is a food record and
#  its strongest evidence is clinical. Number needed to treat is included
#  because it is the honest way to express what a probiotic does in the
#  applications where it demonstrably does something, and because it makes the
#  contrast with the general wellbeing market unavoidable.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # =========================================================================
    #  THE NUMBER ON THE PACKAGE, AND WHY IT PROVES LITTLE
    # =========================================================================
    Metric(
        name="Viable count per dose",
        symbol="N_cfu",
        unit="colony forming units per dose",
        typical="10^8 - 10^11 CFU per dose in commercial products",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The figure on almost every package and not an outcome. It counts "
            "live organisms, which is a necessary condition and not a "
            "sufficient one, exactly as `green.biofertilisers` records that a "
            "viable cell count is not an effect. The adequate dose is strain "
            "and outcome specific, so a large number without a named strain and "
            "a named endpoint conveys almost nothing."
        ),
    ),
    Metric(
        name="Strain identification completeness",
        symbol="I_strain",
        unit="qualitative, whether genus, species and strain designation are "
        "all declared",
        typical="frequently incomplete on commercial products",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Recorded as a metric because it determines whether any published "
            "evidence can be attached to a product at all. Effects are "
            "strain-specific, so a label naming only a species is naming a "
            "category rather than an ingredient. It is the single most useful "
            "thing a consumer can check and the field's most common omission."
        ),
    ),
    # =========================================================================
    #  DOES ANYTHING SURVIVE TO REACH THE GUT
    # =========================================================================
    Metric(
        name="Viability at end of shelf life",
        symbol="N_eol",
        unit="colony forming units per dose at the stated expiry",
        typical="frequently below the label claim, and not routinely verified",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The claim that matters is the one at the point of consumption, not "
            "at manufacture. These organisms die slowly throughout storage and "
            "the decline depends on water activity, oxygen and temperature. "
            "Independent testing has repeatedly found products below their "
            "declared count, which is a quality failure rather than a "
            "scientific one and is no less consequential for that."
        ),
    ),
    Metric(
        name="Gastric and bile survival",
        symbol="f_surv",
        unit="per cent of the administered dose surviving to the small "
        "intestine",
        typical="highly strain-dependent, and reduced by orders of magnitude "
        "for sensitive strains",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The delivered dose is what acts, and it can be far below the dose "
            "swallowed. Encapsulation and spore-forming strains address this "
            "directly. It is rarely measured in the product as sold rather than "
            "in the strain under laboratory conditions."
        ),
    ),
    # =========================================================================
    #  DID ANYTHING ACTUALLY HAPPEN
    # =========================================================================
    Metric(
        name="Faecal recovery of the administered strain",
        symbol="R_fec",
        unit="per cent of subjects in whom the strain is detectable during "
        "administration",
        typical="commonly detectable during administration and absent within "
        "days to weeks of stopping",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The measurement that established transience, which is the field's "
            "least publicised finding. Detection during administration shows "
            "passage rather than colonisation, and disappearance afterwards "
            "shows that the resident community was not displaced. It is the "
            "quantitative form of the lawn in `narrative.ANALOGY`."
        ),
    ),
    Metric(
        name="Short-chain fatty acid production",
        symbol="c_SCFA",
        unit="millimoles per kilogram of faecal material",
        typical="raised measurably by fermentable prebiotic fibre",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Where prebiotic effects are most reliably detected, and the "
            "reason the prebiotic half of this record has firmer ground than "
            "the probiotic half. Feeding the resident community is more "
            "reproducible than introducing a new member, because it does not "
            "depend on anything establishing."
        ),
    ),
    Metric(
        name="Microbiome community shift",
        symbol="dBeta",
        unit="beta diversity distance between before and after samples",
        formula="beta_diversity",
        typical="small for most probiotic interventions and large for faecal "
        "transplantation",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The contrast within this single metric is the record's clearest "
            "quantitative statement. A probiotic dose shifts the community "
            "slightly and temporarily; a faecal transplant replaces it. That "
            "difference in magnitude tracks the difference in demonstrated "
            "clinical effect, which is unlikely to be a coincidence."
        ),
    ),
    # =========================================================================
    #  DID IT HELP ANYONE
    # =========================================================================
    Metric(
        name="Number needed to treat",
        symbol="NNT",
        unit="patients treated per additional good outcome",
        typical="favourable for specific strains in antibiotic-associated "
        "diarrhoea and in preterm necrotising enterocolitis",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The honest expression of what a probiotic does where it "
            "demonstrably does something. Including it in a food record is "
            "deliberate: it makes the contrast with the general wellbeing "
            "market unavoidable, since no such figure exists for a product "
            "sold without a named strain or a named endpoint."
        ),
    ),
    Metric(
        name="Cure rate in recurrent infection",
        symbol="R_cure",
        unit="per cent of patients resolved",
        typical="high for faecal microbiota transplantation in recurrent "
        "Clostridioides difficile infection",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The strongest evidence anywhere in this record, and it concerns "
            "the intervention least like a consumer product: an undefined "
            "community transferred between people, regulated as a medicine or a "
            "tissue. It established that the gut community can be manipulated "
            "therapeutically, which is the premise everything else here rests "
            "on."
        ),
    ),
    # =========================================================================
    #  IS THE PRODUCT WHAT IT SAYS IT IS
    # =========================================================================
    Metric(
        name="Label accuracy",
        symbol="A_label",
        unit="per cent of tested products matching their declared species and "
        "counts",
        typical="imperfect in published surveys",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Surveys have found products containing organisms other than those "
            "declared and counts below those claimed. Recorded as a metric "
            "because it is measurable, has been measured, and bears directly on "
            "whether any of the other numbers in this facet mean anything for a "
            "given product."
        ),
    ),
    Metric(
        name="Prebiotic fermentability",
        symbol="f_ferm",
        unit="per cent of the substrate fermented in the colon",
        typical="high for inulin-type fructans and "
        "galacto-oligosaccharides",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The defining property of a prebiotic: it must reach the colon "
            "undigested and be used there. It is also the source of the "
            "tolerance problem, since rapid fermentation produces gas, and the "
            "effective dose and the tolerated dose are close together for many "
            "people."
        ),
    ),
    Metric(
        name="Gastrointestinal tolerance threshold",
        symbol="D_tol",
        unit="grams per day before bloating and flatulence",
        typical="commonly 10 - 20 g/day for inulin-type fructans, with wide "
        "individual variation",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The practical limit on prebiotic dosing and the reason a larger "
            "dose is not simply better. It is also why prebiotic fibres are "
            "added to foods at modest levels: the effective dose for a measured "
            "outcome and the dose people will tolerate daily are not far apart."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Community measures and the clinical relationships.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "shannon_diversity",
    "beta_diversity",
    "number_needed_to_treat",
    "relative_risk",
    "serial_dilution",
    "specific_growth_rate",
)
