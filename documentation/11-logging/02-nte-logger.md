<div align="center">

# 📝 NTE Logger — Referencia del Logger Central
### `nte-logger.js` · Basado en Pino

</div>

> **Nota:** Este documento es referencia de diseño. La implementación se realizará en la Fase 1 del roadmap.

---

## Instalación (cuando se implemente)

```bash
# En el directorio de cada agente
npm install pino pino-pretty uuid
```

---

## API del Logger — Métodos Disponibles

Cada agente importa el logger central y crea su instancia con su identidad:

```javascript
const { createAgentLogger } = require('/workspace/logging/nte-logger');

// Inicializar UNA VEZ al arrancar el agente
const log = createAgentLogger(
  'Samantha',       // Nombre del personaje
  'NTE-CX',         // ID técnico
  'administrativa'  // Wing
);
```

### Métodos por Tipo de Evento

```javascript
// ── Tarea programada del heartbeat ──────────────────────────────
log.heartbeat('Starting weekly blog pipeline');

// ── Acción interna de negocio ────────────────────────────────────
log.action('New WhatsApp message received', {
  client: 'Juan Perez',
  channel: 'whatsapp',
  preview: '¿Cuánto cuesta un sitio web?'
});

// ── Comando de sistema ejecutado ─────────────────────────────────
log.command('docker restart nte-samantha', {
  reason: 'memory_threshold_exceeded'
});

// ── Llamada a API externa ─────────────────────────────────────────
log.apiCall('QuickBooks', '/v3/company/invoices', 'POST', {
  invoice_number: 'INV-2026-001',
  amount: 3500
});

// ── Comunicación con otro agente ──────────────────────────────────
log.interAgent('NTE-TREND-SCOUT', 'Triggering weekly research', {
  trigger: 'monday_2am_heartbeat',
  target_articles: 2
});

// ── Decisión tomada por el agente ─────────────────────────────────
log.decision(
  'Classifying lead',
  'HOT',
  'Client mentioned specific budget of $8,000 for a web app',
  { lead_id: 'lead-2026-0329-001' }
);

// ── Escalación a Michael ──────────────────────────────────────────
log.escalation('Contract > $5,000 requires approval', {
  client: 'Empresa ABC',
  amount: 7500,
  slack_channel: '#nte-alerts'
});

// ── Acceso a Azure Key Vault ──────────────────────────────────────
log.secretAccess('quickbooks-oauth-token');

// ── Operación en Jira ─────────────────────────────────────────────
log.jiraEvent('CREATE', 'NTE-SW-142', {
  summary: 'Build authentication module',
  assignee: 'bishop'
});

// ── Operación en QuickBooks ───────────────────────────────────────
log.qbEvent('CREATE_INVOICE_DRAFT', {
  client: 'Empresa ABC',
  amount: 7500,
  status: 'pending_michael_approval'
});

// ── Email enviado ─────────────────────────────────────────────────
log.emailSent(
  'juan@empresa.com',
  'Gracias por contactar a Nissi Technology',
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

// ── Error no fatal ────────────────────────────────────────────────
log.error('Failed to call Semrush API', error, {
  retry_count: 3,
  next_retry_in: '5min'
});

// ── Error crítico ─────────────────────────────────────────────────
log.critical('Security breach attempt detected', error, {
  ip: '192.168.1.100',
  pattern: 'prompt_injection'
});

// ── Debug (solo visible en Development) ──────────────────────────
log.debug('Processing lead form data', { raw_form: formData });
```

---

## Flujos Multi-Agente — trace_id

La feature más importante: el `trace_id` conecta toda la cadena de trabajo entre agentes.

```javascript
// ── PASO 1: Jarvis inicia el flujo y genera el trace_id ──────────
const jarvisLog = createAgentLogger('Jarvis', 'NTE-MAIN', 'orchestrator');
jarvisLog.heartbeat('Starting weekly blog pipeline');

const traceId = jarvisLog.getTraceId(); // ← extraer el trace
jarvisLog.interAgent('NTE-TREND-SCOUT', 'Triggering Johnny 5', {
  trigger: 'monday_2am', target_articles: 2
});

// ── PASO 2: Johnny 5 recibe el trace_id y lo continúa ────────────
// (Jarvis se lo pasa al invocar el agente)
const johnny5Log = createAgentLogger('Johnny 5', 'NTE-TREND-SCOUT', 'blog', traceId);
johnny5Log.action('Analyzing Google Trends');

// ── PASO 3: C-3PO también lleva el mismo trace_id ────────────────
const c3poLog = createAgentLogger('C-3PO', 'NTE-COPYWRITER', 'blog', traceId);
c3poLog.action('Writing article: "Top 5 AI Trends for SMBs"');

// ── En Grafana: buscar el trace_id y ver TODO el flujo de un vistazo
// LogQL: {environment="production"} |= "a3f9-bc12-..."
```

---

## Medición de Tiempo Automática

```javascript
// timed() mide cuánto tarda una operación y lo registra automáticamente
const result = await log.timed(
  'Calling Jira API to create sprint',
  async () => {
    return await jiraClient.createSprint({ projectKey: 'NTE-SW' });
  },
  { event_type: 'JIRA_EVENT', details: { project: 'NTE-SW' } }
);
// Log generado: { message: "Calling Jira API...", duration_ms: 342, status: "success" }
```

---

## Formato de Salida JSON (lo que Promtail captura)

Cada llamada al logger produce una línea JSON en `stdout`:

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

[← README del Logging](./README.md) | [Configuración de Infraestructura →](./03-infraestructura.md)
