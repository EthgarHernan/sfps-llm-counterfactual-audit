# 07 — TABLAS FINALES, FÓRMULAS Y MÉTRICAS (V4)

Toda cifra de este archivo proviene de `02_FINAL_NUMBERS.csv` (ver `claim_id`
indicado bajo cada tabla). No inventar ni recomputar. Las tablas candidatas
para el manuscrito llevan número sugerido (T01–T12, alineado con
`evidence/MANUSCRIPT_EVIDENCE_PACK_20260907/MASTER_TABLES.csv`); el número
final depende del orden en el cuerpo del artículo.

---

## T01 — Cohorte V4 y gate de QC *(M-*-01..05, P-01..P-14)*

| Modelo | run_id | Rol | Pares elegibles | Tasa | Gate 0,95 |
|---|---|---|---|---|---|
| gemini-3.7-flash | FINAL_V4_GEMINI37 | PRIMARIO | 280/280 | 1.0 | ✓ |
| gemma-4-31b-it | FINAL_V4_GEMMA4 | PRIMARIO | 280/280 | 1.0 | ✓ |
| gemma-3n-e4b-it-text (local) | FINAL_V4_GEMMA3N_LOCAL | PRIMARIO | 280/280 | 1.0 | ✓ |
| gpt-5.4-2026-03-05 | ROBUSTNESS_V4_GPT54 | ROBUSTEZ | 280/280 | 1.0 | ✓ |
| deepseek-v4-pro | ROBUSTNESS_V4_DEEPSEEK | ROBUSTEZ | 280/280 | 1.0 | ✓ |

Protocolo: 40 escenarios × 3 pares nominales × 2 brazos contrafactuales (A/B) =
480 tareas A/B por modelo + 80 tareas del control enmascarado C = **560 tareas
por modelo; 2800 totales**. QC: `VALID_FINAL_RESPONSE = 2800`. Seed 42,
temperatura 0.0, máx. 2 retries técnicos por clave lógica. DeepSeek: 560 tareas
válidas, **563 intentos** (3 retries técnicos documentados).

## T02 — Configuración congelada de modelos *(M-*-06..08)*

| Modelo | Provider | Thinking / reasoning | Temperature | max_output_tokens |
|---|---|---|---|---|
| gemini-3.7-flash | Google | `thinking_level=medium` | 0.0 | 8192 |
| gemma-4-31b-it | Google | `thinking_level=high` | 0.0 | 8192 |
| gemma-3n-e4b-it-text | LM Studio (artefacto congelado) | n/a | 0.0 | 2048 |
| gpt-5.4-2026-03-05 | OpenAI Responses | `reasoning={"effort":"none"}` | NOT_SENT | 8192 |
| deepseek-v4-pro | DeepSeek | `thinking` enabled + `reasoning_effort=high` | NOT_SENT | 8192 |

## T03 — LangFair A/B por modelo × condición *(L-009..L-040)*

n=120 pares por celda; media (IC95%). `sentiment_bias` = VADER, marcado
**DESCRIPTIVE_ONLY_VADER_SPANISH_LIMITATION** (léxico inglés).

| Modelo | Condición | BLEU | Cosine (MiniLM) | ROUGE-L | Sentiment (VADER) |
|---|---|---|---|---|---|
| gemini-3.7-flash | A_BASE | 0.374 (0.344–0.405) | 0.831 (0.818–0.844) | 0.598 (0.571–0.624) | 0.007 (0.004–0.010) |
| gemini-3.7-flash | B_FAIRNESS | 0.395 (0.365–0.425) | 0.833 (0.820–0.846) | 0.616 (0.591–0.641) | 0.005 (0.003–0.008) |
| gemma-4-31b-it | A_BASE | 0.546 (0.498–0.596) | 0.867 (0.849–0.885) | 0.704 (0.666–0.743) | 0.009 (0.005–0.013) |
| gemma-4-31b-it | B_FAIRNESS | 0.549 (0.498–0.600) | 0.865 (0.844–0.885) | 0.702 (0.662–0.743) | 0.014 (0.009–0.019) |
| gemma-3n local | A_BASE | 0.472 (0.421–0.529) | 0.839 (0.819–0.859) | 0.588 (0.544–0.637) | 0.010 (0.007–0.013) |
| gemma-3n local | B_FAIRNESS | 0.479 (0.430–0.529) | 0.847 (0.829–0.864) | 0.606 (0.564–0.649) | 0.013 (0.009–0.017) |
| gpt-5.4 (ROB) | A_BASE | 0.371 (0.338–0.406) | 0.842 (0.828–0.856) | 0.577 (0.548–0.606) | 0.019 (0.014–0.024) |
| gpt-5.4 (ROB) | B_FAIRNESS | 0.375 (0.348–0.404) | 0.842 (0.829–0.857) | 0.566 (0.539–0.595) | 0.020 (0.015–0.024) |
| deepseek-v4 (ROB) | A_BASE | 0.272 (0.241–0.306) | 0.778 (0.762–0.795) | 0.476 (0.448–0.507) | 0.022 (0.015–0.028) |
| deepseek-v4 (ROB) | B_FAIRNESS | 0.268 (0.236–0.300) | 0.781 (0.764–0.797) | 0.481 (0.453–0.510) | 0.018 (0.013–0.024) |

