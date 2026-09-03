<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/red/regenerative_medicine/.
  Edit the source and run `make docs`.
-->

[Red Biotechnology](index.md) / **Regenerative Medicine and Tissue Engineering**

## Regenerative Medicine and Tissue Engineering

`red.regenerative_medicine`

Restoring the structure and function of damaged tissue by combining cells, scaffolds and signalling molecules.

### What it is

Regenerative medicine aims to restore lost tissue function rather than to compensate for it. Tissue engineering, its main engineering arm, builds constructs from three components, and removing any one of them causes failure. Cells may be primary, expanded from a biopsy, or derived from induced pluripotent stem cells. Scaffolds may be synthetic polymers, natural polymers such as collagen and alginate, or decellularised extracellular matrix that retains the architecture of the original organ. Signals include soluble growth factors, immobilised peptide motifs, and mechanical conditioning in a bioreactor, since many tissues will not mature unless they are loaded while they grow. Scaffold stiffness is itself a signal: identical stem cells differentiate towards bone on a hard substrate and towards nerve on a soft one. Simple avascular tissues have reached clinical use because they can survive on diffusion alone: skin, cartilage, cornea and bladder. Thick, metabolically demanding organs have not. The binding constraint is physical, not biological. Oxygen diffuses roughly one hundred to two hundred micrometres from a capillary before it is exhausted, so no construct thicker than about two hundred micrometres survives without a perfusable vascular network. Two lines of work address this: three-dimensional bioprinting of sacrificial channels that are flushed out to leave plumbing behind, and organoids, which are self-organising miniature tissues used today mainly as disease models and drug-screening platforms rather than as implants.

### In plain language

If you break a bone it heals, but if you lose a large piece of liver or a heart valve, the body cannot rebuild it. Regenerative medicine supplies what is missing: living cells, a supporting framework for them to grow on, and chemical instructions telling them what to become. Thin tissues such as skin and cartilage are already made this way and used in hospitals. Whole complex organs are not, and the reason is simpler than most people expect. Oxygen can only soak about a fifth of a millimetre into living tissue before it runs out. Anything thicker needs its own blood vessels, and building a working network of blood vessels from scratch is the problem the field has not yet solved.

### An analogy

Think of planting a hedge rather than building a fence. The fence is a hip replacement: manufactured, inert, and eventually worn out. The hedge is regenerative medicine: you supply seedlings, a trellis and the right conditions, and the living thing grows into the gap and maintains itself. The comparison holds all the way down to the failure mode. A hedge planted too thick dies in the middle, because water never reaches the centre, and that is precisely what happens to a tissue construct without blood vessels.

### Why it matters

Organ transplantation is limited by donors, not by surgical skill. Tens of thousands of people are on European waiting lists and a significant number die waiting. Engineered tissue would remove the donor constraint and the lifelong immunosuppression that follows a transplant. Even short of that, organoids are already changing drug development by letting a compound be tested on human tissue, and on tissue from a specific patient, before anyone is dosed. Two costs belong in the same paragraph. The first is that the field has promised grown organs for three decades and delivered thin tissues, which has made honest assessment of its timelines difficult. The second is more serious: unproven stem cell clinics sell unregulated injections to desperate patients in jurisdictions with weak oversight. People have been permanently blinded by intraocular injections marketed as stem cell therapy, and people have died. The gap between what this field can do and what is sold in its name is itself a public health problem.

### Applications

- Cultured epidermal autografts for extensive burns
- Limbal stem cell grafts for corneal surface restoration after chemical injury
- Autologous chondrocyte implantation for cartilage defects
- Decellularised heart valve and vascular grafts
- Scaffold-guided bone regeneration in maxillofacial and dental surgery
- Acellular dermal matrices in reconstructive surgery
- Autologous chondrocyte and keratinocyte suspensions applied as sprays
- Bioprinted skin and cartilage constructs in clinical trials
- Engineered airway and urethral segments in small series
- Patient-derived organoids for drug response prediction
- Organoid disease models for inherited disorders
- Organ-on-a-chip systems accepted in some regulatory submissions in place of animal data

### Technologies

- Induced pluripotent stem cell reprogramming and directed differentiation
- Primary cell expansion from a small biopsy
- Mesenchymal stromal cell isolation and expansion
- Decellularisation with detergents and perfusion, retaining native architecture
- Electrospun nanofibre scaffolds
- Hydrogels with independently tunable stiffness and degradation rate
- Synthetic degradable polyesters with controlled resorption
- Growth-factor controlled release from the scaffold itself
- Immobilised peptide motifs presenting adhesion cues
- Perfusion and mechanical-conditioning bioreactors that load tissue while it matures
- Substrate stiffness as a differentiation cue in its own right
- Extrusion, inkjet and laser-assisted three-dimensional bioprinting
- Sacrificial ink strategies that leave perfusable channels behind
- Prevascularisation by co-culture with endothelial cells
- Microfluidic organ-on-a-chip devices, which sidestep the limit by staying thin

### Challenges

