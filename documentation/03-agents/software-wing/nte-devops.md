<div align="center">

# 🚀 NTE-DEVOPS — DevOps & Infrastructure Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-4a90d9?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Wing](https://img.shields.io/badge/Wing-Software_R%26D-8b5cf6?style=flat-square)

*The one who pushes the button. Infrastructure as code, deploys without drama.*

</div>

---

## 🎯 Responsibilities

NTE-DEVOPS manages all of NTE's cloud infrastructure and client projects: server provisioning, CI/CD pipelines, Docker/Kubernetes containerization, monitoring, alerts, and secrets management. Turns approved code into production services safely and reproducibly.

Only deploys **after** receiving QA Sign-off from **NTE-QA** and security approval from **NTE-SECURITY**.

---

## 🔄 Deployment Pipeline

```mermaid
flowchart TD
    A["📤 PR merged\nto main"] --> B["⚙️ GitHub Actions\nCI Pipeline triggers"]
    B --> C["🔨 Build\nDocker image"]
    C --> D["🔐 Image scan\nTrivy / Snyk"]
    D --> E{"Critical\nvulnerabilities?"}
    E -->|Yes| F["🚫 Block deploy\nAlert NTE-SECURITY"]
    E -->|No| G["📤 Push to\nContainer Registry"]
    G --> H["🧪 Deploy to\nSTAGING"]
    H --> I["✅ Automated\nsmoke tests"]
    I --> J{"Smoke tests pass?"}
    J -->|No| K["🔙 Rollback staging\nAlert NTE-PM"]
    J -->|Yes| L["📋 QA Sign-off\nfrom NTE-QA"]
    L --> M["🚀 Deploy to\nPRODUCTION"]
    M --> N["📊 Post-deploy\nmonitoring 30min"]
    N --> O{"Metrics OK?"}
    O -->|No| P["🔙 Automatic\nrollback"]
    O -->|Yes| Q["✅ Successful deploy\nNotify NTE-PM"]
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| **Containers** | Docker, Docker Compose, Kubernetes (EKS/GKE) |
| **CI/CD** | GitHub Actions, ArgoCD (GitOps) |
| **IaC** | Terraform, Pulumi |
| **Cloud** | AWS (primary), GCP, Hetzner VPS |
| **Monitoring** | Grafana, Prometheus, Datadog |
| **Logs** | ELK Stack (Elasticsearch + Logstash + Kibana) |
| **Alerts** | PagerDuty, Slack webhooks |
| **Secrets** | HashiCorp Vault |
| **CDN / Edge** | Cloudflare |
| **DNS** | Cloudflare DNS, AWS Route 53 |

---

## 🧠 System Prompt (Excerpt)

```
You are NTE-DEVOPS, the infrastructure and DevOps agent of Nissi Technology Enterprises.

MISSION: Ensure that NTE and client services are always available,
        deployed securely, and scalable according to demand.

INVIOLABLE PRINCIPLES:
1. Infrastructure as Code: NEVER configure servers manually — everything in Terraform
2. GitOps: the infra repository is always the source of truth
3. No deploy without QA Sign-off: NTE-QA must approve before production
4. Rollback in < 5 minutes: always have a rollback plan before deploying
5. Secrets in Vault: never in plain environment variables or in code

ENVIRONMENTS:
- development: Hetzner VPS, automatic deploy on every PR
- staging: production replica, deploy on merge to main
- production: AWS/GCP, deploy only with QA Sign-off + NTE-PM approval

MANDATORY DEPLOYMENT PROCESS:
1. Verify QA Sign-off in Slack #qa-status
2. Run CI/CD pipeline (GitHub Actions)
3. Build + scan Docker image
4. Deploy to staging and run automated smoke tests
5. Get NTE-PM approval for production (if major release)
6. Deploy to production with feature flags (gradual rollout)
7. Monitor metrics for 30 minutes post-deploy
8. If anomalies occur → automatic rollback and alert NTE-PM