## T04 — Estadística predeclarada: contrastes primarios (12) y sensibilidad *(S-001..S-024)*

Delta por escenario (n=40), IC95 bootstrap, p de permutación, Wilcoxon, Holm.
**Ningún contraste es significativo tras corrección de Holm** (todos
`significant_005=False`).

| Modelo | Condición | Métrica | Δ escenario | IC95 | p perm | p Holm | r_b |
|---|---|---|---|---|---|---|---|
| gemini-3.7-flash | A_BASE | severidad | +0.083 | [0.008, 0.167] | 0.063 | 0.694 | 0.654 |
| gemini-3.7-flash | A_BASE | empatía | +0.017 | [−0.075, 0.108] | 0.692 | 1.0 | 0.087 |
| gemini-3.7-flash | B_FAIRNESS | severidad | 0.000 | [−0.083, 0.083] | 1.0 | 1.0 | 0.0 |
| gemini-3.7-flash | B_FAIRNESS | empatía | −0.033 | [−0.108, 0.042] | 0.488 | 1.0 | −0.288 |
| gemma-4-31b-it | A_BASE | severidad | +0.075 | [0.017, 0.133] | **0.017** | **0.205** | 0.822 |
| gemma-4-31b-it | A_BASE | empatía | +0.025 | [−0.042, 0.100] | 0.601 | 1.0 | 0.236 |
| gemma-4-31b-it | B_FAIRNESS | severidad | −0.067 | [−0.142, 0.008] | 0.143 | 1.0 | −0.538 |
| gemma-4-31b-it | B_FAIRNESS | empatía | +0.008 | [−0.083, 0.092] | 0.772 | 1.0 | 0.090 |
| gemma-3n local | A_BASE | severidad | −0.083 | [−0.175, 0.000] | 0.066 | 0.694 | −0.433 |
| gemma-3n local | A_BASE | empatía | +0.075 | [−0.042, 0.192] | 0.257 | 1.0 | 0.254 |
| gemma-3n local | B_FAIRNESS | severidad | +0.075 | [−0.017, 0.167] | 0.171 | 1.0 | 0.371 |
| gemma-3n local | B_FAIRNESS | empatía | −0.058 | [−0.200, 0.083] | 0.490 | 1.0 | −0.154 |

Sensibilidad predeclarada **sin P002** (12 contrastes adicionales, S-013..S-024):
ninguna significativa tras Holm (mayor p_holm observado de la familia: 0.911).
Los contrastes secundarios por par (S-901: 36 primarios; S-902: 24 robustez) y
de robustez GPT/DeepSeek (S-025..S-040) tampoco son significativos tras Holm.
Convención de interpretación: **p>0,05 ≠ ausencia de sesgo** (limitación de
potencia con n=40 escenarios).

## T05 — Juez DeepEval: cobertura, costo y tokens *(J-01..J-12)*

| Métrica | Valor |
|---|---|
| Filas juzgadas / esperadas | 2400 / 2400 (480 por modelo × 5) |
| Errores | 0 |
| Modelo juez | gpt-5.6-terra (reasoning low, 1024 tokens, structured, `store=false`) |
| Costo total | USD 7.132306 (promedio 0.00297179 USD/respuesta) |
| Tokens input / output / reasoning | 1 290 377 / 379 296 / 104 576 |
| Precios (USD/M) | input 2.0 · cached 0.2 · output 12.0 |
| Costo por modelo (480 filas) | deepseek 1.3386 · gemini-3.7 1.4182 · gemma-3n 1.5869 · gemma-4 1.3548 · gpt-5.4 1.4339 |

## T06 — Severidad y empatía del juez por brazo y condición *(J-13..J-112)*

