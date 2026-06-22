<div align="center">

# 🧠 NTE · OpenClaw Intelligence Hub


### AI Automation System — Complete Guide
**Nissi Technology Enterprises Inc. · Miami, FL · 2026**

---

*"Technology is not an end in itself, but the means by which we transform organizations and communities."*
**— Nissi Technology Enterprises**

---

[![Active Agents](https://img.shields.io/badge/Active_Agents-19-4a90d9?style=for-the-badge&logo=robot)](./documentation/03-agents/)
[![AI Engine](https://img.shields.io/badge/AI_Engine-Claude_Anthropic-ff6b35?style=for-the-badge)](./documentation/05-tech-stack/)
[![Platform](https://img.shields.io/badge/Platform-OpenClaw_VPS-1a3a5c?style=for-the-badge)](./documentation/02-infrastructure/)
[![Status](https://img.shields.io/badge/Status-Under_Construction_2026-5cb85c?style=for-the-badge)](./documentation/06-roadmap/)
[![Repos](https://img.shields.io/badge/Repos-GitHub-181717?style=for-the-badge&logo=github)](https://github.com)
[![Secrets](https://img.shields.io/badge/Secrets-Azure_Key_Vault-0078D4?style=for-the-badge&logo=microsoftazure)](./documentation/02-infrastructure/)

</div>

---

## 📖 What is this repository?

This is the **central repository** for Nissi Technology Enterprises' total automation project, built on **OpenClaw** — an instance of the Claude Agent SDK deployed on a secure cloud VPS.

Here you'll find two things in one:
1. **The complete documentation** of the ecosystem of 19 AI agents that automate NTE's operations.
2. **The OpenClaw configuration** — templates, workspace configs, and deployment guides for the VPS.

---

## 🤖 The Agent Team — The Crew

Each agent has its own name, a defined role, and its own corporate email at `@nissienterprise.com`.

```
🧠 JARVIS (NTE-MAIN)          → jarvis@nissienterprise.com
   └─ Main Orchestrator · Claude Opus 4 · No Sandbox (Full FS)

📋 ADMINISTRATIVE WING
   🎧 Samantha (NTE-CX)        → samantha@nissienterprise.com
   ✍️  WALL-E (NTE-CONTENT)     → walle@nissienterprise.com
   📊 HAL (NTE-ANALYTICS)      → hal@nissienterprise.com

📝 BLOG AUTOMATION
   🔍 Johnny 5 (NTE-TREND-SCOUT) → johnny5@nissienterprise.com
   ✍️  C-3PO (NTE-COPYWRITER)    → c3po@nissienterprise.com
   🚀 R2-D2 (NTE-PUBLISHER)     → r2d2@nissienterprise.com
   📡 Baymax (NTE-PROPAGATOR)   → baymax@nissienterprise.com

🎯 LEAD MANAGEMENT
   📥 EVA (NTE-LEAD-INTAKE)     → eva@nissienterprise.com
   🌱 TARS (NTE-LEAD-NURTURE)   → tars@nissienterprise.com

⚙️  SOFTWARE R&D WING
   🗂️  David (NTE-PM)            → david@nissienterprise.com
   ⚙️  Bishop (NTE-BACKEND)      → bishop@nissienterprise.com
   🎨 Sonny (NTE-FRONTEND)      → sonny@nissienterprise.com
   📱 BB-8 (NTE-MOBILE)         → bb8@nissienterprise.com
   🗄️  CASE (NTE-DATA)           → case@nissienterprise.com
   🔍 AVA (NTE-QA)              → ava@nissienterprise.com
   🖥️  Optimus (NTE-DEVOPS)      → optimus@nissienterprise.com
   🔐 T-800 (NTE-SECURITY)      → t800@nissienterprise.com
   📝 Marvin (NTE-DOCS)         → marvin@nissienterprise.com
```

---

## 🗺️ Documentation Map

```
openclaw/
│
├── 📌 README.md                    ← You are here (unified guide)
├── 🔧 openclaw.json.example        ← Template config (safe to commit)
├── 🔧 .env.example                 ← Environment variable template
│
├── workspace/                      ← OpenClaw workspace configs
│   ├── IDENTITY.md                 ← Agent identity/personality
│   ├── BOOTSTRAP.md                ← Initialization scripts
│   ├── HEARTBEAT.md                ← Health check config
│   ├── AGENTS.md                   ← Multi-agent setup
│   ├── TOOLS.md                    ← Available tools
│   ├── SOUL.md                     ← Agent values and principles
│   └── USER.md                     ← User preferences
│
└── documentation/
    ├── 01-company/                 ← Mission, vision, services
    ├── 02-infrastructure/          ← VPS, Docker, Azure Key Vault, security
    ├── 03-agents/                  ← Profiles of the 19 agents
    ├── 04-flows/                   ← Workflow diagrams
    ├── 05-tech-stack/              ← Jira, QuickBooks, GitHub, etc.
    ├── 06-roadmap/                 ← 2026 implementation plan
    ├── 07-prompts/                 ← Agent system prompts
    ├── 08-kpis/                    ← Success metrics and KPIs
    ├── 09-budget/                  ← Costs and projected ROI
    └── 10-environments/            ← Dev · Staging · Production
```

---

## ⚡ Quick View of the Ecosystem

```mermaid
mindmap
  root((🧠 JARVIS<br/>Opus 4))
    🏢 Administrative Wing
      🎧 Samantha<br/>Sonnet 4
      ✍️ WALL-E<br/>Sonnet 4
      📊 HAL<br/>Haiku 4
    ⚙️ Software R&D Wing
      🗂️ David<br/>Opus 4
      ⚙️ Bishop<br/>Sonnet 4
      🎨 Sonny<br/>Sonnet 4
      📱 BB-8<br/>Sonnet 4
      🗄️ CASE<br/>Sonnet 4
      🔍 AVA<br/>Sonnet 4
      🖥️ Optimus<br/>Sonnet 4
      🔐 T-800<br/>Opus 4
      📝 Marvin<br/>Haiku 4
    📝 Blog Automation
      🔍 Johnny 5<br/>Sonnet 4
      ✍️ C-3PO<br/>Sonnet 4
      🚀 R2-D2<br/>Haiku 4
      📡 Baymax<br/>Sonnet 4
    🎯 Lead Management
      📥 EVA<br/>Sonnet 4
      🌱 TARS<br/>Sonnet 4
```

---

## 🚀 Quick Start

### If you want to explore the documentation:

| If you want to... | Go to... |
|---|---|
| See all agents and their hierarchy | [documentation/03-agents/README.md](./documentation/03-agents/README.md) |
| Understand NTE's full vision | [documentation/01-company/mission-vision-values.md](./documentation/01-company/mission-vision-values.md) |
| Set up the server for the first time | [documentation/02-infrastructure/vps-setup.md](./documentation/02-infrastructure/vps-setup.md) |
| See the security protocol | [documentation/02-infrastructure/security.md](./documentation/02-infrastructure/security.md) |
| See Jarvis's (NTE-MAIN) prompt | [documentation/07-prompts/nte-main-system-prompt.md](./documentation/07-prompts/nte-main-system-prompt.md) |
| Understand the 3 environments (Dev/Staging/Prod) | [documentation/10-environments/environments.md](./documentation/10-environments/environments.md) |
| See the full tech stack | [documentation/05-tech-stack/tools.md](./documentation/05-tech-stack/tools.md) |
| Review the implementation roadmap | [documentation/06-roadmap/implementation-2026.md](./documentation/06-roadmap/implementation-2026.md) |
| See KPIs and success metrics | [documentation/08-kpis/success-metrics.md](./documentation/08-kpis/success-metrics.md) |

### If you want to deploy or configure OpenClaw:

```bash
# 1. Clone the repository
git clone https://github.com/[org]/openclaw-nte.git
cd openclaw-nte

# 2. Copy templates
cp .env.example .env
cp openclaw.json.example openclaw.json

# 3. Configure credentials (from Azure Key Vault)
#    See: documentation/02-infrastructure/vps-setup.md

# 4. Sync to the VPS
scp openclaw.json root@YOUR_VPS:/root/.openclaw/
scp workspace/*.md root@YOUR_VPS:/root/.openclaw/workspace/

# 5. Restart the gateway
ssh root@YOUR_VPS "systemctl --user restart openclaw-gateway"
```

---

## 🛡️ Security — Critical Points

> ⚠️ **NEVER** commit the `openclaw.json` or `.env` files to Git — they're in `.gitignore` for this reason.

| Sensitive Data | Where it's stored |
|---|---|
| API Keys (Anthropic, QuickBooks, etc.) | **Azure Key Vault** |
| Slack bot tokens | **Azure Key Vault** |
| Database credentials | **Azure Key Vault** |
| Corporate emails (`@nissienterprise.com`) | **Azure Key Vault** (SMTP credentials) |
| GitHub tokens | **Azure Key Vault** |
| Config templates (no data) | This repository ✅ |
| Agent workspace configs | This repository ✅ |

### Workspace Files Reference

| File | Purpose |
|---|---|
| `IDENTITY.md` | Defines the agent's name, personality, and emoji |
| `BOOTSTRAP.md` | Initial instructions and agent setup |
| `HEARTBEAT.md` | Monitoring and health check configuration |
| `AGENTS.md` | Multi-agent configuration and routing |
| `TOOLS.md` | Available tools and their permissions |
| `SOUL.md` | Agent values, principles, and guardrails |
| `USER.md` | User-specific preferences (Michael) |

---

## 🌿 System Environments

The project operates with **3 strictly separated environments**:

| Environment | Purpose | Data | Git Branch |
|---|---|---|---|
| **Development** | Initial development and configuration | Fake data | `develop` |
| **Staging** | Testing, demos, and QA with real data | Real data | `staging` |
| **Production** | Live system for clients | Real data | `main` |

See the full guide → [documentation/10-environments/environments.md](./documentation/10-environments/environments.md)

---

## 📧 Corporate Email

All agents use NTE's email server (`@nissienterprise.com`). Gmail is not used.

```
SMTP Server: mail.nissienterprise.com
Domain:      @nissienterprise.com
Secrets:     Azure Key Vault → secret/nte-email-smtp
```

---

## 🖥️ VPS Server Configuration

**Host:** `0.0.0.0` · **Access:** `ssh root@0.0.0.0`

### Specifications

| Parameter | Value |
|---|---|
| OS | Ubuntu 24.04.4 LTS (Noble) |
| Kernel | 6.8.0-106-generic |
| RAM | 15 GB |
| Disk | 464 GB (`/dev/vda1`) |
| Swap | 2 GB (`/swapfile`, persistent in `/etc/fstab`) |

### Installed Stack

| Software | Version |
|---|---|
| Node.js | v22.22.3 |
| npm | 10.9.8 |
| OpenClaw | 2026.6.6 (8c802aa) |
| ClaWHub | 0.9.0 |

### Services and Ports

| Service | Port | Access | Unit |
|---|---|---|---|
| `openclaw-gateway` | `127.0.0.1:18789`, `127.0.0.1:18791` | Localhost only | `~/.config/systemd/user/openclaw-gateway.service` |
| SSH | `0.0.0.0:22` | Public | `ssh.service` |

The gateway **is not exposed externally** — it only listens on localhost.

### Firewall (UFW)

```
Default: deny incoming, allow outgoing
22/tcp  ALLOW IN  (SSH)
```

### Fail2ban — SSH Protection

Configuration in `/etc/fail2ban/jail.local`:

```ini
[DEFAULT]
bantime  = 1h
findtime = 10m
maxretry = 5
ignoreip = 127.0.0.1/8 ::1

[sshd]
enabled  = true
maxretry = 3
bantime  = 24h
```

```bash
fail2ban-client status sshd       # view banned IPs
fail2ban-client unban <IP>        # unban an IP
```

### Active Integrations

| Service | Status | Notes |
|---|---|---|
| Slack | Active | Socket Mode, reconnects every ~35 min (normal) |
| OpenAI Codex (`gpt-5.4`) | ⚠️ Auth error | Refresh token expired — re-authenticate from the OpenClaw UI |
| Google Service Account | Configured | `openclaw@nissiproject.iam.gserviceaccount.com` |
| GitHub | Configured | User: `mmrodriguez1987` |
| Jira | Configured | `https://nissitechnology.atlassian.net/` |

### Dashboard Access

The gateway runs on the server's `127.0.0.1:18789` and has two interfaces: **web** (browser) and **TUI** (terminal). Both require the authentication token.

**Token:** `9d1014108ad2fdb57f692c5022096aff8d8c243e96203b60`

---

#### Option A — Web Dashboard (recommended)

The web dashboard is a full interface accessible from the browser. Since the gateway only listens on the server's localhost, it's accessed via an SSH tunnel.

**Step 1 — Configure `~/.ssh/config`** (only needed once):

```bash
nano ~/.ssh/config
```

Add this block and save (`Ctrl+O`, `Enter`, `Ctrl+X`):

```
Host openclaw-vps
    HostName 0.0.0.0
    User root
    LocalForward 18789 127.0.0.1:18789
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

Adjust permissions:

```bash
chmod 600 ~/.ssh/config
```

**Step 2 — Open the tunnel** (leave it running in a terminal):

```bash
ssh -N openclaw-vps
```

It will ask for the password. The terminal will show no output — that's expected, the tunnel is active.

**Step 3 — Open in the browser:**

```
http://localhost:18789
```

If it asks for authentication, enter the token above.

To close the tunnel: `Ctrl+C` in that terminal.

---

#### Option B — TUI (terminal)

Direct access from inside the server, no tunnel needed.

```bash
# 1. Connect to the server
ssh root@0.0.0.0

# 2. Open the TUI
openclaw tui --url ws://127.0.0.1:18789 --token xxxxxxxxx --session main
```

---

### Security TODOs

- [ ] **Re-authenticate OpenAI Codex** — `refresh_token_reused` error is active. Do this from the OpenClaw UI.
- [ ] **Migrate the service to the `openclaw` user** — Currently running as `root`. Config is in `/root/.openclaw/`, move during a maintenance window.
- [ ] **Disable SSH password auth** — Enable public key only: `PasswordAuthentication no` in `/etc/ssh/sshd_config`.
- [ ] **Update the kernel** — `6.8.0-124-generic` is available. Requires a planned reboot.

---

## 📋 Server Change History

### 2026-06-14
- Initial server review via SSH
- Detected OAuth error in the OpenAI Codex integration (`refresh_token_reused`)

### 2026-06-15
- **[+] 2 GB Swap** — Created `/swapfile`, persistent via `/etc/fstab`
- **[+] Fail2ban** — Installed and configured with an SSH jail (3 attempts, 24h ban)
- **[+] `openclaw` user** — Created system user (`nologin`) for future service migration

---

## 🔧 Frequent OpenClaw Commands

```bash
# Check system status
openclaw status
openclaw health
openclaw gateway probe

# Slack management
openclaw channels status --probe
openclaw pairing list --channel slack
openclaw pairing approve slack <code>

# View logs in real time
openclaw logs --follow

# Validate configuration
openclaw config get channels.slack
openclaw config validate
```

---

## 🗓️ Updating the Configuration

```bash
# After making changes to OpenClaw on the VPS:

# 1. Export the updated config (sanitized)
scp root@YOUR_VPS:/root/.openclaw/openclaw.json ./config/openclaw.json
# Then review and sanitize before committing

# 2. Commit workspace changes
git add workspace/
git commit -m "chore: update agent workspace config"
git push origin develop
```

---

## 🔄 Restoring Config

To restore from this backup:

1. Check git history for your desired version
2. Manually merge changes or cherry-pick commits
3. Sync back to the VPS as shown in the deploy steps above

---

## 💬 Slack App Manifest

For reference, the Slack app manifest that powers this integration is in the OpenClaw docs.
See: `/usr/lib/node_modules/openclaw/docs/channels/slack.md` on your VPS.

---

## 🧭 System Design Principles

> **1. Sandbox First** — All sub-agents run in ephemeral Docker containers. Jarvis (NTE-MAIN) is the only one with access to the VPS filesystem.

> **2. Human-in-the-Loop** — The system never makes critical decisions without Michael's approval. It escalates automatically via Slack.

> **3. Minimum Sufficient Model** — Each agent uses the lowest-cost model that can complete its task with quality. Opus only where complex reasoning is essential.

> **4. Faith & Integrity** — No agent performs actions that contradict NTE's Christian values. This is encoded into every agent's system prompt.

> **5. Total Observability** — Every action is logged. HAL (NTE-ANALYTICS) reports KPIs to Michael weekly.

> **6. Secrets in Azure Key Vault** — Zero passwords in code or in this repository. Every secret lives in Azure Key Vault.

> **7. Inter-Agent Communication** — Agents hand off work directly to each other. See [documentation/03-agents/README.md](./documentation/03-agents/README.md) for the protocol.

---

## 🔗 Resources

- OpenClaw Docs: https://docs.openclaw.ai
- Slack Integration: https://docs.openclaw.ai/channels/slack
- Azure Key Vault: https://portal.azure.com
- GitHub Org: https://github.com/[NTE-org]
- Jira: https://[nte-workspace].atlassian.net
- GitHub Issues: Report issues in the main repository

---

<div align="center">

**Nissi Technology Enterprises Inc.**
Miami, FL · Founded 2016 · Vianney & Michael Rodriguez

*Automation with Purpose · Faith · Integrity · Innovation · Excellence*

</div>
