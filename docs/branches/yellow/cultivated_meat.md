<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/yellow/cultivated_meat/.
  Edit the source and run `make docs`.
-->

[Yellow Biotechnology](index.md) / **Cultivated Meat**

## Cultivated Meat

`yellow.cultivated_meat`

Growing animal muscle and fat cells in culture to produce meat without raising or slaughtering an animal.

### What it is

Cultivated meat grows animal cells in a bioreactor and assembles them into a food. The sequence is established: a cell line is obtained from a biopsy or an existing bank, expanded in a growth medium, differentiated into muscle and fat, and either harvested as loose cells for a formed product or grown on a scaffold to approach the structure of a cut. The biology is not in doubt. Animal cell culture has been routine in laboratories for seventy years and at manufacturing scale in `red.pharmaceutical_biotechnology` for forty. Four problems are unsolved together, and they interact. The growth medium is the dominant cost and was developed as a pharmaceutical input, so removing its serum, replacing its recombinant growth factors with cheaper sources and recycling it are the field's central work. Cell line performance matters more than in pharmaceutical culture because the cells are the product rather than a factory for one: primary cells senesce after a limited number of divisions, and immortalised lines avoid that at the cost of a regulatory conversation about what has been done to them. Bioreactor design must handle shear-sensitive adherent cells at volumes the pharmaceutical industry never needed, since a therapeutic protein is made in grams and food is made in tonnes. And structure is a separate problem again: loose cells make a formed product, and anything resembling a steak requires scaffolding, perfusion and co-culture of at least muscle and fat. What has been achieved is real and modest. A cultivated burger was presented in 2013 at a cost that made the point rather than the product. Regulatory approval for sale followed in Singapore in 2020 and in the United States in 2023, in both cases for chicken products and at small volumes. Several jurisdictions have moved in the other direction and prohibited sale outright. Production remains at kilogram rather than tonne scale. The scale-up problem is not the ordinary one. In most technologies cost falls with volume because fixed costs spread and manufacturing improves. Here the dominant cost is a consumable input, the medium, whose price falls only if its composition changes, and the second cost is capital for bioreactor capacity that does not yet exist at food scale. Neither falls automatically with volume, which is the same error `yellow.precision_fermentation` made in its 2023 projections and the same shape `white.biobased_chemicals` records for succinic acid.

### In plain language

This is growing meat from animal cells instead of from animals. A small sample of cells is taken once, then fed and multiplied in a tank until there is enough to eat. It is genuinely meat, not an imitation, and it has been approved for sale in a couple of places. It is also made in very small quantities and costs a great deal, because the liquid the cells are fed on was developed for medical laboratories and is expensive, and because equipment to do this at the scale of a food industry does not exist yet. The science is real. The price is the problem, and it is not the kind of problem that gets solved simply by making more.

### An analogy

It is growing tomatoes in a heated greenhouse in winter. The tomatoes are real tomatoes and nobody disputes that; what decides whether the business works is the heating bill, not the horticulture. The comparison is kind in one respect and unkind in another. A greenhouse at least gets its light free, while every nutrient these cells receive has to be bought and most of it was priced for a laboratory.

### Why it matters

If it worked at scale it would address something no other record in this branch addresses: meat itself, rather than a substitute for it, produced without raising or slaughtering an animal. That removes the welfare question entirely rather than reducing it, avoids the antibiotic use and zoonotic risk that `green.veterinary_vaccines` describes, and would in principle use a fraction of the land that livestock occupies. For consumers unwilling to accept a substitute, it is the only approach that offers the product rather than an approximation, which is why it attracts attention disproportionate to its volume. The honest position is that none of that has been delivered. Production is at kilogram scale, cost per kilogram remains far above commodity meat, and the dominant cost is a medium input whose price does not fall simply with volume. The environmental case is genuinely uncertain rather than merely unproven: assessments differ on whether cultivated meat beats conventional beef, and the answer depends almost entirely on how the energy for the process is generated and on how the medium inputs are produced. Several jurisdictions have prohibited sale for reasons that are cultural and political rather than evidential, which no technical progress will resolve. And the immortalised cell lines that make continuous production practical raise a regulatory and consumer conversation the field has not had in public.

