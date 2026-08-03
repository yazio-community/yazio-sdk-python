# Everything here expects the nix-shell: `nix-shell --run "make generate"`.

SPEC_REPO ?= yazio-community/yazio-api-specification
SPEC_TAG  ?= latest
SPEC      ?= spec/openapi.yaml

.PHONY: help sync generate version docs lint check

help:
	@echo "make sync      download the $(SPEC_TAG) spec release into spec/, then regenerate"
	@echo "make generate  regenerate src/yazio_sdk/ from the spec already in spec/"
	@echo "make version   print the version this checkout would publish"
	@echo "make docs      render HTML API docs into $(DOCS_DIR)"
	@echo "make check     what CI runs: generate, lint"

# The downloaded asset carries its own version in info.version — the spec repo's
# release workflow stamps it from the git tag — so there is nothing to record
# here. generate.sh reads it back out, which is why the package version cannot
# disagree with the spec it was built from.
sync:
	@set -eu; \
	if [ "$(SPEC_TAG)" = "latest" ]; then \
	  url="https://github.com/$(SPEC_REPO)/releases/latest/download/openapi.yaml"; \
	else \
	  url="https://github.com/$(SPEC_REPO)/releases/download/$(SPEC_TAG)/openapi.yaml"; \
	fi; \
	echo "==> fetching spec from $$url"; \
	curl -sSLf "$$url" -o $(SPEC)
	$(MAKE) generate

generate:
	scripts/generate.sh

version:
	@hatch version

# Docs render from the generated package's docstrings, which come from the
# spec's summaries and descriptions — so this is really a view of the spec, and
# it is a build output rather than something to commit. Default target is
# outside the repo for that reason.
DOCS_DIR ?= /tmp/yazio-sdk-docs

# `pdoc yazio_sdk` on its own emits two pages: the generated __init__.py
# declares __all__, and pdoc honours that by documenting only the two names in
# it — so all 149 endpoint functions and models get skipped. Naming the members
# one level down works around that, and pdoc recurses from there on its own.
# Going deeper would list each module twice and warn about every one.
docs: generate
	pdoc $$(cd src && find yazio_sdk -maxdepth 1 \( -name '*.py' -o -type d \) \
	  ! -name '__init__.py' ! -name '_*' \
	  | sed 's|\.py$$||; s|/|.|g' | sort) \
	  --output-directory $(DOCS_DIR) \
	  --docformat google
	@echo
	@echo "open file://$(DOCS_DIR)/yazio_sdk.html"

# No explicit paths: naming src/ on the command line would override the
# extend-exclude in pyproject.toml that keeps ruff off the generated tree.
lint:
	ruff check .
	ruff format --check .

# There is no test suite. What would have been a smoke test is inside
# scripts/generate.sh, which imports every generated module after writing it —
# that is the check worth running, and it runs on every generation rather than
# only when someone remembers to. A fresh clone has no package until this runs.
check: generate
	$(MAKE) lint
