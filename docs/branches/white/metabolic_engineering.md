<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/white/metabolic_engineering/.
  Edit the source and run `make docs`.
-->

[White Biotechnology](index.md) / **Metabolic Engineering**

## Metabolic Engineering

`white.metabolic_engineering`

Rewiring the metabolism of a living cell so that it converts a cheap feedstock into a chosen product at commercially useful yield.

### What it is

Metabolic engineering modifies the metabolic network of a living organism so that carbon and energy flow towards a chosen product instead of towards biomass and the cell's own priorities. It differs from biocatalysis in the unit of work: biocatalysis performs one or a few steps outside a cell with purified enzymes, whereas metabolic engineering installs a whole pathway inside an organism that then feeds itself, regenerates its own cofactors, and repairs its own catalysts. That is a large advantage and it is bought at a price, because the organism is also growing, mutating and spending carbon on staying alive. The governing insight is that pathway output is not usually set by a single rate-limiting step. Metabolic control analysis established that control is distributed, and that the flux control coefficients of the enzymes in a pathway sum to one. Removing what appears to be the bottleneck therefore redistributes control rather than eliminating it, and a great deal of early disappointment in this field followed from expecting otherwise. Useful gains come from balancing expression across the pathway, from relieving cofactor and precursor competition, and from deleting the branches that divert carbon elsewhere. Practice is organised as a design, build, test and learn cycle. Design uses genome-scale stoichiometric models and flux balance analysis to predict which deletions and insertions move flux towards the product. Build assembles the pathway and adjusts expression through promoter, ribosome binding site and copy number choices. Test measures titre, rate and yield, and increasingly measures internal flux directly using labelled carbon. Learn feeds the result back into the model. The build and test steps are now heavily automated, which has moved the bottleneck of the whole discipline to measurement and to design quality rather than to construction. Two limits are absolute and one is practical. Stoichiometry sets a maximum yield from a given feedstock that no amount of engineering can exceed, and the redox and energy balance of the pathway sets another. The practical limit is evolutionary: a strain engineered to divert carbon away from growth is at a competitive disadvantage against any mutant that stops doing so, and over the many generations of a production fermentation, that mutant will be selected for. Genetic stability is therefore an engineering requirement rather than an assumption.

### In plain language

Every living cell is a chemical factory that runs itself. It takes in sugar and turns it into the hundreds of things it needs in order to grow. Metabolic engineering means rearranging that factory so that it also, or instead, makes something we want: a fuel, a plastic ingredient, a vitamin, a flavour, a medicine. The work is less like inventing a new machine and more like rerouting a road network so that traffic ends up somewhere else. And the awkward part is that the cell has its own priorities. It wants to grow, and anything we divert away from growth is something it is quietly under pressure to stop doing.

### An analogy

It is traffic engineering for a city, not a new engine for a car. When a city is congested, the instinct is to find the worst junction and widen it. It rarely works, because the queue simply forms at the next junction instead; the congestion was a property of the whole network rather than of one place in it. Metabolic engineering works the same way. Progress comes from rebalancing the whole route, closing the side roads that lead nowhere useful, and accepting that the residents still need to get to work.

### Why it matters

This is how a large share of the world's amino acids, vitamins and organic acids are already made. Engineered bacteria produce lysine for animal feed at millions of tonnes a year, which reduces the protein crop that livestock would otherwise need. Engineered routes supply 1,3-propanediol and 1,4-butanediol for polymers, the second by a pathway that does not exist in any organism and had to be assembled from parts. The field also produced one of biotechnology's most instructive stories. A yeast strain engineered to make the precursor of the antimalarial artemisinin was a genuine scientific triumph, delivered on its technical promise, and then failed commercially against farmers growing sweet wormwood more cheaply. The honest lesson is that a working pathway is not the same as a viable product, and that agricultural supply chains are harder to displace than they look. The constraints are equally honest. Stoichiometry caps yield from a given sugar and no engineering can pass it. Fermentation feedstock competes with food and land. And an engineered strain is under constant selective pressure to revert to simply growing, which means stability over hundreds of generations is a design requirement rather than a detail.

### Applications

