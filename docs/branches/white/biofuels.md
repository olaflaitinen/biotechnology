<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/white/biofuels/.
  Edit the source and run `make docs`.
-->

[White Biotechnology](index.md) / **Biofuels and Bioenergy**

## Biofuels and Bioenergy

`white.biofuels`

Producing liquid and gaseous transport fuels from biological feedstocks by fermentation, conversion or hydroprocessing.

### What it is

Biofuels are conventionally described in generations. The first ferments sugar or starch to ethanol, or esterifies vegetable oil to biodiesel, using feedstocks that are also food. It is mature, it operates at very large scale, and it is the source of the field's central controversy. The second converts lignocellulosic residues, meaning straw, bagasse, forest residue and energy grasses, which do not compete directly for food. The third uses algae. A fourth category, made from carbon dioxide and renewable electricity, is really chemistry with a biological step optional. The second generation is where biotechnology matters most and where the field has disappointed most. Plant cell walls evolved specifically to resist microbial degradation, and that recalcitrance is the whole problem. Lignin must be disrupted by a pretreatment that is energy intensive and that generates furans and organic acids which inhibit the organisms in the next step. Cellulase enzyme loadings are high and their cost per litre of fuel has remained a principal barrier. And hydrolysis releases xylose alongside glucose, which the standard ethanol yeast does not naturally ferment, so the organism must be engineered to use a sugar it evolved to ignore. Two questions decide whether any biofuel is worth producing, and neither is answered by the fermentation. The first is energy return: how much energy the fuel delivers relative to the energy consumed growing, harvesting, transporting and converting it. The second is greenhouse gas intensity over the full life cycle, including the emissions caused when land is converted to grow the feedstock, or when displaced food production converts land elsewhere. That second effect, indirect land use change, is real, is difficult to measure, and can be large enough to reverse the apparent benefit of a crop-based fuel. Demand has shifted accordingly. Road transport is electrifying, which removes the largest market that first generation fuels were built for. What cannot easily electrify is aviation, shipping and heavy freight, and the sector's centre of gravity has moved to drop-in fuels for those uses, particularly sustainable aviation fuel made from waste oils and residues rather than from crops.

### In plain language

Biofuels are fuels made from plants or waste rather than from oil wells. The simple version, turning maize or sugarcane into alcohol for cars, works and is made in enormous quantities. The argument about it is whether it is worth doing: growing the crop takes land, fertiliser, water and fuel, so the honest question is not whether you get energy out but how much is left after everything you put in. For sugarcane the answer is clearly favourable. For maize it is much closer, and people who have studied it carefully still disagree. The version that would avoid the argument entirely, making fuel from straw and other waste nobody eats, turned out to be far harder than expected, and most of the plants built to do it have closed.

### An analogy

Judging a fuel by how much energy it contains is like judging a job by its salary while ignoring the commute. If most of the wage goes on getting to work, the number on the contract tells you very little. Some biofuels are a short walk from home and some are a long expensive drive, and the whole argument in this field is about which is which.

### Why it matters

Transport is one of the hardest sectors to decarbonise, and aviation, shipping and heavy freight have no near-term electric answer, so a liquid fuel that is not fossil remains genuinely necessary for them. Brazil has run a substantial share of its light vehicle fleet on sugarcane ethanol for decades, which is a real and large-scale demonstration rather than a proposal. Biogas from waste turns a disposal problem into an energy supply. Against that stand costs this record states plainly. Crop-based fuel competes for land, water and fertiliser with food, and the displacement effects reach countries that never produced the fuel. Cellulosic ethanol, the technology that would have resolved that conflict, was mandated in volumes it never came close to delivering, and most of the flagship plants built for it have closed. Algal fuel absorbed large investment in the late 2000s and largely redirected itself towards higher value products. And a fuel is a low-value, high-volume commodity competing against an incumbent with a century of cost optimisation and, in many jurisdictions, subsidies of its own. Biofuel policy has been unusually prone to mandating outcomes that the underlying technology could not supply, which is a lesson about policy design as much as about biology.

