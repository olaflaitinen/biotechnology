<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/red/gene_therapy/.
  Edit the source and run `make docs`.
-->

[Red Biotechnology](index.md) / **Gene Therapy**

## Gene Therapy

`red.gene_therapy`

Treating disease by adding, silencing, replacing or editing genetic material inside a patient's cells.

### What it is

Gene therapy is the deliberate modification of nucleic acid inside a patient in order to produce a therapeutic effect. Four strategies are in clinical use or late-stage development. Gene addition supplies a working copy of a gene without removing the faulty one, and is the approach used in most approved products. Gene silencing suppresses a harmful transcript with antisense oligonucleotides or short interfering RNA. Gene editing rewrites the genome in place using nuclease, base-editing or prime-editing systems. Gene regulation changes how much of an existing gene is expressed without altering its sequence. Delivery is either in vivo, where the vector is infused or injected into the patient, or ex vivo, where cells are removed, modified in a clean room and returned. The dominant in vivo vehicle is the adeno-associated virus, chosen for low pathogenicity and long episomal persistence in post-mitotic tissue; the dominant ex vivo vehicle is the lentivirus, chosen because it integrates into the genome and is therefore inherited by every daughter cell. The binding constraint is not efficacy but delivery: getting enough vector to the right tissue, in a patient whose immune system may already recognise that vector, at a manufacturing cost that a health system can absorb.

### In plain language

Your body follows a set of written instructions stored in your cells, called DNA. In some illnesses one of those instructions has a mistake in it, so the body cannot make something it needs. Gene therapy puts a corrected instruction into the cells, usually by hiding it inside a harmless virus that acts as a delivery van. If it works, the body starts producing the missing part on its own, sometimes after a single treatment. The change is made only in the treated person; it is not passed on to their children.

### An analogy

Imagine a factory working from a printed manual with one page smudged beyond reading, so a single component never gets made. Gene therapy does not rebuild the factory. It slips a clean copy of that one page into the manual, and the production line starts again. The hard part is not printing the page - it is getting it into every relevant manual in a building with several trillion rooms.

### Why it matters

Most of the roughly seven thousand known rare diseases are caused by a fault in a single gene, and for the great majority there has never been any treatment that addresses the cause rather than the symptoms. Gene therapy is the first approach that can, in principle, treat them at the source, and in several cases a single infusion has replaced a lifetime of transfusions or injections. It also raises hard questions about price - list prices above two million euro per patient are now routine - and about equity, since the health systems with the most patients are often those least able to pay, and almost no manufacturing capacity exists outside a handful of high-income countries.

### Applications

- Adeno-associated virus therapy for inherited retinal dystrophy
- Lentiviral gene addition for beta-thalassaemia and sickle cell disease
- Ex vivo correction of severe combined immunodeficiency
- Antisense oligonucleotides for spinal muscular atrophy
- In vivo base editing to lower lipoprotein cholesterol
- Oncolytic viruses engineered to replicate in and lyse tumour cells
- AAV micro-dystrophin transfer in Duchenne muscular dystrophy
- RNA interference therapeutics for hereditary transthyretin amyloidosis
- AAV factor VIII and factor IX transfer in haemophilia

### Technologies

- Adeno-associated virus (AAV) capsid serotypes and engineered variants
- Third-generation self-inactivating lentiviral vectors
- Lipid nanoparticle encapsulation of messenger and guide RNA
- Non-viral transposon systems such as Sleeping Beauty and piggyBac
- CRISPR-Cas9 nuclease editing with homology-directed repair
- Cytosine and adenine base editors that make no double-strand break
- Prime editing with a reverse-transcriptase-fused nickase
- Tissue-specific and inducible promoter cassettes
- Codon optimisation and intron inclusion for expression strength
- Suspension HEK293 triple-transfection vector production
- Sf9 baculovirus expression for large-scale AAV manufacture
- Affinity and ion-exchange purification with full-empty capsid separation

### Challenges

