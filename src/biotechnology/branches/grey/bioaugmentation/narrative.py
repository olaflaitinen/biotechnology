# =============================================================================
#  biotechnology.branches.grey.bioaugmentation.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS IS THE ONLY RECORD IN THE LIBRARY WHOSE SUBJECT USUALLY FAILS.
#
#  That is not an editorial judgement imposed from outside. It is the field's
#  own repeated finding, established across four decades of controlled
#  comparisons, and the honest way to write the record is to lead with it.
#  Every other record here describes something that works and then qualifies
#  it. This one describes something that does not work, and then identifies
#  the specific conditions under which it does.
#
#  THE REASON IS ECOLOGICAL RATHER THAN TECHNICAL, WHICH IS WHY IMPROVING THE
#  PRODUCT DOES NOT HELP. An introduced strain arrives into a community that
#  is already there because it is adapted to those exact conditions. It is
#  outnumbered, unacclimatised, grazed by protozoa, and competing for a carbon
#  source the residents are already using. Selecting a better degrader in the
#  laboratory optimises the wrong variable: the problem is not that the strain
#  degrades poorly, it is that the strain does not survive.
#
#  AND YET THE RECORD IS NOT A DISMISSAL. There is one clean, well-documented,
#  commercially routine case where bioaugmentation is the correct answer, and
#  it is correct for a reason that predicts exactly when the technique works:
#  the capability was genuinely absent. Establishing that distinction is what
#  this record is for.
#
#      IF THE CAPABILITY IS PRESENT, FEED IT. IF IT IS ABSENT, ADD IT.
#      ALMOST ALL THE FAILURES ARE THE FIRST CASE TREATED AS THE SECOND.
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
    "Introducing organisms into an environment to perform a degradation, "
    "which usually fails because the resident community outcompetes them, and "
    "which works where the capability was genuinely absent."
)

# -----------------------------------------------------------------------------
#  Structure: (a) what it is and the finding, (b) why it fails, (c) the case
#  where it works and what that case has in common, (d) how to tell the two
#  apart before spending money.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) what it is, and the finding stated immediately
    "Bioaugmentation is the deliberate introduction of microorganisms into an "
    "environment to carry out a degradation the resident community is not "
    "performing. It is intuitive, it is commercially available, and controlled "
    "field comparisons have found for four decades that it usually does not "
    "outperform simply supplying oxygen or nutrients to the organisms already "
    "present. That result has been reproduced across contaminated soil, "
    "wastewater plants, agricultural soil and the gut, which is a strong "
    "enough pattern to state as the record's central content rather than as a "
    "caveat at the end of it. "
    # (b) why, and why it is not a product problem
    "The reason is ecological and not technical. A resident community occupies "
    "a site because it is adapted to that site: to its temperature, its pH, "
    "its moisture, its predators and its available carbon. An introduced "
    "strain arrives outnumbered by many orders of magnitude, unacclimatised, "
    "grazed by protozoa, and competing for substrate against organisms that "
    "have been using it for years. Introduced populations therefore decline "
    "rapidly, commonly by orders of magnitude within weeks, whether or not "
    "they are good degraders. This is why selecting a stronger degrader in the "
    "laboratory does not fix the problem: the constraint is survival rather "
    "than capability, and product improvement addresses the wrong variable. "
    # (c) the exception, and the rule it reveals
    "There is one clear and commercially routine exception, and it is "
    "instructive rather than embarrassing. Complete reductive dechlorination "
    "of chlorinated solvents to harmless ethene requires organisms of the "
    "genus Dehalococcoides, and many contaminated aquifers do not contain "
    "them. Where they are absent the process stalls at vinyl chloride, which "
    "is more toxic than the compound it came from. Adding a characterised "
    "dechlorinating consortium works reliably in that setting, and it works "
    "because the capability was genuinely missing rather than merely "
    "underfed. The same logic explains the other legitimate cases: starting a "
    "new anaerobic digester, and recovering a wastewater plant whose community "
    "has been killed by a toxic discharge. In each, there is no incumbent to "
    "compete with. "
    # (d) the diagnostic that decides
    "The practical question is therefore diagnostic rather than commercial. "
    "Molecular methods can establish, before anything is purchased, whether "
    "the relevant organisms and functional genes are present at the site. If "
    "they are, the correct intervention is biostimulation: supply what is "
    "limiting and the residents will do the work. If they are demonstrably "
    "absent, augmentation is justified. Almost every documented failure is the "
    "first case treated as the second."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "The obvious way to clean up pollution with bacteria is to buy some "
    "bacteria and pour them on. It sounds sensible and it usually does not "
    "work. The ground already contains billions of microbes that live there "
    "because they suit the conditions, and the newcomers are outnumbered, out "
    "of their element, and eaten by other organisms, so they mostly die "
    "within a few weeks. In most cases the microbes needed are already there "
    "and are simply short of oxygen, so feeding the residents beats importing "
    "strangers. There is one important exception. Some pollution needs a very "
    "particular kind of bacterium, and some sites genuinely do not have it. "
    "Adding it there works well, and it works precisely because nothing was "
    "already doing the job."
)

# -----------------------------------------------------------------------------
#  The gardener analogy. Chosen because it carries the competition argument
#  and the exception in the same image, and because it makes clear that the
#  failure is about establishment rather than about the quality of what was
#  introduced.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is planting seedlings in an established meadow. The meadow is full "
    "already, everything in it is suited to that soil and that weather, and "
    "the seedlings are shaded out within a season no matter how good the "
    "variety was. Buying better seedlings does not help, because the problem "
    "was never their quality. What does help is planting into bare ground, "
    "which is what starting a new digester amounts to, or planting something "
    "the meadow genuinely does not contain, which is what the dechlorinating "
    "cultures are."
)

WHY_IT_MATTERS = (
    "Bioaugmentation products are sold widely to municipalities, farmers, "
    "industrial operators and homeowners, and most of the money spent on them "
    "buys an effect that controlled comparisons do not detect. That is a "
    "consumer protection matter as much as a scientific one, and it is "
    "recorded here because the buyers are frequently small operators without "
    "the means to run a controlled trial of their own. The finding also "
    "matters for what it saves: knowing that the residents can usually do the "
    "work redirects money toward supplying oxygen or nutrients, which is "
    "cheaper and which is what the evidence supports. "
    "The legitimate cases are genuinely valuable and should not be lost in the "
    "scepticism. Dechlorination augmentation resolves plumes that would "
    "otherwise stall at a more toxic intermediate, and rapid seeding restores "
    "a wastewater plant after a toxic discharge in days rather than weeks, "
    "which is a real public health outcome. "
    "There is a wider lesson worth drawing out. The same pattern appears in "
    "agricultural soil in `green.biofertilisers` and in the human gut in "
    "`yellow.probiotics_and_prebiotics`: three separate fields, decades apart, "
    "each independently learning that established microbial communities resist "
    "invasion. That is one of the most robust generalisations in applied "
    "microbiology, and it is a caution for anything that proposes to fix an "
    "ecosystem by adding a strain to it, including proposals to release "
    "engineered organisms. Finally, the failures are not usually dishonest. "
    "They are laboratory results honestly obtained in flasks where the strain "
    "faced no competition, then sold into fields where it faces nothing else."
)
