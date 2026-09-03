<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from DATA_MODEL.md.
  Edit the source and run `make docs`.
-->

# Data model

Field-by-field specification of every record type in this library.

This is the normative reference. `src/biotechnology/core/models.py` is the
implementation; where the two disagree, the implementation is a bug.

---

## 1. Overview

```
Branch                      one of the ten colours
  └── Subtype               a sub-discipline inside that colour
        ├── Metric          a measurable quantity used in that field
        └── Milestone       a dated event in its history
```

Four record types. All are `@dataclass(frozen=True)` - immutable, hashable,
thread-safe, and fully typed under `mypy --strict`.

Addressing is by **dotted path**, two levels deep and no more:

```
"red"                    a Branch
"red.gene_therapy"       a Subtype
```

The grammar is enforced by `core/paths.py`. Segments are lowercase, start with
a letter, and contain only `a-z`, `0-9` and `_`. Input is normalised before
matching: surrounding whitespace stripped, lower-cased, spaces and hyphens
converted to underscores, repeated underscores collapsed. So `" Red . Gene-Therapy "`
resolves to `red.gene_therapy`, while `"red/gene"` is a `PathSyntaxError`.

---

## 2. `Subtype`

The fundamental unit. Eighty-five of them, each defined by a seven-file package
under `src/biotechnology/branches/<colour>/<key>/`.

### 2.1 Identity

| Field | Type | Required | Notes |
|-------|------|:--------:|-------|
| `key` | `str` | ✔ | Must equal the directory name. Asserted at import. |
| `name` | `str` | ✔ | Display name, title case. |
| `aliases` | `Tuple[str, ...]` | | Lowercase alternative names. Resolve without a branch prefix via `get_subtype()`. |
| `branch_key` | `str` | auto | Stamped on by `Branch.build()`. Empty at definition time. |

**Derived**

| Property | Type | Notes |
|----------|------|-------|
| `path` | `str` | `f"{branch_key}.{key}"`, degrading to `key` before assembly. |
| `branch` | `Branch` | Resolved lazily through the registry; see §7. |

### 2.2 Narrative - from `narrative.py`

| Field | Type | Required | Register | Constraint |
|-------|------|:--------:|----------|------------|
| `summary` | `str` | ✔ | technical | One sentence, ≤ 200 characters. |
| `description` | `str` | ✔ | technical | 3-8 sentences. Structure: boundary → strategies → practice → binding constraint. |
| `plain_language` | `str` | ✔ | public | No unexplained jargon. |
| `analogy` | `str` | ✔ | public | Everyday image whose limits are visible. |
| `why_it_matters` | `str` | ✔ | public | Must state a cost or controversy alongside the benefit. |

Editorial rules 1-5 in [`STYLE_GUIDE.md`](../project/style-guide.md) govern these fields.

### 2.3 Practice - from `practice.py`

| Field | Type | Minimum | Notes |
|-------|------|:-------:|-------|
| `applications` | `Tuple[str, ...]` | 4 | Must name things that exist. |
| `technologies` | `Tuple[str, ...]` | 4 | Enabling methods and platforms. |
| `organisms` | `Tuple[str, ...]` | 0 | **Registry keys** into `biotechnology.organisms`. |
| `techniques` | `Tuple[str, ...]` | 0 | **Registry keys** into `biotechnology.techniques`. |
| `challenges` | `Tuple[str, ...]` | 4 | At least one must be non-technical. |

### 2.4 Quantitative - from `metrics.py`

| Field | Type | Minimum | Notes |
|-------|------|:-------:|-------|
| `metrics` | `Tuple[Metric, ...]` | 3 | See §3. |
| `formulas` | `Tuple[str, ...]` | 0 | **Registry keys** into `biotechnology.formulas`. |

### 2.5 History - from `history.py`

| Field | Type | Minimum | Notes |
|-------|------|:-------:|-------|
| `milestones` | `Tuple[Milestone, ...]` | 3 | Must include a setback where one exists. See §4. |

**Derived**

| Property | Type | Notes |
|----------|------|-------|
| `timeline` | `Tuple[Milestone, ...]` | Sorted oldest first. |
| `first_year` | `Optional[int]` | Year of the earliest milestone. |

### 2.6 Governance - from `governance.py`

| Field | Type | Required | Notes |
|-------|------|:--------:|-------|
| `maturity` | `Maturity` | ✔ | §5.1 |
| `risk_tier` | `RiskTier` | ✔ | §5.2 |
| `scale` | `Scale` | ✔ | §5.3 |
| `domains` | `Tuple[Domain, ...]` | ✔ | §5.5. Orthogonal to the colour branches. |
| `regulatory_status` | `RegulatoryStatus` | ✔ | §5.6 |
| `regulations` | `Tuple[str, ...]` | | Instruments with **legal force**. |
| `standards` | `Tuple[str, ...]` | | Technical consensus documents, **no** independent legal force. |

