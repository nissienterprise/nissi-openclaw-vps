<div align="center">

# 🔍 NTE-TREND-SCOUT
### Trend Research Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Activation](https://img.shields.io/badge/Activation-Monday_2AM_EST-4a90d9?style=flat-square)

</div>

## 🎯 What it does

Every Monday at 2:00 AM EST, NTE-TREND-SCOUT activates and scans the internet for the most relevant technology topics of the week that align with NTE's services.

## 🔎 Research Process

```mermaid
flowchart TD
    A["⏰ Automatic activation\nMonday 2:00 AM EST"] --> B["🌐 Queries sources"]
    B --> C["Google Trends\nSemrush\nReddit r/technology\nLinkedIn Trending\nHacker News"]
    C --> D["🎯 Filters by NTE services\nSoftware · AI · Web · Mobile\nBI · Infrastructure · Marketing"]
    D --> E["📊 Scores by potential\nSearch volume · Competition\nNTE relevance · Trending velocity"]
    E --> F["🏆 Selects Top 2 topics"]
    F --> G["📋 Generates full Briefing\nTopic · Keywords · Audience\nEditorial angle · Target CTA"]
    G --> H["✍️ Sends to NTE-COPYWRITER"]
```

## 📋 Briefing Format

```markdown
## NTE-TREND-SCOUT WEEKLY BRIEFING
Week: [date]

### ARTICLE 1
- **Topic:** [tentative title]
- **Primary Keyword:** [keyword with volume X searches/month]
- **Secondary Keywords:** [list]
- **Target Audience:** [profile of the ideal reader]
- **Editorial Angle:** [why it's relevant NOW for NTE clients]
- **Related NTE Services:** [which services we can tie in]
- **Suggested CTA:** [what action we want the reader to take]
- **Recommended Length:** [1200-1800 words]

### ARTICLE 2
[same structure]
```

## 🛠️ APIs Used

- **Google Trends API (Unofficial)** — Trending topics by region
- **Semrush API** — Search volume and keyword difficulty
- **Reddit API** — Most popular threads in tech subreddits
- **RSS Feeds** — Hacker News, TechCrunch, The Verge

[← Blog Pipeline](./README.md) | [NTE-COPYWRITER →](./nte-copywriter.md)
