<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/white/bioprocess_engineering/.
  Edit the source and run `make docs`.
-->

[White Biotechnology](index.md) / **Bioprocess Engineering**

## Bioprocess Engineering

`white.bioprocess_engineering`

Designing, scaling and operating the equipment train that turns a laboratory biological process into reproducible manufacture, including everything downstream of the vessel.

### What it is

Bioprocess engineering designs and operates the physical train that carries a biological process from a laboratory result to reproducible manufacture: the vessel and its mixing, aeration and heat removal, the instrumentation and control, and every unit operation between the harvest and the packaged product. It is distinguished from microbial fermentation, which is the cultivation itself. That record describes what the culture demands; this one describes what the plant can supply and what happens to the broth afterwards. Scale-up is the discipline's characteristic problem and it has no general solution. Under geometric similarity, constant power per unit volume, constant impeller tip speed, constant oxygen transfer coefficient and constant mixing time cannot be maintained together: fixing one forces the others to move, sometimes by an order of magnitude. A large vessel is therefore not a small vessel writ large. It mixes more slowly, so a culture experiences gradients in dissolved oxygen, substrate and pH as it circulates, and cells spend part of every circulation in conditions the laboratory never presented. Choosing which criterion to preserve is an engineering judgement about which insult the organism tolerates least. Downstream processing is where most of the cost lies for a biological product, commonly the majority of manufacturing cost for a therapeutic protein. The train separates cells from broth by centrifugation or filtration, releases intracellular product by homogenisation if it was not secreted, captures the product on a chromatographic resin, polishes away the remaining impurities, exchanges the buffer, concentrates, and formulates. Each step consumes buffer in volumes far exceeding the product, and buffer preparation and storage frequently size the facility. One piece of arithmetic governs the design of that train. Step yields multiply. Ten steps at ninety per cent each deliver thirty-five per cent overall, so removing a step is usually worth more than improving one. This is why the field pursues fewer operations rather than better ones, and why a modest gain in titre upstream can be worth less than eliminating a single purification step downstream.

### In plain language

Getting something to work in a laboratory flask and getting it to work in a tank the size of a room are different problems. Big tanks mix slowly, so different parts of them are not the same, and cells travelling around one experience changing conditions rather than steady ones. Then there is the part people forget: once the tank has finished, you still have a soup containing the thing you want and thousands of things you do not, and separating them is where most of the cost and most of the equipment actually is. Every separation step also loses a little of the product, and those losses multiply, so the shortest sequence usually beats the cleverest one.

### An analogy

It is the difference between cooking for four and cooking for four thousand. The recipe does not scale. A domestic pan heats evenly and a vat does not, so the edges catch while the middle is cold, and stirring a vat takes long enough that the two are never quite the same thing at the same moment. And the canteen's real work is not the cooking at all. It is everything after: portioning, straining, chilling, packing, each step losing a little and each one needing its own machine.

### Why it matters

This discipline decides whether a biological discovery becomes something people can actually obtain. A therapeutic protein that works in a laboratory is of no use to a patient until it can be made reproducibly, in quantity, to a purity specification, at a price a health system will pay, and the majority of that cost sits in purification rather than in the fermenter. The field also carries a lesson it learned expensively. Between the early 1990s and the 2010s, upstream titres for therapeutic proteins rose by roughly two orders of magnitude while downstream capacity did not follow, so the industry created a bottleneck by succeeding at the wrong end of its own process. Facilities built for the old ratio could not handle what the new cell lines produced. And because these plants are single points of failure for medicines with no alternative supplier, an engineering failure is a public health event: contamination of one manufacturing site in 2009 caused international shortages of two enzyme replacement therapies that patients had no way to substitute. The counterweight to all of this is that improvements here are permanent and cumulative. A purification step removed is removed for the life of the product.

### Applications

- Stirred tank bioreactor design, including impeller selection, baffling and sparger geometry for the oxygen demand the culture will make
- Airlift, bubble column and wave-mixed reactors for shear-sensitive cultures where a stirred impeller does damage
- Heat removal design, since a large aerobic fermentation is a substantial heat source and cooling area does not grow with volume
- Photobioreactor design for phototrophic cultures, where light penetration replaces oxygen transfer as the limiting transport problem
- Harvest by disc-stack centrifugation, depth filtration or tangential flow filtration, chosen by particle size, fragility and viscosity
- Cell disruption by high pressure homogenisation or bead milling, required whenever the product was not secreted and the reason secretion hosts are preferred
- Inclusion body recovery, solubilisation and refolding, a route with characteristically poor and hard-won yields
- Capture chromatography, including affinity capture, which in a single step removes the great majority of impurities and dominates therapeutic protein processing
- Polishing chromatography by ion exchange, hydrophobic interaction or mixed mode, to remove aggregates and product-related variants
- Continuous and simulated moving bed chromatography, which uses resin far more efficiently than a batch column
- Ultrafiltration and diafiltration for concentration and buffer exchange, which consume most of the buffer volume in a facility
- Buffer preparation, hold and in-line dilution, which frequently sizes the plant more than the bioreactor does
- Viral clearance by low pH inactivation and nanofiltration, with the clearance capacity of each step validated independently
- Formulation, sterile filtration and aseptic fill-finish
- Lyophilisation cycle design for products that are not stable in solution
- Single-use assembly design, including the extractables and leachables assessment that plastic contact requires
- Spent broth, biomass and process water treatment, which is a large waste stream and a permit condition rather than an afterthought

