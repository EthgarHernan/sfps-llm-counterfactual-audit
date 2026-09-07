# data/synthetic/ — intentionally empty (explained)

This directory exists to mark the place where the **synthetic scenario table**
and the **surname-pair provenance table** would live in a full data release.

They are **not** included in this public package:

| Table | Original file (private study repository) | SHA-256 |
|---|---|---|
| 40 synthetic scenarios (V3-derived, frozen for V4) | `publication-repository/data/derived/scenarios_v3.csv` | `020f6b569d061b75d956325c2caec9eabf69c7ecc8e04f39a5a66c4b0ec9804b` |
| Surname-pair provenance (INEC + cultural-association sources) | `publication-repository/data/derived/surname_pair_provenance_v3.csv` | `fe4ecd6eb419526c8469aedddd65c75a4a3ec446a408483962bba2deb1b36e5a` |

Why: those files remain in the authors' private study repository. Their
hashes are published so that provenance is auditable. What is public instead:

- the synthetic **design** (40 scenarios, 3 pairs, 2 arms + masked control) in
  `README.md` and `results/07_FINAL_TABLES.md`;
- the **per-scenario results** (IDs `S001`–`S040` are the study keys used in
  `results/06_FINAL_JUDGE_RESULTS.csv`, `results/04_FINAL_STATISTICAL_RESULTS.csv`
  and `results/v4_evidence/langfair_pairs.csv`);
- the reviewer note on masking, `results/v4_evidence/REVIEWER_NOTE_20260906_GENERO_ENMASCARAMIENTO.md`.

If the authors later release the scenario tables under an embargo lift or a
data-availability statement, they can be added to this directory with the
corresponding manifest update in `manifests/PUBLICATION_MANIFEST.csv`.
