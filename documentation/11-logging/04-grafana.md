<div align="center">

# 📊 Grafana — Dashboards & Alertas
### Visualización del Ecosistema NTE

</div>

> **Nota:** Este documento es referencia de diseño. La implementación se realizará en la Fase 1 del roadmap.

---

## Acceso a Grafana

```bash
# Desde tu Mac — SSH tunnel (nunca exponer el puerto 3000 directamente)
ssh -L 3000:localhost:3000 openclaw@TU_VPS_IP

# Abrir en el browser
http://localhost:3000

# Credenciales
Usuario:  admin
Password: [Azure Key Vault → secret/{env}/grafana-admin-password]
```

---

## Dashboards Pre-configurados

### 1. 🧠 NTE Overview — Vista General

El dashboard principal que Michael verá primero. Se carga automáticamente al instalar.

**Qué muestra:**

```
┌─────────────────────────────────────────────────────────────────┐
│  📊 KPIs del Sistema (últimas 24h)                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │🔴 Críticos│ │🟡 Errores │ │🚨 Escalac.│ │📋 Acciones│          │
│  │    0     │ │    2     │ │    1     │ │  1,247   │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│  ┌──────────┐ ┌──────────┐                                     │
│  │🔀 InterAgt│ │📧 Emails │                                     │
│  │   342    │ │   28     │                                     │
│  └──────────┘ └──────────┘                                     │
├─────────────────────────────────────────────────────────────────┤
│  📈 Actividad por Agente — últimas 24h                          │
│  (gráfica de líneas — una línea por agente con distintos colores)│
├─────────────────────────────────────────────────────────────────┤
│  🔴 Errores & Escalaciones — Log viewer filtrado                │
├─────────────────────────────────────────────────────────────────┤
│  🤖 Live Logs — Todos los agentes en tiempo real                │
└─────────────────────────────────────────────────────────────────┘
```

**Filtros disponibles:**
- **Ambiente:** production / staging / development
- **Agente:** All / jarvis / samantha / david / bishop / ... (cada uno por separado)

**Auto-refresh:** cada 30 segundos.

---

### 2. 🔍 NTE por Agente — Drilldown

Seleccionas un agente específico y ves toda su actividad.

```
Filtro: [Agente: Samantha] [Ambiente: production] [Rango: last 7 days]

┌─────────────────────────────────────────────────────────────────┐
│  Samantha (NTE-CX) · samantha@nissienterprise.com               │
├──────────┬──────────┬──────────┬──────────┬────────────────────┤
│ Mensajes │ Leads    │ Emails   │ Escalac. │ Tasa de Resolución │
│ recibidos│ captados │ enviados │ a Michael│ sin escalar        │
│  1,847   │   134    │   312    │    8     │       95.7%        │
├─────────────────────────────────────────────────────────────────┤
│  Timeline de actividad de Samantha                              │
│  (breakdown por event_type: ACTION / DECISION / EMAIL_SENT)     │
├─────────────────────────────────────────────────────────────────┤
│  Últimas decisiones de clasificación de leads                   │
│  HOT: 23  |  WARM: 67  |  COLD: 44                            │
├─────────────────────────────────────────────────────────────────┤
│  Log viewer — todos los logs de Samantha                        │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3. 🔗 NTE Trace Explorer — Seguir un Flujo Completo

La feature más poderosa: dado un `trace_id`, ver todo el viaje de un trabajo a través de múltiples agentes.

```
Buscar trace_id: [a3f9-bc12-4e87-9f1c-d2e3a4b5c6d7]

Timeline del flujo:

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

  Total del flujo: 2h 12m 35s  |  Estado: escalated (pendiente aprobación)
