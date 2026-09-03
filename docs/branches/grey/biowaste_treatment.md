<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/grey/biowaste_treatment/.
  Edit the source and run `make docs`.
-->

[Grey Biotechnology](index.md) / **Biowaste Treatment**

## Biowaste Treatment

`grey.biowaste_treatment`

Anaerobic digestion and composting of organic waste into methane and soil amendment, where the economics turn on avoided disposal cost and the failures turn on feedstock contamination.

### What it is

Biowaste treatment converts the organic fraction of municipal, food and agricultural waste into usable products by two routes that suit different material. Anaerobic digestion excludes oxygen and produces biogas, typically somewhat over half methane, together with a wet digestate; it suits wet, energy-dense material such as food waste, manure and slurry. Composting admits oxygen and produces a stable solid and heat but no recoverable fuel; it suits drier, more fibrous material such as garden waste, and it is far simpler to operate. The choice between them is decided by the moisture and the energy content of the feedstock rather than by preference, and many facilities do both, digesting the wet fraction and composting what the digester rejects. Digestion is performed by a community in four sequential steps, each feeding the next. Hydrolysis breaks polymers into soluble molecules and is the rate-limiting step for fibrous material. Acidogenesis converts those into organic acids. Acetogenesis converts the acids to acetate and hydrogen. Methanogenesis, performed by archaea rather than bacteria, produces methane. The important operational fact is that the last group grows far more slowly than the first, so overfeeding produces acid faster than the methanogens can consume it, the pH falls, and the organisms most needed to recover are the ones the falling pH inhibits most. That is the characteristic failure of a digester and it takes weeks to reverse. The climate case is frequently stated wrongly as a case about renewable energy. The correct comparison is with landfill, where the same organic material decomposes anaerobically regardless and releases methane from a structure that captures only a fraction of it. Methane is a far more potent greenhouse gas than carbon dioxide over the timescales that matter. So the benefit is chiefly that the methane is generated inside a sealed vessel with a pipe on it, and the energy recovered is a consequence of that rather than the reason for it. This also means the benefit is largest where the alternative is landfill and much smaller where it is incineration with energy recovery. Operationally, the determining variable is feedstock contamination. Plastic film, glass and metal in collected food waste damage pumps and mixers, accumulate in the vessel, and pass into the digestate that is spread on farmland, which is how microplastic reaches agricultural soil through a route intended as recycling. Removing contamination after collection is expensive and imperfect; separating it at the household is cheap and effective. The performance of a digester is therefore set largely by municipal collection policy and household behaviour, which is an uncomfortable finding for a process discipline and is the single most reliable predictor of whether a plant meets its design output.

### In plain language

Food and farm waste can be sealed in a tank without air, where microbes break it down and give off a gas that is mostly methane, which is the same thing as natural gas and can be burned for electricity or put into the gas grid. What is left over is a wet fertiliser. Drier garden waste is better composted, which needs air and produces no fuel. The real reason this is good for the climate is not the energy. It is that the same waste in a landfill produces that methane anyway and most of it escapes into the sky, where it is a much stronger greenhouse gas than carbon dioxide. Doing it in a sealed tank means the methane goes down a pipe instead. The thing that makes these plants fail is not the biology at all: it is plastic bags and broken glass in the food waste, which wreck the machinery and end up spread on farm fields.

### An analogy

A digester is a stomach with a schedule. It handles a steady diet well and it handles a sudden large meal badly, because the first stages of digestion run much faster than the last, so the intermediates pile up, the contents turn acid, and the organisms that would clear the acid are the ones the acid disables. Recovery takes weeks of careful feeding. And as with any stomach, what it is given matters more than how it is run: nothing about the vessel can deal with the swallowed plastic.

### Why it matters

Organic waste is a large share of what municipalities collect, and in landfill it is the principal source of the methane the site emits. Diverting it to digestion addresses that at the source rather than capturing it afterwards, which is why landfill diversion targets and landfill taxes have driven the sector more effectively than any energy policy. The material recovered is real: methane displacing fossil gas, and a digestate returning nitrogen and phosphorus to soil at a time when phosphate rock is a finite imported resource. On farms the same process manages slurry that would otherwise be a nutrient runoff problem, which connects this record to `green.biofertilisers`. The limits are as concrete. The economics depend on avoided disposal cost, so the same plant is viable under a landfill tax and unviable without one, and the sector is consequently policy-dependent rather than self-supporting. Digestate is bulky and wet, so it can only be spread economically near the plant, and if there is not enough land within reach at the right time of year the plant has a disposal problem of its own. Spreading is seasonally restricted precisely when storage is fullest. Contamination in the feedstock damages equipment and carries plastic on to farmland. Methane leakage from the plant erodes the climate benefit quickly, since a small percentage loss offsets a large share of the gain, and it is measured far less often than it should be. Ammonia and odour emissions make siting genuinely contentious with neighbours. And the hierarchy point deserves stating plainly: preventing food waste is considerably better than digesting it, and a well-run digester should not be read as a reason to be relaxed about producing the material.

