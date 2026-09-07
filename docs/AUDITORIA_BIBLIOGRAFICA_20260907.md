# AUDITORÍA BIBLIOGRÁFICA IEEE — corpus de literatura del autor (ruta local omitida en esta release pública)

Fecha: 2026-09-07 · Alcance: verificación de fuentes reales para el manuscrito UISRAEL y paper Q1/Q2 futuro.
El manuscrito (IAA-GRUPO6-ART.docx) NO fue modificado. La numeración IEEE NO fue re-numerada.

## Entregables

| Archivo | Contenido |
|---|---|
| `ARTICLE_REFERENCE_CATALOG.csv` | 103 filas: 103 archivos del corpus (83 originales + 20 incorporados como PDF el 2026-09-07: R84–R103). 21 columnas, referencia IEEE por fila. |
| `CITATION_CLAIM_MATRIX.csv` | 34 afirmaciones del manuscrito con clasificación DIRECT_SUPPORT / PARTIAL_SUPPORT / NO_SUPPORT verificada en texto completo. |
| `tmp/pdfs/audit/chunk_1..6.json` | Evidencia cruda de los 6 agentes verificadores (PDF abierto + Crossref por archivo). |
| `tmp/pdfs/audit/build_catalogs.py`, `build_matrix.py` | Generadores reproducibles. |

## Resumen ejecutivo

- **PDFs examinados:** 83 (82 PDF + 1 DOCX). Cada archivo fue abierto y su metadato leído del propio PDF (nunca del nombre de archivo).
- **Graphify:** indexado el 2026-09-07 (post-auditoría) y re-indexado cinco veces el mismo día al incorporar R84–R103. `graphify-out/` existe con snapshot y manifest (5.ª ejecución): **728 nodos · 943 aristas · 59 comunidades · 25 hiperaristas** sobre las **107 fuentes** del corpus (102 PDF = 87 en la raíz + 15 en `ScienceDirect_*`, más `AUDITORIA_BIBLIOGRAFICA_20260907.md` y `CLAUDE.md` —detect los clasifica como *paper* por señales de contenido—, `promtInicial.md` y R43 convertido). Detalles y alcance en `CLAUDE.md` y `graphify-out/GRAPH_REPORT.md`. El grafo sirve para LOCALIZAR; toda la evidencia bibliográfica de ESTA auditoría viene del PDF + Crossref/DataCite.
- **DOIs validados:** 68 YES (Crossref), 1 YES DataCite (R35), 5 CANDIDATE_ONLY, 4 N/A (sin DOI: CFPB, NBER, editoriales, docx), 5 sin DOI real (arXiv).
- **Clasificación:** CORE 16 (16 con archivo en el corpus: 10 originales + R84–R87 + R88 Kusner y R90 LangFair) · SUPPORTING 42 (28 + R89 Nghiem, R91 G-Eval, R92 An, R93 Pawar, R94 Chen, R95 Kumar, R96 Marzi y R97–R103: Model Cards/Datasheets, LOPDP, Whisper/Killkan y onomástica) · BACKGROUND 29 · REMOVE 14 · NEEDS_VERIFICATION 2.

