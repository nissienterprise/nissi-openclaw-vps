<div align="center">

# 🗂️ NTE-PM — Project Manager Agent

![Model](https://img.shields.io/badge/Model-Claude_Opus_4-ff6b35?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)

*The conductor of development. Turns briefs into delivered projects.*

</div>

## 🎯 Responsibilities

NTE-PM is the brain of the Software R&D Wing. Receives client projects, breaks them down into executable tasks, and coordinates the team of 8 developer agents.

## 🔄 Project Lifecycle

```mermaid
flowchart TD
    A["📥 Client Brief"] --> B["📋 Requirements Analysis\nNTE-PM · Opus 4"]
    B --> C["💰 Automatic Quote\nbased on NTE catalog"]
    C --> D{"✅ Client Approves?"}
    D -->|Yes| E["🗓️ Planning\nJira · GitHub Projects"]
    D -->|No| F["🔄 Negotiation via NTE-CX"]
    E --> G["⚙️ Task Assignment\nto the agent team"]
    G --> H["🔁 Weekly Sprint"]
    H --> I["🔍 QA Review (NTE-QA)"]
    I --> J["🚀 Deployment (NTE-DEVOPS)"]
    J --> K["📝 Docs (NTE-DOCS)"]
    K --> L["✅ Delivery to Client"]
```

## 🛠️ Tools

- **Jira / Linear** — Tracking of epics, stories, and tasks
- **GitHub Projects** — Kanban integrated with the code
- **Slack** — Communication with Michael and client reporting
- **Google Calendar** — Timeline and milestones

> **Why Opus 4?** Breaking down ambiguous requirements, detecting dependencies, and maintaining decision coherence over weeks requires the long-horizon reasoning that only Opus delivers consistently.

[← All agents](../README.md)
