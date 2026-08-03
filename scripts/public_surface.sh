#!/usr/bin/env bash
#
# Print the generated package's public surface, one symbol per line, sorted.
#
# src/yazio_sdk/ is not committed, so a "regenerate from spec vX.Y.Z" PR is a
# one-line spec bump that says nothing about what it does to callers. Diffing
# this listing before and after is what makes that visible: a removed or
# renamed line here is a breaking change for anyone importing it.
#
# Usage:  scripts/public_surface.sh [package-dir]
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
package="${1:-$repo_root/src/yazio_sdk}"

if [ ! -d "$package" ]; then
  echo "error: $package does not exist — run scripts/generate.sh first" >&2
  exit 1
fi

{
  # Client functions, as callers import them: yazio_sdk.api.<tag>.<operation>.
  # The module name comes from the spec's operationId, so a renamed operationId
  # shows up here as one removal and one addition.
  find "$package/api" -name '*.py' ! -name '__init__.py' -print0 2>/dev/null \
    | while IFS= read -r -d '' file; do
        tag="$(basename "$(dirname "$file")")"
        printf 'api      %s.%s\n' "$tag" "$(basename "$file" .py)"
      done

  # Model classes, as callers import them from yazio_sdk.models.
  find "$package/models" -name '*.py' ! -name '__init__.py' -print0 2>/dev/null \
    | while IFS= read -r -d '' file; do
        printf 'model    %s\n' "$(basename "$file" .py)"
      done
} | LC_ALL=C sort
