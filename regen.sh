#!/usr/bin/env bash
# Regenerate the public Python SDK (geopera) from the Geopera OpenAPI, then re-apply
# the publish polish (metadata + README + LICENSE) the generator overwrites.
#
#   ./regen.sh                                          # build from the committed spec snapshot
#   GEOPERA_API_URL=https://api.geopera.com ./regen.sh   # refresh the spec from a live backend first
#
# A SCRUB + FENCE runs on EVERY regen (whether the spec came from a live dump or the
# committed snapshot), so a public SDK can NEVER expose the internal surface:
#   - drops every admin/internal operation (*.admin.*, *_internal, diagnostics, …)
#   - prunes component schemas down to the closure the customer ops actually use
#     (so admin input/output model names don't leak either)
#   - strips internal prose from descriptions (money-path/CU/legacy/provenance/
#     service-role/password_hash/"the kernel …") + internal x-* extensions
#   - retitles to "Geopera Operations"
#   - FENCE: aborts the build if any admin/internal op or internal phrase survives.
#
# Needs: openapi-python-client on PATH (pip/pipx install openapi-python-client).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SPEC="$HERE/openapi.json"
RAW="$(mktemp)"; trap 'rm -f "$RAW"' EXIT

# 1) Obtain the RAW spec: a live dump (full surface, incl. admin ops) or the snapshot.
if [[ -n "${GEOPERA_API_URL:-}" ]]; then
  echo "refreshing spec from $GEOPERA_API_URL ..."
  python3 -c "import sys,urllib.request,shutil; shutil.copyfileobj(urllib.request.urlopen(sys.argv[1]+'/openapi.json'), open(sys.argv[2],'wb'))" "$GEOPERA_API_URL" "$RAW"
else
  echo "using committed spec $SPEC (set GEOPERA_API_URL to refresh it)"
  cp "$SPEC" "$RAW"
fi

# 2) SCRUB the raw spec into a customer-safe public spec, then FENCE it (scrub_spec.py).
python3 "$HERE/scrub_spec.py" "$RAW" "$SPEC"

# 3) Codegen + re-apply publish metadata (the generator wipes pyproject/README/LICENSE).
openapi-python-client generate --path "$SPEC" \
  --config "$HERE/opc-config.yaml" \
  --output-path "$HERE/geopera-sdk" --overwrite --meta poetry

python3 "$HERE/patch_metadata.py"
echo "regen complete -> $HERE/geopera-sdk"
