# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
with the additional identifier-stability rule described in
[`GOVERNANCE.md`](GOVERNANCE.md) §3.6.

---

## About the data freeze date

Every release records a **data freeze date**: the date on which the factual,
regulatory and bibliographic claims in the release were last verified.

This matters more here than in most software. A bug in a library is either
present or absent; a regulatory citation is accurate *as of a date* and decays
silently afterwards. A reader relying on `governance.REGULATIONS` needs to know
how old it is. Nothing in this project claims to be current beyond its freeze
date.

---

## [Unreleased]

### Added

- `white.biopolymers` subtype package, seven facets. Organised around the
  independence of biobased content and biodegradability, and around the
  distinction between disintegration and mineralisation that the restriction
  of oxo-degradable plastics turned on.
- `white.cell_free_biomanufacturing` subtype package, seven facets. Completes
  the white branch at nine of nine. It is the only white record at
  `Maturity.PILOT` and the only one at `Scale.BENCH`, both deliberate: the
  technology is established as a research reagent and at demonstration scale
  as a manufacturing platform.
- `tools/check_enum_members.py`, which validates every controlled-vocabulary
  reference under `src/biotechnology/branches/` against `core/enums.py` using
  the abstract syntax tree, with no import. It is the only check in the
  repository that gives a useful answer while the library is half written,
  which is exactly when the error it catches is invisible to Python.
- The new check is wired into `.pre-commit-config.yaml`, the `data` target of
  the `Makefile` and the taxonomy integrity job of `ci.yml`.

### Fixed

- `branches/white/__init__.py` referred to a `Branch.prefers_dark_text` method
  that does not exist. The property is `Branch.is_light`. Found by importing
  the assembled branch rather than by reading the diff.
- Two `governance.py` facets used controlled-vocabulary members that do not
  exist: `RiskTier.MODERATE` and `RiskTier.LOW`, where the vocabulary offers
  `ROUTINE`, `CONTROLLED`, `REGULATED` and `RESTRICTED` and measures governance
  intensity rather than danger; and `Domain.AGRICULTURE`, `Domain.INDUSTRY` and
  `Domain.HEALTHCARE`, where the vocabulary groups by who pays and offers
  `FOOD`, `MATERIALS` and `HEALTH`. Both records were corrected and the values
  justified in comments. `tools/check_enum_members.py` exists so that this
  class of error cannot recur silently.

---

## [0.1.0] - 2026-09-02

First public release.

**Data freeze: 2026-09-02.**

### Added

#### Taxonomy

- Ten colour branches: `red`, `green`, `white`, `blue`, `yellow`, `grey`,
  `brown`, `gold`, `dark`, `purple`.
- Eighty-five subtypes, each an independently reviewable seven-file package
  under `src/biotechnology/branches/<colour>/<key>/`.
- Every subtype carries both registers: technical `summary` and `description`,
  and public `plain_language`, `analogy` and `why_it_matters`.
- Every subtype carries `metrics` with ASCII symbols, written-out units,
  conditional typical ranges and an evidence grade; a dated `milestones`
  history including setbacks; governance placement in six controlled
  vocabularies; `regulations` and `standards` kept in separate tuples; and
  typed cross-references to formulas, organisms, techniques, glossary terms,
  citations and other subtypes.

#### Core

- `core.models` - `Branch`, `Subtype`, `Metric`, `Milestone`, all frozen,
  hashable and typed.
- `core.enums` - `Maturity`, `RiskTier`, `Scale`, `EvidenceLevel`, `Domain`,
  `RegulatoryStatus`, each member carrying a machine token, a human label and
  a plain-language explanation.
- `core.errors` - complete exception hierarchy rooted at
  `BiotechnologyError`, with `difflib`-backed "did you mean" suggestions on
  every lookup failure.
- `core.paths` - two-level dotted-address grammar with forgiving
  normalisation and precise syntax errors.
- `core.registry` - eagerly built indexes, lookup, alias resolution, graph
  traversal, timeline merging, and filters by SDG, domain, maturity, risk tier
  and scale.
- `core.search` - ranked free-text search across every field.
- `core.export` - JSON, CSV, Markdown and DOT emitters.
- `core.validation` - the integrity suite.
- `core.text`, `core.units`, `core.constants`.

#### Formulas

- Computable formula packages, each with `notation.py`, `derivation.py` and
  `implementation.py`, covering molecular biology, bioprocess engineering,
  diagnostics, epidemiology, quantitative genetics, ecology and environmental
  engineering.
- Every formula validates its domain and raises `DomainError` naming the
  parameter, the value and the accepted range.

#### Registries

- `organisms`, `techniques`, `glossary`, `refs`, `sdg`.

#### Interface

- `biotechnology` command line: `list`, `tree`, `show`, `search`, `sdg`,
  `formula`, `compute`, `vocab`, `stats`, `validate`, `export`.
- `python -m biotechnology` equivalent.

#### Quality

- Full integrity suite: every cross-reference resolved on every commit; a dead
  link fails the build.
- Editorial minimums enforced mechanically - five narrative fields, four
  applications, four challenges including at least one non-technical, three
  milestones, units and evidence grades on every metric.
- `tests/test_dark_branch_is_defensive.py` enforcing the dual-use content
  policy.
- PEP 561 typing marker; `mypy --strict` clean.
- Zero runtime dependencies.

#### Documentation

- `README.md`, `ARCHITECTURE.md`, `DATA_MODEL.md`, `STYLE_GUIDE.md`,
  `NOTATION.md`, `GLOSSARY.md`, `BIBLIOGRAPHY.md`, `CONTRIBUTING.md`,
  `GOVERNANCE.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `ROADMAP.md`,
  `FAQ.md`, `AUTHORS.md`, `NOTICE.md`.
- Generated reference pages under `docs/`, one per subtype and per formula.

### Licence

- Released under the **European Union Public Licence v. 1.2**. The official
  licence text is reproduced verbatim in `LICENCE`; the attribution notice
  required by Article 5 is in `NOTICE.md`.

### Known limitations

Stated plainly, because a reader deserves to know them before relying on the
data.

- **European regulatory lean.** `governance.REGULATIONS` cites European
  instruments most completely, United States instruments where they are the
  global reference, and others sparsely. See `CONTRIBUTING.md` §1.2.
- **English only.** No translations of any register, including the
  plain-language one, which is the register that would benefit most.
- **High-income framing of cost.** Price and access discussions are written
  from the perspective of health and agricultural systems that can, in
  principle, pay.
- **The colour scheme is a convention, not a standard.** Boundaries overlap and
  some assignments are arguable. See `FAQ.md`.
- **Bus factor of one.** See `GOVERNANCE.md` §6.

---

<!--
  Link definitions. Update on every release.
-->
[Unreleased]: https://github.com/olaflaitinen/biotechnology/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/olaflaitinen/biotechnology/releases/tag/v0.1.0