### 2.7 Linkage - from `linkage.py`

| Field | Type | Notes |
|-------|------|-------|
| `sdgs` | `Tuple[int, ...]` | Integers 1-17. Each must survive the sceptical-auditor test. |
| `glossary` | `Tuple[str, ...]` | **Registry keys** into `biotechnology.glossary`. |
| `references` | `Tuple[str, ...]` | **Registry keys** into `biotechnology.refs`. |
| `related` | `Tuple[str, ...]` | Dotted subtype paths. 4-8 entries. Reciprocity not required. |

**Derived**

| Property | Type |
|----------|------|
| `sdg_titles` | `Tuple[str, ...]` |

### 2.8 Methods

| Method | Returns | Notes |
|--------|---------|-------|
| `metric(symbol_or_name)` | `Metric` | Case-insensitive lookup by symbol or name. |
| `haystack()` | `str` | Every searchable field, flattened and lower-cased. Computed on demand. |
| `to_dict(verbose=True)` | `Dict[str, Any]` | `verbose=False` emits identity plus both summaries only. |

---

## 3. `Metric`

The bridge between the descriptive and computational halves of the library.

| Field | Type | Required | Notes |
|-------|------|:--------:|-------|
| `name` | `str` | ✔ | Full human name. |
| `symbol` | `str` | ✔ | **ASCII only.** `mu`, not the Greek letter. |
| `unit` | `str` | ✔ | Written out. `"-"` or `"dimensionless"` where none. |
| `typical` | `str` | | A **string**, never a numeric pair. See below. |
| `formula` | `Optional[str]` | | Registry key into `biotechnology.formulas`. |
| `evidence` | `EvidenceLevel` | ✔ | Defaults to `REVIEWED`. §5.4 |
| `note` | `str` | | The caveat that stops the number being misused. |

**Why `typical` is a string.** Almost every real range in biology is
conditional. "1e11 to 2e14 vg/kg" is meaningful only once you know the route of
administration; encoding it as `(1e11, 2e14)` invites a user to average it, plot
it or compare it across routes, all of which are wrong. The string form forces
the reader to read `note`.

**Why ASCII symbols.** The same string has to render in a terminal, a CSV
opened with the wrong encoding, a LaTeX document and an HTML page. Pretty forms
are generated at render time from a lookup table in `core/text.py`.

**Methods:** `to_dict()`, `render()` → `"vg/kg [vector genomes per kilogram] 1e11 - 2e14 - Vector genome dose"`.

---

## 4. `Milestone`

| Field | Type | Required | Notes |
|-------|------|:--------:|-------|
| `year` | `int` | ✔ | Four digits. Negative means BCE. |
| `event` | `str` | ✔ | One clause. |
| `note` | `str` | | Detail: who, why it mattered, what it caused. |

**Methods:** `to_dict()`, `render()` → `"1982  First recombinant medicine approved"`.

---

## 5. Controlled vocabularies

All six are `DescribedEnum` subclasses. Each member carries three things:

```python
Maturity.PILOT.value        # "pilot"                     machine token, stable
Maturity.PILOT.label        # "Pilot"                     human title
Maturity.PILOT.explanation  # "Being run at demonstration size to see whether
                            #  it survives real conditions."
Maturity.PILOT.explain()    # "Pilot - Being run at demonstration size ..."
Maturity.PILOT.rank         # 2                           declaration order
Maturity.parse("Pilot")     # forgiving lookup by value or label
Maturity.values()           # every machine token
Maturity.table()            # the whole vocabulary as dicts, for docs
```

Declaration order is meaningful in every vocabulary, and `rank` exposes it, so
members are orderable (`Maturity.RESEARCH < Maturity.COMMERCIAL`).

### 5.1 `Maturity` - how far from the bench

| Value | Approx. TRL | Meaning |
|-------|:-----------:|---------|
| `research` | 1-3 | Still in laboratories; no product exists. |
| `emerging` | 3-5 | Works in the laboratory; first companies scaling. |
| `pilot` | 5-7 | Demonstration size, testing real conditions. |
| `commercial` | 7-9 | Sold today, though not yet everywhere. |
| `established` | 9 | Routine, widely deployed, often decades old. |

`trl_range()` returns the span as a tuple. Five bands rather than nine because
nine is more resolution than a field survey can honestly support.

### 5.2 `RiskTier` - governance intensity, not personal danger

| Value | Meaning |
|-------|---------|
| `routine` | Ordinary work under standard safety rules. |
| `controlled` | Needs a permit, licence or institutional sign-off. |
| `regulated` | A national agency must authorise before sale or release. |
| `restricted` | Access to materials or methods is limited by law. |

This is **not** a laboratory biosafety level. A BSL-2 organism handled under a
clinical trial protocol is `regulated` here, because the paperwork rather than
the pathogen dominates. `requires_committee()` is true from `controlled` up.

