<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/grey/wastewater_treatment/.
  Edit the source and run `make docs`.
-->

[Grey Biotechnology](index.md) / **Wastewater Treatment**

## Wastewater Treatment

`grey.wastewater_treatment`

Continuous treatment of sewage and effluent by managed microbial communities, in which the engineering selects the organisms rather than supplying them.

### What it is

Biological wastewater treatment is the largest deliberate application of microorganisms anywhere, operating continuously in every city that has sewerage. Its defining feature is that the organisms are neither supplied nor defined. They arrive in the influent, and the plant is engineered to select for the ones that do the required work. Solids retention time determines which organisms can grow fast enough to remain in the system, hydraulic retention time sets the contact available, aeration decides what respires and what does not, and the sequence of aerobic, anoxic and anaerobic zones determines which metabolisms are favoured in turn. An operator changes an outcome by changing a condition, which is the exact inverse of the sterile defined-strain approach recorded in `white.microbial_fermentation`. Three separate jobs are done and they compete for the same reactor. Organic carbon removal is fast, robust and largely solved: heterotrophic organisms oxidise dissolved organic matter within hours, and this is what the original activated sludge process was built for. Nitrogen removal is harder because it takes two contradictory steps. Nitrification, which oxidises ammonium to nitrate, is performed by slow-growing autotrophs that need oxygen and a long solids retention time and that are the first thing lost when a plant is overloaded or cold. Denitrification, which converts nitrate to nitrogen gas, requires the absence of oxygen and a supply of organic carbon, so the plant must provide anoxic and aerobic conditions in sequence, and the carbon that would have been removed in step one is needed in step two. Phosphorus removal is different again, since phosphorus is neither degraded nor volatilised: it can only be moved into biomass or precipitated, and the biological route depends on alternating anaerobic and aerobic exposure to select organisms that store it in excess. Every one of those processes produces sludge, and sludge handling is commonly around half the cost of running a treatment works. This is the part of the subject that public accounts omit. Removing pollutants from water converts them into a wet solid containing the organisms, the phosphorus, the metals and whatever else was in the sewage. It is thickened, frequently digested anaerobically to reduce its mass and produce methane, dewatered, and then applied to land, incinerated or landfilled. The treatment plant does not make the material disappear; it concentrates it into a form that can be dealt with. What the process does not remove matters increasingly. Pharmaceuticals, hormones, per- and polyfluoroalkyl substances and microplastics pass through a plant designed decades ago for carbon and nutrients, and removing them requires additional physical or chemical stages rather than better biology. Antibiotic resistance genes are concentrated rather than destroyed in the dense mixed community of a reactor, which is a concern shared with `dark.antimicrobial_resistance`. And the whole system is energy-intensive, since aeration alone accounts for a substantial share of many municipalities' electricity use.

### In plain language

A sewage works is a farm for bacteria. The sewage arrives already full of microbes, and the plant is built to give the useful ones the conditions they need and to wash the rest out. Nobody buys the bacteria or puts them in; the design decides which ones thrive. They eat the organic matter within hours. Getting rid of nitrogen takes two opposite steps, one needing air and one needing none, so the water is moved between tanks. Phosphorus cannot be destroyed at all and is instead stored inside the bacteria and taken away with them. That is the catch nobody mentions: everything removed from the water ends up in a wet sludge, and dealing with the sludge costs about as much as treating the water. This process protects the drinking water of most of the world, it is over a century old, and it is probably the largest use of biology anywhere.

### An analogy

It is grazing management rather than sowing a crop. Nobody plants the pasture; what grows is decided by how often it is cut, how wet it is kept and how long the animals stay. Change the schedule and different plants take over. A treatment works is run the same way, by adjusting residence times and aeration until the community that thrives is the one doing the job. And as on any farm, the material that comes out at the other end is half the work.

### Why it matters

This is among the largest public health interventions ever deployed. Separating sewage from drinking water is what ended cholera and typhoid as ordinary urban facts, and biological treatment is what makes that possible at city scale without simply moving the problem downstream. It predates antibiotics, it has run continuously for a century, and it protects more people daily than any medicine in this library. It also protects surface waters directly. Untreated sewage strips oxygen from a river and kills it; nutrient discharge causes the algal blooms and dead zones recorded in `blue.algal_biotechnology`. Anaerobic digestion of the resulting sludge recovers methane, which turns part of the energy cost back. The limits are substantial and are becoming more visible. Aeration is energy-intensive enough to be a significant share of municipal electricity consumption. Sludge disposal is roughly half the operating cost and has no comfortable answer: land application returns nutrients and also returns metals and persistent chemicals, incineration costs energy, and landfill defers the question. Pharmaceuticals, hormones and fluorinated compounds pass through a process not designed to catch them. Combined sewer overflows discharge untreated sewage during heavy rain by design, which is a structural feature of old networks rather than a failure of the biology. Nutrient removal costs considerably more than carbon removal and is therefore the first thing not built where budgets are short. And the deepest inequity in this record is one of coverage: a large share of the world's population is not connected to any treatment at all, so the technology is mature, proven, and absent exactly where the disease burden is highest.

