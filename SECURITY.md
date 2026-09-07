# Security policy

## Scope

This is a **scientific reproducibility package**. It contains no live
credentials, no API keys, no private data and no deployment infrastructure.
See `PUBLIC_REPO_SECURITY_AUDIT.md` (performed before the first commit) and
`manifests/PUBLICATION_MANIFEST.csv`.

## Hard rules for contributors

- Never commit `.env*`, `*.key`, `*.pem`, `tokens.csv`, `key.csv`,
  `calificaciones.csv`, credentials, tokens or any evaluator-identifiable data
  (see `.gitignore`).
- Never commit raw generation/judge ledgers or model `reasoning_content`.
- Never commit institutional audio, database exports or third-party PDFs.
- If a file contains a local machine path, redact it and mark the file
  `DERIVED_PUBLIC` in `manifests/PUBLICATION_MANIFEST.csv` instead of copying
  it verbatim.
- If in doubt whether a file may be published: exclude it.

## Reporting a vulnerability

- Do **not** open a public issue for credentials, private data or personal
  data — delete the file locally, purge it from history if already committed,
  and rotate any affected secret.
- For vulnerabilities in this package's own (minimal) code or a suspected
  accidental disclosure in the repository, open a private report through the
  GitHub repository's **Security → Report a vulnerability** flow, or contact
  the authors through the institutional channels of the associated manuscript.
  This repository does not publish author email addresses.
