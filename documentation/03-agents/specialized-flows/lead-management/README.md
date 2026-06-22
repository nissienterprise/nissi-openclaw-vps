<div align="center">

# 🎯 Lead Management Pipeline
### From Stranger to Client — Fully Automated

*2 specialized agents · 24/7 operation · 3 classification levels*

</div>

---

## Full Flow

```mermaid
flowchart TD
    subgraph CANALES["📥 Inbound Channels"]
        WF["🌐 Website"] & WA["📱 WhatsApp"] & SM["📘 Social Media"] & CH["💬 Chatbot"] & EM["📧 Email"]
    end

    subgraph INTAKE["📥 NTE-LEAD-INTAKE · Sonnet 4"]
        I1["Normalizes the lead\ninto a unified profile"]
        I2["Immediate response\n< 5 minutes"]
        I3["Creates CRM record"]
    end

    HOT["🔴 HOT\nSpecific service\n+ budget"]
    WARM["🟡 WARM\nGeneral interest\n+ questions"]
    COLD["🔵 COLD\nInfo only\nBrowsing"]

    subgraph NURTURE["🌱 NTE-LEAD-NURTURE · Sonnet 4"]
        N1["🚨 Immediate alert\nto Michael · Slack"]
        N2["📧 5-touch sequence\n14 days\nEmail + WhatsApp"]
        N3["📚 Educational sequence\n3 emails · 30 days\n+ Newsletter"]
        N4["♻️ Re-classifies\nbased on engagement"]
    end

    MICHAEL["👤 Michael\nDirect contact"] --> CONVERT["💰 NTE-PM Project"]

    CANALES --> I1
    I1 --> I2 & I3
    I1 -->|"Classifies"| HOT & WARM & COLD
    HOT --> N1 --> MICHAEL --> CONVERT
    WARM --> N2
    COLD --> N3
    N2 & N3 --> N4
    N4 -->|"Lead warms up"| HOT

    style HOT fill:#8B0000,color:#fff
    style WARM fill:#7B6000,color:#fff
    style COLD fill:#003380,color:#fff
```

---

## Lead Classification

### 🔴 HOT Lead — Immediate Action (< 15 min)
- Mentions a specific service ("I need a mobile app")
- Has a defined budget or clear timeline
- Already has an established company
- Was referred by an existing client

### 🟡 WARM Lead — 14-day Nurturing
- General interest in NTE services
- Asks questions but lacks clarity on what they need
- Visited the website multiple times (if tracking is available)
- Downloaded a resource or filled out a contact form

### 🔵 COLD Lead — 30-day Education
- Only requested general information
- Did not respond to qualification questions
- Only reads the blog or visits social media
- Very early in their decision process

---

## Monitored Channels

| Channel | API | Response Time |
|---|---|---|
| Website Forms | Webhook | < 2 min |
| WhatsApp Business | Twilio / Meta API | < 5 min |
| Facebook Messenger | Meta API | < 5 min |
| Instagram DMs | Meta API | < 5 min |
| Web Chat (Crisp) | Crisp Webhook | < 2 min |
| Email | Gmail API | < 10 min |

---

[← All agents](../../README.md) | [NTE-LEAD-INTAKE →](./nte-lead-intake.md)
