#!/usr/bin/env python3
"""Scrub a raw Geopera OpenAPI dump into a customer-safe PUBLIC spec, then fence it.

    python3 scrub_spec.py <raw-openapi.json> <out-spec.json>

Runs on EVERY SDK regen (regen.sh), so the public Python/TS SDKs can never expose the
internal surface even if someone refreshes from a live backend that has admin ops:
  - drops every admin/internal operation (*.admin.*, *_internal, diagnostics, …)
  - prunes component schemas to the reference-closure of the kept customer ops, so admin
    request/response MODEL names don't leak either
  - strips internal prose from summaries/descriptions (money-path / CU / legacy / provenance
    / service-role / password_hash / "the kernel …") and internal x-* extensions
  - retitles to "Geopera Operations"
  - FENCE: exits non-zero if any admin/internal op or internal token survives, so a leaky
    spec can never be written (fails the regen / CI).
"""
from __future__ import annotations

import json
import re
import sys

# Operations a public SDK must never expose (callable internal/admin surface).
DENY_OP = re.compile(r'(\.admin\.|(^|\.)admin[._]|_internal\b|(^|\.)diagnostics(\.|$))', re.I)
# Internal mechanics that must never appear in a customer-facing description.
DENY_PHRASES = [
    'money path', 'reserves credit', 'reserves cu', 'legacy /v2', 'legacy post',
    'legacy wire', 'legacy route', 'legacy ', 'raw_response', 'invoke()', 'model_dump',
    'backgroundtask', 'service-role', 'service role', 'password_hash', 'extra=allow',
    'provenance', 'the kernel', 'kernel ', 'idempotency-key parity', 'strangl',
]
DROP_EXT = ('x-side-effect', 'x-kernel-version', 'x-raw-response', 'x-public', 'x-produces')


def _clean(text):
    """Keep only the first (customer-facing) sentence; drop it entirely if even that leaks
    internals. Returns None to mean 'remove the field'."""
    if not text:
        return None
    first = re.split(r'(?<=[.!?])\s', str(text).strip(), maxsplit=1)[0].strip()
    low = first.lower()
    if not first or any(p in low for p in DENY_PHRASES):
        return None
    return first


def _scrub_node(d):
    if not isinstance(d, dict):
        return
    for key in ('summary', 'description'):
        if key in d:
            c = _clean(d.get(key))
            if c:
                d[key] = c
            else:
                d.pop(key, None)


def _refs_in(node, acc):
    if isinstance(node, dict):
        r = node.get('$ref')
        if isinstance(r, str) and r.startswith('#/components/schemas/'):
            acc.add(r.split('/')[-1])
        for v in node.values():
            _refs_in(v, acc)
    elif isinstance(node, list):
        for v in node:
            _refs_in(v, acc)


def scrub(spec: dict) -> tuple[dict, list[str]]:
    """Return (clean_spec, dropped_op_ids). Raises SystemExit(1) via fence on leakage."""
    paths, dropped = {}, []
    for p, v in (spec.get('paths') or {}).items():
        if not (p.startswith('/v1/op/') and '{operation_id}' not in p):
            continue
        op_id = p[len('/v1/op/'):]
        if DENY_OP.search(op_id):
            dropped.append(op_id)
            continue
        for _method, body in list(v.items()):
            if not isinstance(body, dict):
                continue
            body['tags'] = ['operations']
            for ext in DROP_EXT:
                body.pop(ext, None)
            _scrub_node(body)
        paths[p] = v

    schemas = (spec.get('components') or {}).get('schemas', {})
    used: set = set()
    _refs_in(paths, used)
    frontier = list(used)
    while frontier:
        sch = schemas.get(frontier.pop())
        if isinstance(sch, dict):
            nxt: set = set()
            _refs_in(sch, nxt)
            for n in nxt - used:
                used.add(n)
                frontier.append(n)
    kept = {k: v for k, v in schemas.items() if k in used}
    for sch in kept.values():
        _scrub_node(sch)
        for prop in (sch.get('properties') or {}).values():
            _scrub_node(prop)

    clean_spec = {
        'openapi': spec.get('openapi', '3.1.0'),
        'info': {
            'title': 'Geopera Operations',
            'description': 'Official API for the Geopera geospatial data platform.',
            'version': (spec.get('info') or {}).get('version', '1.0.0'),
        },
        'paths': paths,
        'tags': [{'name': 'operations', 'description': 'Geopera operations'}],
        'components': {**(spec.get('components') or {}), 'schemas': kept},
    }

    # FENCE — internals must never reach the public SDK.
    problems = []
    for op_id in (p[len('/v1/op/'):] for p in paths):
        if DENY_OP.search(op_id):
            problems.append(f'admin/internal op survived: {op_id}')
    blob = json.dumps(clean_spec).lower()
    for term in ('"x-kernel', '"x-side-effect', 'password_hash', 'service-role', 'model_dump', 'reserves cu'):
        if term in blob:
            problems.append(f'internal token survived: {term}')
    if re.search(r'kernel', json.dumps(clean_spec.get('info')) + ' '.join(paths.keys()), re.I):
        problems.append("'kernel' in title/paths")
    if problems:
        sys.stderr.write('SCRUB FENCE FAILED — refusing to write a leaky public spec:\n  - '
                         + '\n  - '.join(problems) + '\n')
        raise SystemExit(1)
    return clean_spec, dropped


def main() -> None:
    raw, out = sys.argv[1], sys.argv[2]
    spec = json.load(open(raw))
    clean_spec, dropped = scrub(spec)
    json.dump(clean_spec, open(out, 'w'), indent=1)
    more = '…' if len(dropped) > 10 else ''
    print(f"scrubbed -> {out}: {len(clean_spec['paths'])} customer ops, "
          f"{len(clean_spec['components']['schemas'])} schemas; "
          f"dropped {len(dropped)} admin/internal: {', '.join(sorted(dropped)[:10])}{more}")


if __name__ == '__main__':
    main()
