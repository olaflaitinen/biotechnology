# =============================================================================
#  biotechnology.branches.white.cell_free_biomanufacturing.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by WHICH OF THE THREE ADVANTAGES each one exploits,
#  because this record's applications are otherwise a miscellany. Every genuine
#  use of cell-free manufacturing is buying speed, buying access to chemistry a
#  cell will not tolerate, or buying portability. Anything that needs none of
#  those is cheaper to ferment, and saying so plainly is more useful than
#  listing possibilities.
#
#  ORGANISMS deserves a note, because the field's convention here is unusual.
#  The organisms below are not producing anything. They are the SOURCE OF THE
#  EXTRACT, harvested and lysed, and the choice determines what the resulting
#  reaction can do: bacterial extracts are productive and cannot glycosylate,
#  eukaryotic extracts fold difficult proteins and cost more. Recording them as
#  organisms is correct for the schema and would be misread without this note.
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
#  Grouped by which of the three advantages each one actually buys.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- buying SPEED: hours instead of days ------------------------------------
    "Rapid prototyping of genetic circuits and regulatory elements, where "
    "hundreds of designs are tested in a day before any is committed to an "
    "organism",
    "Screening enzyme variants directly from linear DNA templates, without "
    "cloning, transformation or colony picking",
    "Prototyping metabolic pathways by mixing separately expressed enzymes in "
    "chosen ratios, which is far quicker than balancing expression in a living "
    "strain",
    "Rapid production of protein reagents and antigens for research and assay "
    "development",
    # -- buying ACCESS: chemistry a living cell will not permit ------------------
    "Production of membrane proteins in the presence of nanodiscs, liposomes or "
    "detergents supplied directly to the reaction",
    "Synthesis of toxins, antimicrobial peptides and other products that kill "
    "the organisms normally used to make them",
    "Site-specific incorporation of non-standard amino acids, which is far "
    "simpler without competing cellular translation machinery",
    "Controlled formation of disulphide bonds by setting the redox potential of "
    "the reaction directly, rather than by engineering a compartment inside a "
    "cell",
    "Cell-free glycoprotein synthesis with defined glycosylation, added as "
    "enzymes rather than inherited from a host",
    "Enzyme cascades operating outside any organism, including routes to "
    "products whose intermediates would be consumed by native metabolism",
    # -- buying PORTABILITY: no cold chain, no laboratory -------------------------
    "Freeze-dried paper-based sensors that are rehydrated with a sample and "
    "report a specific nucleic acid sequence by colour change",
    "Field-deployable diagnostics for outbreak pathogens, demonstrated for "
    "emerging viruses and for antimicrobial resistance markers",
    "On-demand production of therapeutic proteins from stored DNA templates, "
    "which replaces a cold chain for the product with a shelf-stable "
    "instruction",
    "Water and food contaminant sensors built on the same lyophilised format",
    # -- and one that buys none of them, honestly labelled -----------------------
    "Educational kits that make protein expression visible without requiring a "
    "containment laboratory or living modified organisms, which is a teaching "
    "advantage rather than a manufacturing one",
)


