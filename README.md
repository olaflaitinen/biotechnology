<!--
  README.md
  Project front page. Written for three audiences at once, in this order:
    1. someone deciding in ten seconds whether this library is relevant
    2. someone who has decided and wants to use it in the next ten minutes
    3. someone who wants to contribute or cite it
  Everything below the "Documentation" heading is for audience 3.
  SPDX-License-Identifier: EUPL-1.2
-->

<div align="center">

# biotechnology

**A machine-readable, dual-register taxonomy of the ten colour-coded branches of biotechnology.**

*Ten branches | 85 subtypes | every record written twice - once for specialists, once for everybody else.*

[![License: EUPL-1.2](https://img.shields.io/badge/License-EUPL--1.2-blue.svg)](LICENCE)
[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](pyproject.toml)
[![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)](pyproject.toml)
[![Typed](https://img.shields.io/badge/typing-PEP%20561-blue.svg)](src/biotechnology/py.typed)
[![Style](https://img.shields.io/badge/code%20style-ruff-black.svg)](.pre-commit-config.yaml)

</div>

---

## What this is

Biotechnology is conventionally divided into colour-coded branches - red for
medicine, green for agriculture, white for industry, and so on.<sup>[1](#ref-1)</sup>
The scheme is taught in introductory courses and used in policy documents,
funding calls and curricula across Europe. It has never existed as structured,
queryable, citable data.

This library is that data.

```bash
pip install biotechnology
```

```python
import biotechnology as bt

bt.RED.name                                   # 'Red Biotechnology'
bt.RED["gene_therapy"].summary                # one technical sentence
bt.RED["gene_therapy"].plain_language         # the same thing, no jargon
bt.search("CRISPR")                           # ranked hits across all branches
bt.by_sdg(14)                                 # subtypes serving SDG 14
bt.formulas.get("herd_immunity_threshold")(r0=15)   # 0.933
```

Zero dependencies. Pure Python. Everything is an immutable, hashable, fully
typed dataclass, so the whole taxonomy can be passed around, cached, diffed and
serialised without ceremony.

---

## Why it exists

Three problems this library was built to solve.

**1. The colour scheme is undocumented in machine-readable form.**
Ask "which parts of biotechnology are at pilot scale and require
national-agency authorisation?" and there is no dataset to query. Here it is one
line: `[s for s in bt.subtypes() if s.scale is Scale.PILOT and s.risk_tier is RiskTier.REGULATED]`.
Every record carries a stable identifier, a controlled vocabulary placement and
an explicit licence, which is what makes the taxonomy findable, accessible,
interoperable and reusable in the sense the FAIR principles
set out.<sup>[2](#ref-2)</sup> A structured vocabulary changes what can be asked
of a field, which is the lesson of the Gene Ontology: the value was never the
definitions, it was that they became queryable.<sup>[3](#ref-3)</sup>

**2. Technical writing excludes the people who decide about biotechnology.**
Parliamentary committees, procurement officers, journalists and school students
make or shape decisions about this field and are handed prose written for
postdocs. Every record in this library carries a `plain_language` paragraph, an
everyday `analogy` and a `why_it_matters` statement - and the editorial rules
require `why_it_matters` to state the cost or the controversy alongside the
benefit. A record that lists only upside is advertising, and the review process
rejects it.

**3. Descriptive taxonomies are inert.**
This one is not. Every subtype's `metrics` carry symbols, units, typical ranges
and an evidence grade, and most link to a `formulas` module that computes them.
The description of qPCR diagnostics points at the module that calculates
delta-delta Ct; the description of vaccine development points at the one that computes a
herd-immunity threshold from R0.

---

## The ten branches

| Key | Branch | Domain | Subtypes | Colour |
|-----|--------|--------|---------:|--------|
| `red` | Red Biotechnology | Medicine, health care, pharmaceuticals | 8 | `#C62828` |
| `green` | Green Biotechnology | Agriculture, livestock, crop production | 8 | `#2E7D32` |
| `white` | White Biotechnology | Industrial processes, biofuels, biomaterials | 9 | `#ECEFF1` |
| `blue` | Blue Biotechnology | Marine and aquatic resources | 8 | `#1565C0` |
| `yellow` | Yellow Biotechnology | Food production, fermentation, nutrition | 9 | `#F9A825` |
| `grey` | Grey Biotechnology | Environment, waste, ecological balance | 9 | `#607D8B` |
| `brown` | Brown Biotechnology | Arid zones, deserts, degraded land | 8 | `#6D4C41` |
| `gold` | Gold Biotechnology | Bioinformatics, computation, nanobiotechnology | 9 | `#C9A227` |
| `dark` | Dark Biotechnology | Biosecurity, biosafety, misuse risk | 8 | `#212121` |
| `purple` | Purple Biotechnology | Law, ethics, patents, intellectual property | 9 | `#6A1B9A` |

The colour scheme is a convention, not a standard.<sup>[1](#ref-1)</sup> It grew
out of European science-policy writing rather than being designed, so the
boundaries overlap:
an enzyme in a washing powder is white, the same enzyme in a cheese vat is
yellow, and the algorithm that designed it is gold. This library records the
conventional assignment and then makes the overlaps navigable through explicit
cross-references, rather than pretending they do not exist.

---

## Quick start

### Navigate

```python
import biotechnology as bt

bt.branches()                    # all ten, in colour-wheel order
bt.RED, bt.GREEN, bt.WHITE       # branch constants (GRAY aliases GREY)
len(bt.RED)                      # 8 subtypes
list(bt.RED.keys())              # ('pharmaceutical_biotechnology', ...)

bt.get("blue")                          # -> Branch
bt.get("blue.algal_biotechnology")      # -> Subtype
bt.get("medical.gene_therapy")          # branch aliases resolve too
bt.get_subtype("car-t")                 # subtype aliases resolve without a prefix
bt.resolve("nope", default=None)        # non-raising variant
```

Unknown paths raise a typed error that tells you how to fix it:

```python
>>> bt.get("purple.patent")
UnknownSubtypeError: unknown subtype in branch 'purple' 'patent';
did you mean 'biotechnology_patents'?; valid subtypes: biotechnology_patents, bioethics, ...
```

### Read a record, in either register

```python
gt = bt.get("red.gene_therapy")

gt.summary          # technical, one sentence, fits in a table cell
gt.description      # technical, 3-8 sentences
gt.plain_language   # no unexplained jargon, ~14-year-old reading level
gt.analogy          # one everyday image, chosen so its limits are visible
gt.why_it_matters   # consequence, with the cost stated alongside the benefit
```

### Query

```python
from biotechnology import Maturity, RiskTier, Scale, Domain

bt.search("CRISPR")                          # ranked, all fields, all branches
bt.search("enzyme", branch_key="white", limit=3)
bt.by_sdg(14)                                # Life Below Water
bt.by_domain(Domain.ENERGY)
bt.by_maturity(Maturity.RESEARCH)            # what is still in the laboratory
bt.by_risk_tier(RiskTier.RESTRICTED)
bt.related("red.gene_therapy", depth=2)      # graph traversal
bt.timeline(since=1970)                      # merged history of the whole field
```

### Compute

```python
from biotechnology import formulas as f

f.get("herd_immunity_threshold")(r0=15)          # 0.933  -> measles needs 93 %
f.get("vaccine_efficacy")(risk_vax=0.01, risk_ctrl=0.10)
f.get("gc_content")("ATGCGC")
f.get("melting_temperature")("ATGCGCATTAGC")
f.get("monod_growth")(mu_max=0.5, s=2.0, ks=0.5)
f.get("breeders_equation")(h2=0.35, selection_differential=12.0)
```

Every formula module carries its notation, its derivation, its domain of
validity, its unit contract and its citation. See [`NOTATION.md`](NOTATION.md).

### Export

```python
bt.to_dict()                     # plain dicts and lists
bt.to_json(indent=2)
bt.tree()                        # indented text tree
```

```bash
biotechnology export --format json  -o taxonomy.json
biotechnology export --format csv   -o taxonomy.csv
biotechnology export --format dot   -o graph.dot
```

---

## Command line

```bash
biotechnology list                          # the ten branches
biotechnology tree                          # branches with their subtypes
biotechnology show red.gene_therapy         # full record
biotechnology show red.gene_therapy --plain # plain-language view only
biotechnology search fermentation -n 5
biotechnology sdg 14
biotechnology formula herd_immunity_threshold --explain
biotechnology compute gc_content --sequence ATGCGC
biotechnology vocab maturity                # the controlled vocabularies
biotechnology stats                         # headline counts
```

`python -m biotechnology` works identically.

---

## How a record is stored

Every subtype is a **package**, not a module - split into six facet files so
that each can be reviewed by a different specialist without any of them having
to read the others.

```
src/biotechnology/branches/red/gene_therapy/
├── __init__.py       assembles the six facets into one frozen Subtype
├── narrative.py      SUMMARY, DESCRIPTION, PLAIN_LANGUAGE, ANALOGY, WHY_IT_MATTERS
├── practice.py       APPLICATIONS, TECHNOLOGIES, ORGANISMS, TECHNIQUES, CHALLENGES
├── metrics.py        METRICS (symbol, unit, range, evidence grade), FORMULAS
├── history.py        MILESTONES - including the failures
├── governance.py     MATURITY, RISK_TIER, SCALE, DOMAINS, REGULATIONS, STANDARDS
└── linkage.py        SDGS, GLOSSARY, REFERENCES, RELATED
```

A clinical geneticist reviews `narrative.py` and `metrics.py`. A regulatory
affairs professional reviews `governance.py` alone. A science communicator
rewrites the plain-language paragraph without opening a file that contains a
regulation citation. One file per concern means one reviewer per file - and a
correction produces a diff against 150 lines instead of 900.

Full rationale: [`ARCHITECTURE.md`](ARCHITECTURE.md).
Field-by-field specification: [`DATA_MODEL.md`](DATA_MODEL.md).
Editorial rules every record must satisfy: [`STYLE_GUIDE.md`](STYLE_GUIDE.md).

---

## Data integrity

The taxonomy is a graph, and every edge is checked on every commit.

- Each `related`, `formulas`, `organisms`, `techniques`, `glossary` and
  `references` key must resolve. A dead cross-reference **fails the build**,
  so the generated documentation never renders a broken link.
- Each subtype must populate all five narrative fields, at least four
  applications, at least four challenges - **including at least one
  non-technical challenge** - and at least three milestones.
- Each `Metric` must carry a unit and an evidence grade.
- Each SDG number must be an integer in 1-17.
- Controlled vocabularies are enumerations, so a typo is an `ImportError` at
  package load rather than a silently empty query result.

```bash
biotechnology validate --strict     # run the full integrity suite
pytest tests/test_integrity.py
```

---

## A note on the dark branch

`bt.DARK` covers bioterrorism, biological weapons and biosafety risk. It is
documented **exclusively from the protective side**: biosafety containment,
biosecurity governance, dual-use research oversight, gene synthesis screening,
biosurveillance, medical countermeasures, microbial forensics and biological
arms control.

The package contains no operational information about causing harm, and
`tests/test_dark_branch_is_defensive.py` enforces that framing on every commit.
This is a deliberate, documented editorial position, not an oversight.

---

## Security

The attack surface is deliberately small, and every claim below is checked
mechanically on every commit rather than asserted.

| Property | Checked by |
|---|---|
| Zero runtime dependencies | `tools/check_no_dependencies.py` |
| No network access, the package never opens a socket | `security-audit.yml` |
| No `subprocess`, `eval`, `exec`, `pickle`, `marshal` or `ctypes` | `security-audit.yml` |
| No filesystem writes except an explicit export path | `tools/check_no_writes.py` |
| No secrets, publication uses trusted publishing not a token | `gitleaks`, PyPI OIDC |
| Every GitHub Action governed and pinned | `tools/check_action_pinning.py` |
| Every workflow least-privilege, `persist-credentials: false` | `tools/check_workflow_permissions.py` |

Releases carry a **signed tag**, a **build provenance attestation** and a
**CycloneDX SBOM**. Verify one with:

```bash
gh attestation verify biotechnology-0.1.0-py3-none-any.whl    --repo olaflaitinen/biotechnology
```

Full policy in [`SECURITY.md`](SECURITY.md); the reasoning, including the risks
this project **accepts rather than mitigates**, in
[`THREAT_MODEL.md`](THREAT_MODEL.md).

---

## Documentation

| Document | Contents |
|----------|----------|
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Package layout, the six-facet design, import graph |
| [`DATA_MODEL.md`](DATA_MODEL.md) | Every field of every record type, with types and constraints |
| [`STYLE_GUIDE.md`](STYLE_GUIDE.md) | Editorial rules for both registers; how to write a record |
| [`NOTATION.md`](NOTATION.md) | Symbols, units, ASCII conventions, formula documentation contract |
| [`GLOSSARY.md`](GLOSSARY.md) | Every term used in the library, defined in both registers |
| [`BIBLIOGRAPHY.md`](BIBLIOGRAPHY.md) | Every citation key, resolved to a full reference |
| [`FAQ.md`](FAQ.md) | Why ten colours, why these boundaries, what this is not |
| [`ROADMAP.md`](ROADMAP.md) | What is planned, what is explicitly out of scope |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to correct a record, add a subtype, add a formula |
| [`GOVERNANCE.md`](GOVERNANCE.md) | How decisions are made and who makes them |
| [`SECURITY.md`](SECURITY.md) | Vulnerability reporting, dual-use content policy, supply-chain controls |
| [`THREAT_MODEL.md`](THREAT_MODEL.md) | What the risks are, what is done about each, and what is accepted |
| [`CHANGELOG.md`](CHANGELOG.md) | Versioned history, following Keep a Changelog |

Full generated reference, with a page per subtype and per formula, is built
with `make docs` and published from `docs/`.

---

## Installing for development

```bash
git clone https://github.com/olaflaitinen/biotechnology.git
cd biotechnology
python -m pip install -e ".[dev]"
pre-commit install

make test        # pytest with coverage
make lint        # ruff + black --check + mypy
make validate    # taxonomy integrity suite
make docs        # regenerate docs/ from the source of truth
make all         # everything above, in the order CI runs it
```

Supported on Python 3.9 through 3.14, on Linux, macOS and Windows.

---

## Contributing

Corrections are the most valuable contribution. If a figure is wrong, a
regulation has been superseded, or a plain-language paragraph is condescending
or unclear, open an issue or a pull request - you do not need to be a
programmer, and a change to one facet file touches nothing else.

Priorities, in order:

1. **Factual corrections** to existing records.
2. **Non-European regulatory coverage.** The governance facets lean European
   because that is what the maintainers can cite accurately. This is a stated
   bias, not a hidden one, and additions are the most welcome kind.
3. **Plain-language review** by people who are not scientists. If a
   `plain_language` field needs a second reading, it has failed.
4. **New formula modules** with derivation, domain of validity and citation.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

---

## Citing

If this library informs a publication, a curriculum or a policy document,
please cite it. Machine-readable metadata is in [`CITATION.cff`](CITATION.cff);
GitHub renders a formatted citation from it in the sidebar.

```bibtex
@software{laitinen_fredriksson_lundstrom_imanov_biotechnology,
  author    = {Laitinen-Fredriksson Lundstrom-Imanov, Gustav Olaf Yunus},
  title     = {biotechnology: a machine-readable taxonomy of the colour-coded
               branches of biotechnology},
  year      = {2026},
  publisher = {Metropolia University of Applied Sciences},
  url       = {https://github.com/olaflaitinen/biotechnology},
  license   = {EUPL-1.2}
}
```

---

## References

Numbered in order of first appearance, in the style of *Nature*. Every DOI here
is resolved against Crossref by `tools/verify_references.py`, which fails the
build if one does not resolve or if any stored field disagrees with the
publisher's deposited record. Run it with `make citations`.

<a id="ref-1"></a>
1. Barcelos, M. C. S., Lupki, F. B., Campolina, G. A., Nelson, D. L. & Molina, G.
   The colors of biotechnology: general overview and developments of white,
   green and blue areas. *FEMS Microbiology Letters* **365**, fny239 (2018).
   DOI: 10.1093/femsle/fny239

<a id="ref-2"></a>
2. Wilkinson, M. D. *et al.* The FAIR Guiding Principles for scientific data
   management and stewardship. *Scientific Data* **3**, 160018 (2016).
   DOI: 10.1038/sdata.2016.18

<a id="ref-3"></a>
3. Ashburner, M. *et al.* Gene Ontology: tool for the unification of biology.
   *Nature Genetics* **25**, 25-29 (2000). DOI: 10.1038/75556

The full bibliography for the taxonomy itself, one entry for every citation key
used in any record, is in [`BIBLIOGRAPHY.md`](BIBLIOGRAPHY.md).

---

## Author

**Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov**
School of Information and Communication Technology
Metropolia University of Applied Sciences
Karaportti 2, 02610 Espoo, Finland
<yunus.imanov@metropolia.fi>

---

## Licence

Licensed under the **European Union Public Licence v. 1.2** (EUPL-1.2).
See [`LICENCE`](LICENCE) for the full text and [`NOTICE.md`](NOTICE.md) for the
attribution notice.

The EUPL is a copyleft licence: you may use, modify and redistribute this work,
including commercially, provided derivative works are distributed under the
EUPL or a compatible licence listed in its Appendix. It is available in all
twenty-three official languages of the European Union, and all versions are
equally authentic.

> **This library is a reference work, not professional advice.** Nothing in it
> is medical, legal, regulatory or safety guidance. Regulations change; verify
> every citation against the current official text before relying on it.