### Technologies

- Scale-up on constant power per unit volume, the most common default, which preserves turbulence intensity and lets tip speed rise
- Scale-up on constant impeller tip speed, chosen for shear-sensitive cultures at the cost of mixing and transfer
- Scale-up on constant oxygen transfer coefficient, chosen where the process is transfer-limited rather than shear-limited
- Computational fluid dynamics and scale-down models that reproduce the gradients of a large vessel in a small one, so that an organism can be tested against the insult before the plant is built
- Dimensional analysis and the use of Reynolds, Froude and power numbers to reason about regimes rather than about specific vessels
- Process analytical technology, including in-line spectroscopy for concentration and quality attributes
- Off-gas analysis and soft sensors that infer biomass and metabolic state from what can actually be measured
- Digital twins and mechanistic process models used for control and for predicting the consequence of a deviation
- Multivariate data analysis across batches to detect drift before it becomes a failure
- Single-use bioreactors, bags, tubing and connectors, which remove cleaning and sterilisation between campaigns at the cost of a plastic waste stream
- Modular and ballroom facility design, which allows several products in one building without dedicated suites
- Continuous and intensified processing, including perfusion culture and connected downstream trains that remove hold tanks
- Process intensification by higher cell density and smaller vessels, which reduces facility footprint rather than improving the biology
- Quality by design, with critical quality attributes linked to critical process parameters and a defined design space
- Process validation across its three stages, from design through qualification to continued verification in routine production
- Cleaning validation and campaign changeover control, which is where cross-contamination between products is actually prevented

### Challenges

- The mutual incompatibility of scale-up criteria, since power per volume, tip speed, oxygen transfer and mixing time cannot be held constant together, so every scale-up sacrifices something and the engineer must know which insult the organism tolerates least
- Multiplicative yield loss across a purification train, where ten steps at ninety per cent deliver thirty-five per cent overall, which makes removing a step worth more than improving one
- Gradients in dissolved oxygen, substrate and pH within a large vessel, so that cells cycle through conditions the laboratory never presented and respond metabolically to the transit rather than to the average
- Shear damage and interfacial damage at the bubble surface, which limits how hard a fragile culture may be mixed and aerated
- Downstream cost dominance, since purification typically exceeds cultivation in the cost of goods for a biological product
- Buffer volume and storage, which routinely sizes a facility more than the bioreactor does and is the least discussed constraint in the field
- Chromatography resin cost, capacity and lifetime, which for affinity capture is a major consumable rather than a fixed asset
- The imbalance created by improving upstream titre without matching downstream capacity, which the industry demonstrated at scale and which left existing facilities unable to process what new cell lines produced
- Comparability after any process change, since for a biological product the process defines the molecule and a change must be shown not to have altered it
- Contamination and its consequences in a single-source facility, where an engineering failure becomes a shortage of a medicine that has no substitute
- The waste and supply chain consequences of single-use plastics, which trade cleaning validation and water use for a disposal stream and a dependence on specific suppliers

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Power input per unit volume | `P/V` | watts per cubic metre | 500 - 5000 W/m3 for microbial culture, 10 - 100 W/m3 for animal cell culture | CONSENSUS |
| Impeller tip speed | `v_tip` | metres per second | 2 - 8 m/s for microbial, below 2 m/s for shear-sensitive cultures | CONSENSUS |
| Volumetric oxygen transfer coefficient | `kLa` | per hour | 50 - 500 h^-1, and harder to sustain as volume rises | CONSENSUS |
| Mixing time | `t_m` | seconds to reach a stated degree of homogeneity | 5 - 10 s at laboratory scale, 30 - 200 s in large vessels | CONSENSUS |
| Impeller Reynolds number | `Re_i` | dimensionless | above 10^4 for fully turbulent operation | CONSENSUS |
| Overall process yield | `Y_overall` | per cent of product formed that reaches the final container | 30 - 70 % for a multi-step biological purification | CONSENSUS |
| Step yield | `Y_step` | per cent recovered across one unit operation | 85 - 98 % for a well-developed step | CONSENSUS |
| Dynamic binding capacity | `DBC` | grams of product per litre of resin at a stated residence time | 30 - 70 g/L for modern affinity resins | REVIEWED |
| Resin lifetime | `N_cycles` | purification cycles before replacement | 50 - 300 cycles | REVIEWED |
| Buffer consumption ratio | `B_ratio` | litres of buffer per gram of purified product | hundreds to thousands of litres per gram | REVIEWED |
| Process mass intensity | `PMI` | kilograms of total input per kilogram of product | in the thousands for a therapeutic protein, dominated by water | REVIEWED |
| Facility utilisation | `U_fac` | per cent of available operating time in productive use | 40 - 80 % | REVIEWED |
| Viral clearance factor | `LRV` | log10 reduction value, summed across orthogonal steps | a total above 12 log10 expected for a mammalian cell product | CONSENSUS |

