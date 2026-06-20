#!/usr/bin/env python3
"""Post-regen polish for the generated Geopera Python SDK.

`openapi-python-client generate --overwrite` rewrites the whole package every run,
stripping publish metadata and replacing the README. This restores the "top tier"
bits so the published artifact is professional and reproducible:

  * full PyPI metadata on [tool.poetry] (authors, license, urls, keywords, classifiers)
  * the curated README (README_sdk.md) instead of the generic generated one
  * the LICENSE shipped inside the wheel/sdist

Idempotent. Run by regen.sh after generation (and by the publish CI).
"""
from __future__ import annotations

import shutil
from pathlib import Path

import tomlkit

HERE = Path(__file__).resolve().parent
PKG = HERE / "geopera-sdk"
PYPROJECT = PKG / "pyproject.toml"

REPO_URL = "https://github.com/geo-pera/geopera-python"
DOCS_URL = "https://docs.geopera.com"

doc = tomlkit.parse(PYPROJECT.read_text())
poetry = doc["tool"]["poetry"]
poetry["description"] = "Official Python client for the Geopera geospatial data platform"
poetry["authors"] = ["Geopera <support@geopera.com>"]
poetry["license"] = "MIT"
poetry["homepage"] = DOCS_URL
poetry["repository"] = REPO_URL
poetry["documentation"] = f"{DOCS_URL}/api-reference"
poetry["keywords"] = [
    "geopera", "satellite", "geospatial", "earth-observation",
    "stac", "remote-sensing", "api-client",
]
poetry["classifiers"] = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Scientific/Engineering :: GIS",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Typing :: Typed",
]
# urls block for the PyPI sidebar
poetry["urls"] = {
    "Documentation": f"{DOCS_URL}/api-reference",
    "Source": REPO_URL,
    "Changelog": f"{REPO_URL}/blob/main/CHANGELOG.md",
}
PYPROJECT.write_text(tomlkit.dumps(doc))

# curated README + LICENSE shipped inside the package
shutil.copyfile(HERE / "README_sdk.md", PKG / "README.md")
shutil.copyfile(HERE / "LICENSE", PKG / "LICENSE")

print(f"patched {PYPROJECT.name}: metadata + README + LICENSE")