- Vascularisation of constructs thicker than about two hundred micrometres, which is a diffusion limit rather than a biological one and cannot be engineered around without building plumbing
- Innervation and functional integration with host tissue, since a graft that survives but is not wired in restores structure without function
- Matching scaffold degradation rate to the rate at which the patient deposits their own matrix, where too fast collapses and too slow blocks
- Scale-up and reproducibility of constructs that are shaped for one patient's anatomy and cannot be made to inventory
- Potency assays for a product whose intended effect is structural, where there is often no measurable activity to release against
- Teratoma risk from residual undifferentiated pluripotent cells, which requires a purification step sensitive enough to detect a rare cell in millions
- Reimbursement for a one-off structural repair whose benefit accrues over decades, assessed by systems built for recurring treatment
- Unproven stem cell clinics operating outside regulation, which have permanently blinded and in some cases killed patients, and which trade on the credibility of the legitimate field

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Oxygen diffusion limit | `L_O2` | micrometres from the nearest capillary | 100 - 200 um | CONSENSUS |
| Young modulus of the construct | `E` | pascals, spanning ten orders of magnitude across tissues | 0.5 kPa for brain to 20 GPa for cortical bone | CONSENSUS |
| Scaffold porosity | `phi` | void volume fraction, dimensionless | 0.6 - 0.9 | CONSENSUS |
| Mean pore diameter | `d_pore` | micrometres | 100 - 500 um for bone, 20 - 125 um for skin | REVIEWED |
| Cell seeding density | `rho_seed` | cells per cubic centimetre of scaffold | 1e6 - 1e8 cells/cm^3 | REVIEWED |
| Residual double-stranded DNA | `dsDNA` | nanograms per milligram dry weight | < 50 ng/mg | CONSENSUS |
| Scaffold degradation half-life | `t_deg` | weeks | 2 weeks for skin to 24 months for bone | REVIEWED |
| Construct cell viability | `V` | per cent viable cells | > 80 % at release, measured through the depth | CONSENSUS |

### History

- **1975** - Rheinwald and Green establish serial cultivation of human keratinocytes
- **1981** - First cultured epidermal autografts used on burn patients
- **1987** - The term tissue engineering is formalised at a National Science Foundation workshop
- **1993** - Langer and Vacanti publish the cells, scaffolds and signals framework
- **1997** - A cartilage construct grown in the shape of a human ear on a mouse is widely publicised
- **1998** - Human embryonic stem cell lines derived
- **2006** - Yamanaka reprograms adult cells to pluripotency
- **2009** - Intestinal organoids grown from single stem cells
- **2014** - Stimulus-triggered acquisition of pluripotency papers retracted
- **2015** - Bioprinted vascular channels perfused in vitro
- **2017** - Patients permanently blinded by unregulated intraocular stem cell injections
- **2021** - Organ-on-a-chip data accepted in some regulatory submissions

### Governance

| Field | Value |
|---|---|
| Maturity | PILOT |
| Risk tier | REGULATED |
| Scale | BENCH |
| Regulatory status | AUTHORISED |
| Domains | HEALTH, MATERIALS |
| SDGs | 3, 9 |

### Regulations

- EU Regulation (EC) No 1394/2007 on advanced therapy medicinal products, which defines the tissue-engineered product category
- EU Directive 2001/83/EC on medicinal products for human use
- EU Regulation (EC) No 726/2004 centralised authorisation procedure
- EU hospital exemption under Regulation 1394/2007 Article 28, permitting non-routine preparation for an individual patient under national authorisation, which is both a genuine clinical need and the widest gap in the regime
- EU Regulation (EU) 2017/745 on medical devices, applied to the scaffold component of a combined product
- EU Directive 2004/23/EC on standards of quality and safety for human tissues and cells
- EU Directive 2006/17/EC on donation, procurement and testing
- EU Directive 2006/86/EC on traceability and adverse reaction reporting
- US FDA 21 CFR Part 1271, and the more-than-minimal-manipulation and homologous-use criteria that decide whether a product is a tissue or a regulated medicine
- US Public Health Service Act section 351, applying where those criteria are exceeded
- EU Regulation (EU) No 536/2014 on clinical trials

### Standards

- ISO 10993 series, biological evaluation of medical devices, which governs whether a scaffold is tolerated at all
- ASTM F2150 standard guide for characterisation of scaffolds used in tissue-engineered medical products
- ASTM F2451 assessment of tissue-engineered cartilage products
- ISO 13485 medical devices, quality management systems
- ISO 20387 biotechnology, biobanking general requirements
- ISO 24603 requirements for human and mouse pluripotent stem cells
- International Society for Stem Cell Research guidelines for stem cell research and clinical translation, which explicitly address unproven commercial offerings
- EU GMP Part IV for advanced therapy medicinal products
- EU GMP Annex 1 manufacture of sterile medicinal products
- Ph. Eur. 5.14 and general chapters on cell-based preparations
- USP <1046> cellular and tissue-based products
- ISO 21973 general requirements for transportation of cells for therapeutic use

### Related records

- `red.cell_therapy`
- `red.gene_therapy`
- `white.biopolymers`
- `blue.marine_biomaterials`
- `gold.nanobiotechnology`
- `purple.bioethics`
- `purple.regulatory_affairs`

### Cross-references

- [red.cell_therapy](cell_therapy.md)
- [red.gene_therapy](gene_therapy.md)
- [white.biopolymers](../white/biopolymers.md)
- [blue.marine_biomaterials](../blue/marine_biomaterials.md)
- `gold.nanobiotechnology` (branch not written yet)
- `purple.bioethics` (branch not written yet)
- `purple.regulatory_affairs` (branch not written yet)
