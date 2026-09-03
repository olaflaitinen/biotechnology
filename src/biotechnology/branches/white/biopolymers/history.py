# =============================================================================
#  biotechnology.branches.white.biopolymers.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks.
#  This record has two, and the second is among the clearest cases anywhere in
#  the library of a marketing claim that survived for two decades because the
#  distinction it exploited was one the public had no way to check.
#
#  SUBTYPE-SPECIFIC NOTE
#  The timeline opens with the same correction as `white.biobased_chemicals`,
#  and it is even more emphatic here: PLASTICS BEGAN BIOBASED. Celluloid, made
#  from cellulose, was commercialised in 1869; casein plastics followed in
#  1897. The first fully synthetic polymer arrived only in 1907, and petroleum
#  feedstock dominated only from the middle of the twentieth century.
#
#  So this record is not introducing a novelty. It is attempting a return, and
#  the material it competes against is one that already displaced its
#  predecessor on cost and performance.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  PLASTICS BEGAN BIOBASED
    # =========================================================================
    Milestone(
        1869,
        "Celluloid, made from cellulose, is commercialised as the first "
        "widely used plastic",
        note=(
            "A biobased polymer, developed partly to replace ivory. The "
            "plastics industry began with a modified natural polymer and moved "
            "to petroleum only later, which is the ordering this record's "
            "readers most often have backwards."
        ),
    ),
    Milestone(
        1897,
        "Casein plastics are produced from milk protein",
        note=(
            "Used for buttons, buckles and fittings for decades. Recorded "
            "because it demonstrates that a biobased plastic industry existed "
            "and was displaced, rather than never having been tried."
        ),
    ),
    Milestone(
        1907,
        "The first fully synthetic polymer is produced",
        note=(
            "The beginning of the transition. Petroleum feedstock came to "
            "dominate through the middle of the century on cost and "
            "performance, and that is the incumbent this record competes with."
        ),
    ),
    # =========================================================================
    #  THE BIOLOGICAL POLYMERS ARE DISCOVERED
    # =========================================================================
    Milestone(
        1926,
        "Polyhydroxybutyrate is discovered as a storage granule inside "
        "bacteria",
        note=(
            "A polyester that a living cell makes for itself as a carbon "
            "reserve. Because environmental organisms already possess the "
            "enzymes to consume it, it is biodegradable in soil and seawater "
            "rather than only in an industrial composter, which is the property "
            "that still distinguishes this family from every other biopolymer."
        ),
    ),
    Milestone(
        1932,
        "Lactide polymerisation to polylactic acid is demonstrated and set "
        "aside as impractical",
        note=(
            "The molecular weight achievable at the time was too low for a "
            "useful material, and the work was abandoned. It waited sixty years "
            "for cheap fermentative lactic acid and better ring-opening "
            "catalysis to make it viable."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE RIGHT MATERIAL, THE WRONG DECADE
    # =========================================================================
    Milestone(
        1990,
        "A bacterial polyhydroxyalkanoate copolymer is commercialised and "
        "marketed in consumer packaging",
        note=(
            "Genuinely biodegradable in ordinary environments, produced by "
            "fermentation, and sold in a shampoo bottle as a demonstration. It "
            "was a real product with real properties."
        ),
    ),
    Milestone(
        2001,
        "Commercial polyhydroxyalkanoate production is discontinued after "
        "successive ownership changes",
        note=(
            "The material cost several times more than polyethylene, "
            "recovering an intracellular polymer proved expensive, and neither "
            "regulation nor public concern about plastic waste was yet strong "
            "enough to pay the premium. The business passed between owners and "
            "production ceased. It is recorded as a setback because nothing was "
            "wrong with the material: the environmental case that would have "
            "supported it arrived roughly twenty years too late, and the field "
            "has been rebuilding that capacity since."
        ),
    ),
    # =========================================================================
    #  THE MATERIAL THAT DID SCALE
    # =========================================================================
    Milestone(
        2002,
        "A large-scale polylactic acid plant begins operation",
        note=(
            "Fermentative lactic acid at commodity scale, polymerised through "
            "lactide. It made polylactic acid the first biobased compostable "
            "polymer available in genuine industrial quantity, and it remains "
            "the reference material for the whole category."
        ),
    ),
    Milestone(
        2010,
        "Bio-based polyethylene from sugarcane enters commercial production",
        note=(
            "Chemically identical to fossil polyethylene, fully biobased, and "
            "not biodegradable at all. It is the single clearest demonstration "
            "that the two axes in `narrative.py` are independent, and it is "
            "recycled in the ordinary polyethylene stream."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A CLAIM THAT WORKED BECAUSE NOBODY COULD CHECK IT
    # =========================================================================
    Milestone(
        2019,
        "Oxo-degradable plastics are restricted after being marketed for years "
        "as degradable",
        note=(
            "Additives caused conventional plastic to fragment on exposure to "
            "light and heat. Fragmentation is not mineralisation: the material "
            "became small pieces rather than carbon dioxide and biomass, which "
            "is a mechanism for producing microplastics rather than for "
            "removing plastic. The products were sold on a distinction that "
            "consumers had no means of verifying, and it took roughly two "
            "decades and a legislative restriction to settle. It is the reason "
            "`metrics.py` records disintegration and mineralisation as separate "
            "quantities."
        ),
    ),
    # =========================================================================
    #  REGULATION DECLINES TO TREAT COMPOSTABLE AS DIFFERENT
    # =========================================================================
    Milestone(
        2019,
        "Single-use plastic restrictions apply to compostable plastics as well "
        "as conventional ones",
        note=(
            "A significant and widely misunderstood decision: compostable "
            "single-use items were not exempted from bans. The reasoning was "
            "that the collection infrastructure to compost them does not "
            "generally exist, so in practice they behave as litter and as "
            "recycling stream contaminants. It confirms the position taken "
            "throughout this record that infrastructure, not chemistry, is the "
            "binding constraint."
        ),
    ),
    Milestone(
        2022,
        "Policy frameworks begin specifying WHERE a material must biodegrade "
        "rather than whether it does",
        note=(
            "Guidance distinguishing industrial composting, home composting, "
            "soil and marine environments, and restricting compostable "
            "materials to applications where collection actually exists, such "
            "as caddy liners and agricultural mulch. It is the regulatory form "
            "of this record's central argument."
        ),
    ),
    Milestone(
        2023,
        "Chemical recycling of biopolyesters back to monomer is demonstrated at "
        "pilot scale",
        note=(
            "For a durable article this is frequently a better end of life than "
            "composting, which recovers no material value. It reframes "
            "biodegradability as one disposal option suited to specific "
            "applications rather than as a universal virtue, which is where the "
            "field's thinking has settled."
        ),
    ),
)
