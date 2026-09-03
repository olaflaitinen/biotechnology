# Threat model

What this project believes its risks are, what it does about each of them, and
what it explicitly accepts.

Written so that an organisation evaluating whether to depend on this package
can check our reasoning rather than take our word for it. Every control listed
is either enforced by a named file in this repository or is honestly marked as
a manual practice.

**Last reviewed: 2026-09-02. Reviewed at every minor release.**

---

## 1. What is being protected, and from whom

### 1.1 Assets

| Asset | Why it matters |
|-------|----------------|
| **The published artefact on PyPI** | Executes on the machines of universities, hospitals, regulators and public administrations. |
| **The repository contents** | The source of the artefact, and a citable reference work in its own right. |
| **The factual content** | Cited in curricula, reports and policy documents. Corrupted content misleads without ever executing anything. |
| **The published documentation site** | Runs in every reader's browser. |
| **The maintainer's publishing identity** | The ability to release as this project. |
| **Contributor trust** | Once lost, corrections stop arriving, and corrections are the whole point. |

### 1.2 Adversaries considered

| Adversary | Motivation | Capability assumed |
|-----------|-----------|---------------------|
| **Opportunistic supply-chain attacker** | Reach downstream machines cheaply | Can compromise a popular action or a development-time package; can typosquat |
| **Targeted supply-chain attacker** | Reach one specific downstream organisation | Can phish the maintainer, can compromise a maintainer device |
| **Malicious contributor** | Insert a subtle change | Can open a pull request, can be patient, can build reputation first |
| **Well-meaning but wrong contributor** | Genuinely believes an incorrect fact | Ordinary contributor access |
| **Dual-use seeker** | Extract operationally useful harm information | Can open issues, can propose content, can frame requests as research |
| **Denial-of-service actor** | Waste maintainer or CI resources | Can open many issues, can send pathological input |

### 1.3 Explicitly out of scope

Stated so that nobody assumes a protection that does not exist.

- **The correctness of the biology.** No control in this document stops a
  plausible, well-cited, wrong fact from entering the taxonomy. That risk is
  managed editorially, not technically, and it is the largest residual risk
  this project carries. See section 5.
- **A compromise of GitHub or PyPI themselves.** Out of our control. Provenance
  attestation limits what such a compromise could do undetected, but does not
  prevent it.
- **A compromise of the maintainer's device.** Mitigated by signed tags and by
  environment protection on publication, but a fully compromised device
  defeats both.
- **What downstream users do with the data.** The library is a reference work,
  not validated software. See `NOTICE.md` section 6.

---

## 2. Structural properties that remove risk classes entirely

The strongest security property of this project is what it does not do. Each
line below removes a class of attack rather than mitigating it, and each is
checked mechanically.

| Property | Risk class removed | Enforced by |
|----------|--------------------|-------------|
| **Zero runtime dependencies** | Every transitive dependency compromise | Automated check, run in CI, in the security audit, in dependency review and as a pre-commit hook |
| **No network capability** | Data exfiltration, callback, beaconing | `security-audit.yml`, job `attack-surface` |
| **No code execution primitives** | Deserialisation attacks, command injection, sandbox escape | `security-audit.yml`, job `attack-surface`, greps for `subprocess`, `os.system`, `eval`, `exec`, `pickle`, `marshal`, `ctypes` |
| **No filesystem writes except an explicit export path** | Path traversal, arbitrary write | Automated check, security audit |
| **No parsing of untrusted input at import** | Deserialisation of hostile data | The taxonomy is compiled into the package as Python literals |
| **No secrets in the repository or in CI** | Credential theft | Trusted publishing, `gitleaks` in pre-commit and in CI, GitHub secret scanning |
| **No `pull_request_target`** | Fork code running with write permissions | `security-audit.yml`, job `workflows` |
| **No third-party origin on the documentation site** | Script injection into every reader's browser | Automated check, documentation build |

