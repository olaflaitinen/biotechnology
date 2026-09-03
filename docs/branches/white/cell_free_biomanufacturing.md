<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/white/cell_free_biomanufacturing/.
  Edit the source and run `make docs`.
-->

[White Biotechnology](index.md) / **Cell-Free Biomanufacturing**

## Cell-Free Biomanufacturing

`white.cell_free_biomanufacturing`

Producing proteins and metabolites using extracted cellular machinery rather than living cells, programmed directly with DNA or RNA.

### What it is

Cell-free biomanufacturing carries out biological synthesis in a reaction mixture rather than inside an organism. A crude extract or a reconstituted set of components supplies the transcription and translation machinery, and a DNA or RNA template supplies the instruction. The trade against fermentation is sharp in both directions: the system cannot replicate itself, so the catalyst is consumed rather than grown, and every component must be supplied rather than made. In exchange there is no growth phase, no genetic drift, no carbon diverted to biomass, and no membrane between the operator and the reaction. Two kinds of system exist and they answer different questions. Crude extracts, prepared by lysing cells and removing the debris, are cheap, productive and chemically complex, retaining metabolism that can be exploited for energy regeneration or that can consume the product unhelpfully. Reconstituted systems, assembled from individually purified components, contain only what was deliberately added, which makes them clean, fully defined, expensive and much less productive. Extracts are used for making things; reconstituted systems are used for answering questions about what is sufficient. The absence of a membrane is the practical advantage. The reaction environment can be set directly rather than through what a cell will tolerate, so redox potential, chaperones, unusual cofactors and non-standard amino acids can simply be added. Products that would kill an organism, including membrane proteins, toxins and antimicrobial peptides, can be produced because there is nothing alive to poison. A linear DNA template works directly, so the cloning and transformation steps disappear, and a design-build-test cycle that takes days in cells takes hours here. Reactions can also be freeze-dried onto paper or into pellets and rehydrated later, which turns a biological process into a shelf-stable reagent that needs no cold chain and no laboratory. It has nonetheless not displaced fermentation, and the reasons are economic rather than conceptual. The energy substrates that drive protein synthesis cost more than sugar, the extract itself must be manufactured from cells that were grown conventionally, batch-to-batch variability in crude extracts is a real and under-reported problem, and the catalyst is consumed rather than reproducing. Cell-free manufacture therefore competes where speed, control or portability are worth more than cost per gram, which is a narrower set of applications than its advocates have historically claimed.

### In plain language

Normally, making a protein means growing bacteria or yeast and persuading them to produce it. Cell-free manufacturing skips the organism: the working parts are taken out of cells, put in a tube, and given written instructions in the form of DNA. Nothing in the tube is alive. That has real advantages. It is fast, taking hours rather than days. You can make things that would kill a living cell. You can reach in and adjust the conditions directly, because there is no cell wall in the way. And the whole mixture can be freeze-dried, stored on a shelf without refrigeration, and started later by adding water, which means a biological test can be carried out somewhere with no laboratory at all.

### An analogy

Fermentation is hiring a chef who will cook for you but has opinions, needs feeding, takes days to arrive and refuses certain dishes. Cell-free is taking the chef's kitchen and doing it yourself. Everything is to hand and nothing argues, so an unusual dish is no harder than an ordinary one. The catch is that the chef would have gone shopping and the kitchen will not: when the ingredients run out, they run out, and you paid for all of them in advance.

### Why it matters

Two capabilities are difficult to obtain any other way. The first is speed: a design-build-test cycle measured in hours rather than days makes it practical to test hundreds of genetic designs before committing any of them to an organism, which is why this technique now underpins much of the prototyping in synthetic biology. The second is portability. A freeze-dried reaction on paper needs no cold chain, no power and no laboratory, and rehydrating it with a drop of sample can give a specific diagnostic result in the field. That has been demonstrated for outbreak pathogens and it puts molecular diagnosis somewhere a molecular laboratory will never be. Manufacturing biologics on demand, at the point of care, from a stored template rather than a stored product, is the same argument applied to medicines. The honest counterweight is that this technology has been described as imminent for a very long time and remains a small share of biological manufacturing. Energy substrates cost more than sugar, the extract must itself be grown, crude preparations vary between batches in ways that are poorly documented, and the catalyst is spent rather than self-renewing. It wins on speed, on control and on portability, and it does not win on cost per gram.

### Applications

