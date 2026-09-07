# 15 — MAPA DE REPRODUCIBILIDAD DE LA PUBLICACIÓN (V4)

Todo artefacto citado en el manuscrito debe poder localizarse desde este mapa.
Fuente de hashes: `V4_RUN_MANIFEST.json` (`tooling_sha256`) y
`MASTER_ARTIFACT_MANIFEST.csv` (copias verbatim en `evidence/`).

## Protocolo congelado

| Artefacto | Ruta original | sha256 |
|---|---|---|
| Config V4 | `publication-repository/config/confirmatory_experiment_v4_20260906.yaml` | `87bfbd97871d30c059a75ff3683ecc1d959a8d68aa398b5ea5f8ee21657349fc` |
| Scheduler runtime | `publication-repository/config/v4_scheduler_runtime_20260906.json` | `7fc76c922501a5bb7a26f6d0d0d8fb1aa3dd73c6b74fb23da244fa3183ad3d0c` |
| Escenarios | `publication-repository/data/derived/scenarios_v3.csv` | `020f6b569d061b75d956325c2caec9eabf69c7ecc8e04f39a5a66c4b0ec9804b` |
| Pares de apellidos | `publication-repository/data/derived/surname_pair_provenance_v3.csv` | `fe4ecd6eb419526c8469aedddd65c75a4a3ec446a408483962bba2deb1b36e5a` |
| Prompt A_BASE (= C) | `publication-repository/config/prompts/collection_agent_base_v2.txt` | `fcb7eef04216515576d15819d0b4b30d698b58a2a08f7c034da25e8eae0ea2cb` |
| Prompt B_FAIRNESS | `publication-repository/config/prompts/collection_agent_fairness_v2.txt` | `32d96b30f3556851a5a1f1720e34bef2410dc5990d15a292db365c3da6794555` |
| Rúbrica del juez | `publication-repository/config/prompts/deepeval_judge_v3.txt` | `7f9cf40a5a524fb000d66d5765203a477fd6a806c7f9107ef6cd54b21c0a6b96` |
| Smoke del juez | `publication-repository/config/smoke_deepeval_v4_20260906.yaml` | (en evidence/config) |

## Tooling congelado (hashes de `V4_RUN_MANIFEST.json`)

| Script | sha256 |
|---|---|
| run_v4_window.py | `a0cd8d0f575d62bf43aa091203d2c3825d638047bb04182b093471b807fd2a33` |
| run_v4_canary.py | `b706db0d9c5f5de578f527012865ae7b7f168df311a759083c1a8108b5a00e08` |
| run_v4_preflight.py | `e062691c9ea2d5f80fcda26e85fff5c9f850fbcc38e4965a192c38ae0f103b5c` |
| v4_providers.py | `b7dce9802ebac9b2222d7a3a8618ac761efa7ba7e236ee8ed9c89125f73778c1` |
| validate_v4_qc.py | `1b5763b88443afc22b3ad975c427c827c4de7803ad21be81121190a83ef2e7b5` |
| run_deepeval_judge_v4.py | `49db6290d23e0307b0bf60e6df489e784ffb555e661fc60d5a62498a242bb7da` |
| run_langfair_v4.py | `e8bf186a8af55497926fb0eb4e6b4082e0c9c8995d34a1c6ba1caf2a92318730` |
| run_statistics_v4.py | `ba8efb91a4582b394a2492ec59038b91d25e10b665374f6262dcf9eaad612367` |
| build_final_results_v4.py | `96d60d789a470d6bea71ae9f03a7a022cddfac27b1fceb7ed9c51745b1d8ab73` |
| v4_scheduler_runtime | `7fc76c922501a5bb7a26f6d0d0d8fb1aa3dd73c6b74fb23da244fa3183ad3d0c` |
| analyze_ratings_v2.py (humano) | ubicado en `research/fairness-audit/human_validation_v2/scripts/` |

## Ledgers (append-only, NO duplicados en este paquete)