### Applications

- Sugarcane ethanol, produced at very large scale for decades and the clearest case of a favourable energy return in the field
- Maize and wheat starch ethanol, the largest volume by production and the subject of a long unresolved argument about its net energy and emissions
- Biodiesel by transesterification of vegetable oils, mature and limited by the same feedstock competition
- Molasses and beet ethanol as regional variants of the same process
- Hydrotreated esters and fatty acids from used cooking oil and rendered animal fats, which is currently the principal route to sustainable aviation fuel and is constrained by feedstock availability rather than by technology
- Biogas and upgraded biomethane from anaerobic digestion of manure, sewage sludge and food waste, which converts a disposal cost into an energy supply and is the least disputed application in this record
- Lignocellulosic ethanol from straw, bagasse, corn stover and energy grasses, demonstrated at commercial scale and then largely withdrawn, as recorded in `history.py`
- Lignin valorisation into materials and chemicals, pursued because lignocellulosic fuel economics do not close on the fuel alone
- Consolidated bioprocessing, in which one organism both secretes the enzymes and ferments the sugars, which would remove the enzyme cost entirely and remains a research objective
- Gas fermentation of steel mill and refinery off-gas to ethanol, commercially operating and notable for using a feedstock that competes with nothing
- Syngas fermentation from gasified biomass and waste
- Algal lipid and hydrocarbon production, which absorbed substantial investment in the late 2000s and mostly redirected towards higher value products, as `blue.algal_biotechnology` records
- Electrofuels and carbon dioxide derived fuels using renewable electricity, where the biological step is optional and the economics are set by electricity price
- Biobutanol and isobutanol as higher energy density alternatives to ethanol that avoid the blend limit
- Farnesane and other terpene-derived drop-in fuels, produced by engineered strains and generally viable only where a specialty market pays more than a fuel market would

### Technologies

- Dilute acid, steam explosion and hydrothermal pretreatment, which disrupt the lignin barrier and in doing so generate the furans and organic acids that inhibit the fermentation two steps later
- Alkaline and organosolv pretreatment, which preserve more of the lignin for valorisation at higher reagent cost
- Ionic liquid and deep eutectic solvent pretreatment, effective and so far too expensive at fuel scale
- Mechanical size reduction, which is unglamorous and a substantial part of the parasitic energy load
- Cellulase and hemicellulase cocktails, whose cost per litre of fuel has remained the principal unresolved barrier for this route
- Simultaneous saccharification and fermentation, which removes the sugar as it is released and thereby relieves the product inhibition of the enzymes
- Consolidated bioprocessing by an organism that secretes the enzymes and ferments the sugars itself
- Engineered pentose-fermenting yeast, since hydrolysis releases xylose alongside glucose and the standard ethanol yeast does not use it
- Inhibitor-tolerant strains selected or evolved against the pretreatment products, which is why adaptive evolution appears in a fuel process
- Thermophilic and anaerobic fermentation, which reduces cooling and contamination control cost in a margin-critical process
- Distillation and molecular sieve dehydration, the largest single energy consumer in ethanol production and the reason low titre is fatal here rather than merely undesirable
- In situ product removal by gas stripping or pervaporation for butanol, where product toxicity caps titre far lower than for ethanol
- Transesterification and hydrotreating to produce esters and drop-in hydrocarbons that meet existing fuel specifications
- Anaerobic digestion and biogas upgrading to pipeline-quality biomethane
- Life cycle assessment and carbon intensity modelling, including indirect land use change, which is not an accounting exercise here but the determinant of whether the fuel may be sold as renewable at all

### Challenges

