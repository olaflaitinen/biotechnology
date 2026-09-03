<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/red/cell_therapy/.
  Edit the source and run `make docs`.
-->

[Red Biotechnology](index.md) / **Cell Therapy**

## Cell Therapy

`red.cell_therapy`

Using living cells as the therapeutic agent, autologous or allogeneic, often after genetic modification to redirect their function.

### What it is

In a cell therapy the medicine is a population of living cells. The source may be autologous, harvested from the patient who will receive them, or allogeneic, taken from a healthy donor. Where the cells are also gene-modified the product is regulated as a gene therapy medicinal product in the European Union, which is why the two fields are so often conflated; the distinction kept here is that this record concerns the sourcing, expansion, potency and delivery of the cells themselves. Three families dominate clinical practice. Haematopoietic stem cell transplantation, in use since the 1950s, replaces a patient's entire blood-forming system. Adoptive immune cell transfer arms T cells or natural killer cells against a chosen antigen, most famously through a chimeric antigen receptor that fuses an antibody binding domain to intracellular signalling domains. Stromal and progenitor cell products, typically mesenchymal, act mainly by secreting immunomodulatory factors rather than by engrafting at all. The manufacturing problem is unlike that of any other medicine: an autologous product is a batch of one, made under time pressure for a named patient whose disease is progressing, and every release assay must complete before the cells lose potency. Allogeneic and induced pluripotent stem cell derived products aim to convert this bespoke model into a conventional inventory one, at the cost of having to suppress or engineer away immune rejection.

### In plain language

Doctors take living cells - usually white blood cells drawn from the patient - and treat them in a laboratory so that they can recognise and attack a disease they previously ignored. The cells are grown until there are enough of them and then infused back into the same person, where they keep working, dividing and hunting for as long as they survive. The treatment is a living thing rather than a chemical, which is why it can keep acting for years after a single infusion, and also why it cannot simply be made in advance and kept on a shelf.

### An analogy

It is closer to retraining a police force than to spraying a pesticide. The officers already exist and already patrol the streets; they simply were not looking for this particular offender. Cell therapy sends them on a course and returns them to the same streets, where they continue working, recruit colleagues, and remain on duty long after the training budget has been spent.

### Why it matters

For some blood cancers that had exhausted every other option, a single CAR-T infusion produces lasting remission in roughly four out of ten patients. No chemical drug had achieved a result in that category. The counterweight is cost and access: manufacturing is bespoke and cannot benefit from ordinary economies of scale, the list price sits in the high hundreds of thousands of euro, and treatment can only be given at accredited centres, so geography decides eligibility as much as biology does. Solid tumours, which are most cancers, remain largely out of reach.

### Applications

- Allogeneic haematopoietic stem cell transplantation for leukaemia and inherited marrow failure
- CD19-directed CAR-T therapy for B-cell lymphoma and leukaemia
- BCMA-directed CAR-T therapy for multiple myeloma
- Tumour-infiltrating lymphocyte therapy for advanced melanoma
- Virus-specific T cells for post-transplant infection
- Mesenchymal stromal cells for steroid-refractory graft-versus-host disease
- Islet cell transplantation in brittle type 1 diabetes
- Induced pluripotent stem cell derived cardiomyocyte and retinal grafts
- Allogeneic off-the-shelf natural killer cell products

### Technologies

- Leukapheresis and mononuclear cell collection
- Magnetic bead and column-based cell selection
- Cord blood and donor registry sourcing for allogeneic products
- Chimeric antigen receptor design and signalling domain selection
- Lentiviral and retroviral transduction of primary T cells
- CRISPR knockout of TCR and HLA loci for allogeneic products
- Serum-free expansion media with defined cytokine cocktails
- Closed-system automated cell processing platforms
- Rocking-motion and gas-permeable expansion vessels
- Potency assays based on cytotoxicity and cytokine release
- Controlled-rate freezing and vapour-phase liquid nitrogen storage
- Chain-of-identity and chain-of-custody tracking systems
- Induced pluripotent stem cell reprogramming and directed differentiation

### Challenges

