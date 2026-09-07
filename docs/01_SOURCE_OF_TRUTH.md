# 01 — FUENTE DE VERDAD (V4)

Regla: las carpetas de resultados V4 están CONGELADAS. Nada de este handoff las
modifica. Todo archivo copiado aquí es **verbatim**; su hash coincide con el
registrado en el pack de evidencia y en `V4_RUN_MANIFEST.json`.

## Fuentes autoritativas (originales, nunca modificar)

| Fuente | Ruta | Qué contiene |
|---|---|---|
| Carpeta final V4 | `publication-repository/results/FINAL_CONFIRMATORY_V4_20260906/` | QC, LangFair, estadística, juez, figuras, manifest, mapa de números (19 archivos + `figures/`) |
| Pack de evidencia | `publication-repository/results/MANUSCRIPT_EVIDENCE_PACK_20260907/` | MASTER_NUMBERS (355 filas), acuerdo humano, tablas/figuras/referencias, issues |
| Ledgers de generación | `publication-repository/runs/<run_id>/generation_attempts.jsonl` | intentos append-only por cohorte (NO copiados aquí; ver hashes abajo) |
| Ledger del juez | `publication-repository/results/FINAL_CONFIRMATORY_V4_20260906/deepeval_judge_v4_ledger.jsonl` | 2400/2400 juzgadas (fuente autoritativa del juez) |
| Config V4 | `publication-repository/config/confirmatory_experiment_v4_20260906.yaml` | protocolo congelado (sha `87bfbd97…`) |
| Validación humana | `publication-repository/human_validation_v2/` | manifiesto, integridad 180/180, truncation audit (solo públicos) |
| Auditoría bibliográfica | `<corpus local del autor — fuera del repositorio público>` | ARTICLE_REFERENCE_CATALOG.csv (87 filas; R84–R87 ahora con PDF físico en el corpus), CITATION_CLAIM_MATRIX.csv (34 filas), informe, PDFs CORE (copia en `evidence/AUDITORIA_BIBLIOGRAFICA_20260907/`) |
| Manuscrito | `IAA-GRUPO6-ART.docx` (raíz del repo) | copiado a `SOURCE_DOCUMENT/` como PRE_FINAL |

## Sello clean-room V4

`V4_RUN_MANIFEST.json` (sha del propio manifest no fijado; contenido verificado):
- `protocol_id`: `FINAL_CONFIRMATORY_PROTOCOL_V4_20260906`.
- V3 y recuperaciones = `ENGINEERING_PRETEST_TECHNICAL_VALIDATION`, excluidas
  del análisis, preservadas append-only, nunca regeneradas como V4.
- run_ids excluidos: `CONFIRMATORY_TEXT_V3`, `CONFIRMATORY_GEMINI37_RECOVERY_V1`,
  `CONFIRMATORY_GEMMA4_RECOVERY_V1`, `CONFIRMATORY_GEMINI37_FINAL_V2`,
  `CONFIRMATORY_GEMMA4_FINAL_V2`, `CONFIRMATORY_GEMMA4_FINAL_V3`.
- Config sha256 `87bfbd97871d30c059a75ff3683ecc1d959a8d68aa398b5ea5f8ee21657349fc`;
  canary 5/5 passed; QC `VALID_FINAL_RESPONSE=2800`; gate mínimo 0,95 superado
  por las 5 cohortes.

## Hashes de cohortes (ledgers y manifests)

| run_id | ledger_sha256 | manifest_sha256 |
|---|---|---|
| FINAL_V4_GEMINI37 | `13a1295aa3410a42fcd62e25f9a2461c2ce8fe8119d6ca18a226db3522951ae2` | `a60b3e9356b67a31b7ba908ebcf56786e3ef21a65f1cfbd124daf04d0d4142ac` |
| FINAL_V4_GEMMA4 | `b0f4766d72faa9ee9c638c3b9b48179ae192abc941c4a8cbd2401524426c659c` | `d3f6e8721c361dbb1f95ea8803d14b7f14d685594726bb5add6dd2f0cd34faa7` |
| FINAL_V4_GEMMA3N_LOCAL | `55dd48ebccec2e0dd4dbd165b8db0c636338a1c36cb9ec3c3af5e6aa47abd0ae` | `454d76395ce1191046db0f3d651fbd7c304bfe22f69c5aa6295f24041696518e` |
| ROBUSTNESS_V4_GPT54 | `2ebfed8d24473d5a76f200a0e290fb9d9233d9f6fca43f4ab6e8eff3f2702920` | `390d6eda1775c043c26d256e5e4759b38249df60203a81b3e487f8f0025bc5d8` |
| ROBUSTNESS_V4_DEEPSEEK | `962c6dec037f4479a1eff6274a2fecee98f0913cff2073dc252a545cb21a05b4` | `2aa64164982662e117754b427c7f0a0988563c3ba454a914205d4c547e2b43be` |

## Hashes de los CSVs de este handoff (verificados al copiar, 2026-09-07)

| Archivo del handoff | sha256 |
|---|---|
| 02_FINAL_NUMBERS.csv | `fcc1ea277a50b6f824c8017651ffce12c875373f8ae808f75e02aa0dda821ace` |
| 03_FINAL_HUMAN_RESULTS.csv | `8b3afd931b94939120e923007e6f902db2bc7307ba84ff6fe9076550c6220a70` |
| 04_FINAL_STATISTICAL_RESULTS.csv | `f1a182ca2b5c3428919bdae693cfa0a03d5449f8d072c411eef716758a5abc82` |
| 05_FINAL_LANGFAIR_RESULTS.csv | `f82c8aefb78d39da21d660ec115ac855ed6c85f0321c71d337cb89f029fc922a` |
| 06_FINAL_JUDGE_RESULTS.csv | `c03f68274c437fe91b31a86584e436467a4efa19c9009ef09c0864532c5efbd5` |
| 06_FINAL_JUDGE_COST_REPORT.csv | `e3f7ee05d3510a899a9e64f51c73e881c232de194912c6dd471be9575ac4a6d1` |
| V4_QC_TAXONOMY.json | `b4501da0f004fd20a309d904a1b5fd2867b3508b0bdfda99614b3d463c74789` |

Fuente de los hashes: `evidence/MANUSCRIPT_EVIDENCE_PACK_20260907/MASTER_NUMBERS.csv`
(columna `source_sha256`) y `MASTER_ARTIFACT_MANIFEST.csv`; verificados por
`Get-FileHash` al copiar.

## Lo que NO está en este paquete (por privacidad o tamaño)

- `tokens.csv`, `key.csv`, `calificaciones.csv` humanos → PRIVADOS
  (`research/fairness-audit/human_validation_v2/server-private-v2/` y descarga
  del autor). Nunca copiar al paquete público.
- Ledgers jsonl grandes (`deepeval_judge_v4_ledger.jsonl`,
  `V4_ELIGIBLE_RESPONSES.jsonl`, `generation_attempts.jsonl` de cada run) →
  referenciados por ruta; no duplicados.
- Cohortes V3/recovery → excluidas por diseño; preservadas en
  `publication-repository/runs/` con sus nombres históricos.
