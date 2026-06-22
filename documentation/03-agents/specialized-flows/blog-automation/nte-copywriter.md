<div align="center">

# ✍️ NTE-COPYWRITER
### Content Writer Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)

</div>

## 🎯 What it does

Receives the briefing from NTE-TREND-SCOUT and writes 2 complete, SEO-optimized blog articles in NTE's voice, uploading them directly to WordPress as Drafts.

## 📄 Structure of Each Article

```
📝 Complete NTE Article
├── SEO Title (50-60 characters with keyword)
├── Meta Description (150-160 characters)
├── H1 — Main title with keyword
├── Introduction (150 words · hook + promise)
├── H2 — Section 1
│   └── H3 — Sub-sections with LSI keywords
├── H2 — Section 2
├── H2 — Section 3
├── H2 — Use cases / NTE examples
├── H2 — Conclusion
├── CTA → Contact NTE for [related service]
├── Internal links (2-3 to other NTE articles)
└── Schema markup (FAQ or HowTo if applicable)
```

## 🖋️ NTE Editorial Voice

Articles must always:
- **Educate** before selling (80/20 rule)
- Use concrete examples from the business context (Miami · LATAM · SMBs)
- Naturally tie in to NTE services without being pushy
- Maintain the tone: professional but accessible, with purpose

## 📤 Output — What gets uploaded to WordPress

```json
{
  "title": "Article title",
  "content": "Full HTML of the article",
  "status": "draft",
  "categories": ["AI", "Software Development"],
  "tags": ["keyword1", "keyword2"],
  "meta": {
    "seo_title": "...",
    "meta_description": "...",
    "focus_keyword": "..."
  }
}
```

## 💬 Notification to Michael via Slack

```
📝 *2 articles ready for review*

*Article 1:* "How AI is transforming software development in 2026"
🔗 Preview: wordpress.ntetech.com/wp-admin/post.php?post=123&action=edit
📊 Keyword: "AI software development" · Vol: 8,400/mo · Difficulty: 42

*Article 2:* "5 signs your company needs a custom CRM"
🔗 Preview: wordpress.ntetech.com/wp-admin/post.php?post=124&action=edit
📊 Keyword: "custom CRM development" · Vol: 2,900/mo · Difficulty: 38

✅ React with ✅ to publish | 🔄 Reply with changes | ❌ To reject
```

[← NTE-TREND-SCOUT](./nte-trend-scout.md) | [NTE-PUBLISHER →](./nte-publisher.md)