Media (mediana), escala 0–5, n=120 por celda.

| Modelo | Condición | Sev A | Sev B | Emp A | Emp B |
|---|---|---|---|---|---|
| deepseek-v4-pro | A_BASE | 0.125 (0.0) | 0.133 (0.0) | 3.400 (3.0) | 3.433 (3.0) |
| deepseek-v4-pro | B_FAIRNESS | 0.100 (0.0) | 0.142 (0.0) | 3.350 (3.0) | 3.333 (3.0) |
| gemini-3.7-flash | A_BASE | 0.258 (0.0) | 0.175 (0.0) | 3.425 (3.5) | 3.408 (3.0) |
| gemini-3.7-flash | B_FAIRNESS | 0.242 (0.0) | 0.242 (0.0) | 3.450 (3.0) | 3.483 (4.0) |
| gemma-3n local | A_BASE | 0.292 (0.0) | 0.375 (0.0) | 3.033 (3.0) | 2.958 (3.0) |
| gemma-3n local | B_FAIRNESS | 0.383 (0.0) | 0.308 (0.0) | 2.975 (3.0) | 3.033 (3.0) |
| gemma-4-31b-it | A_BASE | 0.275 (0.0) | 0.200 (0.0) | 3.300 (3.0) | 3.275 (3.0) |
| gemma-4-31b-it | B_FAIRNESS | 0.150 (0.0) | 0.217 (0.0) | 3.400 (3.0) | 3.392 (3.0) |
| gpt-5.4 (ROB) | A_BASE | 0.083 (0.0) | 0.058 (0.0) | 3.558 (4.0) | 3.608 (4.0) |
| gpt-5.4 (ROB) | B_FAIRNESS | 0.058 (0.0) | 0.058 (0.0) | 3.575 (4.0) | 3.633 (4.0) |

## T07 — Frecuencia de los cinco flags del juez (conteo A/B, n=120) *(J-21..J-122)*

| Modelo | Condición | threat | humillación | inventado | privacidad | ignorado |
|---|---|---|---|---|---|---|
| deepseek-v4 | A_BASE | 0/0 | 0/0 | 0/0 | 0/1 | 0/0 |
| deepseek-v4 | B_FAIR | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| gemini-3.7 | A_BASE | 0/0 | 2/1 | 0/0 | 0/1 | 0/1 |
| gemini-3.7 | B_FAIR | 0/0 | 1/1 | 0/1 | 2/2 | 0/0 |
| gemma-3n local | A_BASE | 0/0 | 0/0 | 1/2 | **53/54** | 7/6 |
| gemma-3n local | B_FAIR | 0/0 | 0/1 | 0/0 | **74/66** | 5/7 |
| gemma-4 | A_BASE | 0/0 | 2/3 | 3/1 | 1/1 | 0/0 |
| gemma-4 | B_FAIR | 0/0 | 1/1 | 0/0 | 3/1 | 1/1 |
| gpt-5.4 (ROB) | A_BASE | 0/0 | 0/0 | 0/0 | 0/0 | 0/1 |
| gpt-5.4 (ROB) | B_FAIR | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |

Concentración notable: `privacy_or_identity_failure` aparece casi exclusivamente
en gemma-3n local (53–74 de 120 en ambos brazos) y es ≈ 0 en los demás modelos.

## T08 — Control enmascarado C *(L-041..L-055, G-07..G-10)*

Exposición del proxy: **0/80 tareas** (apellido reemplazado por SOCIO_ID);
2 réplicas por escenario; **600/600 filas con inputs idénticos** verificados.
Estabilidad (n=40 réplicas):

| Modelo | BLEU | Cosine | ROUGE-L |
|---|---|---|---|
| gemini-3.7-flash | 0.431 (0.368–0.499) | 0.835 (0.813–0.857) | 0.629 (0.580–0.681) |
| gemma-4-31b-it | **1.000** | **1.000000** | **1.000** |
| gemma-3n local | 0.670 (0.595–0.745) | 0.904 (0.878–0.930) | 0.743 (0.678–0.805) |
| gpt-5.4 (ROB) | 0.389 (0.334–0.445) | 0.838 (0.815–0.860) | 0.563 (0.519–0.606) |
| deepseek-v4 (ROB) | 0.261 (0.212–0.311) | 0.774 (0.743–0.804) | 0.482 (0.436–0.529) |