- Glutamate and lysine production by Corynebacterium glutamicum, which has run at industrial scale since the late 1950s and now supplies millions of tonnes of feed amino acid a year
- Threonine, tryptophan and methionine fermentation, which reduce the protein crop that livestock diets would otherwise require
- Vitamin B2, B12 and vitamin C intermediate production, which displaced multi-step chemical syntheses
- Citric, lactic, succinic and itaconic acid production from sugar
- 1,3-propanediol for polymer manufacture, produced by an engineered Escherichia coli from glucose in place of a petrochemical route
- 1,4-butanediol by a pathway assembled from parts and present in no natural organism, which is the clearest demonstration that metabolism can be designed rather than only optimised
- Lactic acid for polylactic acid, linking this record directly to `white.biopolymers`
- Artemisinic acid in engineered yeast as a precursor to the antimalarial artemisinin, a technical success and a commercial disappointment recorded honestly in `history.py`
- Precursors for opioid, steroid and terpenoid drug substances, shortening routes that begin from a plant extract
- Isoprenoid and polyketide scaffolds for medicinal chemistry
- Fermentation-derived vanillin, nootkatone, valencene and steviol glycosides, which reduce dependence on scarce or seasonal plant sources
- Human milk oligosaccharides for infant formula, produced by engineered bacteria rather than isolated from milk
- Heme protein for plant-based meat analogues, which sits at the boundary with `yellow.alternative_proteins`
- Farnesene, isobutanol and fatty acid derived fuels and lubricant precursors, viable where the product commands a specialty price and difficult where it competes with bulk fuel
- Gas fermentation of carbon monoxide and carbon dioxide by acetogens, which converts industrial off-gas into ethanol and acetone
- Methanol and formate as one-carbon feedstocks for organisms engineered to grow on them, which decouples production from agricultural land

### Technologies

- Genome-scale metabolic models, which represent every known reaction in an organism as a stoichiometric matrix
- Flux balance analysis and its variants, which predict the flux distribution that maximises an objective subject to stoichiometry and uptake constraints
- Metabolic control analysis, which quantifies how much control each enzyme actually exerts and is the formal answer to the rate-limiting step assumption
- Elementary mode and pathway enumeration for finding routes that do not exist in any single organism
- Retrobiosynthesis software that proposes enzymatic routes to a target compound, the biological counterpart of chemical retrosynthesis
- Multiplexed genome editing and recombineering, which introduce many changes in one round
- Promoter, ribosome binding site and copy number libraries for tuning expression across a pathway rather than maximising any single enzyme
- Pathway refactoring, in which native regulation is stripped out and replaced with parts that behave predictably
- Enzyme scaffolding and compartmentalisation, which hold sequential enzymes close together or confine a toxic intermediate
- Carbon-13 metabolic flux analysis, which measures internal fluxes from labelling patterns rather than inferring them, and is the only direct measurement of what the cell is actually doing
- Biosensors and transcription factor based reporters that couple product concentration to a fluorescent or growth signal, converting a slow assay into a sortable one
- Growth-coupled selection, in which the strain is designed so that making the product is necessary for growth, which turns evolution from an adversary into a collaborator
- Adaptive laboratory evolution for tolerance to the product, the solvent or the feedstock
- Automated design, build, test and learn foundries operating at hundreds of strains per cycle
- Machine learning on strain performance data to propose the next round, linking to `gold.machine_learning_in_biology`

### Challenges

- Stoichiometric yield ceilings, since carbon, redox and energy balances set a maximum product per unit of feedstock that no amount of engineering can exceed, and the useful question is what fraction of it a strain achieves
- Redox and energy imbalance in a designed pathway, where a route that works on paper consumes cofactors the cell cannot supply at that rate
- Genetic instability under production conditions, because a strain that diverts carbon from growth is outcompeted by any mutant that stops doing so, and a production fermentation lasts many generations
- Product toxicity, which caps titre for alcohols, acids and solvents long before the pathway runs out of capacity
- Native regulation that resists the change, since the cell evolved feedback control specifically to prevent overproduction of its own metabolites
- Competing branch pathways that divert intermediates, where deleting them often impairs growth because they were there for a reason
- Measurement rather than construction, since building a strain is now cheap and automated while determining what it does internally is slow, which makes the test step the rate-limiting one for the discipline itself
- The gap between a shake flask and a production fermenter, where oxygen transfer, mixing and gradients change the answer, as recorded in `white.bioprocess_engineering`
- Feedstock cost and its competition with food and land use, which is frequently the difference between a working strain and a viable business

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Product titre | `C_p` | grams of product per litre of broth | 1 - 200 g/L, with roughly 50 g/L a common commercial threshold for a bulk product | CONSENSUS |
| Volumetric productivity | `Q_p` | grams of product per litre per hour | 0.5 - 5 g/L/h | CONSENSUS |
| Product yield on substrate | `Y_ps` | grams of product per gram of substrate, or Cmol/Cmol | 0.1 - 0.5 g/g depending on the product | CONSENSUS |
| Fraction of theoretical maximum yield | `Y_frac` | per cent of the stoichiometric maximum | 40 - 90 %, with above 90 % rare and usually growth-coupled | CONSENSUS |
| Carbon balance closure | `C_bal` | per cent of input carbon accounted for in products | 95 - 105 % for a trustworthy dataset | CONSENSUS |
| Genetic stability over generations | `G_stab` | generations of retained productivity | 60 - 100 generations required for a large-scale process | REVIEWED |
| Specific productivity | `q_p` | grams of product per gram of dry cell weight per hour | 0.01 - 0.5 g/gDCW/h | CONSENSUS |
| Specific growth rate | `mu` | per hour | 0.05 - 0.7 h^-1 depending on organism and phase | CONSENSUS |
| Flux control coefficient | `C_J_i` | dimensionless, and the coefficients over a pathway sum to 1 | rarely above 0.3 for any single enzyme | CONSENSUS |
| Intracellular flux distribution | `v` | millimoles per gram dry cell weight per hour | reported as a map rather than a single number | REVIEWED |
| Oxygen uptake rate | `OUR` | millimoles of oxygen per litre per hour | 50 - 250 mmol/L/h, and often the true ceiling at scale | CONSENSUS |