- Rapid prototyping of genetic circuits and regulatory elements, where hundreds of designs are tested in a day before any is committed to an organism
- Screening enzyme variants directly from linear DNA templates, without cloning, transformation or colony picking
- Prototyping metabolic pathways by mixing separately expressed enzymes in chosen ratios, which is far quicker than balancing expression in a living strain
- Rapid production of protein reagents and antigens for research and assay development
- Production of membrane proteins in the presence of nanodiscs, liposomes or detergents supplied directly to the reaction
- Synthesis of toxins, antimicrobial peptides and other products that kill the organisms normally used to make them
- Site-specific incorporation of non-standard amino acids, which is far simpler without competing cellular translation machinery
- Controlled formation of disulphide bonds by setting the redox potential of the reaction directly, rather than by engineering a compartment inside a cell
- Cell-free glycoprotein synthesis with defined glycosylation, added as enzymes rather than inherited from a host
- Enzyme cascades operating outside any organism, including routes to products whose intermediates would be consumed by native metabolism
- Freeze-dried paper-based sensors that are rehydrated with a sample and report a specific nucleic acid sequence by colour change
- Field-deployable diagnostics for outbreak pathogens, demonstrated for emerging viruses and for antimicrobial resistance markers
- On-demand production of therapeutic proteins from stored DNA templates, which replaces a cold chain for the product with a shelf-stable instruction
- Water and food contaminant sensors built on the same lyophilised format
- Educational kits that make protein expression visible without requiring a containment laboratory or living modified organisms, which is a teaching advantage rather than a manufacturing one

### Technologies

- Crude cell extract preparation by lysis and clarification, which is cheap and productive and carries residual metabolism with it
- Reconstituted systems assembled from individually purified translation components, fully defined and much less productive
- Eukaryotic extracts from wheat germ, insect and mammalian cells for proteins that bacterial systems fold badly or cannot modify
- Extract processing to remove nucleases and proteases that would otherwise destroy the template and the product
- Energy regeneration from phosphoenolpyruvate or creatine phosphate, effective and expensive
- Glucose and maltodextrin based regeneration coupled to residual glycolysis in the extract, which is much cheaper and is the main reason crude extracts are preferred for manufacture
- Phosphate and inorganic by-product management, since accumulating phosphate inhibits the reaction and is a common reason yields stall
- Batch reactions, simple and limited by substrate depletion and by-product accumulation
- Continuous exchange and dialysis formats, which feed substrates and remove inhibitors across a membrane and extend reactions from hours to a day or more
- Microfluidic and droplet formats for very high throughput screening
- Linear template use, which removes cloning entirely and requires the nuclease protection noted above
- Lyophilisation of complete reactions onto paper or into pellets, which is what converts a biological process into a shelf-stable reagent
- Sensor design using toehold switches and other RNA elements that couple sequence recognition to a visible output
- Coupling to isothermal nucleic acid amplification, which supplies the sensitivity that the cell-free readout alone lacks

### Challenges

- Cost of energy substrates and cofactors, which must all be purchased rather than made by a growing organism, and which is the principal reason cost per gram cannot match fermentation
- A catalyst that is consumed rather than reproducing, so each reaction pays for its own machinery instead of inheriting it from the last generation
- The extract itself must be manufactured from cells grown conventionally, so the technology does not escape fermentation but sits downstream of it
- Batch-to-batch variability of crude extracts, which is real, under-reported and the largest obstacle to using cell-free systems in a regulated manufacturing process
- Residual metabolism in crude extracts that consumes substrates or degrades the product in ways that differ between preparations
- Accumulation of inorganic phosphate and other inhibitory by-products, which caps batch reactions long before the machinery is exhausted
- Nuclease and protease activity degrading template and product, particularly when linear DNA is used
- Limited reaction duration, so a process that a fermenter would run for a week runs here for hours
- Scale-up, which is demonstrated at the scale of tens to hundreds of litres rather than the hundreds of cubic metres routine in `white.microbial_fermentation`
- Absence of native glycosylation and other post-translational machinery in bacterial extracts, which must be supplied enzymatically and adds cost and complexity
- A biosecurity control point that has moved, since a system programmed by nucleic acid and containing nothing alive is not captured by the frameworks written for living modified organisms, which places the burden on DNA synthesis screening instead

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Time from template to product | `t_result` | hours | 2 - 8 h, against 2 - 5 days for an equivalent result in cells | CONSENSUS |
| Design-build-test cycle time | `t_DBTL` | hours per iteration | under 24 h, against days to weeks in a living host | REVIEWED |
| Protein titre | `C_p` | grams of protein per litre of reaction | 0.1 - 1 g/L routinely, with above 2 g/L reported for optimised bacterial extracts in batch | REVIEWED |
| Volumetric productivity | `Q_p` | grams per litre per hour | often favourable against fermentation, since the same titre is reached in hours rather than days | REVIEWED |
| Reaction duration before stall | `t_run` | hours of continued synthesis | 2 - 6 h in batch; 10 - 24 h or more in continuous exchange formats | CONSENSUS |
| Cost per milligram of product | `C_mg` | euro per milligram | one to three orders of magnitude above fermentation for the same protein | REPORTED |
| Energy substrate consumption | `n_ATP` | ATP equivalents per peptide bond formed | at least 4 by stoichiometry, and considerably more in practice | CONSENSUS |
| Extract batch-to-batch variability | `CV_extract` | per cent coefficient of variation in yield between preparations | frequently substantial and rarely reported | REPORTED |
| Shelf life of the lyophilised reaction | `t_shelf` | months of retained activity at ambient temperature | 6 - 12 months reported without refrigeration | REVIEWED |
| Limit of detection of a cell-free sensor | `LOD` | molar concentration or copies per reaction | picomolar to femtomolar when coupled to isothermal amplification, far poorer without it | REVIEWED |
| Non-standard amino acid incorporation efficiency | `f_nsAA` | per cent of target sites correctly substituted | above 90 % achievable at a single site in an optimised system | REVIEWED |