### Applications

- Cultivated chicken sold in Singapore following approval in 2020, in small volumes and in formed rather than whole-cut products
- Cultivated chicken approved for sale in the United States in 2023 and offered through restaurants at limited scale
- Cultivated pet food, which reached market in some jurisdictions ahead of human food because the regulatory path is shorter and the consumer acceptance question does not arise in the same form
- Cultivated beef in formed products, demonstrated publicly since 2013 and not commercially available
- Hybrid products combining cultivated animal fat with plant protein, which use the cultivated component for flavour rather than for bulk and are the most plausible near-term route to market
- Cultivated fat as an ingredient, which is technically easier than muscle because adipocytes require no alignment and because fat carries much of what is recognised as meat flavour
- Cultivated seafood, including finfish and crustacean cells, where the argument connects to the wild stock pressure in `blue.aquaculture_biotechnology`
- Structured whole cuts requiring scaffolding, vascularisation and co-culture of muscle, fat and connective tissue, which remains the field's stated objective and has not been produced at any commercial scale
- Production at tonne rather than kilogram scale, which no facility has yet demonstrated and which the cost structure in `metrics.py` explains
- Price parity with commodity meat, which no published figure has approached and which is the condition on every environmental and welfare argument made for the field
- Food-grade growth medium development, which is where most of the field's technical progress has actually occurred and where the cost reductions have been real
- Cell line banking and characterisation for food use, which is infrastructure the field did not have and now does

### Technologies

- Serum-free medium formulation, which removed the foetal bovine serum that made the whole proposition incoherent, since a meat alternative cannot depend on a slaughterhouse product
- Food-grade replacement of pharmaceutical-grade medium components, which is the largest single cost reduction available and is a purity specification question rather than a biological one
- Recombinant growth factor production by microbial fermentation, which links this record directly to `yellow.precision_fermentation` and is where the remaining medium cost concentrates
- Medium recycling and perfusion, recovering unconsumed components rather than discarding spent medium
- Plant hydrolysate and low-cost nutrient sources as partial replacements
- Cell line establishment from biopsy, and banking under food-appropriate conditions
- Immortalisation or selection of spontaneously immortalised lines, which makes continuous production practical and raises a regulatory and consumer question the field has not had in public
- Adaptation to suspension growth, which removes the need for a surface and is the single change that would most simplify scale-up
- Differentiation control into myotubes and adipocytes, since undifferentiated cells are biomass rather than meat
- Stirred tank and perfusion bioreactor design for shear-sensitive animal cells at food volumes, which is `white.bioprocess_engineering` applied to a product worth a thousandth as much per kilogram
- Microcarrier culture, including edible microcarriers that need not be removed from the product
- Oxygen transfer and metabolite removal at high cell density, where lactate and ammonia accumulation limit the achievable density
- Edible scaffolds from plant protein, alginate or decellularised material, which give cells something to align on
- Co-culture of muscle, fat and connective tissue, since a cut of meat is several tissues rather than one
- Perfusion and vascularisation approaches for thick constructs, which is the same diffusion limit `red.regenerative_medicine` records and the same unsolved problem
- Three-dimensional printing and fibre alignment for whole-cut structure

### Challenges

