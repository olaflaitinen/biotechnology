<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/white/biobased_chemicals/.
  Edit the source and run `make docs`.
-->

[White Biotechnology](index.md) / **Biobased Chemicals**

## Biobased Chemicals

`white.biobased_chemicals`

Producing bulk and speciality chemicals from biological feedstocks in place of petroleum, by fermentation and catalytic upgrading.

### What it is

Biobased chemicals are the molecules of the chemical industry made from sugars, oils, residues and gases rather than from petroleum. The field's structural advantage follows from a single property of its feedstock: biomass is highly oxygenated, with roughly one oxygen per carbon in glucose, whereas petroleum has essentially none. Producing an oxygen-containing molecule such as a diacid, a diol or a hydroxy acid therefore requires several selective oxidation steps from petroleum and very few from sugar. Producing a pure hydrocarbon requires the reverse, and stripping oxygen from sugar wastes carbon as carbon dioxide. Which biobased chemicals have succeeded is largely predicted by this asymmetry. Two market strategies exist and they fail differently. A drop-in product is chemically identical to its petrochemical equivalent, so it needs no requalification and can enter an existing supply chain immediately, but it competes purely on price against an incumbent with a century of optimisation and no performance premium to offer. A novel molecule offers properties the petrochemical range cannot match and must create its own market, qualify with every downstream user and wait years for adoption. The successes in this record are mostly the second kind, or the first kind where the oxygen asymmetry gave a genuine cost advantage rather than parity. Much of the field is organised around platform chemicals: a small set of building blocks from which many products can be derived, so that investment in one fermentation supports a family of downstream molecules. Published lists of priority platforms have shaped research funding for two decades. They have also proved a poor predictor of commercial outcome, because a molecule can be an excellent chemical platform and a poor business if nobody has built the downstream capacity to consume it. What decides in practice is rarely the fermentation. It is feedstock cost against oil price, the capital intensity of a plant that must be built before any revenue exists, the separation cost of recovering a dilute product from an aqueous broth, and whether a customer will pay anything at all for the biobased attribute. The last of these is a market question rather than a technical one, and it has ended more projects than any titre.

### In plain language

Almost everything manufactured passes through the chemical industry: plastics, paints, solvents, detergents, fibres, adhesives, coatings. Nearly all of it currently starts from oil. Biobased chemicals make the same substances from plants, sugar or waste instead. This works better than making fuel from plants, for a reason that is easy to state: sugar already contains a lot of oxygen, and many useful chemicals need oxygen in them, whereas fuels need it removed. So biology starts closer to the chemical than to the fuel. Chemicals are also worth far more per tonne than fuel is, so a smaller amount of farmland goes much further.

### An analogy

Petroleum is a pile of identical plain bricks and sugar is a pile of parts that already have fittings attached. If you want a plain wall, the bricks are better and the fittings only get in the way. If you want something with plumbing in it, the parts that already have fittings save you most of the work. Fuel is the plain wall. Most chemicals are not.

### Why it matters

The chemical industry is one of the largest industrial consumers of energy and fossil feedstock, and unlike electricity generation it cannot be decarbonised by changing the power supply, because the carbon in a plastic is the product rather than the fuel. A carbon atom that ends up in a material has to come from somewhere, and biomass, waste and carbon dioxide are the alternatives to a well. Chemicals are also a far better match for biomass than fuels are: they account for a much smaller share of petroleum use and are worth several times more per tonne, so the same hectare of land displaces a great deal more fossil carbon when it makes a chemical than when it makes a fuel. Some of the field's products are genuinely better rather than merely greener, with fibres and polymers whose properties the petrochemical range does not match. The failures are equally instructive and are recorded here rather than passed over. Succinic acid was named a priority platform chemical, attracted at least four companies and several commercial plants, and most of them had exited or failed within a decade, because the downstream demand that the platform logic assumed did not materialise. Biobased does not automatically mean lower impact either: a route that needs more energy, more land or more processing can carry a larger footprint than the petrochemical one it replaces, and only a full life cycle assessment settles it.

### Applications

- Lactic acid production by fermentation, the largest biobased platform chemical by volume and the feedstock for polylactic acid
- 1,3-propanediol from glucose, produced commercially for a polyester fibre whose properties differ from the petrochemical alternative, which is the clearest case of a biobased route winning on performance rather than on virtue
- 1,4-butanediol by a pathway that exists in no natural organism, a solvent and polymer intermediate previously made only from acetylene or maleic anhydride
- Citric, itaconic and gluconic acid, long-established fermentation products that predate the biobased label entirely
- 2,5-furandicarboxylic acid from sugar, a potential replacement for terephthalic acid in polyesters, still scaling
- Bio-based monoethylene glycol for polyester bottles, produced via bio-ethanol and adopted at scale by consumer brands
- Glycerol derivatives including epichlorohydrin, which exploit a cheap by-product stream from biodiesel manufacture
- Levulinic acid, succinic acid and other platform acids proposed as building blocks, whose mixed commercial record is recorded honestly in `history.py`
- Amino acids for feed, food and chemical use, the oldest and largest fermentation chemistry in existence
- Bio-based acrylamide by nitrile hydratase, which replaced a copper catalysed route and is a standing example of enzymatic substitution
- Fermentation-derived 1,5-pentanediamine and other polyamide monomers
- Fragrance and flavour molecules including vanillin, nootkatone and santalol, where a natural label and a scarce plant source make the biological route commercially comfortable
- Cosmetic ingredients such as squalane produced by engineered yeast, which is where several fuel programmes profitably redirected themselves
- Surfactants including sophorolipids and rhamnolipids, and enzymatically made sugar esters
- Solvents such as ethyl lactate and 2-methyltetrahydrofuran, adopted where a regulator has restricted the petrochemical alternative
- Bio-ethylene by dehydration of bio-ethanol, technically simple, commercially marginal, and viable mainly where sugarcane is very cheap
- Bio-based aromatics from lignin, pursued for two decades and still without a large commercial process, since lignin is heterogeneous and its depolymerisation is unselective
- Isoprene, farnesene and terpene hydrocarbons, whose producers have generally moved upmarket into speciality applications rather than competing as commodities

