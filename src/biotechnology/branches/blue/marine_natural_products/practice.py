# =============================================================================
#  biotechnology.branches.blue.marine_natural_products.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by HOW THE SUPPLY PROBLEM WAS SOLVED rather than by
#  therapeutic area, because that is the distinction that determines whether a
#  compound became a medicine or stayed a publication. A reader who scans the
#  groups will notice that the harvesting group is empty, and that absence is
#  the record's central claim made visible.
#
#  ORGANISMS are the source organisms, with the caveat that for several of them
#  the animal is not the producer. Where a microbial symbiont is known or
#  strongly suspected to make the compound, the entry says so, because that
#  fact is the route out of the supply problem and not a taxonomic footnote.
#
#  TECHNOLOGIES follow the pipeline in order: collect, separate, identify,
#  test, and then the supply work that is this field's real difficulty.
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
#  Grouped by how supply was solved. Note that no group is headed "harvesting".
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- solved by SEMISYNTHESIS from a fermentation product --------------------
    "Trabectedin for soft tissue sarcoma, originally from a Caribbean tunicate "
    "and manufactured by semisynthesis from a bacterial fermentation product, "
    "which is the clearest case of a supply problem being engineered away",
    # -- solved by ANALOGUE DESIGN ---------------------------------------------
    "Eribulin for breast cancer, a simplified synthetic analogue of a sponge "
    "macrolide that retains the active portion and discards the synthetically "
    "intractable remainder",
    "Plinabulin and other simplified analogues developed from marine scaffolds "
    "too complex to make whole",
    # -- solved by TOTAL SYNTHESIS ---------------------------------------------
    "Ziconotide for severe chronic pain, a cone snail venom peptide made by "
    "peptide synthesis and delivered intrathecally because it survives no other "
    "route",
    "Marine-derived nucleoside analogues, including the antiviral and "
    "anticancer agents developed from sponge chemistry in the 1950s and 1960s, "
    "which were simple enough to synthesise from the start",
    # -- solved by USING IT AS A PAYLOAD, so that milligrams suffice -------------
    "Auristatin cytotoxins of marine origin used as warheads in antibody drug "
    "conjugates, where the antibody supplies the targeting and the required "
    "quantity is small enough that synthesis is straightforward",
    # -- solved by FERMENTING THE ACTUAL PRODUCER -------------------------------
    "Compounds attributed to invertebrates and later traced to their microbial "
    "symbionts, where culturing or heterologously expressing the symbiont "
    "replaces collection entirely",
    "Marine actinomycete and cyanobacterial metabolites, which have the "
    "advantage of coming from organisms that can sometimes be grown",
    # -- still unsolved, and named honestly -------------------------------------
    "Bryostatin, a bryozoan compound of long-standing interest whose supply has "
    "required many tonnes of animal for grams of material and which remains "
    "without a settled manufacturing route",
    # -- not medicines at all ---------------------------------------------------
    "Marine toxins as pharmacological tools and as reference standards, "
    "including channel blockers that define the assays other fields use",
    "Ultraviolet-absorbing compounds from marine organisms used in cosmetic "
    "formulation",
    "Antifouling and antimicrobial compounds investigated for the applications "
    "in `blue.marine_biofouling_control`",
)


