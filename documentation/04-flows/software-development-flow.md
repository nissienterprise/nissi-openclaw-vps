<div align="center">

# ⚙️ Flujo: Desarrollo de Software Automatizado
### Las 6 Fases — De Brief a Entrega

</div>

```mermaid
flowchart TD
    F1["📥 FASE 1: INTAKE\nSamantha recibe brief → EVA califica → David crea proyecto\nPresupuesto automático (QuickBooks draft) → Aprobación cliente + Michael"]
    F2["📋 FASE 2: PLANIFICACIÓN\nDavid: Épicas · Historias · Tareas en Jira (NTE-SW)\nTimeline · Repositorio GitHub · Asignación de agentes\nHitos en NTE-Calendar"]
    F3["🏗️ FASE 3: ARQUITECTURA\nBishop + Sonny: Diseño técnico · CASE: Schema de BD\nT-800: Risk review inicial de seguridad"]
    F4["💻 FASE 4: DESARROLLO ITERATIVO\nSprints semanales · Bishop + Sonny + BB-8 en paralelo\nCI/CD automático (Optimus) · QA en cada PR (AVA)\nReporte al cliente cada viernes via David"]
    F5["🔍 FASE 5: REVISIÓN & QA\nAVA: Reporte completo post-sprint en Jira\nT-800: Scan de seguridad pre-release\nBugs asignados de vuelta al agente correspondiente"]
    F6["🚀 FASE 6: DEPLOYMENT & ENTREGA\nOptimus: Deploy a producción (con aprobación Michael)\nMarvin: Documentación final en Confluence\nDavid: Cierre del proyecto en Jira + solicitud de testimonio"]

    F1 --> F2 --> F3 --> F4 --> F5
    F5 -->|"Bugs críticos"| F4
    F5 -->|"QA ✅"| F6
    F6 -->|"Nuevo proyecto"| F1

    style F1 fill:#1a1a2e,color:#fff
    style F2 fill:#1a2c1a,color:#fff
    style F3 fill:#2c1a1a,color:#fff
    style F4 fill:#1a1a2e,color:#fff
    style F5 fill:#2c1654,color:#fff
    style F6 fill:#1a3a1a,color:#fff
```

## Roles por Fase

| Fase | Agentes Activos | Output |
|---|---|---|
| 1. Intake | Samantha (NTE-CX) · EVA (NTE-LEAD-INTAKE) · David (NTE-PM) | Brief estructurado + QuickBooks estimado aprobado |
| 2. Planificación | David (NTE-PM) | Jira board (NTE-SW) + repo GitHub + NTE-Calendar |
| 3. Arquitectura | David · Bishop · Sonny · T-800 | Documento de arquitectura técnica |
| 4. Desarrollo | Bishop · Sonny · BB-8 · CASE · AVA · Optimus | Código + CI/CD pipeline funcionando |
| 5. QA & Revisión | AVA (NTE-QA) · T-800 (NTE-SECURITY) | Reporte de bugs en Jira + security clearance |
| 6. Entrega | Optimus · Marvin · David | App en producción + documentación en Confluence |

---

## SCRUM: Detalle del Proceso

La Fase 4 (Desarrollo Iterativo) opera bajo **sprints semanales** con Jira (proyecto `NTE-SW`).

Consulta el documento completo del proceso SCRUM:

**[→ Workflow SCRUM Detallado: Ceremonias · Jira · Branches · Definition of Done](./flujo-scrum-detallado.md)**

Incluye:
- Sprint Planning, Daily Standup, Sprint Review, Retrospectiva
- Columnas del board Jira y lifecycle de tickets
- Convención de branches y commits (Conventional Commits)
- Definition of Done completo
- Gestión de hotfixes en producción
- KPIs del proceso ágil

[← Todos los flujos](./README.md)
