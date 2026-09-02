# =============================================================================
#  biotechnology.branches.green.biofertilisers.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two facts frame this record and both belong in the reader's head before any
#  description of the microbiology.
#
#  The first is scale. Manufacturing synthetic nitrogen fertiliser by the
#  Haber-Bosch process consumes on the order of one to two per cent of global
#  primary energy and supplies the nitrogen in roughly half the protein eaten
#  by humanity. Any biological substitution therefore matters at planetary
#  scale even where it replaces only part of the load.
#
#  The second is that this is the field in this branch with the widest gap
#  between glasshouse results and field results. That gap is not a marketing
#  problem to be explained away; it is the honest state of the evidence, and
#  WHY_IT_MATTERS says so in the same breath as the benefit, because a farmer
#  deciding whether to buy a product deserves both halves.
#
#  The tenant analogy is chosen because it makes the living nature of the
#  product, and therefore its failure modes, immediate.
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
    "Living microbial inoculants that fix nitrogen, solubilise phosphate or "
    "stimulate root growth, substituting for part of the synthetic fertiliser "
    "load."
)

# -----------------------------------------------------------------------------
#  Structure: (a) definition, (b) the four functional groups, (c) the fifth
#  looser category, (d) the constraint that explains the field's reputation.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) definition
    "Biofertilisers are formulated preparations of living microorganisms "
    "applied to seed, root or soil in order to improve nutrient availability. "
    "The product is the organism, not a chemical it makes, which is what "
    "distinguishes the category from a fertiliser and governs everything about "
    "its manufacture, storage and failure. "
    # (b) the four functional groups
    "Four functional groups dominate. Symbiotic nitrogen fixers, chiefly "
    "Rhizobium and Bradyrhizobium, form root nodules on legumes and reduce "
    "atmospheric dinitrogen to ammonia using the nitrogenase enzyme complex, an "
    "irreversibly oxygen-sensitive reaction protected inside the nodule by "
    "leghaemoglobin. Free-living and associative fixers such as Azotobacter and "
    "Azospirillum fix at much lower rates without forming a nodule. "
    "Phosphate-solubilising bacteria and fungi secrete organic acids and "
    "phosphatases that release phosphorus bound to calcium, iron or aluminium, "
    "which is abundant in most soils and unavailable to roots. Arbuscular "
    "mycorrhizal fungi colonise root cortical cells and extend hyphae far "
    "beyond the nutrient depletion zone around the root, functioning as an "
    "extension of the root system in exchange for photosynthate. "
    # (c) the fifth category
    "A fifth, looser category, plant-growth-promoting rhizobacteria, acts "
    "through hormone production, siderophore-mediated iron acquisition and "
    "suppression of pathogens rather than through nutrient supply as such, and "
    "the boundary with `green.biopesticides` is genuinely blurred. "
    # (d) the constraint
    "The binding constraint is establishment in a soil that already has "
    "residents. An inoculant must survive formulation, storage, sowing and "
    "sometimes a seed treatment chemical, then colonise a rhizosphere already "
    "occupied by a native community that is adapted to that soil and vastly "
    "outnumbers it. That is why glasshouse results routinely fail to replicate "
    "in the field, and it is a competition problem rather than a biochemical "
    "one."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Air is nearly four fifths nitrogen, and plants need nitrogen, but they "
    "cannot use it straight from the air. Certain bacteria can. If those "
    "bacteria live in little swellings on a bean plant's roots, they capture "
    "nitrogen from the air and hand it to the plant, and the plant feeds them "
    "sugar in return. Other microbes act like a spade, unlocking nutrients "
    "already in the soil that are chemically stuck and out of reach. "
    "Biofertilisers are these helpful microbes, grown in a factory and added to "
    "the seed or the soil on purpose. Because they are alive, they can also "
    "arrive dead, fail to settle in, or be crowded out by whatever already "
    "lives in that field."
)

# -----------------------------------------------------------------------------
#  The tenant analogy. Its limit is the field's actual problem: a tenant has to
#  get along with the neighbours, and the neighbours were there first.
# -----------------------------------------------------------------------------
ANALOGY = (
    "Fertiliser is delivering groceries to the door. A biofertiliser is "
    "installing a tenant in the basement who grows food and shares it, and who "
    "keeps doing so all season without another delivery. The catch is exactly "
    "the catch with tenants: they are alive. They can arrive in poor health, "
    "refuse to settle in, or be pushed out by whoever already lives in the "
    "building. The last of those is the usual reason a product that worked in "
    "a glasshouse does nothing in a field."
)

WHY_IT_MATTERS = (
    "Synthetic nitrogen fertiliser is energy-intensive to make, expensive to "
    "buy, and when it runs off it is the primary cause of eutrophication in "
    "rivers and coastal seas. Biological fixation in a well-nodulated legume "
    "crop can supply the equivalent of one to three hundred kilograms of "
    "nitrogen per hectare per year at essentially no emissions cost, and for a "
    "farmer facing volatile fertiliser prices, a few euro of inoculant against "
    "a hundred euro of urea is an obvious trade. The honest qualifier is that "
    "it is an obvious trade only when the product works, and field results are "
    "far less consistent than glasshouse results. Much of the market is "
    "unregulated in practice: independent testing has repeatedly found products "
    "containing far fewer viable cells than the label claims, or the wrong "
    "organism, or nothing living at all. That inconsistency has done more "
    "damage to the credibility of the category than any scientific limitation, "
    "because a farmer who buys a dead product once does not buy a live one "
    "afterwards. And nitrogen fixation remains largely confined to legumes; "
    "transferring it to cereals has been an active goal for fifty years and "
    "has not arrived."
)
