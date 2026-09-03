# =============================================================================
#  biotechnology.branches.yellow.biofortification.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped BY NUTRIENT rather than by crop, because the
#  nutrient determines the difficulty. Provitamin A can be seen and therefore
#  meets consumer resistance; iron and zinc are invisible and meet
#  bioavailability problems instead; and a nutrient absent from the crop
#  entirely requires engineering rather than breeding.
#
#  Within each group the entries are ordered by DEPLOYMENT rather than by
#  scientific interest, so the varieties in farmers' fields come before the
#  ones in the literature. That ordering makes visible a fact the coverage of
#  this field obscures: the conventionally bred crops have fed people and the
#  engineered ones have mostly not.
#
#  TECHNOLOGIES separate the two routes deliberately, and add a third group for
#  the work that decides whether any of it reaches anyone, which is delivery.
#  A biofortified variety that farmers do not plant is a publication.
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
#  By nutrient, and within each by deployment rather than by scientific
#  interest.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- provitamin A: visible, which is both the evidence and the obstacle -----
    "Orange-fleshed sweet potato, conventionally bred, distributed at scale "
    "across sub-Saharan Africa with measured improvements in vitamin A status, "
    "which is the field's clearest delivered success",
    "Provitamin A maize, conventionally bred, released in several countries and "
    "facing consumer preference for white maize in populations accustomed to it",
    "Provitamin A cassava, bred for a crop that is a staple for hundreds of "
    "millions and is otherwise almost purely starch",
    "Provitamin A rice, which requires genetic engineering because the pathway "
    "is absent from the endosperm entirely, and whose deployment history is "
    "recorded in `history.py` as a caution rather than a success",
    # -- iron: invisible, and limited by what the same grain contains ------------
    "Iron-biofortified beans, released widely in east and central Africa and in "
    "Latin America, where beans are a staple and the baseline iron content is "
    "already relatively high",
    "Iron-biofortified pearl millet, released in India, in a crop grown in "
    "areas with high deficiency prevalence and poor access to fortified foods",
    "Iron-biofortified wheat and rice varieties, where the gain is constrained "
    "by the low baseline and by phytate in the same grain",
    # -- zinc: the same problem, and a larger deficiency burden -------------------
    "Zinc-biofortified wheat, released in south Asia where wheat is the staple "
    "and zinc deficiency is widespread",
    "Zinc-biofortified rice and maize varieties",
    "Zinc-biofortified beans and lentils, which combine a reasonable baseline "
    "with a crop people already eat daily",
    # -- reducing what blocks absorption, which is the other half of the problem ---
    "Low-phytate varieties, which raise the availability of the iron and zinc "
    "already present rather than adding more, and which trade against seed "
    "viability because phytate is the seed's phosphorus store",
    "Varieties bred for promoter compounds that enhance absorption, which is "
    "the less explored complement to reducing inhibitors",
    # -- other nutrients, mostly still in development ------------------------------
    "Folate-biofortified rice and other staples, addressing neural tube defects",
    "Provitamin A and folate banana varieties for regions where banana is a "
    "staple rather than a fruit",
    "Amino acid composition improvement in maize and cassava, addressing "
    "protein quality rather than micronutrients",
)


