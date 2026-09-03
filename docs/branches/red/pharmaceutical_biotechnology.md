<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/red/pharmaceutical_biotechnology/.
  Edit the source and run `make docs`.
-->

[Red Biotechnology](index.md) / **Pharmaceutical Biotechnology**

## Pharmaceutical Biotechnology

`red.pharmaceutical_biotechnology`

Discovery, production and formulation of biologic medicines made in living expression systems rather than by chemical synthesis.

### What it is

A biologic is a medicine whose active ingredient is produced by a living system: a recombinant protein, a monoclonal antibody, a peptide, an enzyme, a nucleic acid, or a conjugate of these. The molecule is typically a hundred to a thousand times larger than a conventional small-molecule drug and carries post-translational modifications, above all glycosylation, that no synthetic route can reproduce economically or reproducibly. Production follows a fixed sequence. A gene of interest is cloned into an expression vector; a host cell line is transfected and a single high-producing clone is isolated and banked as a master and a working cell bank; the clone is expanded through seed trains into production bioreactors; the product is captured on an affinity resin, polished by one or two orthogonal chromatography steps, and formulated. Chinese hamster ovary cells dominate for glycosylated proteins, Escherichia coli for simple non-glycosylated ones, and yeast for peptides and some vaccine antigens. Because the product is defined by its process as much as by its sequence, regulators treat any change to the process as a change to the medicine. That single principle is why generic copies are called biosimilars rather than generics, why a comparability exercise follows every process change, and why manufacturing capacity rather than chemistry is the barrier to entry.

### In plain language

Aspirin is a small, simple molecule that a chemist can build from scratch in a flask. Insulin is not: it is a folded chain of building blocks far too complicated to assemble that way. So instead of building it, we give the recipe to living cells, grow those cells in enormous stainless steel tanks, and let them do the manufacturing. Afterwards the medicine is separated out and purified until nothing of the cells remains. Almost all modern cancer and arthritis medicines are made like this.

### An analogy

You cannot carve a loaf of bread out of a block of wood, however sharp your knife. You have to let yeast make it. Biologic medicines are the same: the product is grown rather than machined. And as with bread, the recipe alone is not enough - the temperature, the timing and the particular strain of yeast all end up in the result, which is why a copy made in a different factory is never quite identical and has to be tested rather than assumed equivalent.

### Why it matters

Biologics changed the prognosis of rheumatoid arthritis, several cancers and a long list of autoimmune conditions from managed decline to something close to normal life. They are also the most expensive class of medicine ever made, and about half of all pharmaceutical spending in high-income health systems now goes to them. That is why biosimilar competition matters so much: when a biosimilar enters a European market the price of the reference product typically falls by a quarter to a half within two years, which is often the difference between a health system funding a treatment for everyone who needs it and rationing it.

### Applications

- Recombinant human insulin and engineered insulin analogues
- Recombinant human growth hormone
- Erythropoietin and granulocyte colony-stimulating factors
- Recombinant clotting factors VIII and IX for haemophilia
- Therapeutic monoclonal antibodies in oncology and immunology
- Fusion proteins and Fc-fusion decoy receptors
- Enzyme replacement therapy for lysosomal storage disorders
- PEGylated proteins with extended circulating half-life
- Biosimilar development and formal comparability exercises
- Contract development and manufacturing for third-party products

### Technologies

- Chinese hamster ovary (CHO) suspension cell lines
- Escherichia coli periplasmic secretion and inclusion-body refolding
- Pichia pastoris and Saccharomyces cerevisiae secretion systems
- Glycoengineered host lines producing defined glycoforms
- Single-use stirred-tank bioreactors from 50 L to 2000 L
- Fed-batch, perfusion and intensified seed-train strategies
- Chemically defined, animal-component-free media
- Protein A affinity capture chromatography
- Ion exchange and hydrophobic interaction polishing
- Viral inactivation by low pH and nanofiltration
- Tangential flow filtration for concentration and buffer exchange
- Quality by design with defined critical quality attributes
- Process analytical technology and multivariate batch monitoring
- Extended characterisation by peptide mapping and glycan profiling

### Challenges

