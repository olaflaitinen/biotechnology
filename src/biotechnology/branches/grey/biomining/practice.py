# =============================================================================
#  biotechnology.branches.grey.biomining.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS ARE SPLIT FIRST BY WHETHER THE TARGET METAL DISSOLVES, BECAUSE
#  THAT IS THE DIFFERENCE BETWEEN THE TWO PROCESSES THAT SHARE THIS NAME.
#
#      BIOLEACHING    the metal goes into solution and is recovered from it
#      BIOOXIDATION   the metal stays in the solid; the mineral around it is
#                     destroyed so a later step can reach it
#
#  A recovery percentage means a completely different thing in each. Grouping
#  them together, which the trade literature routinely does, makes the numbers
#  incomparable.
#
#  THE THIRD GROUP IS REMEDIATION AND RECYCLING, where the same chemistry is
#  turned on material that is already waste. That group includes the treatment
#  of acid mine drainage itself, which is this record cleaning up after its own
#  chemistry and is the sharpest illustration available of the identity between
#  the two.
#
#  THE FOURTH GROUP IS WHAT DOES NOT WORK, AND IT IS LABELLED. Several metals
#  and several waste streams are proposed for this treatment repeatedly and do
#  not repay it. Rule 6 forbids listing aspirations as applications; here the
#  useful service to a reader is to say which proposals recur and why they fail.
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
#  Split by whether the target dissolves, then by what the material is.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # ---- BIOLEACHING: the metal goes into solution ------------------------------
    "Heap bioleaching of low-grade copper sulphide ore, which accounts for a "
    "substantial share of world copper production and is the application that "
    "carries the whole field commercially",
    "Dump leaching of waste rock already excavated and stockpiled, which "
    "recovers metal from material that was mined and discarded and therefore "
    "requires no new ground to be disturbed",
    "In situ leaching of uranium and copper through injection and recovery "
    "wells, where the ore is never brought to the surface and the containment "
    "problem becomes a groundwater problem instead",
    "Tank bioleaching of nickel and cobalt concentrates, which is faster and "
    "far better controlled than a heap and is economic only for higher-value "
    "material",
    "Zinc and uranium recovery from sulphide ores, which are the secondary "
    "leaching targets after copper",
    # ---- BIOOXIDATION: the metal stays in the solid -----------------------------
    "Biooxidation pretreatment of refractory gold concentrates, in which the "
    "sulphide matrix enclosing the gold is destroyed so that cyanide "
    "extraction can reach it, and in which no gold is dissolved by the "
    "bacteria at all",
    "Stirred tank biooxidation plants operating continuously at controlled "
    "temperature, which is the standard configuration for gold and is the "
    "most industrially mature part of this record",
    "Heap biooxidation of lower-grade refractory gold ore, which trades "
    "recovery and time for a much smaller capital outlay",
    "Arsenopyrite oxidation as part of gold pretreatment, which mobilises "
    "arsenic into solution and makes arsenic management the governing "
    "environmental issue of the operation",
    # ---- THE SAME CHEMISTRY, TURNED ON WASTE ------------------------------------
    "Treatment of acid mine drainage by sulphate-reducing bioreactors, which "
    "runs the reaction backwards to precipitate metals as sulphides, and which "
    "is this record cleaning up after its own chemistry",
    "Reprocessing of historic tailings and smelter slag, which recovers metal "
    "from a legacy waste and reduces the mass of material left behind",
    "Desulphurisation of coal and mineral concentrates, removing pyritic "
    "sulphur before combustion or smelting",
    "Bioleaching of metals from electronic waste and spent catalysts, which is "
    "genuine and remains a small fraction of what is recycled, since mechanical "
    "and pyrometallurgical routes are faster",
    # ---- PROPOSED REPEATEDLY, AND DOES NOT REPAY IT -----------------------------
    "Bioleaching of oxide and silicate ores, which is proposed regularly and "
    "does not work by this mechanism, since the organisms attack sulphide "
    "minerals and there is no sulphide present to oxidise",
    "Bioleaching of rare earth elements, recorded as a research area rather "
    "than an application, since the leaching chemistry that succeeds for copper "
    "does not transfer to these mineral hosts",
    "Deep sea and space resource proposals, which are recorded here only to say "
    "that they are proposals, since neither has an operating process and both "
    "appear in the literature more often than the evidence supports",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the constraint each addresses. Oxygen and temperature dominate,
