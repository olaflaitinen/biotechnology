# =============================================================================
#  biotechnology.branches.blue.marine_natural_products.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has three: a compound that could not be supplied, an
#  industry that withdrew from the field entirely, and a discovery that showed
#  decades of attribution had been wrong.
#
#  SUBTYPE-SPECIFIC NOTE
#  The timeline has an unusual shape. The scientific results improve steadily
#  and the commercial position gets worse, and both are true at once. By the
#  2000s the field had better analytical methods, better screens and better
#  genomics than ever, and large pharmaceutical companies were leaving natural
#  product discovery altogether. That divergence is the honest story and the
#  timeline is written to show it rather than to smooth it.
#
#  The 1951 entry deserves its position. Bergmann's sponge nucleosides did not
#  themselves become drugs; they showed that a nucleoside could carry an
#  unusual sugar and remain biologically active, which is the insight the
#  earliest antiviral and anticancer nucleosides were built on. It is the
#  clearest case in this record of a marine compound mattering as an idea
#  rather than as a product.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  A MARINE COMPOUND AS AN IDEA RATHER THAN A PRODUCT
    # =========================================================================
    Milestone(
        1951,
        "Unusual nucleosides are isolated from a Caribbean sponge",
        note=(
            "The compounds themselves did not become medicines. What they "
            "showed was that a nucleoside could carry a sugar other than ribose "
            "and remain biologically active, and that observation underlies the "
            "antiviral and anticancer nucleoside analogues developed over the "
            "following two decades. It is the clearest case in this record of a "
            "marine natural product mattering as an idea."
        ),
    ),
    Milestone(
        1969,
        "Cytarabine is approved for leukaemia",
        note=(
            "Developed from the sponge nucleoside chemistry of 1951 and made "
            "synthetically from the start, because the molecule was simple "
            "enough that supply was never a question. It remains in use, and it "
            "is the field's first therapeutic success by a route that later "
            "compounds could not follow."
        ),
    ),
    # =========================================================================
    #  THE SEA TURNS OUT TO BE FULL OF CHEMISTRY
    # =========================================================================
    Milestone(
        1974,
        "Systematic screening of marine invertebrate extracts begins at scale",
        note=(
            "Diving and dredging programmes collected and screened thousands of "
            "extracts. Hit rates were encouraging and the collection was, by "
            "later standards, damaging: sampling intensity on reefs and beds "
            "was not sustainable and was not understood at the time to be a "
            "problem."
        ),
    ),
    Milestone(
        1981,
        "Bryostatin is isolated from a bryozoan and immediately poses the "
        "field's supply problem",
        note=(
            "Highly active and present in minute quantity. Obtaining material "
            "for early clinical work required many tonnes of animal for a few "
            "grams. It has been studied for decades and has still not settled "
            "into a manufacturing route, which makes it the standing example of "
            "a compound whose pharmacology was never the obstacle."
        ),
    ),
    Milestone(
        1987,
        "Trabectedin is isolated from a Caribbean tunicate",
        note=(
            "Similarly potent and similarly scarce, at roughly a gram of "
            "compound per tonne of animal. Unlike bryostatin it eventually "
            "found a route, and the difference between the two is the subject "
            "of the 2007 entry."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE INDUSTRY LEAVES
    # =========================================================================
    Milestone(
        1995,
        "Large pharmaceutical companies withdraw from natural product "
        "discovery in favour of combinatorial chemistry and high throughput "
        "screening",
        note=(
            "Natural products were slow, legally complicated after the "
            "Convention on Biological Diversity, and awkward to supply. "
            "Synthetic libraries promised more compounds faster. The libraries "
            "underperformed against expectations, and by then the extraction, "
            "isolation and taxonomic expertise had been dispersed. It is "
            "recorded as a setback because the capability lost was not "
            "rebuilt, and marine compounds that reached development afterwards "
            "did so through small companies and academic groups rather than "
            "through the industry that would have to market them."
        ),
    ),
    # =========================================================================
    #  THE FINDING THAT REDIRECTED THE SUPPLY PROBLEM
    # =========================================================================
    Milestone(
        1997,
        "Evidence accumulates that microbial symbionts, rather than their "
        "invertebrate hosts, produce many attributed compounds",
        note=(
            "Compounds credited to sponges, tunicates and bryozoans for decades "
            "were being made by bacteria living inside them. This changed the "
            "supply problem rather than solving it: the target became culturing "
            "or heterologously expressing a symbiont instead of farming an "
            "animal, and most such symbionts do not grow either. It is recorded "
            "as a setback as well as a discovery, because it showed that a "
            "generation of attribution had been wrong and that aquaculture "
            "efforts aimed at the host had been aimed at the wrong organism."
        ),
    ),
    # =========================================================================
    #  THE COMPOUNDS THAT REACHED PATIENTS
    # =========================================================================
    Milestone(
        2004,
        "Ziconotide is approved for severe chronic pain",
        note=(
            "A cone snail venom peptide, made by peptide synthesis, delivered "
            "directly into the spinal fluid because it survives no other route. "
            "It treats patients who respond to nothing else, and it exists "
            "because a snail evolved a molecule selective for a channel that "
            "terrestrial chemistry had not provided a tool for."
        ),
    ),
    Milestone(
        2007,
        "Trabectedin is approved in Europe, supplied by semisynthesis",
        note=(
            "The supply problem was solved by starting from a compound "
            "available in quantity by bacterial fermentation and converting it "
            "chemically. Twenty years elapsed between isolation and approval, "
            "and almost all of that interval was manufacturing rather than "
            "pharmacology. It is the field's clearest demonstration that supply "
            "is an engineering problem with an engineering answer."
        ),
    ),
    Milestone(
        2010,
        "Eribulin is approved, a simplified synthetic analogue of a sponge "
        "macrolide",
        note=(
            "The natural product was far too complex to manufacture. The "
            "answer was to identify the portion responsible for activity and "
            "build a simpler molecule around it. It established analogue design "
            "as a legitimate supply strategy rather than a compromise."
        ),
    ),
    Milestone(
        2011,
        "An antibody drug conjugate carrying a cytotoxin of marine origin is "
        "approved",
        note=(
            "A molecule too toxic to give systemically became usable when an "
            "antibody restricted where it went. It also solved supply "
            "incidentally, since a targeted payload is needed in milligrams. "
            "Marine chemistry is present in modern targeted cancer therapy "
            "without appearing in its name."
        ),
    ),
    # =========================================================================
    #  READING CHEMISTRY INSTEAD OF EXTRACTING IT
    # =========================================================================
    Milestone(
        2015,
        "Genome mining for biosynthetic gene clusters becomes a standard "
        "discovery route",
        note=(
            "Reading what chemistry an organism can encode rather than what it "
            "happens to be producing. It reduced dependence on collection and "
            "introduced its own difficulty, since the large majority of "
            "predicted clusters are silent under any laboratory condition "
            "anyone has tried."
        ),
    ),
    Milestone(
        2023,
        "The agreement on marine biological diversity beyond national "
        "jurisdiction addresses genetic resources from the high seas",
        note=(
            "Relevant here because a substantial part of this field's "
            "historical collection came from waters where no access rule "
            "existed. The framework governs future activity and leaves the "
            "status of existing libraries, and of compounds already derived "
            "from them, unresolved."
        ),
    ),
)
