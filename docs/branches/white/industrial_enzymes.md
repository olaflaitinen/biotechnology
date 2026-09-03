<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/white/industrial_enzymes/.
  Edit the source and run `make docs`.
-->

[White Biotechnology](index.md) / **Industrial Enzymes**

## Industrial Enzymes

`white.industrial_enzymes`

Discovery, engineering and large-scale production of enzymes used as catalysts in detergents, food, textiles, paper, feed and chemistry.

### What it is

An industrial enzyme is a protein sold as process equipment. It accelerates one reaction by many orders of magnitude while working in water, near ambient temperature and near neutral pH, and it is selective enough that it usually yields one product rather than a mixture requiring separation. Those three properties are the entire commercial case: less energy into the vessel, less solvent to buy and dispose of, and fewer purification steps afterwards. Candidate enzymes come from screening culture collections, from metagenomic libraries built directly from environmental DNA without culturing anything, and increasingly from sequence databases and structure prediction. A candidate is then improved rather than accepted as found. Directed evolution applies rounds of mutagenesis and selection and requires no understanding of the mechanism; rational design uses structure to choose substitutions deliberately; the two are now usually combined, with computational design proposing variants and laboratory screening testing them. Production is by submerged fermentation of a small number of well-characterised host organisms, chiefly Bacillus, Aspergillus and Trichoderma species, at scales of tens to hundreds of cubic metres. The enzyme is usually secreted into the broth, which is why these hosts were chosen: recovery is a matter of removing the cells rather than breaking them open. The product is sold as a liquid concentrate, a granulate or an immobilised preparation on a solid support, and immobilisation is what makes the catalyst recoverable and reusable across many batches. The limits are the ones that follow from the enzyme being a protein. It denatures above its thermal tolerance, it is inhibited by many of the conditions an industrial process would prefer to use, it works in water when much of chemistry is done in organic solvents, and its operational lifetime rather than its initial activity is what determines cost per kilogram of product. Improving stability, not improving speed, is where most engineering effort in this field goes.

### In plain language

Enzymes are the tools living things use to take molecules apart and put them together, and they can be purified and sold in a drum. They are already in things you use daily: in washing powder, where they digest food and grass stains so the wash works at a low temperature; in bread, where they keep the loaf soft for longer; in cheese, where they set the curd; in fruit juice, where they stop it going cloudy; and in the stone washing of denim, which used to be done with actual pumice stones. What makes them valuable is that they do one job very precisely, in ordinary warm water, instead of needing heat, pressure and harsh chemicals.

### An analogy

An enzyme is a key and conventional chemistry is a hammer. The hammer will open the box, and it works on any box, but it destroys whatever was inside that you wanted to keep and leaves splinters to sweep up. The key opens exactly one lock, silently, with almost no effort. The trade is in the last part: a hammer needs no preparation, and every new lock needs a new key cut for it, which is what enzyme engineering is.

### Why it matters

The clearest example is in most homes. Detergent enzymes are why a domestic wash cleans properly at 30 degrees instead of 60, and a wash at 30 uses roughly a third of the electricity. Across the world's washing machines that is one of the largest emissions reductions attributable to any biotechnology, achieved quietly and largely unremarked. Phytase in animal feed releases phosphorus that pigs and poultry otherwise excrete, which both reduces the mined phosphate added to feed and reduces the phosphorus running off into rivers, where it causes algal blooms. Enzymes in pulp bleaching displaced a share of the chlorine chemistry that paper mills once relied on. In pharmaceutical manufacture, enzymatic routes have replaced multi-step syntheses and eliminated tonnes of solvent per tonne of product. The limits are real and are not marketing problems. An enzyme is a protein: it denatures, it is inhibited, it prefers water when much of chemistry is done in solvents, and its operating lifetime rather than its raw speed usually decides whether a process is affordable. Where those constraints bind, conventional chemistry remains the better answer, and this record says so rather than claiming the field for everything.

### Applications

