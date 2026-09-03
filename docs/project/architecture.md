<!--
  GENERATED FILE. Do not edit.
  Produced from ARCHITECTURE.md.
  Edit the source and run `make docs`.
-->

# Architecture

How this repository is laid out, why it is laid out that way, and what you have
to understand before changing it.

---

## 1. The shape of the problem

This library is a **curated dataset with a small runtime around it**. That is an
unusual shape, and almost every design decision below follows from it.

A normal Python library is mostly logic with a little configuration. Here the
ratio is inverted: roughly ninety per cent of the source tree is hand-written,
hand-reviewed subject-matter content, and ten per cent is the machinery that
indexes, searches, validates and renders it. Optimising for the usual things -
minimal line count, DRY abstraction, clever generic code - would be exactly
wrong. The things worth optimising for are:

| Priority | Why |
|----------|-----|
| **Reviewability by non-programmers** | The people who can tell you a figure is wrong are clinicians, agronomists, regulatory affairs professionals and lawyers, not Python developers. |
| **Small, isolated diffs** | A correction to one milestone must not produce a conflict with someone editing an unrelated paragraph. |
| **Mechanical checking of everything checkable** | Hand-curated cross-references rot. If a link can be validated, it must be validated on every commit. |
| **Import-time failure** | A malformed record should fail loudly when the package is imported, not silently as an empty column three months later. |

---

## 2. Top-level layout

```
biotechnology/
├── LICENCE                     official EUPL-1.2 text, verbatim
├── NOTICE.md                   attribution notice required by Article 5
├── README.md                   front page
├── ARCHITECTURE.md             this file
├── DATA_MODEL.md               field-by-field specification
├── STYLE_GUIDE.md              editorial rules for content
├── NOTATION.md                 symbol, unit and formula conventions
├── GLOSSARY.md                 terms, both registers
├── BIBLIOGRAPHY.md             citation keys resolved
├── CONTRIBUTING.md             how to change something
├── GOVERNANCE.md               who decides what
├── CODE_OF_CONDUCT.md
├── SECURITY.md                 vulnerabilities and dual-use content policy
├── CHANGELOG.md
├── ROADMAP.md
├── FAQ.md
├── AUTHORS.md
├── pyproject.toml              packaging + all tool configuration
├── Makefile                    the commands CI runs, runnable locally
├── tox.ini                     multi-version test matrix
├── mkdocs.yml                  documentation site
├── .pre-commit-config.yaml
├── .editorconfig
├── .gitattributes
├── .github/                    workflows, issue templates, CODEOWNERS
├── docs/                       generated reference pages
├── tests/                      the test suite
└── src/biotechnology/          the package
```

`src`-layout is used deliberately. Tests import the *installed* package, never
the working directory, which is the only reliable way to notice a file that was
never added to the distribution.

---

## 3. Package layout

```
src/biotechnology/
├── __init__.py          the public API surface; re-exports and branch constants
├── __main__.py          enables `python -m biotechnology`
├── py.typed             PEP 561 marker
│
├── core/                the machinery
│   ├── enums.py         controlled vocabularies
│   ├── errors.py        the complete exception hierarchy
│   ├── models.py        Branch, Subtype, Metric, Milestone
│   ├── paths.py         dotted-address grammar
│   ├── registry.py      indexes, lookup, filters, graph traversal
│   ├── search.py        ranked free-text search
│   ├── graph.py         cross-reference graph analysis
│   ├── export.py        JSON, CSV, Markdown, DOT emitters
│   ├── validation.py    the integrity suite
│   ├── text.py          wrapping, tables, symbol rendering
│   ├── units.py         unit parsing and conversion
│   └── constants.py     physical and biological constants
│
├── branches/            the ten colours; the bulk of the content
│   ├── __init__.py      assembles ALL_BRANCHES; import-time consistency checks
│   ├── red/
│   │   ├── __init__.py  assembles the branch from its subtype packages
│   │   ├── profile.py   branch-level narrative, history, key questions
│   │   ├── gene_therapy/          <- a subtype ecosystem (see section 4)
│   │   ├── cell_therapy/
│   │   └── ...
│   └── ... nine more colours
│
├── formulas/            one package per computable relationship
├── organisms/           model organisms and production hosts
├── techniques/          bench methods
├── glossary/            term definitions, both registers
├── refs/                the bibliography, as data
├── sdg/                 the seventeen Sustainable Development Goals
└── cli/                 one module per subcommand
```

