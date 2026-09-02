# Glossary

Every term used in this library, defined in both registers.

**Technical** is the definition a specialist would recognise.
**Plain** is the definition for a reader with no scientific training - the
register that makes this library usable by the people who decide about
biotechnology without practising it.

This document is the human-readable rendering of
`src/biotechnology/glossary/`, which is the machine-readable source of truth.
Every `glossary` key in every subtype's `linkage.py` resolves here, and the
integrity suite fails the build if one does not.

Terms are grouped by field rather than alphabetised, because a reader meeting
them for the first time meets them in clusters. Use your browser's find
function for a specific term.

---

## Molecular biology and genetics

| Term | Technical | Plain |
|------|-----------|-------|
| **allele** | One of the alternative sequences of a gene at a given locus. | One of the possible versions of a gene. You inherit one from each parent. |
| **amplification** | Exponential copying of a defined nucleic acid region, doubling per cycle. | Making millions of copies of one specific piece of genetic material so it can be detected. |
| **base editing** | Chemical conversion of one base pair into another without a double-strand break. | Changing a single letter of DNA without cutting the strand. |
| **capsid** | The protein shell of a virus particle, enclosing its genome. | The protein container a virus keeps its genetic material in. |
| **CRISPR** | A bacterial adaptive immune system repurposed as a programmable, RNA-guided DNA endonuclease. | A tool borrowed from bacteria that can be pointed at a chosen spot in DNA and cut it there. |
| **episome** | Genetic material persisting in the nucleus without integrating into a chromosome. | Genetic material that sits alongside the cell's own DNA rather than joining it. |
| **germline** | Cells whose genetic material is transmitted to offspring. | Egg and sperm cells. Changes here would be passed to children. |
| **guide RNA** | Short RNA directing a CRISPR nuclease to a complementary genomic target. | The address label that tells the CRISPR tool where to go. |
| **homology-directed repair** | Template-dependent repair of a double-strand break, giving a precise edit. | The cell's careful repair mode: it copies from a template, so the result is exact. |
| **non-homologous end joining** | Template-free repair of a double-strand break; error-prone, produces indels. | The cell's quick repair mode: it sticks the ends together and often loses a few letters. |
| **off-target effect** | Activity of a targeted tool at an unintended, similar sequence. | The tool acting somewhere it was not meant to, because that place looks similar. |
| **plasmid** | A small circular DNA molecule replicating independently of the chromosome. | A small loop of DNA that bacteria carry and share, used as a container for genes. |
| **polymorphism** | Sequence variation present in a population above a threshold frequency. | A spot in the genetic code where people commonly differ. |
| **primer** | A short oligonucleotide defining where amplification begins. | A short piece of DNA that marks the starting point for copying. |
| **probe** | A labelled oligonucleotide reporting the presence of a target sequence. | A tagged piece of DNA that lights up when it finds its match. |
| **promoter** | A regulatory sequence controlling when and where a gene is transcribed. | The switch that decides when a gene is turned on, and in which tissue. |
| **somatic cell** | Any cell of the body other than a germ cell. | Any cell except egg and sperm. Changes here affect only that person. |
| **transgene** | A gene deliberately introduced into an organism from another source. | A gene added on purpose, usually from a different species. |
| **transduction** | Delivery of genetic material into a cell by a viral vector. | Using a virus as a delivery van to carry genetic material into a cell. |
| **vector** | The vehicle carrying genetic material into a cell - viral or non-viral. | Whatever is used to carry genetic material into a cell. Often a harmless virus. |

---

## Medicine and therapeutics

