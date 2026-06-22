<div align="center">

# 🎧 NTE-CX
### Customer Experience Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Frequency](https://img.shields.io/badge/Frequency-24/7_Continuous-4a90d9?style=flat-square)

*NTE's first point of contact with the world. Never sleeps.*

</div>

---

## 🎯 Responsibilities

NTE-CX is the guardian of the customer experience. Responds in under **5 minutes** across all channels, upholds NTE's voice (Faith, Integrity, Excellence), and knows exactly when to escalate.

---

## 📡 Monitored Channels

```mermaid
flowchart LR
    WA["📱 WhatsApp Business\n(Twilio API)"] --> CX
    EM["📧 Email\n(Gmail API)"] --> CX
    FB["📘 Facebook Messenger\n(Meta API)"] --> CX
    IG["📸 Instagram DMs\n(Meta API)"] --> CX
    CH["💬 Web Chat\n(Crisp API)"] --> CX
    FM["📝 Web Forms\n(Webhook)"] --> CX
    SMS["📟 SMS\n(Twilio)"] --> CX

    CX["🎧 NTE-CX\nClassifies & Responds"]

    CX -->|"Project detected"| LI["📥 NTE-LEAD-INTAKE"]
    CX -->|"Complex technical support"| PM["🗂️ NTE-PM"]
    CX -->|"Urgent escalation"| SLACK["💬 #nte-cx"]
```

---

## 🔀 Classification Flow

| Detected intent | Action | Time |
|---|---|---|
| Service quote | Generates preliminary proposal + passes to NTE-LEAD-INTAKE | < 5 min |
| Technical support | Responds with basic steps; escalates to NTE-PM if complex | < 5 min |
| General information | Responds using NTE services knowledge base | < 2 min |
| Active customer complaint | Logs + immediate alert to Michael via #nte-cx | Immediate |
| Spam / irrelevant | Archives and does not respond | Automatic |

---

## 🛠️ Tools & APIs

- **Twilio** — WhatsApp Business + SMS
- **Gmail API** — Corporate email
- **Meta API** — Facebook + Instagram
- **Crisp** — Website live chat
- **CRM (HubSpot)** — Logs all interactions

---

[← NTE-MAIN](../nte-main.md) | [NTE-CONTENT →](./nte-content.md)
