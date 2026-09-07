# CONTROL C DENOMINATOR AUDIT — V4 UISRAEL (2026-09-07, auditoría de provenance, NO experimento nuevo)

> **APLICADO 2026-09-07 en `IAA-GRUPO6-ART_V4_UISRAEL_PRECODEX.docx` (M-11):** las 5 correcciones de
> precisión de este archivo están aplicadas — "0 de 80 tareas expuestas por modelo (0 de 400 en las
> cinco cohortes)", "600 de 600 comparaciones métricas entre réplicas idénticas (5 modelos × 40
> escenarios × 3 métricas)", "tasa de exposición … 0 de 80 tareas por modelo", pie de Fig. 2
> "comparaciones" (no "entradas") y Tabla IV con esas unidades. Resumen y Conclusiones usan las cifras
> solo con las unidades demostradas.

Objetivo: demostrar desde los artefactos congelados (código, config, CSVs, manifest) el significado
exacto de **0/80** y **600/600**, usados en el borrador (P211 matriz, P261 Conclusiones, pie de Fig. 3
propuesto). Regla del autor: no inferir ni aproximar denominadores; toda explicación debe provenir de
código/ledger/manifiesto; si una cifra no puede demostrarse, no se usa en Resumen ni Conclusiones.

## Veredicto del gate