# =============================================================================
#  TECHNOLOGIES
#  The pipeline in order. The last group is where the field's difficulty is.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- getting the material --------------------------------------------------
    "Diving, dredging and remotely operated vehicle collection, with voucher "
    "specimens deposited so the source organism can be identified afterwards",
    "Taxonomic identification of the source, without which a rediscovery cannot "
    "be distinguished from a discovery",
    # ---- separating a mixture --------------------------------------------------
    "Solvent extraction and liquid chromatographic fractionation",
    "Bioassay-guided fractionation, in which activity rather than abundance "
    "decides which fraction to pursue",
    "Preparative and high performance liquid chromatography for isolation at "
    "milligram scale",
    # ---- working out what it is -------------------------------------------------
    "Nuclear magnetic resonance and high resolution mass spectrometry for "
    "structure elucidation, frequently on quantities below a milligram",
    "X-ray crystallography and circular dichroism for absolute configuration, "
    "which matters because the wrong enantiomer is a different compound",
    "Dereplication against natural product databases, which is what prevents a "
    "known compound being isolated a fifth time and published as new",
    "Molecular networking of mass spectrometry data, which groups related "
    "compounds across samples and finds analogues without isolating them",
    # ---- finding it without isolating it ----------------------------------------
    "Genome mining for biosynthetic gene clusters, which reads the chemistry an "
    "organism can encode rather than the chemistry it happens to be making",
    "Metagenomic identification of the symbiont that actually produces a "
    "compound attributed to its host",
    # ---- SOLVING SUPPLY, which is the real work ---------------------------------
    "Total synthesis, viable where the molecule is tractable and defeated by "
    "the ones that are not",
    "Semisynthesis from a fermentation-derived starting material, which is how "
    "the field's most cited success is actually manufactured",
    "Analogue and pharmacophore simplification, keeping the active portion and "
    "discarding what cannot be made",
    "Heterologous expression of a biosynthetic gene cluster in a culturable "
    "host, which turns an uncultivable symbiont into a fermentation",
    "Aquaculture of the source organism, attempted repeatedly and rarely "
    "economic, since the animals grow slowly and the yield stays minute",
)


# =============================================================================
#  ORGANISMS
#  Source organisms, with the producer named where it is not the animal.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "ecteinascidia_turbinata",  # tunicate; the compound is of bacterial symbiont origin
    "conus_magus",  # cone snail; the venom peptide is genuinely the animal's own
    "halichondria_okadai",  # sponge; source of the macrolide behind eribulin
    "bugula_neritina",  # bryozoan; bryostatin, attributed to a bacterial symbiont
    "salinispora_tropica",  # marine actinomycete, culturable and a prolific producer
    "cryptotheca_crypta",  # sponge; the nucleosides behind the earliest marine drugs
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "chromatography",
    "mass_spectrometry",
    "nuclear_magnetic_resonance",
    "x_ray_crystallography",
    "bioassay",
    "total_synthesis",
    "metagenomics",
    "high_throughput_screening",
)


# =============================================================================
#  CHALLENGES
#  Supply first, because it is the one that decides outcomes.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the constraint that defines the field ---------------------------------
    "Supply, since the interesting compounds occur at parts per million in "
    "animals that grow slowly and cannot be farmed, so a promising molecule "
    "with no manufacturing route is a publication rather than a candidate",
    "Structural complexity that defeats total synthesis, with multiple "
    "stereocentres and ring systems that make a route commercially impossible "
    "even when it is chemically achievable",
    # -- getting the material at all ---------------------------------------------
    "Collection cost and depth access, which limit sampling to what a vessel "
    "can reach and bias discovery towards shallow, warm and convenient waters",
    "Damage to the sampled habitat, which for slow-growing reef and deep-sea "
    "communities is not recoverable on a human timescale",
    # -- knowing what you have -----------------------------------------------------
    "Rediscovery of known compounds, which consumes a large share of the "
    "field's effort and is only avoided by systematic dereplication",
    "Structure elucidation on sub-milligram quantities, where an error in "
    "stereochemistry produces a synthetic target that is not the natural "
    "product",
    # -- who actually made it -------------------------------------------------------
    "Attribution of a compound to a host that did not make it, which misdirects "
    "supply efforts towards farming an animal instead of culturing a symbiont",
    "Uncultivability of the producing symbiont, which moves the problem to "
    "heterologous expression rather than removing it",
    # -- economics -------------------------------------------------------------------
    "Withdrawal of pharmaceutical investment from natural product discovery, "
    "which removed the development capacity that this field's compounds depend "
    "on regardless of their quality",
    "The long interval between collection and any return, frequently decades, "
    "which no ordinary commercial arrangement is designed to bridge",
    # -- the law --------------------------------------------------------------------
    "Access and benefit sharing obligations, which attach to samples and to "
    "sequences and which historical collections predate",
    "Uncertain legal status of material collected beyond national jurisdiction "
    "before 2023, which leaves parts of the field's existing library in an "
    "unresolved position",
)
