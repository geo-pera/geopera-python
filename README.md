# geopera-python

Source repo for **[`geopera`](https://pypi.org/project/geopera/)** — the official Python
client for the [Geopera](https://geopera.com) geospatial data platform.

> Looking for **how to use the SDK** (install, quickstart, auth, async, errors)?
> See [`README_sdk.md`](./README_sdk.md) — that file is shipped as the PyPI package README.
> This file is for **maintaining/regenerating** the package.

## Layout

| Path | What it is |
| --- | --- |
| `geopera-sdk/` | The generated package (`geopera`). **Generated — do not hand-edit.** |
| `openapi.json` | The committed, scrubbed, customer-safe OpenAPI snapshot the package is built from. |
| `regen.sh` | Regenerate `geopera-sdk/` from the spec (scrub + fence + codegen + metadata). |
| `scrub_spec.py` | Scrubs a raw API dump into the customer-safe public spec, then fences it. |
| `patch_metadata.py` | Re-applies PyPI metadata + README + LICENSE the generator overwrites. |
| `opc-config.yaml` | `openapi-python-client` config (package name override). |
| `README_sdk.md` | The package README (shipped to PyPI). |
| `CHANGELOG.md`, `LICENSE` | Shipped with the package. |
| `test_python_sdk_smoke.py` | No-mock smoke test (import + typed op surface + optional live call). |

## Prerequisites

- Python 3.11+
- `pip install openapi-python-client tomlkit build twine`

Always generate in a throwaway virtualenv — never reuse another project's venv.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install openapi-python-client tomlkit build twine
```

## Regenerate the package

Build from the committed spec snapshot (no network):

```bash
./regen.sh
```

Refresh the spec from a live backend first, then build (the scrub + fence runs either way,
so admin/internal operations and internal prose can never reach the public package):

```bash
GEOPERA_API_URL=https://api.geopera.com ./regen.sh
```

`regen.sh` will:

1. Obtain the raw spec (committed snapshot, or a live `/openapi.json` dump).
2. **Scrub + fence** it into `openapi.json` (drops `*.admin.*` / `*_internal` /
   `diagnostics` ops, prunes leaked model names, strips internal prose, retitles to
   "Geopera Operations"; aborts if anything internal survives).
3. Run `openapi-python-client` into `geopera-sdk/`.
4. Re-apply PyPI metadata + the curated README + LICENSE (`patch_metadata.py`).

## Build + test locally

```bash
# build sdist + wheel
cd geopera-sdk && python -m build && cd ..

# validate distribution metadata
twine check geopera-sdk/dist/*

# install the built wheel and smoke-test it
pip install geopera-sdk/dist/*.whl
python -m pytest test_python_sdk_smoke.py -q

# optional live half (reaches the real API):
GEOPERA_API_URL=https://api.geopera.com GEOPERA_API_TOKEN=gpra_... \
  python -m pytest test_python_sdk_smoke.py -q
```

## Publish

Publishing is automated via `.github/workflows/publish.yml` (PyPI Trusted Publishing, no
stored token). To cut a release:

1. If the API changed, refresh the spec and commit it:
   `GEOPERA_API_URL=https://api.geopera.com ./regen.sh && git commit openapi.json`
2. Bump the version (`spec info.version` flows into the package; verify `geopera-sdk/pyproject.toml`).
3. Tag and push: `git tag v2.0.0 && git push origin v2.0.0`.

The workflow regenerates, builds, runs `twine check`, smoke-tests the wheel, and publishes
to [PyPI](https://pypi.org/project/geopera/).

> One-time PyPI setup: on the project's *Publishing* settings, add a GitHub Actions publisher
> for repo `geo-pera/geopera-python`, workflow `publish.yml`, environment `pypi`.

## License

MIT © Geopera