- Laundry and dishwashing detergents, where proteases, lipases, amylases and cellulases together allow effective washing at 30 degrees rather than 60 and therefore about a third of the electricity
- Cellulases in detergent that remove the microfibrils responsible for greying and pilling, which is why enzyme-washed cotton keeps its colour
- Phytase in pig and poultry feed, which releases phosphorus bound in plant phytate so that less mined phosphate is added and less phosphorus is excreted into watercourses
- Xylanases and beta-glucanases in feed, which break down cereal fibre that monogastric animals cannot digest
- Alpha-amylase and glucoamylase in starch liquefaction and saccharification, the first stage of nearly every fermentation feedstock
- Glucose isomerase in the production of high fructose syrups, one of the earliest and largest immobilised enzyme processes
- Amylases, xylanases and lipases in baking, which control dough handling, loaf volume and staling rate
- Asparaginase in baking and frying, which reduces acrylamide formation, a process contaminant, without changing the recipe
- Chymosin produced by fermentation for cheesemaking, which replaced calf rennet and was among the first recombinant products in the food chain
- Lactase in dairy processing for lactose-free milk
- Amylases in textile desizing and cellulases in denim finishing, which replaced pumice stone abrasion
- Proteases in leather bating, replacing part of the sulphide chemistry
- Xylanase pre-bleaching of pulp, which reduces the chlorine-based bleaching chemistry required for the same brightness
- Cellulase and hemicellulase cocktails for lignocellulosic ethanol, where enzyme cost per litre remains a principal barrier
- Enzymatic steps in pharmaceutical manufacture, including transaminases, ketoreductases and nitrilases, which replace multi-step chemical routes and eliminate solvent
- Analytical and diagnostic enzymes, including glucose oxidase in blood glucose strips and the polymerases underlying `red.molecular_diagnostics`

### Technologies

- Screening of culture collections and extremophile isolates from hot springs, alkaline lakes, polar water and deep-sea vents
- Metagenomic library construction from environmental DNA, which reaches the large majority of organisms that cannot be cultured
- Sequence-based mining and structure prediction, which now supply candidates without any isolation step at all
- Directed evolution by iterative mutagenesis and screening, which requires no mechanistic understanding and is the reason the field advanced faster than protein theory did
- Rational and semi-rational design using structural information to target specific residues
- Ancestral sequence reconstruction, which frequently yields more thermostable variants than any modern homologue
- Consensus design, which substitutes the most common residue at each position across a family
- Computational design and machine learning models trained on variant activity data, linking this record to `gold.machine_learning_in_biology`
- Submerged fed-batch fermentation of secreting hosts at tens to hundreds of cubic metres
- Signal peptide and promoter engineering to raise secreted titre, which is usually a larger commercial lever than raising specific activity
- Downstream recovery by filtration, ultrafiltration and formulation into liquid, granulate or spray-dried product
- Immobilisation by adsorption, covalent attachment, entrapment or cross-linked enzyme aggregates, which makes the catalyst recoverable and reusable and is often what makes a process economic
- Granulation and coating for detergent products, which is also a worker safety measure against inhaled enzyme dust
- Enzyme cocktail formulation, where several activities are balanced against one substrate, as in cellulase blends for biomass

### Challenges

- Operational stability rather than initial activity, because cost per kilogram of product depends on total turnovers before the catalyst dies, and a fast enzyme with a short life is worth less than a slow durable one
- Tolerance of the conditions industry would prefer to use, meaning organic solvents, extremes of pH, high substrate loading and high temperature
- Inhibition by the product itself, which caps conversion and forces either product removal in situ or dilute operation
- Screening throughput, since a directed evolution campaign is limited by how many variants can be assayed rather than by how many can be made
- Enzyme cost per litre of product in low-margin applications, which is the principal unresolved barrier for lignocellulosic biofuel
- Cofactor dependence in oxidoreductases, where the cofactor costs more than the product unless it is regenerated in situ
- Respiratory sensitisation from inhaled enzyme dust, a genuine occupational hazard that caused serious harm in the detergent industry in the 1960s and is the reason granulation is standard rather than optional
- Regulatory and labelling divergence for enzymes in food between jurisdictions, including whether a processing aid must be declared

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Total turnover number | `TTN` | moles of product per mole of enzyme, dimensionless | 10^4 - 10^6 for a viable industrial biocatalyst | CONSENSUS |
| Biocatalyst cost contribution | `C_cat` | euro per kilogram of product | below 1 % of product value for bulk, higher for fine chemicals | REVIEWED |
| Space-time yield | `STY` | grams of product per litre of reactor per hour | 10 - 500 g/L/h depending on product value | CONSENSUS |
| Operational half-life | `t_half` | hours of retained activity under process conditions | 100 - 5000 h | CONSENSUS |
| Melting temperature | `T_m` | degrees Celsius | 50 - 105 degrees C depending on source and engineering | CONSENSUS |
| Turnover number | `k_cat` | per second | 1 - 10^5 s^-1 | CONSENSUS |
| Michaelis constant | `K_M` | millimolar | 0.01 - 100 mM | CONSENSUS |
| Specificity constant | `k_cat/K_M` | per molar per second | 10^3 - 10^8 M^-1 s^-1 | CONSENSUS |
| Specific activity | `A_sp` | units per milligram of protein | 1 - 10^4 U/mg | CONSENSUS |
| Secreted titre | `T_sec` | grams of enzyme per litre of fermentation broth | 1 - 100 g/L in optimised industrial hosts | REVIEWED |
| Environmental factor | `E_factor` | kilograms of waste per kilogram of product | under 5 for bulk chemistry, 25 - 100 for pharmaceuticals | CONSENSUS |
| Enantiomeric excess | `ee` | per cent | above 99 % required for a pharmaceutical intermediate | CONSENSUS |

