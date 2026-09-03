<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/white/microbial_fermentation/.
  Edit the source and run `make docs`.
-->

[White Biotechnology](index.md) / **Microbial Fermentation**

## Microbial Fermentation

`white.microbial_fermentation`

Cultivating microorganisms at industrial scale under controlled and usually sterile conditions, so that a strain performs in a vessel what it was engineered to do.

### What it is

Microbial fermentation is the cultivation step: growing a defined strain from a preserved vial to a production vessel of tens or hundreds of cubic metres, feeding it, keeping everything else out, and holding the conditions that make it produce. It is distinguished from bioprocess engineering, which designs the equipment and carries the product through recovery and purification afterwards. This record is about what the culture does; that one is about what the plant does. Four modes are used. Batch is the simplest and is limited by the inhibition that follows from putting all the substrate in at once. Fed-batch supplies substrate gradually and dominates industrial practice, for a reason that is not obvious: above a critical feed rate most organisms switch to overflow metabolism, excreting acetate or ethanol rather than converting carbon to product, so feeding faster lowers output. Controlling the feed to hold specific growth rate below that threshold is the central operating decision of the field. Continuous culture holds a steady state indefinitely by matching dilution rate to growth rate. Solid-state fermentation grows organisms on a moist solid substrate with little free water, which suits filamentous fungi and some enzyme production. Two things decide whether a campaign succeeds, and neither is the strain. The first is sterility. A production vessel is a rich, warm, well-mixed nutrient broth, which is to say an excellent growth medium for whatever arrives first, and a contaminant with a shorter doubling time will outgrow the production organism within hours. Sterilisation of the vessel, the medium, the air and every addition is therefore not a precaution but the process itself. The second is oxygen. Aerobic fermentation consumes oxygen far faster than it dissolves, oxygen transfer does not improve with vessel size, and in most large aerobic processes the real ceiling on productivity is set by the vessel rather than by the organism. Continuous culture is more productive per unit of capital and is used very little. The reasons are practical rather than theoretical: a long run gives contamination more opportunities, selection favours any mutant that stops making the product, and a regulated product is defined by batch, which a process without batches does not naturally provide. This record treats that gap between the theoretically better option and the commonly chosen one as a finding rather than an embarrassment.

### In plain language

Fermentation is growing microbes on purpose, in a tank, to make something. It is how penicillin is made, how vitamins and food ingredients are made, and how most of the enzymes and biological medicines in use today are made. The engineering is mostly about three unglamorous problems. Keeping everything else out, because a tank of warm nutrient broth is exactly what every other microbe in the world would like. Getting enough air in, because a dense culture uses oxygen far faster than it can dissolve. And feeding at the right speed, because feeding a culture too fast makes it waste the food rather than grow faster.

### An analogy

It is tending a stove rather than filling a tank. A tank simply takes whatever you pour into it. A stove has an air supply, and fuel piled on faster than the air can support it does not burn hotter, it smoulders and makes smoke. So the skill is in matching the feed to the draught, continuously, for days. And the fire is in a room where every other spark in the neighbourhood would happily take over, so the door stays shut.

### Why it matters

Almost every product in this branch reaches the world through a fermenter. Antibiotics, insulin and most therapeutic proteins, the industrial enzymes in detergent and feed, the amino acids and vitamins that go into animal nutrition, citric acid, and the newer proteins made without animals all depend on this one operation. It is also where a great deal of a plant's cost sits: sterilisation consumes energy and time, aeration and agitation consume power continuously, and a contaminated batch is a complete loss of everything that went into it, including the days it occupied the vessel. Two structural limits deserve stating plainly. Oxygen transfer does not scale with volume, so a strain that performs beautifully in a shake flask can disappoint in a large vessel for reasons that have nothing to do with its biology. And feedstock, usually sugar or starch, competes with food and land, which is why gas and one-carbon feedstocks are being pursued despite being harder. The oldest cautionary tale in the field is a warning about the second of those: a single cell protein process that worked technically and was defeated by the price of soy.

### Applications

- Antibiotic production by filamentous fungi and actinomycetes, the process that created the modern fermentation industry
- Recombinant therapeutic protein production, including insulin and the microbial share of the biologics in `red.pharmaceutical_biotechnology`
- Vaccine antigen and viral vector production in microbial hosts
- Industrial enzyme manufacture by secreting Bacillus, Aspergillus and Trichoderma hosts, which is how every product in `white.industrial_enzymes` is physically made
- Amino acid production for animal feed at millions of tonnes a year, the largest tonnage in this record
- Vitamin and organic acid production, including citric acid, which is among the oldest large-scale fermentations still running
- Precision fermentation of dairy and egg proteins without animals, which is where this record meets `yellow.precision_fermentation`
- Yeast, probiotic and starter culture production, where the cells themselves are the product rather than something they secrete
- Bulk chemical and polymer precursor fermentation, including lactic acid and the diols in `white.biobased_chemicals`
- Ethanol and advanced biofuel production, the largest fermentation by volume anywhere in the world
- Solid-state fermentation for fungal enzyme production and for substrate upgrading, which uses little free water and suits filamentous growth
- Gas fermentation of carbon monoxide and carbon dioxide by acetogens, which removes the competition with food and land
- Methanotroph and methylotroph cultivation on methane or methanol, including single cell protein

