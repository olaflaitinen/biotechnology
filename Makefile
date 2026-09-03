# =============================================================================
#  Makefile
# -----------------------------------------------------------------------------
#  The commands continuous integration runs, runnable identically on a laptop.
#
#  WHY A MAKEFILE IN A PYTHON PROJECT
#  Because "what do I run before opening a pull request?" must have exactly one
#  answer, and that answer must be the same locally and in CI. Every job in
#  .github/workflows/ invokes a target from this file or a script from tools/,
#  and nothing else, so a green local "make all" means a green pipeline.
#
#  PORTABILITY
#  POSIX make, GNU extensions avoided. Works with GNU make on Linux and macOS,
#  and with GNU make under Git Bash or WSL on Windows. PowerShell users without
#  make can read the recipes below and run them directly; each is a single
#  command line.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

PYTHON  ?= python
PIP     ?= $(PYTHON) -m pip
PKG     := biotechnology
SRC     := src/$(PKG)
TESTS   := tests
TOOLS   := tools
DOCS    := docs

.PHONY: help install install-dev clean test test-fast coverage lint format \
        typecheck validate policy security audit sbom pin-actions docs \
        docs-serve build check-dist citation precommit all ci stats tree \
        fix-dashes

.DEFAULT_GOAL := help

# -----------------------------------------------------------------------------
#  Self-documenting help.
# -----------------------------------------------------------------------------
help:
	@echo "biotechnology - available targets"
	@echo ""
	@echo "  Setup"
	@echo "    install        install the package"
	@echo "    install-dev    install with all development extras + pre-commit"
	@echo "    clean          remove build, cache and coverage artefacts"
	@echo ""
	@echo "  Quality"
	@echo "    test           full test suite with coverage"
	@echo "    test-fast      test suite excluding slow whole-taxonomy walks"
	@echo "    coverage       terminal + HTML coverage report"
	@echo "    lint           ruff + black --check"
	@echo "    format         apply ruff --fix and black"
	@echo "    typecheck      mypy --strict"
	@echo "    validate       taxonomy integrity suite"
	@echo "    policy         repository invariants: dependencies, dashes, pins"
	@echo "    precommit      run every pre-commit hook over all files"
	@echo ""
	@echo "  Security"
	@echo "    security       bandit + pip-audit + zizmor + attack-surface checks"
	@echo "    audit          dependency advisories only"
	@echo "    sbom           generate a CycloneDX bill of materials"
	@echo "    pin-actions    resolve action refs to commit SHAs (needs network)"
	@echo ""
	@echo "  Documentation"
	@echo "    docs           regenerate docs/ from the source of truth"
	@echo "    docs-serve     serve the documentation site locally"
	@echo ""
	@echo "  Release"
	@echo "    build          build sdist and wheel"
	@echo "    check-dist     twine check the built artefacts"
	@echo "    citation       validate CITATION.cff"
	@echo ""
	@echo "  Aggregate"
	@echo "    all            everything CI runs, in CI order"
	@echo "    ci             alias for all"
	@echo ""
	@echo "  Inspection"
	@echo "    stats          headline counts for the taxonomy"
	@echo "    tree           print the taxonomy as an indented tree"
	@echo "    fix-dashes     rewrite forbidden punctuation to ASCII"

# =============================================================================
#  Setup
# =============================================================================
install:
	$(PIP) install .

install-dev:
	$(PIP) install -e ".[dev]"
	pre-commit install
	pre-commit install --hook-type commit-msg

clean:
	rm -rf build dist .eggs *.egg-info
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov site
	rm -f bandit.sarif zizmor.sarif scorecard-results.sarif
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name "*.py[co]" -delete

# =============================================================================
#  Quality. Ordered by how fast they fail.
# =============================================================================
lint:
	$(PYTHON) -m ruff check $(SRC) $(TESTS) $(TOOLS)
	$(PYTHON) -m black --check --diff $(SRC) $(TESTS) $(TOOLS)

format:
	$(PYTHON) -m ruff check --fix $(SRC) $(TESTS) $(TOOLS)
	$(PYTHON) -m black $(SRC) $(TESTS) $(TOOLS)

typecheck:
	$(PYTHON) -m mypy $(SRC)

test:
	$(PYTHON) -m pytest $(TESTS) --cov=$(PKG) --cov-report=term-missing

