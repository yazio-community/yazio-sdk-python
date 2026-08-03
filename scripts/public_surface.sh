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

# An absent package has an empty surface. That is the honest answer rather than
# an error: this script's whole job is to be one side of a before/after diff,
# and "nothing was here yet" is a real before-state — it is what the regenerate
# workflow sees on a branch whose package has not been generated into it yet.
# Every symbol then shows up as an addition, which is correct.
#
# The note goes to stderr so an interactive run still says why it printed
# nothing, without putting anything in the diff.
if [ ! -d "$package" ]; then
  echo "note: $package does not exist — reporting an empty surface" >&2
  exit 0
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
