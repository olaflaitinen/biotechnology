# =============================================================================
#  biotechnology.branches.green.biofertilisers.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks;
#  this record has two of different kinds. The 1913 entry is a setback only in
#  the sense that a competing technology arrived and was better at the job for
#  a century. The 1980s entry is the field's own doing: a market that sold dead
#  product and spent its credibility.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the oldest commercial biotechnology in the taxonomy. Nitragin was
#  sold in 1895, thirty years before penicillin was noticed and eighty-seven
#  years before the first recombinant medicine. A farmer in the 1890s could buy
#  a living microbial product off a shelf.
#
#  The 1888 and 1913 entries should be read together, because they set up the
#  whole record: Beijerinck showed that biology could fix nitrogen, and
#  twenty-five years later Haber and Bosch showed that chemistry could do it
#  faster. Everything since has been an argument about the terms of that trade.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE OBSERVATION, LONG BEFORE THE EXPLANATION
    # =========================================================================
    Milestone(
        -300,
        "Legume rotation is recorded as a practice that restores soil fertility",
        note=(
            "Theophrastus and later Roman writers describe it without any idea "
            "why it works. The practice preceded the explanation by more than "
            "two thousand years."
        ),
    ),
    Milestone(
        1886,
        "Hellriegel and Wilfarth show that legumes obtain nitrogen from the air "
        "and that nodules are required",
        note=(
            "The experiment that connected the rotation practice to a "
            "mechanism, by growing legumes in sterile sand with and without "
            "soil extract."
        ),
    ),
    Milestone(
        1888,
        "Beijerinck isolates the root nodule bacterium in pure culture",
        note=(
            "Naming the organism made it a product. Seven years later it was on "
            "sale."
        ),
    ),
    # =========================================================================
    #  THE OLDEST COMMERCIAL BIOTECHNOLOGY IN THIS TAXONOMY
    # =========================================================================
    Milestone(
        1895,
        "The first commercial legume inoculant, Nitragin, is sold",
        note=(
            "Thirty-three years before penicillin was noticed and eighty-seven "
            "before the first recombinant medicine. A living microbial product, "
            "on a shelf, for farmers."
        ),
    ),
    # =========================================================================
    #  THE COMPETITOR THAT WON FOR A CENTURY
    # =========================================================================
    Milestone(
        1913,
        "The Haber-Bosch process is industrialised, making synthetic nitrogen "
        "fertiliser available at scale",
        note=(
            "It now supplies the nitrogen in roughly half the protein eaten by "
            "humanity and consumes one to two per cent of global primary "
            "energy. For most of the twentieth century it made biological "
            "fixation an agronomic curiosity rather than an economic "
            "proposition, and the entire modern interest in this record follows "
            "from energy prices and eutrophication making that trade look "
            "different."
        ),
    ),
    # =========================================================================
    #  THE MECHANISM
    # =========================================================================
    Milestone(
        1960,
        "The nitrogenase enzyme complex is characterised",
        note=(
            "Irreversibly inactivated by oxygen, which is why the nodule "
            "produces leghaemoglobin to keep oxygen away from it, and why "
            "transferring fixation to a cereal has proved so much harder than "
            "it sounds."
        ),
    ),
    Milestone(
        1975,
        "Arbuscular mycorrhizal inoculum is produced commercially",
        note=(
            "Constrained then and now by the fact that these fungi are obligate "
            "symbionts and cannot be grown without a host plant."
        ),
    ),
    # =========================================================================
    #  THE FIELD DAMAGES ITSELF
    # =========================================================================
    Milestone(
        1985,
        "Independent surveys of commercial inoculants find widespread quality "
        "failure",
        note=(
            "Products across several markets were found to contain far fewer "
            "viable cells than labelled, the wrong organism, or nothing living "
            "at all. Recorded as a setback because it is the clearest instance "
            "in this branch of a field losing its market for reasons that were "
            "entirely within its own control, and the reputational effect "
            "outlasted the technical fix by decades."
        ),
    ),
    # =========================================================================
    #  UNDERSTANDING WHAT IS ALREADY THERE
    # =========================================================================
    Milestone(
        2005,
        "Rhizosphere microbiome sequencing becomes routine",
        note=(
            "Made it possible to ask what an inoculant is actually competing "
            "with, which reframed the central problem from fixation rate to "
            "competitive establishment."
        ),
    ),
    Milestone(
        2012,
        "Large-scale field syntheses conclude that inoculant response is "
        "strongly conditional on soil, season and native population",
        note=(
            "Not a negative result but a clarifying one: the question stopped "
            "being whether biofertilisers work and became where and when they "
            "work, which is a far more useful question and a much harder one "
            "to sell against."
        ),
    ),
    # =========================================================================
    #  A REGULATORY CATEGORY, AT LAST
    # =========================================================================
    Milestone(
        2019,
        "EU Regulation (EU) 2019/1009 creates a single market category for "
        "fertilising products including microbial plant biostimulants",
        note=(
            "For the first time a defined legal product class with composition "
            "and labelling requirements, in a market where quality failure had "
            "been the main obstacle for over a century."
        ),
    ),
)