#  because the biology is regenerating a reagent rather than doing the work.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- the configurations -----------------------------------------------------
    "Irrigated heap leaching on lined and drained pads, with solution collected "
    "at the base, which is the low-cost configuration and the one whose "
    "containment is the environmental question",
    "Stirred tank bioreactors under controlled temperature, pH and aeration, "
    "which give far higher rates and are justified only for concentrates",
    "Dump leaching of run-of-mine waste rock, which is the least controlled "
    "arrangement and the closest in practice to spontaneous acid generation",
    "In situ well field leaching, where there is no heap and the containment "
    "problem is transferred to the aquifer",
    # ---- getting air and heat where they are needed -------------------------------
    "Forced aeration through heap bases, since oxygen supply rather than "
    "organism count is what limits the rate in most heaps",
    "Heap agglomeration and particle size control, which prevents fines "
    "blocking the flow paths and is what keeps solution and air moving through "
    "the whole heap rather than around it",
    "Thermophilic and extreme thermophilic operation, which raises reaction "
    "rates substantially and requires organisms that tolerate the heat the "
    "reaction itself generates",
    "Heat management in heaps, since sulphide oxidation is exothermic and a "
    "heap can run hotter than the organisms that started it can survive",
    # ---- keeping the chemistry in the right window ---------------------------------
    "Acid and iron balance management in the recirculating solution, which is "
    "the operational core: too little acid and leaching stalls, too much and "
    "reagent is wasted",
    "Jarosite and precipitate control, since iron precipitates coat mineral "
    "surfaces and passivate them, which is the commonest reason a heap stops "
    "performing while everything else looks correct",
    "Chloride and impurity tolerance management, which is why seawater use is "
    "constrained in arid coastal operations that would otherwise prefer it",
    "Inoculation and adaptation of consortia to the specific ore, which is one "
    "of the settings where adding organisms genuinely helps because the "
    "material starts effectively sterile",
    # ---- getting the metal out of the liquid ----------------------------------------
    "Solvent extraction and electrowinning, which recovers copper from the "
    "leach solution and produces cathode metal directly on site",
    "Ion exchange and precipitation circuits for uranium, nickel and cobalt",
    "Cyanide leaching of the biooxidised residue, which is the step the gold "
    "pretreatment exists to enable and which carries its own substantial "
    "regulatory burden",
    # ---- and closing the site --------------------------------------------------------
    "Heap rinsing, neutralisation and closure treatment, which is where the "
    "long-term liability sits and which is frequently underfunded relative to "
    "the centuries the reaction can persist",
    "Sulphate-reducing bioreactors and passive treatment wetlands for residual "
    "drainage, which link this record to `grey.phytoremediation`",
)


# =============================================================================
#  ORGANISMS
#  Chemolithotrophs. None of them consumes metal; all of them regenerate the
#  oxidant that does.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "acidithiobacillus_ferrooxidans",  # the defining organism of the field
    "acidithiobacillus_thiooxidans",  # sulphur oxidation, and acid generation
    "leptospirillum_ferriphilum",  # dominates real heaps more often than expected
    "sulfolobus_metallicus",  # thermophilic archaeon, for hot operation
    "acidiphilium_cryptum",  # heterotroph clearing organic inhibitors
    "desulfovibrio_desulfuricans",  # sulphate reduction, the reverse reaction
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "column_leach_test",
    "mineralogical_analysis",
    "inductively_coupled_plasma_spectrometry",
    "x_ray_diffraction",
    "qpcr",
    "metagenomics",
    "process_modelling",
    "titration",
)


# =============================================================================
#  CHALLENGES
#  Containment first, because it is what separates this record from its own
#  worst externality.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the identity with acid mine drainage ----------------------------------
    "Containment failure, since the process chemistry is acid mine drainage and "
    "a leaking pad or a failed liner produces exactly the pollution the "
    "technique is credited with avoiding",
    "Self-sustaining reaction after closure, which continues for centuries "
    "unless the residual material is neutralised, so the liability outlasts the "
    "operating company more often than not",
    "Arsenic mobilisation during arsenopyrite oxidation, which is the governing "
    "environmental issue of refractory gold operations and requires stable "
    "long-term arsenic disposal",
    "Water consumption in arid regions, where heap irrigation competes directly "
    "with agricultural and community supply",
    # -- why it is slow, and why that cannot easily be fixed --------------------
    "Slow kinetics measured in months to years, which exposes an operation to a "
    "metal price cycle it cannot wait out",
    "Oxygen supply as the rate-limiting factor in heaps, so the constraint is "
    "gas transport through a pile of rock rather than anything biological",
    "Mineral surface passivation by jarosite and sulphur layers, which coats "
    "the surface being attacked and is the commonest reason a heap stops "
    "performing",
    "Heat generation from an exothermic reaction, which can raise heap "
    "temperature beyond the tolerance of the organisms that started it",
    "Preferential flow and channelling through a heap, so solution and air "
    "reach part of the material and the rest is never leached",
    # -- what it cannot do at all -------------------------------------------------
    "Restriction to sulphide minerals, since the mechanism is sulphide "
    "oxidation and oxide and silicate ores are outside it rather than slow "
    "within it",
    "Lower recovery than smelting, so a decision between them is a trade of "
    "yield against capital and against emissions rather than a straightforward "
    "improvement",
    "Confinement of the economics to copper, gold and a few others, since most "
    "metals of interest do not leach fast enough to repay the wait",
    # -- and the operating conditions ----------------------------------------------
    "Chloride and impurity inhibition, which constrains the use of seawater in "
    "coastal arid operations that would otherwise prefer it",
    "Organic inhibitors from flotation reagents and from the ore itself, which "
    "suppress the chemolithotrophs at low concentrations",
    "Corrosion of plant and pipework by the acid the process is designed to "
    "generate, which is an unavoidable maintenance burden",
    "The wider question of whether making low-grade material economic displaces "
    "new extraction or simply extends the reach of mining, which is a genuine "
    "and unresolved objection rather than a rhetorical one",
)