### 5.3 `Scale` - physical working size

| Value | Meaning |
|-------|---------|
| `bench` | Millilitres to a few litres. |
| `pilot` | Tens to thousands of litres. |
| `industrial` | Cubic metres and upward. |
| `field` | Open land, water or an animal herd. |
| `population` | Whole communities, countries or ecosystems. |

### 5.4 `EvidenceLevel` - how solid a claim is

| Value | Meaning |
|-------|---------|
| `consensus` | Textbook material the field agrees on. |
| `reviewed` | Supported by peer-reviewed literature or an official report. |
| `reported` | Stated in one credible source, not widely replicated. |
| `indicative` | Order-of-magnitude only, for orientation. |

Recording which is which keeps the library honest and lets cautious users
filter to settled material.

### 5.5 `Domain` - sector, orthogonal to colour

`health`, `food`, `energy`, `materials`, `environment`, `information`,
`governance`, `security`.

Colours group by tradition; domains group by who pays. One colour spans several
domains and one domain appears in several colours, giving a second filter axis.

### 5.6 `RegulatoryStatus`

| Value | Meaning |
|-------|---------|
| `unregulated` | No product-specific approval normally required. |
| `notified` | Authorities must be told; no full approval needed. |
| `authorised` | A formal licence is required before sale or release. |
| `varies` | Jurisdictions reach materially different decisions. |
| `prohibited` | Banned in most or all jurisdictions. |

`varies` is jurisdiction-neutral on purpose. A genome-edited plant is a GMO in
the European Union and a conventional variety in Japan, Argentina and the
United States - the same organism, three answers.

---

## 6. `Branch`

| Field | Type | Notes |
|-------|------|-------|
| `key`, `name` | `str` | `key` must equal the package directory name. |
| `colour` | `str` | Hex, `#RRGGBB`. `color` is a US-spelling alias property. |
| `summary`, `description` | `str` | Technical register. |
| `plain_language`, `analogy`, `why_it_matters` | `str` | Public register. |
| `origin_note` | `str` | How this colour label came into use. |
| `subtypes` | `Tuple[Subtype, ...]` | Published order; narrative, not alphabetical. |
| `aliases` | `Tuple[str, ...]` | `"industrial"` → `white`, `"gray"` → `grey`. |
| `domains`, `sdgs` | tuples | Branch-level. |
| `milestones` | `Tuple[Milestone, ...]` | Branch-level history. |
| `key_questions` | `Tuple[str, ...]` | The open questions of the field. |
| `references` | `Tuple[str, ...]` | Registry keys. |
| `_index` | `Dict[str, Subtype]` | Private. `repr=False, compare=False`. |

### Mapping protocol

```python
len(branch)            # subtype count
for s in branch: ...   # declaration order
"key" in branch        # by key or by Subtype instance
branch["key"]          # raises UnknownSubtypeError with candidates
branch.get("key")      # non-raising
branch.keys() / .names() / .paths()
```

### Derived

| Property / method | Returns | Notes |
|-------------------|---------|-------|
| `rgb` | `(int, int, int)` | Parsed from `colour`. |
| `is_light` | `bool` | ITU-R BT.601 luma > 160. True only for `white`, which is exactly why it exists - its swatch would otherwise render white-on-white. |
| `timeline` | `Tuple[Milestone, ...]` | Branch plus every subtype milestone, sorted. |
| `all_sdgs` | `Tuple[int, ...]` | Union across the branch. |
| `all_formulas` | `Tuple[str, ...]` | De-duplicated union. |
| `by_maturity(m)` | `Tuple[Subtype, ...]` | |
| `search(q)` | `List[Subtype]` | Substring, this branch only. |

### Construction

`Branch.build(...)` is the only supported constructor. It stamps `branch_key`
onto every subtype via `dataclasses.replace` (necessary because `Subtype` is
frozen) and raises `SchemaError` on duplicate keys at import time.

---

## 7. Deferred imports

Two properties import inside their function body to break a cycle:

- `Subtype.branch` → `core.registry.get_branch`
- `Subtype.sdg_titles` → `biotechnology.sdg`

`core.models` is imported by the branch packages, which are imported by
`core.registry`. A module-level import in either direction fails at load. Both
deferrals are commented at the point of deferral. Do not "tidy them up".

---

## 8. Serialisation contract

`to_dict()` output is stable within a major version and is what
`to_json()`, the CSV exporter and the documentation generator consume.

```json
{
  "branches": [ { "key": "red", "...": "...", "subtypes": [ ... ] } ],
  "branch_count": 10,
  "subtype_count": 85
}
```

- Enum values serialise to their **machine token**, never their label.
- Tuples serialise to JSON arrays.
- `Metric` and `Milestone` serialise to objects with all fields present,
  empty strings where unset.
- Key order is insertion order and is deliberately stable, so that a
  round-trip through `json.dumps` produces a diffable file.
