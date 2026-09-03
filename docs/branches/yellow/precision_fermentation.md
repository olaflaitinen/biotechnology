<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/yellow/precision_fermentation/.
  Edit the source and run `make docs`.
-->

[Yellow Biotechnology](index.md) / **Precision Fermentation**

## Precision Fermentation

`yellow.precision_fermentation`

Producing specific animal proteins and other defined food molecules by engineered microorganisms rather than by animals.

### What it is

Precision fermentation produces a defined molecule, usually a protein, by an engineered microorganism grown in a fermenter. The technique is not new. Recombinant human insulin has been made this way since 1982 and chymosin for cheesemaking since 1988, and the great majority of cheese produced in several countries has been made with fermentation-derived chymosin for decades without controversy or much public awareness. What the term names is a shift in target rather than in method. The shift matters commercially rather than technically. A pharmaceutical protein is required in grams per patient and competes on efficacy against a patented alternative, so a manufacturing cost of hundreds of euro per gram is unremarkable. A dairy protein is required in millions of tonnes and competes on price against an agricultural commodity produced by an industry with enormous scale and, in many countries, subsidy. The engineering problem is therefore not making the protein, which is solved, but making it at a cost per kilogram that a food ingredient can bear, which is the problem `white.bioprocess_engineering` describes in general and which bites hardest here. The products divide into three. Dairy proteins, chiefly beta-lactoglobulin and casein, are furthest advanced and have reached the market in several jurisdictions. Egg proteins including ovalbumin follow. And a wider set of molecules is produced the same way without attracting the same label: vitamins, flavour compounds, sweetener proteins, human milk oligosaccharides for infant formula, and the heme protein used to give plant-based meat its character. The last of these is the most widely eaten precision fermentation product that most consumers have never heard described as one. Three constraints govern. Cost per kilogram must approach that of an agricultural commodity, which requires titres and downstream efficiency that only some products have reached. Regulatory approval is required in full, because the product has no history of consumption even where the identical animal protein does, which is the position `yellow.food_fermentation` contrasts with. And functionality is not guaranteed by identity: a protein with the correct sequence may not behave in a food matrix as the animal protein does, because glycosylation, folding and the accompanying minor components all contribute to how a real ingredient performs.

### In plain language

This is making the proteins that are in milk or eggs without using an animal. A microbe is given the instructions for the protein, grown in a tank, and the protein is collected. The result is the same molecule, not an imitation, so it behaves in cooking the way the real thing does. It is also not new: the enzyme used to make most cheese has been produced this way since the 1980s, and so has the insulin that people with diabetes use. One thing is worth knowing plainly. Because the protein is genuinely the same, it causes the same allergies. Milk protein made without a cow will still affect someone allergic to milk.

### An analogy

It is printing a document rather than describing it. A plant-based substitute is a description, however good, and this is the same text on different paper. The limit of the comparison is worth stating: an identical copy inherits everything, so if the original was difficult for somebody to read, the copy is too. A milk protein made without a cow is still a milk protein to an immune system.

### Why it matters

Dairy and egg production occupy a great deal of land, water and feed, and producing the functional proteins directly removes the animal from that part of the supply. The proteins behave as the originals do, so a cheese or a mayonnaise can be made rather than approximated, which is the difference between substitution and replacement. Human milk oligosaccharides for infant formula and vitamin B12 for people eating no animal products are cases where fermentation supplies something that has no practical alternative source. And the technology is genuinely mature: most cheese in several countries has been made with a fermentation-derived enzyme for over thirty years. The costs deserve equal clarity. Cost per kilogram remains the binding problem for the bulk proteins, and the comparison is against a heavily scaled and often subsidised agricultural commodity. The feedstock is sugar, which is grown on farmland, so the land saving is real and smaller than the marketing suggests, and only a full life cycle assessment settles it. Regulatory approval is slow and expensive, and it applies in full to a molecule identical to one people have eaten for millennia, which is defensible as caution and is a genuine barrier to entry that favours incumbents. And the allergen position is unchanged, which is not a marketing inconvenience but a labelling requirement and a safety fact.

### Applications

- Chymosin for cheesemaking, produced by fermentation since 1988 and used in the great majority of cheese made in several countries, which is the largest and least controversial precision fermentation product in existence
- Vitamin B2 and vitamin B12 by fermentation, which for B12 is the only practical source for people eating no animal products
- Amino acids and vitamins for food and feed fortification, produced this way at very large scale and rarely described by this name
- Food enzymes across baking, dairy and starch processing, which belong technically to `white.industrial_enzymes` and are made by the same process as everything else in this record
- Heme protein produced by yeast, used to give plant-based meat its colour and flavour, which is the most widely eaten product in this record that consumers do not associate with it
- Human milk oligosaccharides for infant formula, supplying compounds that have no other practical source at scale
- Sweet-tasting proteins such as brazzein and thaumatin as sugar alternatives, where the plant source is scarce and geographically restricted
- Fermentation-derived flavour and fragrance compounds including vanillin, which reduce dependence on scarce plant material
- Beta-lactoglobulin and other whey proteins for dairy applications, approved and sold in several jurisdictions
- Caseins, which are harder than whey because they function in a food as an assembled micelle rather than as an isolated protein
- Ovalbumin and other egg proteins for baking and emulsification
- Collagen and gelatin produced without animals, for food and for the materials applications in `blue.marine_biomaterials`
- Lactoferrin and other minor milk proteins, where the animal source yields very little and the fermentation route competes on availability rather than only on price
- Fermentation-derived fats and oils, including cocoa butter and dairy fat equivalents, which are made by whole-cell metabolic engineering rather than by expressing a single protein and belong here only loosely

