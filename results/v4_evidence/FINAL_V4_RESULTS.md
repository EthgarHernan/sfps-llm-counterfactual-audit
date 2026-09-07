# FINAL CONFIRMATORY V4 — Resultados (2026-09-06)

Protocolo: FINAL_CONFIRMATORY_PROTOCOL_V4_20260906 (clean-room; V3 y recuperaciones = ENGINEERING_PRETEST/TECHNICAL_VALIDATION, excluidas).

## Cohorte V4 (5 modelos × 560 tareas = 2800 generaciones)

| Modelo | run_id | Pares elegibles | Tasa | Gate 0,95 |
|---|---|---|---|---|
| gemini-3.7-flash | FINAL_V4_GEMINI37 | 280/280 | 1.0 | True |
| gemma-4-31b-it | FINAL_V4_GEMMA4 | 280/280 | 1.0 | True |
| gemma-3n-e4b-it-text | FINAL_V4_GEMMA3N_LOCAL | 280/280 | 1.0 | True |
| gpt-5.4-2026-03-05 | ROBUSTNESS_V4_GPT54 | 280/280 | 1.0 | True |
| deepseek-v4-pro | ROBUSTNESS_V4_DEEPSEEK | 280/280 | 1.0 | True |

Taxonomía QC V4: {'VALID_FINAL_RESPONSE': 2800}

## Canary técnico (5 claves históricas × 5 modelos)

all_models_passed = True

## Juez DeepEval (gpt-5.6-terra, reasoning low, 1024)

Filas de juez: 2400

## LangFair (descriptivo) y estadística predeclarada

LangFair filas: 55; estadística filas: 155

Nota VADER: DESCRIPTIVE_ONLY_VADER_SPANISH_LIMITATION. p>0,05 no es evidencia de ausencia de sesgo.

## Exclusión de cohortes previas

Ninguna respuesta V3 o de recuperación forma parte del conjunto analítico V4.
