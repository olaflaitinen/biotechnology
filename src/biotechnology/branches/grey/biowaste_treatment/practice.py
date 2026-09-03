# =============================================================================
#  biotechnology.branches.grey.biowaste_treatment.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS ARE GROUPED BY FEEDSTOCK, BECAUSE FEEDSTOCK DECIDES EVERYTHING
#  ELSE: which route is used, what the gas yield is, and whether the plant has
#  a contamination problem.
#
#      FARM         wet, predictable, low contamination, poor gas yield alone
#      FOOD         wet, energy-dense, and the contamination problem
#      MUNICIPAL    mixed, and the route determined by collection policy
#      MUNICIPAL SOLID WASTE ORGANIC FRACTION  the hardest, and the reason
#                   mechanical separation exists
#
#  THE LAST GROUP IS THE OUTPUTS, AND IT IS PART OF THE APPLICATIONS RATHER
#  THAN A FOOTNOTE. A digester that produces gas and cannot place its digestate
#  has not completed a process; it has changed the shape of a disposal problem.
#
#  TECHNOLOGIES ARE GROUPED BY WHERE THEY SIT IN THE LINE: what happens before
#  the vessel, in it, and after it. The before and after groups are longer than
#  the vessel group, which is an accurate reflection of where the engineering
#  effort and the capital actually go.
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
#  By feedstock, then by what comes out.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # ---- FARM: predictable material, and a nutrient problem being solved -------
    "Farm digestion of manure and slurry, which manages a nutrient runoff "
    "problem and produces gas as a secondary benefit rather than the reverse",
    "Co-digestion of manure with food waste or crop residue, which raises the "
    "gas yield of an otherwise poor feedstock by adding energy density to a "
    "stable base",
    "On-farm combined heat and power generation, where the heat has an obvious "
    "local use and therefore does not go to waste as it does at many "
    "standalone plants",
    "Digestion of crop residues and processing by-products at the site that "
    "produces them, which removes the transport cost that governs most "
    "feedstock decisions",
    # ---- FOOD: the energy-dense stream, and the contamination problem -----------
    "Separately collected household food waste digestion, which is the "
    "highest-yield municipal stream and the one whose success depends on "
    "household separation behaviour",
    "Commercial and institutional food waste from supermarkets, caterers and "
    "canteens, which is high in energy and unusually consistent because it "
    "comes from a controlled setting",
    "Food processing effluent and by-product digestion at the factory, which "
    "converts a trade effluent charge into an energy input",
    "Depackaging and digestion of out-of-date packaged food, which is "
    "technically feasible and is the largest single source of plastic "
    "contamination in digestate",
    # ---- MUNICIPAL SOLID WASTE: the hardest feedstock ---------------------------
    "Mechanical biological treatment of mixed residual waste, which separates "
    "an organic fraction mechanically and treats it, and which produces a "
    "material too contaminated for agricultural use in most jurisdictions",
    "Landfill gas capture, which is the retrospective version of the same "
    "chemistry: the methane is generated anyway and a fraction of it is "
    "collected, which is the comparison the whole record is judged against",
    # ---- COMPOSTING: the aerobic route, for the material digestion suits less ----
    "Windrow and in-vessel composting of garden and green waste, which suits "
    "fibrous dry material and is far simpler to operate than digestion",
    "In-vessel composting of catering waste under pathogen reduction "
    "requirements, which is what animal by-product rules demand where the "
    "material may contact livestock",
    "Composting of digestate solids, which stabilises the fraction the "
    "digester could not break down and makes it storable",
    "Home and community composting, which handles material without collecting "
    "or transporting it at all and is the lowest-cost route by a wide margin",
    # ---- WHAT COMES OUT, WHICH COMPLETES THE PROCESS ----------------------------
    "Biogas combustion for electricity and heat, which is the simplest use and "
    "wastes the heat wherever there is no local demand for it",
    "Biomethane upgrading and grid injection, which removes the carbon dioxide "
    "to produce gas of natural gas quality and which is the highest-value route "
    "where a grid connection exists",
    "Digestate application to agricultural land as a nitrogen and phosphorus "
    "source, which is what makes the process a nutrient cycle rather than a "
    "waste treatment",
    "Separation of digestate into a fibrous solid and a liquid fraction, which "
    "is done because the wet whole digestate is too bulky to transport "
    "economically beyond a short radius",
)


