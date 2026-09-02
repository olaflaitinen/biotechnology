# =============================================================================
#  biotechnology.branches.white.industrial_enzymes.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the record most readers have already used today without knowing it.
#  Enzymes are in laundry detergent, in bread, in cheese, in fruit juice, in
#  denim, in paper and in animal feed. The public register is built on that,
#  because the fastest way to make an abstract subject concrete is to point at
#  something in the reader's own kitchen.
#
#  The single most useful number in the record is the wash temperature. Moving
#  a domestic wash from 60 to 30 degrees cuts the electricity for that wash by
#  roughly two thirds, and enzymes are what made the lower temperature work.
#  Multiplied across the world's washing machines this is one of the largest
#  quiet emissions reductions attributable to any biotechnology, and almost
#  nobody knows it happened.
#
#  The analogy is a key rather than a hammer, and it is used consistently in
#  this branch: `white/__init__.py` uses the same locksmith framing at branch
#  level, and this record narrows it to the single lock.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

__all__ = [
    "SUMMARY",
    "DESCRIPTION",
    "PLAIN_LANGUAGE",
    "ANALOGY",
    "WHY_IT_MATTERS",
]


# =============================================================================
#  TECHNICAL REGISTER
# =============================================================================

SUMMARY = (
    "Discovery, engineering and large-scale production of enzymes used as "
    "catalysts in detergents, food, textiles, paper, feed and chemistry."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what an enzyme is as a piece of process equipment,
#  (b) how one is obtained, (c) how it is made and sold, (d) the limits.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the enzyme as equipment
    "An industrial enzyme is a protein sold as process equipment. It "
    "accelerates one reaction by many orders of magnitude while working in "
    "water, near ambient temperature and near neutral pH, and it is selective "
    "enough that it usually yields one product rather than a mixture requiring "
    "separation. Those three properties are the entire commercial case: less "
    "energy into the vessel, less solvent to buy and dispose of, and fewer "
    "purification steps afterwards. "
    # (b) how one is obtained
    "Candidate enzymes come from screening culture collections, from "
    "metagenomic libraries built directly from environmental DNA without "
    "culturing anything, and increasingly from sequence databases and "
    "structure prediction. A candidate is then improved rather than accepted "
    "as found. Directed evolution applies rounds of mutagenesis and selection "
    "and requires no understanding of the mechanism; rational design uses "
    "structure to choose substitutions deliberately; the two are now usually "
    "combined, with computational design proposing variants and laboratory "
    "screening testing them. "
    # (c) manufacture
    "Production is by submerged fermentation of a small number of "
    "well-characterised host organisms, chiefly Bacillus, Aspergillus and "
    "Trichoderma species, at scales of tens to hundreds of cubic metres. The "
    "enzyme is usually secreted into the broth, which is why these hosts were "
    "chosen: recovery is a matter of removing the cells rather than breaking "
    "them open. The product is sold as a liquid concentrate, a granulate or an "
    "immobilised preparation on a solid support, and immobilisation is what "
    "makes the catalyst recoverable and reusable across many batches. "
    # (d) the limits
    "The limits are the ones that follow from the enzyme being a protein. It "
    "denatures above its thermal tolerance, it is inhibited by many of the "
    "conditions an industrial process would prefer to use, it works in water "
    "when much of chemistry is done in organic solvents, and its operational "
    "lifetime rather than its initial activity is what determines cost per "
    "kilogram of product. Improving stability, not improving speed, is where "
    "most engineering effort in this field goes."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Enzymes are the tools living things use to take molecules apart and put "
    "them together, and they can be purified and sold in a drum. They are "
    "already in things you use daily: in washing powder, where they digest "
    "food and grass stains so the wash works at a low temperature; in bread, "
    "where they keep the loaf soft for longer; in cheese, where they set the "
    "curd; in fruit juice, where they stop it going cloudy; and in the stone "
    "washing of denim, which used to be done with actual pumice stones. What "
    "makes them valuable is that they do one job very precisely, in ordinary "
    "warm water, instead of needing heat, pressure and harsh chemicals."
)

# -----------------------------------------------------------------------------
#  The key analogy. It carries three things at once: selectivity (one lock),
#  mild conditions (no force), and the engineering cost (each lock needs its
#  own key). The branch-level analogy in `white/__init__.py` is the same
#  framing at a larger scale, deliberately.
# -----------------------------------------------------------------------------
ANALOGY = (
    "An enzyme is a key and conventional chemistry is a hammer. The hammer "
    "will open the box, and it works on any box, but it destroys whatever was "
    "inside that you wanted to keep and leaves splinters to sweep up. The key "
    "opens exactly one lock, silently, with almost no effort. The trade is in "
    "the last part: a hammer needs no preparation, and every new lock needs a "
    "new key cut for it, which is what enzyme engineering is."
)

WHY_IT_MATTERS = (
    "The clearest example is in most homes. Detergent enzymes are why a "
    "domestic wash cleans properly at 30 degrees instead of 60, and a wash at "
    "30 uses roughly a third of the electricity. Across the world's washing "
    "machines that is one of the largest emissions reductions attributable to "
    "any biotechnology, achieved quietly and largely unremarked. Phytase in "
    "animal feed releases phosphorus that pigs and poultry otherwise excrete, "
    "which both reduces the mined phosphate added to feed and reduces the "
    "phosphorus running off into rivers, where it causes algal blooms. Enzymes "
    "in pulp bleaching displaced a share of the chlorine chemistry that paper "
    "mills once relied on. In pharmaceutical manufacture, enzymatic routes have "
    "replaced multi-step syntheses and eliminated tonnes of solvent per tonne "
    "of product. The limits are real and are not marketing problems. An enzyme "
    "is a protein: it denatures, it is inhibited, it prefers water when much of "
    "chemistry is done in solvents, and its operating lifetime rather than its "
    "raw speed usually decides whether a process is affordable. Where those "
    "constraints bind, conventional chemistry remains the better answer, and "
    "this record says so rather than claiming the field for everything."
)