| Term | Technical | Plain |
|------|-----------|-------|
| **advanced therapy medicinal product** | An EU regulatory class covering gene therapy, somatic cell therapy and tissue-engineered products. | The European legal category for medicines made of genes, cells or engineered tissue. |
| **adverse drug reaction** | A harmful, unintended response at a normal therapeutic dose. | A harmful side effect at an ordinary dose. |
| **allogeneic** | Derived from a genetically different individual of the same species. | Coming from a donor rather than from the patient. |
| **autologous** | Derived from the individual who will receive it. | Coming from the patient's own body. |
| **biologic** | A medicine whose active ingredient is produced by a living system. | A medicine grown in living cells rather than mixed in a chemical plant. |
| **biosimilar** | A biologic demonstrated highly similar to an authorised reference biologic. | A close copy of a grown medicine. Not identical, because living factories vary. |
| **chimeric antigen receptor** | An engineered receptor fusing an antibody binding domain to intracellular signalling domains. | A custom-built sensor added to an immune cell so it recognises a target it previously ignored. |
| **cytokine release syndrome** | Systemic inflammatory response from large-scale immune activation. | A dangerous, whole-body inflammatory reaction when many immune cells fire at once. |
| **engraftment** | Establishment and sustained function of transferred cells in a recipient. | Transplanted cells settling in and starting to work. |
| **potency assay** | A test measuring the biological activity that produces the clinical effect. | A test proving the medicine can still do the thing it is supposed to do. |
| **therapeutic index** | The ratio between a toxic dose and an effective dose. | How much room there is between a dose that helps and a dose that harms. |

---

## Immunology and vaccines

| Term | Technical | Plain |
|------|-----------|-------|
| **adjuvant** | A substance enhancing the immune response to a co-administered antigen. | An ingredient that makes a vaccine work better by getting the immune system's attention. |
| **antigen** | A molecule recognised by the adaptive immune system. | The part of a germ the immune system learns to recognise. |
| **attenuation** | Reduction of virulence while retaining the ability to provoke immunity. | Weakening a germ so it teaches the immune system without causing disease. |
| **correlate of protection** | A measurable immune marker statistically predicting protection. | A measurement that reliably tells you someone is protected. |
| **herd immunity** | Indirect protection of susceptible individuals when enough of a population is immune. | When enough people are immune that the germ cannot spread, protecting those who are not. |
| **neutralising antibody** | An antibody that blocks a pathogen from entering cells. | An antibody that stops a germ getting into cells at all, rather than just marking it. |
| **seroconversion** | Development of detectable specific antibodies. | The point at which a blood test can show you have responded. |

---

## Bioprocess and industry

| Term | Technical | Plain |
|------|-----------|-------|
| **bioreactor** | A vessel providing controlled conditions for cells or enzymes to work in. | A tank that keeps living cells at exactly the right temperature, acidity and oxygen. |
| **cell bank** | A characterised, frozen, tested stock of a production cell line. | A frozen library of the exact cells a medicine is made from, so every batch starts identically. |
| **fed-batch** | A culture mode in which nutrients are added during the run without harvest. | Topping up the food during a run instead of starting a fresh tank. |
| **fermentation** | Cultivation of microorganisms at scale to make a product. | Growing microbes on purpose so they manufacture something for us. |
| **glycosylation** | Enzymatic attachment of sugar chains to a protein. | Sugar decorations added to a protein, which change how long it lasts and how well it works. |
| **good manufacturing practice** | The regulated quality system governing medicine manufacture. | The legally enforced rulebook for making medicines safely and consistently. |
| **titre** | Concentration of product in a culture. | How much medicine there is in each litre of tank. |

---

## Agriculture and breeding