# =============================================================================
#  TECHNOLOGIES
#  Before the vessel, in the vessel, after the vessel.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- before the vessel, which is where projects are won or lost -------------
    "Source separation collection systems, which is the cheapest and most "
    "effective contamination control available and which is a municipal policy "
    "decision rather than a process technology",
    "Depackaging and mechanical contaminant removal, including screens, "
    "hydrocyclones and magnetic separation, which is the expensive and "
    "imperfect substitute for the entry above",
    "Maceration and particle size reduction, which raises the surface area "
    "available for hydrolysis and therefore attacks the rate-limiting step "
    "directly",
    "Thermal, chemical and enzymatic pretreatment of fibrous feedstock, which "
    "is aimed at the same rate limitation for material that resists it",
    "Pasteurisation and sanitisation to satisfy animal by-product requirements "
    "before or after digestion",
    # ---- in the vessel ----------------------------------------------------------
    "Mesophilic digestion at moderate temperature, which is more stable and "
    "more forgiving and is the default choice",
    "Thermophilic digestion at higher temperature, which is faster and achieves "
    "pathogen reduction inside the process, at the cost of a community far more "
    "sensitive to disturbance",
    "Wet and dry digestion configurations, selected by the solids content of "
    "the feedstock rather than by preference",
    "Two-stage systems separating the acid-forming steps from methanogenesis, "
    "which addresses the characteristic failure of the process by giving the "
    "slow organisms their own vessel",
    "Continuous stirred tank and plug flow reactor designs, and the mixing "
    "systems that keep solids in suspension",
    "Process monitoring and control on volatile fatty acids, alkalinity and gas "
    "composition, which is how an operator sees an overfeeding failure while it "
    "can still be corrected",
    # ---- after the vessel -------------------------------------------------------
    "Biogas desulphurisation, which is required before combustion because "
    "hydrogen sulphide is corrosive and toxic",
    "Biogas upgrading to biomethane by water scrubbing, pressure swing "
    "adsorption or membrane separation, which removes carbon dioxide to reach "
    "grid quality",
    "Combined heat and power generation, and the heat demand matching that "
    "decides whether the thermal output is used or vented",
    "Digestate separation, dewatering and storage, which determines the "
    "transport cost and therefore the radius within which the material can be "
    "placed",
    "Nutrient recovery from the liquid fraction, including ammonia stripping "
    "and struvite crystallisation, which concentrates nutrients into a "
    "transportable product",
    "Methane leakage detection and quantification across the plant, which is "
    "measured far less often than it should be given how quickly a small loss "
    "erodes the climate benefit",
)


# =============================================================================
#  ORGANISMS
#  A four-stage community, and the entries follow the sequence.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "clostridium_species",  # hydrolysis and acidogenesis, the fast first steps
    "syntrophomonas_wolfei",  # acetogenesis, and only viable next to a methanogen
    "methanosaeta_concilii",  # acetate to methane, dominant at low acetate
    "methanosarcina_barkeri",  # the robust methanogen, tolerates shock better
    "methanobacterium_formicicum",  # hydrogen and carbon dioxide to methane
    "actinomycetes_group",  # the composting route, degrading fibrous material
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "biomethane_potential_assay",
    "gas_chromatography",
    "titration",
    "qpcr",
    "metagenomics",
    "process_modelling",
    "calorimetry",
    "online_sensing",
)


# =============================================================================
#  CHALLENGES
#  Feedstock first, because that is where these projects actually fail.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the feedstock, which is a social problem in a process discipline -------
    "Plastic, glass and metal contamination in collected food waste, which "
    "damages equipment, accumulates in the vessel and passes into digestate "
    "spread on farmland, so recycling becomes a route by which microplastic "
    "reaches agricultural soil",
    "Dependence on household separation behaviour and municipal collection "
    "policy, which sets plant performance more reliably than any process "
    "variable and is outside the operator's control",
    "Feedstock variability in composition and supply, since a plant sized for a "
    "contract is exposed when the contract or the local waste stream changes",
    # -- the characteristic process failure ---------------------------------------
    "Acidification from overfeeding, in which acid-forming organisms outpace "
    "the slower methanogens, the pH falls, and the organisms needed for "
    "recovery are the ones the acidity inhibits most, so recovery takes weeks",
    "Ammonia inhibition from nitrogen-rich feedstock such as poultry manure, "
    "which suppresses methanogenesis at concentrations the feedstock reaches "
    "readily",
    "Hydrolysis as the rate-limiting step for fibrous material, which sets the "
    "residence time and therefore the size and cost of the vessel",
    "Trace element deficiency in single-feedstock digesters, which limits "
    "methanogen activity in a way that is easy to misdiagnose as an "
    "overfeeding problem",
    "Foaming, crust formation and sedimentation, which reduce the working "
    "volume and are the commonest ordinary maintenance burden",
    # -- what to do with what comes out -----------------------------------------------
    "Digestate volume and water content, which restrict economic transport to a "
    "short radius, so a plant without enough land nearby has a disposal problem "
    "rather than a product",
    "Seasonal restrictions on land spreading, which fall in the period when "
    "storage is fullest and are a nitrate protection requirement rather than an "
    "operational choice",
    "Nutrient imbalance in digestate relative to what a crop needs, so applying "
    "enough of one nutrient over-applies another",
    "Pathogen and weed seed survival where the process temperature and "
    "residence time do not meet sanitisation requirements",
    # -- the emissions the process itself creates --------------------------------------
    "Methane leakage from vessels, storage and upgrading, where a small "
    "percentage loss offsets a large share of the climate benefit and which is "
    "measured far less often than it should be",
    "Ammonia emission from digestate storage and spreading, which is an air "
    "quality problem and a loss of the nitrogen value at the same time",
    "Odour, which is the reason siting is contentious and is the objection "
    "neighbours raise first",
    # -- and the economics -------------------------------------------------------------
    "Dependence on avoided disposal cost and on policy support, so the same "
    "plant is viable under a landfill tax and unviable without one",
    "Heat with no local demand, which is vented at many standalone plants and "
    "is the largest routine waste of recovered energy in the record",
)