### Technologies

- The seed train, a staged sequence of vessels each roughly ten times the last, which takes a culture from a preserved vial to production volume without ever diluting the inoculum too far
- Master and working cell bank systems, so that every campaign starts from genetically identical material rather than from a strain that has been passaged for years
- Cryopreservation and lyophilisation of production strains
- Steam-in-place and clean-in-place systems, which sterilise a vessel and its pipework without dismantling it
- Continuous medium sterilisation, which heats briefly at high temperature and preserves nutrients that batch sterilisation destroys
- Sterile filtration of process air and of heat-sensitive feed components
- Aseptic transfer, sampling and addition design, since most contamination enters through an operation rather than through a wall
- Non-sterile or contamination-resistant fermentation using extreme pH, thermophiles or a substrate only the production organism can use, which removes the largest single cost in low-value processes
- Fed-batch feeding strategies designed to hold specific growth rate below the threshold at which overflow metabolism begins
- Feedback control on dissolved oxygen, pH, or the respiratory quotient, so that the culture's own signals set the feed rate
- Complex media from molasses, corn steep liquor and other by-products, traded against defined media that cost more and behave reproducibly
- Induction strategy design, including the decision to separate a growth phase from a production phase
- Antifoam addition and foam control, an unglamorous necessity that nonetheless changes oxygen transfer
- Off-gas analysis for oxygen uptake, carbon dioxide evolution and respiratory quotient, which is the only continuous non-invasive window into a running culture
- In-line probes for dissolved oxygen, pH, temperature, pressure and optical density
- Process analytical technology and soft sensors that infer biomass and product from measurable signals
- Contamination detection by microscopy, plating and rapid molecular methods, where hours of delay decide whether a batch can be saved

### Challenges

- Contamination, which destroys not only the product but the days of vessel occupancy that produced it, and which a faster-growing organism can cause within hours of entry
- Bacteriophage infection in bacterial processes, which spreads through a plant and can idle it for weeks, and against which sterility alone is not protection
- Oxygen transfer, which does not improve with vessel size and is the true ceiling on most large aerobic processes regardless of the strain
- Overflow metabolism above a critical feed rate, which turns extra substrate into inhibitory acetate or ethanol rather than into product
- Heat removal, since a large aerobic fermentation is a substantial heat source and cooling surface does not scale with volume either
- Genetic drift and reversion over the generations of a seed train and production run, which is the operational face of the stability metric in `white.metabolic_engineering`
- Foaming, shear damage to filamentous and fragile organisms, and the rising viscosity of a dense fungal culture, all of which degrade mixing and transfer as the run proceeds
- Feedstock cost and its competition with food and land, which for a bulk product is frequently the whole economic question
- Water and energy consumption, since sterilisation, aeration, agitation and cooling are continuous demands rather than one-off ones
- Spent broth and biomass disposal, which is a large waste stream that a life cycle assessment must count against the process

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Volumetric oxygen transfer coefficient | `kLa` | per hour | 50 - 500 h^-1 in stirred tanks, falling as scale increases | CONSENSUS |
| Oxygen uptake rate | `OUR` | millimoles of oxygen per litre per hour | 50 - 250 mmol/L/h | CONSENSUS |
| Respiratory quotient | `RQ` | moles carbon dioxide evolved per mole oxygen consumed | near 1.0 for fully oxidative growth on glucose; a rise signals overflow or fermentative metabolism | CONSENSUS |
| Dissolved oxygen tension | `DOT` | per cent of air saturation | held above 20 - 30 % for most aerobic processes | CONSENSUS |
| Maximum specific growth rate | `mu_max` | per hour | 0.1 - 1.0 h^-1 depending on organism and medium | CONSENSUS |
| Critical specific growth rate | `mu_crit` | per hour | 0.1 - 0.3 h^-1, well below mu_max | REVIEWED |
| Substrate saturation constant | `K_s` | grams per litre | 0.001 - 0.5 g/L, often far below the analytical detection limit | CONSENSUS |
| Biomass yield on substrate | `Y_xs` | grams dry cell weight per gram of substrate | 0.3 - 0.5 g/g on glucose for aerobic growth | CONSENSUS |
| Maintenance coefficient | `m_s` | grams of substrate per gram dry cell weight per hour | 0.02 - 0.1 g/gDCW/h | CONSENSUS |
| Dilution rate in continuous culture | `D` | per hour | set below mu_max; washout occurs when D exceeds it | CONSENSUS |
| Batch contamination rate | `R_cont` | per cent of batches lost to contamination | below 1 - 2 % for a well-run sterile plant | REVIEWED |
| Sterilisation lethality | `F0` | equivalent minutes at 121 degrees Celsius | 15 - 20 min equivalent for medium and vessel sterilisation | CONSENSUS |
| Turnaround time | `t_turn` | hours between the end of one batch and the start of the next | 8 - 48 h | REVIEWED |

