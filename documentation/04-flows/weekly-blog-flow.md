<div align="center">

# 🔄 Flow: Automated Weekly Blog
### From Trend to Tweet in 48 hours

</div>

## Complete Sequence Diagram

```mermaid
sequenceDiagram
    participant MAIN as 🧠 Jarvis (NTE-MAIN)
    participant TS as 🔍 Johnny 5 (TREND-SCOUT)
    participant CW as ✍️ C-3PO (COPYWRITER)
    participant M as 👤 Michael
    participant PUB as 🚀 R2-D2 (PUBLISHER)
    participant PROP as 📡 Baymax (PROPAGATOR)
    participant WP as 🌐 WordPress
    participant BUF as 📱 Buffer/Social

    Note over MAIN,TS: ⏰ MONDAY 2:00 AM EST — AUTOMATIC START

    MAIN->>TS: Activate weekly analysis
    TS->>TS: Analyzes Google Trends, Semrush, Reddit
    TS->>TS: Filters by NTE services
    TS->>TS: Selects Top 2 topics with scoring
    TS->>CW: Briefing: topic, keywords, audience, CTA

    Note over CW: Drafting of 2 complete articles
    CW->>CW: Article 1: full SEO, 1200-1800 words
    CW->>CW: Article 2: full SEO, 1200-1800 words
    CW->>WP: POST /wp-json/wp/v2/posts (status: draft)
    CW->>M: 📨 Slack #nte-content with preview links

    Note over M: ⏳ 24-48 hour approval window

    alt ✅ Michael approves
        M->>PUB: ✅ Reaction or "publish" reply
        PUB->>PUB: DALL-E generates featured image
        PUB->>WP: PATCH post → status: published + image
        WP-->>PUB: Published article URL
        PUB->>M: ✅ "Article published: [URL]"
        PUB->>PROP: Trigger with URL + content

        Note over PROP: Adaptation for 5 platforms
        PROP->>PROP: LinkedIn: 300 words professional
        PROP->>PROP: Instagram: caption + 10 hashtags
        PROP->>PROP: Facebook: community post + question
        PROP->>PROP: Twitter/X: 4-5 tweet thread
        PROP->>PROP: YouTube: 60-second script
        PROP->>BUF: Schedules staggered posts (3-5 days)
        PROP->>M: 📊 Report with publication dates

    else 🔄 Michael requests changes
        M->>CW: "Changes: [instructions]"
        CW->>WP: Updates draft with changes
        CW->>M: 📨 "Draft updated — [preview link]"

    else ❌ Michael rejects
        M->>PUB: "Reject article X"
        PUB->>WP: DELETE draft
        PUB->>M: "✓ Article discarded"

    else ⏰ No response after 72h
        MAIN->>M: 🔔 Reminder in #nte-alerts
        Note over M: If still no response → archived
    end
```

## Typical Timeline

| Time | Event |
|---|---|
| Monday 2:00 AM | Johnny 5 (NTE-TREND-SCOUT) starts analysis |
| Monday 2:30 AM | Briefing sent to C-3PO (NTE-COPYWRITER) |
| Monday 5:00 AM | 2 articles drafted and uploaded as drafts |
| Monday 7:00 AM | Michael receives notification on Slack |
| Monday/Tuesday | Michael reviews and approves |
| +30 min | Article published + image generated |
| Week | Social media posts distributed on a staggered schedule |

[← All flows](./README.md)
