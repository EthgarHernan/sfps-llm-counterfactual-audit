# PROVENANCE AUDIT — BORRADOR UISRAEL (2026-09-07)

Regla L: el DOCX **no** es fuente de verdad. Cada cifra/tabla/figura del borrador
re-dirige a su archivo final del handoff congelado `MANUSCRIPT_FINAL_HANDOFF_20260907/`
y su `source_sha256`. El ledger append-only del juez es la evidencia primaria del juez;
`06_FINAL_JUDGE_RESULTS.csv` es la materialización derivada verificada (no se recalcula).

| Elemento del borrador | claim_ids (02_FINAL_NUMBERS.csv) | Archivo final del handoff | sha256 (16 hex) |
|---|---|---|---|
| Resumen: 5 cohortes, 2800 respuestas válidas, gate 0,95 | ^M-.+-0[1-5]$ + ^P-0\d$ (49 filas) | `02_FINAL_NUMBERS.csv + V4_QC_TAXONOMY.json` | `` |
| Resumen/Método: 40 escenarios, 3 pares, 2 brazos, control C (560 tareas/modelo) | ^P-(0[1-9]|1[0-4])$ + ^M-.+-0[1-5]$ (54 filas) | `02_FINAL_NUMBERS.csv` | `fcc1ea277a50b6f824c8017651ffce12c875373f8ae808f75e02aa0dda821ace` |
| Método: seed 42, temperatura 0,0, máx. 2 reintentos | ^P-(0[1-9]|1[0-4])$ (14 filas) | `02_FINAL_NUMBERS.csv` | `fcc1ea277a50b6f824c8017651ffce12c875373f8ae808f75e02aa0dda821ace` |
| Método: juez gpt-5.6-terra, 2400/2400, 0 errores, USD 7,132306, tokens | ^J-(0[1-9]|1[0-2])$ (12 filas) | `06_FINAL_JUDGE_RESULTS.csv + 06_FINAL_JUDGE_COST_REPORT.csv (ledger = fuente autoritativa)` | `` |
| Resultados A/B: severidad y empatía por brazo (0,058–0,375 / 2,958–3,633) | ^J-(1[3-9]|[2-9]\d|1[0-1]\d|112)$ (107 filas) | `06_FINAL_JUDGE_RESULTS.csv` | `c03f68274c437fe91b31a86584e436467a4efa19c9009ef09c0864532c5efbd5` |
| Resultados: flags del juez (privacy 53–74 de 120 en gemma-3n) | ^J-2[1-9]$ + ^J-[3-9]\d$ + ^J-1[0-2]\d$ (102 filas) | `06_FINAL_JUDGE_RESULTS.csv` | `c03f68274c437fe91b31a86584e436467a4efa19c9009ef09c0864532c5efbd5` |
| Resultados: deltas de severidad +0,083 / +0,075 / −0,083; p 0,017; p_holm 0,205 | ^S-0(0[1-9]|1\d|2[0-4])$ (24 filas) | `04_FINAL_STATISTICAL_RESULTS.csv` | `f1a182ca2b5c3428919bdae693cfa0a03d5449f8d072c411eef716758a5abc82` |
| Resultados B: deltas −0,067 a +0,075, p ≥ 0,143, p_holm 1,0 | ^S-0(0[1-9]|1\d|2[0-4])$ (24 filas) | `04_FINAL_STATISTICAL_RESULTS.csv` | `f1a182ca2b5c3428919bdae693cfa0a03d5449f8d072c411eef716758a5abc82` |
| Resultados: LangFair descriptivo (sentiment 0,005–0,022 VADER) | ^L-(00[1-9]|0[1-3]\d|040)$ (40 filas) | `05_FINAL_LANGFAIR_RESULTS.csv` | `f82c8aefb78d39da21d660ec115ac855ed6c85f0321c71d337cb89f029fc922a` |
| Resultados C: 0/80 expuestas; 600/600 entradas idénticas | ^G-0[7-9]$ + ^G-10$ (4 filas) | `02_FINAL_NUMBERS.csv (fuente: V4_ELIGIBLE_RESPONSES / QC)` | `` |
| Resultados C: estabilidad BLEU/coseno/ROUGE-L (0,261–1,0) | ^L-0(4[1-9]|5[0-5])$ (15 filas) | `05_FINAL_LANGFAIR_RESULTS.csv` | `f82c8aefb78d39da21d660ec115ac855ed6c85f0321c71d337cb89f029fc922a` |
| Método: INEC 5358/4873, 2485/2148 (CORDOVA), 1697/1549 | ^PR-0[1-9]$ (1 filas) | `02_FINAL_NUMBERS.csv` | `fcc1ea277a50b6f824c8017651ffce12c875373f8ae808f75e02aa0dda821ace` |
| Método: validación humana 7 × 90 = 630 ratings | ^H-(0[2-9]|[1-3]\d|4[0-3])$ (42 filas) | `03_FINAL_HUMAN_RESULTS.csv` | `8b3afd931b94939120e923007e6f902db2bc7307ba84ff6fe9076550c6220a70` |
| Limitaciones: Krippendorff 0,0192 / −0,0145 / 0,0256; Spearman −0,0953 / +0,1794 | ^H-(1[4-9]|[2-3]\d|4[0-1])$ (28 filas) | `03_FINAL_HUMAN_RESULTS.csv` | `8b3afd931b94939120e923007e6f902db2bc7307ba84ff6fe9076550c6220a70` |
| Limitaciones: DeepSeek 560 tareas, 563 intentos (3 retries) | ^M-ROBUSTNESS_V4_DEEPSEEK-\d+$ + ^P-(0[1-9]|1[0-4])$ (22 filas) | `02_FINAL_NUMBERS.csv` | `fcc1ea277a50b6f824c8017651ffce12c875373f8ae808f75e02aa0dda821ace` |
| Fig. 1 | ^L-(00[1-9]|0[1-3]\d|040)$ (40 filas) | `figures/fig1_langfair_ci_v4.png` | `5a455d12f75d8c3e` |
| Fig. 2 | ^M-.+-0[1-5]$ + ^P-0\d$ (49 filas) | `figures/fig2_qc_gate_v4.png` | `a46df4d24c3a7b51` |
| Fig. 3 | ^G-0[7-9]$ + ^G-10$ + ^L-0(4[1-9]|5[0-5])$ (19 filas) | `figures/fig3_masked_stability_v4.png` | `985c13dc0448620b` |
| Fig. 4 | ^L-00[1-8]$ + ^S-0(2[5-9]|3\d|40)$ (24 filas) | `figures/fig4_robustness_langfair_v4.png` | `8b935200271d7596` |