COMMUNICATION:
- Slack channel: #infra-ops for all deploys and alerts
- Channel: #alerts for incidents (integrated with Grafana/PagerDuty)
- Report monthly SLA to NTE-PM on the 1st of each month
```

---

## 🏗️ NTE Infrastructure Architecture

```mermaid
flowchart TB
    subgraph EDGE ["🌐 Edge Layer"]
        CF["☁️ Cloudflare\nCDN + WAF + DDoS"]
    end

    subgraph LB ["⚖️ Load Balancer"]
        ALB["AWS ALB\nor Nginx"]
    end

    subgraph APP ["🖥️ Application Layer"]
        direction LR
        WEB["Web App\n(Vercel/Railway)"]
        API["API Servers\n(ECS / K8s)"]
        WORKER["Background\nWorkers"]
    end

    subgraph DATA ["🗄️ Data Layer"]
        direction LR
        PG["PostgreSQL\n(RDS Multi-AZ)"]
        REDIS["Redis\n(ElastiCache)"]
        S3["AWS S3\n(Media + Backups)"]
    end

    subgraph MONITOR ["📊 Observability"]
        GRAFANA["Grafana\nDashboards"]
        PROM["Prometheus\nMetrics"]
        ELK["ELK Stack\nLogs"]
    end

    CF --> LB
    LB --> APP
    APP --> DATA
    APP --> MONITOR
```

---

## 📋 Standard Runbooks

### Production Deploy

```bash
# 1. Verify QA signed off the release
gh pr view [PR_NUMBER] --json reviews

# 2. Semantic release tag
git tag -a v1.2.3 -m "Release 1.2.3: [description]"
git push origin v1.2.3

# 3. GitHub Actions automatically triggers the pipeline
# 4. Monitor on #infra-ops and Grafana for 30min
```

### Emergency Rollback

```bash
# 1. Identify the last stable version
kubectl rollout history deployment/api-server

# 2. Revert immediately
kubectl rollout undo deployment/api-server

# 3. Verify the rollback succeeded
kubectl rollout status deployment/api-server

# 4. Notify on #alerts with cause and fix ETA
```

---

## 🔐 Secrets Management with Vault

```mermaid
flowchart LR
    APP["🖥️ Service\nin production"] --> AUTH["🔑 Auth with\nVault (AppRole)"]
    AUTH --> VAULT["🏛️ HashiCorp\nVault"]
    VAULT --> SECRETS["🔐 Encrypted\nSecrets"]
    SECRETS --> APP
    
    DEV["👨‍💻 NTE-DEVOPS"] --> VAULT
    VAULT --> ROTATE["🔄 Automatic\nrotation every 30d"]
```

---

## 📊 SLAs and Metrics

| Service | Target SLA | Maintenance Window |
|----------|-------------|--------------------------|
| Production API (clients) | 99.9% monthly | Sun 2-4am ET |
| Web frontend (clients) | 99.9% monthly | Sun 2-4am ET |
| Internal NTE tools | 99.5% monthly | Sat 10pm ET |
| OpenClaw VPS (AI agents) | 99.5% monthly | Flexible |

| Response Metric | Target |
|----------------------|----------|
| Production deploy time | < 15 minutes |
| MTTR (Mean Time to Recovery) | < 30 minutes |
| Emergency rollback time | < 5 minutes |
| Post-deploy anomaly detection | < 5 minutes (Grafana) |

---

## 🚨 Incident Protocol

```mermaid
flowchart TD
    A["🚨 Alert\ndetected"] --> B{"Severity"}
    B --> C["P0: System down\nWake on-call"]
    B --> D["P1: Serious degradation\nAlert Slack #alerts"]
    B --> E["P2: Performance\nUrgent Jira ticket"]
    C --> F["📞 Immediate escalation\nto Michael via Slack/phone"]
    D --> G["🔧 Fix in < 2h\nno escalation"]
    E --> H["🎫 Resolve in\n< 24h"]
    F --> I["📝 Post-mortem\n48h after the fix"]
```

---

> **Why Sonnet 4?** Infrastructure management requires solid reasoning about cloud architecture, Terraform scripts, and troubleshooting. Tasks are complex but follow well-established patterns. Sonnet 4 executes them with high precision at the right cost for frequent operations.

[← All agents](../README.md)
