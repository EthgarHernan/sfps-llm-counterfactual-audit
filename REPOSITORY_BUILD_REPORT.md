# REPOSITORY_BUILD_REPORT — sfps-llm-counterfactual-audit

Construcción clean-room del paquete de reproducibilidad del estudio UISRAEL
Grupo 6 (corrida confirmatoria V4). Fecha del informe: **2026-09-07**.

> **Alcance de este informe:** documenta la **construcción inicial** del
> paquete. El commit `d95c58a…` referido abajo es el commit raíz/inicial de
> esa construcción, y este informe no pretende registrar el SHA del HEAD de
> cada corrección documental posterior (terminología, metadatos de citación,
> etc.). El **estado vigente** del repositorio debe consultarse en la rama
> `main` del repositorio público.

## Estado — construcción inicial

| Campo | Valor |
|---|---|
| Ruta local | `C:\Libreria\fuentes\codex\sfps-llm-counterfactual-audit` |
| Archivos versionados | **62** (commit raíz `d95c58a`) |
| Tamaño total (árbol público, sin `.git`) | 4 052 338 bytes (~3.86 MB) |
| Rama | `main` |
| Commit de construcción inicial | `d95c58a98a2a827f39e5c967c383cc800a801802` — "Initial reproducibility package for UISRAEL V4 study" |
| Autor del commit (identidad git local del equipo) | Ethgart `<ethgart@hotmail.com>` — usar identidad diferente si el autor lo prefiere (amend antes de difundir) |
| `git status` | limpio (0 cambios) |
| URL remota | https://github.com/EthgarHernan/sfps-llm-counterfactual-audit |
| Remoto creado | `gh repo create` (2026-09-07), PRIVATE durante la auditoría |
| Visibilidad actual | **PUBLIC** (cambio explícito autorizado por el autor tras PASS, 2026-09-07) |
| Push realizado | **SÍ** — push del commit de construcción inicial (2026-09-07). Para el estado vigente: consultar la rama `main` del repositorio público |

## Seguridad

`PUBLIC_REPO_SECURITY_AUDIT.md` = **PASS, 0 BLOCKER**.

- Secretos encontrados: **0** (patrones de alto valor: claves API, tokens GitHub,
  PEM, JWT, Bearer, credenciales en URLs → 0 coincidencias).
- Hallazgos corregidos antes del commit (todos documentados como
  `DERIVED_PUBLIC` en `manifests/PUBLICATION_MANIFEST.csv`):
  1. Rutas internas de máquina en 4 archivos copiados (redactadas);
  2. Un email de terceros en una nota bibliográfica (`docs/ARTICLE_REFERENCE_CATALOG.csv`,
     fila R80 — redactado).
- Emails de evaluadores, IPs privadas, `reasoning_content` persistido,
  `chain-of-thought`: 0 en el árbol público.
- Fidelidad byte-a-byte verificada: los 62 blobs de git son idénticos a los
  bytes en disco (`.gitattributes` con `* -text`); `manifests/SHA256SUMS.txt`
  (61 entradas) verifica el paquete tal como GitHub lo sirve.

## Excluido del repositorio público

Listado íntegro con motivo en `manifests/PUBLICATION_MANIFEST.csv` (16 filas
`EXCLUDED_*`). Resumen:

- **Privacidad** (`EXCLUDED_PRIVATE`): identidades de evaluadores, `tokens.csv`,
  `key.csv`, `calificaciones.csv`, textos crudos de ledgers, audios y datos
  institucionales de clientes, material del manuscrito UISRAEL (DOCX y
  documentos de trabajo), herramientas operativas de despliegue.
- **Seguridad** (`EXCLUDED_SECURITY`): `.env`/claves reales (solo nombres de
  variables de entorno en configs), cualquier `reasoning_content` persistido.
- **Copyright** (`EXCLUDED_COPYRIGHT`): 13 PDFs de papers de terceros
  (metadatos con DOI incluidos), corpus Killkan, pesos GGUF.

## Hashes y manifest

- `manifests/PUBLICATION_MANIFEST.csv` — 77 filas (60 PUBLIC + 5
  DERIVED_PUBLIC + 11 EXCLUDED_PRIVATE + 3 EXCLUDED_COPYRIGHT +
  2 EXCLUDED_SECURITY + nota de alcance); `public_sha256` y `source_sha256`
  por archivo.
- `manifests/SHA256SUMS.txt` — 61 entradas, calculadas 2026-09-07, formato
  `sha256sum` (LF estricto).
- Hashes de referencia verificados contra los registros congelados del
  estudio: config V4 `87bfbd97…`, juez `c03f6827…`, figuras 1–4 (iguales a
  `results/08_FINAL_FIGURES.md`), QC `b4501da0…`/`45c11eaa…`, estabilidad C
  `62275410…`, manifest humano `d10038db…`.

## Copias verbatim vs derivadas

- 41 copias verbatim byte-idénticas a la fuente (source_sha256 == public_sha256).
- 5 archivos `DERIVED_PUBLIC` con una única redacción documentada (ver
  `PUBLIC_REPO_SECURITY_AUDIT.md`, sección "Files classified DERIVED_PUBLIC").

## Reproducibilidad

`REPRODUCIBILITY.md` separa **REPRODUCE_ANALYSIS** (offline, sin costo, sin
APIs — comandos incluidos) de **RE-RUN_GENERATION** (requiere claves,
presupuesto y activos no públicos listados con hash). No se re-ejecutó ninguna
API para construir este paquete. Entorno real ejecutado pinneado en
`requirements-reproduction.txt` (discrepancia con el `requirements.txt`
histórico documentada en `docs/14_LIMITATIONS_AND_CLAIMS.md`, R-02…R-04).

## Pendientes del autor (no ejecutados por diseño)

- Agregar colaboradores cuando existan usernames/emails verificados
  (`COLLABORATOR_SETUP.md`; nadie ha sido invitado).
- Verificar doble ciego antes de sumitir a revista y decidir anexo
  anonimizado (`docs/JOURNAL_SUBMISSION_NOTE.md`).
- Conectar Zenodo y crear Release para DOI inmutable; actualizar `CITATION.cff`
  (preparado; sin DOI inventado).
- Si se desea otra identidad git para el commit, hacer amend/push antes de
  difundir la URL.
