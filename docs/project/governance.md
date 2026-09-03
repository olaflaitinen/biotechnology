<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from GOVERNANCE.md.
  Edit the source and run `make docs`.
-->

# Governance

How decisions are made in this project, who makes them, and how that changes.

---

## 1. Current state: a single maintainer

This project is currently maintained by one person.

**Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov**
School of Information and Communication Technology
Metropolia University of Applied Sciences
<yunus.imanov@metropolia.fi>

Saying so plainly is more useful than describing a committee that does not
exist. A single-maintainer project has a known failure mode - the bus factor is
one - and section 6 says what is being done about it.

---

## 2. What counts as a decision

The project distinguishes four kinds of change, because they carry very
different risk and deserve very different scrutiny.

| Kind | Example | Who decides | Bar |
|------|---------|-------------|-----|
| **Factual correction** | A dose bound is wrong; a regulation was superseded | Maintainer, on the source | A citation. Merged quickly. |
| **Editorial change** | Rewriting a `plain_language` paragraph | Maintainer, with review from a non-specialist where possible | Clearer, and still accurate |
| **Structural change** | A new field on `Subtype`; a new facet file | Maintainer, after a public issue | Justified in `ARCHITECTURE.md`; migration for all 85 records |
| **Scope change** | A new subtype; a new branch; a new module family | Maintainer, after a public issue and a waiting period | Argued in the issue, at least 14 days open |

Anything in the first two rows can be proposed directly as a pull request.
Anything in the last two should start as an issue.

---

## 3. Principles that constrain the maintainer

These are commitments, not aspirations. They exist so that a contributor can
predict how a decision will go before spending effort on it.

### 3.1 Sources beat opinions

A factual dispute is settled by a primary source: a DOI, an official document
identifier, a regulator's published text. Where sources genuinely conflict, the
record says so and cites both. The maintainer does not get to break a tie by
preference.

### 3.2 The plain-language mandate is not negotiable

No record ships without `plain_language`, `analogy` and `why_it_matters`. No
`why_it_matters` ships that states only the benefit. These are the rules that
make this library different from an encyclopaedia, and they are not traded away
for coverage or for speed.

### 3.3 Zero runtime dependencies

A hard constraint, stated in `pyproject.toml` and repeated here so that it is
governance rather than habit. A feature that cannot be built against the
standard library goes into an optional extra or into a separate package.

### 3.4 The dual-use policy is not subject to consensus

`SECURITY.md` §2 governs. It is not a majority decision, it does not soften with
contributor pressure, and a stated purpose does not change the outcome. This is
the one area where the maintainer will decline to discuss further.

### 3.5 Stated bias, not hidden bias

Where the project's coverage is uneven - the European lean of the `governance`
facets, the English-only content, the high-income-country framing of cost
discussions - that is written down in the open, in `NOTICE.md` and
`CONTRIBUTING.md`, rather than left for a reader to discover.

### 3.6 Backwards compatibility of identifiers

Subtype keys, branch keys, formula keys, glossary keys and citation keys are
public API. A rename is a breaking change requiring a major version bump and an
alias retained for at least one minor cycle. External work cites these strings.

---

## 4. How a proposal moves

```
        issue opened
             │
             ├── factual correction ──────► maintainer verifies source ──► merge
             │
             ├── editorial ───────────────► review, ideally by a non-specialist
             │                                          │
             │                                          └──► merge
             │
             └── structural or scope ─────► public discussion, ≥ 14 days
                                                        │
                                          ┌─────────────┴─────────────┐
                                          │                           │
                                     accepted                     declined,
                                          │                    with written reasons
                                          ▼                           │
                                 implementation +                     ▼
                                 migration of all                 recorded in
                                 affected records                 the issue
```

Declined proposals get written reasons. An issue closed without explanation is
a governance failure, and you should say so.

---

## 5. Releases

- **Versioning** follows [Semantic Versioning](https://semver.org/) with the
  identifier-stability rule in §3.6.
- **`CHANGELOG.md`** follows [Keep a Changelog](https://keepachangelog.com/).
  Every release records its **data freeze date** - the date on which regulatory
  and factual claims were last verified - because that is what a reader needs
  in order to know how much to trust a citation.
- **Release mechanics** are in `.github/workflows/release.yml`: built from a
  signed tag, published to PyPI by trusted publishing rather than a long-lived
  token.
- **Cadence** is when there is something worth releasing. There is no schedule
  and no pressure to invent one.

---

## 6. Succession and the bus factor

The bus factor is one, and that is a real risk for a work intended to be cited.

Mitigations in place:

1. **EUPL-1.2.** Copyleft and irrevocable. If the maintainer disappears, anyone
   may fork and continue, and no one can close the fork off.
2. **No proprietary infrastructure.** Everything needed to build, test,
   validate and publish is in the repository. There is no private build server
   and no secret configuration beyond the PyPI trusted-publishing link.
3. **Documented architecture.** `ARCHITECTURE.md`, `DATA_MODEL.md` and
   `STYLE_GUIDE.md` exist so that a successor does not have to reverse-engineer
   the reasoning from the code.
4. **Machine-checked invariants.** The integrity suite encodes the rules that
   would otherwise live only in the maintainer's head.

Mitigations sought:

- **Co-maintainers.** A contributor with a sustained record of good factual
  corrections will be offered commit rights. This is how the project intends to
  grow, and it is an open invitation.
- **Domain editors.** The ideal structure is one editor per colour branch, each
  responsible for the accuracy of their branch, with the maintainer responsible
  for the machinery and the editorial standard. If you would like to hold a
  branch, say so.

---

## 7. If governance needs to change

Amendments to this document are a **structural change** under §2: proposed as a
public issue, open at least fourteen days, decided by the maintainer with
written reasons.

Once there is more than one maintainer, this document will be replaced by one
describing a real decision procedure among them, and the change from "the
maintainer decides" to something else will itself follow the process above.