```

**LogQL para buscarlo:**
```
{environment="production"} |= "a3f9-bc12-4e87-9f1c-d2e3a4b5c6d7"
```

---

### 4. 🔐 NTE Seguridad — T-800 Dashboard

Dashboard dedicado exclusivamente a logs de seguridad.

```
┌─────────────────────────────────────────────────────────────────┐
│  🔐 T-800 (NTE-SECURITY) — Security Dashboard                   │
├──────────────┬─────────────────┬──────────────────────────────┤
│ Scans (7d)   │ Vulnerabilidades │ Accesos Azure KV             │
│     28       │    0 críticas   │          847                 │
├─────────────────────────────────────────────────────────────────┤
│  Historial de Security Scans                                    │
│  ✅ 2026-03-29  NTE-SW-142 PR  → PASS (0 vulnerabilidades)     │
│  ✅ 2026-03-28  Deploy v1.2.3  → PASS (0 críticas, 1 low)     │
│  ⚠️  2026-03-27  NTE-SW-139 PR  → WARN (1 medium)              │
├─────────────────────────────────────────────────────────────────┤
│  Accesos a Azure Key Vault — por secreto y agente               │
│  (tabla: secreto | agente | timestamp | estado)                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5. 💼 NTE QuickBooks & Finanzas

```
┌─────────────────────────────────────────────────────────────────┐
│  💼 Actividad Financiera — QuickBooks                           │
├─────────────────────────────────────────────────────────────────┤
│  Últimas operaciones                                            │
│  • 2026-03-29 09:14  TARS → draft invoice $7,500 [PENDIENTE]   │
│  • 2026-03-28 16:30  Jarvis → invoice aprobado por Michael     │
│  • 2026-03-25 11:00  TARS → reminder payment vencido [SENT]    │
├─────────────────────────────────────────────────────────────────┤
│  Todas las operaciones QB requieren aprobación de Michael       │
│  → Las que están en estado PENDIENTE se muestran en rojo        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Consultas LogQL de Referencia

LogQL es el lenguaje de query de Loki. Funciona similar a PromQL pero para logs.

```logql
── Ver todos los logs de un agente ────────────────────────────────
{agent="samantha", environment="production"}

── Ver solo errores de las últimas 24h ────────────────────────────
{environment="production"} |= "ERROR" | json | level = "ERROR"

── Ver todas las escalaciones a Michael ───────────────────────────
{environment="production", event_type="ESCALATION"}

── Seguir un flujo por trace_id ───────────────────────────────────
{environment="production"} |= "a3f9-bc12-4e87-9f1c"

── Ver llamadas a QuickBooks ──────────────────────────────────────
{environment="production", event_type="QB_EVENT"}

── Ver toda la comunicación inter-agente ──────────────────────────
{environment="production", event_type="INTER_AGENT"}

── Ver deployments de Optimus ─────────────────────────────────────
{agent="optimus", event_type="DEPLOY"}

── Contar errores por agente (últimas 6h) ─────────────────────────
sum by (agent) (count_over_time({environment="production", level="ERROR"} [6h]))

── Ver accesos a Azure Key Vault ──────────────────────────────────
{event_type="SECRET_ACCESS"} | json | vault = "nte-keyvault"
```

---

## Alertas de Grafana

Las alertas se configuran en Grafana y notifican a Slack `#nte-alerts` y email de T-800.

| Alerta | Condición | Destino |
|---|---|---|
| **Agente caído** | 0 logs de un agente en > 10 min (horario activo) | `#nte-alerts` + Michael |
| **Error crítico** | Cualquier log con `level=CRITICAL` | `#nte-alerts` inmediato |
| **Tasa de error alta** | > 5 errores/min en cualquier agente | `#nte-alerts` |
| **Escalación financiera** | Cualquier `QB_EVENT` con `status=pending_approval` | Michael DM + `#nte-alerts` |
| **Security scan fallido** | `SECURITY_SCAN` con `result=fail` | `#nte-alerts` + T-800 email |
| **Presupuesto API** | Token API > $400/mes detectado | Michael DM |

---

## Provisioning Automático de Grafana

Cuando el stack arranca por primera vez, Grafana carga automáticamente:
- Datasource de Loki (sin configuración manual)
- Todos los dashboards de `/grafana/dashboards/`
- Contactos de alerta (Slack `#nte-alerts`)

Archivos de provisioning de referencia:

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
      # trace_id clickeable para ver el flujo completo
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

[← Infraestructura](./03-infraestructura.md) | [Volver al inicio](../README.md)
