<div align="center">

# 📥 NTE-LEAD-INTAKE
### Lead Intake Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Frequency](https://img.shields.io/badge/Frequency-24/7_Continuous-4a90d9?style=flat-square)

*The first filter. Captures, classifies, and responds in under 5 minutes.*

</div>

## 🎯 What it does

Operates 24/7 listening to all of NTE's inbound channels. When it detects a potential lead, it normalizes it into a unified profile, classifies it by temperature, creates the CRM record, and sends an immediate personalized response.

## 📋 Unified Lead Profile

```json
{
  "lead_id": "NTE-LEAD-2026-001",
  "timestamp": "2026-03-28T14:32:00Z",
  "channel": "whatsapp",
  "contact": {
    "name": "Ana García",
    "phone": "+1-305-555-0123",
    "email": "ana@empresa.com",
    "company": "García Dental Group",
    "location": "Miami, FL"
  },
  "intent": {
    "service_interest": "website_development",
    "budget_range": "$2000-$5000",
    "timeline": "2 months",
    "urgency": "medium"
  },
  "classification": "WARM",
  "original_message": "Hi, I'm looking for information about websites for my dental practice",
  "response_sent": true,
  "crm_id": "HS-12345",
  "assigned_to": "NTE-LEAD-NURTURE"
}
```

## 💬 Immediate Responses by Type

**HOT Lead:** Personalized response + "An NTE representative will contact you within the next 15 minutes" → Immediate alert to Michael

**WARM Lead:** Response with 2-3 qualification questions + a mini-presentation of NTE relevant to the mentioned service

**COLD Lead:** Response with relevant educational resources + invitation to learn more about NTE

## 🛠️ Tools

- **Twilio API** — WhatsApp + SMS
- **Gmail API** — Incoming email
- **Meta Webhooks** — Facebook + Instagram
- **Crisp Webhooks** — Web chat
- **HubSpot CRM API** — Lead registration

[← Lead Management](./README.md) | [NTE-LEAD-NURTURE →](./nte-lead-nurture.md)
