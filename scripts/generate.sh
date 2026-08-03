#!/usr/bin/env bash
#
# Regenerate src/yazio_sdk/ from spec/openapi.yaml.
#
# Everything under src/yazio_sdk/ is a build artifact. Never edit it by hand:
# the next release overwrites the lot. Fixes belong in the spec repo
# (yazio-community/yazio-api-specification) or in this script's post-steps.
#
# Usage:  nix-shell --run scripts/generate.sh
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

spec="${1:-spec/openapi.yaml}"
package="src/yazio_sdk"

if ! command -v openapi-python-client >/dev/null 2>&1; then
  echo "error: openapi-python-client not found — run inside 'nix-shell'." >&2
  exit 1
fi

# The package version *is* the spec version, read out of the spec rather than
# tracked separately — that is what makes the two impossible to drift, since
# there is no second place to forget to update. The spec repo's release
# workflow stamps info.version from the git tag, so a downloaded release always
# carries the right value. An unreleased local bundle says 0.0.0-dev, which is
# fine for local work and is rejected before publishing.
spec_version="$(python3 - "$spec" <<'PY'
import sys

import yaml

with open(sys.argv[1]) as handle:
    spec = yaml.safe_load(handle)

version = spec.get("info", {}).get("version")
if not version:
    raise SystemExit(f"error: {sys.argv[1]} has no info.version")
print(version)
PY
)"

echo "==> generating $package/ from $spec (spec version $spec_version)"

# Nothing under src/ is committed — the package is generated and gitignored —
# and git cannot track an empty directory, so a fresh clone has no src/ at all.
# openapi-python-client creates its output directory with a plain os.mkdir,
# which fails rather than creating the parent, so make the parent here.
mkdir -p "$(dirname "$package")"

# --meta=none emits just the importable package, no pyproject or setup.py of its
# own — this repo's pyproject.toml owns the packaging. With --meta=none the
# output path *is* the package directory, hence src/yazio_sdk rather than src/.
openapi-python-client generate \
  --path "$spec" \
  --config openapi-python-client.yaml \
  --meta none \
  --output-path "$package" \
  --overwrite

rm -rf "$package/.ruff_cache"

# Written after generation because the generator owns every other file in that
# directory. `__version__` is what hatchling reads for the distribution version
# (see [tool.hatch.version] in pyproject.toml); SPEC_VERSION is the same string
# under the name that explains why, so a bug report can name a spec release
# rather than a date.
cat > "$package/_version.py" <<EOF
"""Written by scripts/generate.sh from the spec's info.version. Do not edit."""

__version__ = "${spec_version}"

# The SDK is versioned as the spec it was generated from, so these are one
# string. See the spec repo's CONTRIBUTING for why.
SPEC_VERSION = __version__
EOF

if ! grep -q "_version" "$package/__init__.py"; then
  cat >> "$package/__init__.py" <<'EOF'

from ._version import SPEC_VERSION as __spec_version__  # noqa: E402
from ._version import __version__  # noqa: E402
EOF
fi

echo "==> verifying the generated package imports"
PYTHONPATH="$repo_root/src${PYTHONPATH:+:$PYTHONPATH}" \
  python3 "$repo_root/scripts/verify_imports.py"

echo "==> done"
