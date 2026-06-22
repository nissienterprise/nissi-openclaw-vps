<div align="center">

# 📝 NTE Logger — Central Logger Reference
### `nte-logger.js` · Based on Pino

</div>

> **Note:** This document is a design reference. The implementation will take place in Phase 1 of the roadmap.

---

## Installation (when implemented)

```bash
# In each agent's directory
npm install pino pino-pretty uuid
```

---

## Logger API — Available Methods

Each agent imports the central logger and creates its instance with its identity:

```javascript
const { createAgentLogger } = require('/workspace/logging/nte-logger');

// Initialize ONCE when the agent starts
const log = createAgentLogger(
  'Samantha',       // Character name
  'NTE-CX',         // Technical ID
  'administrative'  // Wing
);
```

### Methods by Event Type

```javascript
// ── Scheduled heartbeat task ──────────────────────────────
log.heartbeat('Starting weekly blog pipeline');

// ── Internal business action ────────────────────────────────────
log.action('New WhatsApp message received', {
  client: 'Juan Perez',
  channel: 'whatsapp',
  preview: 'How much does a website cost?'
});

// ── System command executed ─────────────────────────────────
log.command('docker restart nte-samantha', {
  reason: 'memory_threshold_exceeded'
});

// ── External API call ─────────────────────────────────────────
log.apiCall('QuickBooks', '/v3/company/invoices', 'POST', {
  invoice_number: 'INV-2026-001',
  amount: 3500
});

// ── Communication with another agent ──────────────────────────────────
log.interAgent('NTE-TREND-SCOUT', 'Triggering weekly research', {
  trigger: 'monday_2am_heartbeat',
  target_articles: 2
});

// ── Decision made by the agent ─────────────────────────────────
log.decision(
  'Classifying lead',
  'HOT',
  'Client mentioned specific budget of $8,000 for a web app',
  { lead_id: 'lead-2026-0329-001' }
);

// ── Escalation to Michael ──────────────────────────────────────────
log.escalation('Contract > $5,000 requires approval', {
  client: 'Company ABC',
  amount: 7500,
  slack_channel: '#nte-alerts'
});

// ── Azure Key Vault access ──────────────────────────────────────
log.secretAccess('quickbooks-oauth-token');

// ── Jira operation ─────────────────────────────────────────────────
log.jiraEvent('CREATE', 'NTE-SW-142', {
  summary: 'Build authentication module',
  assignee: 'bishop'
});

// ── QuickBooks operation ───────────────────────────────────────
log.qbEvent('CREATE_INVOICE_DRAFT', {
  client: 'Company ABC',
  amount: 7500,
  status: 'pending_michael_approval'
});

// ── Email sent ─────────────────────────────────────────────────────
log.emailSent(
  'juan@empresa.com',
  'Thank you for contacting Nissi Technology',
  'smtp'
);

// ── Deployment ────────────────────────────────────────────────────
log.deploy('staging', 'v1.2.3', {
  environment: 'staging',
  triggered_by: 'david'
});

// ── Security scan ─────────────────────────────────────────────────
log.securityScan('NTE-SW-142 PR', 'pass', {
  vulnerabilities_found: 0,
  scan_duration_ms: 4200
});

// ── Non-fatal error ────────────────────────────────────────────────
log.error('Failed to call Semrush API', error, {
  retry_count: 3,
  next_retry_in: '5min'
});

// ── Critical error ─────────────────────────────────────────────────
log.critical('Security breach attempt detected', error, {
  ip: '192.168.1.100',
  pattern: 'prompt_injection'
});

// ── Debug (only visible in Development) ──────────────────────────
log.debug('Processing lead form data', { raw_form: formData });
```

---

## Multi-Agent Flows — trace_id

The most important feature: the `trace_id` connects the entire chain of work across agents.

```javascript
// ── STEP 1: Jarvis starts the flow and generates the trace_id ──────────
const jarvisLog = createAgentLogger('Jarvis', 'NTE-MAIN', 'orchestrator');
jarvisLog.heartbeat('Starting weekly blog pipeline');

const traceId = jarvisLog.getTraceId(); // ← extract the trace
jarvisLog.interAgent('NTE-TREND-SCOUT', 'Triggering Johnny 5', {
  trigger: 'monday_2am', target_articles: 2
});

// ── STEP 2: Johnny 5 receives the trace_id and continues it ────────────
// (Jarvis passes it along when invoking the agent)
const johnny5Log = createAgentLogger('Johnny 5', 'NTE-TREND-SCOUT', 'blog', traceId);
johnny5Log.action('Analyzing Google Trends');

// ── STEP 3: C-3PO also carries the same trace_id ────────────────
const c3poLog = createAgentLogger('C-3PO', 'NTE-COPYWRITER', 'blog', traceId);
c3poLog.action('Writing article: "Top 5 AI Trends for SMBs"');

// ── In Grafana: search for the trace_id to see the ENTIRE flow at a glance
// LogQL: {environment="production"} |= "a3f9-bc12-..."
```

---

## Automatic Timing Measurement

```javascript
// timed() measures how long an operation takes and logs it automatically
const result = await log.timed(
  'Calling Jira API to create sprint',
  async () => {
    return await jiraClient.createSprint({ projectKey: 'NTE-SW' });
  },
  { event_type: 'JIRA_EVENT', details: { project: 'NTE-SW' } }
);
// Log generated: { message: "Calling Jira API...", duration_ms: 342, status: "success" }
```

---

## JSON Output Format (what Promtail captures)

Each call to the logger produces a JSON line on `stdout`:

```json
{
  "time": "2026-03-29T10:30:00.123Z",
  "level": "INFO",
  "trace_id": "a3f9-bc12-4e87-9f1c-d2e3a4b5c6d7",
  "span_id": "f1e2-4d89-11b2-8c3f-e9a0b1c2d3e4",
  "event_type": "INTER_AGENT",
  "agent_name": "Jarvis",
  "agent_id": "NTE-MAIN",
  "agent_email": "jarvis@nissienterprise.com",
  "wing": "orchestrator",
  "environment": "production",
  "status": "success",
  "triggered_by": "heartbeat",
  "parent_agent": null,
  "duration_ms": 12,
  "details": {
    "target_agent": "NTE-TREND-SCOUT",
    "trigger": "monday_2am_heartbeat",
    "target_articles": 2
  },
  "msg": "Triggering Johnny 5 for weekly blog research"
}
```

---

[← Logging README](./README.md) | [Infrastructure Configuration →](./03-infrastructure.md)