| Artefacto | Ruta | sha256 |
|---|---|---|
| Generación gemini-3.7-flash | `runs/FINAL_V4_GEMINI37/generation_attempts.jsonl` | `13a1295aa3410a42fcd62e25f9a2461c2ce8fe8119d6ca18a226db3522951ae2` |
| Generación gemma-4-31b-it | `runs/FINAL_V4_GEMMA4/generation_attempts.jsonl` | `b0f4766d72faa9ee9c638c3b9b48179ae192abc941c4a8cbd2401524426c659c` |
| Generación gemma-3n local | `runs/FINAL_V4_GEMMA3N_LOCAL/generation_attempts.jsonl` | `55dd48ebccec2e0dd4dbd165b8db0c636338a1c36cb9ec3c3af5e6aa47abd0ae` |
| Generación gpt-5.4 | `runs/ROBUSTNESS_V4_GPT54/generation_attempts.jsonl` | `2ebfed8d24473d5a76f200a0e290fb9d9233d9f6fca43f4ab6e8eff3f2702920` |
| Generación deepseek-v4-pro | `runs/ROBUSTNESS_V4_DEEPSEEK/generation_attempts.jsonl` | `962c6dec037f4479a1eff6274a2fecee98f0913cff2073dc252a545cb21a05b4` |
| Juez (2400/2400) | `results/FINAL_CONFIRMATORY_V4_20260906/deepeval_judge_v4_ledger.jsonl` | fuente autoritativa del juez |
| Respuestas elegibles | `results/FINAL_CONFIRMATORY_V4_20260906/V4_ELIGIBLE_RESPONSES.jsonl` | (grande; referenciar) |

## Entorno real de la corrida (run manifests)

Python 3.10.0 · Windows 10.0.26100 · `google-genai 1.74.0` · `openai 2.16.0` ·
`pyyaml 6.0.2` · langfair 0.8.0 · deepeval 4.2.1. Discrepancia con
`requirements.txt` documentada en R-02..R-04 (archivo 14).

## Costos

- Juez gpt-5.6-terra: **USD 7.132306** (2400 respuestas; tokens 1 290 377 /
  379 296 / 104 576) — `06_FINAL_JUDGE_COST_REPORT.csv`.
- OpenAI total documentado en el handoff del proyecto (Bloque 9): **USD 7.90**
  (generación GPT ≈ 0.77 + juez 7.13) ≤ 15 autorizado. El costo de generación
  GPT no tiene CSV dedicado; no recomputar.

## Validación humana — mapa público/privado

| Artefacto | Naturaleza | Ubicación |
|---|---|---|
| HUMAN_VALIDATION_V2_MANIFEST.json | PÚBLICO (agregados) | `evidence/human_validation_v2/` |
| HUMAN_VALIDATION_V2_INTEGRITY.csv | PÚBLICO (180/180, sin textos crudos) | `evidence/human_validation_v2/` |
| HUMAN_VALIDATION_V2_TRUNCATION_AUDIT.txt | PÚBLICO | `evidence/human_validation_v2/` |
| 03_FINAL_HUMAN_RESULTS.csv | PÚBLICO (agregados, 0 menciones de EVALUADOR_) | raíz del handoff |
| tokens.csv / key.csv / calificaciones.csv | **PRIVADOS — nunca publicar** | `research/fairness-audit/human_validation_v2/server-private-v2/` + descarga del autor |

## Corridas excluidas (clean-room)

`CONFIRMATORY_TEXT_V3`, `CONFIRMATORY_GEMINI37_RECOVERY_V1`,
`CONFIRMATORY_GEMMA4_RECOVERY_V1`, `CONFIRMATORY_GEMINI37_FINAL_V2`,
`CONFIRMATORY_GEMMA4_FINAL_V2`, `CONFIRMATORY_GEMMA4_FINAL_V3` — preservadas
append-only, excluidas del análisis, nunca regeneradas como V4
(`V4_RUN_MANIFEST.json`).

## Incidentes que respaldan decisiones

- `INCIDENT_2026-09-06_DEEPSEEK_ISOLATED_EMPTY_V4.md` (3 anomalías aisladas, 3 retries).
- `VERIFICATION_2026-09-06_JUDGE_DENOMINATOR_950.md` (denominador parcial de un snapshot; ledger final completo).
- `REVIEWER_NOTE_20260906_GENERO_ENMASCARAMIENTO.md` ("doña Ana": el primer nombre es constante; el contraste varía solo el apellido).
- Auditoría bibliográfica completa: `evidence/AUDITORIA_BIBLIOGRAFICA_20260907/`.