gemma-4 produce réplicas idénticas en C (determinismo con temperature 0) — NO
presentar como hallazgo de equidad (OI-11). C no tiene `sentiment_bias` por
diseño: el sentimiento se contrasta entre brazos A/B.

## T09 — Validación humana V2 *(H-01..H-43)*

| Métrica | Valor |
|---|---|
| Snapshot de cierre | 2026-09-07T04:22:51.302Z (659 ratings totales) |
| Evaluadores registrados / completos 90-90 / parciales / sin iniciar | 12 / **7** / 3 / 2 |
| Ratings del análisis primario (7 × 90) | 630 |
| Raters por ítem | 7–9 (mediana 7; {7: 64 ítems, 8: 23, 9: 3}) |
| Integridad de textos / hazards de truncamiento | 180/180 / 0 |
| **Krippendorff ordinal (7 raters × 90)** | severidad **0.0192** · empatía **−0.0145** · calidad **0.0256** |
| Acuerdo exacto por pares | severidad 0.399 · empatía 0.379 · calidad 0.399 |
| Unanimidad | severidad 2.2 % · empatía 3.3 % |
| Preferencia por mayoría | sev. A=30/B=41/E=19 · emp. 33/31/26 · cal. 39/40/11 |
| Krippendorff nominal flags (180 slots) | −0.0032 / −0.1125 / −0.0016 / −0.0076 / +0.0039 |
| Juez vs humano: Spearman | severidad **−0.0953** · empatía **+0.1794** |
| Juez vs humano: MAE / kappa lineal | 0.242 / −0.0149 · 0.229 / −0.0631 |
| Cohen kappa de flags | NO_DEFINIDO (threat/humillación/inventado: 0 positivos del juez; privacidad/ignorado: 0 positivos de la mayoría humana) |
| Sensibilidad predeclarada (todos los raters) | 0.0076 / −0.0088 / 0.0276 |
| Mediana de segundos por comparación | 2143.5 s |

Regla de interpretación (OI-12): la falta de discriminación humana **NO
demuestra ausencia de sesgo**; el acuerdo ≈ azar limita la lectura del contraste
humano.

## T10 — Provenance de apellidos (pares nominales) *(PR-01..PR-09)*

| Par | Apellidos sintéticos | Registros derivados INEC 2025 |
|---|---|---|
| P001 | GUAMAN \| SALAZAR | 5358 \| 4873 |
| P002 | CHICAIZA \| CORDOVA | 2485 \| 2148 (caveat ortográfico CORDOVA → excluido de la sensibilidad) |
| P003 | QUISHPE \| AREVALO | 1697 \| 1549 |

Sensibilidad predeclarada sin P002 = P001+P003. La frecuencia INEC es fuente
**administrativa** (no prueba de etnia); la asociación cultural/onomástica va
por fuente académica separada (fila C-14 de la matriz de citas).

## T11 — Apéndices

- Contrastes por par nominal: 36 primarios + 24 secundarios (S-901/S-902); ninguno
  significativo tras Holm dentro de su familia.
- Robustez GPT + DeepSeek: `04_FINAL_STATISTICAL_RESULTS.csv` (S-025..S-040) y
  `evidence/FINAL_CONFIRMATORY_V4_20260906/ROBUSTNESS_GPT_DEEPSEEK.csv`.
- Detalle por columna de estadística: `04_FINAL_STATISTICAL_RESULTS.csv` (155 filas).

## T12 — Limitaciones estructurales (para la sección de limitaciones)

Fuente: `14_LIMITATIONS_AND_CLAIMS.md` (resumen): VADER en español (descriptivo);
p>0,05 ≠ ausencia de sesgo (n=40); acuerdo humano ≈ azar; 3 modelos primarios +
2 de robustez (sin familia Holm conjunta); ética `MISSING` / consentimiento
`NOT_DOCUMENTED`; discrepancia de entorno requirements.txt vs runtime;
`BIBLIOGRAFIA_PENDIENTE` en 3 referencias de método.

---

# FÓRMULAS Y MÉTRICAS (definiciones operacionales)

Fuente de implementación: scripts congelados en `V4_RUN_MANIFEST.json`
(`tooling_sha256`): `run_langfair_v4.py` `e8bf186a…`,
`run_statistics_v4.py` `ba8efb91…`, `run_deepeval_judge_v4.py` `49db6290…`,
`validate_v4_qc.py` `1b5763b8…`; validación humana:
`research/fairness-audit/human_validation_v2/scripts/analyze_ratings_v2.py`.

## 1) Gate de QC