### Applications

- Farm digestion of manure and slurry, which manages a nutrient runoff problem and produces gas as a secondary benefit rather than the reverse
- Co-digestion of manure with food waste or crop residue, which raises the gas yield of an otherwise poor feedstock by adding energy density to a stable base
- On-farm combined heat and power generation, where the heat has an obvious local use and therefore does not go to waste as it does at many standalone plants
- Digestion of crop residues and processing by-products at the site that produces them, which removes the transport cost that governs most feedstock decisions
- Separately collected household food waste digestion, which is the highest-yield municipal stream and the one whose success depends on household separation behaviour
- Commercial and institutional food waste from supermarkets, caterers and canteens, which is high in energy and unusually consistent because it comes from a controlled setting
- Food processing effluent and by-product digestion at the factory, which converts a trade effluent charge into an energy input
- Depackaging and digestion of out-of-date packaged food, which is technically feasible and is the largest single source of plastic contamination in digestate
- Mechanical biological treatment of mixed residual waste, which separates an organic fraction mechanically and treats it, and which produces a material too contaminated for agricultural use in most jurisdictions
- Landfill gas capture, which is the retrospective version of the same chemistry: the methane is generated anyway and a fraction of it is collected, which is the comparison the whole record is judged against
- Windrow and in-vessel composting of garden and green waste, which suits fibrous dry material and is far simpler to operate than digestion
- In-vessel composting of catering waste under pathogen reduction requirements, which is what animal by-product rules demand where the material may contact livestock
- Composting of digestate solids, which stabilises the fraction the digester could not break down and makes it storable
- Home and community composting, which handles material without collecting or transporting it at all and is the lowest-cost route by a wide margin
- Biogas combustion for electricity and heat, which is the simplest use and wastes the heat wherever there is no local demand for it
- Biomethane upgrading and grid injection, which removes the carbon dioxide to produce gas of natural gas quality and which is the highest-value route where a grid connection exists
- Digestate application to agricultural land as a nitrogen and phosphorus source, which is what makes the process a nutrient cycle rather than a waste treatment
- Separation of digestate into a fibrous solid and a liquid fraction, which is done because the wet whole digestate is too bulky to transport economically beyond a short radius

### Technologies

- Source separation collection systems, which is the cheapest and most effective contamination control available and which is a municipal policy decision rather than a process technology
- Depackaging and mechanical contaminant removal, including screens, hydrocyclones and magnetic separation, which is the expensive and imperfect substitute for the entry above
- Maceration and particle size reduction, which raises the surface area available for hydrolysis and therefore attacks the rate-limiting step directly
- Thermal, chemical and enzymatic pretreatment of fibrous feedstock, which is aimed at the same rate limitation for material that resists it
- Pasteurisation and sanitisation to satisfy animal by-product requirements before or after digestion
- Mesophilic digestion at moderate temperature, which is more stable and more forgiving and is the default choice
- Thermophilic digestion at higher temperature, which is faster and achieves pathogen reduction inside the process, at the cost of a community far more sensitive to disturbance
- Wet and dry digestion configurations, selected by the solids content of the feedstock rather than by preference
- Two-stage systems separating the acid-forming steps from methanogenesis, which addresses the characteristic failure of the process by giving the slow organisms their own vessel
- Continuous stirred tank and plug flow reactor designs, and the mixing systems that keep solids in suspension
- Process monitoring and control on volatile fatty acids, alkalinity and gas composition, which is how an operator sees an overfeeding failure while it can still be corrected
- Biogas desulphurisation, which is required before combustion because hydrogen sulphide is corrosive and toxic
- Biogas upgrading to biomethane by water scrubbing, pressure swing adsorption or membrane separation, which removes carbon dioxide to reach grid quality
- Combined heat and power generation, and the heat demand matching that decides whether the thermal output is used or vented
- Digestate separation, dewatering and storage, which determines the transport cost and therefore the radius within which the material can be placed
- Nutrient recovery from the liquid fraction, including ammonia stripping and struvite crystallisation, which concentrates nutrients into a transportable product
- Methane leakage detection and quantification across the plant, which is measured far less often than it should be given how quickly a small loss erodes the climate benefit

### Challenges

