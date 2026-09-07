# Public repository security audit

- **Repository:** `sfps-llm-counterfactual-audit` (reproducibility package, UISRAEL V4 study)
- **Audit date:** 2026-09-07
- **Scope:** full working tree **before** `git init` (no file was ever in git history)
- **Method:** file-name inventory + content pattern scans (regex) over all text
  and binary files; targeted context inspection of every residual hit;
  verbatim-integrity check (SHA-256) of every copied file against its source.
- **Result:** **PASS** — 0 BLOCKER.

## Checks

| # | Check (spec §8) | Finding | Verdict |
|---|---|---|---|
| 1 | File names / hidden files | 58 files inventoried at audit time; only dotfile is `.gitignore`; no `.env`, `*.key`, `*.pem`, logs, caches, archives | PASS |
| 2 | High-value secret patterns (`sk-…`, `AIza…`, `gh*_…`, `github_pat_`, `AKIA…`, `xox…`, `-----BEGIN … PRIVATE KEY-----`, JWT, `Bearer <value>`, credentials in URLs) | **0 matches** in the whole tree | PASS |
| 3 | Word-level denylist (`api_key`, `token`, `password`, `secret`, `bearer`, `authorization`, `private_key`, provider names) | Occurrences are all descriptive: environment-variable **names** in frozen configs (`api_env: GOOGLE_API_KEY`), token **counts** in judge CSVs (`judge_input_tokens`…), protocol policy text, and exclusion documentation. No value material | PASS |
| 4 | Emails / evaluator identifiers | No evaluator names or emails. One **third-party** academic email in a bibliographic-audit note (`docs/ARTICLE_REFERENCE_CATALOG.csv`, row R80) → **redacted** (documented; file now `DERIVED_PUBLIC`). Remaining `@` matches are binary noise inside PNG compression | PASS |
| 5 | IP addresses | No true IP addresses (private or public). Regex candidates were DOI prefixes (`10.1038/…`, `10.18653/…`) and the Windows build string `10.0.26100` — verified false positives | PASS |
| 6 | Internal machine paths | Zero occurrences of drive-letter paths, `/Users/`, `/home/`, the product repository name or local corpus names after 4 documented redactions (`docs/01_SOURCE_OF_TRUTH.md`, `docs/10_REFERENCES_VERIFIED_IEEE.md`, `docs/AUDITORIA_BIBLIOGRAFICA_20260907.md`, `manifests/V4_RUN_MANIFEST.json`) plus the R80 note (see #4) | PASS |
| 7 | `reasoning_content` / chain-of-thought | Only protocol-policy sentences ("reasoning_content is NEVER persisted as content"), `.gitignore` guards, and bibliographic metadata about the G-Eval paper. No reasoning content anywhere | PASS |
| 8 | Private infrastructure references (hostinger, whatsapp, anthropic, elevenlabs) | Only as documentation of **excluded** categories (`.gitignore`, `DATA_AVAILABILITY.md`, `README.md`, `docs/MASTER_PUBLIC_PRIVATE_MAP.csv`) | PASS |
| 9 | Evaluator-related identifiers (`EVALUADOR_NN`, `rater_id`, …) | Only pseudonymization-policy descriptions (rows E-04/E-05) and the public/private map. No `tokens.csv`/`key.csv`/`calificaciones.csv` content | PASS |
| 10 | Verbatim integrity of copies | All 41 verbatim copies are byte-identical to their sources (SHA-256 equal, including the 4 frozen figures vs. their recorded hashes in `results/08_FINAL_FIGURES.md`); all JSON files parse; both YAML configs parse | PASS |
| 11 | Repository hygiene guards | `.gitignore` blocks `.env*`, `*.key`, `*.pem`, `tokens.csv`, `key.csv`, `calificaciones.csv`, ledgers, `reasoning_content*`, `*.gguf`, `*.wav`, institutional data; `SECURITY.md` states hard rules | PASS |

## Files classified DERIVED_PUBLIC (single, documented redaction each)

| File | Redaction |
|---|---|
| `manifests/V4_RUN_MANIFEST.json` | `final_folder` absolute machine path → explanatory placeholder |
| `docs/01_SOURCE_OF_TRUTH.md` | absolute local corpus path in provenance table → placeholder |
| `docs/10_REFERENCES_VERIFIED_IEEE.md` | absolute local corpus path → "local corpus" text |
| `docs/AUDITORIA_BIBLIOGRAFICA_20260907.md` | machine path in title → text without path |
| `docs/ARTICLE_REFERENCE_CATALOG.csv` | third-party email in row R80 notes → verification note without email |

Every redaction is registered in `manifests/PUBLICATION_MANIFEST.csv`
(`source_sha256` = original; `public_sha256` = shipped file).

## Excluded content (never copied; see `manifests/PUBLICATION_MANIFEST.csv`)

Evaluator identities and raw ratings (`tokens.csv`, `key.csv`,
`calificaciones.csv`), `.env`/API keys, institutional audio and client data,
raw generation/judge ledgers, blinded human-validation texts, the manuscript
DOCX and institutional manuscript working documents, full third-party PDFs,
the Killkan corpus, GGUF weights, and the operational deployment scripts.

## Conclusion

**PASS — the repository is clear for `git init` and push (private first).**
No BLOCKER was found. If a file is later added, the checks above (especially
§7 of the spec denylist) must be re-run before any visibility change.
