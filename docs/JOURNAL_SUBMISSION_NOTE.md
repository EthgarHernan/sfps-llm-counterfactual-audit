# Nota de sumisión a revista — anonimato y archivo

**Estado (2026-09-07):** el repositorio público conserva la autoría real de los
tres autores. Esta nota describe qué verificar antes de una futura sumisión.

## 1. Doble ciego

Antes de sumitir a cualquier revista, verificar sus normas de revisión:

- Si la revista usa **evaluación doble ciego (double-blind)**, un repositorio
  público con los nombres de los autores puede revelar la identidad. Opciones:
  1. **Anexo anonimizado para revisión:** crear un archivo/rama o un release
     separado con la autoría removida (p. ej. reemplazar la sección de autores
     de `CITATION.cff`, quitar nombres del `README` y del `LICENSE`) **solo** para
     el periodo de revisión, manteniendo intacta la versión pública con autoría.
  2. No enlazar el repositorio desde el manuscrito anónimo; usar el anexo
     anonimizado y restaurar los enlaces al aceptarse.
- Si la revista **no** exige doble ciego (preprint/archivo), el repositorio
  público con autoría es el apropiado.

**No modificar hoy la autoría del repositorio** — se hará solo si la revista
elegida lo exige y el autor lo autoriza.

## 2. URL estable

La URL `https://github.com/EthgarHernan/sfps-llm-counterfactual-audit` debe
permanecer estable (no renombrar el repositorio). Si se cambia la visibilidad
de private a public, la URL no cambia.

## 3. Archivo con DOI (Zenodo)

Pasos previstos (requieren autorización expresa del autor; **no ejecutados**):

1. Conectar el repositorio a Zenodo (GitHub App).
2. Crear una **Release** etiquetada (p. ej. `v0.1.0` o `v1.0.0`).
3. Zenodo emite un DOI inmutable para esa versión.
4. Actualizar `CITATION.cff` (campo DOI / `preferred-citation`) y el
   `README.md` con el DOI.
5. Citar la versión archivada (DOI) en el artículo.

## 4. Checklist previo a sumisión

- [ ] Verificar norma de doble ciego de la revista objetivo.
- [ ] Si aplica, crear anexo anonimizado y revisar `CITATION.cff`, `README.md`,
      `LICENSE`, `LICENSE-DATA`, `COLLABORATOR_SETUP.md`.
- [ ] Confirmar `PUBLIC_REPO_SECURITY_AUDIT.md = PASS` antes de que el
      repositorio sea público.
- [ ] Confirmar estado ético declarado en el manuscrito (aprobación/consentimiento
      `MISSING`/`NOT_DOCUMENTED`, filas E-01/E-02) — la revista puede exigirlo.
- [ ] Decidir con el autor si los pares de apellidos y la tabla de escenarios
      sintéticos deben liberarse (hoy documentados por hash únicamente).
- [ ] Asignar DOI en Zenodo y actualizar `CITATION.cff` antes de citar la
      versión archivada.
