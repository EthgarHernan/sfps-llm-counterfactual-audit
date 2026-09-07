#!/usr/bin/env python3
"""Integrity gate for the V2 human-validation deployment.

For every public item and for the JSON actually handed to the frontend/backend,
verifies that SHA256(source_text) == SHA256(delivered_text) for BOTH responses
of all 90 items (180 texts). Also flags truncation hazards: substr()/slice,
maxlength attributes, short DB columns, CSS text-overflow/ellipsis, JSON/PHP
truncation and non-UTF-8 bytes. The page must NOT be enabled until every
delivered text matches (match=true).

Outputs: HUMAN_VALIDATION_V2_INTEGRITY.csv
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

TRUNCATION_PATTERNS = [
    re.compile(r"substr\s*\(", re.IGNORECASE),
    re.compile(r"\[:\d+\]"),
    re.compile(r"maxlength\s*=", re.IGNORECASE),
    re.compile(r"text-overflow\s*:\s*ellipsis", re.IGNORECASE),
    re.compile(r"overflow\s*:\s*hidden", re.IGNORECASE),
    re.compile(r"substring\s*\(", re.IGNORECASE),
]
# Generic `.slice(` is only a hazard when applied to response content:
RESPONSE_SLICE_PATTERN = re.compile(r"(response|resp\d|text|content)[^\n]{0,40}\.slice\s*\(", re.IGNORECASE)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-items", type=Path, required=True)
    parser.add_argument("--delivered-json", type=Path, required=True, help="the JSON actually handed to the frontend/backend")
    parser.add_argument("--deployables", nargs="*", default=[], help="optional files (php/js/html) scanned for truncation hazards")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source_items = {item["item_id"]: item for item in json.loads(args.public_items.read_text(encoding="utf-8"))}
    delivered_items = {item["item_id"]: item for item in json.loads(args.delivered_json.read_text(encoding="utf-8"))}

    if set(source_items) != set(delivered_items):
        raise SystemExit(f"Item id mismatch: source={sorted(source_items)[:5]} delivered={sorted(delivered_items)[:5]}")

    rows = []
    hazards = []
    for item_id in sorted(source_items):
        source = source_items[item_id]
        delivered = delivered_items[item_id]
        for side in ("response_1", "response_2"):
            source_text = source[side]
            delivered_text = delivered.get(side, "")
            source_sha = sha256_text(source_text)
            delivered_sha = sha256_text(delivered_text)
            rows.append({
                "human_item_id": item_id,
                f"source_logical_id_{side}": None,  # filled by caller-side mapping when available
                f"source_sha_{side}": source_sha,
                f"web_sha_{side}": delivered_sha,
                "match": str(source_sha == delivered_sha).lower(),
            })
    for path in args.deployables:
        content = Path(path).read_text(encoding="utf-8", errors="replace")
        for pattern in TRUNCATION_PATTERNS:
            for match in pattern.finditer(content):
                line = content[:match.start()].count("\n") + 1
                hazards.append(f"{path}:{line}: {match.group(0)}")
        for match in RESPONSE_SLICE_PATTERN.finditer(content):
            line = content[:match.start()].count("\n") + 1
            hazards.append(f"{path}:{line}: {match.group(0)}")
        try:
            Path(path).read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            hazards.append(f"{path}: NOT_VALID_UTF8")

    # column-width audit for the delivered JSON itself: recompute UTF-8 length per field
    for item in delivered_items.values():
        for side in ("response_1", "response_2"):
            text = item.get(side, "")
            if len(text.encode("utf-8")) > 65535:
                hazards.append(f"{item['item_id']}:{side}: utf8_bytes={len(text.encode('utf-8'))} > 65535 (TEXT column hazard)")

    rows_wide = []
    for row in rows:
        for side in ("response_1", "response_2"):
            if row.get(f"source_sha_{side}"):
                rows_wide.append({
                    "human_item_id": row["human_item_id"],
                    "side": side,
                    "source_sha": row[f"source_sha_{side}"],
                    "web_sha": row[f"web_sha_{side}"],
                    "match": row["match"],
                })
    all_match = all(row["match"] == "true" for row in rows_wide)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["human_item_id", "side", "source_sha", "web_sha", "match"])
        writer.writeheader()
        writer.writerows(rows_wide)
    (args.output.parent / "HUMAN_VALIDATION_V2_TRUNCATION_AUDIT.txt").write_text(
        "\n".join(hazards) + "\n" + ("NO_HAZARDS" if not hazards else ""), encoding="utf-8"
    )
    print(json.dumps({
        "texts_checked": len(rows_wide),
        "all_match": all_match,
        "truncation_hazards": len(hazards),
    }, ensure_ascii=False, indent=2))
    return 0 if (all_match and not hazards) else 2


if __name__ == "__main__":
    raise SystemExit(main())
