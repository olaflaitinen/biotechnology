# =============================================================================
#  biotechnology.branches.green.plant_tissue_culture.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is the invisible foundation of the green branch, and the public
#  register is written to make that visible rather than to describe a
#  technique.
#
#  Every transgenic plant and every edited plant that has ever existed was
#  regenerated from a single cell in a sterile jar. When a genotype is
#  described as impossible to engineer, the failure is almost never DNA
#  delivery; it is that nobody can persuade that variety to become a plant
#  again. Two neighbouring records depend on this one and neither says so as
#  plainly as it should.
#
#  The photocopier analogy is chosen because it captures both what the
#  technique gives, meaning exact copies rather than a new edition, and what it
#  costs, meaning that a photocopy of a photocopy eventually degrades, which is
#  precisely somaclonal variation.
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
    "Regenerating whole plants from cells, tissues or organs on sterile media "
    "to mass-produce uniform, disease-free planting material."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the property being exploited, (b) how the medium controls
#  what happens, (c) the two regeneration routes and the virus trick,
#  (d) the constraint that limits everything downstream.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the property
    "Plant tissue culture exploits totipotency: most living plant cells retain "
    "the full genetic programme needed to rebuild an entire organism, which is "
    "a property animal cells lost long ago. "
    # (b) the medium
    "An explant, meaning a shoot tip, a leaf disc, an anther or an immature "
    "embryo, is surface-sterilised and placed on a defined medium containing "
    "mineral salts, sucrose, vitamins and, critically, a balance of two hormone "
    "classes. The ratio does the work: a high cytokinin to auxin ratio favours "
    "shoot formation, the reverse favours roots, and an intermediate ratio "
    "produces undifferentiated callus. Skoog and Miller established that "
    "relationship in 1957, and it remains the single most useful fact in the "
    "field. "
    # (c) the two routes, and the virus trick
    "Regeneration proceeds either by organogenesis, in which shoots and roots "
    "form successively from callus or directly from tissue, or by somatic "
    "embryogenesis, in which bipolar embryos form and can be encapsulated as "
    "synthetic seed. Meristem culture exploits a separate accident of plant "
    "biology: the apical dome is usually virus-free, because viral movement "
    "through the plant lags behind cell division at the growing tip, so "
    "excising a fragment under a millimetre across yields clean stock from an "
    "infected mother plant. "
    # (d) the constraint
    "The binding constraint is genotype-dependent recalcitrance. Regeneration "
    "protocols are developed species by species and often variety by variety, "
    "and elite commercial lines are frequently the hardest of all. That single "
    "fact limits `green.plant_genetic_engineering` and "
    "`green.agricultural_genome_editing` more than any property of the DNA "
    "delivery methods they use."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "A cutting from a houseplant will grow roots in a glass of water. Plant "
    "tissue culture is that idea taken to its limit. With the right nutrients "
    "and the right balance of two plant hormones, a piece of tissue smaller "
    "than a grain of rice can be persuaded to grow into a complete plant, and "
    "each of those plants can be divided again. Because everything is done in "
    "sealed sterile jars, the resulting plants carry none of the diseases the "
    "parent may have had, and every one of them is genetically identical to "
    "that parent. Almost every banana eaten in the world was produced this way."
)

# -----------------------------------------------------------------------------
#  The photocopier analogy. Its limit is the field's actual quality problem:
#  copies of copies degrade, which is exactly somaclonal variation.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is photocopying rather than reprinting. A seed is a new edition with "
    "fresh typesetting, and every one comes out slightly different. Tissue "
    "culture makes exact copies of a page you already like, and it makes them "
    "clean, without the coffee stains the original picked up. The comparison "
    "holds all the way to the failure mode: photocopy a photocopy of a "
    "photocopy for long enough and errors creep in, which is why commercial "
    "protocols cap how many times a line may be subcultured before it is "
    "started again from stock."
)

WHY_IT_MATTERS = (
    "Almost every banana eaten in the world is a clone produced this way, and "
    "the technique keeps the virus-free potato, sugarcane, strawberry, cassava "
    "and orchid industries running. For a smallholder, certified disease-free "
    "planting material can be the difference between a normal harvest and a "
    "loss of a third of the crop, and cassava and sweet potato programmes "
    "across Africa and Asia depend on it entirely. It is also the quiet "
    "prerequisite for genetic engineering and genome editing, neither of which "
    "can deliver a plant without it. The costs are specific and are usually "
    "left out. Labour dominates the economics, because a skilled operator "
    "dividing plantlets by hand is the whole production line, and that keeps "
    "micropropagation viable only for high-value or high-volume crops. "
    "Clonality means an entire industry can share one susceptibility: the "
    "Cavendish banana is genetically uniform across the planet and is losing "
    "ground to a soil fungus that no fungicide reaches. And the technique that "
    "conserves rare genotypes in a genebank is the same one that, applied "
    "commercially, replaces thousands of local varieties with one."
)