# =============================================================================
#  TECHNOLOGIES
#  The four things that must be solved to run any cell-free reaction.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- what supplies the machinery -------------------------------------------
    "Crude cell extract preparation by lysis and clarification, which is cheap "
    "and productive and carries residual metabolism with it",
    "Reconstituted systems assembled from individually purified translation "
    "components, fully defined and much less productive",
    "Eukaryotic extracts from wheat germ, insect and mammalian cells for "
    "proteins that bacterial systems fold badly or cannot modify",
    "Extract processing to remove nucleases and proteases that would otherwise "
    "destroy the template and the product",
    # ---- what pays for the chemistry ---------------------------------------------
    "Energy regeneration from phosphoenolpyruvate or creatine phosphate, "
    "effective and expensive",
    "Glucose and maltodextrin based regeneration coupled to residual glycolysis "
    "in the extract, which is much cheaper and is the main reason crude "
    "extracts are preferred for manufacture",
    "Phosphate and inorganic by-product management, since accumulating "
    "phosphate inhibits the reaction and is a common reason yields stall",
    # ---- how the reaction is run -------------------------------------------------
    "Batch reactions, simple and limited by substrate depletion and by-product "
    "accumulation",
    "Continuous exchange and dialysis formats, which feed substrates and remove "
    "inhibitors across a membrane and extend reactions from hours to a day or "
    "more",
    "Microfluidic and droplet formats for very high throughput screening",
    "Linear template use, which removes cloning entirely and requires the "
    "nuclease protection noted above",
    # ---- how it is stored and moved ------------------------------------------------
    "Lyophilisation of complete reactions onto paper or into pellets, which is "
    "what converts a biological process into a shelf-stable reagent",
    "Sensor design using toehold switches and other RNA elements that couple "
    "sequence recognition to a visible output",
    "Coupling to isothermal nucleic acid amplification, which supplies the "
    "sensitivity that the cell-free readout alone lacks",
)


# =============================================================================
#  ORGANISMS
#  Sources of extract, not producers. See the note in the module header.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "escherichia_coli",  # the dominant extract, most productive, no glycosylation
    "triticum_aestivum",  # wheat germ extract, good folding of eukaryotic proteins
    "spodoptera_frugiperda",  # insect cell extract for post-translational modification
    "cricetulus_griseus",  # CHO extract, mammalian modifications, expensive
    "saccharomyces_cerevisiae",  # yeast extract, eukaryotic and inexpensive
    "vibrio_natriegens",  # very fast growth, an emerging alternative extract source
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "protein_expression",
    "dna_assembly",
    "cell_lysis",
    "lyophilisation",
    "fluorescence_assay",
    "mass_spectrometry",
    "high_throughput_screening",
    "isothermal_amplification",
)


# =============================================================================
#  CHALLENGES
#  The first three are why this is a pilot-scale technology rather than a
#  manufacturing platform.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the economics ---------------------------------------------------------
    "Cost of energy substrates and cofactors, which must all be purchased "
    "rather than made by a growing organism, and which is the principal reason "
    "cost per gram cannot match fermentation",
    "A catalyst that is consumed rather than reproducing, so each reaction pays "
    "for its own machinery instead of inheriting it from the last generation",
    "The extract itself must be manufactured from cells grown conventionally, "
    "so the technology does not escape fermentation but sits downstream of it",
    # -- the reproducibility problem nobody publishes -----------------------------
    "Batch-to-batch variability of crude extracts, which is real, "
    "under-reported and the largest obstacle to using cell-free systems in a "
    "regulated manufacturing process",
    "Residual metabolism in crude extracts that consumes substrates or degrades "
    "the product in ways that differ between preparations",
    # -- what stops the reaction --------------------------------------------------
    "Accumulation of inorganic phosphate and other inhibitory by-products, "
    "which caps batch reactions long before the machinery is exhausted",
    "Nuclease and protease activity degrading template and product, "
    "particularly when linear DNA is used",
    "Limited reaction duration, so a process that a fermenter would run for a "
    "week runs here for hours",
    # -- scale ---------------------------------------------------------------------
    "Scale-up, which is demonstrated at the scale of tens to hundreds of litres "
    "rather than the hundreds of cubic metres routine in "
    "`white.microbial_fermentation`",
    # -- the modifications a bacterial extract cannot make ---------------------------
    "Absence of native glycosylation and other post-translational machinery in "
    "bacterial extracts, which must be supplied enzymatically and adds cost and "
    "complexity",
    # -- the governance gap ----------------------------------------------------------
    "A biosecurity control point that has moved, since a system programmed by "
    "nucleic acid and containing nothing alive is not captured by the frameworks "
    "written for living modified organisms, which places the burden on DNA "
    "synthesis screening instead",
)
