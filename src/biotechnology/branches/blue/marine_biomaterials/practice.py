# =============================================================================
#  biotechnology.branches.blue.marine_biomaterials.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped BY MATERIAL CLASS rather than by industry, because
#  the properties that make each class useful are shared across its
#  applications and a reader who learns why alginate gels can predict most of
#  where alginate appears.
#
#  The last group is different in kind and is separated deliberately. The
#  biomimetic materials are not extracted and sold; they are structures that
#  are studied and then reproduced synthetically, because harvesting the
#  organism is either impossible at scale or unacceptable. Presenting them
#  beside the extractive applications without that distinction would suggest a
#  supply chain that does not exist.
#
#  ORGANISMS are the sources, and the note on each gives what part is used,
#  since in most cases it is the part that would otherwise be discarded.
#
#  A NOTE ON WHAT IS ABSENT. The farming of the seaweed is
#  `blue.seaweed_cultivation`. The enzymes that process these polysaccharides
#  are `blue.marine_enzymes`. This record is the material and what is made from
#  it.
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
#  By material class. The final group is biomimetic rather than extractive.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- alginate and the seaweed polysaccharides -------------------------------
    "Alginate wound dressings, which gel on contact with the calcium in wound "
    "fluid so that the dressing conforms to the wound and lifts off without "
    "tearing new tissue",
    "Alginate dental impression materials, which set at mouth temperature and "
    "reproduce fine detail",
    "Cell encapsulation in alginate beads, including immunoisolation of "
    "transplanted cells, since gelation happens under conditions a living cell "
    "survives",
    "Agarose gels for electrophoresis and chromatography, on which molecular "
    "biology depends",
    "Carrageenan and alginate as pharmaceutical excipients, controlling "
    "viscosity and release rate in formulation",
    "Fucoidan and sulphated polysaccharides investigated for anticoagulant and "
    "immunomodulatory activity, where the sulphation pattern is the active "
    "feature and also the least controlled one",
    # -- chitin and chitosan, from shells nobody wanted --------------------------
    "Chitosan haemostatic dressings, which stop bleeding by a mechanism "
    "independent of the patient's own clotting cascade and therefore work in "
    "trauma and in anticoagulated patients",
    "Chitosan antimicrobial coatings and food preservation films",
    "Chitosan in drug delivery, exploiting its adhesion to mucosal surfaces",
    "Chitin nanofibres and nanocrystals as reinforcement in composites",
    "Chitosan as a flocculant in water treatment and as a plant biostimulant, "
    "which are the high-volume low-value uses that absorb material the medical "
    "applications cannot",
    # -- collagen and gelatin, from skin and scales ------------------------------
    "Marine collagen and gelatin for wound care, tissue scaffolds and "
    "cosmetics, avoiding the mammalian sourcing that raises disease and "
    "religious objections",
    "Fish gelatin capsules and food applications, for the same reason",
    "Jellyfish collagen, which is unusual in being available in quantity from "
    "an organism that is frequently a nuisance",
    # -- mineralised structures ---------------------------------------------------
    "Coral-derived and coral-converted bone graft substitutes, whose pore "
    "structure resembles human cancellous bone closely enough to guide "
    "ingrowth",
    "Marine-derived calcium phosphate and hydroxyapatite from fish bone",
    "Diatom and sponge biosilica as porous scaffolds and as templates",
    # -- biomimetic: studied, then made synthetically ------------------------------
    "Mussel-inspired adhesives based on the catechol chemistry that lets a "
    "mussel bond to wet rock, reproduced synthetically because harvesting the "
    "protein is not scalable",
    "Nacre-inspired layered composites, which copy an arrangement that makes "
    "calcium carbonate orders of magnitude tougher than the mineral alone",
    "Antifreeze and ice-binding protein analogues, which link this record to "
    "the cryopreservation applications in `blue.marine_enzymes`",
    "Byssus-inspired self-healing and energy-absorbing fibres",
)


