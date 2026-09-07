# Data availability

## PUBLIC — included in this repository

| Category | Files |
|---|---|
| Frozen protocol configuration | `config/` (4 files, SHA-256 in `manifests/SHA256SUMS.txt`) |
| Aggregated results / final numbers | `results/02_FINAL_NUMBERS.csv`, `results/04_FINAL_STATISTICAL_RESULTS.csv`, `results/05_FINAL_LANGFAIR_RESULTS.csv`, `results/06_FINAL_JUDGE_RESULTS.csv`, `results/06_FINAL_JUDGE_COST_REPORT.csv`, `results/07_FINAL_TABLES.md`, `results/08_FINAL_FIGURES.md` |
| Human-validation aggregates (no identifiers) | `results/03_FINAL_HUMAN_RESULTS.csv`, `results/human_validation_v2/` (manifest, integrity 180/180, truncation audit) |
| Evidence / pair-level tables | `results/v4_evidence/` (QC, LangFair pair-level, judge calibration, numbers map, reviewer note) |
| Figures (frozen) | `figures/` (4 PNG; hashes in `results/08_FINAL_FIGURES.md`) |
| Scripts (public subset) | `src/human_validation/` (blinded-sample builder, integrity checker) |
| Documentation, provenance, references | `docs/` (source-of-truth, limitations, reproducibility map, audits, reference catalog with DOIs) |
| Manifests / hashes | `manifests/` (`V4_RUN_MANIFEST.json`, `PUBLICATION_MANIFEST.csv`, `SHA256SUMS.txt`) |

## RESTRICTED / NOT PUBLIC — excluded

| Data | Why excluded |
|---|---|
| Evaluator identities; `tokens.csv` (tokens hex64 + names), unmasking map `key.csv`, raw ratings `calificaciones.csv` | Personal data of human raters; breaks blinding; no release authorization (rows H-/E- of `results/02_FINAL_NUMBERS.csv`; `docs/MASTER_PUBLIC_PRIVATE_MAP.csv`) |
| Institutional audio (718 files) and client data (Oracle / FitBank / SATJE / WhatsApp) | Privacy and institutional agreements; scenarios are synthetic and no client data was used in them |
| Credentials: `.env`, API keys, Hostinger credentials, tokens | Security |
| Raw generation/judge ledgers (JSONL) and `V4_ELIGIBLE_RESPONSES.jsonl` | Contain full response texts; policy: only presence/length of `reasoning_content` was recorded, never content; large files referenced by SHA-256 instead (`docs/01_SOURCE_OF_TRUTH.md`) |
| Blinded human-validation texts (`public_items.json`, delivered JSON) | Instrument confidentiality (would not break blinding alone, but kept out of the public package) |
| Scenario table and surname-pair provenance tables | Kept in the private study repository; hashes published so provenance can be verified (`docs/15_PUBLICATION_REPRODUCIBILITY_MAP.md`); the synthetic scenario *design* is described in the documentation and figures |
| Third-party literature PDFs | Copyright: not redistributed. Citations with verified DOI are provided (`docs/10_REFERENCES_VERIFIED_IEEE.md`, `docs/ARTICLE_REFERENCE_CATALOG.csv`) |
| Killkan corpus (audio) | Third-party corpus (CC BY 4.0 TEST subset per the source study's own map); not redistributed — download from the original source; see `docs/MASTER_PUBLIC_PRIVATE_MAP.csv` |
| Model weights / GGUF binaries | Third-party downloads; documented in the source study, not redistributed |
| UISRAEL manuscript (DOCX), signed letters, CRediT forms, journal target notes | Institutional manuscript material, kept separate from the scientific reproducibility package |
| V1/V2/V3, pilots and recovery cohorts | Engineering pre-tests / technical validation, excluded from V4 analysis by design (`manifests/V4_RUN_MANIFEST.json`) |

## Notes

- **Synthetic nature:** the conversational scenarios, customer messages and
  persons in them are synthetic. Surnames are experimental stimuli with
  documented nominal cultural association (frequency provenance INEC,
  administrative register), not claims about any real person's ethnicity.
- **Ethics:** the study itself declares that institutional ethics approval is
  `MISSING` and evaluator consent `NOT_DOCUMENTED` (see
  `docs/14_LIMITATIONS_AND_CLAIMS.md`). Data availability decisions follow the
  study's own public/private map (`docs/MASTER_PUBLIC_PRIVATE_MAP.csv`).
- **Access requests:** inquiries about restricted assets should be directed to
  the study authors through the institutional channels of the associated
  manuscript (no author emails are published in this repository).
- **Hashes of excluded files** are listed in `docs/01_SOURCE_OF_TRUTH.md` and
  `manifests/PUBLICATION_MANIFEST.csv` so the boundary is auditable.