- Growth medium cost, which dominates the cost of goods and which falls only if the composition changes, since it is a consumable input rather than a fixed cost that volume spreads
- A scale-up curve that does not behave like the ones the projections were borrowed from, because the two dominant costs are a purchased consumable and capital for capacity that does not exist, neither of which falls automatically with production volume
- Capital cost of food-scale animal cell bioreactor capacity, which has never been built and for which the pharmaceutical industry's equipment is sized for grams rather than tonnes
- Shear sensitivity of animal cells, which limits agitation and therefore oxygen transfer, in direct tension with the cell densities the economics require
- Replicative senescence in primary cells, and the regulatory and consumer questions raised by the immortalised lines that avoid it
- Metabolite accumulation, particularly lactate and ammonia, which caps achievable cell density independently of nutrient supply
- Contamination risk in an open-ended culture with no antibiotic use and no terminal sterilisation of the product
- Diffusion limits in thick constructs, which is the same hundred to two hundred micrometre oxygen limit `red.regenerative_medicine` is organised around and which no cultivated meat process has solved either
- Co-culture of multiple tissue types at different differentiation rates
- Genuine uncertainty in the life cycle assessment, where published results differ on whether cultivated meat beats conventional beef and the answer depends chiefly on the energy source and on how medium inputs are produced
- Outright prohibition of sale in several jurisdictions on cultural and political grounds, which no technical progress addresses
- Consumer acceptance of a product grown from cells, which surveys measure inconsistently and which no approved market has yet tested at scale
- Naming and labelling disputes, including whether the product may be called meat, which are being decided by legislatures rather than by composition

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Production cost per kilogram | `C_kg` | euro per kilogram of product | far above commodity meat; the 2013 demonstration cost was in the hundreds of thousands of euro per kilogram and current figures are much lower and not competitive | REPORTED |
| Medium cost per litre | `C_med` | euro per litre of growth medium | the dominant component of cost of goods, and the target of most of the field's technical work | REPORTED |
| Medium consumption per kilogram of product | `V_med` | litres of medium per kilogram of biomass | high, and reduced by perfusion and recycling rather than by cell biology | REVIEWED |
| Maximum cell density | `X_max` | cells per millilitre | 10^7 - 10^8 cells/mL in high-density perfusion systems | REVIEWED |
| Population doubling time | `t_d` | hours | 18 - 30 h for animal cells, against under an hour for bacteria | CONSENSUS |
| Population doublings before senescence | `N_pd` | doublings | limited in primary cells; unlimited in immortalised lines | CONSENSUS |
| Differentiation efficiency | `f_diff` | per cent of cells forming myotubes or adipocytes | varies widely and is a principal determinant of product quality | REVIEWED |
| Oxygen transfer coefficient | `kLa` | per hour | constrained by shear tolerance far below what microbial culture permits | CONSENSUS |
| Protein and fat composition | `C_comp` | per cent by weight | matched to the conventional product it represents | REVIEWED |
| Construct thickness achievable | `d_max` | micrometres without perfusion | roughly 100 - 200 um, the same oxygen diffusion limit that governs tissue engineering | CONSENSUS |
| Greenhouse gas intensity | `GWP` | kilograms of carbon dioxide equivalent per kilogram of product | published assessments disagree on whether it beats conventional beef | REPORTED |
| Energy use per kilogram | `E_kg` | megajoules per kilogram of product | high, since the process replaces an animal's metabolism with heating, mixing and sterile manufacture | REVIEWED |
| Land use per kilogram of protein | `A_land` | square metres per kilogram | much lower than ruminant meat, and not zero because medium inputs are agricultural | REVIEWED |

### History

- **1931** - Churchill speculates that meat might be grown from the relevant parts rather than from a whole animal
- **1951** - Continuously culturable human cells establish that animal cells can be propagated indefinitely
- **1986** - Large-scale mammalian cell culture becomes routine in pharmaceutical manufacture
- **2013** - The first cultivated beef burger is presented publicly
- **2017** - Serum-free media suitable for cultivated meat are developed
- **2020** - Singapore approves the sale of cultivated chicken
- **2022** - Cultivated pet food reaches market ahead of human food in some jurisdictions
- **2023** - The United States approves cultivated chicken for sale
- **2023** - Italy prohibits the production and sale of cultivated meat
- **2024** - Cost reduction slows and investment in the sector contracts sharply
- **2024** - Food-grade medium components and recombinant growth factor production become the field's principal work

