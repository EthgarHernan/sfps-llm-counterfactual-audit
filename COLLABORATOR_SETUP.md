# Collaborator setup (pendiente — no se ha invitado a nadie)

El repositorio se creó con el propietario **Edgar Hernan Changoluisa Lasluisa**
(cuenta GitHub `EthgarHernan`). Los coautores deben agregarse como
**colaboradores** cuando el autor proporcione sus identificadores verificados:

- **Changoluisa Lasluisa María Belén** — username/email GitHub pendiente
- **Alemán Gualpa Pablo David** — username/email GitHub pendiente

> Decisión 2026-09-07: **no se ha invitado a ningún colaborador** porque no hay
> usernames ni emails verificados. No inventar identificadores. Si el repositorio
> se hace público antes de agregarlos, cualquier persona puede contribuir vía
> issues/PRs mientras tanto.

## Cómo agregar un colaborador (cuando se tengan los datos)

Opción A — interfaz web (recomendado):

1. GitHub → repositorio `sfps-llm-counterfactual-audit` → **Settings → Collaborators**.
2. Invitar por username o email.
3. El invitado acepta la invitación por correo.

Opción B — GitHub CLI:

```powershell
gh api repos/EthgarHernan/sfps-llm-counterfactual-audit/collaborators/USERNAME -X PUT
```

Reemplazar `USERNAME` por el username real del coautor (es un permiso de
escritura directo; solo otorgar a cuentas verificadas de los coautores).

## Alternativa más segura

Si el repositorio será público y se prefiere flujo de revisión, los coautores
pueden contribuir vía **pull requests** sin permiso de escritura, y el
propietario puede otorgar rol *Maintain* vía **Settings → Collaborators** o
*Teams* cuando corresponda.

## Recordatorios

- Antes de cualquier invitación: confirmar que el GitHub username pertenece al
  coautor (pedir confirmación cruzada; no invitar por correo no verificado).
- No usar cuentas organizacionales compartidas para autoría científica.
- Si se prepara la sumisión a revista doble ciego, revisar
  `docs/JOURNAL_SUBMISSION_NOTE.md` antes de publicar el repositorio.
