<div align="center">

# 🗂️ NTE-PM — Project Manager Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Opus_4-ff6b35?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)

*El director de orquesta del desarrollo. Convierte briefs en proyectos entregados.*

</div>

## 🎯 Responsabilidades

NTE-PM es el cerebro del Wing Software R&D. Recibe proyectos de clientes, los descompone en tareas ejecutables y coordina al equipo de 8 agentes desarrolladores.

## 🔄 Ciclo de Vida de un Proyecto

```mermaid
flowchart TD
    A["📥 Brief del Cliente"] --> B["📋 Análisis de Requisitos\nNTE-PM · Opus 4"]
    B --> C["💰 Presupuesto Automático\nbasado en catálogo NTE"]
    C --> D{"✅ Cliente Aprueba?"}
    D -->|Sí| E["🗓️ Planificación\nJira · GitHub Projects"]
    D -->|No| F["🔄 Negociación via NTE-CX"]
    E --> G["⚙️ Asignación de Tareas\nal equipo de agentes"]
    G --> H["🔁 Sprint Semanal"]
    H --> I["🔍 QA Review (NTE-QA)"]
    I --> J["🚀 Deployment (NTE-DEVOPS)"]
    J --> K["📝 Docs (NTE-DOCS)"]
    K --> L["✅ Entrega al Cliente"]
```

## 🛠️ Herramientas

- **Jira / Linear** — Tracking de épicas, historias y tareas
- **GitHub Projects** — Kanban integrado con el código
- **Slack** — Comunicación con Michael y reporte al cliente
- **Google Calendar** — Timeline y milestones

> **¿Por qué Opus 4?** Descomponer requisitos ambiguos, detectar dependencias y mantener coherencia en decisiones a lo largo de semanas requiere el razonamiento de largo horizonte que solo Opus proporciona con consistencia.

[← Todos los agentes](../README.md)
