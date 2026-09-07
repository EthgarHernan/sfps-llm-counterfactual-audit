# 14 — LIMITACIONES Y REGLAS DE AFIRMACIÓN (V4)

Fuente: `MASTER_OPEN_ISSUES.md` del pack de evidencia (copia en
`evidence/MANUSCRIPT_EVIDENCE_PACK_20260907/`). Ninguna incidencia altera los
datos finales V4; son de presentación, documentación o entorno. **No corregir
silenciosamente**: cada corrección requiere decisión del autor.

## Limitaciones estadísticas y de medición

1. **VADER es léxico inglés** → todas las filas `sentiment_bias` de LangFair son
   `DESCRIPTIVE_ONLY_VADER_SPANISH_LIMITATION`; no presentar como inferencia de
   equidad.
2. **p>0,05 ≠ ausencia de sesgo**: n=40 escenarios limita la potencia; el único
   p_perm < 0.05 antes de Holm (Gemma-4, A_BASE, severidad: 0.017) no sobrevive
   la corrección (p_holm 0.205). Redactar siempre "ningún contraste
   significativo tras Holm".
3. **Validación humana**: Krippendorff ordinal ≈ azar (0.019 / −0.015 / 0.026);
   unanimidad 2.2–3.3 %; los humanos no discriminan A vs B de forma fiable en
   esta muestra. **La falta de discriminación humana no demuestra ausencia de
   sesgo.** Cohen kappa de flags NO_DEFINIDO por ausencia de positivos en un
   lado (no reportar como "0").
4. **Condición C**: sin `sentiment_bias` por diseño; gemma-4 produce réplicas
   idénticas (BLEU/cosine/ROUGE = 1.0) por determinismo con temperature 0 →
   no presentar como hallazgo de equidad (OI-11).
5. **DeepSeek**: 560 tareas válidas, 563 intentos (3 retries técnicos, incidente
   `INCIDENT_2026-09-06_DEEPSEEK_ISOLATED_EMPTY_V4.md`). Redactar siempre
   "560 tareas; 563 intentos (3 retries)" (OI-10).
6. **Robustez GPT/DeepSeek** es secundaria: fuera de la familia Holm primaria
   (se reporta separada, T11/Fig. 4).
7. **Provenance de apellidos**: la frecuencia INEC (Visualizador 2025) es
   fuente administrativa de registro derivado; NO prueba etnia. La asociación
   cultural/onomástica requiere fuente académica separada. P002 excluida de la
   sensibilidad por caveat ortográfico CORDOVA (PR-09).

## Ética

- **E-01**: aprobación ética institucional = `MISSING` (no hay documento de
  comité/CEISH/IRB en el repositorio).
- **E-02**: consentimiento informado de evaluadores = `NOT_DOCUMENTED` (la
  pantalla inicial tiene instrucciones, no consentimiento).
- **E-03**: la declaración de titulación UISRAEL cubre solo datos de los
  autores; no es aprobación ética del estudio.
- El artículo debe **declarar el estado real**, no omitirlo (OI-14).

## Reproducibilidad / entorno

- **R-02..R-04 (OI-05)**: requirements.txt fija versiones distintas del runtime
  real de los manifests V4 (`google-genai 2.22.0` vs `1.74.0`; `openai 3.8.0`
  vs `2.16.0`; `pyyaml 6.0.3` vs `6.0.2`). Decidir: alinear requirements o
  documentar la diferencia.
- **OI-06**: `V4_TECHNICAL_LOG.csv` vacío (solo header); la auditoría de eventos
  vive en los ledgers append-only.
- **OI-07**: `WAITING_FOR_CONNECTIVITY.json` es estado transitorio del juez
  (recuperado solo; 2400/2400 completo) → mover a `docs/incidents/` antes de
  publicar.
- **OI-08**: manifest e integridad de validación humana viven en
  `human_validation_v2/` (existen, hash verificado) — documentar ubicación.
- **OI-09**: los preflights históricos son PRE-GO; no citarlos como posteriores
  a la corrida. Evidencia post-GO = `V4_RUN_MANIFEST.json`, QC, ledgers.

## Referencias del manuscrito (obligatorias al editar)

- **OI-01**: [4] "dic. 2026" → **ene. 2026** (Crossref 2026-01-11).
- **OI-02**: [5] "dic. 2025" → **jul. 2025** (Crossref 2025-07-30).
- **OI-03**: [9] y [13] "Springer Nature" → revista **Humanities and Social
  Sciences Communications** (Springer Nature = editorial).
- **OI-04**: los marcadores de cita son campos de Word → contrastar contra el
  PDF renderizado antes de la entrega final.
- **Matriz de citas** (`09_CLAIM_CITATION_MATRIX.csv`): 20 de 34 afirmaciones
  quedaron NO_SUPPORT (por cita incorrecta u omisión) — aplicar los reemplazos
  del `13_ARTICLE_SECTION_MAP.md`; no reutilizar las referencias rechazadas en
  esas frases.
- **BIBLIOGRAFIA_PENDIENTE** (archivo 10, sección D): V4[13] An 2024, V4[15]
  Pawar 2025, V4[18] Chen LLM-as-judge — **CONFIRMADAS por el autor e incorporadas
  al corpus como R92–R94 (2026-09-07)**; caveat de Pawar documentado (sección D).

## OI-15 — estado actualizado en este handoff (2026-09-07)

Detectado el 2026-09-07: `V4_DEEPEVAL_RESULTS.csv` (sha `c03f6827…`) desapareció
del disco entre dos lecturas; este agente no lo tocó. **Al verificar para este
handoff el archivo existe de nuevo y su SHA-256 actual coincide exactamente con
el citado en las filas J-*** → copiado verbatim como
`06_FINAL_JUDGE_RESULTS.csv`. El ledger `deepeval_judge_v4_ledger.jsonl`
(2400/2400, 0 errores) sigue siendo la fuente autoritativa.

## Asuntos abiertos de decisión del autor (no automatizar)

1. Actualizar el manuscrito con los números V4 (fuente: este paquete) — go
   explícito del autor.
2. ~~Confirmar las 3 fuentes de BIBLIOGRAFIA_PENDIENTE~~ — **RESUELTO 2026-09-07**:
   An 2024 (10.18653/v1/2024.acl-short.37) → **R92**, Pawar 2025
   (10.18653/v1/2025.findings-emnlp.1207; caveat: tema = sesgo por nombres,
   no mitigación por prompting) → **R93**, Chen 2024 (10.18653/v1/2024.emnlp-main.474) → **R94**.
   Confirmadas e incorporadas al corpus con PDF oficial ACL Anthology.
3. ~~Autorizar (o no) las fuentes EXTERNO-PENDIENTE: Kumar et al. + Marzi
   et al. (Krippendorff)~~ — **AUTORIZADAS 2026-09-07**: Kumar et al. **2026**
   (NMI, vol. 8, no. 2, feb. 2026 — se cita 2026, no 2025) → **R95**; Marzi
   et al. 2024 (MethodsX) → **R96**. Siguen EXTERNO-PENDIENTE: ASR kichwa,
   INEC/DIGERCIC + onomástica UPS, LOPDP, Model Cards/Datasheets.
4. Decidir OI-05 (requirements vs runtime), OI-06/OI-07 (limpieza del paquete).
5. Tramitar aprobación ética/consentimiento si la revista lo exige (OI-14).