### History

- **1943** - Deep-tank penicillin manufacture requires an engineering discipline that does not yet exist
- **1959** - Centrifuge scale-up is placed on a rational basis by the sigma factor
- **1960** - Oxygen transfer correlations and dimensional analysis become standard practice in reactor design
- **1968** - Affinity chromatography is introduced
- **1986** - Affinity capture becomes the standard first purification step for therapeutic antibodies
- **2004** - Regulators adopt process analytical technology and quality by design
- **2005** - Upstream titres outgrow downstream capacity and create the downstream bottleneck
- **2005** - Single-use bioreactors and disposable flow paths enter widespread use
- **2009** - Viral contamination of a single manufacturing plant causes international shortages of two enzyme replacement therapies
- **2015** - Continuous and intensified bioprocessing move from proposal to practice
- **2021** - Rapid capacity expansion for pandemic vaccine manufacture tests every assumption in this record at once

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | HEALTH, MATERIALS, FOOD |
| SDGs | 3, 6, 9, 12 |

### Regulations

- EudraLex Volume 4 Good Manufacturing Practice, Parts I and II, and Annex 1 on the manufacture of sterile medicinal products, which is the most demanding single document most of these facilities work to
- United States 21 CFR Parts 210 and 211, and Part 600 for biological products
- Regulation (EC) No 1234/2008 on variations, which is the instrument that makes a process improvement expensive to deploy once approved
- 21 CFR Part 11 and Annex 11 on electronic records and signatures, which govern the process control and data historian systems these plants depend on
- Directive 2014/68/EU on pressure equipment, for sterilisable vessels operated above atmospheric pressure
- Directive 2006/42/EC on machinery, and Directive 1999/92/EC on explosive atmospheres where solvents or dusts are handled
- Directive 2010/75/EU on industrial emissions, and national discharge consents for spent broth and process water
- Directive 2009/41/EC on the contained use of genetically modified microorganisms, and Directive 2000/54/EC on biological agents at work
- Regulation (EU) 2017/745 and food contact material rules as applicable to single-use components, whose extractables and leachables must be assessed because the plastic touches the product

### Standards

- ICH Q5E on comparability of biotechnological products subject to changes in their manufacturing process, which is the document behind this record's central governance idea
- ICH Q6B on specifications for biotechnological products, and ICH Q5A on viral safety evaluation, under which the clearance factors in `metrics.py` are established
- ICH Q8 on pharmaceutical development and the design space concept
- ICH Q9 on quality risk management and ICH Q10 on the pharmaceutical quality system
- ICH Q11 on development and manufacture of drug substances
- ICH Q13 on continuous manufacturing, which addresses how a batch may be defined for a process that has no natural batch boundary
- ICH Q14 on analytical procedure development, since a process can only be controlled as well as it can be measured
- Process validation guidance in three stages, from process design through performance qualification to continued verification in routine production
- Cleaning validation and campaign changeover expectations, which is where cross-contamination between products is actually prevented
- American Society of Mechanical Engineers Bioprocessing Equipment standards for hygienic design, surface finish, drainability and weld quality
- ISO 14644 cleanroom classification, and ISO 13408 on aseptic processing
- Bio-Process Systems Alliance and pharmacopoeial guidance on extractables and leachables from single-use systems
- ISO 14040 and ISO 14044 life cycle assessment, which is how the trade between single-use plastic waste and the water and energy of cleaning is actually settled rather than asserted

### Related records

- `white.microbial_fermentation`
- `white.metabolic_engineering`
- `red.pharmaceutical_biotechnology`
- `white.biocatalysis`
- `white.industrial_enzymes`
- `grey.wastewater_treatment`
- `yellow.precision_fermentation`

### Cross-references

- [white.microbial_fermentation](microbial_fermentation.md)
- [white.metabolic_engineering](metabolic_engineering.md)
- [red.pharmaceutical_biotechnology](../red/pharmaceutical_biotechnology.md)
- [white.biocatalysis](biocatalysis.md)
- [white.industrial_enzymes](industrial_enzymes.md)
- [grey.wastewater_treatment](../grey/wastewater_treatment.md)
- [yellow.precision_fermentation](../yellow/precision_fermentation.md)
