<div align="center">

# 🌱 NTE-LEAD-NURTURE
### Lead Nurturing Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Frequency](https://img.shields.io/badge/Frequency-24/7_Continuous-4a90d9?style=flat-square)

*Turns interest into conversation and conversation into clients.*

</div>

## 🎯 What it does

Receives classified leads from NTE-LEAD-INTAKE and works them with personalized follow-up sequences based on their temperature. Monitors engagement and re-classifies automatically.

## 📧 Nurturing Sequences

### 🔴 HOT Lead — Immediate Alert

```
Slack → #nte-leads:

🔴 *HOT LEAD DETECTED*

👤 *Name:* Ana García — García Dental Group
📱 *Channel:* WhatsApp
💬 *Message:* "I need a professional website for my dental clinic, I have a budget of $3,000-$5,000 and need it in 6 weeks"
🎯 *Service:* Web Development — Corporate Site
💰 *Estimated Budget:* $3,000-$5,000
⏰ *Timeline:* 6 weeks

*Suggested next step:* Discovery call (30 min)
[View full profile in CRM →]
```

### 🟡 WARM Lead — 5-Touch Sequence (14 days)

| Touch | Day | Channel | Content |
|---|---|---|---|
| 1 | Day 1 | Email | Welcome + relevant case study |
| 2 | Day 3 | WhatsApp | "Were you able to review the information?" + qualification question |
| 3 | Day 7 | Email | Blog article relevant to the service of interest |
| 4 | Day 10 | WhatsApp | Invitation to a free consultation call (15 min) |
| 5 | Day 14 | Email | "Last chance" + special offer or testimonial |

### 🔵 COLD Lead — Educational Sequence (30 days)

| Email | Day | Topic |
|---|---|---|
| 1 | Day 2 | "Welcome to NTE — The guide you need for [topic]" |
| 2 | Day 10 | "5 mistakes companies make in [area of interest]" |
| 3 | Day 25 | "Ready for the next step? NTE success stories" |

## ♻️ Automatic Re-classification

NTE-LEAD-NURTURE monitors:
- **Email opens** → If they open 3+ consecutive emails: COLD → WARM
- **WhatsApp reply** → If they reply with specific questions: WARM → HOT
- **Click on "Schedule a call"** → Immediately HOT + alert to Michael
- **No activity for 30 days** → Archived with a note for future reactivation

## 🛠️ Tools

- **SendGrid API** — Automated email sequences
- **Twilio API** — WhatsApp follow-up
- **HubSpot CRM** — Tracking the entire lead cycle
- **Google Calendar API** — Automatic call scheduling

[← NTE-LEAD-INTAKE](./nte-lead-intake.md) | [Back to home](../../../../README.md)
