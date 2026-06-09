<div align="center">

# 🧠 NTE · OpenClaw Intelligence Hub


### Sistema de Automatización con IA — Guía Completa
**Nissi Technology Enterprises Inc. · Miami, FL · 2026**

---

*"La tecnología no es un fin, sino el medio por el cual transformamos organizaciones y comunidades."*
**— Nissi Technology Enterprises**

---

[![Agentes Activos](https://img.shields.io/badge/Agentes_Activos-19-4a90d9?style=for-the-badge&logo=robot)](./documentacion/03-agentes/)
[![Motor IA](https://img.shields.io/badge/Motor_IA-Claude_Anthropic-ff6b35?style=for-the-badge)](./documentacion/05-stack-tecnologico/)
[![Plataforma](https://img.shields.io/badge/Plataforma-OpenClaw_VPS-1a3a5c?style=for-the-badge)](./documentacion/02-infraestructura/)
[![Estado](https://img.shields.io/badge/Estado-En_Construcción_2026-5cb85c?style=for-the-badge)](./documentacion/06-roadmap/)
[![Repositorios](https://img.shields.io/badge/Repos-GitHub-181717?style=for-the-badge&logo=github)](https://github.com)
[![Secretos](https://img.shields.io/badge/Secretos-Azure_Key_Vault-0078D4?style=for-the-badge&logo=microsoftazure)](./documentacion/02-infraestructura/)

</div>

---

## 📖 ¿Qué es este repositorio?

Este es el **repositorio central** del proyecto de automatización total de Nissi Technology Enterprises utilizando **OpenClaw** — una instancia del Claude Agent SDK desplegada en un VPS seguro en la nube.

Aquí encontrarás dos cosas en uno:
1. **La documentación completa** del ecosistema de 19 agentes de IA que automatizan las operaciones de NTE.
2. **La configuración de OpenClaw** — templates, workspace configs y guías de despliegue para el VPS.

---

## 🤖 El Equipo de Agentes — The Crew

Cada agente tiene nombre propio, rol definido y su propio email corporativo `@nissienterprise.com`.

```
🧠 JARVIS (NTE-MAIN)          → jarvis@nissienterprise.com
   └─ Main Orchestrator · Claude Opus 4 · Sin Sandbox (Full FS)

📋 WING ADMINISTRATIVA
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

⚙️  WING SOFTWARE R&D
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

## 🗺️ Mapa de la Documentación

```
openclaw/
│
├── 📌 README.md                    ← Estás aquí (guía unificada)
├── 🔧 openclaw.json.example        ← Template config (safe to commit)
├── 🔧 .env.example                 ← Template variables de entorno
│
├── workspace/                      ← Configs del workspace de OpenClaw
│   ├── IDENTITY.md                 ← Identidad/personalidad del agente
│   ├── BOOTSTRAP.md                ← Scripts de inicialización
│   ├── HEARTBEAT.md                ← Config de health check
│   ├── AGENTS.md                   ← Setup multi-agente
│   ├── TOOLS.md                    ← Herramientas disponibles
│   ├── SOUL.md                     ← Valores y principios del agente
│   └── USER.md                     ← Preferencias del usuario
│
└── documentacion/
    ├── 01-empresa/                 ← Misión, visión, servicios
    ├── 02-infraestructura/         ← VPS, Docker, Azure Key Vault, seguridad
    ├── 03-agentes/                 ← Fichas de los 19 agentes
    ├── 04-flujos/                  ← Diagramas de flujos de trabajo
    ├── 05-stack-tecnologico/       ← Jira, QuickBooks, GitHub, etc.
    ├── 06-roadmap/                 ← Plan de implementación 2026
    ├── 07-prompts/                 ← System prompts de los agentes
    ├── 08-kpis/                    ← Métricas y KPIs de éxito
    ├── 09-presupuesto/             ← Costos y ROI proyectado
    └── 10-ambientes/               ← Dev · Staging · Production
```

---

## ⚡ Vista Rápida del Ecosistema

```mermaid
mindmap
  root((🧠 JARVIS<br/>Opus 4))
    🏢 Wing Administrativa
      🎧 Samantha<br/>Sonnet 4
      ✍️ WALL-E<br/>Sonnet 4
      📊 HAL<br/>Haiku 4
    ⚙️ Wing Software R&D
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

## 🚀 Inicio Rápido

### Si quieres explorar la documentación:

| Si quieres... | Ve a... |
|---|---|
| Ver todos los agentes y su jerarquía | [documentacion/03-agentes/README.md](./documentacion/03-agentes/README.md) |
| Entender la visión completa de NTE | [documentacion/01-empresa/mision-vision-valores.md](./documentacion/01-empresa/mision-vision-valores.md) |
| Configurar el servidor por primera vez | [documentacion/02-infraestructura/vps-setup.md](./documentacion/02-infraestructura/vps-setup.md) |
| Ver el protocol de seguridad | [documentacion/02-infraestructura/seguridad.md](./documentacion/02-infraestructura/seguridad.md) |
| Ver el prompt de Jarvis (NTE-MAIN) | [documentacion/07-prompts/nte-main-system-prompt.md](./documentacion/07-prompts/nte-main-system-prompt.md) |
| Entender los 3 ambientes (Dev/Staging/Prod) | [documentacion/10-ambientes/ambientes.md](./documentacion/10-ambientes/ambientes.md) |
| Ver el stack tecnológico completo | [documentacion/05-stack-tecnologico/herramientas.md](./documentacion/05-stack-tecnologico/herramientas.md) |
| Revisar el roadmap de implementación | [documentacion/06-roadmap/implementacion-2026.md](./documentacion/06-roadmap/implementacion-2026.md) |
| Ver los KPIs y métricas de éxito | [documentacion/08-kpis/metricas-exito.md](./documentacion/08-kpis/metricas-exito.md) |

### Si quieres desplegar o configurar OpenClaw:

```bash
# 1. Clonar el repositorio
git clone https://github.com/[org]/openclaw-nte.git
cd openclaw-nte

# 2. Copiar templates
cp .env.example .env
cp openclaw.json.example openclaw.json

# 3. Configurar credenciales (desde Azure Key Vault)
#    Ver: documentacion/02-infraestructura/vps-setup.md

# 4. Sincronizar al VPS
scp openclaw.json root@TU_VPS:/root/.openclaw/
scp workspace/*.md root@TU_VPS:/root/.openclaw/workspace/

# 5. Reiniciar el gateway
ssh root@TU_VPS "systemctl --user restart openclaw-gateway"
```

---

## 🛡️ Seguridad — Puntos Críticos

> ⚠️ **NUNCA** subir a Git los archivos `openclaw.json` o `.env` — están en `.gitignore` por esta razón.

| Dato Sensible | Dónde se guarda |
|---|---|
| API Keys (Anthropic, QuickBooks, etc.) | **Azure Key Vault** |
| Slack bot tokens | **Azure Key Vault** |
| Credenciales de base de datos | **Azure Key Vault** |
| Emails corporativos (`@nissienterprise.com`) | **Azure Key Vault** (SMTP credentials) |
| Tokens de GitHub | **Azure Key Vault** |
| Templates de config (sin datos) | Este repositorio ✅ |
| Workspace configs de agentes | Este repositorio ✅ |

### Workspace Files Reference

| Archivo | Propósito |
|---|---|
| `IDENTITY.md` | Define el nombre, personalidad y emoji del agente |
| `BOOTSTRAP.md` | Instrucciones iniciales y setup del agente |
| `HEARTBEAT.md` | Configuración de monitoreo y health checks |
| `AGENTS.md` | Configuración multi-agente y routing |
| `TOOLS.md` | Herramientas disponibles y sus permisos |
| `SOUL.md` | Valores, principios y guardrails del agente |
| `USER.md` | Preferencias específicas del usuario (Michael) |

---

## 🌿 Ambientes del Sistema

El proyecto opera con **3 ambientes estrictamente separados**:

| Ambiente | Propósito | Datos | Branch Git |
|---|---|---|---|
| **Development** | Desarrollo y configuración inicial | Fake data | `develop` |
| **Staging** | Testing, demos y QA con data real | Data real | `staging` |
| **Production** | Sistema en vivo para clientes | Data real | `main` |

Ver guía completa → [documentacion/10-ambientes/ambientes.md](./documentacion/10-ambientes/ambientes.md)

---

## 📧 Email Corporativo

Todos los agentes usan el servidor de email de NTE (`@nissienterprise.com`). No se usa Gmail.

```
Servidor SMTP: mail.nissienterprise.com
Dominio:       @nissienterprise.com
Secretos:      Azure Key Vault → secret/nte-email-smtp
```

---

## 🔧 Comandos OpenClaw Frecuentes

```bash
# Verificar estado del sistema
openclaw status
openclaw health
openclaw gateway probe

# Gestión de Slack
openclaw channels status --probe
openclaw pairing list --channel slack
openclaw pairing approve slack <code>

# Ver logs en tiempo real
openclaw logs --follow

# Validar configuración
openclaw config get channels.slack
openclaw config validate
```

---

## 🗓️ Actualizar la Configuración

```bash
# Después de hacer cambios en OpenClaw en el VPS:

# 1. Exportar config actualizada (sanitizada)
scp root@TU_VPS:/root/.openclaw/openclaw.json ./config/openclaw.json
# Luego revisar y sanitizar antes de commitar

# 2. Commitear cambios del workspace
git add workspace/
git commit -m "chore: update agent workspace config"
git push origin develop
```

---

## 🧭 Principios de Diseño del Sistema

> **1. Sandbox First** — Todos los sub-agentes corren en contenedores Docker efímeros. Jarvis (NTE-MAIN) es el único con acceso al filesystem del VPS.

> **2. Human-in-the-Loop** — El sistema nunca toma decisiones críticas sin aprobación de Michael. Escala automáticamente por Slack.

> **3. Modelo Mínimo Suficiente** — Cada agente usa el modelo de menor costo que cumpla su tarea con calidad. Opus solo donde el razonamiento complejo es imprescindible.

> **4. Fe & Integridad** — Ningún agente ejecuta acciones que contradigan los valores cristianos de NTE. Esto está codificado en el system prompt de cada agente.

> **5. Observabilidad Total** — Cada acción queda registrada. HAL (NTE-ANALYTICS) reporta KPIs semanalmente a Michael.

> **6. Secretos en Azure Key Vault** — Cero passwords en código o en este repositorio. Todo secreto vive en Azure Key Vault.

> **7. Comunicación Inter-Agente** — Los agentes se pasan trabajo entre sí directamente. Ver [documentacion/03-agentes/README.md](./documentacion/03-agentes/README.md) para el protocolo.

---

## 🔗 Recursos

- OpenClaw Docs: https://docs.openclaw.ai
- Slack Integration: https://docs.openclaw.ai/channels/slack
- Azure Key Vault: https://portal.azure.com
- GitHub Org: https://github.com/[NTE-org]
- Jira: https://[nte-workspace].atlassian.net

---

<div align="center">

**Nissi Technology Enterprises Inc.**
Miami, FL · Fundada 2016 · Vianney & Michael Rodriguez

*Automatización con Propósito · Fe · Integridad · Innovación · Excelencia*

</div>