- Plastic, glass and metal contamination in collected food waste, which damages equipment, accumulates in the vessel and passes into digestate spread on farmland, so recycling becomes a route by which microplastic reaches agricultural soil
- Dependence on household separation behaviour and municipal collection policy, which sets plant performance more reliably than any process variable and is outside the operator's control
- Feedstock variability in composition and supply, since a plant sized for a contract is exposed when the contract or the local waste stream changes
- Acidification from overfeeding, in which acid-forming organisms outpace the slower methanogens, the pH falls, and the organisms needed for recovery are the ones the acidity inhibits most, so recovery takes weeks
- Ammonia inhibition from nitrogen-rich feedstock such as poultry manure, which suppresses methanogenesis at concentrations the feedstock reaches readily
- Hydrolysis as the rate-limiting step for fibrous material, which sets the residence time and therefore the size and cost of the vessel
- Trace element deficiency in single-feedstock digesters, which limits methanogen activity in a way that is easy to misdiagnose as an overfeeding problem
- Foaming, crust formation and sedimentation, which reduce the working volume and are the commonest ordinary maintenance burden
- Digestate volume and water content, which restrict economic transport to a short radius, so a plant without enough land nearby has a disposal problem rather than a product
- Seasonal restrictions on land spreading, which fall in the period when storage is fullest and are a nitrate protection requirement rather than an operational choice
- Nutrient imbalance in digestate relative to what a crop needs, so applying enough of one nutrient over-applies another
- Pathogen and weed seed survival where the process temperature and residence time do not meet sanitisation requirements
- Methane leakage from vessels, storage and upgrading, where a small percentage loss offsets a large share of the climate benefit and which is measured far less often than it should be
- Ammonia emission from digestate storage and spreading, which is an air quality problem and a loss of the nitrogen value at the same time
- Odour, which is the reason siting is contentious and is the objection neighbours raise first
- Dependence on avoided disposal cost and on policy support, so the same plant is viable under a landfill tax and unviable without one
- Heat with no local demand, which is vented at many standalone plants and is the largest routine waste of recovered energy in the record

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Volatile fatty acid to alkalinity ratio | `VFA/TA` | dimensionless ratio | a low ratio indicates a stable digester; a rising ratio is the warning before pH moves | CONSENSUS |
| Organic loading rate | `OLR` | kilograms of volatile solids per cubic metre of reactor per day | raised cautiously toward the design value and reduced immediately when the ratio above rises | CONSENSUS |
| Hydraulic retention time | `HRT` | days | weeks for mesophilic digestion of typical feedstock | CONSENSUS |
| Specific methane yield | `Y_CH4` | cubic metres of methane per tonne of volatile solids added | high for food waste and fats, low for manure and fibrous material | CONSENSUS |
| Biomethane potential | `BMP` | cubic metres of methane per tonne of volatile solids | a laboratory ceiling that field plants approach and do not reach | CONSENSUS |
| Volatile solids destruction | `VS_dest` | per cent of volatile solids converted | a majority for readily degradable food waste, considerably less for fibrous material | CONSENSUS |
| Methane content of raw biogas | `x_CH4` | per cent by volume | somewhat over half, with most of the balance carbon dioxide | CONSENSUS |
| Methane leakage rate | `f_leak` | per cent of methane produced that escapes unburned | small in percentage terms and large in effect, and measured at few plants | INDICATIVE |
| Avoided landfill methane emission | `M_avoid` | tonnes of carbon dioxide equivalent per tonne of waste diverted | the largest single term in the climate case, and larger than the energy displacement term | REVIEWED |
| Digestate nutrient content | `c_NPK` | kilograms of nitrogen, phosphorus and potassium per tonne | dilute, and with a nutrient ratio that rarely matches what a crop needs | CONSENSUS |
| Digestate transport radius | `r_econ` | kilometres within which spreading remains economic | short, because the material is mostly water | REPORTED |
| Physical contaminant content of digestate | `c_phys` | per cent by mass of plastic, glass and metal | low where waste is separated at the household, higher where it is separated mechanically afterwards | CONSENSUS |
| Gate fee | `C_gate` | euro per tonne of waste accepted | set by what disposal would otherwise have cost, which is set by landfill tax | REPORTED |
| Parasitic energy demand | `f_para` | per cent of energy produced consumed by the plant itself | a modest but not negligible share, for heating, mixing and upgrading | REPORTED |

### History

- **1776** - Combustible gas is identified rising from decomposing matter in marshes
- **1895** - Gas from a covered sewage tank is used for street lighting
- **1930** - The four-stage microbiology of anaerobic digestion is characterised
- **1950** - Small-scale digesters are deployed widely in rural households in Asia
- **1977** - Methanogens are recognised as archaea, a domain distinct from bacteria
- **1999** - A landfill directive sets binding targets for diverting biodegradable waste from landfill
- **2000** - Renewable energy tariffs make crop-fed digestion commercially attractive in Germany
- **2010** - Biomethane upgrading and gas grid injection reach commercial scale
- **2012** - Crop-fed digestion is found to be displacing food production, and support is restructured
- **2015** - Separate food waste collection becomes mandatory in a growing number of jurisdictions
- **2018** - Digestate quality protocols are tightened after plastic contamination is documented on agricultural land
- **2020** - Methane leakage measurement campaigns find emissions higher than reported at operating plants

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | ENVIRONMENT, ENERGY, FOOD, MATERIALS |
| SDGs | 2, 7, 11, 12, 13 |

