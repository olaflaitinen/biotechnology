# =============================================================================
#  biotechnology.branches.green.plant_genetic_engineering.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  One metric in this set is misread more often than any other in the library,
#  and it is worth stating the correction before the list rather than after.
#
#  A Bt or virus-resistance trait does NOT raise the genetic yield potential of
#  a variety. It PROTECTS the yield the variety already had, by removing a loss
#  that would otherwise occur. The observed yield difference against an
#  isogenic line is therefore a function of pest pressure: large where the pest
#  is present, near zero where it is not, and occasionally negative because of
#  the small metabolic cost of expressing the protein.
#
#  Both the strongest claims made for these crops and the strongest claims made
#  against them come from quoting a yield difference measured under one pest
#  pressure as though it were a property of the technology. It is a property of
#  the field it was measured in.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # -------------------------------------------------------------------------
    #  Transformation efficiency. The laboratory bottleneck, and the reason
    #  elite genotypes are often not the ones that get engineered.
    # -------------------------------------------------------------------------
    Metric(
        name="Transformation efficiency",
        symbol="TE_plant",
        unit="per cent of explants yielding an independent event",
        typical="0.1 % in recalcitrant maize inbreds to 30 % in tobacco",
        formula="transformation_efficiency",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Almost entirely genotype-dependent, and the limiting step is "
            "regeneration rather than DNA delivery. This is why a construct is "
            "often made in an easily transformed variety and then crossed into "
            "the one farmers want, which adds years."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Copy number. Single copy is strongly preferred, and the reason is
    #  regulatory and genetic rather than aesthetic.
    # -------------------------------------------------------------------------
    Metric(
        name="Transgene copy number",
        symbol="CN",
        unit="inserted copies per haploid genome",
        typical="1 to 3; single copy strongly preferred",
        formula="copy_number",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Multiple copies segregate unpredictably, are more prone to "
            "silencing, and make the molecular characterisation dossier far "
            "harder to assemble. Most events generated are discarded on this "
            "criterion alone."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Expression level of the introduced protein. A release specification and
    #  a safety assessment input.
    # -------------------------------------------------------------------------
    Metric(
        name="Trait protein expression level",
        symbol="E_trait",
        unit="micrograms of protein per gram fresh weight",
        typical="1 - 100 ug/g, varying by tissue and growth stage",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Measured across tissues, growth stages and seasons, because the "
            "dietary exposure assessment depends on the concentration in the "
            "part actually eaten, not on the maximum anywhere in the plant."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Yield difference. The most misread number in this library. See header.
    # -------------------------------------------------------------------------
    Metric(
        name="Yield difference versus isogenic line",
        symbol="dY",
        unit="per cent",
        typical="0 % under no pest pressure to 25 % or more under heavy "
        "pressure",
        formula="relative_yield",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Insect and virus resistance PROTECT yield rather than raise "
            "potential. The figure is therefore a property of the pest pressure "
            "in the field where it was measured, not of the technology. Quoting "
            "a single number without the pest pressure is the most common error "
            "made by advocates and critics alike, in opposite directions."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Insecticide application count. The outcome measure that survives across
    #  studies better than yield does.
    # -------------------------------------------------------------------------
    Metric(
        name="Insecticide applications avoided",
        symbol="dA",
        unit="sprays per season",
        typical="2 - 8 fewer sprays in Bt cotton systems",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "More robust across studies than yield, and the outcome that "
            "matters most where spraying is done by hand without protective "
            "equipment. It does not transfer to herbicide-tolerant systems, "
            "where total herbicide volume has often risen."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Refuge fraction. The resistance management requirement, and a rare case
    #  of an evolutionary calculation written into a licence condition.
    # -------------------------------------------------------------------------
    Metric(
        name="Structured refuge fraction",
        symbol="R_ref",
        unit="per cent of the planted area sown to non-Bt plants",
        typical="5 - 20 % depending on crop and jurisdiction",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A deliberately unprotected area maintains susceptible insects that "
            "dilute any resistance allele arising in the treated crop. It is an "
            "evolutionary calculation imposed as a legal condition, and where "
            "compliance has been poor, resistance has followed within a decade."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Segregation ratio. The genetic check that an event behaves as a single
    #  Mendelian locus.
    # -------------------------------------------------------------------------
    Metric(
        name="Segregation ratio",
        symbol="chi2",
        unit="observed against expected Mendelian ratio",
        typical="3:1 in a selfed hemizygous progeny",
        formula="mendelian_segregation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Departure from the expected ratio indicates multiple insertion "
            "sites, silencing, or linkage to a deleterious region, and is one of "
            "the earliest screens applied to a new event."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Adventitious presence. A regulatory threshold, not a scientific one.
    # -------------------------------------------------------------------------
    Metric(
        name="Adventitious presence threshold",
        symbol="AP",
        unit="per cent of the ingredient by weight",
        typical="0.9 % labelling threshold in the European Union",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "A policy figure rather than a safety one. It defines the level of "
            "accidental admixture tolerated before labelling is required, and it "
            "is what makes coexistence rules and buffer distances necessary."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  gene_flow_distance is included because coexistence rules and buffer widths
#  are derived from it, and hardy_weinberg because resistance allele frequency
#  in a pest population is how refuge policy is evaluated.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "transformation_efficiency",
    "copy_number",
    "relative_yield",
    "mendelian_segregation",
    "gene_flow_distance",
    "hardy_weinberg",
    "serial_dilution",
)
