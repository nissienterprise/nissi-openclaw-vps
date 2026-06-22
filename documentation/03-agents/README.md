<div align="center">

# 🤖 Ecosistema de Agentes OpenClaw — NTE
### Los 19 Agentes de Nissi Technology Enterprises

</div>

---

## Arquitectura General

```mermaid
flowchart TD
    MICHAEL["👤 Michael Rodriguez — CEO/COO"]

    subgraph SLACK["💬 Slack — Hub de Comunicación"]
        CH["#nte-main · #nte-alerts · #nte-reports · #nte-dev · #nte-content · #nte-cx · #nte-leads"]
    end

    subgraph VPS["🖥️ VPS Ubuntu 22.04 — OpenClaw"]
        MAIN["🧠 JARVIS (NTE-MAIN) · Opus 4\nMain Orchestrator\n[Sin Sandbox — Full FS]\njarvis@nissienterprise.com"]

        subgraph ADMIN["📋 WING ADMINISTRATIVA"]
            CX["🎧 Samantha (NTE-CX)\nSonnet 4 · Docker\nsamantha@nissienterprise.com"]
            CONTENT["✍️ WALL-E (NTE-CONTENT)\nSonnet 4 · Docker\nwalle@nissienterprise.com"]
            ANALYTICS["📊 HAL (NTE-ANALYTICS)\nHaiku 4 · Docker\nhal@nissienterprise.com"]
        end

        subgraph BLOG["📝 BLOG AUTOMATION"]
            TS["🔍 Johnny 5 (NTE-TREND-SCOUT)\nSonnet 4 · Docker\njohnny5@nissienterprise.com"]
            CW["✍️ C-3PO (NTE-COPYWRITER)\nSonnet 4 · Docker\nc3po@nissienterprise.com"]
            PUB["🚀 R2-D2 (NTE-PUBLISHER)\nHaiku 4 · Docker\nr2d2@nissienterprise.com"]
            PROP["📡 Baymax (NTE-PROPAGATOR)\nSonnet 4 · Docker\nbaymax@nissienterprise.com"]
        end

        subgraph LEADS["🎯 LEAD MANAGEMENT"]
            LI["📥 EVA (NTE-LEAD-INTAKE)\nSonnet 4 · Docker\neva@nissienterprise.com"]
            LN["🌱 TARS (NTE-LEAD-NURTURE)\nSonnet 4 · Docker\ntars@nissienterprise.com"]
        end

        subgraph DEV["⚙️ WING SOFTWARE R&D"]
            PM["🗂️ David (NTE-PM)\nOpus 4 · Docker\ndavid@nissienterprise.com"]
            BACKEND["⚙️ Bishop (NTE-BACKEND)\nSonnet 4 · Docker\nbishop@nissienterprise.com"]
            FRONTEND["🎨 Sonny (NTE-FRONTEND)\nSonnet 4 · Docker\nsonny@nissienterprise.com"]
            MOBILE["📱 BB-8 (NTE-MOBILE)\nSonnet 4 · Docker\nbb8@nissienterprise.com"]
            DATA["🗄️ CASE (NTE-DATA)\nSonnet 4 · Docker\ncase@nissienterprise.com"]
            QA["🔍 AVA (NTE-QA)\nSonnet 4 · Docker\nava@nissienterprise.com"]
            DEVOPS["🖥️ Optimus (NTE-DEVOPS)\nSonnet 4 · Docker\noptimus@nissienterprise.com"]
            SECURITY["🔐 T-800 (NTE-SECURITY)\nOpus 4 · Docker\nt800@nissienterprise.com"]
            DOCS["📝 Marvin (NTE-DOCS)\nHaiku 4 · Docker\nmarvin@nissienterprise.com"]
        end
    end

    MICHAEL <-->|"Approvals & Commands"| SLACK
    SLACK <-->|"Alerts & Reports"| MAIN
    MAIN --> ADMIN & BLOG & LEADS & DEV
    PM --> BACKEND & FRONTEND & MOBILE & DATA & QA & DEVOPS & SECURITY & DOCS
    BACKEND <-->|"Inter-agent"| QA
    FRONTEND <-->|"Inter-agent"| QA
    MOBILE <-->|"Inter-agent"| QA
    QA <-->|"Inter-agent"| DEVOPS
    CX -.->|"Nuevo proyecto detectado"| LI
    LI -.->|"Lead calificado"| PM
    TS --> CW --> PUB --> PROP
    ANALYTICS -.->|"KPIs"| MAIN

    style MAIN fill:#1a1a2e,color:#fff,stroke:#4a90d9,stroke-width:3px
    style PM fill:#2c1654,color:#fff,stroke:#9b59b6,stroke-width:2px
    style MICHAEL fill:#2d5016,color:#fff,stroke:#5cb85c
    style ADMIN fill:#0d1a2d,color:#ccc,stroke:#4a90d9
    style DEV fill:#0d1f0d,color:#ccc,stroke:#5cb85c
    style BLOG fill:#1a0d00,color:#ccc,stroke:#cc7700
    style LEADS fill:#1a001a,color:#ccc,stroke:#9b59b6
```