---

## 4. The subtype ecosystem - the central design decision

**Every subtype is a package of seven files, not a module.**

```
branches/red/gene_therapy/
├── __init__.py       assembles the six facets into one frozen Subtype
├── narrative.py      SUMMARY, DESCRIPTION, PLAIN_LANGUAGE, ANALOGY, WHY_IT_MATTERS
├── practice.py       APPLICATIONS, TECHNOLOGIES, ORGANISMS, TECHNIQUES, CHALLENGES
├── metrics.py        METRICS, FORMULAS
├── history.py        MILESTONES
├── governance.py     MATURITY, RISK_TIER, SCALE, DOMAINS, REGULATORY_STATUS,
│                     REGULATIONS, STANDARDS
└── linkage.py        SDGS, GLOSSARY, REFERENCES, RELATED
```

### 4.1 Why split it

**Reviewability.** A subtype record mixes five kinds of content - prose,
practice, numbers, dates, law - and the people qualified to check each kind are
different people. One file per concern means one reviewer per file. A regulatory
affairs professional can open `governance.py`, check every citation, and never
encounter a Python construct more complicated than a tuple of strings.

**Diff hygiene.** Correcting a single milestone touches `history.py` and
nothing else. In a single-file layout, every correction produces a diff against
a 600-line file and two contributors working on different aspects of the same
subtype collide on every pull request.

**Mechanical checking.** Each facet exports a fixed set of names with fixed
types. `tests/test_facets.py` walks every subtype package and asserts the
contract holds. A missing field is an error at import time, not an empty column
in a generated table.

**Comment density where it belongs.** Each facet file carries the editorial
rules that govern *that facet* in its header. The rule "APPLICATIONS must name
something that exists, not something proposed" lives at the top of
`practice.py`, where the person about to break it is already looking.

### 4.2 The facet contract

Every subtype package exports exactly these names, from exactly these files:

| File | Exports | Types |
|------|---------|-------|
| `narrative.py` | `SUMMARY`, `DESCRIPTION`, `PLAIN_LANGUAGE`, `ANALOGY`, `WHY_IT_MATTERS` | 5 × `str` |
| `practice.py` | `APPLICATIONS`, `TECHNOLOGIES`, `ORGANISMS`, `TECHNIQUES`, `CHALLENGES` | 5 × `Tuple[str, ...]` |
| `metrics.py` | `METRICS`, `FORMULAS` | `Tuple[Metric, ...]`, `Tuple[str, ...]` |
| `history.py` | `MILESTONES` | `Tuple[Milestone, ...]` |
| `governance.py` | `MATURITY`, `RISK_TIER`, `SCALE`, `DOMAINS`, `REGULATORY_STATUS`, `REGULATIONS`, `STANDARDS` | enums + tuples |
| `linkage.py` | `SDGS`, `GLOSSARY`, `REFERENCES`, `RELATED` | `Tuple[int, ...]` + 3 × `Tuple[str, ...]` |
| `__init__.py` | `KEY`, `NAME`, `ALIASES`, `SUBTYPE` | `str`, `str`, tuple, `Subtype` |

`__init__.py` holds **no descriptive content** beyond identity. A reviewer never
has to read it to check a fact.

### 4.3 Adding a subtype

1. Copy an existing subtype directory.
2. Keep all seven filenames. Replace the content.
3. Add one import line and one tuple entry to the parent branch `__init__.py`.

Nothing else changes. The registry, search engine, exporters, CLI and
documentation generator all discover it automatically.

---

## 5. The import graph

Import order is constrained and deliberately acyclic:

```
core.enums ──┐
core.errors ─┴─> core.models ──> branches/*/*/facets ──> branches/*/__init__
                      │                                         │
                      │                                         v
                      └────────────────────────────> branches/__init__ (ALL_BRANCHES)
                                                                │
                                                                v
core.paths ────────────────────────────────────────────> core.registry
                                                                │
                                          ┌─────────────────────┼─────────────────┐
                                          v                     v                 v
                                    core.search           core.export        core.graph
                                          └─────────────────────┼─────────────────┘
                                                                v
                                                        biotechnology/__init__
```