### Applications

- Municipal sewage treatment by activated sludge, which is the largest single deployment of microorganisms anywhere and which oxidises dissolved organic matter within hours
- Trickling filter and rotating biological contactor treatment, which achieve the same removal with the biomass fixed on a surface and far less energy for mixing
- High-strength industrial effluent treatment at breweries, dairies, pulp mills and food factories, where the organic load per volume is many times that of sewage
- Anaerobic treatment of high-strength effluent in upflow sludge blanket reactors, which converts the organic load to methane instead of to biomass and therefore produces energy rather than consuming it
- Lagoon and waste stabilisation pond treatment, which is the low-cost option where land is available and which is how a large share of the world's treated wastewater is actually handled
- Nitrification of ammonium to nitrate by slow-growing autotrophs, which requires oxygen and a long solids retention time and which is the first capability a plant loses when it is overloaded or cold
- Denitrification of nitrate to nitrogen gas, which requires the absence of oxygen and a supply of organic carbon, so the plant must sequence anoxic and aerobic zones and must not have removed all the carbon first
- Anaerobic ammonium oxidation for concentrated side streams, which converts ammonium directly to nitrogen gas without the full oxygen demand or the carbon requirement of the conventional pair
- Nitrite shunt operation, stopping the oxidation one step early to save aeration energy and carbon, which requires holding a community in a state it does not naturally settle into
- Enhanced biological phosphorus removal, in which alternating anaerobic and aerobic exposure selects organisms that store phosphorus far in excess of their needs, so the phosphorus leaves in the sludge rather than in the water
- Chemical precipitation with iron or aluminium salts, which is the reliable alternative and which produces more sludge and no recoverable product
- Struvite crystallisation from digester liquors, which recovers phosphorus as a usable fertiliser and simultaneously prevents the scaling that the same chemistry causes inside the pipework
- Pathogen reduction by disinfection and by retention in ponds, which is a distinct unit process rather than a by-product of the biological stages and which is the objective most directly tied to public health
- Water reuse treatment for irrigation and industrial supply, and potable reuse where the additional physical and chemical barriers are present
- Anaerobic digestion of sludge, which reduces its mass, destroys pathogens and produces methane that offsets part of the plant's energy demand
- Thickening and dewatering, which determine the mass of material that has to be transported and are therefore the dominant handling cost
- Land application of treated biosolids, which returns nitrogen and phosphorus to soil and simultaneously returns the metals and persistent chemicals that arrived in the sewage
- Incineration and thermal treatment, which destroys organic contaminants and concentrates metals into ash that must then be disposed of

### Technologies

- Activated sludge with return of settled biomass, which is the whole invention: separating solids retention time from hydraulic retention time so slow-growing organisms can be kept in a fast-flowing system
- Sequencing batch reactors, which perform the same sequence of conditions in time within one tank rather than in space across several
- Oxidation ditches and extended aeration, which trade footprint and energy for stability and a simpler operating regime
- Trickling filters and rotating contactors, where the community grows as a film on media and the water passes over it
- Moving bed and integrated fixed-film systems, which suspend carrier media in a reactor to add biomass without adding settling duty
- Granular sludge processes, in which the biomass self-aggregates into dense granules that settle rapidly and hold aerobic and anoxic zones within a single granule
- Membrane bioreactors, which remove the settling constraint entirely and permit very high biomass concentrations at the cost of energy and membrane fouling
- Anaerobic membrane bioreactors, which combine energy recovery with complete solids retention
- Solids retention time control, which is the primary lever: it decides whether slow-growing nitrifiers can persist at all
- Dissolved oxygen control and aeration management, which is the largest energy cost in the plant and therefore the largest optimisation target
- Anaerobic, anoxic and aerobic zone sequencing, which is how nitrogen and phosphorus removal are engineered into the same reactor
- Real-time sensing and model-based control, including ammonium-based aeration control that matches air supply to actual load
- Molecular community profiling of the mixed liquor, which turned plant operation from inference into observation and identified organisms that had never been cultured
- Microscopic examination of floc structure and filament identification, which remains the fastest practical diagnostic for settling problems
- Biogas capture and combined heat and power generation, which is what makes an energy-neutral works conceivable
- Nutrient recovery as struvite and ammonium salts, and polyhydroxyalkanoate recovery from sludge, which links this record to `white.biopolymers`

### Challenges