- Competing as a low-value high-volume commodity against a fossil incumbent with a century of cost optimisation, which means a technically successful process can still be commercially worthless
- Lignocellulose recalcitrance, since plant cell walls evolved specifically to resist microbial degradation and every pretreatment is an attempt to defeat that evolution at acceptable energy cost
- Inhibitors generated by pretreatment, which poison the fermentation that the pretreatment exists to enable
- Enzyme cost per litre of fuel, the principal unresolved barrier to cellulosic ethanol and the reason consolidated bioprocessing is pursued
- Pentose utilisation, since a large fraction of the available sugar is xylose and the standard ethanol organism ignores it
- The stoichiometric ceiling of 0.51 grams of ethanol per gram of glucose, which means roughly half the feedstock mass leaves as carbon dioxide before any process inefficiency is counted
- Product toxicity, which caps butanol titre far below ethanol and makes in situ removal a requirement rather than an optimisation
- Distillation energy at low titre, which can consume a large share of the fuel's own energy content
- Feedstock competition with food for land, water and fertiliser, which is the field's defining controversy and is not resolved by any technical improvement to the conversion step
- Indirect land use change, real in principle, contested in magnitude, and capable of reversing the apparent benefit of a crop-based fuel
- Feedstock collection logistics, since residues are bulky, low in density and seasonal, which caps the economic radius of a plant
- The ethanol blend limit in existing vehicle fleets, which caps demand independently of supply and is why drop-in fuels are pursued
- Policy instability and mandates set beyond what the technology could deliver, which drew investment into capacity that then had no market

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Energy return on investment | `EROI` | megajoules of fuel delivered per megajoule consumed, dimensionless | around 8 - 10 for sugarcane ethanol; roughly 1.2 - 1.6 for maize ethanol, and disputed | REPORTED |
| Life cycle greenhouse gas intensity | `CI` | grams of carbon dioxide equivalent per megajoule | roughly 90 for fossil petrol; 15 - 80 for biofuels depending on feedstock and on the land use change assumption | REPORTED |
| Indirect land use change penalty | `ILUC` | grams of carbon dioxide equivalent per megajoule added | near zero for wastes and residues; substantial and disputed for crop-based fuels, largest for those displacing oilseed | REPORTED |
| Fuel yield per hectare per year | `Y_land` | litres of fuel per hectare per year | roughly 6000 - 8000 L/ha for sugarcane ethanol; roughly 3500 - 4500 for maize; roughly 1000 - 1500 for rapeseed biodiesel | REVIEWED |
| Theoretical ethanol yield from glucose | `Y_max` | grams of ethanol per gram of glucose | 0.511 g/g, with industrial processes reaching 90 - 95 % of it | CONSENSUS |
| Ethanol titre | `C_EtOH` | per cent weight per volume in the fermented broth | 12 - 16 % w/v for starch and sugar feedstocks; 4 - 6 % is common for lignocellulosic | CONSENSUS |
| Sugar release from pretreatment and hydrolysis | `X_sugar` | per cent of theoretically available sugar released | 65 - 90 % depending on feedstock and pretreatment severity | REVIEWED |
| Enzyme cost per litre of fuel | `C_enz` | euro cents per litre | historically the largest single unresolved operating cost for lignocellulosic ethanol | REPORTED |
| Volumetric energy density | `E_v` | megajoules per litre | about 21 for ethanol, 27 for butanol, 33 for biodiesel, against about 32 for petrol and 36 for diesel | CONSENSUS |
| Blend limit | `B_max` | per cent by volume compatible with the existing vehicle fleet | around 10 % ethanol in petrol for unmodified vehicles; higher only with flex-fuel engines | CONSENSUS |
| Water footprint | `W_f` | litres of water per litre of fuel | dominated by feedstock irrigation, and negligible for rain-fed or residue feedstocks | REVIEWED |

### History