### History

- **1857** - Pasteur establishes that fermentation is caused by living microorganisms
- **1881** - Koch introduces solid media and pure culture technique
- **1916** - Weizmann's acetone-butanol-ethanol fermentation is deployed at industrial scale
- **1923** - Citric acid production by Aspergillus niger displaces extraction from citrus fruit
- **1943** - Submerged deep-tank aerated fermentation is developed for penicillin
- **1950** - The chemostat is described, allowing growth rate to be set by the operator
- **1957** - Glutamate fermentation begins commercial operation
- **1980** - A large continuous single cell protein plant begins operation and is closed within a decade
- **1982** - Recombinant human insulin produced in Escherichia coli is approved
- **1990** - Fed-batch operation with controlled feeding becomes standard industrial practice
- **2005** - Single-use bioreactors enter widespread use
- **2015** - Non-sterile and contamination-resistant fermentation is adopted for low-value products
- **2022** - Gas fermentation of industrial off-gas reaches commercial operation

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | CONTROLLED |
| Scale | INDUSTRIAL |
| Regulatory status | VARIES |
| Domains | HEALTH, FOOD, MATERIALS |
| SDGs | 2, 3, 6, 9 |

### Regulations

- Directive 2010/75/EU on industrial emissions, under which a fermentation installation above a threshold capacity requires a permit with conditions set by reference to best available techniques
- Directive 2000/60/EC, the Water Framework Directive, and national discharge consents governing spent broth and process effluent
- Directive 2014/68/EU on pressure equipment, which applies to sterilisable vessels operated above atmospheric pressure
- Directive 1999/92/EC on explosive atmospheres, relevant to solvent recovery, dust handling and gas fermentation feedstocks
- Directive 2009/41/EC on the contained use of genetically modified microorganisms, which governs the strain regardless of the product
- Directive 2000/54/EC on biological agents at work, including the classification of the production organism
- EudraLex Volume 4 Good Manufacturing Practice, Parts I and II, where the product is a medicine or an active substance
- Regulation (EC) No 852/2004 on the hygiene of foodstuffs and Regulation (EU) 2015/2283 on novel foods, where the product enters the food chain
- Regulation (EC) No 1831/2003 on feed additives, which covers the amino acids and enzymes that constitute much of this record's tonnage
- Regulation (EC) No 1907/2006 REACH, where the product is a chemical
- Directive 89/391/EEC on safety and health at work, including confined space entry and the asphyxiation hazard from carbon dioxide accumulation in and around large fermenters

### Standards

- Pharmacopoeial sterility test methods and the sterility assurance level convention, under which sterility is demonstrated to a probability rather than asserted absolutely
- Bacterial endotoxin testing for products from Gram-negative hosts, a requirement that follows from the choice of production organism
- Culture identity and purity verification at every stage of the seed train
- Master and working cell bank conventions, including characterisation, storage and the limit on passage number, which is how a strain stays the same organism across a product's commercial life
- Strain deposit in a recognised culture collection under the Budapest Treaty where patent protection is sought
- American Society of Mechanical Engineers Bioprocessing Equipment standards for hygienic design, surface finish and drainability
- ISO 14159 on hygiene requirements for machinery, and hygienic design guidance from the European Hygienic Engineering and Design Group
- ICH Q7 for active pharmaceutical ingredients and ICH Q8, Q9 and Q10 for pharmaceutical development, risk management and quality systems
- Process analytical technology and continuous manufacturing guidance, including how a batch may be defined for a process that does not naturally have one
- HACCP and FSSC 22000 certification where the product enters food or feed
- ISO 14040 and ISO 14044 life cycle assessment, required to substantiate any claim that a fermentation route is lower impact, since feedstock cultivation, sterilisation energy, aeration power and spent broth all count against it

### Related records

- `white.metabolic_engineering`
- `white.bioprocess_engineering`
- `white.industrial_enzymes`
- `red.pharmaceutical_biotechnology`
- `white.biobased_chemicals`
- `white.biofuels`
- `yellow.precision_fermentation`

### Cross-references

- [white.metabolic_engineering](metabolic_engineering.md)
- [white.bioprocess_engineering](bioprocess_engineering.md)
- [white.industrial_enzymes](industrial_enzymes.md)
- [red.pharmaceutical_biotechnology](../red/pharmaceutical_biotechnology.md)
- [white.biobased_chemicals](biobased_chemicals.md)
- [white.biofuels](biofuels.md)
- [yellow.precision_fermentation](../yellow/precision_fermentation.md)