# =============================================================================
#  TECHNOLOGIES
#  Extraction, then the characterisation that this field actually lives on,
#  then fabrication.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- getting the polymer out ------------------------------------------------
    "Alkaline extraction and calcium precipitation of alginate from brown "
    "seaweed",
    "Demineralisation and deproteinisation of crustacean shell to chitin, "
    "followed by alkaline deacetylation to chitosan, which is effective and "
    "chemically harsh",
    "Enzymatic and fermentative shell processing as a milder alternative, "
    "which reduces the reagent waste stream at higher cost",
    "Acid and enzymatic extraction of collagen from fish skin and scales",
    "Controlled depolymerisation to defined molecular weight fractions and "
    "oligosaccharides, which is how a variable raw material is turned into a "
    "specified one",
    # ---- knowing what you have, which is where the effort goes -------------------
    "Determination of degree of deacetylation for chitosan, which governs "
    "solubility, charge and biological activity",
    "Determination of the mannuronic to guluronic acid ratio for alginate, "
    "which decides whether a gel is stiff and brittle or soft and elastic",
    "Sulphation pattern analysis for carrageenan and fucoidan, which is the "
    "active feature and the hardest to control",
    "Molecular weight distribution by size exclusion chromatography with "
    "multi-angle light scattering",
    "Endotoxin, protein and heavy metal testing, which is what separates a "
    "technical grade from a medical grade of the same polymer",
    # ---- making something out of it ---------------------------------------------
    "Ionic and covalent crosslinking to form hydrogels, including the calcium "
    "gelation that underlies most alginate applications",
    "Electrospinning and wet spinning into fibres and non-woven mats",
    "Freeze drying and porogen methods for porous scaffolds",
    "Three-dimensional printing of marine polysaccharide bioinks, where mild "
    "gelation conditions are the reason these materials are used",
    "Composite formation with ceramic and synthetic polymer phases",
    # ---- copying a structure rather than extracting a substance --------------------
    "Structural characterisation of biomineralised composites by microscopy and "
    "diffraction, as the first step towards reproducing the arrangement",
    "Recombinant production of adhesive and structural proteins, which is the "
    "only scalable route to materials whose source organism cannot be harvested",
)


# =============================================================================
#  ORGANISMS
#  Sources, and the part used, which is usually the part discarded.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "saccharina_japonica",  # brown seaweed; alginate from the harvested thallus
    "gracilaria_gracilis",  # red seaweed; agar and agarose
    "penaeus_vannamei",  # shrimp; chitin from shell waste the industry discards
    "mytilus_edulis",  # mussel; the adhesive proteins, studied then made recombinantly
    "pinctada_margaritifera",  # pearl oyster; nacre, studied as a structure
    "rhopilema_esculentum",  # jellyfish; collagen, from an organism often a nuisance
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "solvent_extraction",
    "chromatography",
    "nuclear_magnetic_resonance",
    "electron_microscopy",
    "mechanical_testing",
    "rheometry",
    "electrospinning",
    "protein_expression",
)


# =============================================================================
#  CHALLENGES
#  Variability first, because it is what blocks the applications worth having.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the constraint that replaces supply ------------------------------------
    "Batch-to-batch variability by species, season, individual and processing, "
    "in exactly the parameters that determine performance, which is the "
    "principal obstacle to any regulated application",
    "Absence of agreed specifications and reference materials, so two suppliers "
    "of the same named polymer may deliver materials that behave differently "
    "and both be within their own specification",
    "Traceability of a waste-derived raw material back to a species and a "
    "catch, which a medical device file requires and a fish market does not "
    "provide",
    # -- what the material itself cannot do ---------------------------------------
    "Lower thermal stability of marine collagen than mammalian collagen, which "
    "restricts the applications it can substitute into",
    "Mechanical weakness of polysaccharide hydrogels, which limits them to "
    "applications where load bearing is not required",
    "Uncontrolled degradation rate in vivo, which is difficult to specify for a "
    "material whose molecular weight distribution is itself variable",
    # -- safety questions that are unresolved rather than absent --------------------
    "Allergenicity of shellfish-derived materials, which is unresolved in the "
    "literature and treated conservatively in practice, since the tropomyosin "
    "responsible for shellfish allergy is a protein and purified chitosan "
    "should not contain it",
    "Endotoxin and residual protein control, which is what separates a material "
    "usable in a device from the same polymer sold industrially",
    # -- the process is not automatically green -------------------------------------
    "Harsh reagent use and effluent from conventional chitin extraction, which "
    "means the environmental case for a waste-derived material has to be "
    "demonstrated rather than assumed",
    "Seasonal and geographic variation in supply of a by-product whose volume "
    "is set by an industry with entirely different priorities",
    # -- where extraction is not an option --------------------------------------------
    "Unacceptability of harvesting coral, sponge or mussel at any scale that "
    "would matter, which makes biomimetic reproduction the only route for the "
    "structural materials",
    "Difficulty of reproducing a hierarchical structure rather than a "
    "composition, since the interesting property of nacre and byssus lies in an "
    "arrangement built over time by a living organism",
)
