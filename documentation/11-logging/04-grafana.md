<div align="center">

# 📊 Grafana — Dashboards & Alerts
### Visualization of the NTE Ecosystem

</div>

> **Note:** This document is a design reference. The implementation will take place in Phase 1 of the roadmap.

---

## Accessing Grafana

```bash
# From your Mac — SSH tunnel (never expose port 3000 directly)
ssh -L 3000:localhost:3000 openclaw@YOUR_VPS_IP

# Open in browser
http://localhost:3000

# Credentials
User:     admin
Password: [Azure Key Vault → secret/{env}/grafana-admin-password]
```

---

## Pre-configured Dashboards

### 1. 🧠 NTE Overview — General View

The main dashboard Michael will see first. It loads automatically on installation.

**What it shows:**

```
┌─────────────────────────────────────────────────────────────────┐
│  📊 System KPIs (last 24h)                                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │🔴 Critical│ │🟡 Errors │ │🚨 Escalat.│ │📋 Actions │          │
│  │    0     │ │    2     │ │    1     │ │  1,247   │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│  ┌──────────┐ ┌──────────┐                                     │
│  │🔀 InterAgt│ │📧 Emails │                                     │
│  │   342    │ │   28     │                                     │
│  └──────────┘ └──────────┘                                     │
├─────────────────────────────────────────────────────────────────┤
│  📈 Activity by Agent — last 24h                                 │
│  (line chart — one line per agent, different colors)            │
├─────────────────────────────────────────────────────────────────┤
│  🔴 Errors & Escalations — Filtered log viewer                  │
├─────────────────────────────────────────────────────────────────┤
│  🤖 Live Logs — All agents in real time                         │
└─────────────────────────────────────────────────────────────────┘
```

**Available filters:**
- **Environment:** production / staging / development
- **Agent:** All / jarvis / samantha / david / bishop / ... (each one separately)

**Auto-refresh:** every 30 seconds.

---

### 2. 🔍 NTE by Agent — Drilldown

You select a specific agent and see all of its activity.

```
Filter: [Agent: Samantha] [Environment: production] [Range: last 7 days]

┌─────────────────────────────────────────────────────────────────┐
│  Samantha (NTE-CX) · samantha@nissienterprise.com               │
├──────────┬──────────┬──────────┬──────────┬────────────────────┤
│ Messages │ Leads    │ Emails   │ Escalat. │ Resolution Rate    │
│ received │ captured │ sent     │ to Michael│ without escalation│
│  1,847   │   134    │   312    │    8     │       95.7%        │
├─────────────────────────────────────────────────────────────────┤
│  Samantha's activity timeline                                   │
│  (breakdown by event_type: ACTION / DECISION / EMAIL_SENT)      │
├─────────────────────────────────────────────────────────────────┤
│  Most recent lead classification decisions                      │
│  HOT: 23  |  WARM: 67  |  COLD: 44                            │
├─────────────────────────────────────────────────────────────────┤
│  Log viewer — all of Samantha's logs                            │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3. 🔗 NTE Trace Explorer — Follow a Complete Flow

The most powerful feature: given a `trace_id`, see the entire journey of a job across multiple agents.

```
Search trace_id: [a3f9-bc12-4e87-9f1c-d2e3a4b5c6d7]

Flow timeline:

  02:00:01  🧠 Jarvis     → heartbeat        "Starting weekly blog pipeline"
  02:00:02  🧠 Jarvis     → inter_agent      "Triggering Johnny 5"
  02:00:03  🔍 Johnny 5   → action           "Analyzing Google Trends (8 keywords)"
  02:04:17  🔍 Johnny 5   → api_call         "Semrush: GET /keywords [200 OK · 342ms]"
  02:06:02  🔍 Johnny 5   → inter_agent      "Sending briefing to C-3PO"
  02:06:05  ✍️  C-3PO      → action           "Writing article: Top 5 AI Trends for SMBs"
  04:12:33  ✍️  C-3PO      → action           "Article completed · 1,642 words"
  04:12:34  ✍️  C-3PO      → api_call         "WordPress: POST /wp/v2/posts [201 · 890ms]"
  04:12:35  ✍️  C-3PO      → inter_agent      "Notifying Michael via Slack"
  04:12:36  🧠 Jarvis     → escalation       "Blog draft ready for review · #nte-content"

  Total flow time: 2h 12m 35s  |  Status: escalated (pending approval)