- Cost of goods dominated by upstream titre and by the price of downstream capture resin, both of which resist further improvement
- Immunogenicity in a fraction of patients, producing anti-drug antibodies that neutralise the therapy over months to years
- Glycan heterogeneity between batches and between manufacturing sites, which is the usual sticking point in a comparability exercise
- Cold chain requirements that limit distribution in warm climates and in settings without reliable electricity
- The comparability evidence required after any process change, which discourages manufacturers from improving processes at all
- Concentration of large-scale manufacturing capacity in a small number of countries, exposed during every supply shock
- Biosimilar uptake that varies more with national procurement policy than with clinical evidence

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Product titre | `C_p` | grams per litre of harvested culture | 1 - 10 g/L for CHO fed-batch | CONSENSUS |
| Specific productivity | `q_p` | picograms per cell per day | 10 - 60 pg/cell/day | CONSENSUS |
| Viable cell density | `VCD` | million viable cells per millilitre | 5 - 30 x 10^6 cells/mL peak | CONSENSUS |
| Downstream step yield | `Y_step` | per cent recovered per unit operation | 85 - 98 % per step | REVIEWED |
| Host cell protein residual | `HCP` | nanograms per milligram of product | < 100 ng/mg | REVIEWED |
| High molecular weight aggregate | `HMW` | per cent by size-exclusion chromatography | < 2 - 5 % at release | CONSENSUS |

### History

- **1922** - Insulin extracted from animal pancreas is first used to treat a patient
- **1973** - Cohen and Boyer demonstrate recombinant DNA in bacteria
- **1975** - Asilomar conference agrees voluntary safety guidelines for recombinant DNA
- **1978** - Human insulin gene expressed in Escherichia coli
- **1980** - Diamond v. Chakrabarty establishes that living organisms may be patented
- **1980** - Bayh-Dole Act allows universities to patent federally funded inventions
- **1982** - Humulin approved: the first recombinant medicine anywhere
- **1985** - Growth hormone from human pituitary extract withdrawn after Creutzfeldt-Jakob transmission
- **1986** - Muromonab-CD3 approved: the first therapeutic monoclonal antibody
- **1997** - Rituximab approved, establishing antibodies as a mainstream modality
- **2006** - European Union creates the first biosimilar regulatory pathway
- **2015** - First biosimilar approved in the United States
- **2021** - Single-use and continuous processing reach routine commercial scale

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | HEALTH |
| SDGs | 3, 9 |

### Regulations

- EU Directive 2001/83/EC on the Community code relating to medicinal products for human use
- EU Regulation (EC) No 726/2004 establishing the European Medicines Agency and the centralised authorisation procedure, mandatory for all biotechnology-derived medicines
- EU Directive 2003/94/EC on good manufacturing practice
- EU Regulation (EU) No 536/2014 on clinical trials
- EU Directive 2009/41/EC on contained use of genetically modified micro-organisms, which covers the production strain
- US Public Health Service Act section 351 biologics licence application
- US Biologics Price Competition and Innovation Act 2009, creating the biosimilar pathway
- US 21 CFR Parts 210 and 211 current good manufacturing practice
- ICH Q5A-Q5E incorporated into EU and US law by reference

### Standards

- EU GMP Annex 1 manufacture of sterile medicinal products
- EU GMP Annex 2 manufacture of biological active substances and medicinal products for human use
- ISO 13408 aseptic processing of health care products
- ISO 14644 cleanrooms and associated controlled environments
- ICH Q8(R2) pharmaceutical development, introducing quality by design
- ICH Q9 quality risk management
- ICH Q10 pharmaceutical quality system
- ICH Q11 development and manufacture of drug substances
- ICH Q12 lifecycle management of post-approval changes
- Ph. Eur. and USP monographs for biotechnological products
- EMA and FDA guidelines on similar biological medicinal products

### Related records

- `white.microbial_fermentation`
- `white.bioprocess_engineering`
- `yellow.precision_fermentation`
- `red.antibody_engineering`
- `red.gene_therapy`
- `red.vaccine_development`
- `purple.regulatory_affairs`
- `purple.biotechnology_patents`

### Cross-references

- [white.microbial_fermentation](../white/microbial_fermentation.md)
- [white.bioprocess_engineering](../white/bioprocess_engineering.md)
- [yellow.precision_fermentation](../yellow/precision_fermentation.md)
- [red.antibody_engineering](antibody_engineering.md)
- [red.gene_therapy](gene_therapy.md)
- [red.vaccine_development](vaccine_development.md)
- `purple.regulatory_affairs` (branch not written yet)
- `purple.biotechnology_patents` (branch not written yet)
