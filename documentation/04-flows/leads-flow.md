<div align="center">

# 🎯 Flujo: Gestión de Leads Multicanal
### De Extraño a Cliente en Tiempo Real

</div>

## Diagrama del Ciclo de Vida del Lead

```mermaid
flowchart TD
    subgraph ENTRADA["📥 CANALES 24/7"]
        WF["🌐 Website\nForms"] 
        WA["📱 WhatsApp\nBusiness"]
        SM["📘 Social\nMedia DMs"]
        CH["💬 Chatbot\nCrisp"]
        EM["📧 Email\n@nissienterprise.com"]
    end

    INTAKE["📥 EVA (NTE-LEAD-INTAKE)\nNormaliza · Clasifica · Responde < 5min"]

    HOT["🔴 HOT\nServicio específico + budget"]
    WARM["🟡 WARM\nInterés + preguntas"]
    COLD["🔵 COLD\nSolo información"]

    ALERT["🚨 Alerta Slack\n#nte-leads\n< 15 minutos"]
    NURTURE["📧 TARS (NTE-LEAD-NURTURE)\nSecuencia 5 toques · 14 días · Email + WA"]
    EDUCATE["📚 TARS (NTE-LEAD-NURTURE)\nSecuencia 3 emails · 30 días + Newsletter"]

    MICHAEL["👤 Michael\nContacto directo"]
    DISCOVERY["📞 Llamada\nDiscovery 30min"]
    PROPOSAL["💰 Cotización\nSamantha genera (QuickBooks estimado)"]
    PROJECT["⚙️ Proyecto\nDavid (NTE-PM) inicia en Jira"]

    RECLASS["♻️ Re-clasifica\nsegún engagement"]
    ARCHIVE["📁 Archiva\nsin actividad 60 días"]

    ENTRADA --> INTAKE
    INTAKE --> HOT & WARM & COLD
    HOT --> ALERT --> MICHAEL --> DISCOVERY --> PROPOSAL --> PROJECT
    WARM --> NURTURE
    COLD --> EDUCATE
    NURTURE --> RECLASS
    EDUCATE --> RECLASS
    RECLASS -->|"Calienta"| HOT
    RECLASS -->|"Sin actividad"| ARCHIVE

    style HOT fill:#8B0000,color:#fff,stroke:#CC0000
    style WARM fill:#7B6000,color:#fff,stroke:#CC9900
    style COLD fill:#003380,color:#fff,stroke:#4a90d9
    style PROJECT fill:#2c1654,color:#fff,stroke:#9b59b6
    style MICHAEL fill:#2d5016,color:#fff,stroke:#5cb85c
```

## Métricas del Pipeline

| Métrica | Meta |
|---|---|
| Tiempo de primera respuesta | < 5 minutos |
| Tasa de conversión COLD → WARM | > 20% en 30 días |
| Tasa de conversión WARM → HOT | > 15% en 14 días |
| HOT leads cerrados | > 30% |
| Consultas resueltas sin escalada | > 70% |

[← Todos los flujos](./README.md)