### Technologies

- Host selection between bacterial, yeast and filamentous fungal systems, decided by whether the protein must be secreted and whether it requires post-translational modification
- Gene design and codon optimisation for the chosen host
- Secretion signal and promoter engineering to raise secreted titre, which is usually a larger commercial lever than any change to the protein
- Strain development by classical and genomic methods, drawing on `white.metabolic_engineering`
- Fed-batch fermentation on sugar feedstock, on the terms `white.microbial_fermentation` sets out including the overflow metabolism constraint
- Food-grade host and medium selection, since a host with a history of safe use in food shortens the regulatory path considerably
- Scale-up to production volumes, where the cost target is set by an agricultural commodity rather than by a pharmaceutical
- Downstream recovery and purification, which for a food protein must reach a cost per kilogram that a pharmaceutical process never has to consider
- Removal of host cell protein, DNA and endotoxin to food-grade specifications, which are less stringent than pharmaceutical ones and are not absent
- Spray drying and formulation into an ingredient a food manufacturer can actually use
- Identity confirmation against the animal protein by mass spectrometry and sequencing, which is the basis of the substantial equivalence argument
- Glycosylation and folding characterisation, since sequence identity does not guarantee identical behaviour in a food
- Functional testing in the actual food matrix, covering gelation, foaming, emulsification and heat stability, because a protein that is chemically right and functionally wrong is not an ingredient
- Allergenicity assessment, which for an identical protein confirms rather than removes the allergen status

### Challenges

- Cost per kilogram against an agricultural commodity, where the comparison is with a heavily scaled and frequently subsidised industry, and where a pharmaceutical cost structure is two orders of magnitude too expensive
- Downstream processing cost, which for a food ingredient cannot carry the purification burden that `white.bioprocess_engineering` records as normal for a therapeutic protein
- Capital intensity of fermentation capacity at food volumes, and the shortage of suitable contract manufacturing capacity
- Functionality in a real food matrix, since gelation, foaming and emulsification depend on folding, glycosylation and accompanying minor components as well as on sequence
- Reproducing assembled structures such as the casein micelle, which is not a protein but an arrangement of several with calcium and phosphate
- Full novel food authorisation for a molecule identical to one eaten for millennia, which is defensible caution and a real barrier to entry that favours incumbents
- Divergent approval timelines and requirements between jurisdictions, so a product on sale in one market may be years from another
- Labelling and naming disputes, including whether a product may be called milk or cheese, which are decided by law rather than by composition
- Unchanged allergen status, since an identical protein provokes an identical response, which must be declared and which limits the market a product can address
- Sugar feedstock grown on farmland, so the land saving is real and smaller than commonly claimed, and demonstrable only by full life cycle assessment against a named dairy or egg benchmark
- Consumer acceptance of a genetically modified organism in the production chain, which chymosin achieved and which newer products cannot assume, since the objection is frequently to the process rather than to the molecule

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Production cost per kilogram | `C_kg` | euro per kilogram of purified protein | must approach commodity dairy and egg protein prices; pharmaceutical-grade production of the same protein is orders of magnitude higher | REPORTED |
| Secreted titre | `T_sec` | grams of target protein per litre of broth | single digits to tens of grams per litre in optimised hosts | REVIEWED |
| Downstream cost share | `f_dsp` | per cent of total production cost in recovery and purification | a large share, and the principal difference between food and pharmaceutical economics for the same molecule | REVIEWED |
| Product yield on substrate | `Y_ps` | grams of protein per gram of sugar consumed | the term that determines feedstock cost per kilogram of product | CONSENSUS |
| Sequence identity to the animal protein | `I_seq` | per cent of residues matching the reference sequence | 100 % is the claim and the expectation | CONSENSUS |
| Glycosylation profile | `P_glyc` | distribution of glycan structures on the expressed protein | differs from the animal protein in most microbial hosts | REVIEWED |
| Host cell protein and DNA residue | `c_hcp` | parts per million of total protein | food-grade limits, less stringent than pharmaceutical ones | CONSENSUS |
| Gelation temperature and strength | `T_gel` | degrees Celsius and kilopascals at stated concentration | must match the animal protein for the application to work | CONSENSUS |
| Foaming and emulsifying capacity | `C_foam` | per cent overrun or emulsion stability index | benchmarked against the animal-derived ingredient | CONSENSUS |
| Heat stability in the food matrix | `S_heat` | per cent of function retained after a stated thermal process | tested against the actual process the food undergoes | REVIEWED |
| Cradle-to-gate greenhouse gas intensity | `GWP` | kilograms of carbon dioxide equivalent per kilogram of protein | compared against a named dairy or egg benchmark, and favourable in most published assessments | REPORTED |
| Land use per kilogram of protein | `A_land` | square metres per kilogram | lower than dairy and egg production, and not zero | REPORTED |
| Allergenic equivalence | `A_eq` | qualitative, established by sequence and immunological testing | equivalent to the animal protein by design | CONSENSUS |

