# Reproducibility

This file states precisely what can and cannot be reproduced from this public
package, how, and at what cost. It distinguishes

- **`REPRODUCE_ANALYSIS`** — recompute every aggregated claim from the
  persisted outputs included here (no API calls, no spending); and
- **`RE-RUN_GENERATION`** — regenerate the study from scratch (requires API
  credentials, budget, and assets that are **not** public).

> Status note (2026-09-07): the generation/judge APIs were **not** re-executed
> to build this package. Nothing in this repository was recomputed except SHA-256
> hashes of the copied files.

## 1. Environment that actually ran V4 (authoritative)

Source: V4 run manifests and `docs/15_PUBLICATION_REPRODUCIBILITY_MAP.md`.
The runtime **actually executed** was:

| Component | Version |
|---|---|
| Python | 3.10.0 |
| OS | Windows 10.0.26100 |
| google-genai | 1.74.0 |
| openai | 2.16.0 |
| pyyaml | 6.0.2 |
| langfair | 0.8.0 |
| deepeval | 4.2.1 |

**Difference with the historical `requirements.txt` (documented, R-02…R-04 in
`docs/14_LIMITATIONS_AND_CLAIMS.md`):** the historical file pinned
`google-genai==2.22.0`, `openai==3.8.0`, `pyyaml==6.0.3`, which was **not** the
executed environment. The executed environment is pinned in
`requirements-reproduction.txt` at the repository root. The historical
`requirements.txt` is not distributed here.

Human validation V2 analysis ran outside the API runtime; its manifest
(`results/human_validation_v2/HUMAN_VALIDATION_V2_MANIFEST.json`) records
seed `42`, the 90-item blinded sample and its integrity checks (180/180 texts,
`HUMAN_VALIDATION_V2_INTEGRITY.csv`).

## 2. Frozen scientific configuration

| File in this repo | SHA-256 (also in `manifests/SHA256SUMS.txt`) |
|---|---|
| `config/confirmatory_experiment_v4_20260906.yaml` | `87bfbd97871d30c059a75ff3683ecc1d959a8d68aa398b5ea5f8ee21657349fc` |
| `config/smoke_deepeval_v4_20260906.yaml` | see manifest |
| `config/final_model_run_map_v4_20260906.json` | see manifest |
| `config/v4_scheduler_runtime_20260906.json` | `7fc76c922501a5bb7a26f6d0d0d8fb1aa3dd73c6b74fb23da244fa3183ad3d0c` (scheduling only, not scientific config) |

Key frozen parameters (from the config and the numbers map
`results/v4_evidence/V4_ARTICLE_NUMBERS_MAP.csv`): temperature `0.0`, up to 2
retries, `max_output_tokens` 8192 (2048 for `gemma-3n-e4b-it-text`), 40
scenarios × 2 arms + 80 masked-control tasks per model, judge
`gpt-5.6-terra` (reasoning low, max 1024 tokens, structured, `store=false`).
`reasoning_content` was never persisted as content — only its presence and
length (protocol policy; see config `metadata_deepseek_extra`).

## 3. Run IDs and ledger hashes (raw ledgers NOT public)

| run_id | model | role | ledger sha256 (raw ledger, not in this package) |
|---|---|---|---|
| `FINAL_V4_GEMINI37` | gemini-3.7-flash | PRIMARY | `13a1295aa3410a42fcd62e25f9a2461c2ce8fe8119d6ca18a226db3522951ae2` |
| `FINAL_V4_GEMMA4` | gemma-4-31b-it | PRIMARY | `b0f4766d72faa9ee9c638c3b9b48179ae192abc941c4a8cbd2401524426c659c` |
| `FINAL_V4_GEMMA3N_LOCAL` | gemma-3n-e4b-it-text | PRIMARY | `55dd48ebccec2e0dd4dbd165b8db0c636338a1c36cb9ec3c3af5e6aa47abd0ae` |
| `ROBUSTNESS_V4_GPT54` | gpt-5.4-2026-03-05 | SECONDARY_ROBUSTNESS | `2ebfed8d24473d5a76f200a0e290fb9d9233d9f6fca43f4ab6e8eff3f2702920` |
| `ROBUSTNESS_V4_DEEPSEEK` | deepseek-v4-pro | SECONDARY_ROBUSTNESS | `962c6dec037f4479a1eff6274a2fecee98f0913cff2073dc252a545cb21a05b4` |

Execution order of the frozen V4 run (per `manifests/V4_RUN_MANIFEST.json`):
canary (5/5 passed) → preflight → generation of the 5 cohorts →
QC gate (`VALID_FINAL_RESPONSE=2800`, threshold ≥ 0.95, all passed) →
DeepEval judge 2400/2400 → predeclared statistics (155 rows) → LangFair
descriptive (55 rows) → human validation V2 → figures 1–4.

## 4. REPRODUCE_ANALYSIS (no API calls, no cost)

Everything below works offline with the files in this package, Python 3.10
(any recent Python with pandas works for the row checks) or PowerShell.

**4.1 Verify package integrity**

```powershell
Get-FileHash -Algorithm SHA256 <file>   # compare against manifests/SHA256SUMS.txt
# bulk check (PowerShell):
Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notmatch '\\.git\\' } |
  Get-FileHash -Algorithm SHA256 | Sort-Object Path
```

**4.2 Recompute the aggregated numbers from the persisted CSVs**

The claim table `results/02_FINAL_NUMBERS.csv` records, per claim id, the
authoritative `source_file` and `source_sha256`. To recompute a claim from its
source CSV:

```bash
# row counts that anchor the headline numbers:
python -c "
import pandas as pd
j = pd.read_csv('results/06_FINAL_JUDGE_RESULTS.csv');      print('judge rows:', len(j), 'statuses:', j.judge_status.value_counts().to_dict())
s = pd.read_csv('results/04_FINAL_STATISTICAL_RESULTS.csv'); print('statistical rows:', len(s), 'status:', s.status.value_counts().to_dict())
l = pd.read_csv('results/05_FINAL_LANGFAIR_RESULTS.csv');    print('langfair rows:', len(l))
h = pd.read_csv('results/03_FINAL_HUMAN_RESULTS.csv');       print('human rows:', len(h))
q = pd.read_csv('results/v4_evidence/V4_QC_SUMMARY.csv');    print('qc rows:', len(q), 'eligible:', q.eligible.sum())
qc = pd.read_csv('results/v4_evidence/langfair_masked_stability.csv'); print('masked-stability rows:', len(qc), 'inputs_identical:', (qc.inputs_identical==True).sum(), 'exposed:', (qc.attribute_exposed==True).sum())
"
# expected: judge 2400 (all OK), statistical 155 (all COMPUTED), langfair 55,
# human 177, QC eligible 2800, masked stability 600/600 identical, 0 exposed.
```

Expected outcome anchors (claim ids in `results/02_FINAL_NUMBERS.csv`):
5 cohorts COMPLETED (P-01…), 2 800 valid responses (QC),
judge 2400/2400 with 0 errors (J-01…), 155 statistical rows with no
significant contrast after Holm (S-01…), LangFair 55 rows with
`DESCRIPTIVE_ONLY_VADER_SPANISH_LIMITATION` on sentiment (L-01…), masked
control 0/80 exposed per model and 600/600 identical inputs (G-07…G-10),
human validation 630 complete ratings, 7 complete raters (H-02…).

**4.3 Sanity checks available out of the box**

- Judge score aggregates per condition/arm: recompute mean severity/empathy
  deltas from `results/06_FINAL_JUDGE_RESULTS.csv` and compare with the
  corresponding J-rows of `results/02_FINAL_NUMBERS.csv` (exact CI method:
  see `results/07_FINAL_TABLES.md`).
- Masked-control stability: from `results/v4_evidence/langfair_masked_stability.csv`
  filter `condition == C_MASKED` and confirm 0 exposed / 600 identical.
- QC gate: `results/v4_evidence/V4_QC_TAXONOMY.json` reports
  `valid_pair_rate: 1.0` and `passes_threshold: true` for all 5 models.

The human-validation integrity gate can be re-executed on the delivered
artifacts with the shipped script:

```bash
python src/human_validation/integrity_check_v2.py \
  --public-items <public_items.json> --delivered-json <delivered.json> \
  --output out.csv
# (public_items.json and the delivered JSON are NOT public; the precomputed
# 180/180 result is results/human_validation_v2/HUMAN_VALIDATION_V2_INTEGRITY.csv)
```

**4.4 What cannot be recomputed from this package alone**

The judge CSV (`results/06_FINAL_JUDGE_RESULTS.csv`) is a **verified derived
materialization** of the append-only judge ledger (per study decision OI-15:
"no se recalcula"). The raw ledgers, scenario tables, prompt files and the
blinded human-validation texts are not public; their hashes are recorded so
that any future owner of those files can verify them (section 3 and
`docs/01_SOURCE_OF_TRUTH.md`).

## 5. RE-RUN_GENERATION (requires APIs and non-public assets)

Full regeneration requires:

1. **Non-public assets** (kept in the authors' private study repository; not
   distributed here): the scenario table `scenarios_v3.csv` (sha
   `020f6b569d061b75d956325c2caec9eabf69c7ecc8e04f39a5a66c4b0ec9804b`),
   the surname-pair provenance `surname_pair_provenance_v3.csv` (sha
   `fe4ecd6eb419526c8469aedddd65c75a4a3ec446a408483962bba2deb1b36e5a`), the
   three prompt files (`collection_agent_base_v2.txt`,
   `collection_agent_fairness_v2.txt`, `deepeval_judge_v3.txt`) and the V4
   runner scripts (hashes in `manifests/V4_RUN_MANIFEST.json`, field
   `tooling_sha256`).
2. **Credentials** for Google, OpenAI (judge + gpt-5.4), DeepSeek and a local
   LM Studio host (`gemma-3n-e4b-it-text`). The frozen config reads keys from
   environment variables (`GOOGLE_API_KEY`, `OPENAI_API_KEY`,
   `DEEPSEEK_API_KEY`, …); no key is stored in any file here.
3. **Budget.** Historical documented API cost: judge USD 7.132306 (2 400
   responses, 1 290 377 / 379 296 / 104 576 input/output/reasoning tokens);
   gpt-5.4 generation ≈ USD 0.77. Model versions and prices will differ if
   re-run later — that is expected and must be reported.

If a full re-run is ever authorized, the frozen protocol and config in this
package, executed in the exact environment of section 1, are the reference
for reproducibility (clean-room V4 discipline: V3/recoveries are
`ENGINEERING_PRETEST_TECHNICAL_VALIDATION`, never scientific input).

## 6. Hash and provenance summary

- `manifests/SHA256SUMS.txt` — SHA-256 of every public file in this package
  (computed 2026-09-07).
- `manifests/PUBLICATION_MANIFEST.csv` — path, description, original source,
  source sha256, public sha256, classification (PUBLIC / DERIVED_PUBLIC /
  EXCLUDED_*) and reason, per file.
- `docs/01_SOURCE_OF_TRUTH.md` — authoritative sources and cohort hashes.
- `docs/15_PUBLICATION_REPRODUCIBILITY_MAP.md` — artifact → hash map used by
  the publication.
- `results/08_FINAL_FIGURES.md` — figure hashes (verified equal to the PNGs
  shipped in `figures/`).