### History

- **1833** - Payen and Persoz isolate diastase from malt
- **1897** - Buchner shows that cell-free yeast extract still ferments sugar
- **1913** - Michaelis and Menten publish the kinetic treatment of enzyme action
- **1913** - Rohm patents a laundry product containing pancreatic enzymes
- **1926** - Sumner crystallises urease and demonstrates that enzymes are proteins
- **1960** - Bacterial alkaline proteases are introduced into detergents
- **1969** - Occupational asthma among detergent factory workers halts the enzyme detergent boom
- **1973** - Immobilised glucose isomerase enters commercial high fructose syrup production
- **1988** - Fermentation-produced chymosin is approved for cheesemaking
- **1993** - Directed evolution of enzymes is demonstrated
- **2003** - Enzymatic bleaching and biopolishing become standard in pulp and textile processing
- **2010** - Computationally designed enzymes for reactions with no natural counterpart are reported
- **2018** - The Nobel Prize in Chemistry is awarded for directed evolution of enzymes and for phage display
- **2021** - Deep learning structure prediction becomes routinely available for enzyme engineering

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | CONTROLLED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | MATERIALS, FOOD, ENVIRONMENT |
| SDGs | 6, 9, 12, 13 |

### Regulations

- Directive 2004/37/EC and national occupational exposure frameworks as applied to enzyme dust, which is classified as a respiratory sensitiser and is the reason granulated rather than powdered product is standard
- Directive 2000/54/EC on biological agents at work, which covers handling of the production organism in the plant
- Regulation (EC) No 1332/2008 on food enzymes, which establishes the Union list and the authorisation procedure
- Regulation (EC) No 1829/2003, which governs the position where the enzyme is produced by a genetically modified microorganism, and under which a purified enzyme carrying no viable organism or recombinant DNA is treated differently from a modified organism itself
- United States Generally Recognised As Safe notification and food contact notification procedures for food-processing enzymes
- Regulation (EC) No 1831/2003 on additives for use in animal nutrition, under which phytase and the feed carbohydrases are authorised
- Regulation (EC) No 1907/2006 REACH, under which enzyme preparations are registered as substances, and Regulation (EC) No 1272/2008 CLP, under which they are classified and labelled
- Regulation (EC) No 648/2004 on detergents, which governs the largest single application by volume
- Directive 2009/41/EC on the contained use of genetically modified microorganisms, which regulates the production step rather than the product
- The Nagoya Protocol on access and benefit sharing, which applies directly to enzymes discovered by bioprospecting or from metagenomic sampling in another country

### Standards

- Association of Manufacturers and Formulators of Enzyme Products guidance on safe handling, encapsulation and airborne enzyme monitoring, which is the industry's own answer to the 1969 sensitisation episode
- Occupational exposure guidance values for airborne enzyme protein, expressed in nanograms per cubic metre rather than milligrams, which indicates how potent a sensitiser this class is
- Joint FAO/WHO Expert Committee on Food Additives specifications for enzyme preparations, which set the purity and contaminant limits
- Food Chemicals Codex monographs for food-grade enzyme preparations
- International Union of Biochemistry and Molecular Biology enzyme nomenclature and EC numbering, which is what makes two suppliers' products comparable at all
- Supplier-declared assay conditions for the activity unit, since a unit is meaningful only alongside the pH, temperature and substrate at which it was measured, as noted in `metrics.py`
- ISO 9001 and, for food and feed grades, HACCP and FSSC 22000 certification of the manufacturing site
- Good Manufacturing Practice for enzymes intended for pharmaceutical synthesis
- ISO 14040 and ISO 14044 life cycle assessment methodology, which is how the wash temperature and solvent displacement claims in this record are substantiated rather than asserted
- Green chemistry metric reporting conventions for E factor and atom economy

### Related records

- `white.biocatalysis`
- `white.microbial_fermentation`
- `white.bioprocess_engineering`
- `white.metabolic_engineering`
- `white.biofuels`
- `yellow.food_safety_biotechnology`
- `purple.access_benefit_sharing`

### Cross-references

- [white.biocatalysis](biocatalysis.md)
- [white.microbial_fermentation](microbial_fermentation.md)
- [white.bioprocess_engineering](bioprocess_engineering.md)
- [white.metabolic_engineering](metabolic_engineering.md)
- [white.biofuels](biofuels.md)
- [yellow.food_safety_biotechnology](../yellow/food_safety_biotechnology.md)
- `purple.access_benefit_sharing` (branch not written yet)