### History

- **1982** - Recombinant human insulin produced in bacteria is approved
- **1988** - Fermentation-produced chymosin is approved for cheesemaking
- **1994** - Recombinant bovine somatotropin is approved in the United States and rejected in Europe
- **1997** - European novel food authorisation is established
- **2005** - Fermentation-derived vitamins and amino acids dominate their markets
- **2019** - Yeast-produced heme protein enters wide use in plant-based meat
- **2020** - Precision fermentation dairy proteins reach the market
- **2021** - Human milk oligosaccharides produced by fermentation are authorised for infant formula
- **2023** - Cost projections for bulk precision fermentation proteins prove optimistic and funding contracts
- **2024** - Regulatory approvals accumulate across jurisdictions on divergent timelines

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | REGULATED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | FOOD, HEALTH, ENVIRONMENT |
| SDGs | 3, 9, 12 |

### Regulations

- Regulation (EU) 2015/2283 on novel foods, which requires authorisation for any food without significant consumption history in the Union and which applies in full to a molecule identical to one eaten for millennia
- EFSA guidance on the information required for a novel food application, covering identity, production process, compositional analysis, exposure and allergenicity
- United States Generally Recognised As Safe notification, and the equivalent routes in other jurisdictions, whose divergent timelines are recorded as a challenge in this record
- Directive 2009/41/EC on the contained use of genetically modified microorganisms, which governs production and not the purified product
- Regulation (EC) No 1829/2003 and Regulation (EC) No 1830/2003, whose labelling obligations attach where modified material is present in the product rather than only in the process
- Regulation (EC) No 1332/2008 on food enzymes, the route by which chymosin and the food enzymes in this record are authorised
- Regulation (EC) No 1333/2008 on food additives, relevant to colour and functional applications
- Regulation (EU) No 609/2013 on food for specific groups, under which the human milk oligosaccharides for infant formula are approved, in one of the most demanding food categories that exists
- Regulation (EU) No 1169/2011 on food information, whose allergen provisions apply unchanged to an identical protein, which is the point this record insists on
- Compositional and naming rules restricting the use of terms such as milk and cheese, which are decided by law rather than by molecular composition
- Regulation (EC) No 178/2002 and Regulation (EC) No 852/2004 on general food law and hygiene
- Regulation (EC) No 1881/2006 on contaminants, applied to the fermentation product and its feedstock

### Standards

- Analytical characterisation conventions for recombinant proteins, including mass spectrometric confirmation of sequence and determination of the glycosylation profile, which is where identity most often diverges
- Reference material comparison against the animal-derived protein, which is the only meaningful basis for a substantial equivalence argument
- Host cell protein and DNA residue limits to food-grade specifications, less stringent than pharmaceutical limits and not absent
- Functional testing protocols for gelation, foaming, emulsification and heat stability, benchmarked against the ingredient being replaced rather than against a specification
- Sensory evaluation by trained panel, since a functionally correct ingredient that tastes wrong is not a product
- Qualified presumption of safety assessment and inventories of microorganisms with a documented history of safe use in food, which shorten the regulatory path considerably when the host qualifies
- Culture collection deposit and strain characterisation, including the absence of antimicrobial resistance markers and of toxin production
- HACCP, FSSC 22000 and Good Manufacturing Practice for food ingredient production
- Kosher, halal and vegan certification schemes, which for this record are commercially significant because the animal-free claim is central to the proposition and the certifications are what make it credible
- ISO 14040 and ISO 14044 life cycle assessment against a named dairy or egg benchmark, with feedstock cultivation counted, which is what converts the land and emissions claims in `metrics.py` from assertion into evidence
- Conventions on declaring assumed production scale in a life cycle assessment, since most published figures for this record assume a scale not yet achieved

### Related records

- `yellow.food_fermentation`
- `yellow.alternative_proteins`
- `red.pharmaceutical_biotechnology`
- `white.microbial_fermentation`
- `white.bioprocess_engineering`
- `white.metabolic_engineering`

### Cross-references

- [yellow.food_fermentation](food_fermentation.md)
- [yellow.alternative_proteins](alternative_proteins.md)
- [red.pharmaceutical_biotechnology](../red/pharmaceutical_biotechnology.md)
- [white.microbial_fermentation](../white/microbial_fermentation.md)
- [white.bioprocess_engineering](../white/bioprocess_engineering.md)
- [white.metabolic_engineering](../white/metabolic_engineering.md)