### History

- **1957** - Glutamate fermentation by Corynebacterium glutamicum is commercialised
- **1961** - Jacob and Monod describe operon regulation and feedback inhibition
- **1973** - Metabolic control analysis establishes that flux control is distributed
- **1991** - Metabolic engineering is named and defined as a discipline
- **1994** - Flux balance analysis is applied to predict metabolic behaviour from stoichiometry alone
- **1999** - The first genome-scale metabolic reconstruction is published
- **2006** - Engineered Escherichia coli enters commercial production of 1,3-propanediol from glucose
- **2006** - Engineered yeast is shown to produce artemisinic acid, the precursor to the antimalarial artemisinin
- **2013** - Commercial production begins for 1,4-butanediol by a pathway that exists in no natural organism
- **2013** - Semi-synthetic artemisinin reaches the market and then fails to displace the agricultural supply
- **2016** - Growth-coupled design and adaptive laboratory evolution become standard industrial practice
- **2018** - Automated design, build, test and learn foundries operate at hundreds of strains per cycle
- **2022** - Gas fermentation of industrial off-gas to ethanol and acetone reaches commercial operation

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | CONTROLLED |
| Scale | INDUSTRIAL |
| Regulatory status | VARIES |
| Domains | MATERIALS, ENERGY, FOOD |
| SDGs | 2, 7, 9, 12 |

### Regulations

- Directive 2009/41/EC on the contained use of genetically modified microorganisms, which is the single instrument that governs this field regardless of what is being produced
- Directive 2000/54/EC on biological agents at work
- National contained use notification and institutional biosafety committee requirements, which determine the containment class of a given strain
- Regulation (EU) 2015/2283 on novel foods, under which a fermentation-derived food ingredient with no significant consumption history requires authorisation
- Regulation (EC) No 1334/2008 on flavourings, which decides whether a fermentation-derived flavour compound may be labelled natural, a legal distinction rather than a chemical one
- Regulation (EC) No 1829/2003, relevant where the product carries material from the modified organism rather than being purified away from it
- Regulation (EC) No 1831/2003 on feed additives, which covers the amino acids that are this field's largest tonnage
- Regulation (EC) No 1907/2006 REACH and Regulation (EC) No 1272/2008 CLP
- Directive 2018/2001 on renewable energy, including its sustainability and feedstock criteria, which govern whether a biofuel counts towards a target
- EudraLex Volume 4 Good Manufacturing Practice, Part II, where the strain produces a drug substance or its precursor
- The Convention on Biological Diversity and the Nagoya Protocol, which apply to the enzymes and pathways sourced from organisms collected in another country, including where only sequence information was used

### Standards

- Minimum Information Required in the Annotation of Models, the community standard for reporting a metabolic model so that another group can rerun it
- Systems Biology Markup Language for exchanging metabolic models between tools
- Community conventions on reporting titre, rate and yield together with the cultivation conditions, without which the trio is not comparable between laboratories
- Reporting of carbon balance closure as a data quality condition, which is the fastest available check that a published result is internally consistent
- Synthetic Biology Open Language and standard part registries for describing genetic constructs unambiguously
- Strain deposit in a recognised culture collection under the Budapest Treaty where patent protection is sought
- ISO 9001, and HACCP and FSSC 22000 where the product enters food or feed
- Good Manufacturing Practice for pharmaceutical intermediates
- ISO 14040 and ISO 14044 life cycle assessment, required before a fermentation route may be called lower impact than the petrochemical one it replaces, since feedstock cultivation carries its own burden
- Greenhouse gas accounting conventions for biobased products, including how biogenic carbon is treated
- Institutional and industry codes on responsible engineering of microorganisms, including screening of synthesised DNA orders, which connects this record to `dark.biosecurity`

### Related records

- `white.biocatalysis`
- `white.bioprocess_engineering`
- `white.microbial_fermentation`
- `white.biobased_chemicals`
- `white.biofuels`
- `gold.machine_learning_in_biology`
- `yellow.precision_fermentation`

### Cross-references

- [white.biocatalysis](biocatalysis.md)
- [white.bioprocess_engineering](bioprocess_engineering.md)
- [white.microbial_fermentation](microbial_fermentation.md)
- [white.biobased_chemicals](biobased_chemicals.md)
- [white.biofuels](biofuels.md)
- `gold.machine_learning_in_biology` (branch not written yet)
- [yellow.precision_fermentation](../yellow/precision_fermentation.md)
