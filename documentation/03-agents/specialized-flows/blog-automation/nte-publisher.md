<div align="center">

# 🚀 NTE-PUBLISHER
### WordPress Publisher Agent

![Model](https://img.shields.io/badge/Model-Claude_Haiku_4-5cb85c?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)

</div>

## 🎯 What it does

Monitors the `#nte-content` Slack channel waiting for Michael's approval. Once detected, it publishes the draft on WordPress, generates the featured image with AI, and triggers NTE-PROPAGATOR.

## 🔍 Approval Detection

NTE-PUBLISHER recognizes these signals on Slack:
- ✅ emoji reaction on the draft message
- A reply containing: "approved", "publish", "go ahead", "go"
- Direct message: "publish article X"

## ⚙️ Publishing Process

```mermaid
flowchart LR
    A["🔔 Approval detected\non Slack"] --> B["🔍 Identifies which post\nMichael approved"]
    B --> C["🎨 Generates featured image\nvia DALL-E API"]
    C --> D["📤 WordPress REST API\nstatus: draft → published"]
    D --> E["✅ Confirms publication\non Slack"]
    E --> F["📡 Triggers NTE-PROPAGATOR\nwith the article URL"]
```

## 🖼️ Featured Image Generation

```
DALL-E Prompt: "Professional technology illustration for blog post about 
[article topic], corporate style, blue and white color palette, 
no text, modern minimalist, suitable for Nissi Technology Enterprises blog"
```

> **Why Haiku 4?** NTE-PUBLISHER's task is simple: detect a pattern on Slack and make 2-3 API calls. It does not require complex reasoning. Haiku executes this perfectly at a fraction of the cost.

[← NTE-COPYWRITER](./nte-copywriter.md) | [NTE-PROPAGATOR →](./nte-propagator.md)
