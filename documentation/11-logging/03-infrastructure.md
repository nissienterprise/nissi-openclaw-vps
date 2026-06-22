<div align="center">

# 🖥️ Logging System Infrastructure
### Loki · Promtail · Grafana Configuration

</div>

> **Note:** This document is a design reference. The implementation will take place in Phase 1 of the roadmap.

---

## Docker Compose — Full Stack

Reference file: `workspace/logging/docker-compose.logging.yml`

```yaml
# ── Start: docker-compose -f docker-compose.logging.yml up -d
# ── Stop:  docker-compose -f docker-compose.logging.yml down
# ── Grafana access: SSH tunnel → ssh -L 3000:localhost:3000 openclaw@VPS_IP

version: '3.8'

networks:
  nte-logging:
    name: nte-logging
    driver: bridge
  nte-agents:          # Network shared with the agent containers
    external: true
    name: nte-agents

volumes:
  loki_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /workspace/logs/loki
  grafana_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /workspace/logs/grafana

services:

  loki:
    image: grafana/loki:2.9.0
    container_name: nte-loki
    restart: unless-stopped
    ports:
      - "127.0.0.1:3100:3100"   # Localhost only — never expose externally
    volumes:
      - ./loki-config.yml:/etc/loki/local-config.yaml
      - loki_data:/loki
    command: -config.file=/etc/loki/local-config.yaml
    networks: [nte-logging]
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'

  promtail:
    image: grafana/promtail:2.9.0
    container_name: nte-promtail
    restart: unless-stopped
    volumes:
      - ./promtail-config.yml:/etc/promtail/config.yml
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - /var/run/docker.sock:/var/run/docker.sock
    command: -config.file=/etc/promtail/config.yml
    networks: [nte-logging, nte-agents]
    depends_on: [loki]
    deploy:
      resources:
        limits:
          memory: 128M
          cpus: '0.25'

  grafana:
    image: grafana/grafana:10.2.0
    container_name: nte-grafana
    restart: unless-stopped
    ports:
      - "127.0.0.1:3000:3000"   # Only via SSH tunnel
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
      - ./grafana/dashboards:/var/lib/grafana/dashboards
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD}
      - GF_DEFAULT_THEME=dark
      - GF_ANALYTICS_REPORTING_ENABLED=false
    networks: [nte-logging]
    deploy:
      resources:
        limits:
          memory: 256M
          cpus: '0.5'
```

**Estimated total consumption: ~900 MB RAM** — within the 8 GB VPS budget.

---

## Loki Configuration

Reference file: `workspace/logging/loki-config.yml`

```yaml
auth_enabled: false   # Single-tenant (NTE does not need multi-tenancy)

server:
  http_listen_port: 3100
  log_level: warn

ingester:
  wal:
    enabled: true
    dir: /loki/wal
  lifecycler:
    ring:
      kvstore:
        store: inmemory
      replication_factor: 1
  chunk_idle_period: 1h
  max_chunk_age: 1h
  chunk_target_size: 1048576   # 1 MB per chunk

schema_config:
  configs:
    - from: 2026-01-01
      store: boltdb-shipper
      object_store: filesystem
      schema: v11
      index:
        prefix: loki_index_
        period: 24h              # One index per day

storage_config:
  boltdb_shipper:
    active_index_directory: /loki/boltdb-shipper-active
    cache_location:          /loki/boltdb-shipper-cache
    cache_ttl:               24h
    shared_store:            filesystem
  filesystem:
    directory: /loki/chunks

# ── Log retention ────────────────────────────────────────────
compactor:
  working_directory: /loki/boltdb-shipper-compactor
  shared_store:      filesystem
  retention_enabled: true

limits_config:
  retention_period:       2160h   # 90 days in production
  ingestion_rate_mb:      16
  ingestion_burst_size_mb: 32
  max_query_length:       720h    # Query up to 30 days at a time
  max_entries_limit_per_query: 5000
```

---

## Promtail Configuration

Reference file: `workspace/logging/promtail-config.yml`

Promtail **automatically** detects all Docker containers with the label `nte.agent=true` and assigns them the correct labels in Loki.