### Regulations

- The Landfill Directive 1999/31/EC and equivalent national regimes, whose binding targets for diverting biodegradable waste from landfill gave organic waste a disposal cost and thereby created the economic basis for this record
- Landfill taxes and gate fee structures, which set the avoided disposal cost that most plants earn more from than they earn from the gas
- The Waste Framework Directive 2008/98/EC, including the waste hierarchy which places prevention above recovery, so a well-run digester does not justify producing the material
- Mandatory separate collection requirements for biowaste, which determine feedstock quality and therefore plant performance more reliably than any process variable
- End-of-waste criteria and quality protocols for digestate and compost, which determine whether the output is a product or a waste and thereby change who may handle it, where it may go and what it is worth, without the material changing at all
- Environmental permitting for waste treatment operations, setting permitted throughput, accepted waste codes and emission conditions
- Fertilising products regulation, including Regulation (EU) 2019/1009, which sets the route by which digestate may be placed on the market as a fertilising product across a single market
- Animal by-products regulation, including Regulation (EC) No 1069/2009, which imposes pasteurisation time and temperature requirements on catering waste and animal material before or after digestion
- Restrictions on feeding and on land application where treated material may contact livestock, which are disease control measures rather than environmental ones
- The Nitrates Directive 91/676/EEC and national action programmes, which set closed periods and application limits for nitrogen, and whose closed periods fall when storage is fullest
- Groundwater and surface water protection requirements applying to storage and spreading, including buffer distances from watercourses
- Metal and physical contaminant limits for material applied to agricultural land, which are what the 2018 protocol tightening addressed
- Storage capacity requirements sized to the closed periods above, which are a substantial part of a plant's capital cost and are frequently underestimated
- Renewable energy support schemes and feed-in tariffs, restructured in several jurisdictions after crop-fed digestion was found to be displacing food production
- Gas quality specifications and grid injection requirements for upgraded biomethane
- Explosion protection and hazardous area requirements, including the ATEX framework, since digester gas is explosive and gas handling is where the serious accidents occur
- Industrial emissions and air quality requirements covering ammonia and odour, which are the objections neighbours raise and the reason siting is contentious

### Standards

- Biomethane potential assay protocols, including inoculum standardisation and the reporting conventions that keep the result legible as a ceiling rather than as a prediction
- Volatile solids and moisture determination methods, since yields quoted per wet tonne are not comparable between feedstocks
- Feedstock characterisation and acceptance criteria, which is how a plant protects itself from a delivery it cannot digest
- Volatile fatty acid and alkalinity determination methods, which underpin the ratio that gives warning before pH moves
- Process monitoring and control conventions on gas composition, temperature and loading rate
- Commissioning and inoculation practice, which is the uncontested case of seeding discussed in `grey.bioaugmentation`, since a new vessel has no incumbent community
- Anaerobic digestion process modelling conventions, which are the shared description the field designs against
- PAS 110 and equivalent digestate quality specifications, and the compost quality schemes alongside them, which set limits on physical contaminants and stability
- Compost stability and maturity testing, including respiration and self-heating methods, which distinguish a finished product from one that will continue reacting in a heap
- Nutrient analysis and application planning conventions, which is how a spreading rate is derived from crop demand rather than from what is in storage
- Sampling protocols for physical contaminants, which is the measurable consequence of collection policy
- Methane leakage measurement and quantification protocols, which are the difference between a measured climate benefit and an assumed one
- Life cycle assessment conventions under ISO 14040 and ISO 14044, applied with landfill rather than with nothing as the counterfactual
- Greenhouse gas accounting practice for waste treatment, including the global warming potential horizon chosen, which materially changes how methane leakage is weighed
- Gas safety, storage and flare practice, which is where the record's most serious physical hazards sit

### Related records

- `grey.wastewater_treatment`
- `white.biofuels`
- `green.biofertilisers`
- `grey.air_biotreatment`
- `grey.bioaugmentation`
- `white.microbial_fermentation`

### Cross-references

- [grey.wastewater_treatment](wastewater_treatment.md)
- [white.biofuels](../white/biofuels.md)
- [green.biofertilisers](../green/biofertilisers.md)
- [grey.air_biotreatment](air_biotreatment.md)
- [grey.bioaugmentation](bioaugmentation.md)
- [white.microbial_fermentation](../white/microbial_fermentation.md)