- Poor efficacy in solid tumours, where the product must traffic, penetrate and survive a hostile microenvironment rather than meet its target in the bloodstream
- Antigen escape, in which the tumour simply stops expressing the single marker the product was engineered to see
- Cytokine release syndrome and immune effector cell associated neurotoxicity, both requiring intensive care capability on site
- Manufacturing failure rate in heavily pre-treated patients whose T cells are exhausted before collection
- Potency assay design that actually predicts clinical benefit rather than merely demonstrating the cells are alive
- Vein-to-vein turnaround time of two to five weeks, during which the disease progresses and some patients become ineligible
- A cost structure that resists conventional economies of scale, because doubling output means doubling clean-room suites and operators
- Restriction to accredited centres, which makes access a question of postcode as much as of diagnosis

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Cell dose | `D_cell` | CAR-positive cells per kilogram body weight | 1e6 - 5e6 CAR-positive T cells/kg | REVIEWED |
| Cell viability | `V` | per cent viable | > 70 % at release | CONSENSUS |
| Population doubling level | `PDL` | cumulative doublings | 10 - 30 before senescence in primary T cells | CONSENSUS |
| Transduction efficiency | `TE` | per cent CAR-positive cells | 20 - 60 % | CONSENSUS |
| Fold expansion | `FE` | dimensionless multiple | 50 - 1000 x over 7 - 14 days | REVIEWED |
| Vector copy number per cell | `VCN` | copies per diploid genome | < 5 copies/genome as a safety limit | CONSENSUS |

### History

- **1956** - First successful bone marrow transplant, between identical twins
- **1957** - Thomas reports six unrelated-donor marrow infusions; none survives
- **1968** - First successful allogeneic transplant for severe combined immunodeficiency, using a matched sibling
- **1989** - Gross, Waks and Eshhar describe the first chimeric antigen receptor
- **1990** - Nobel Prize in Physiology or Medicine awarded for organ and cell transplantation
- **2002** - Second-generation CAR designs add a costimulatory domain
- **2010** - Durable complete remission reported in chronic lymphocytic leukaemia after CD19 CAR-T therapy
- **2017** - Tisagenlecleucel approved: the first CAR-T product anywhere
- **2021** - First BCMA-directed CAR-T approvals for multiple myeloma
- **2023** - Regulators begin requiring long-term follow-up for secondary malignancy after CAR-T therapy
- **2024** - Allogeneic and in vivo CAR platforms enter late-stage trials

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | REGULATED |
| Scale | BENCH |
| Regulatory status | AUTHORISED |
| Domains | HEALTH |
| SDGs | 3, 10 |

### Regulations

- EU Regulation (EC) No 1394/2007 on advanced therapy medicinal products
- EU Directive 2001/83/EC on medicinal products for human use
- EU Regulation (EC) No 726/2004 centralised authorisation procedure
- EU Directive 2004/23/EC on standards of quality and safety for human tissues and cells
- EU Directive 2006/17/EC on donation, procurement and testing
- EU Directive 2006/86/EC on traceability and serious adverse reactions
- EU Directive 2009/41/EC on contained use of genetically modified micro-organisms
- US FDA 21 CFR Part 1271, the risk-based HCT/P framework
- US Public Health Service Act section 351 for more-than-minimally manipulated products
- EU Regulation (EU) No 536/2014 on clinical trials
- ICH E6(R2) Good Clinical Practice

### Standards

- JACIE standards for haematopoietic cell therapy in Europe
- FACT standards for cellular therapy in North America
- EU GMP Part IV for advanced therapy medicinal products
- EU GMP Annex 1 manufacture of sterile medicinal products
- ISO 14644 cleanrooms and controlled environments
- ISO 20387 biotechnology: biobanking general requirements
- ISO 21973 general requirements for transportation of cells for therapeutic use
- Ph. Eur. 5.14 and general chapters on cell-based preparations
- USP <1046> cellular and tissue-based products

### Related records

- `red.gene_therapy`
- `red.regenerative_medicine`
- `red.antibody_engineering`
- `red.pharmaceutical_biotechnology`
- `purple.clinical_trial_ethics`
- `purple.regulatory_affairs`
- `purple.bioethics`

### Cross-references

- [red.gene_therapy](gene_therapy.md)
- [red.regenerative_medicine](regenerative_medicine.md)
- [red.antibody_engineering](antibody_engineering.md)
- [red.pharmaceutical_biotechnology](pharmaceutical_biotechnology.md)
- `purple.clinical_trial_ethics` (branch not written yet)
- `purple.regulatory_affairs` (branch not written yet)
- `purple.bioethics` (branch not written yet)