### CORE (usar como columna vertebral)
R13 Fu et al. ISR 2021 (sesgo en ML de crédito — CORE #1) · R26 Segovia-Vargas (cooperativas Ecuador) · R30 Sivamayilvelan (chatbot cobranza LLM) · R32 CFPB (chatbots en finanzas de consumo) · R40 Kuan et al. PNAS (nudges 13M) · R47 Barboni et al. (repago, Colombia) · R51 Przybyłek (DSR cobranza) · R55 Matz et al. (persuasión genAI) · R58 Vuković (regulación IA financiera) · R82 Carrera-Silva (credit unions LatAm) · R84 de Castro Vieira 2025 (SLR sesgo en crédito) · R85 Mehrabi 2021 (survey sesgo/equidad) · R86 Blodgett 2020 (sesgo NLP) · R87 Barocas & Selbst 2016 (disparate impact). R84–R87: PDFs incorporados al corpus el 2026-09-07 (antes referencias externas aprobadas; archivo de R85 = preprint oficial arXiv:1908.09635v3, texto ACM CSUR tras paywall). Mismo día: R88 Kusner 2017 (equidad contrafáctica, NeurIPS 30; sin DOI Crossref) y R90 LangFair 2025 (versión publicada en JOSS 10(105):7570) — CORE; R89 Nghiem 2024, R91 G-Eval 2023, R92 An 2024, R93 Pawar 2025, R94 Chen 2024, R95 Kumar y R96 Marzi — SUPPORTING. NOTA AÑO: R95 Kumar (Nature Machine Intelligence 8(2):173–185) se cataloga como 2026 — Crossref y portada del PDF imprimen vol. 8, febrero 2026, pese al "025" del DOI. R95/R96 cubren el vacío C-31 (acuerdo interevaluador/Krippendorff). Mismo día (5.º ciclo): R97 Mitchell et al. 2019 (Model Cards, FAT* '19 pp. 220–229 — archivo arXiv:1810.03993v2) y R98 Gebru et al. 2021 (Datasheets for Datasets, CACM 64(12):86–92 — archivo arXiv:1803.09010) cubren C-18; R99 LOPDP (Quinto Suplemento del Registro Oficial No. 459, 26-may-2021; fuente legal exenta de cuartil) cubre C-08/C-17 — NO C-03b (la provisión líquida SEPS 100% es norma prudencial ajena a la LOPDP; sigue pendiente); R100 Radford 2023 (Whisper, ICML/PMLR v202 pp. 28492–28518) y R101 Taguchi et al. 2024 (Killkan, LREC-COLING 2024 pp. 9753–9763) cubren C-22 como contexto — licencias verificadas por separado el 2026-09-07: artículo CC BY-NC 4.0 (ELRA/ICCL), dataset y modelo ctaguchi/killkan CC BY 4.0; R102 Cabrera Moreno 2025 (Universidad Verdad 87, pp. 152–167, DOI 10.33324/uv.vi87.1074) es la fuente PRINCIPAL de C-14 y R103 Gómez Rendón 2016 (Antropología Cuadernos de Investigación 16, pp. 115–129) el respaldo lingüístico histórico (respaldo histórico/excepción autorizada 2026-09-07: ene.–jun. 2016 queda fuera de la ventana estricta de 10 años; R102 es la fuente PRINCIPAL y R103 no la sustituye).

**Congelamiento (provenance):** la bibliografía estuvo cerrada en R96; **R97–R103 son una excepción autorizada posterior al cierre** (2026-09-07) incorporada exclusivamente para resolver gaps concretos — C-18 (R97/R98), C-08/C-17 (R99), C-22 como contexto (R100/R101), C-14 (R102/R103) — y NO formaban parte del corpus inicial. `BIBLIOGRAPHY_FREEZE_V2 = R01–R103` quedó **APROBADO y ACTIVO el 2026-09-07** por el autor (PASS del PRE-FREEZE AUDIT REPORT y del FINAL FREEZE CHECK, `tmp/recovery/`); desde entonces no se agregan fuentes sin gap + autorización.

### Descartadas (REMOVE, 14)
R09 CIRP (predictive maintenance) · R46 duplicado exacto de R40 · R65/R66/R68 (bycatch JBEF) · R69/R77 (páginas de comité editorial) · R71–R75 (dump JBEF off-topic) · R76 (corrigendum EJOR) · R78 (optimización minera).

### NEEDS_VERIFICATION (2)
R23 Journal of Ecohumanism (alerta de editorial depredadora) · R43 docx de nudging NPL (identidad candidata: Saulitis, JBEF 37:100776, 2023; el archivo no imprime autores).

## Problemas detectados y corregidos

1. **Duplicado:** R40 = R46 (Kuan et al. PNAS, mismo DOI). Citar solo R40.
2. **DOIs incorrectos del inventario previo (descartados):** R05 (10.1257/rct = prerregistros AEA, no el artículo), R16 (DOI de Computers in Human Behavior 2000), R18 (DOI de paper ESG), R19 (DOI de RecMind), R32 (DOI MDPI ajeno al CFPB), R34 (DOI IEEE ajeno), R38/R39 (DOIs truncados), R79 (DOI truncado), R80 (SSRN ajeno), R14 (placeholder ACM).
3. **Revistas mal nombradas en el manuscrito:** [9]/[13] “Springer Nature” → Humanities and Social Sciences Communications; [2] “MDPI” → Sustainability.
4. **Años incorrectos en el manuscrito:** [4] “dic. 2026” → ene. 2026 (Crossref 2026-01-11); [5] “dic. 2025” → jul. 2025; [11] “may 2024” → jun. 2024 (IMWUT 8(2) Art. 73). En el corpus: R45 (2022, no 2017), R09 (2023, no 2022), R79 (citar 2021), R31 (2023, no 2022), R04 (2024, no 2023).
5. **Citas que NO respaldan su afirmación (CITATION_CLAIM_MATRIX):**
   - **C-07 (crítico):** “los algoritmos codifican/perpetúan/amplifican sesgos” citaba [5][7][10] (sistema DSR, taxonomía agéntica, survey agéntico) → los tres NO_SUPPORT. Reemplazos aprobados: R84 Vieira, R85 Mehrabi, backup R13/R55/R86.
   - **C-09:** “el sesgo deriva en tono y opciones de negociación” citaba [9][11] (confianza general + salud) → NO_SUPPORT. Reemplazo: V4[13] An et al. (no duplicar) + R86.
   - **C-03b:** la provisión SEPS 100% citaba [3] (Naili) → 0 menciones de SEPS/Ecuador en el texto completo → NO_SUPPORT. Reemplazo: resolución normativa SEPS.
   - **C-05:** [6] Aldboush citado para “oportunidad de automatizar” → NO_SUPPORT (su texto es ética/privacidad). Reasignar a C-06/C-11/C-17.
   - **Sin cita (NO_SUPPORT por omisión):** Counterfactual Fairness (C-12 → V4[12] Kusner), LangFair (C-16 → V4[16]), DeepEval/G-Eval (C-15 → V4[17]), prompting frágil (C-20 → V4[15]), sesgo de representación/narrativo (C-23/C-24 → R86), impacto dispar (C-25 → R87), validez estructural (C-26 → R51/R30), concentración anglo (C-27 → R86), Model Cards/Datasheets (C-18 → R97/R98).
6. **Regla de apellidos (provenance separado):** FRECUENCIA → INEC/DIGERCIC (administrativa web, citada sin PDF); ASOCIACIÓN CULTURAL/ONOMÁSTICA → investigación académica (R102 Cabrera Moreno 2025 — principal; R103 Gómez Rendón 2016 — respaldo lingüístico). Nunca mezclar INEC con onomástica ni usar apellidos/frecuencia como prueba de etnia (C-14, reformulado 2026-09-07): los pares del manuscrito son señal nominal cultural/lingüística, estímulos sintéticos contrafactuales. Tesis UPS Saquisilí (may-2010) descartada por quedar fuera de la ventana de 10 años.
7. **R86 (Blodgett et al.):** el inventario previo listaba 3 autores; el PDF impreso y Crossref imprimen **4 (Hanna Wallach, 4.ª autora)**. Corregido en el catálogo (2026-09-07). Proveniencia de archivos nuevos: R84 PDF oficial MDPI (CC BY 4.0), R85 arXiv:1908.09635v3 (ACM CSUR tras paywall), R86 PDF oficial ACL Anthology, R87 texto final California Law Review vía archivo web de la revista (CC BY-SA).

## Vacíos bibliográficos que requieren búsqueda externa

| Tema | Estado |
|---|---|
| Counterfactual fairness (Kusner), LangFair, G-Eval, LLM-as-judge, name-bias (An), prompt-mitigation (Pawar) | Kusner/LangFair/G-Eval/Nghiem → R88–R91; An 2024 / Pawar 2025 / Chen 2024 → R92–R94 (PDFs en el corpus desde 2026-09-07). No duplicar. |
| Mehrabi 2021, Blodgett 2020, de Castro Vieira 2025, Barocas & Selbst 2016 | R84–R87: PDFs en el corpus desde 2026-09-07 (ver catálogo; archivo R85 = arXiv v3, DOI de cita ACM). |
| Krippendorff / acuerdo interevaluador (C-31) | R95 Kumar et al. (Nature Machine Intelligence 8(2):173–185, 2026, DOI 10.1038/s42256-025-01169-6) y R96 Marzi et al. (MethodsX 12:102545, 2024, K-Alpha Calculator, DOI 10.1016/j.mex.2023.102545): PDFs incorporados al corpus el 2026-09-07. |
| ASR kichwa / lenguas de bajos recursos | R100 Radford 2023 (Whisper, ICML PMLR v202) y R101 Taguchi et al. 2024 (Killkan, LREC-COLING 2024, pp. 9753–9763): PDFs incorporados al corpus el 2026-09-07. No duplicar. |
| INEC/DIGERCIC (frecuencia de apellidos) + onomástica académica UPS | Fuentes SEPARADAS (regla 6): INEC/DIGERCIC = administrativa web, citada sin PDF. Onomástica: R102 Cabrera Moreno 2025 (principal, PDF 2026-09-07) + R103 Gómez Rendón 2016 (respaldo histórico). Tesis UPS Saquisilí (may-2010) descartada: fuera de la ventana de 10 años. |
| Texto de la LOPDP (sanciones 1%) | R99 LOPDP, Quinto Suplemento del Registro Oficial No. 459 (26-may-2021): PDF oficial (repositorio gob.ec) incorporado el 2026-09-07. Cubre C-08/C-17; no C-03b. |
| Model Cards (Mitchell 2019) / Datasheets (Gebru 2021) | R97/R98: PDFs incorporados al corpus el 2026-09-07 (C-18). No duplicar. |

## Matriz de citas — conteo de clasificación

DIRECT_SUPPORT 4 · PARTIAL_SUPPORT 4 · NO_SUPPORT 20 · EXPERIMENTAL/PROPIA 5 · AUDITORÍA 1 (34 filas).

## Reglas aplicadas

- Nunca inferir metadatos desde nombres de archivo (todo leído del PDF impreso o de Crossref/DataCite).
- Un nodo Graphify nunca es evidencia bibliográfica final.
- No copiar párrafos de los artículos; la redacción es síntesis propia.
- Numeración IEEE final = orden de primera aparición tras cerrar la redacción (no re-numerar todavía).