- Pre-existing neutralising antibodies exclude a large share of patients from adeno-associated virus therapy, and there is no accepted way to redose someone who has been treated once
- Insertional mutagenesis risk with integrating vectors, demonstrated in early trials and still a lifelong monitoring obligation
- Off-target editing and unintended large deletions or chromosomal rearrangements that short-read sequencing can miss
- Durability of expression in dividing tissue is measured in years rather than decades, and no product has yet been observed over a full lifespan
- Manufacturing yield and cost of goods at commercial scale, which set the floor under prices that already exceed two million euro per patient
- Payer and reimbursement models built for chronic dosing rather than for a single curative administration
- Almost no manufacturing or administration capacity outside a small number of high-income countries, so eligibility is decided by geography

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Vector genome dose | `vg/kg` | vector genomes per kilogram body weight | 1e11 - 2e14 vg/kg | REVIEWED |
| Vector copy number per cell | `VCN` | copies per diploid genome | 0.3 - 4 copies/genome | CONSENSUS |
| Transduction efficiency | `TE` | per cent of target cells | 10 - 90 % | CONSENSUS |
| Editing efficiency | `indel%` | per cent of alleles carrying the intended edit | 20 - 90 % | REVIEWED |
| Full-to-empty capsid ratio | `F:E` | dimensionless | > 0.7 full | REVIEWED |
| Multiplicity of infection | `MOI` | transducing units per cell | 1 - 100 TU/cell | CONSENSUS |

### History

- **1972** - Friedmann and Roblin propose gene therapy for human genetic disease
- **1990** - First authorised human gene transfer trial, for adenosine deaminase deficiency
- **1999** - Death of a trial participant halts the field and reshapes oversight
- **2003** - Leukaemias in an X-linked SCID trial reveal insertional mutagenesis
- **2012** - Glybera becomes the first gene therapy approved in the European Union
- **2017** - Luxturna approved for inherited retinal dystrophy in the United States
- **2019** - Zolgensma approved for spinal muscular atrophy
- **2023** - First CRISPR-based therapy authorised, for sickle cell disease and beta-thalassaemia
- **2024** - In vivo base editing enters registrational trials for hypercholesterolaemia

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | REGULATED |
| Scale | BENCH |
| Regulatory status | AUTHORISED |
| Domains | HEALTH |
| SDGs | 3, 9, 10 |

### Regulations

- EU Regulation (EC) No 1394/2007 on advanced therapy medicinal products
- EU Directive 2001/83/EC on medicinal products for human use
- EU Regulation (EC) No 726/2004 establishing the centralised procedure, under which every advanced therapy must be authorised
- EU Directive 2001/18/EC on the deliberate release of genetically modified organisms, which applies in parallel where the vector is a GMO
- EU Directive 2009/41/EC on the contained use of genetically modified micro-organisms, applying to the manufacturing site
- EU Regulation (EU) No 536/2014 on clinical trials on medicinal products
- US Public Health Service Act section 351 biologics licence
- US FDA 21 CFR Part 1271 on human cells, tissues and cellular products
- ICH E6(R2) Good Clinical Practice
- Council of Europe Convention on Human Rights and Biomedicine, which prohibits interventions modifying the germline

### Standards

- EU GMP Part IV, Guidelines on Good Manufacturing Practice specific to advanced therapy medicinal products
- EU GMP Annex 1 on the manufacture of sterile medicinal products
- Ph. Eur. 5.14 gene transfer medicinal products for human use
- USP <1047> gene therapy product quality
- ICH Q5A(R2) viral safety evaluation of biotechnology products
- ISO 20387 biotechnology: biobanking general requirements
- ISO 9001 quality management systems, for supporting operations

### Related records

- `red.cell_therapy`
- `red.pharmaceutical_biotechnology`
- `green.agricultural_genome_editing`
- `gold.computational_drug_discovery`
- `gold.nanobiotechnology`
- `purple.bioethics`
- `purple.regulatory_affairs`
- `purple.genetic_data_privacy`

### Cross-references

- [red.cell_therapy](cell_therapy.md)
- [red.pharmaceutical_biotechnology](pharmaceutical_biotechnology.md)
- [green.agricultural_genome_editing](../green/agricultural_genome_editing.md)
- `gold.computational_drug_discovery` (branch not written yet)
- `gold.nanobiotechnology` (branch not written yet)
- `purple.bioethics` (branch not written yet)
- `purple.regulatory_affairs` (branch not written yet)
- `purple.genetic_data_privacy` (branch not written yet)
