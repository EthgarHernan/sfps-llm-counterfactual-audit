# SFPS LLM Counterfactual Audit — Reproducibility Package

Reproducibility package for a counterfactual audit of nominally associated
cultural signals in generative AI assistants for debt collection in Ecuador's
Popular and Solidarity Financial Sector (SFPS, *sector financiero popular y
solidario*).

**Resumen (ES):** paquete independiente de reproducibilidad del estudio UISRAEL
Grupo 6, corrida confirmatoria **V4** (2026-09-06) + validación humana V2
(2026-09-07). Contiene la configuración congelada, los resultados finales
agregados y su documentación de provenance. **No** incluye el manuscrito
institucional, datos privados de evaluadores, credenciales, ledgers crudos de
generación ni código comercial. Es un repositorio *clean-room*: no forma parte
de ningún producto de software y no debe usarse como tal.

---

## 1. Purpose

This repository publishes, with clear provenance, the frozen artifacts of a
scientific audit that asks:

> When a debt-collection assistant built on a generative AI model is exposed to
> a *surname* carrying a documented nominal cultural signal (SN-K or SN-H,
> defined below), does the assistant's behavior change — in severity, empathy,
> or other guardrail dimensions — relative to a counterfactual twin differing
> **only** in that surname?

The surname is treated as an **experimental signal with a documented nominal
cultural association**:

- **SN-K:** nominal signals documented as culturally associated with
  Kichwa/Andean heritage.
- **SN-H:** nominal signals of Hispanic/Iberian tradition used as
  counterfactual controls.

These labels describe experimental nominal signals and do not infer any
individual's ethnicity, language, self-identification, nationality, or
Indigenous affiliation. They are **not** a claim of ethnic identity of any
person: the stimuli are synthetic, the frequency evidence is administrative
(INEC), and the limitations in `docs/14_LIMITATIONS_AND_CLAIMS.md` bound every
interpretation.

## 2. Study design (V4, frozen 2026-09-06)

| Element | Value |
|---|---|
| Protocol | `FINAL_CONFIRMATORY_PROTOCOL_V4_20260906` — `config/confirmatory_experiment_v4_20260906.yaml` (sha256 `87bfbd97…`, see `manifests/V4_RUN_MANIFEST.json`) |
| Synthetic scenarios | 40 debt-collection scenarios (IDs `S001`–`S040`), synthetic; per-scenario context and customer message |
| Nominal surname pairs | 3 documented pairs: P001 `GUAMAN`‖`SALAZAR`, P002 `CHICAIZA`‖`CORDOVA`, P003 `QUISHPE`‖`AREVALO` (INEC frequency provenance in `results/02_FINAL_NUMBERS.csv`, rows PR-01…PR-09; P002 excluded from a sensitivity due to the CORDOVA orthographic caveat) |
| Experimental conditions | `A_BASE` (base prompt) vs. `B_FAIRNESS` (fairness-instructed prompt); plus masked control **C** (`C_MASKED`, proxy replaced by `SOCIO_ID`) |
| Counterfactual logic | First name constant; the contrast varies only the surname (see `results/v4_evidence/REVIEWER_NOTE_20260906_GENERO_ENMASCARAMIENTO.md`) |
| Models | 5: `gemini-3.7-flash`, `gemma-4-31b-it`, `gemma-3n-e4b-it-text` (local) — **PRIMARY**; `gpt-5.4-2026-03-05`, `deepseek-v4-pro` — **SECONDARY_ROBUSTNESS** |
| Valid generations | 2 800 QC-valid responses (`VALID_FINAL_RESPONSE = 2800`; 5 cohorts × 560 tasks; QC gate ≥ 0.95 passed by all 5 cohorts) |
| Judge | DeepEval-style LLM judge `gpt-5.6-terra`, 2 400/2 400 judged responses (A/B pairs only), 0 errors, USD 7.132306 — `results/06_FINAL_JUDGE_RESULTS.csv` |
| Statistics | 155 predeclared rows; **no contrast significant after Holm correction** — `results/04_FINAL_STATISTICAL_RESULTS.csv` |
| LangFair | 55 descriptive rows; VADER sentiment = descriptive only (English lexicon) — `results/05_FINAL_LANGFAIR_RESULTS.csv` |
| Condition C | 0/80 tasks with the proxy exposed **per model** (0/400 across cohorts); 600/600 masked-stability comparisons with `inputs_identical=True` (metric comparisons between technical replicates, not generations) — `docs/CONTROL_C_DENOMINATOR_AUDIT.md` |
| Human validation V2 | 90 paired items, blinded; 12 raters registered, 7 complete (7 × 90 = 630 ratings); Krippendorff ordinal ≈ chance — `results/03_FINAL_HUMAN_RESULTS.csv` |
| Ethics status | Institutional ethics approval: `MISSING`; informed consent: `NOT_DOCUMENTED` — declared, not omitted (rows E-01/E-02 in `results/02_FINAL_NUMBERS.csv`, `docs/14_LIMITATIONS_AND_CLAIMS.md`) |

