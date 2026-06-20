#!/usr/bin/env bash
# Regenerate the Geopera Python SDK package from the committed OpenAPI spec.
#
#   ./regen.sh
#
# Generates geopera-sdk/ from openapi.json, then re-applies the PyPI metadata + curated
# README + LICENSE that the generator overwrites. Do not hand-edit geopera-sdk/ — change
# the spec or patch_metadata.py instead.
#
# Needs: openapi-python-client (pip/pipx install openapi-python-client).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

openapi-python-client generate --path "$HERE/openapi.json" \
  --config "$HERE/opc-config.yaml" \
  --output-path "$HERE/geopera-sdk" --overwrite --meta poetry

python3 "$HERE/patch_metadata.py"
echo "regen complete -> $HERE/geopera-sdk"