```

**LogQL to search for it:**
```
{environment="production"} |= "a3f9-bc12-4e87-9f1c-d2e3a4b5c6d7"
```

---

### 4. 🔐 NTE Security — T-800 Dashboard

Dashboard dedicated exclusively to security logs.

```
┌─────────────────────────────────────────────────────────────────┐
│  🔐 T-800 (NTE-SECURITY) — Security Dashboard                   │
├──────────────┬─────────────────┬──────────────────────────────┤
│ Scans (7d)   │ Vulnerabilities  │ Azure KV Access               │
│     28       │   0 critical    │          847                 │
├─────────────────────────────────────────────────────────────────┤
│  Security Scan History                                          │
│  ✅ 2026-03-29  NTE-SW-142 PR  → PASS (0 vulnerabilities)      │
│  ✅ 2026-03-28  Deploy v1.2.3  → PASS (0 critical, 1 low)      │
│  ⚠️  2026-03-27  NTE-SW-139 PR  → WARN (1 medium)              │
├─────────────────────────────────────────────────────────────────┤
│  Azure Key Vault access — by secret and agent                   │
│  (table: secret | agent | timestamp | status)                   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5. 💼 NTE QuickBooks & Finance

```
┌─────────────────────────────────────────────────────────────────┐
│  💼 Financial Activity — QuickBooks                             │
├─────────────────────────────────────────────────────────────────┤
│  Latest operations                                               │
│  • 2026-03-29 09:14  TARS → draft invoice $7,500 [PENDING]    │
│  • 2026-03-28 16:30  Jarvis → invoice approved by Michael      │
│  • 2026-03-25 11:00  TARS → reminder payment overdue [SENT]    │
├─────────────────────────────────────────────────────────────────┤
│  All QB operations require Michael's approval                   │
│  → Those in PENDING status are shown in red                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## LogQL Reference Queries

LogQL is Loki's query language. It works similarly to PromQL but for logs.

```logql
── View all logs for an agent ────────────────────────────────
{agent="samantha", environment="production"}

── View only errors from the last 24h ────────────────────────────
{environment="production"} |= "ERROR" | json | level = "ERROR"

── View all escalations to Michael ───────────────────────────
{environment="production", event_type="ESCALATION"}

── Follow a flow by trace_id ───────────────────────────────────
{environment="production"} |= "a3f9-bc12-4e87-9f1c"

── View QuickBooks calls ──────────────────────────────────────
{environment="production", event_type="QB_EVENT"}

── View all inter-agent communication ──────────────────────────
{environment="production", event_type="INTER_AGENT"}

── View Optimus's deployments ─────────────────────────────────────
{agent="optimus", event_type="DEPLOY"}

── Count errors by agent (last 6h) ─────────────────────────
sum by (agent) (count_over_time({environment="production", level="ERROR"} [6h]))

── View Azure Key Vault access ──────────────────────────────────
{event_type="SECRET_ACCESS"} | json | vault = "nte-keyvault"
```

---

## Grafana Alerts

Alerts are configured in Grafana and notify Slack `#nte-alerts` and T-800's email.

| Alert | Condition | Destination |
|---|---|---|
| **Agent down** | 0 logs from an agent in > 10 min (during active hours) | `#nte-alerts` + Michael |
| **Critical error** | Any log with `level=CRITICAL` | `#nte-alerts` immediate |
| **High error rate** | > 5 errors/min on any agent | `#nte-alerts` |
| **Financial escalation** | Any `QB_EVENT` with `status=pending_approval` | Michael DM + `#nte-alerts` |
| **Failed security scan** | `SECURITY_SCAN` with `result=fail` | `#nte-alerts` + T-800 email |
| **API budget** | API token usage > $400/month detected | Michael DM |

---

## Grafana Automatic Provisioning

When the stack starts for the first time, Grafana automatically loads:
- The Loki datasource (no manual configuration)
- All dashboards from `/grafana/dashboards/`
- Alert contacts (Slack `#nte-alerts`)

Reference provisioning files:

```yaml
# grafana/provisioning/datasources/loki.yml
apiVersion: 1
datasources:
  - name: Loki
    type: loki
    access: proxy
    url: http://loki:3100
    isDefault: true
    jsonData:
      maxLines: 5000
      # clickable trace_id to view the full flow
      derivedFields:
        - name: TraceID
          matcherRegex: '"trace_id":"([^"]+)"'
          url: '$${__value.raw}'
          datasourceUid: loki
```

```yaml
# grafana/provisioning/dashboards/dashboards.yml
apiVersion: 1
providers:
  - name: NTE Dashboards
    type: file
    options:
      path: /var/lib/grafana/dashboards
    folder: NTE Intelligence Hub
```

---

[← Infrastructure](./03-infrastructure.md) | [Back to home](../README.md)