Two cycles are broken by deferred import:

- `Subtype.branch` needs `core.registry.get_branch`, but the registry needs the
  branches, which need `core.models`. The property imports inside the function
  body.
- `Subtype.sdg_titles` needs the `sdg` package for the same reason.

Both are documented at the point of deferral. Do not "clean them up" to a
module-level import; the package will fail to load.

---

## 6. Immutability

Every record type is a `@dataclass(frozen=True)`.

- **Hashable**, so records can be dict keys and set members. Deduplicating
  search results across branches relies on this.
- **Safe to share.** The taxonomy is built once at import and handed out by
  reference. Nothing can corrupt a global by accident.
- **Thread-safe** with no locking.

The cost is that `Branch.build()` must construct copies via
`dataclasses.replace` when it stamps `branch_key` onto each subtype, rather
than mutating in place. That is a few microseconds once per process.

`Branch` additionally carries a private `_index` dict, declared with
`repr=False, compare=False` so that it neither prints nor participates in
equality. Without both flags a `Branch` would print thousands of lines.

---

## 7. Eager index construction

`core/registry.py` builds three flat indexes at import time:

```
_BRANCH_INDEX    key or alias      -> Branch
_SUBTYPE_INDEX   "branch.subtype"  -> Subtype
_ALIAS_INDEX     subtype alias     -> Subtype
```

Eager rather than lazy, because:

- alias collisions are detected the moment the package is imported, not when an
  unlucky user hits one;
- every lookup afterwards is a dict hit;
- the objects are immutable, so an index can never drift out of date.

Canonical keys always beat aliases: the branch index is built in two passes so
that a future alias cannot shadow an existing canonical key.

---

## 8. Errors

Every exception raised by this package inherits from `BiotechnologyError`, so a
caller can wrap the whole library in one `except` clause while ordinary Python
errors still propagate.

Lookup errors additionally inherit from `KeyError`, so code written around
dict-style access keeps working. `__str__` is overridden, because
`KeyError.__str__` wraps its argument in quotes and mangles a carefully written
sentence.

Every "unknown X" message names the offending token, offers a `difflib`
suggestion where one exists, and lists the valid values. The user should never
have to open a source file to find out what they were allowed to type.

---

## 9. Validation

Three layers, running at different times:

| Layer | When | What it catches |
|-------|------|-----------------|
| **Enumerations** | Import | Typos in controlled vocabularies - an `ImportError`, not a silent miss |
| **`Branch.build`** | Import | Duplicate subtype keys inside a branch |
| **`branches/__init__`** | Import | Directory name not matching `BRANCH.key`; empty branch |
| **Integrity suite** | `pytest`, CI | Dead cross-references, missing required fields, out-of-range SDG numbers, metrics without units, records violating the editorial minimums |

`tests/test_integrity.py` is the single most valuable test in the suite, because
cross-references are exactly what rots first in a hand-curated dataset.

---

## 10. Generated versus authored

| Path | Status | Rule |
|------|--------|------|
| `src/**` | **Authored** | Hand-written and hand-reviewed. Never generated. |
| `tests/**` | **Authored** | |
| `docs/**` | **Generated** | Produced by the documentation generator from `src/`. Do not edit; edit the source facet and re-run `make docs`. |
| Root `*.md` | **Authored** | |

The generator reads the same objects the library exposes, so the documentation
cannot describe a field that does not exist.

---

## 11. Things that were considered and rejected

**A database or a JSON blob instead of Python modules.** Rejected: it would
lose the comments, and the comments carry the editorial reasoning that makes
the dataset reviewable. A JSON file cannot explain why `MATURITY` is
`COMMERCIAL` rather than `ESTABLISHED`. A Python module can, and does.

**Generating the facet files from a compact spec.** Rejected: generated source
of truth is not source of truth. A domain expert must be able to edit the file
they are reading.

**A third taxonomy level.** Rejected: two levels are enough, the grammar in
`core/paths.py` enforces it, and every proposed third level turned out to be a
cross-reference in disguise.

**Runtime dependencies for search or export.** Rejected: see the hard
constraint in `pyproject.toml`. The dataset is small enough that a full scan
costs well under a millisecond.