### Technologies

- Fermentation of engineered strains to the target molecule or its immediate precursor, drawing on `white.metabolic_engineering`
- Enzymatic conversion of a biobased intermediate, drawing on `white.biocatalysis`
- Whole-cell biotransformation of a purchased substrate, which avoids building the pathway from sugar when the substrate is cheap
- Gas fermentation of carbon monoxide and carbon dioxide, which supplies acetate and ethanol as chemical feedstock rather than as fuel
- Reactive extraction and back-extraction for organic acids, which must handle a product that is ionised at the pH the organism prefers
- Electrodialysis and bipolar membrane processes for acid recovery, avoiding the salt waste that neutralisation produces
- Crystallisation and antisolvent precipitation, the cheapest recovery route when the product will cooperate
- Simulated moving bed chromatography for separations that a column cannot do economically in batch
- In situ product removal, which relieves inhibition and raises effective titre simultaneously
- Azeotropic and extractive distillation for alcohols and solvents
- Catalytic hydrogenation and hydrogenolysis of biobased acids and sugars to diols, which is where chemistry and biology are combined rather than opposed
- Dehydration chemistry converting sugars to furans, and alcohols to olefins
- Oxidation and esterification steps that finish a fermentation product into a saleable specification
- Lignin depolymerisation by catalytic, reductive or oxidative routes, still the field's least solved problem
- Radiocarbon determination of biobased carbon content, which distinguishes recently fixed carbon from fossil carbon in a finished product
- Techno-economic analysis and minimum selling price modelling, which is how a project is killed or funded long before a plant exists
- Life cycle assessment against the incumbent petrochemical route, without which the biobased claim is unsupported

### Challenges

- Competing on price against a petrochemical incumbent with a century of optimisation, depreciated assets and enormous scale, where a technically excellent process can still be commercially worthless
- Exposure to the oil price, since the competitiveness of a biobased route is set by a commodity nobody in the field controls and can reverse within a year
- Willingness to pay for the biobased attribute, which is frequently zero outside consumer-facing products, and which is a market question that no amount of process improvement answers
- The platform chemical fallacy, in which a molecule is an excellent chemical building block and a poor business because the downstream capacity to consume it was never built
- Separation of a dilute product from an aqueous broth, which for a bulk chemical often exceeds the cost of making it
- Salt waste from neutralising an organic acid fermentation, which is a real and unglamorous environmental burden of the route
- Product toxicity and low pH tolerance, which cap titre and therefore make the separation problem worse
- Capital intensity, since a plant must be financed and built before any revenue exists and cannot be scaled incrementally the way a chemical process line sometimes can
- Feedstock price volatility and its competition with food, real but an order of magnitude smaller than for fuels because the volumes are smaller and the values higher
- Removing oxygen to reach hydrocarbon targets, which wastes carbon as carbon dioxide and is the structural reason bio-based olefins and aromatics have struggled
- Lignin heterogeneity and unselective depolymerisation, which has kept biobased aromatics unsolved for two decades
- Substantiating an environmental claim, since biobased is not automatically lower impact and a route needing more energy, land or processing can be worse than what it replaces

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Oxygen to carbon ratio of the target | `O/C` | moles of oxygen per mole of carbon, dimensionless | about 1.0 for glucose; 0.5 - 1.0 for acids and diols; 0 for hydrocarbons | CONSENSUS |
| Degree of reduction of the product | `gamma` | available electrons per carbon, dimensionless | 4.0 for glucose; higher for reduced products such as alcohols and hydrocarbons | CONSENSUS |
| Carbon yield from feedstock | `Y_C` | moles of product carbon per mole of feedstock carbon | 0.3 - 0.9 Cmol/Cmol depending on how reduced the target is | CONSENSUS |
| Minimum selling price | `MSP` | euro per tonne of product | compared directly against the prevailing petrochemical price | REPORTED |
| Capital intensity | `C_capex` | euro of capital per annual tonne of capacity | substantially higher than for an equivalent petrochemical plant | REPORTED |
| Separation cost share | `f_sep` | per cent of operating cost attributable to product recovery | frequently the largest single share for a bulk product | REVIEWED |
| Salt burden of acid recovery | `m_salt` | tonnes of salt by-product per tonne of acid | approaching or exceeding one tonne per tonne for classical neutralisation routes | REVIEWED |
| Biobased carbon content | `f_bio` | per cent of total carbon that is recently fixed | 0 - 100 %, and measurable to within a few per cent | CONSENSUS |
| Cradle-to-gate greenhouse gas intensity | `GWP` | kilograms of carbon dioxide equivalent per kilogram of product | compared against the incumbent route, and not always lower | REPORTED |
| Process mass intensity | `PMI` | kilograms of input per kilogram of product | dominated by water for fermentation routes | CONSENSUS |
| Fossil resource displacement | `D_fossil` | kilograms of fossil feedstock avoided per kilogram of product | near one for a true drop-in replacement | REVIEWED |