- **1900** - Diesel demonstrates a compression ignition engine running on peanut oil
- **1908** - The Ford Model T is designed to run on ethanol as well as petrol
- **1975** - Brazil launches a national programme to substitute sugarcane ethanol for imported petrol
- **2003** - The European Union adopts its first biofuels directive with indicative targets
- **2005** - The United States establishes a renewable fuel standard with volumetric mandates
- **2008** - Indirect land use change is quantified and the case for crop-based fuels is substantially weakened
- **2008** - Food price spikes bring the food and fuel argument into public politics
- **2009** - Algal biofuel attracts major investment and largely fails to deliver fuel
- **2014** - Commercial cellulosic ethanol plants open, and most are idled or closed within a few years
- **2016** - A global market-based measure for international aviation emissions is agreed
- **2018** - European policy caps crop-based fuels and prioritises wastes and residues
- **2022** - Gas fermentation of industrial off-gas to ethanol reaches commercial operation

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | REGULATED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | ENERGY, ENVIRONMENT, FOOD |
| SDGs | 7, 12, 13 |

### Regulations

- Directive (EU) 2018/2001 on the promotion of energy from renewable sources, with its transport target, its cap on crop-based fuels, its sustainability criteria and its treatment of high indirect land use change risk feedstocks
- The United States Renewable Fuel Standard and its volumetric mandates, including the repeatedly revised cellulosic obligation described in `history.py`
- Low carbon fuel standards that price a fuel by its computed carbon intensity rather than by its volume
- Directive 98/70/EC on fuel quality and its greenhouse gas reduction obligation on suppliers
- Sustainability and greenhouse gas saving criteria, including the prohibition on feedstock from land with high carbon stock or high biodiversity value
- Rules on wastes and residues, and on the double counting that distinguishes them from crop feedstocks
- Regulation (EU) 2023/2405 and comparable instruments mandating sustainable aviation fuel uptake
- Directive 2010/75/EU on industrial emissions, and discharge consents for stillage and process effluent, which for ethanol production is a large stream
- Directive 2012/18/EU Seveso III and Directive 1999/92/EC, since these plants hold substantial inventories of flammable liquid
- Directive 2009/41/EC on the contained use of genetically modified microorganisms, which applies to the engineered pentose-fermenting strains this record depends on
- Excise duty differentials and tax exemptions for renewable fuels, which in several jurisdictions have moved more volume than any mandate

### Standards

- Voluntary certification schemes recognised for demonstrating compliance with sustainability criteria, which audit the chain of custody from field to fuel
- Mass balance chain of custody methodology, the bookkeeping convention that allows certified and uncertified material to share infrastructure without the claim being lost
- Roundtable on Sustainable Biomaterials and comparable scheme criteria covering land rights, labour and biodiversity alongside carbon
- Prescribed life cycle methodologies and default values, which fix system boundary and co-product allocation so that two suppliers are computing the same quantity
- ISO 14040, ISO 14044 and ISO 14067 as the underlying assessment methodology
- CORSIA eligibility criteria and default life cycle values for aviation fuel
- EN 15376 and ASTM D4806 for ethanol as a blending component
- EN 14214 and ASTM D6751 for fatty acid methyl ester biodiesel
- ASTM D7566 for aviation turbine fuel containing synthesised hydrocarbons, which is what makes a drop-in fuel usable in an existing aircraft
- EN 16723 and comparable specifications for biomethane injected into the gas grid
- Radiocarbon-based biobased content determination, one of the few properties of the finished fuel that can be verified analytically rather than by audit

### Related records

- `white.industrial_enzymes`
- `white.metabolic_engineering`
- `green.plant_genetic_engineering`
- `white.bioprocess_engineering`
- `white.biobased_chemicals`
- `blue.algal_biotechnology`
- `grey.wastewater_treatment`

### Cross-references

- [white.industrial_enzymes](industrial_enzymes.md)
- [white.metabolic_engineering](metabolic_engineering.md)
- [green.plant_genetic_engineering](../green/plant_genetic_engineering.md)
- [white.bioprocess_engineering](bioprocess_engineering.md)
- [white.biobased_chemicals](biobased_chemicals.md)
- [blue.algal_biotechnology](../blue/algal_biotechnology.md)
- [grey.wastewater_treatment](../grey/wastewater_treatment.md)
