<div align="center">

# ✍️ NTE-CONTENT
### Content & Marketing Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Frequency](https://img.shields.io/badge/Frequency-Daily-4a90d9?style=flat-square)

*NTE's digital voice. Generates, schedules, and distributes content aligned with the brand.*

</div>

---

## 🎯 Responsibilities

Autonomously runs NTE's **monthly editorial calendar**. Coordinates with NTE-TREND-SCOUT for blog articles and manages evergreen social media content.

---

## 📅 Editorial Calendar

| Channel | Frequency | Content type |
|---|---|---|
| WordPress Blog | 2 articles/week | SEO · Educational · Use cases |
| LinkedIn | 5 posts/week | Professional · Thought leadership |
| Instagram | 1 post + 3 stories/day | Visual · Tips · Behind the scenes |
| Facebook | 3 posts/week | Community · News · Testimonials |
| Twitter/X | 2 tweets/day | Quick · Tips · Tech news |
| Newsletter | 1 email/month | Summary + NTE updates |

---

## 🔧 Content Pipeline

```mermaid
flowchart LR
    TS["🔍 NTE-TREND-SCOUT\nTrending topics"] --> CW["✍️ NTE-COPYWRITER\nFull article"]
    CW --> PUB["🚀 NTE-PUBLISHER\nPublishes on WP"]
    PUB --> PROP["📡 NTE-PROPAGATOR\nAdapts for social media"]
    
    CONTENT["✍️ NTE-CONTENT\nCoordinates everything"] -.->|"Oversees"| TS & CW & PUB & PROP
```

---

## 🛠️ Tools & APIs

- **WordPress REST API** — Blog publishing
- **Buffer API** — Social media scheduling
- **SendGrid / Mailchimp** — Monthly newsletter
- **DALL-E / Stable Diffusion** — Content images
- **Semrush API** — Keywords and SEO analysis

---

[← NTE-CX](./nte-cx.md) | [NTE-ANALYTICS →](./nte-analytics.md)