### History

- **1916** - Acetone and butanol are produced industrially by fermentation
- **1923** - Citric acid fermentation displaces extraction from citrus fruit
- **1950** - Petrochemical feedstocks displace fermentation across the bulk chemical industry
- **1990** - Enzymatic acrylamide production replaces the copper catalysed route
- **2004** - A national laboratory publishes a list of top value-added chemicals from biomass
- **2006** - Commercial production of 1,3-propanediol from glucose begins
- **2009** - Bio-based monoethylene glycol enters large-scale use in beverage packaging
- **2012** - Four companies build commercial biobased succinic acid capacity
- **2013** - Commercial 1,4-butanediol production begins by a designed pathway
- **2016** - Fuel-oriented fermentation companies redirect to speciality and cosmetic ingredients
- **2019** - Most commercial biobased succinic acid capacity has been closed or sold
- **2021** - Regulatory attention turns to substantiating environmental claims
- **2022** - Gas fermentation and carbon dioxide derived chemicals reach commercial operation

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | CONTROLLED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | MATERIALS, ENVIRONMENT, FOOD |
| SDGs | 9, 12, 13 |

### Regulations

- Regulation (EC) No 1907/2006 REACH, under which a novel biobased molecule must be registered from scratch with its own toxicological dossier while the incumbent it competes with was registered long ago
- Regulation (EC) No 1272/2008 CLP on classification, labelling and packaging, which depends on the molecule and not on where its carbon came from
- Regulation (EU) No 528/2012 on biocidal products, and Regulation (EC) No 1223/2009 on cosmetic products, where the application requires its own authorisation
- Regulation (EC) No 1935/2004 and Regulation (EU) No 10/2011 on materials intended to come into contact with food
- Directive 2005/29/EC on unfair commercial practices and the subsequent instruments on substantiating environmental claims, which make an unevidenced biobased or renewable claim a regulated act
- Directive 2009/41/EC on the contained use of genetically modified microorganisms, and Directive 2000/54/EC on biological agents at work
- Directive 2010/75/EU on industrial emissions, with discharge consents covering the salt and organic load that acid fermentation recovery produces
- Directive 2012/18/EU Seveso III where solvent or reagent inventories pass threshold quantities
- Sustainability criteria for biomass feedstock where a product claims renewable content or benefits from a support scheme
- The Nagoya Protocol, where the producing organism or its pathway derives from another country's genetic resources

### Standards

- ASTM D6866 and EN 16640 for determining biobased carbon content by radiocarbon analysis, which verifies the claim on the finished product rather than by auditing the supply chain
- EN 16785 for determining the biobased content of products, including those containing both biobased and fossil carbon
- EN 16575 and the associated terminology standards, which fix what the word biobased may be taken to mean
- ISO 14040, ISO 14044 and ISO 14067, and the product environmental footprint category rules, which fix system boundaries so that two producers compute a comparable number
- Conventions on the accounting treatment of biogenic carbon and of end-of-life, which materially change the result and must therefore be declared
- Public procurement schemes with minimum biobased content requirements, which have moved more volume in some markets than any environmental argument
- Certification schemes for biobased products and for the mass balance attribution of certified feedstock through shared infrastructure
- Product specification standards for purity, colour and trace impurities, which a drop-in molecule must meet exactly, since a customer's process was tuned to the incumbent's impurity profile rather than to the ideal one
- Pharmacopoeial and food-grade specifications where the chemical enters those supply chains
- Responsible Care and industry codes on process safety and product stewardship, which apply to this sector on the same terms as to the petrochemical one

### Related records

- `white.biofuels`
- `white.metabolic_engineering`
- `white.biocatalysis`
- `white.bioprocess_engineering`
- `white.biopolymers`
- `green.plant_genetic_engineering`
- `purple.biotechnology_patents`

### Cross-references

- [white.biofuels](biofuels.md)
- [white.metabolic_engineering](metabolic_engineering.md)
- [white.biocatalysis](biocatalysis.md)
- [white.bioprocess_engineering](bioprocess_engineering.md)
- [white.biopolymers](biopolymers.md)
- [green.plant_genetic_engineering](../green/plant_genetic_engineering.md)
- `purple.biotechnology_patents` (branch not written yet)
