# =============================================================================
#  biotechnology.branches.green.plant_tissue_culture.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications are grouped by PURPOSE rather than by species, because the
#  same jar and the same medium serve four completely different goals:
#  multiplying a genotype, cleaning it of disease, rescuing something that
#  would otherwise die, and storing it.
#
#  The fifth group exists because it is the reason two neighbouring records
#  function at all, and it is routinely omitted from descriptions of this
#  field: regeneration is the step that turns a transformed or edited cell back
#  into a plant.
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
#  Grouped by purpose. The same jar, four different goals, plus the one that
#  makes the neighbouring records possible.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- multiplying a genotype -------------------------------------------------
    "Clonal propagation of banana, which supplies almost the entire global "
    "export trade",
    "Micropropagation of orchids, which created the modern cut-flower and "
    "potted orchid industry",
    "Sugarcane and date palm multiplication from elite selections",
    "Somatic embryogenesis in oil palm and in conifer forestry, where seed "
    "propagation loses the selected genotype",
    # -- cleaning it of disease ---------------------------------------------------
    "Virus elimination from potato seed systems by meristem culture, often "
    "combined with thermotherapy",
    "Cassava and sweet potato clean-seed programmes, which underpin food "
    "security across large parts of Africa and Asia",
    "Certified virus-free strawberry and citrus foundation stock",
    # -- rescuing what would otherwise die -----------------------------------------
    "Embryo rescue in wide crosses, where the hybrid embryo forms but the "
    "endosperm fails and the seed would abort",
    "Ovule and anther culture where fertilisation succeeds but development does "
    "not",
    # -- producing haploids and storing genotypes -----------------------------------
    "Anther and microspore culture for doubled-haploid production, reaching "
    "complete homozygosity in one step",
    "In vitro germplasm banks under slow-growth conditions",
    "Cryopreservation of shoot tips for crops whose seed cannot be dried and "
    "frozen, including banana, potato and cassava",
    # -- making the neighbouring records possible -------------------------------------
    "Regeneration of transformed and edited cells into whole plants, without "
    "which no transgenic or genome-edited crop could exist",
    "Protoplast culture and regeneration, the route used for DNA-free editing",
    # -- a product rather than a plant -------------------------------------------------
    "Cell suspension culture for secondary metabolite production, including "
    "paclitaxel and shikonin",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped along the workflow: the medium, getting started cleanly, getting a
#  plant out, scaling it up, and keeping it.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- the medium ----------------------------------------------------------
    "Murashige and Skoog basal medium and its derivatives, still the default "
    "formulation more than sixty years after publication",
    "Auxin to cytokinin ratio control, the lever that decides shoot, root or "
    "callus",
    "Gelling agents and liquid systems, which change oxygen availability and "
    "therefore morphology",
    "Activated charcoal and antioxidants to absorb phenolics released by "
    "wounded tissue",
    # ---- starting cleanly -----------------------------------------------------
    "Surface sterilisation with hypochlorite or mercuric chloride, followed by "
    "rinsing",
    "Laminar flow sterile technique and contamination indexing",
    "Meristem excision under a stereomicroscope, taking domes under one "
    "millimetre",
    "Thermotherapy and chemotherapy before excision to push the virus front "
    "further back",
    "Indexing by ELISA and PCR to confirm the material really is virus-free",
    # ---- getting a plant out ----------------------------------------------------
    "Direct and indirect organogenesis",
    "Somatic embryogenesis and synthetic seed encapsulation in calcium alginate",
    "Developmental regulators such as Baby Boom and Wuschel to make recalcitrant "
    "genotypes regenerable",
    # ---- scaling up --------------------------------------------------------------
    "Temporary immersion bioreactors, which cut labour and improve gas exchange",
    "Photoautotrophic culture, growing plantlets on carbon dioxide rather than "
    "sucrose so they are less prone to contamination and acclimatise better",
    # ---- keeping it ---------------------------------------------------------------
    "Slow-growth storage under reduced temperature and osmotic stress",
    "Cryopreservation by vitrification, droplet freezing and encapsulation "
    "dehydration",
    "Acclimatisation and hardening protocols before transfer to soil",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "musa_acuminata",  # banana, the largest commercial application by volume
    "solanum_tuberosum",  # potato, the classic virus elimination case
    "nicotiana_tabacum",  # tobacco, where nearly every protocol was first worked out
    "arabidopsis_thaliana",  # the model, and unusually easy to regenerate
    "elaeis_guineensis",  # oil palm, and the mantled-fruit epigenetic failure
    "manihot_esculenta",  # cassava, where clean seed underpins food security
    "daucus_carota",  # carrot, where somatic embryogenesis was first demonstrated
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "tissue_culture",
    "cryopreservation",
    "microscopy",
    "pcr",
    "elisa",
    "plant_transformation",
    "protoplast_transfection",
)


# =============================================================================
#  CHALLENGES
#  Four biological, then three economic and structural. The first is the one
#  that limits two other records in this branch.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the constraint that reaches beyond this record ------------------------
    "Genotype-dependent recalcitrance, where protocols must be developed "
    "variety by variety and elite commercial lines are often the hardest, which "
    "limits genetic engineering and genome editing more than any DNA delivery "
    "problem does",
    # -- quality --------------------------------------------------------------------
    "Somaclonal variation accumulating during extended callus phases, including "
    "epigenetic changes such as the mantled-fruit abnormality that cost the oil "
    "palm industry years of production",
    "Endophytic bacterial contamination that is invisible for months and then "
    "appears simultaneously across a whole production batch",
    "Hyperhydricity, where plantlets become glassy and water-soaked in high "
    "humidity and fail to survive transfer",
    # -- the step where plants are lost in bulk ---------------------------------------
    "Acclimatisation, where plantlets grown in saturated humidity with no "
    "functional cuticle meet real air, and losses of a fifth or more are "
    "ordinary",
    # -- economics -----------------------------------------------------------------------
    "Labour cost, which dominates the economics because dividing plantlets by "
    "hand is the production line, and which confines the technique to "
    "high-value or high-volume crops",
    # -- structural --------------------------------------------------------------------
    "Cryopreservation protocols that must be developed species by species, so "
    "the crops most dependent on clonal conservation are often those with the "
    "least reliable way to store it",
)