## Juez (provenance especial)

- Ledger autoritativo: `results/FINAL_CONFIRMATORY_V4_20260906/deepeval_judge_v4_ledger.jsonl`
  (2400/2400, 0 errores, append-only).
- Derivado verificado: `06_FINAL_JUDGE_RESULTS.csv` sha `c03f6827…` (OI-15 cerrada).
- NO se recalculó el juez para este borrador.

## Figuras (copiadas verbatim a word/media del docx)

- `fig1_langfair_ci_v4.png`: `5a455d12f75d8c3e`
- `fig2_qc_gate_v4.png`: `a46df4d24c3a7b51`
- `fig3_masked_stability_v4.png`: `985c13dc0448620b`
- `fig4_robustness_langfair_v4.png`: `8b935200271d7596`

## Hashes de los CSVs del handoff (01_SOURCE_OF_TRUTH.md)

- `02_FINAL_NUMBERS.csv`: `fcc1ea277a50b6f824c8017651ffce12c875373f8ae808f75e02aa0dda821ace`
- `03_FINAL_HUMAN_RESULTS.csv`: `8b3afd931b94939120e923007e6f902db2bc7307ba84ff6fe9076550c6220a70`
- `04_FINAL_STATISTICAL_RESULTS.csv`: `f1a182ca2b5c3428919bdae693cfa0a03d5449f8d072c411eef716758a5abc82`
- `05_FINAL_LANGFAIR_RESULTS.csv`: `f82c8aefb78d39da21d660ec115ac855ed6c85f0321c71d337cb89f029fc922a`
- `06_FINAL_JUDGE_RESULTS.csv`: `c03f68274c437fe91b31a86584e436467a4efa19c9009ef09c0864532c5efbd5`
- `06_FINAL_JUDGE_COST_REPORT.csv`: `e3f7ee05d3510a899a9e64f51c73e881c232de194912c6dd471be9575ac4a6d1`
- `V4_QC_TAXONOMY.json`: `b4501da0f004fd20a309d904a1b5fd2867b3508b0bdfda99614b3d463c74789`