---

## 3. Threats, ranked by expected loss

### T-01. Compromised GitHub Action

**Scenario.** A third-party action used in a workflow is compromised upstream.
It runs with the repository's `GITHUB_TOKEN` and can read anything the job can
read, modify the working tree before a build, or exfiltrate to an external
host.

**Why it is ranked first.** It is the largest real attack surface in this
repository, and it is the one that has repeatedly been exploited in the wild
against projects with otherwise good hygiene.

**Controls.**

- Every `uses:` reference is recorded in `.github/action-pins.yml` with a
  pinned commit SHA, a review date and a justification.
  An automated check fails CI on any reference that is not governed by that
  file.
- Top-level `permissions: {}` in every workflow. Each job re-grants only what
  it needs; most get `contents: read` and nothing else.
- `persist-credentials: false` on every checkout, so the token is not left in
  `.git/config` for a later step to read.
- `id-token: write` exists in exactly three jobs, all of them named and
  reviewed: publish, attest and scorecard.
- Dependabot checks actions weekly rather than monthly.
- `zizmor` and `actionlint` run on every change to a workflow.

**Residual risk.** A compromise of an action between the pin being set and the
next review window. Accepted, and bounded by least-privilege permissions.

---

### T-02. Malicious pull request

**Scenario.** A contributor opens a pull request whose CI run reads secrets,
writes to the repository, or poisons a cache that a later trusted run consumes.

**Controls.**

- `pull_request_target` is forbidden and its absence is checked on every run.
  This single control removes the standard version of this attack.
- Fork pull requests run with read-only permissions and no secrets, which is
  GitHub's default and is not overridden anywhere.
- Deployment jobs are gated on `github.event_name == 'push'` and on
  `github.ref == 'refs/heads/main'`.
- Publication runs in a protected environment that can require human approval.
- `CODEOWNERS` routes every workflow change and every governance document to
  the maintainer.
- No workflow interpolates an untrusted expression such as a pull request title
  or body into a `run:` block, which is the standard script-injection vector.
  `zizmor` checks this.

**Residual risk.** A subtle logic change in the library itself, reviewed and
merged in good faith. Mitigated by review, not eliminated.

---

### T-03. Compromised development-time package

**Scenario.** `ruff`, `black`, `mypy`, `pytest`, `mkdocs` or another tool in
the optional extras is compromised. It executes on maintainer machines and in
CI, though never on a user's machine.

**Controls.**

- These are optional extras, never runtime dependencies, so a compromise never
  reaches a user through this package.
- `pip-audit --strict` runs daily over the installed development environment.
- `dependency-review` blocks a pull request that introduces a package with a
  known advisory at any severity, including low.
- Dependabot groups and proposes updates monthly, with major bumps of the
  formatting tools deliberately held back so that a reformatting commit is
  never merged unread.
- The published wheel is separately audited in an isolated environment, so that
  a development-time compromise cannot silently reach the artefact.

**Residual risk.** A zero-day in a development tool between disclosure and the
next daily audit. Accepted.

---

### T-04. Malicious input to the library

**Scenario.** An application passes attacker-controlled strings to `get()`,
`search()` or a formula. The realistic outcome is denial of service through
catastrophic backtracking, not code execution, because there is nothing to
execute.

**Controls.**

- Path parsing uses anchored, bounded expressions and rejects anything outside
  `[a-z0-9_.]` before matching. Depth is capped at two segments.
- Search is a linear scan over a fixed, small corpus with no user-supplied
  pattern compilation. A user string is a substring needle, never a regular
  expression.
- Formulas validate their domain and raise `DomainError` naming the parameter,
  the value and the accepted range, rather than letting `math` raise from deep
  inside a pipeline.
- CodeQL runs `security-and-quality`, which includes the polynomial
  backtracking queries.

**Residual risk.** Low. The corpus is fixed at build time and small.

---