- Filamentous bulking, in which filament-forming organisms prevent the sludge from settling, so biomass leaves with the effluent and the plant loses the community it depends on, which is the commonest serious operational failure
- Foaming caused by hydrophobic filamentous organisms, which floats biomass off the surface and is difficult to eliminate once established
- Loss of nitrification under cold, overload or toxic conditions, since the autotrophs grow slowly enough that recovery takes weeks rather than days
- Toxic and hydraulic shock loads from industrial discharges, which can kill the biomass outright and leave reseeding as the only recovery
- Aeration energy, which is a substantial share of the electricity use of many municipalities and is the single largest operating cost
- Sludge handling and disposal, commonly around half the cost of running a works, with no comfortable destination for the material
- Metals and persistent organic chemicals accumulating in biosolids, which constrain land application and are the reason a nutrient resource is treated as a waste
- Pharmaceuticals, hormones and endocrine active compounds passing through at concentrations sufficient to affect receiving water organisms
- Per- and polyfluoroalkyl substances, which resist biological treatment entirely and require additional physical or chemical stages
- Microplastics, which are largely captured into the sludge and therefore returned to land with it rather than removed from the system
- Antibiotic resistance genes, which are concentrated rather than destroyed in a dense mixed community and are discharged in both effluent and biosolids
- Combined sewer overflows discharging untreated sewage during heavy rainfall by design, which is a property of old networks rather than a failure of treatment
- Nutrient removal costing considerably more than carbon removal, so it is the first capability omitted where budgets are constrained
- Ageing infrastructure and deferred renewal, which is the commonest reason a plant underperforms its design
- Absence of any treatment for a large share of the world's population, which is the deepest inequity in this record and is a matter of capital and governance rather than of technology

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Solids retention time | `SRT` | days | a few days for carbon removal alone; substantially longer where nitrification must be maintained | CONSENSUS |
| Hydraulic retention time | `HRT` | hours | hours for the aerated stages of a municipal works | CONSENSUS |
| Food to microorganism ratio | `F/M` | kilograms of biochemical oxygen demand per kilogram of mixed liquor suspended solids per day | low values give stable well-settling sludge, high values give rapid growth and poor settling | CONSENSUS |
| Biochemical oxygen demand | `BOD5` | milligrams of oxygen per litre over five days at twenty degrees | a few hundred in raw municipal sewage, a small fraction of that in treated effluent | CONSENSUS |
| Chemical oxygen demand | `COD` | milligrams of oxygen per litre | higher than the biochemical value for the same sample, since it includes matter the organisms will not oxidise | CONSENSUS |
| Removal efficiency | `eta` | per cent of influent load removed | high for carbon in any functioning works; lower and far more variable for nitrogen and phosphorus | CONSENSUS |
| Ammonium and total nitrogen in effluent | `c_N` | milligrams of nitrogen per litre | tightly limited in sensitive catchments and unregulated in many others | CONSENSUS |
| Total phosphorus in effluent | `c_P` | milligrams of phosphorus per litre | low limits in sensitive catchments, achieved biologically, chemically or by both together | CONSENSUS |
| Sludge volume index | `SVI` | millilitres per gram of settled sludge | a low value settles well; a high value indicates bulking | CONSENSUS |
| Sludge production | `Y_obs` | kilograms of dry solids per kilogram of oxygen demand removed | substantially lower for anaerobic processes than for aerobic ones | CONSENSUS |
| Mixed liquor suspended solids | `MLSS` | milligrams per litre | a few thousand in conventional activated sludge, several times that in a membrane bioreactor | CONSENSUS |
| Aeration energy per volume treated | `E_air` | kilowatt hours per cubic metre | the dominant electricity demand of a conventional works | REPORTED |
| Biogas yield from digestion | `Y_gas` | cubic metres of methane per kilogram of volatile solids destroyed | sufficient at many works to offset a substantial share of the site electricity demand | CONSENSUS |
| Micropollutant removal | `eta_micro` | per cent removal of a named pharmaceutical or industrial compound | highly compound-dependent, from near complete to negligible | REVIEWED |

### History

- **1854** - A London cholera outbreak is traced to a contaminated water supply
- **1890** - Septic tanks and contact beds provide the first deliberate biological treatment
- **1914** - Activated sludge is developed by returning settled solids to the aeration tank
- **1936** - Anaerobic digestion of sludge with gas capture is adopted at municipal scale
- **1965** - Eutrophication is attributed to nutrient discharge from treated effluent
- **1972** - Comprehensive water pollution legislation makes secondary treatment a legal requirement
- **1976** - Enhanced biological phosphorus removal is developed by alternating anaerobic and aerobic conditions
- **1980** - Combined nitrification and denitrification process configurations enter general use
- **1989** - Membrane bioreactors remove the settling constraint on biomass concentration
- **1995** - Molecular methods reveal that the dominant organisms in activated sludge had never been cultured
- **1999** - Anaerobic ammonium oxidation is confirmed in engineered systems
- **2005** - Aerobic granular sludge achieves settling and nutrient removal in a single reactor
- **2012** - Micropollutants and antibiotic resistance genes are documented passing through conventional treatment
- **2020** - Wastewater surveillance is deployed at population scale for infectious disease monitoring

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | ENVIRONMENT, HEALTH, ENERGY, FOOD |
| SDGs | 3, 6, 7, 11, 14 |