| Term | Technical | Plain |
|------|-----------|-------|
| **backcross** | Crossing a hybrid to one parent line to recover that parent's genome. | Breeding a plant back to its parent repeatedly to keep one new trait and nothing else. |
| **doubled haploid** | A plant produced by chromosome doubling of a haploid cell; instantly homozygous. | A plant made genetically uniform in one step instead of six generations. |
| **heritability** | The fraction of observed variation attributable to genetic variation. | How much of the difference between individuals is inherited rather than caused by conditions. |
| **landrace** | A locally adapted, genetically diverse traditional variety. | An old local variety, not uniform, adapted over generations to one place. |
| **quantitative trait locus** | A genomic region statistically associated with a continuous trait. | A stretch of DNA that has some influence on a trait such as yield or height. |
| **somaclonal variation** | Genetic and epigenetic change arising during tissue culture. | Unintended changes that creep in when plants are grown from cells in jars for too long. |
| **totipotency** | The capacity of a single cell to regenerate a complete organism. | The ability of one plant cell to grow into a whole new plant. |

---

## Environment and ecology

| Term | Technical | Plain |
|------|-----------|-------|
| **bioaugmentation** | Adding selected organisms to install a capability a community lacks. | Introducing microbes that can do a job the ones already there cannot. |
| **bioremediation** | Using organisms to degrade or immobilise contaminants. | Using living things to clean up pollution. |
| **eutrophication** | Nutrient over-enrichment of water, causing algal blooms and oxygen depletion. | Too much fertiliser reaching water, causing algae to bloom and fish to suffocate. |
| **rhizosphere** | The soil zone immediately surrounding and influenced by a root. | The thin layer of soil right around a root, where most of the action is. |
| **symbiosis** | A persistent close association between organisms of different species. | Two different living things sharing a life, usually to mutual benefit. |

---

## Governance, law and ethics

| Term | Technical | Plain |
|------|-----------|-------|
| **antimicrobial resistance** | Loss of susceptibility of a microorganism to a drug that previously worked. | Germs becoming immune to the medicines we use against them. |
| **biosafety** | Protection of people and the environment from unintended exposure to biological agents. | Stopping dangerous organisms escaping by accident. |
| **biosecurity** | Protection of biological materials from theft, loss or deliberate misuse. | Stopping dangerous organisms being taken or used on purpose. |
| **coexistence** | Measures allowing GM and non-GM farming in the same region. | Rules that let farmers who use modified crops and farmers who do not work side by side. |
| **dual-use research of concern** | Legitimate research that could be misapplied to cause harm. | Honest research that could also be used to do damage. |
| **GMO** | An organism whose genetic material has been altered in a way not occurring naturally. | An organism whose genes have been deliberately changed in the laboratory. |
| **one health** | The recognition that human, animal and environmental health form one system. | The idea that human, animal and environmental health cannot be dealt with separately. |
| **prior informed consent** | Agreement obtained after full disclosure of the intended use of a genetic resource. | Permission given by a country or community after being told exactly what will be done. |
| **substantial equivalence** | The principle of assessing a new food by comparison with an established counterpart. | Judging a new food by how it differs from the familiar version it replaces. |
| **zoonosis** | An infectious disease transmissible between animals and humans. | A disease that jumps between animals and people. |

---

## Measurement and statistics

| Term | Technical | Plain |
|------|-----------|-------|
| **limit of detection** | The lowest concentration reliably distinguishable from zero. | The smallest amount a test can honestly say it has found. |
| **prevalence** | The proportion of a population with a condition at a point in time. | How common something is right now. |
| **sensitivity** | The proportion of true positives correctly identified. | Of the people who have it, how many the test finds. |
| **specificity** | The proportion of true negatives correctly identified. | Of the people who do not have it, how many the test correctly clears. |
| **positive predictive value** | The probability of disease given a positive test - depends on prevalence. | If your test is positive, the chance you actually have it. This drops sharply when a disease is rare, however good the test. |
| **variant of uncertain significance** | A sequence variant whose clinical consequence is unknown. | A genetic difference nobody yet knows the meaning of. |

---

## Adding a term

Add it to `src/biotechnology/glossary/`, not to this file - this document is
generated from that package. Both registers are required: a technical
definition alone will be rejected in review, because the plain definition is
the one that makes the library useful to the audience it exists for.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`STYLE_GUIDE.md`](STYLE_GUIDE.md).