```yaml
server:
  http_listen_port: 9080
  log_level: warn

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:

  # ── NTE agents via Docker ─────────────────────────────────────
  - job_name: nte-agents

    docker_sd_configs:
      - host: unix:///var/run/docker.sock
        refresh_interval: 15s
        filters:
          - name: label
            values: ["nte.agent=true"]   # Only containers marked as NTE agents

    relabel_configs:
      # Extract labels from each Docker container → Loki labels
      - source_labels: ['__meta_docker_container_label_nte_agent_name']
        target_label: agent
      - source_labels: ['__meta_docker_container_label_nte_agent_id']
        target_label: agent_id
      - source_labels: ['__meta_docker_container_label_nte_wing']
        target_label: wing
      - source_labels: ['__meta_docker_container_label_nte_environment']
        target_label: environment

    pipeline_stages:
      # Parse the JSON emitted by Pino
      - json:
          expressions:
            level:       level
            event_type:  event_type
            trace_id:    trace_id
            status:      status
      # Convert the extracted fields into Loki labels
      - labels:
          level:
          event_type:
          status:
      # Timestamp from the Pino JSON
      - timestamp:
          source: time
          format: RFC3339Nano

  # ── VPS system logs (Jarvis, outside Docker) ──────────
  - job_name: nte-system-logs
    static_configs:
      - targets: [localhost]
        labels:
          job:        nte-system
          agent:      jarvis
          agent_id:   NTE-MAIN
          wing:       orchestrator
          __path__:   /workspace/logs/*.log
```

---

## Required Docker Labels on Each Agent

Each agent's `Dockerfile` must include these labels so Promtail can detect it:

```dockerfile
# ── REQUIRED in every agent Dockerfile ──────────────────────
LABEL nte.agent="true"
LABEL nte.agent.name="Samantha"          # Character name
LABEL nte.agent.id="NTE-CX"             # Technical ID
LABEL nte.wing="administrativa"          # Wing it belongs to
LABEL nte.environment="${NTE_ENV}"       # Injected on docker run
LABEL nte.email="samantha@nissienterprise.com"
```

| Agent | `nte.agent.name` | `nte.agent.id` | `nte.wing` |
|---|---|---|---|
| Jarvis | Jarvis | NTE-MAIN | orchestrator |
| Samantha | Samantha | NTE-CX | administrative |
| WALL-E | WALL-E | NTE-CONTENT | administrative |
| HAL | HAL | NTE-ANALYTICS | administrative |
| Johnny 5 | Johnny 5 | NTE-TREND-SCOUT | blog |
| C-3PO | C-3PO | NTE-COPYWRITER | blog |
| R2-D2 | R2-D2 | NTE-PUBLISHER | blog |
| Baymax | Baymax | NTE-PROPAGATOR | blog |
| EVA | EVA | NTE-LEAD-INTAKE | leads |
| TARS | TARS | NTE-LEAD-NURTURE | leads |
| David | David | NTE-PM | software |
| Bishop | Bishop | NTE-BACKEND | software |
| Sonny | Sonny | NTE-FRONTEND | software |
| BB-8 | BB-8 | NTE-MOBILE | software |
| CASE | CASE | NTE-DATA | software |
| AVA | AVA | NTE-QA | software |
| Optimus | Optimus | NTE-DEVOPS | software |
| T-800 | T-800 | NTE-SECURITY | software |
| Marvin | Marvin | NTE-DOCS | software |

---

## Startup Script

Reference file: `workspace/logging/setup-logging.sh`

```bash
#!/bin/bash
# Usage: bash setup-logging.sh [development|staging|production]

ENVIRONMENT="${1:-production}"
VAULT="nte-keyvault"

# 1. Create data directories
mkdir -p /workspace/logs/loki /workspace/logs/grafana
chmod 777 /workspace/logs/loki /workspace/logs/grafana

# 2. Get Grafana password from Azure Key Vault
export GRAFANA_ADMIN_PASSWORD=$(az keyvault secret show \
  --name "${ENVIRONMENT}/grafana-admin-password" \
  --vault-name "${VAULT}" \
  --query "value" -o tsv)

# 3. Create Docker networks
docker network create nte-agents  2>/dev/null || true
docker network create nte-logging 2>/dev/null || true

# 4. Start the stack
export NTE_ENV="${ENVIRONMENT}"
docker-compose -f workspace/logging/docker-compose.logging.yml up -d

# 5. Wait until ready
until curl -s http://localhost:3100/ready | grep -q "ready"; do sleep 2; done
until curl -s http://localhost:3000/api/health | grep -q "ok";  do sleep 2; done

echo "✅ Logging stack operational"
echo "📊 Grafana: http://localhost:3000 (via SSH tunnel)"
echo "   ssh -L 3000:localhost:3000 openclaw@YOUR_VPS_IP"
```

---

[← Logging README](./README.md) | [Grafana Dashboards →](./04-grafana.md)
