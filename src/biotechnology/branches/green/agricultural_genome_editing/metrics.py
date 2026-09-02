# =============================================================================
#  biotechnology.branches.green.agricultural_genome_editing.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  One correction belongs before the list, because it is the most common
#  misstatement about this technology in both directions.
#
#  OFF-TARGET EDITING IS REAL AND IS SMALL RELATIVE TO ITS ALTERNATIVES. A
#  typical edited line carries a handful of detectable unintended changes at
#  similar-looking sites. The tissue culture step that accompanies the edit
#  introduces hundreds to thousands of somaclonal mutations on its own, and
#  chemical or radiation mutagenesis, used without special regulation since the
#  1950s to produce thousands of commercial varieties, introduces tens of
#  thousands.
#
#  Stating that is not an argument that off-target effects do not matter. They
#  are screened for, and lines carrying them are discarded. It is a statement
#  that the number has to be compared with something, and that the something
#  is usually left out.
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
    #  Editing efficiency. The headline laboratory number, and the one that
    #  collapses in polyploids.
    # -------------------------------------------------------------------------
    Metric(
        name="Editing efficiency",
        symbol="indel%",
        unit="per cent of alleles carrying the intended edit",
        typical="5 - 90 %, falling sharply in polyploid species",
        formula="editing_efficiency",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Quantified by amplicon sequencing of the target site. In a "
            "hexaploid such as bread wheat the phenotype appears only when all "
            "six copies are edited, so an apparently good per-allele efficiency "
            "can still yield very few useful plants."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Off-target rate. See the header note for the comparison that belongs
    #  with it.
    # -------------------------------------------------------------------------
    Metric(
        name="Off-target editing rate",
        symbol="OT",
        unit="detectable unintended edits per genome",
        typical="0 - 5 sites in a screened line",
        formula="off_target_rate",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Detected by whole-genome sequencing against the unedited parent. "
            "The figure is meaningful only against a comparator: the "
            "accompanying tissue culture step introduces hundreds to thousands "
            "of somaclonal mutations, and chemical or radiation mutagenesis "
            "introduces tens of thousands. Lines carrying off-target edits are "
            "discarded, which is cheap because the edit can simply be repeated."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Guide design score. A predicted quantity, not a measured one, and one
    #  whose predictive value is modest.
    # -------------------------------------------------------------------------
    Metric(
        name="Guide RNA on-target score",
        symbol="S_guide",
        unit="dimensionless, scaled 0 to 1",
        typical="design threshold around 0.6",
        formula="guide_rna_score",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "A model prediction rather than a measurement, trained largely on "
            "mammalian cell data and transferring imperfectly to plants. It is "
            "used to rank candidate guides, not to promise an outcome, and "
            "three or four guides are usually tested empirically."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Repair outcome distribution. What the cell actually does with the break,
    #  which is only partly under the experimenter's control.
    # -------------------------------------------------------------------------
    Metric(
        name="Homology-directed repair fraction",
        symbol="HDR%",
        unit="per cent of edits using the supplied template",
        typical="0.1 - 10 % in plant cells",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The reason type 1 knockouts dominate deployment. Precise "
            "substitution requires the cell to choose template-directed repair, "
            "which it rarely does outside dividing tissue. Base and prime "
            "editing exist largely to sidestep this number."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Transgene-free recovery. The number that decides the regulatory class of
    #  the finished plant in most jurisdictions.
    # -------------------------------------------------------------------------
    Metric(
        name="Transgene-free recovery rate",
        symbol="TFR",
        unit="per cent of edited lines free of editing machinery",
        typical="10 - 50 % after one or two generations of segregation",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Not applicable where ribonucleoprotein delivery was used, since "
            "nothing was ever integrated. Where Agrobacterium was used, this is "
            "the fraction that segregates cleanly, and it is the number that "
            "determines whether the product is treated as edited or as "
            "transgenic."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Generations to a usable line. The timeline advantage over backcrossing,
    #  expressed honestly.
    # -------------------------------------------------------------------------
    Metric(
        name="Generations to a clean edited line",
        symbol="G_clean",
        unit="generations",
        typical="1 - 3, against 6 or more for introgression by backcrossing",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The core practical advantage of the technology. It does not "
            "include the time to regenerate plants from edited cells, which in "
            "a recalcitrant genotype can exceed the breeding time saved."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Regeneration efficiency. The bottleneck, shared with
    #  green.plant_genetic_engineering and green.plant_tissue_culture.
    # -------------------------------------------------------------------------
    Metric(
        name="Protoplast regeneration efficiency",
        symbol="RE",
        unit="per cent of protoplasts yielding a plantlet",
        typical="below 1 % in most crop species",
        formula="regeneration_frequency",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The limiting step for DNA-free editing. Ribonucleoprotein delivery "
            "into protoplasts is regulatorily attractive and biologically "
            "punishing, because very few species regenerate reliably from a "
            "single wall-less cell."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Segregation. The genetic check that the edit behaves as a single locus.
    # -------------------------------------------------------------------------
    Metric(
        name="Segregation ratio",
        symbol="chi2",
        unit="observed against expected Mendelian ratio",
        typical="3:1 in a selfed heterozygous progeny",
        formula="mendelian_segregation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Used both to confirm the edit is a single heritable locus and to "
            "confirm the editing construct has been segregated away, which are "
            "two separate questions answered by the same cross."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  melting_temperature is included because guide and primer design both depend
#  on it, and relative_yield because a knockout's agronomic cost has to be
#  measured against the unedited parent before a line is advanced.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "editing_efficiency",
    "off_target_rate",
    "guide_rna_score",
    "regeneration_frequency",
    "mendelian_segregation",
    "melting_temperature",
    "relative_yield",
    "gc_content",
)