### T-05. Leaked credential in the repository

**Scenario.** A contributor commits a token, key or password, whether in code,
in a test fixture, or in a screenshot.

**Why it is ranked here despite there being no project secrets.** The risk is
to the contributor's own credential, not to ours, and it is not repairable
after the fact: a public commit must be assumed compromised even after a force
push.

**Controls.**

- `gitleaks` runs as a pre-commit hook, so the commit is stopped before it
  exists.
- `gitleaks` runs again over the full history in the daily security audit.
- GitHub secret scanning and push protection.
- `detect-private-key` in the pre-commit hygiene set.
- `.gitignore` lists `.env`, `.pypirc`, `*.pem`, `*.key`, `*.p12`, `.secrets/`.
- The project itself holds no secret to leak.

---

### T-06. Stolen or misused publishing identity

**Scenario.** An attacker publishes a malicious version of the package to PyPI
under this project's name.

**Controls.**

- **No PyPI API token exists.** Publication uses trusted publishing over
  OpenID Connect. PyPI verifies the specific repository, workflow and
  environment and issues a token valid for one upload. There is nothing to
  steal.
- Publication runs only from a tag matching a strict pattern.
- The tag must be **signed**, and `git verify-tag` gates the release job.
- Version consistency across the tag, `pyproject.toml` and `CITATION.cff` is
  enforced before anything is built.
- A `CHANGELOG.md` entry with a data freeze date is required.
- `actions/attest-build-provenance` signs a statement binding each artefact to
  the commit, workflow and runner that produced it. A consumer can verify with
  `gh attestation verify`.
- The `pypi` environment can require reviewer approval.

**Residual risk.** A fully compromised maintainer device could produce a signed
tag. Environment protection with a second reviewer is the intended mitigation
once a second maintainer exists. See `GOVERNANCE.md` section 6.

---

### T-07. Compromised documentation site

**Scenario.** The published site loads a script from a third party which is
later compromised, executing in the browser of every reader.

**Controls.**

- The site loads **no third-party JavaScript, stylesheet or font**. MathJax is
  vendored into `docs/javascripts/` and served same-origin.
- An automated check fails the documentation build if any external origin
  appears in the built output.
- Deployment happens only from a push to `main`, never from a fork.
- `pages: write` is held by one small job that does nothing except deploy.

---

### T-08. Dual-use content

**Scenario.** Content that functions as operational instructions for causing
harm enters the repository, whether through a contribution, an incremental
accumulation across several merges, or a well-argued request framed as
research or education.

**Why it is in a threat model at all.** Because for a project with a `dark`
branch it is a real adversarial scenario with a motivated adversary, not a
content-policy footnote.

**Controls.**

- `SECURITY.md` section 2 states exactly what is out of scope, in every facet
  of every record, in every branch.
- An automated dual-use screen scans the taxonomy on every commit, in
  pre-commit and in CI.
- `tests/test_dark_branch_is_defensive.py` runs in the test suite.
- `CODEOWNERS` never delegates the `dark` branch, even after domain editors
  exist for the other nine.
- The policy is exempt from consensus. `GOVERNANCE.md` section 3.4 says so, and
  a stated purpose does not change the outcome because the published text is
  identical either way.
- Private reporting channel for content concerns, so that a report does not
  have to quote the material in a public issue.

**Residual risk.** Judgement. The automated screen is a floor, not a ceiling,
and both documents say so.

---

### T-09. Factually wrong content merged in good faith

**Scenario.** A plausible, well-presented, incorrect fact enters the taxonomy
and is cited downstream.

**Why it is listed here.** Because it is the **highest-probability harm this
project can cause**, and a threat model that omitted it because it is not a
software vulnerability would be dishonest. No firewall stops a wrong number.

**Controls.**

- Corrections are settled by citation, not by seniority. `GOVERNANCE.md` 3.1.
- Every claim carries an `EvidenceLevel`, so a reader can filter to settled
  material.
