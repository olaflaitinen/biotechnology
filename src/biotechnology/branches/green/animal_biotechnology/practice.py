# =============================================================================
#  biotechnology.branches.green.animal_biotechnology.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications are grouped by the three layers from
#  `narrative.DESCRIPTION`, and then by whether the purpose is production or
#  welfare. That second split matters because it is exactly the distinction
#  public opinion makes and the science does not: an edit that removes horn
#  growth and an edit that increases muscle mass are the same operation, and
#  people judge them very differently.
#
#  Editorial rule 6 is applied strictly. Every entry names something in
#  commercial use or with a completed regulatory decision, and the two entries
#  that are neither say so.
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
#  Grouped by layer, then by purpose within the editing layer.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- layer 1: reproduction, in use for decades -----------------------------
    "Artificial insemination in dairy and beef cattle, which is near universal "
    "in developed dairy systems",
    "Sexed semen, sorting sperm by the DNA difference between X-bearing and "
    "Y-bearing cells to bias the calf crop",
    "Superovulation with embryo flushing and transfer",
    "Ovum pick-up with in vitro embryo production, which multiplies the female "
    "side where the biological ceiling is far lower than the male",
    "Cryopreservation of semen, oocytes and embryos, which also underpins rare "
    "breed conservation",
    # -- layer 2: genomic selection, adopted from 2009 --------------------------
    "Genomic selection in dairy cattle, which roughly halved the generation "
    "interval and nearly doubled annual genetic gain",
    "Genomic selection in pigs, poultry and salmon",
    "Genomic management of inbreeding, using relationship matrices to constrain "
    "mating decisions rather than only to rank animals",
    "Parentage verification and traceability from genotype",
    # -- layer 3, welfare purpose ------------------------------------------------
    "POLLED cattle carrying a naturally occurring hornless allele, avoiding "
    "disbudding of calves with a hot iron",
    "PRRS-resistant pigs produced by editing the CD163 receptor the virus "
    "requires, approved in the United States in 2025 and pending elsewhere",
    "Heat-tolerant cattle carrying the slick-coat allele from tropical breeds",
    # -- layer 3, production purpose ----------------------------------------------
    "Cloning of elite breeding animals by somatic cell nuclear transfer, used "
    "commercially in a small number of species",
    "Transgenic animals as protein bioreactors, secreting a therapeutic protein "
    "into milk or egg white",
    "Fast-growing farmed salmon carrying a growth hormone construct, approved "
    "for sale in the United States and Canada",
    # -- conservation rather than production ---------------------------------------
    "Cryobanking and assisted reproduction for rare and endangered breeds",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by layer, mirroring the applications.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- reproduction --------------------------------------------------------
    "Semen collection, extension and cryopreservation",
    "Flow-cytometric sperm sexing",
    "Oestrus synchronisation and fixed-time insemination protocols",
    "Superovulation, embryo flushing and non-surgical transfer",
    "Ovum pick-up, in vitro maturation, fertilisation and culture",
    "Vitrification of oocytes and embryos",
    # ---- genomics --------------------------------------------------------------
    "Single nucleotide polymorphism chips designed for each livestock species",
    "Genomic estimated breeding value pipelines using single-step evaluation "
    "that combines genotyped and ungenotyped animals",
    "International genetic evaluation across national datasets",
    "Sensor-based phenotyping of feed intake, rumination, activity and health, "
    "which addresses the phenotyping bottleneck this field shares with plant "
    "breeding",
    "Relationship-matrix constrained mate allocation to manage inbreeding",
    # ---- direct alteration ------------------------------------------------------
    "Somatic cell nuclear transfer",
    "CRISPR editing of zygotes by microinjection or electroporation",
    "Editing of primordial germ cells, particularly in poultry where the "
    "zygote is difficult to access",
    "Genotype screening of edited founders for off-target and mosaic outcomes",
    "Surrogate sire technology, in which a germline-ablated recipient carries "
    "donor spermatogonia",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "bos_taurus",  # cattle, where genomic selection was adopted first
    "sus_scrofa",  # pigs, and the CD163 disease resistance edit
    "gallus_gallus",  # poultry, where primordial germ cell editing is the route
    "ovis_aries",  # sheep, and the species Dolly belonged to
    "salmo_salar",  # Atlantic salmon, genomic selection and the growth construct
    "capra_hircus",  # goats, the main transgenic bioreactor species
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "next_generation_sequencing",
    "microarray",
    "crispr_cas9",
    "cryopreservation",
    "flow_cytometry",
    "pcr",
    "cell_culture",
    "phenotyping",
)


# =============================================================================
#  CHALLENGES
#  Three biological, two technical, three social and regulatory. The last is
#  the binding constraint on the third layer.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- what intense selection costs ------------------------------------------
    "Loss of genetic diversity through very intense sire selection, which has "
    "driven the effective population size of major dairy breeds to levels that "
    "would concern a conservation biologist",
    "Unfavourable correlated responses, where selecting hard on production "
    "historically carried fertility, lameness and metabolic disease with it, "
    "and correcting that required deliberately rewriting the breeding goal "
    "rather than any new technology",
    "Prediction accuracy that falls sharply outside the reference population, "
    "so the breeds and regions with the least recording benefit least",
    # -- technical --------------------------------------------------------------
    "Low efficiency and high loss rates in somatic cell nuclear transfer, "
    "including large offspring syndrome and placental abnormality",
    "Mosaicism in edited founders, where an embryo edited after the first "
    "division carries a mixture of edited and unedited cells and must be bred "
    "out",
    # -- social and regulatory ----------------------------------------------------
    "Public acceptance, which distinguishes sharply between an edit that "
    "reduces suffering and one that increases output, in a way the underlying "
    "science does not",
    "Concentration of livestock genetics in a very small number of "
    "multinational suppliers, which narrows both the gene pool and the market",
    "Regulatory uncertainty for edited food animals, which is the binding "
    "constraint on the whole third layer: editing a zygote is routine, and "
    "obtaining approval to sell the animal in most jurisdictions is not",
)