All excluded V3/recovery cohorts are classified
`ENGINEERING_PRETEST_TECHNICAL_VALIDATION` and are **not** scientific results
here (see `manifests/V4_RUN_MANIFEST.json`).

## 3. Main results at a glance

- **Judge (A_BASE vs B_FAIRNESS):** small descriptive deltas in mean severity /
  empathy per arm; per-response analyses in `results/06_FINAL_JUDGE_RESULTS.csv`.
- **Statistics:** no statistically significant difference survives Holm
  correction in the primary family (only `p_perm < 0.05` pre-correction:
  Gemma-4, A_BASE, severity, 0.017 → `p_holm` 0.205).
- **Condition C:** the masked control shows no measurable exposure of the
  nominal proxy (0/80 per model) and metric-identical replicates for `gemma-4`
  due to temperature-0 determinism — presented as a determinism property, not
  as a fairness finding.
- **Human validation:** human raters do not reliably discriminate A vs B in
  this sample (agreement ≈ chance). This does **not** demonstrate absence of
  bias; it is a measurement limitation.

None of the above is stated as "bias eliminated", "discrimination proven",
"0% bias" or "prompting is fragile". Read the claim rules in
`docs/14_LIMITATIONS_AND_CLAIMS.md` before citing any number.

## 4. Repository structure

```
config/                 Frozen V4 protocol config, smoke config, scheduler runtime, model→run map
results/                02_FINAL_NUMBERS.csv … 08_FINAL_FIGURES.md (final aggregated tables)
results/v4_evidence/    Frozen V4 evidence folder (QC, LangFair pair-level, judge calibration, mapas)
results/human_validation_v2/  Human validation V2 manifest + integrity + truncation audit
data/synthetic/         (see its README: scenario/provenance tables are NOT public)
src/                    Public subset of study scripts (human-validation sample/integrity)
figures/                Frozen V4 figures 1–4 (PNG, hashes recorded in results/08_FINAL_FIGURES.md)
docs/                   Provenance, limitations, reproducibility map, references, audits
manifests/              V4 run manifest, PUBLICATION_MANIFEST.csv, SHA256SUMS.txt
```

A file-by-file map with original source path, SHA-256 and classification lives
in `manifests/PUBLICATION_MANIFEST.csv`.

## 5. What is public — and what is deliberately excluded

**Public:** frozen config; aggregated/derived result tables; per-response judge
scores (scores + rubric justifications, no prompt texts, no raw responses);
human-validation aggregates; figures; documentation; hashes.

**Excluded for privacy/security/copyright** (reasons in
`manifests/PUBLICATION_MANIFEST.csv` and `DATA_AVAILABILITY.md`):

