# 08 — FIGURAS FINALES (V4)

Fuente: `figures/` de `results/FINAL_CONFIRMATORY_V4_20260906/`, copiadas
verbatim a `figures/` de este handoff. Script generador:
`publication-repository/src/analysis/build_figures_v4.py`. Hashes según
`MASTER_FIGURES.csv` (pack de evidencia).

| # | Archivo | Contenido | sha256 (script) |
|---|---|---|---|
| Figura 1 | `figures/fig1_langfair_ci_v4.png` | IC95% LangFair por modelo y condición (cosine / ROUGE-L / BLEU / sentiment_bias; A_BASE vs B_FAIRNESS; PRIMARY + SECONDARY_ROBUSTNESS) | `5a455d12f75d8c3e5f11d8f5978a2958a08d085f9d0a1540059eb85eb8b9a627` |
| Figura 2 | `figures/fig2_qc_gate_v4.png` | Gate de QC por cohorte: 280/280 pares y tasa 1.0 por modelo contra el umbral congelado 0.95 | `a46df4d24c3a7b51581bc030b10d5449408b9f2e4f5ffdf727f5b5a90b3df927` |
| Figura 3 | `figures/fig3_masked_stability_v4.png` | Estabilidad del control enmascarado C entre las 2 réplicas por escenario (inputs_identical=true); gemma-4 idéntico por determinismo | `985c13dc0448620b0310d67227ef7deec14d11c930948034fe1ed2e927afcafc` |
| Figura 4 | `figures/fig4_robustness_langfair_v4.png` | LangFair descriptivo de las cohortes de robustez GPT y DeepSeek (fuera del análisis primario) | `8b935200271d7596e5efe227910ed679093be0c46e9c1b710af7df486f42400d` |

Reglas de uso:

- No regenerar las figuras; no editar los PNG (los hashes del script quedan
  registrados; si se cambia el script, es una nueva versión y debe
  re-publicarse el paquete).
- Si el comité exige vectores (SVG/EPS), regenerar con el MISMO script
  `build_figures_v4.py` y los MISMOS CSVs congelados, y registrar el nuevo hash;
  no se vale re-dibujar a mano.
- Pies de figura IEEE: "Fig. 1." con descripción técnica y fuente de datos
  (archivo CSV + n). Los textos sugeridos están en `MASTER_FIGURES.csv`.
