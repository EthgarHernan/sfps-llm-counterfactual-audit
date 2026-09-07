#!/usr/bin/env python3
"""Build the blinded V2 human-validation sample from the V4 principal cohorts.

Sample: 90 pairs = 3 principal models x 2 conditions (A_BASE, B_FAIRNESS) x 15,
with 5 items per nominal pair inside each cell, drawn ONLY from QC-eligible
V4 pairs of FINAL_V4_GEMINI37 / FINAL_V4_GEMMA4 / FINAL_V4_GEMMA3N_LOCAL.
Selection is random with frozen seed 42; never selected by result, severity,
empathy or narrative interest. The V1 pilot sample is never reused.

Blinding: surname replaced by [PERSONA]; arm, model, condition and run_id are
hidden; left/right position is randomized per item with seed 42. The private
unmasking key stays out of the public package.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
from collections import defaultdict
from pathlib import Path

PRINCIPAL_RUN_IDS = {"FINAL_V4_GEMINI37", "FINAL_V4_GEMMA4", "FINAL_V4_GEMMA3N_LOCAL"}


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def mask(text: str, names: set[str]) -> str:
    result = text
    for name in sorted(names, key=len, reverse=True):
        result = re.sub(rf"\b{re.escape(name)}\b", "[PERSONA]", result, flags=re.IGNORECASE)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--qc-summary", type=Path, required=True)
    parser.add_argument("--eligible-responses", type=Path, required=True)
    parser.add_argument("--scenarios", type=Path, required=True)
    parser.add_argument("--surname-pairs", type=Path, required=True)
    parser.add_argument("--public-output", type=Path, required=True)
    parser.add_argument("--private-key-output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    for output in (args.public_output, args.private_key_output):
        if output.exists():
            raise SystemExit(f"Refusing to overwrite {output}")

    records = read_jsonl(args.eligible_responses)
    by_key = {str(row["logical_key"]): row for row in records}
    with args.qc_summary.open(encoding="utf-8", newline="") as handle:
        eligible = [
            row for row in csv.DictReader(handle)
            if row["eligible"] == "true" and row["condition"] in {"A_BASE", "B_FAIRNESS"}
            and row["run_id"] in PRINCIPAL_RUN_IDS
        ]
    with args.scenarios.open(encoding="utf-8", newline="") as handle:
        scenarios = {row["scenario_id"]: row for row in csv.DictReader(handle)}
    with args.surname_pairs.open(encoding="utf-8", newline="") as handle:
        surname_rows = list(csv.DictReader(handle))
    names = {"Ana"}
    for row in surname_rows:
        names.update((row.get("surname_a") or row.get("arm_a_surname"), row.get("surname_b") or row.get("arm_b_surname")))

    pair_records: dict[tuple[str, str, str, str], dict[str, dict]] = defaultdict(dict)
    for row in records:
        if row["qc_class"] == "VALID_FINAL_RESPONSE" and row["condition"] in {"A_BASE", "B_FAIRNESS"}:
            if row["run_id"] not in PRINCIPAL_RUN_IDS:
                continue
            key = (row["model"], row["condition"], row["scenario_id"], row["surname_pair"])
            pair_records[key][row["counterfactual_arm"]] = by_key[row["logical_key"]]

    rng = random.Random(args.seed)
    cells: dict[tuple[str, str, str], list[tuple]] = defaultdict(list)
    eligible_keys = {
        (row["model"], row["condition"], row["scenario_id"], row["surname_pair_or_control"])
        for row in eligible
    }
    for key, arms in pair_records.items():
        if key in eligible_keys and set(arms) == {"A", "B"}:
            cells[(key[0], key[1], key[3])].append(key)

    selected: list[tuple] = []
    for cell, candidates in sorted(cells.items()):
        if len(candidates) < 5:
            raise SystemExit(f"Cell {cell} has only {len(candidates)} eligible pairs; needs 5")
        selected.extend(rng.sample(sorted(candidates), 5))
    model_condition_cells = {(key[0], key[1]) for key in selected}
    if len(model_condition_cells) != 6 or len(selected) != 90:
        raise SystemExit(f"Expected 6 model-condition cells and 90 items; got {len(model_condition_cells)} and {len(selected)}")

    public_items = []
    private_rows = []
    for index, key in enumerate(rng.sample(selected, len(selected)), 1):
        arms = pair_records[key]
        order = ["A", "B"] if rng.random() < 0.5 else ["B", "A"]
        first, second = arms[order[0]], arms[order[1]]
        item_id = f"HV2-{index:03d}"
        scenario = scenarios[key[2]]
        public_items.append({
            "item_id": item_id,
            "minimal_context": scenario.get("financial_context") or scenario.get("context"),
            "customer_message": mask(first["raw_input"], names),
            "response_1": mask(first["response"], names),
            "response_2": mask(second["response"], names),
        })
        private_rows.append({
            "item_id": item_id, "model": key[0], "condition": key[1],
            "scenario_id": key[2], "surname_pair": key[3],
            "response_1_arm": order[0], "response_2_arm": order[1],
            "response_1_logical_key": first["logical_key"], "response_2_logical_key": second["logical_key"],
            "response_1_sha256": None, "response_2_sha256": None,
        })

    args.public_output.parent.mkdir(parents=True, exist_ok=True)
    args.private_key_output.parent.mkdir(parents=True, exist_ok=True)
    args.public_output.write_text(json.dumps(public_items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with args.private_key_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(private_rows[0]))
        writer.writeheader()
        writer.writerows(private_rows)
    print(json.dumps({"items": len(public_items), "cells": len(cells), "seed": args.seed}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