# =============================================================================
#  TECHNOLOGIES
#  The two routes, then the delivery work that decides whether either matters.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- route one: use variation that already exists ---------------------------
    "Germplasm screening across genebank collections for existing variation in "
    "micronutrient content, which is where every conventional programme starts "
    "and which depends entirely on collections assembled decades earlier",
    "Marker-assisted selection for micronutrient traits, which allows selection "
    "on a seedling rather than on a harvested and analysed grain",
    "Genomic selection for traits controlled by many small-effect loci, drawing "
    "directly on `green.molecular_plant_breeding`",
    "Crossing biofortified traits into locally adapted and preferred varieties, "
    "which is the unglamorous majority of the work and the part that determines "
    "whether farmers plant it",
    # ---- route two: build a pathway that is not there ---------------------------
    "Transgenic introduction of a complete biosynthetic pathway, required where "
    "the crop cannot make the nutrient at all, as for provitamin A in rice "
    "endosperm",
    "Metabolic engineering of nutrient uptake, translocation and storage in the "
    "edible tissue rather than in the leaves",
    "Genome editing of transporters and of phytate biosynthesis, which in some "
    "jurisdictions avoids the regulatory position that has constrained the "
    "transgenic route",
    # ---- measuring what is actually there and what is absorbed -------------------
    "High-throughput micronutrient analysis, including X-ray fluorescence "
    "screening that measures grain without destroying or dissolving it, which "
    "is what made screening thousands of lines practical",
    "Bioavailability assessment by in vitro digestion, cell models and stable "
    "isotope studies in people, since content and absorbed dose are different "
    "quantities",
    "Retention testing through the actual local processing and cooking, because "
    "a carotenoid that does not survive the pot has not been delivered",
    # ---- delivery, without which none of it reaches anyone ------------------------
    "Participatory variety selection, in which farmers choose among candidates, "
    "which is how yield parity and preference are established rather than "
    "assumed",
    "Seed system development, including community multiplication and vine "
    "distribution for vegetatively propagated crops such as sweet potato",
    "Demand creation and nutrition education, which for a visible trait such as "
    "orange maize is the difference between adoption and rejection",
    "Efficacy and effectiveness trials measuring nutritional status in the "
    "target population, which is the only evidence that the delivery argument "
    "actually holds",
)


# =============================================================================
#  ORGANISMS
#  The staple crops, and the note says why each is a target.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "ipomoea_batatas",  # sweet potato; the field's clearest delivered success
    "oryza_sativa",  # rice; a staple for billions, and provitamin A needs engineering
    "triticum_aestivum",  # wheat; the zinc target in south Asia
    "phaseolus_vulgaris",  # beans; high baseline iron and eaten daily
    "manihot_esculenta",  # cassava; a staple that is otherwise almost pure starch
    "pennisetum_glaucum",  # pearl millet; grown where deficiency prevalence is highest
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "selective_breeding",
    "marker_assisted_selection",
    "genomic_selection",
    "genetic_transformation",
    "genome_editing",
    "x_ray_fluorescence",
    "stable_isotope_analysis",
    "field_trial",
)


# =============================================================================
#  CHALLENGES
#  Yield parity first, because a farmer decides before a nutritionist does.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the farmer's decision comes first ---------------------------------------
    "Yield parity, which is a hard requirement rather than a preference, since "
    "a farmer will not accept a smaller harvest in exchange for a nutrient they "
    "cannot see and whose benefit is invisible and delayed",
    "Adaptation to local conditions, because a biofortified trait in an "
    "unadapted variety is worthless and crossing it into locally preferred "
    "varieties is most of the work",
    "Seed system access, since a variety that exists in a research station and "
    "not in a farmer's hands has delivered nothing",
    # -- the nutrient has to survive and be absorbed --------------------------------
    "Bioavailability, since phytate in cereals binds iron and zinc and limits "
    "how much of an increased content is actually absorbed, which is why "
    "low-phytate breeding is a complement rather than an alternative",
    "Retention through local processing and cooking, particularly for "
    "carotenoids, which degrade with heat, light and storage",
    "The trade between low phytate and seed viability, since phytate is the "
    "seed's phosphorus store and removing it can impair germination and "
    "seedling vigour",
    # -- what people will eat ---------------------------------------------------------
    "Consumer acceptance of visible traits, where orange maize in a population "
    "accustomed to white maize is a preference problem before it is a "
    "nutritional one, and where the visibility that aids adoption messaging "
    "also invites rejection",
    "Sustained consumption, since the benefit depends on the biofortified "
    "variety remaining a substantial part of the diet year after year rather "
    "than being tried once",
    # -- proving it worked ------------------------------------------------------------
    "Demonstrating an effect on nutritional status rather than on grain "
    "content, which requires efficacy trials in the target population and is "
    "far more expensive and slower than the breeding",
    # -- and the constraint that is not agronomic at all ---------------------------------
    "Regulatory and political treatment of the transgenic route, which has been "
    "decisive rather than incidental and which the provitamin A rice history "
    "documents over more than two decades",
    "Dependence on donor funding for crops and populations that no commercial "
    "seed market serves, which makes the field's continuation a policy decision "
    "rather than a market outcome",
    "Genebank dependence, since conventional breeding requires variation that "
    "was collected and conserved decades ago by institutions now underfunded",
)