- Every release records a **data freeze date**, so nobody mistakes an old
  regulatory citation for a current one.
- `NOTICE.md` section 6 states plainly that metrics are orientation figures and
  must never set a dose, a limit or a safety threshold.
- Cross-references are validated mechanically, so a reader can always reach the
  related record and cross-check.
- The data correction issue template is the first template, is the easiest to
  file, and requires no programming knowledge.

**Residual risk.** High, and openly acknowledged. The mitigation is more
reviewers, which is why `CONTRIBUTING.md` ranks factual corrections above
everything else and why `GOVERNANCE.md` seeks domain editors.

---

### T-10. Typosquatting and impersonation

**Scenario.** A malicious package with a similar name, or a repository claiming
to be an official mirror.

**Controls.**

- The canonical locations are stated in `README.md`, `CITATION.cff`,
  `NOTICE.md` and `pyproject.toml` project URLs.
- Build provenance lets a consumer verify that an artefact came from this
  repository.
- The EUPL-1.2 permits forks, and that is intended. A fork is not
  impersonation; a fork claiming to be *this* project is.

**Residual risk.** Accepted. Namespace policing is not within the means of an
unfunded academic project.

---

## 4. Control summary

| Control | File | Runs |
|---------|------|------|
| No runtime dependencies | Automated check, CI and pre-commit | pre-commit, CI, security audit, dependency review |
| No code execution primitives | `security-audit.yml` | push, pull request, daily |
| No network capability | `security-audit.yml` | push, pull request, daily |
| No filesystem writes | Automated check, security audit | security audit |
| Action pinning | Automated check, CI and pre-commit | pre-commit, CI, security audit |
| Workflow permissions | Automated check, security audit | security audit |
| No `pull_request_target` | `security-audit.yml` | security audit |
| Secret scanning | `gitleaks` | pre-commit, daily over full history |
| Dependency advisories | `pip-audit`, `dependency-review` | daily, and on every pull request |
| Static analysis | `bandit`, `semgrep` rules, CodeQL | push, pull request, weekly |
| Workflow static analysis | `actionlint`, `zizmor` | pre-commit, security audit |
| Supply-chain posture | OpenSSF Scorecard | weekly, published |
| Build provenance | `attest-build-provenance` | release |
| Signed tags | `git verify-tag` | release |
| Trusted publishing | PyPI OIDC | release |
| Software bill of materials | CycloneDX | release |
| Dual-use screen | Automated dual-use screen, CI and pre-commit | pre-commit, CI |
| Site origin check | Automated check, documentation build | documentation build |

---

## 5. Accepted risks

Listed plainly, because an unstated accepted risk is an undisclosed one.

1. **Factual error is the dominant residual risk.** See T-09. It is managed
   editorially and it is not eliminated.
2. **Bus factor of one.** See `GOVERNANCE.md` section 6. Mitigated by a
   copyleft licence, no proprietary infrastructure, and documented
   architecture, but not eliminated.
3. **Regulatory citations decay.** Every release records a data freeze date.
   Nothing claims currency beyond it.
4. **European regulatory bias.** Stated in `NOTICE.md` and `CONTRIBUTING.md`.
   It is a coverage gap, not a hidden distortion.
5. **English only.** The plain-language register, which exists precisely for
   non-specialist readers, is unavailable to anyone who does not read English.
6. **A compromised maintainer device defeats signed tags.** Mitigated by
   environment protection, which needs a second person to be fully effective.
7. **Action pin review windows.** A pinned SHA is trusted between reviews.

---

## 6. Reporting

Security concerns go to <yunus.imanov@metropolia.fi>, never to a public issue.
See `SECURITY.md` for what to include and what response times to expect.

If you believe this threat model is wrong, incomplete, or too generous to
itself, that is also worth an email. A threat model nobody argues with is
usually one nobody has read.
