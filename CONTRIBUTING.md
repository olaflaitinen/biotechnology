# Contributing

Thank you for considering a contribution. This project is a curated dataset
with a small runtime around it, so **the most valuable contributions are
factual, not technical**, and most of them do not require you to write any code.

---

## 1. What is most needed

In priority order.

### 1.1 Factual corrections

If a figure is wrong, a regulation has been superseded, a date is off, or a
claim overstates the evidence - please say so. This is the single most useful
thing you can do.

You do not need to be a programmer. Open an issue using the **Data correction**
template, name the record (`red.gene_therapy`), the facet (`metrics.py`), the
field, what it says, what it should say, and a source. A maintainer will make
the change and credit you.

### 1.2 Non-European regulatory coverage

The `governance.py` facets lean European, because that is what the maintainers
can cite accurately. **This is a stated bias, not a hidden one.** Additions
covering the United States, Japan, China, India, Brazil, the African Union, the
Gulf states or anywhere else are the most welcome kind of contribution, and a
pull request that adds two lines to one `REGULATIONS` tuple is a complete,
mergeable contribution.

### 1.3 Plain-language review

If a `plain_language` field needs a second reading, it has failed. If an
`analogy` is condescending, misleading, or assumes a cultural reference not
everyone has, it has failed.

We specifically want review from people who are **not** scientists: teachers,
journalists, nurses, patients, policy staff, translators, students. You are the
audience those fields exist for, and you are better placed than the author to
say when they miss.

### 1.4 New formula modules

A formula module needs: the relationship, its notation, its derivation or a
citation for it, its domain of validity, its unit contract, worked examples as
doctests, and a test module. See [`NOTATION.md`](NOTATION.md) for the contract.

### 1.5 New subtypes

Rarer, but the taxonomy is not complete. Propose it in an issue first, with a
short argument for why it is a distinct subtype rather than a facet of an
existing one, and which branch it belongs in.

---

## 2. Before you start

```bash
git clone https://github.com/olaflaitinen/biotechnology.git
cd biotechnology
python -m pip install -e ".[dev]"
pre-commit install
make all          # test + lint + validate + docs, in the order CI runs them
```

If `make all` passes on a clean checkout, your environment is correct.

**Read [`STYLE_GUIDE.md`](STYLE_GUIDE.md).** It is normative, it is short, and
review will hold you to it. Section 2 contains fourteen numbered rules; the
review checklist at the end is the same one a maintainer will use.

**Skim [`ARCHITECTURE.md`](ARCHITECTURE.md)** if you are changing anything under
`src/biotechnology/core/`.

---

## 3. Correcting an existing record

This is a one-file change.

1. Find the record: `src/biotechnology/branches/<colour>/<subtype>/`.
2. Open the facet that owns the field:

   | You want to change | Open |
   |--------------------|------|
   | any prose | `narrative.py` |
   | applications, technologies, organisms, techniques, challenges | `practice.py` |
   | a number, unit, range or formula link | `metrics.py` |
   | a date or historical event | `history.py` |
   | maturity, risk, scale, a regulation, a standard | `governance.py` |
   | an SDG, glossary term, citation or cross-reference | `linkage.py` |

3. Make the change. **Update the comment above it if the reasoning changed.**
4. `make validate && make test`
5. Open a pull request against `main`.

You will not touch any other file. That is the whole point of the layout.

---

## 4. Adding a new subtype

```bash
cp -r src/biotechnology/branches/red/gene_therapy \
      src/biotechnology/branches/<colour>/<new_key>
```

1. Keep **all seven filenames**. The facet contract is checked by
   `tests/test_facets.py`.
2. Replace the content of each facet. Do not leave a field inherited from the
   template - the integrity suite will not catch a plausible-but-wrong
   paragraph, only a reviewer will.
3. Set `KEY` in `__init__.py` to match the directory name exactly. This is
   asserted at import time.
4. Register it in the parent branch `src/biotechnology/branches/<colour>/__init__.py`:
   add one import line and one entry to the `subtypes=(...)` tuple, in the
   position the published order calls for.
5. Add cross-references **from** at least two existing subtypes **to** the new
   one. A record nothing points at is a record nobody finds.
6. `make validate && make test && make docs`

Nothing else changes. The registry, search, exporters, CLI and documentation
generator discover it automatically.

---

## 5. Adding a formula

```
src/biotechnology/formulas/<name>/
├── __init__.py      exports FORMULA and the callable
├── notation.py      symbols, units, domain of validity
├── derivation.py    where the relationship comes from, with citation
└── implementation.py the function itself, with doctests
```

Requirements, all enforced:

- **Units are documented and checked.** A formula that silently accepts
  millilitres where it wanted litres is worse than no formula.
- **The domain of validity is stated and enforced.** Raise `DomainError` with
  the parameter name, the value given and the accepted range. Never let
  `math` raise a bare `ValueError` from inside a pipeline.
- **Doctests are worked examples**, with numbers a reader can verify by hand
  or against a cited source.
- **A citation exists** in `src/biotechnology/refs/` and is linked from
  `derivation.py`.
- **A test module exists** in `tests/formulas/`, covering the normal case, the
  boundary and at least one rejected input.

---

## 6. Commit and pull request conventions

Conventional Commits, with a scope that names what changed:

```
fix(red.gene_therapy): correct upper vector dose bound to 2e14 vg/kg
feat(formulas): add limit_of_detection with probit derivation
docs(style-guide): clarify rule 8 on including setbacks
data(green.biopesticides): add EU Regulation 2022/1439
chore(ci): pin actions to commit SHAs
```

Types: `feat`, `fix`, `data`, `docs`, `test`, `refactor`, `chore`, `ci`.

A pull request should:

- change **one thing**, or one coherent set of things;
- state its source for any factual change - a DOI, an official document
  identifier, or a URL to a primary source;
- pass `make all`;
- complete the review checklist from [`STYLE_GUIDE.md`](STYLE_GUIDE.md) §5.

Reviews are about the content first and the code second. Expect questions about
your source and about whether a plain-language paragraph really is plain.

---

## 7. The one hard rule

**The `dark` branch is documented defensively, and so is everything else.**

No facet of any record, in any branch, may contain operational information
about causing harm - synthesis routes for dangerous agents, methods to enhance
transmissibility or virulence, ways to evade detection or screening, or
anything that reads as a protocol rather than as a description of a governance
problem.

`tests/test_dark_branch_is_defensive.py` enforces this automatically. If your
contribution fails that test, the test is not wrong.

Content about biosafety, biosecurity governance, dual-use oversight, synthesis
screening, surveillance, medical countermeasures, forensics and arms control is
welcome and wanted. Content that would function as instructions is not, and
will be closed without merge regardless of stated intent.

See [`SECURITY.md`](SECURITY.md) for the full policy and for how to report a
concern privately.

---

## 8. Licence and attribution of contributions

By contributing you agree that your contribution is licensed under the
**EUPL-1.2**, the same licence as the rest of the project. There is no
contributor licence agreement to sign and no copyright assignment: you retain
your copyright in what you wrote.

Contributors are listed in [`AUTHORS.md`](AUTHORS.md). If you would prefer not
to be listed, or would like to be listed differently, say so in your pull
request and it will be respected.

---

## 9. Code of conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
Reports go to <yunus.imanov@metropolia.fi>.