### History

- **1897** - Buchner shows that cell-free yeast extract ferments sugar
- **1961** - Nirenberg and Matthaei crack the first codon using a cell-free extract
- **1988** - Continuous-flow cell-free synthesis extends reactions from minutes to many hours
- **2001** - A fully reconstituted translation system is assembled from purified components
- **2004** - Glucose-based energy regeneration replaces phosphorylated energy substrates
- **2010** - Cell-free manufacturing remains a small share of biological production despite four decades of expectation
- **2014** - Complete cell-free reactions are freeze-dried onto paper and reactivated with water
- **2016** - Paper-based cell-free sensors are demonstrated against an outbreak pathogen in the field
- **2018** - Freeze-dried cell-free kits enter classroom use
- **2020** - On-demand production of biologics from stored templates is demonstrated at the point of care
- **2022** - Cell-free glycoprotein synthesis with defined glycans is demonstrated

### Governance

| Field | Value |
|---|---|
| Maturity | PILOT |
| Risk tier | CONTROLLED |
| Scale | BENCH |
| Regulatory status | VARIES |
| Domains | HEALTH, MATERIALS, SECURITY |
| SDGs | 3, 4, 9 |

### Regulations

- Directive 2009/41/EC on the contained use of genetically modified microorganisms, which applies in full to culturing the cells that the extract is made from and not to the cell-free reaction itself
- Directive 2000/54/EC on biological agents at work, for the same production step
- Regulation (EU) 2017/746 on in vitro diagnostic medical devices, under which a cell-free sensor intended to inform a clinical decision is a regulated device
- EudraLex Volume 4 Good Manufacturing Practice, where the reaction produces a medicinal product, including at the point of care
- Regulation (EC) No 1907/2006 REACH for reagent components placed on the market as chemicals
- Export control and dual-use regulations applying to genetic sequences of concern rather than to organisms, which is where oversight of this technology necessarily sits
- National biosecurity provisions on the possession and synthesis of listed agent sequences, which apply to the template even though nothing in the reaction is alive
- Requirements for diagnostics used outside a laboratory setting, including instructions, interpretation and result reporting, which govern the record's most distinctive application
- Clinical trial and ethics approval where field diagnostics are evaluated on human samples

### Standards

- Reporting conventions for extract preparation, composition and batch-to-batch performance, which are not yet consistently applied and whose absence is the largest obstacle to regulated use of these systems
- Reference materials and positive controls allowing yields to be compared between laboratories, without which a published titre is not a reproducible claim
- Synthetic Biology Open Language and standard part registries for describing the genetic template
- Minimum information conventions for reporting synthetic circuits and their performance
- International Gene Synthesis Consortium screening protocols for synthesised DNA orders, which are voluntary and are the operative control on what a cell-free system can be asked to produce
- Institutional review of sequences of concern, applied to templates rather than to organisms
- ISO 13485 and IEC 62304 where a cell-free diagnostic is developed as a device
- ISO 15189 and point-of-care testing guidance for results generated outside a laboratory
- Good Manufacturing Practice expectations for reagents used in the manufacture of a medicinal product
- Stability testing conventions for lyophilised biological reagents, which are what substantiate the ambient shelf life claim in `metrics.py`

### Related records

- `white.biocatalysis`
- `white.metabolic_engineering`
- `white.microbial_fermentation`
- `red.molecular_diagnostics`
- `red.pharmaceutical_biotechnology`
- `dark.biosecurity`

### Cross-references

- [white.biocatalysis](biocatalysis.md)
- [white.metabolic_engineering](metabolic_engineering.md)
- [white.microbial_fermentation](microbial_fermentation.md)
- [red.molecular_diagnostics](../red/molecular_diagnostics.md)
- [red.pharmaceutical_biotechnology](../red/pharmaceutical_biotechnology.md)
- `dark.biosecurity` (branch not written yet)