- Evaluator identities, `tokens.csv`, `key.csv` (unmasking map), `calificaciones.csv`;
- Institutional audio/data (Oracle, FitBank, SATJE, WhatsApp); credentials, `.env`;
- Raw generation/judge ledgers (JSONL) — referenced by SHA-256 in `docs/01_SOURCE_OF_TRUTH.md`;
- Full third-party PDFs (citations with DOI provided instead);
- The UISRAEL manuscript DOCX and all institutional manuscript working documents;
- Operational scripts tied to the private deployment infrastructure.

Four files were copied with a single documented redaction of a local machine
path (`DERIVED_PUBLIC` in the manifest): `docs/01_SOURCE_OF_TRUTH.md`,
`docs/10_REFERENCES_VERIFIED_IEEE.md`, `docs/AUDITORIA_BIBLIOGRAFICA_20260907.md`
and `manifests/V4_RUN_MANIFEST.json`.

## 6. How to reproduce

See `REPRODUCIBILITY.md` for the full protocol. In short:

- **`REPRODUCE_ANALYSIS`** (no API calls, no cost): verify hashes against
  `manifests/SHA256SUMS.txt` and recompute every aggregated claim from the
  persisted CSVs with the commands documented there.
- **`RE-RUN_GENERATION`**: requires live API credentials, budget, and
  non-public assets (prompts, scenario tables, surname-pair provenance), which
  remain in the authors' private study repository and are listed with SHA-256s.
  Historical API cost for the judge run: USD 7.13; generation ≈ USD 0.77.

The runtime environment that actually ran V4 is documented in
`REPRODUCIBILITY.md` and pinned in `requirements-reproduction.txt` (the
project's older `requirements.txt` is **not** the executed environment;
discrepancy R-02…R-04).

## 7. Licenses

- **Code** (`src/`, configs, scripts): MIT — see `LICENSE`.
- **Data and authored documentation** (results, figures, docs, manifests,
  README): CC BY 4.0 — see `LICENSE-DATA`.
- **Third-party material:** never relicensed; only cited with DOI. Full
  third-party PDFs are not distributed.

## 8. Citation

If you use this package or its data, cite it with the metadata in
`CITATION.cff` (all three study authors). Example:

> E. H. Changoluisa Lasluisa, M. B. Changoluisa Lasluisa, and P. D. Alemán
> Gualpa, *sfps-llm-counterfactual-audit: reproducibility package of the UISRAEL
> V4 counterfactual audit*, 2026. GitHub. [version 0.1.0]

A DOI will be added to `CITATION.cff` when the package is archived (Zenodo).

## 9. Known limitations (summary)

Full text in `docs/14_LIMITATIONS_AND_CLAIMS.md`:

1. VADER is an English lexicon — all LangFair `sentiment_bias` rows are
   descriptive only.
2. `p > 0.05` ≠ absence of bias; n = 40 scenarios limits power.
3. Human raters ≈ chance agreement in this sample; does not prove absence of bias.
4. Condition C says nothing about fairness (determinism artifact for gemma-4).
5. DeepSeek: 560 valid tasks, 563 attempts (3 technical retries).
6. Robustness cohorts GPT/DeepSeek are secondary (outside the primary Holm family).
7. Surname-frequency evidence (INEC) does not prove ethnicity.
8. Institutional ethics approval is MISSING and evaluator consent NOT_DOCUMENTED
   — the study states this openly instead of omitting it.

## 10. Provenance chain

`manifests/V4_RUN_MANIFEST.json` → `docs/01_SOURCE_OF_TRUTH.md` (ledger and
config hashes) → `docs/15_PUBLICATION_REPRODUCIBILITY_MAP.md` (artifact map) →
`results/08_FINAL_FIGURES.md` (figure hashes) → `manifests/PUBLICATION_MANIFEST.csv`
(this package's own manifest, with `public_sha256` computed on 2026-09-07).

## Security

This repository contains **no** credentials, tokens, or private data. See
`SECURITY.md` for the reporting policy and `PUBLIC_REPO_SECURITY_AUDIT.md` for
the audit that preceded the first commit.