### Regulations

- Discharge consents and permits setting numerical limits on oxygen demand, suspended solids, ammonium, total nitrogen and total phosphorus, which specify the result and say nothing about the process used to reach it
- The Urban Waste Water Treatment Directive 91/271/EEC and its national equivalents, which set collection and treatment obligations by settlement size and impose stricter nutrient limits on sensitive catchments
- The Water Framework Directive 2000/60/EC, which sets the receiving water status that discharge limits are ultimately derived from
- Self-monitoring, record-keeping and reporting obligations, including continuous instrumentation where the consent requires it
- Personal criminal liability for operators and managers on consent breach in several jurisdictions, which is a level of enforcement almost nothing else in this library carries
- Combined sewer overflow permits authorising the discharge of untreated sewage during heavy rainfall, which are lawful by design rather than a failure of enforcement and which reflect the cost of separating storm and foul networks in old cities
- Storm water and emergency overflow reporting requirements, including event duration monitoring
- Trade effluent consents and pretreatment requirements, which control what industry may discharge to sewer and are the plant's protection against the toxic shock loads that kill its biomass
- Prohibitions on discharging listed hazardous substances to sewer, since a works cannot remove what it was not designed for and will simply pass it on
- The Sewage Sludge Directive 86/278/EEC and national equivalents, setting metal limits, treatment requirements and application rates for biosolids used on agricultural land
- Waste framework legislation classifying sludge, and the end-of-waste criteria that determine when treated biosolids cease to be waste
- Animal by-products and pathogen reduction requirements where biosolids are applied to grazing land or to crops entering the food chain
- Emission limits and permitting for sludge incineration, and the classification of the resulting ash
- Water reuse regulation, including Regulation (EU) 2020/741 on minimum requirements for water reuse in agricultural irrigation
- Drinking water quality legislation, which sets the standard that any potable reuse scheme must ultimately satisfy
- Bathing water and shellfish water designations, which impose pathogen limits on discharges upstream of them
- Operator certification and competence requirements, which in many jurisdictions are a condition of the permit itself
- Confined space, gas and worker safety law, since digester gas is explosive and treatment works contain the two most common causes of fatal accidents in the water industry

### Standards

- Standard Methods for the Examination of Water and Wastewater, which define the biochemical oxygen demand procedure that discharge law is written in and without which the limit would have no meaning
- ISO analytical standards for chemical oxygen demand, nitrogen species, phosphorus and suspended solids
- Sampling and flow measurement conventions, including composite sampling, which determine whether a reported value represents the day or the moment it was taken
- Instrument calibration, validation and data quality practice for continuous online monitoring
- Laboratory accreditation to ISO 17025 for compliance analysis
- Activated sludge model formulations, which are the shared mathematical description the field designs and simulates against
- Design codes and loading guidance for the unit processes, including the solids retention time required to sustain nitrification at a given temperature
- Aeration system testing and oxygen transfer efficiency determination, which is how the plant's largest energy cost is specified and verified
- Energy benchmarking conventions for treatment works, which is what an efficiency programme is measured against
- Microscopic sludge examination and filament identification protocols, which remain the fastest practical diagnostic for a settling problem
- Sludge volume index determination methods, which are the early warning for the failure that shuts plants down
- Molecular community profiling conventions for mixed liquor, which identified the organisms the process had been using for eighty years without knowing it
- Respirometric testing for influent characterisation and toxicity screening
- ISO 9001 and ISO 14001 management systems as applied by water utilities
- Asset management practice under ISO 55000, which is what determines whether ageing infrastructure is renewed before it underperforms
- Water safety plan methodology, which applies a hazard analysis approach from source to discharge and to reuse
- Digester gas handling and explosion protection practice, which is the safety standard with the highest consequence attached to it

### Related records

- `white.microbial_fermentation`
- `grey.biowaste_treatment`
- `blue.algal_biotechnology`
- `grey.environmental_biomonitoring`
- `grey.bioaugmentation`
- `dark.antimicrobial_resistance`

### Cross-references

- [white.microbial_fermentation](../white/microbial_fermentation.md)
- [grey.biowaste_treatment](biowaste_treatment.md)
- [blue.algal_biotechnology](../blue/algal_biotechnology.md)
- [grey.environmental_biomonitoring](environmental_biomonitoring.md)
- [grey.bioaugmentation](bioaugmentation.md)
- `dark.antimicrobial_resistance` (branch not written yet)