---

## 🔀 Comunicación Inter-Agente

Los agentes no son islas. Se pasan trabajo directamente sin necesidad de que Jarvis intermedie en cada paso:

```mermaid
flowchart LR
    JARVIS["🧠 Jarvis\nOrquestador"]
    DAVID["🗂️ David\nPM"]
    BISHOP["⚙️ Bishop\nBackend"]
    SONNY["🎨 Sonny\nFrontend"]
    BB8["📱 BB-8\nMobile"]
    AVA["🔍 AVA\nQA"]
    OPTIMUS["🖥️ Optimus\nDevOps"]
    T800["🔐 T-800\nSecurity"]
    MARVIN["📝 Marvin\nDocs"]

    JARVIS -->|"Sprint brief"| DAVID
    DAVID -->|"Tareas"| BISHOP & SONNY & BB8
    BISHOP -->|"PR listo"| AVA
    SONNY -->|"PR listo"| AVA
    BB8 -->|"PR listo"| AVA
    AVA -->|"QA aprobado"| OPTIMUS
    OPTIMUS -->|"Deploy done"| T800
    T800 -->|"Security clear"| MARVIN
    MARVIN -->|"Docs updated"| DAVID
    DAVID -->|"Sprint report"| JARVIS
```

**Protocolo de comunicación entre agentes:**
- Cada agente puede invocar directamente a otro usando el sistema de mensajería de OpenClaw.
- Todas las comunicaciones inter-agente quedan registradas en `/workspace/logs/agent-comms.log`.
- Jarvis supervisa el estado pero no bloquea el flujo entre agentes de nivel inferior.
- Si un agente no puede completar su tarea, escala a David (Wing Software) o a Jarvis (cualquier wing).

---

## Tabla de Todos los Agentes