**PASS — ambas cifras quedan demostradas de forma inequívoca desde los artefactos.**
Ambas pueden usarse en Resumen/Conclusiones **solo** con las correcciones de precisión de la sección
final (añadir "por modelo" a 0/80; definir 600 como filas de comparación métrica; no extender "fuga
medible" más allá de la tasa de exposición).

## Tabla de denominadores

| métrica | numerador | denominador | unidad | por_modelo/global | factorización_del_denominador | source_file | claim_id | sha256 |
|---|---|---|---|---|---|---|---|---|
| Tasa de exposición del proxy en C | 0 | 80 | tareas C (generaciones) | **POR MODELO** | 80 = 40 escenarios × 2 réplicas técnicas (`c_tasks: 80`, `replicates_per_scenario: 2`) | `publication-repository/config/confirmatory_experiment_v4_20260906.yaml` | G-07 | `87bfbd97871d30c059a75ff3683ecc1d959a8d68aa398b5ea5f8ee21657349fc` |
| Tareas C totales (5 modelos) | 0 | 400 | tareas C (generaciones) | global | 400 = 5 modelos × 80 | config v4 (`c_tasks: 80`) + `V4_QC_TAXONOMY.json` (5 cohortes COMPLETED) | G-07 (derivación global) | config `87bfbd97…` |
| Filas de estabilidad enmascarada | 600 | 600 | filas de comparación métrica pairwise entre réplicas | global | 600 = 5 modelos × 40 escenarios × 3 métricas (cosine, rouge_l, bleu; **sentimiento excluido por diseño**) | `results/FINAL_CONFIRMATORY_V4_20260906/langfair_masked_stability.csv` (600 filas) | G-09, G-10 | `62275410080688b9b4991a716110555e0c95409aa755e185ffc308f029cbcd70` |
| Comparaciones con inputs idénticos | 600 | 600 | filas con `inputs_identical=True` | global | las mismas 600 filas: 200 pares de réplicas × 3 métricas | `langfair_masked_stability.csv` | G-10 | `62275410…` |
| Pares elegibles C | 40 | 40 | escenarios C por modelo | por modelo | 40 escenarios, 1 par de réplicas por escenario | `V4_QC_SUMMARY.csv` (200 filas C_MASKED elegibles = 5 × 40) | (derivación) | `45c11eaacd3b4103d3c9482a29e90e3508969f10d02a4a719b2c06e50eeb9cea` |
| Réplicas técnicas por escenario | 2 | 2 | réplicas | por modelo | config `replicates_per_scenario: 2`; brazos `MASKED_CONTROL` A/B | config v4 | G-08 | `87bfbd97…` |
| n por celda C en LangFair | — | 40 | pares (escenarios) por (modelo × métrica) | por modelo | n=40 en las 15 filas `C_MASKED_CONTROL` de `V4_LANGFAIR_RESULTS.csv` | `V4_LANGFAIR_RESULTS.csv` filas C_MASKED_CONTROL | L-041…L-055 | `f82c8aefb78d39da21d660ec115ac855ed6c85f0321c71d337cb89f029fc922a` |

## A. Explicación exacta de 0/80

- **Unidad:** tareas C = generaciones de la condición `C_MASKED`, **por modelo**. La config congelada lo
  declara literalmente: `c_tasks: 80  # 40 scenarios x 2 replicates`.
- **Factorización:** 80 = 40 escenarios × 2 réplicas técnicas (`replicates_per_scenario: 2`; brazos
  `MASKED_CONTROL` A y B, claves `run_id|model|C_MASKED|scenario|MASKED_CONTROL|A|B` en
  `run_langfair_v4.py` líneas 130–132).
- **Modelos:** los 5 (3 primarios + gpt-5.4 + deepseek). Total global = **400 tareas C**
  (5 × 80), consistente con 2800 = 5 × (480 A/B + 80 C).
- **Numerador 0:** política de proxy `proxy_policy: replace_with_SOCIO_ID` (config v4); el código fija
  `attribute_exposed=False` para toda fila enmascarada (`run_langfair_v4.py` línea 171) y las 600 filas
  del CSV tienen `attribute_exposed=False`. Cero tareas con el apellido expuesto.

## B. Explicación exacta de 600/600

- **Unidad:** filas del CSV `langfair_masked_stability.csv` — comparaciones métricas pairwise de LangFair
  (`CounterfactualMetrics`, `how="pairwise"`, sin `neutralize_tokens`) entre las **dos réplicas técnicas
  enmascaradas** de cada escenario. **No son generaciones**: son métricas derivadas sobre las 400 tareas C.
- **Factorización:** 600 = **5 modelos × 40 escenarios × 3 métricas** (cosine, rouge_l, bleu). El
  sentimiento está excluido por diseño (`if canonical == "sentiment_bias": continue`, línea 163) → no hay
  filas de sentimiento en C.
- **Conteo verificado en disco:** 600 filas totales, 120 por modelo (5 × 120), 40 escenarios por modelo;
  `inputs_identical=True` en 600/600 y `attribute_exposed=False` en 600/600.
- **Por qué NO contradice 2800:** 2800 es el total de **generaciones** válidas (5 cohortes × 560 tareas;
  QC `VALID_FINAL_RESPONSE=2800`). Las 400 generaciones C (200 pares × 2 brazos) producen las 600 filas
  (200 pares × 3 métricas). Unidades distintas: generaciones vs filas derivadas. gemma-4 presenta
  BLEU/coseno/ROUGE-L = 1,0 por temperatura 0 (determinismo declarado en P240, no hallazgo de equidad).

## C. Condición C global (reporte explícito)

| Concepto | Valor | Fuente |
|---|---|---|
| Tareas C por modelo | 80 (40 esc × 2 réplicas) | config v4 `c_tasks: 80`; G-07/G-08 |
| Tareas C totales (5 modelos) | 400 generaciones | 5 × 80; consistente con `V4_QC_TAXONOMY.json` |
| Comparaciones/controles de identidad | 600 filas | `langfair_masked_stability.csv`; G-09/G-10 |
| Exposiciones | 0 | `attribute_exposed=False` ×600 |
| Réplicas por escenario | 2 | config v4; G-08 |

**No escribir "600 generaciones C"**: el ledger demuestra 400 generaciones C (2 por escenario por
modelo). "600/600" son comparaciones métricas, no generaciones.

## Correcciones de precisión obligatorias en el manuscrito (cuando se autorice editar)

1. **P261 (Conclusiones):** "0 de 80 tareas expuestas" → **"0 de 80 tareas expuestas por modelo
   (0 de 400 en las cinco cohortes)"**. El claim G-07 dice "0/80 tareas por modelo"; sin el calificador
   la cifra es ambigua.
2. **P261:** "600 de 600 entradas idénticas entre réplicas" → **"600 de 600 comparaciones métricas entre
   réplicas idénticas (5 modelos × 40 escenarios × 3 métricas)"**. "Entradas" no es la unidad demostrada.
3. **P261:** "la fuga medible de la señal nominal hacia el modelo generativo fue del 0 %" → restringir a
   la cifra demostrada: **tasa de exposición del proxy en el control enmascarado = 0/80 por modelo**.
   "Fuga medible" como concepto de fuga de datos no fue medido (se alinea con O-11/O-19 de
   OVERCLAIM_AUDIT).
4. **Pie de Fig. 3 propuesto (FIGURE_LAYOUT_AUDIT):** cambiar "600 de 600 entradas idénticas" por
   "600 de 600 comparaciones entre réplicas idénticas".
5. **P211 (matriz):** se elimina con la matriz (B-2); el texto de reemplazo en Tabla IV (T08) debe usar
   las unidades de esta auditoría.

## Alcance

Esta verificación es auditoría de provenance sobre artefactos congelados V4. **No es un experimento
nuevo, no recalcula nada y no modifica ningún resultado.** No se usó ningún número de este archivo fuera
de las cifras ya presentes en el handoff congelado.
