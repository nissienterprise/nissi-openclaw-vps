<div align="center">

# 🎯 Flow: Multichannel Lead Management
### From Stranger to Customer in Real Time

</div>

## Lead Lifecycle Diagram

```mermaid
flowchart TD
    subgraph ENTRADA["📥 24/7 CHANNELS"]
        WF["🌐 Website\nForms"] 
        WA["📱 WhatsApp\nBusiness"]
        SM["📘 Social\nMedia DMs"]
        CH["💬 Chatbot\nCrisp"]
        EM["📧 Email\n@nissienterprise.com"]
    end

    INTAKE["📥 EVA (NTE-LEAD-INTAKE)\nNormalizes · Classifies · Responds < 5min"]

    HOT["🔴 HOT\nSpecific service + budget"]
    WARM["🟡 WARM\nInterest + questions"]
    COLD["🔵 COLD\nInfo only"]

    ALERT["🚨 Slack Alert\n#nte-leads\n< 15 minutes"]
    NURTURE["📧 TARS (NTE-LEAD-NURTURE)\n5-touch sequence · 14 days · Email + WA"]
    EDUCATE["📚 TARS (NTE-LEAD-NURTURE)\n3-email sequence · 30 days + Newsletter"]

    MICHAEL["👤 Michael\nDirect contact"]
    DISCOVERY["📞 Discovery\nCall 30min"]
    PROPOSAL["💰 Quote\nSamantha generates (QuickBooks estimate)"]
    PROJECT["⚙️ Project\nDavid (NTE-PM) starts in Jira"]

    RECLASS["♻️ Re-classifies\nbased on engagement"]
    ARCHIVE["📁 Archives\nno activity for 60 days"]

    ENTRADA --> INTAKE
    INTAKE --> HOT & WARM & COLD
    HOT --> ALERT --> MICHAEL --> DISCOVERY --> PROPOSAL --> PROJECT
    WARM --> NURTURE
    COLD --> EDUCATE
    NURTURE --> RECLASS
    EDUCATE --> RECLASS
    RECLASS -->|"Warms up"| HOT
    RECLASS -->|"No activity"| ARCHIVE

    style HOT fill:#8B0000,color:#fff,stroke:#CC0000
    style WARM fill:#7B6000,color:#fff,stroke:#CC9900
    style COLD fill:#003380,color:#fff,stroke:#4a90d9
    style PROJECT fill:#2c1654,color:#fff,stroke:#9b59b6
    style MICHAEL fill:#2d5016,color:#fff,stroke:#5cb85c
```

## Pipeline Metrics

| Metric | Target |
|---|---|
| First response time | < 5 minutes |
| COLD → WARM conversion rate | > 20% in 30 days |
| WARM → HOT conversion rate | > 15% in 14 days |
| HOT leads closed | > 30% |
| Inquiries resolved without escalation | > 70% |

[← All flows](./README.md)