test-fast:
	$(PYTHON) -m pytest $(TESTS) -m "not slow" -q

coverage:
	$(PYTHON) -m pytest $(TESTS) --cov=$(PKG) --cov-report=term-missing --cov-report=html
	@echo "HTML report written to htmlcov/index.html"

# The integrity suite is separated from `test` so that a contributor who has
# only changed a data record can run the fast, relevant check on its own.
validate:
	$(PYTHON) -m $(PKG) validate --strict
	$(PYTHON) $(TOOLS)/check_facets.py
	$(PYTHON) $(TOOLS)/check_enum_members.py
	$(PYTHON) $(TOOLS)/check_references.py
	$(PYTHON) $(TOOLS)/check_ascii.py
	$(PYTHON) $(TOOLS)/check_defensive.py
	$(PYTHON) $(TOOLS)/check_packaging.py
	$(PYTHON) -m pytest $(TESTS)/test_integrity.py -q

# Repository invariants that hold regardless of the taxonomy content. Fast
# enough to run constantly, and each failure prints its own remedy.
# -----------------------------------------------------------------------------
#  citations
#  Resolves every DOI in BIBLIOGRAPHY.md against Crossref. Separate from
#  `validate` because it needs the network, and a target that fails on a train
#  is a target people stop running. `--offline` verifies against the cache.
# -----------------------------------------------------------------------------
citations:
	$(PYTHON) $(TOOLS)/verify_references.py

citations-offline:
	$(PYTHON) $(TOOLS)/verify_references.py --offline


policy:
	$(PYTHON) $(TOOLS)/check_no_dependencies.py
	$(PYTHON) $(TOOLS)/check_dashes.py
	$(PYTHON) $(TOOLS)/check_action_pinning.py --strict
	$(PYTHON) $(TOOLS)/check_workflow_permissions.py
	$(PYTHON) $(TOOLS)/check_licence_headers.py

precommit:
	pre-commit run --all-files

fix-dashes:
	$(PYTHON) $(TOOLS)/check_dashes.py --fix

# =============================================================================
#  Security
#
#  Mirrors .github/workflows/security-audit.yml, so that a finding can be
#  reproduced locally rather than only read in a dashboard.
# =============================================================================
security: policy
	$(PYTHON) -m bandit -c pyproject.toml -r $(SRC) $(TOOLS)
	$(PYTHON) -m pip_audit --strict --progress-spinner off
	$(PYTHON) $(TOOLS)/check_no_writes.py
	@echo ""
	@echo "  Security checks passed. See THREAT_MODEL.md for what they cover"
	@echo "  and, importantly, for what they do not."

audit:
	$(PYTHON) -m pip_audit --strict --progress-spinner off

sbom: build
	$(PYTHON) -m cyclonedx_py environment \
		--output-format JSON \
		--output-file dist/$(PKG)-sbom.cdx.json
	@echo "SBOM written to dist/$(PKG)-sbom.cdx.json"

# Resolve every action ref in .github/action-pins.yml to a full commit SHA and
# rewrite the workflows to use it. Needs network access, so it is a deliberate
# maintainer action rather than something a contributor is asked to run.
pin-actions:
	$(PYTHON) $(TOOLS)/pin_actions.py --write
	$(PYTHON) $(TOOLS)/check_action_pinning.py --strict

# =============================================================================
#  Documentation
#  docs/ is GENERATED. Never edit it by hand; edit the source facet and re-run.
# =============================================================================
docs:
	$(PYTHON) $(TOOLS)/generate_docs.py --output $(DOCS)
	@echo "Regenerated $(DOCS)/ from $(SRC)/"

docs-serve: docs
	$(PYTHON) -m mkdocs serve

# =============================================================================
#  Release
# =============================================================================
build: clean
	$(PYTHON) -m build

check-dist: build
	$(PYTHON) -m twine check --strict dist/*

citation:
	cffconvert --validate

# =============================================================================
#  Aggregate. The contract: if `make all` passes, the pipeline passes.
# =============================================================================
all: lint typecheck policy validate test security docs check-dist citation
	@echo ""
	@echo "  All checks passed."

ci: all

# =============================================================================
#  Inspection helpers
# =============================================================================
stats:
	$(PYTHON) -m $(PKG) stats

tree:
	$(PYTHON) -m $(PKG) tree
