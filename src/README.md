# src/ — public subset of the study scripts

The V4 run tooling (generation, QC, judge, LangFair, statistics, figures)
lives in the authors' private study repository and is **not** part of this
public package. Its SHA-256s are recorded in
`manifests/V4_RUN_MANIFEST.json` (`tooling_sha256`) and
`docs/15_PUBLICATION_REPRODUCIBILITY_MAP.md`, so the exact scripts are
identifiable and verifiable.

What is shipped here (human-validation V2, public subset):

| File | Purpose |
|---|---|
| `build_sample_v2.py` | Builds the blinded 90-item paired sample (seed 42, randomized left/right sides) and the private unmasking key (the key itself is **not** public) |
| `integrity_check_v2.py` | Integrity gate: verifies SHA-256(source) == SHA-256(delivered) for all 180 texts and audits truncation hazards; reproduced result: `results/human_validation_v2/HUMAN_VALIDATION_V2_INTEGRITY.csv` |

See `REPRODUCIBILITY.md` for what can be re-executed offline and what
requires non-public assets.