| # | Nombre | ID Técnico | Email | Rol | Modelo | Sandbox | Frecuencia |
|---|---|---|---|---|---|---|---|
| 01 | [🧠 **Jarvis**](./jarvis.md) | NTE-MAIN | jarvis@nissienterprise.com | Main Orchestrator | Opus 4 | ❌ Full FS | 24/7 + Heartbeat |
| — | **WING ADMINISTRATIVA** | | | | | | |
| 02 | [🎧 **Samantha**](./wing-administrativa/samantha.md) | NTE-CX | samantha@nissienterprise.com | Customer Experience | Sonnet 4 | ✅ Docker | 24/7 Continuo |
| 03 | [✍️ **WALL-E**](./wing-administrativa/walle.md) | NTE-CONTENT | walle@nissienterprise.com | Content & Marketing | Sonnet 4 | ✅ Docker | Alta (diaria) |
| 04 | [📊 **HAL**](./wing-administrativa/hal.md) | NTE-ANALYTICS | hal@nissienterprise.com | Analytics & Reporting | Haiku 4 | ✅ Docker | Semanal + alertas |
| — | **BLOG AUTOMATION** | | | | | | |
| 05 | [🔍 **Johnny 5**](./flujos-especializados/blog-automation/johnny5.md) | NTE-TREND-SCOUT | johnny5@nissienterprise.com | Investigador de Tendencias | Sonnet 4 | ✅ Docker | Semanal (Lun 2AM) |
| 06 | [✍️ **C-3PO**](./flujos-especializados/blog-automation/c3po.md) | NTE-COPYWRITER | c3po@nissienterprise.com | Redactor de Artículos | Sonnet 4 | ✅ Docker | 2x/semana |
| 07 | [🚀 **R2-D2**](./flujos-especializados/blog-automation/r2d2.md) | NTE-PUBLISHER | r2d2@nissienterprise.com | Publicador WordPress | Haiku 4 | ✅ Docker | On-demand |
| 08 | [📡 **Baymax**](./flujos-especializados/blog-automation/baymax.md) | NTE-PROPAGATOR | baymax@nissienterprise.com | Distribuidor Redes Sociales | Sonnet 4 | ✅ Docker | Post-publicación |
| — | **LEAD MANAGEMENT** | | | | | | |
| 09 | [📥 **EVA**](./flujos-especializados/lead-management/eva.md) | NTE-LEAD-INTAKE | eva@nissienterprise.com | Captador Multicanal | Sonnet 4 | ✅ Docker | 24/7 Continuo |
| 10 | [🌱 **TARS**](./flujos-especializados/lead-management/tars.md) | NTE-LEAD-NURTURE | tars@nissienterprise.com | Nurturing & Seguimiento | Sonnet 4 | ✅ Docker | 24/7 Continuo |
| — | **WING SOFTWARE R&D** | | | | | | |
| 11 | [🗂️ **David**](./wing-software/david.md) | NTE-PM | david@nissienterprise.com | Project Manager | Opus 4 | ✅ Docker | Por Sprint |
| 12 | [⚙️ **Bishop**](./wing-software/bishop.md) | NTE-BACKEND | bishop@nissienterprise.com | Backend Developer | Sonnet 4 | ✅ Docker | Activo en sprints |
| 13 | [🎨 **Sonny**](./wing-software/sonny.md) | NTE-FRONTEND | sonny@nissienterprise.com | Frontend Developer | Sonnet 4 | ✅ Docker | Activo en sprints |
| 14 | [📱 **BB-8**](./wing-software/bb8.md) | NTE-MOBILE | bb8@nissienterprise.com | Mobile Developer | Sonnet 4 | ✅ Docker | Por proyecto mobile |
| 15 | [🗄️ **CASE**](./wing-software/case.md) | NTE-DATA | case@nissienterprise.com | Data Engineer | Sonnet 4 | ✅ Docker | Por proyecto BI |
| 16 | [🔍 **AVA**](./wing-software/ava.md) | NTE-QA | ava@nissienterprise.com | QA & Tester | Sonnet 4 | ✅ Docker | Cada PR/commit |
| 17 | [🖥️ **Optimus**](./wing-software/optimus.md) | NTE-DEVOPS | optimus@nissienterprise.com | DevOps & Sysadmin | Sonnet 4 | ✅ Docker | Por deployment |
| 18 | [🔐 **T-800**](./wing-software/t800.md) | NTE-SECURITY | t800@nissienterprise.com | Security Agent | Opus 4 | ✅ Docker | Por release |
| 19 | [📝 **Marvin**](./wing-software/marvin.md) | NTE-DOCS | marvin@nissienterprise.com | Technical Writer | Haiku 4 | ✅ Docker | Post-commit |

---

## 📧 Servidor de Email Corporativo

Todos los agentes usan el servidor de email de NTE. No se usa Gmail.

```
Dominio:    @nissienterprise.com
Servidor:   mail.nissienterprise.com
Secretos:   Azure Key Vault → secret/nte-email-smtp
Protocolo:  SMTP/TLS (port 587) + IMAP (port 993)
```

Los agentes envían notificaciones por email cuando se amerita:
- **Samantha** → confirmaciones de citas, respuestas a clientes, escalaciones
- **TARS** → secuencias de nurturing, seguimientos de leads
- **WALL-E** → newsletter mensual, anuncios
- **David** → reportes de sprint a stakeholders
- **Optimus** → alertas de deployment y downtime
- **T-800** → reportes de seguridad y alertas críticas

---

## 🌿 Ambientes por Agente

Cada agente opera en 3 ambientes separados:

| Ambiente | Propósito | Datos |
|---|---|---|
| **Development** | Construcción y configuración de agentes | Fake data |
| **Staging** | Testing y demos con data real | Data real |
| **Production** | Sistema en vivo 24/7 | Data real |

Ver detalles completos → [../10-ambientes/ambientes.md](../10-ambientes/ambientes.md)

---

## Distribución de Modelos

```mermaid
pie title Distribución de Modelos Claude por Agente
    "Claude Sonnet 4 (12 agentes)" : 12
    "Claude Haiku 4 (3 agentes)" : 3
    "Claude Opus 4 (4 agentes)" : 4
```

---

[← Seguridad](../02-infraestructura/seguridad.md) | [Volver al inicio](../README.md) | [Jarvis →](./jarvis.md)