### Governance

| Field | Value |
|---|---|
| Maturity | PILOT |
| Risk tier | REGULATED |
| Scale | PILOT |
| Regulatory status | VARIES |
| Domains | FOOD, ENVIRONMENT, HEALTH |
| SDGs | 3, 12, 15 |

### Regulations

- Singapore Food Agency novel food framework, under which the first approval anywhere was granted in 2020
- United States joint oversight between the Food and Drug Administration and the Food Safety and Inspection Service, the first agency assessing cell collection and culture and the second the harvest, processing and labelling, which is how a product falling between frameworks was actually handled
- Regulation (EU) 2015/2283 on novel foods, which is the route in the European Union and which no application has yet completed
- National prohibitions on the production and sale of cultivated meat, enacted in Italy in 2023 and in comparable form in several other jurisdictions, in most cases before any such product was available for sale there
- Naming and denomination restrictions preventing the use of meat terms for cultivated products, which in several places accompany or substitute for prohibition
- Regulation (EC) No 178/2002 and Regulation (EC) No 852/2004 on general food law and hygiene
- Regulation (EC) No 853/2004 on food of animal origin, whose applicability to a product from cells rather than from a carcass is not straightforward and is part of why the product falls between frameworks
- Regulation (EU) No 1169/2011 on food information, including allergen declaration and the naming question
- Feed and food ingredient rules applying to growth medium components, since the medium is an input to a food and its components must be food-grade
- Directive 2009/41/EC on contained use, where genetically modified microorganisms produce the recombinant growth factors the medium requires
- Directive 2010/63/EU on animals used for scientific purposes, applicable to the biopsy from which a cell line is established

### Standards

- Cell bank characterisation conventions from pharmaceutical manufacture, covering identity, purity, stability and freedom from adventitious agents, which this record inherited wholesale
- Good Manufacturing Practice concepts for cell culture, applied at a cost structure they were never designed for
- Adventitious agent and mycoplasma testing, which is routine in pharmaceutical culture and non-negotiable here
- Food-grade specifications for growth medium components, which did not exist because no previous application needed a cell culture medium at food purity and food price
- Characterisation expectations for immortalised cell lines used in food, which are still being established and which are the least settled area of the record's governance
- Compositional and nutritional characterisation against the conventional meat the product represents
- Allergen assessment, which for an animal cell product is expected to mirror the conventional meat, on the same reasoning `yellow.precision_fermentation` records for identical proteins
- ISO 14040 and ISO 14044 life cycle assessment with the energy source and the medium input production route declared, since `metrics.py` records that the result depends chiefly on those two assumptions and published studies disagree because of them
- Absence of agreed terminology, so cultivated, cultured, cell-based and lab-grown are used interchangeably in scientific literature and are treated as materially different in regulation and marketing
- Absence of accepted scale-up and validation conventions for food-scale animal cell culture, which is unsurprising since no facility has operated at that scale

### Related records

- `red.regenerative_medicine`
- `yellow.alternative_proteins`
- `yellow.precision_fermentation`
- `white.bioprocess_engineering`
- `green.animal_biotechnology`
- `blue.aquaculture_biotechnology`
- `purple.bioethics`

### Cross-references

- [red.regenerative_medicine](../red/regenerative_medicine.md)
- [yellow.alternative_proteins](alternative_proteins.md)
- [yellow.precision_fermentation](precision_fermentation.md)
- [white.bioprocess_engineering](../white/bioprocess_engineering.md)
- [green.animal_biotechnology](../green/animal_biotechnology.md)
- [blue.aquaculture_biotechnology](../blue/aquaculture_biotechnology.md)
- `purple.bioethics` (branch not written yet)
