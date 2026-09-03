<!--
  GENERATED FILE. Do not edit.
  Produced from SECURITY.md.
  Edit the source and run `make docs`.
-->

# Security policy

This project has two kinds of security concern, and they are handled
differently. Please read the right section.

| Concern | Section |
|---------|---------|
| A software vulnerability in the package | [1](#1-software-vulnerabilities) |
| Content that could function as instructions for harm | [2](#2-dual-use-content-policy) |
| How the supply chain is protected | [3](#3-supply-chain-security) |
| What this software is and is not qualified for | [4](#4-scope-disclaimer) |

A full analysis of what this project believes its risks are, what it does about
each, and what it accepts, is in [`THREAT_MODEL.md`](threat-model.md).

---

## 1. Software vulnerabilities

### 1.1 Supported versions

| Version | Supported | Notes |
|---------|:---------:|-------|
| 0.1.x | Yes | Current |
| Below 0.1 | No | Pre-release |

Until 1.0, only the latest minor release receives fixes. After 1.0 the intent
is to support the current and the previous minor release.

### 1.2 Attack surface

The attack surface is deliberately small, and every claim below is checked
mechanically on every commit rather than asserted.

| Property | Checked by |
|----------|-----------|
| **No runtime dependencies.** Nothing is installed beyond the standard library, so there is no transitive dependency risk. | Automated check, CI and pre-commit |
| **No network access.** The package never opens a socket. | `security-audit.yml`, job `attack-surface` |
| **No code execution primitives.** No `subprocess`, `os.system`, `eval`, `exec`, `pickle`, `marshal` or `ctypes` anywhere in `src/`. | `security-audit.yml`, job `attack-surface` |
| **No filesystem writes**, except to a path the caller passes explicitly to `export`. | Automated check, security audit |
| **No deserialisation of untrusted input.** The taxonomy is compiled into the package as Python literals; nothing is parsed from user data at import. | Structural |
| **No secrets.** The project holds none, and publication uses trusted publishing rather than a token. | `gitleaks`, GitHub secret scanning |

The realistic risk classes that remain are: a supply-chain compromise of the
published artefact, a denial of service through pathological input to the
search or path parser, and a vulnerability in a development-time tool. All
three are analysed in [`THREAT_MODEL.md`](threat-model.md).

### 1.3 Reporting a vulnerability

**Do not open a public issue for a vulnerability.**

Two channels, either is fine:

1. **GitHub private vulnerability reporting**, from the Security tab of the
   repository. Preferred, because it keeps the discussion attached to the
   project.
2. **Email** <yunus.imanov@metropolia.fi>.

Please include:

- a description of the issue and the class of vulnerability;
- the version affected, and the earliest version you know to be affected;
- steps to reproduce, or a proof of concept;
- the impact as you assess it, and any assumptions that assessment rests on;
- whether the issue is already public anywhere;
- how you would like to be credited, if at all.

If the issue looks like it may be exploitable, please describe the class of
problem rather than sending a fully weaponised exploit.

### 1.4 What to expect

| Stage | Target |
|-------|--------|
| Acknowledgement of your report | 5 working days |
| Initial assessment and a severity judgement | 10 working days |
| Fix released, or a written plan with dates | 90 days |
| Public disclosure | After a fix, or by agreement |

Coordinated disclosure is preferred. Credit is given in
[`CHANGELOG.md`](changelog.md) and [`AUTHORS.md`](https://github.com/olaflaitinen/biotechnology/blob/main/AUTHORS.md) unless you ask
otherwise.

**There is no bug bounty.** This is an unfunded academic project with one
maintainer. That is stated plainly so that nobody spends effort expecting one.

### 1.5 Safe harbour

If you make a good-faith effort to comply with this policy during your
research, we will consider your research authorised, we will work with you to
understand and resolve the issue quickly, and we will not pursue or support
legal action against you.

Good faith means: you avoid privacy violations, data destruction and service
degradation; you only interact with systems you own or have permission to
test; you give us reasonable time to respond before disclosing; and you do not
exploit an issue beyond the minimum needed to demonstrate it.

This safe harbour covers this project. It cannot bind GitHub, PyPI, Read the
Docs or any other third party.

---

## 2. Dual-use content policy

This is a library about biotechnology, and one of its ten branches, `dark`, is
explicitly about the harmful potential of the field: bioterrorism, biological
weapons, and accidental release. That branch is not an oversight and it is not
a gap in judgement. It is documented deliberately, and it is documented
**exclusively from the protective side**.

### 2.1 What the `dark` branch contains

Biosafety and containment. Biosecurity governance. Dual-use research oversight.
Gene synthesis screening. Biosurveillance and early detection. Biodefence and
medical countermeasures. Microbial forensics and attribution. Biological arms
control and the Biological Weapons Convention.

Every one of these is defensive, institutional or diplomatic. They describe the
apparatus by which societies keep biological research safe, from accident and
from deliberate misuse, and they are the subjects of a large open literature,
of United Nations treaty processes, and of university courses.

### 2.2 What it does not, and will not, contain

The following are out of scope in **every facet** of **every record**, in
**every branch** of this taxonomy, regardless of stated intent:

- synthesis, acquisition or production routes for dangerous pathogens or
  toxins;
- methods to enhance transmissibility, virulence, environmental stability or
  host range;
- methods to defeat detection, screening, containment or medical
  countermeasures;
- weaponisation, formulation, stabilisation or dissemination information of any
  kind;
- target selection, vulnerability assessment of specific facilities or
  populations, or anything that reads as operational planning;
- quantities, thresholds or parameters whose only use is operational;
- any content that functions as a protocol rather than as a description of a
  governance problem.

### 2.3 How this is enforced

- An automated dual-use screen runs as a pre-commit hook and in CI. It scans
  the full text of the `dark` branch and applies a narrower screen across the
  whole taxonomy, for operational framing.
- `tests/test_dark_branch_is_defensive.py` runs in the test suite.
- [`CODEOWNERS`](https://github.com/olaflaitinen/biotechnology/blob/main/.github/CODEOWNERS) never delegates the `dark` branch, even
  after domain editors exist for the other nine.
- Every issue and pull request template carries a dual-use declaration.

The automated screen is a **floor, not a ceiling**. Maintainer judgement
applies above it, and a contribution that passes the screen may still be
rejected on review.

The maintainers will not negotiate about this. A stated purpose, meaning
research, education, fiction or testing, does not change the outcome, because
the published text is identical either way. This is the one area of the project
explicitly exempted from consensus in [`GOVERNANCE.md`](governance.md) section
3.4.

### 2.4 Reporting a content concern

If you believe something in this repository crosses that line, in the `dark`
branch or anywhere else, please report it **privately** to
<yunus.imanov@metropolia.fi> rather than opening a public issue that quotes it.

Include the file path, the specific text, and why you assess it as operational
rather than descriptive. Reports of this kind are treated with the same
priority as a software vulnerability, and material judged to cross the line is
removed first and discussed afterwards.

### 2.5 Why the branch exists at all

Removing it would not make anyone safer. The colour scheme this library
documents includes `dark` as one of its ten branches; a taxonomy that silently
omitted it would be an inaccurate description of how the field is taught and
discussed.

More importantly, the subject matter of the branch, meaning containment
standards, oversight of risky research, synthesis screening, treaty compliance,
is exactly the material that policy staff, journalists and students need in
order to understand and argue about biosecurity, and it is poorly served by
existing accessible sources.

The choice made here is to cover the governance of the risk, thoroughly and in
plain language, and to cover nothing else.

---

## 3. Supply chain security

### 3.1 Release integrity

| Control | What it gives a consumer |
|---------|--------------------------|
| **Trusted publishing** over OpenID Connect | There is no PyPI API token to steal. PyPI verifies this repository, this workflow and this environment, and issues a token valid for one upload. |
| **Signed tags**, verified by `git verify-tag` before anything builds | The release originated from a tag the maintainer signed. |
| **Build provenance attestation** | A cryptographic statement binding each artefact to the commit, workflow and runner that produced it. |
| **CycloneDX SBOM** attached to each release | An ingestible bill of materials, rather than one reconstructed by guesswork. |
| **Version consistency gate** | The tag, `pyproject.toml` and `CITATION.cff` must agree, and a `CHANGELOG.md` entry with a data freeze date must exist. |
| **Environment protection** on the `pypi` environment | Publication can require human approval. |

### 3.2 Verifying a release

```bash
# Verify that a wheel came from this repository.
gh attestation verify biotechnology-0.1.0-py3-none-any.whl \
   --repo olaflaitinen/biotechnology

# Compare against the checksums recorded in the GitHub release notes.
sha256sum biotechnology-0.1.0-py3-none-any.whl

# Confirm the installed package pulled in nothing.
python -m venv /tmp/check
/tmp/check/bin/pip install biotechnology
/tmp/check/bin/pip list
```

The last command should list `biotechnology` and nothing else beyond `pip`,
`setuptools` and `wheel`. If it lists anything more, something is wrong and we
would like to hear about it.

### 3.3 Repository hardening

- Every workflow declares a top-level `permissions: {}` and grants each job the
  minimum it needs. Checked in the security audit.
- Every checkout uses `persist-credentials: false`.
- `pull_request_target` is forbidden and its absence is checked on every run.
- Every action reference is governed by `.github/action-pins.yml` and checked
  in CI and pre-commit.
- `actionlint` and `zizmor` analyse the workflows themselves.
- OpenSSF Scorecard runs weekly and its result is published to the public
  dataset, so that a downstream consumer can query it without asking us.

### 3.4 Continuous checks

| Check | Tool | Frequency |
|-------|------|-----------|
| Semantic code analysis | CodeQL, `security-and-quality` | push, pull request, weekly |
| Python security linting | Bandit | pre-commit, push, pull request |
| Dependency advisories | `pip-audit --strict` | daily |
| New dependency review | `dependency-review-action` | every pull request |
| Secret scanning | `gitleaks`, GitHub push protection | pre-commit, daily over full history |
| Workflow security | `actionlint`, `zizmor` | pre-commit, push |
| Supply-chain posture | OpenSSF Scorecard | weekly |
| Attack-surface assertions | `security-audit.yml` | push, pull request, daily |

---

## 4. Scope disclaimer

**This library is a reference work, not validated software.**

It is not qualified under any medical device, in vitro diagnostic, clinical
laboratory, GxP, or functional-safety framework, and must not be used as if it
were. In particular:

- **`Metric` ranges are orientation figures** carrying an explicit evidence
  grade. They are not specifications and must never set a dose, a limit, a
  release criterion or a safety threshold.
- **`formulas` modules implement published relationships** for teaching and
  estimation. Verify against the primary source cited in each module's
  `derivation.py` before any decision depends on the result.
- **Regulatory citations were accurate** to the best of the author's knowledge
  at the data freeze date recorded in [`CHANGELOG.md`](changelog.md). Law
  changes. Verify against the current official text.
- **Nothing here is medical, veterinary, legal, regulatory, investment or
  biosafety advice.**

See [`NOTICE.md`](https://github.com/olaflaitinen/biotechnology/blob/main/NOTICE.md) section 6 for the full disclaimer, and
[`THREAT_MODEL.md`](threat-model.md) section 5 for the risks this project
accepts rather than mitigates.

---

## 5. Contact

| Purpose | Route |
|---------|-------|
| Software vulnerability | GitHub private vulnerability reporting, or <yunus.imanov@metropolia.fi> |
| Dual-use content concern | <yunus.imanov@metropolia.fi>, privately |
| Code of conduct | <yunus.imanov@metropolia.fi> |
| Everything else | A public issue |

Machine-readable contact metadata is published at
[`.well-known/security.txt`](https://github.com/olaflaitinen/biotechnology/blob/main/.well-known/security.txt).
