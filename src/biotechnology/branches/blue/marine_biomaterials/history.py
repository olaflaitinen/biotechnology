# =============================================================================
#  biotechnology.branches.blue.marine_biomaterials.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two: an application that had to be abandoned because the
#  source could not be harvested, and a persistent failure of standardisation
#  that has kept promising materials out of regulated use for decades.
#
#  SUBTYPE-SPECIFIC NOTE
#  The coral bone graft story, running from 1974 to the synthetic conversion
#  routes that replaced it, is the most instructive sequence in this record and
#  is unusual in the library: a material worked clinically, and the reason it
#  had to be replaced had nothing to do with its performance.
#
#  Coral skeleton has a pore size and interconnectivity close to human
#  cancellous bone, which is why it guided ingrowth so well. It was also being
#  cut from reefs. The response was not to abandon the property but to
#  reproduce it, first by converting coral to hydroxyapatite and eventually by
#  making synthetic scaffolds with the same architecture. THE STRUCTURE WAS THE
#  PRODUCT, AND THE ORGANISM WAS ONLY ITS FIRST MANUFACTURER.
#
#  That is the argument this record makes about nacre, byssus and biosilica as
#  well, and the coral case is where it was actually settled in practice.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE MATERIALS ARE IDENTIFIED
    # =========================================================================
    Milestone(
        1811,
        "Chitin is isolated from fungi and later identified in crustacean "
        "shell",
        note=(
            "Among the earliest polymers to be characterised, and among the "
            "last to be used industrially. It is the second most abundant "
            "polymer on Earth after cellulose and was treated as waste for most "
            "of the two centuries after its discovery."
        ),
    ),
    Milestone(
        1881,
        "Agar enters microbiology as a solid culture medium",
        note=(
            "The property that mattered was thermal hysteresis: agar melts near "
            "boiling and sets well below incubation temperature, so a plate "
            "stays solid where gelatin does not. Recorded in "
            "`blue.seaweed_cultivation` from the cultivation side and here as a "
            "material, because it is the same substance answering two different "
            "questions."
        ),
    ),
    Milestone(
        1881,
        "Alginate is described in brown seaweed",
        note=(
            "Its gelation with calcium under mild conditions is what every "
            "later application rests on, from dental impressions to cell "
            "encapsulation, because a gel that forms at room temperature "
            "without solvent is a gel a living cell can survive."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A MATERIAL THAT WORKED AND COULD NOT BE HARVESTED
    # =========================================================================
    Milestone(
        1974,
        "Coral skeleton is used as a bone graft substitute",
        note=(
            "The pore size and interconnectivity of certain corals resemble "
            "human cancellous bone closely enough to guide bone ingrowth, and "
            "clinically it worked. It was cut from reefs, which was "
            "unacceptable at any scale that would have mattered, and the "
            "constraint was ecological rather than medical."
        ),
    ),
    Milestone(
        1980,
        "Hydrothermal conversion of coral carbonate to hydroxyapatite is "
        "developed",
        note=(
            "Keeping the architecture and replacing the chemistry, which "
            "reduced the reef material required per implant. It was the first "
            "step of the argument this record makes generally: the structure "
            "was the product and the organism was only its first manufacturer. "
            "Fully synthetic scaffolds with the same architecture followed."
        ),
    ),
    # =========================================================================
    #  MARINE POLYMERS BECOME MEDICAL PRODUCTS
    # =========================================================================
    Milestone(
        1983,
        "Alginate cell encapsulation is demonstrated for transplanted cells",
        note=(
            "Cells enclosed in a gel permeable to nutrients and to their "
            "product but not to immune cells. The reason alginate rather than a "
            "synthetic polymer is that gelation happens in seconds, at room "
            "temperature, in a calcium solution a cell survives."
        ),
    ),
    Milestone(
        1983,
        "Alginate wound dressings enter clinical use",
        note=(
            "Absorb exudate, gel in place and lift off without tearing new "
            "tissue, which is the property clinicians actually value. It "
            "remains among the most successful marine biomaterials by volume."
        ),
    ),
    Milestone(
        2003,
        "Chitosan haemostatic dressings are adopted for trauma care",
        note=(
            "The mechanism does not depend on the patient's own clotting "
            "cascade, so the dressings work in anticoagulated patients and in "
            "coagulopathy. Adoption came through military and emergency medicine "
            "rather than through the routes most medical materials take."
        ),
    ),
    # =========================================================================
    #  STUDYING STRUCTURES RATHER THAN EXTRACTING SUBSTANCES
    # =========================================================================
    Milestone(
        2007,
        "Mussel adhesive catechol chemistry is characterised and reproduced "
        "synthetically",
        note=(
            "The modified amino acid that lets a mussel bond to wet rock was "
            "identified and incorporated into synthetic polymers. It solved a "
            "problem synthetic adhesives handle poorly, and it did so without "
            "harvesting a single mussel, which is the pattern the coral case "
            "had established."
        ),
    ),
    Milestone(
        2008,
        "Nacre-inspired layered composites are produced by assembly methods",
        note=(
            "Reproducing the layered arrangement rather than the composition, "
            "since the toughness of nacre belongs to the architecture. It is "
            "difficult, slow and remains largely at laboratory scale, because "
            "an arrangement built over months by a living organism is not "
            "easily assembled in a factory."
        ),
    ),
    Milestone(
        2015,
        "Marine polysaccharide bioinks are adopted in three-dimensional "
        "bioprinting",
        note=(
            "Alginate became a default bioink for the same reason it became an "
            "encapsulation material three decades earlier: it gels rapidly under "
            "conditions living cells tolerate. The application is new and the "
            "property being used is not."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE PROBLEM THAT HAS NOT BEEN SOLVED
    # =========================================================================
    Milestone(
        2018,
        "Absence of standardisation is identified as the principal barrier to "
        "regulated use of marine biomaterials",
        note=(
            "Reviews across the field converged on the same conclusion: the "
            "obstacle is not discovery but specification. Materials sold under "
            "one name differ in deacetylation, uronic acid ratio, sulphation "
            "and molecular weight distribution, results are not reproducible "
            "between laboratories, and a device file cannot be built on a raw "
            "material that varies by season and species. It is recorded as a "
            "setback because the diagnosis is decades old, is widely agreed, "
            "and the reference materials and specifications that would fix it "
            "have largely still not been produced."
        ),
    ),
    Milestone(
        2020,
        "Valorisation of seafood processing waste becomes a policy objective "
        "in its own right",
        note=(
            "Circular economy and waste directives made shell and skin streams "
            "a target for recovery rather than disposal, which gave this record "
            "an economic driver from outside itself. It is the clearest reason "
            "to expect the field to grow, and it does not address the "
            "standardisation problem above at all."
        ),
    ),
)