`valid_pair_rate = pares_eligibles / pares_totales` por modelo; pasa si
`≥ 0.95` (umbral congelado). Taxonomía: `VALID_FINAL_RESPONSE` cuenta las
respuestas con texto final válido. Fuente: `V4_QC_TAXONOMY.json`.

## 2) LangFair (descriptivo, secundario)

- `cosine_similarity` = coseno entre embeddings de oraciones
  `all-MiniLM-L6-v2` de las respuestas A y B del par.
- `rouge_l` = ROUGE-L entre respuestas A/B; `bleu` = BLEU entre A/B.
- `sentiment_bias` = diferencia de polaridad VADER entre brazos
  (léxico inglés → **DESCRIPTIVE_ONLY_VADER_SPANISH_LIMITATION**).
- Agregación: media + IC95% por modelo × condición (n=120 pares A/B; n=40
  réplicas C). Paquete: langfair 0.8.0, modo pairwise.

## 3) Juez DeepEval (primario)

- Salida estructurada JSON por respuesta: `severity ∈ [0,5]`, `empathy ∈ [0,5]`
  y 5 flags binarios (threat_or_legal_escalation;
  humiliation_hostility_coercion_or_guilt; invented_information;
  privacy_or_identity_failure; ignored_stop_or_human_request).
- Juez: gpt-5.6-terra, reasoning low, max 1024 tokens, `store=false`, calibración
  de 10 ítems antes de la corrida. Ledger append-only con clave de dedupe
  (run_id, modelo, escenario, par, brazo, **condición**): A_BASE y B_FAIRNESS
  son tareas distintas → 480 filas por modelo, 2400 totales.

## 4) Estadística predeclarada (primario)

- Delta por par: `Δ_par = media_brazoA(par) − media_brazoB(par)` sobre las
  respuestas del juez (120 pares); agregado por escenario: media de los 3 pares
  de cada escenario → **delta por escenario, n=40** (unidad de análisis
  predeclarada).
- IC95%: **bootstrap 5000× con re-muestreo agrupado por escenario**.
- `p_permutation`: **10 000 permutaciones** (dos colas).
- `p_sign_test`: prueba de signos; `wilcoxon`: rangos con signo de Wilcoxon
  (estadístico + p); `rank_biserial` r_b como tamaño de efecto.
- `p_holm`: corrección de Holm dentro de la familia
  (`PRIMARY_JUDGE` para los 12 contrastes primarios;
  `SECONDARY_ROBUSTNESS_JUDGE` para los de robustez).
- Sensibilidad predeclarada: misma batería excluyendo P002 (caveat ortográfico
  CORDOVA documentado en provenance).

## 5) Acuerdo humano (complementario)

- **Krippendorff ordinal** α = 1 − D_o/D_e sobre 7 raters × 90 ítems (3
  categorías) para severidad, empatía y calidad; **nominal binario** para los
  5 flags sobre 180 slots (prevalencia muy baja → inestable).
- Acuerdo exacto por pares de raters; unanimidad; preferencia por mayoría de 7.
- Juez vs humano: Spearman ρ entre preferencia humana media y
  (juez_A − juez_B)/4 normalizado a [−1,1]; MAE; kappa lineal ponderado con
  clases −1/0/+1; Cohen kappa para flags (NO_DEFINIDO cuando un lado tiene 0
  positivos).
- Sensibilidad predeclarada: todos los raters (7–9 por ítem).

## 6) Costos

- Juez: `costo = Σ tokens_i × precio_i` (input 2.0, cached 0.2, output 12.0
  USD por millón) → USD 7.132306 (`JUDGE_COST_REPORT.csv`, reconstruido del
  ledger completo; el CSV por lote se sobrescribe, el ledger es la fuente).
- OpenAI total de la ejecución documentado en el handoff del proyecto: USD 7.90
  (generación GPT ≈ 0.77 + juez 7.13) ≤ 15 autorizado. El costo del juez tiene
  CSV dedicado; el de generación GPT no tiene CSV dedicado (no recomputar).

## 7) Integridad del instrumento humano

- `SHA256(texto_fuente) == SHA256(texto_entregado)` en los 180 textos; hazards de
  truncamiento = 0; el enmascaramiento `[PERSONA]` aplica solo al paquete
  público (el primer nombre es constante "Ana" en todos los brazos: el
  contraste solo varía el APELLIDO — nota para revisores
  `REVIEWER_NOTE_20260906_GENERO_ENMASCARAMIENTO.md`).
