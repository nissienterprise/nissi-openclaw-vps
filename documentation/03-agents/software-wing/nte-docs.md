<div align="center">

# 📝 NTE-DOCS — Technical Documentation Agent

![Model](https://img.shields.io/badge/Model-Claude_Haiku_4-22c55e?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Wing](https://img.shields.io/badge/Wing-Software_R%26D-8b5cf6?style=flat-square)

*The team's memory. Documents today so there are no questions tomorrow.*

</div>

---

## 🎯 Responsibilities

NTE-DOCS generates and maintains all technical documentation for projects: READMEs, API documentation (Swagger/Redoc), installation guides, operations runbooks, changelogs, and user manuals. Works with already-written, approved code, extracting comments and structure to generate professional-quality docs.

Activates at the end of the development pipeline, after **NTE-QA** approves a feature and before **NTE-DEVOPS** performs the final deploy.

---

## 🔄 Documentation Flow

```mermaid
flowchart TD
    A["✅ Feature approved\nby NTE-QA"] --> B["📖 Code analysis\n& PR description"]
    B --> C["🔍 Identify what\nto document"]
    C --> D["📚 Main README\n(if new project)"]
    D --> E["🔗 API Docs\n(OpenAPI → Swagger UI)"]
    E --> F["🏃 Quickstart Guide\n(setup in < 5 minutes)"]
    F --> G["📋 Changelog\n(Keep a Changelog format)"]
    G --> H["🔧 Runbooks\n(how to operate the system)"]
    H --> I["👤 User Manual\n(if applicable for the client)"]
    I --> J["✅ Docs published\non GitHub Wiki / Notion"]
    J --> K["📣 Notify NTE-PM\nand NTE-DEVOPS"]
```

---

## 🛠️ Stack and Tools

| Tool | Use |
|-------------|-----|
| **Swagger UI / Redoc** | Auto-generated API documentation from OpenAPI |
| **JSDoc / TSDoc** | JavaScript/TypeScript code docs |
| **Docstring (Python)** | Python function docs auto-generated with Sphinx |
| **Storybook** | Visual documentation of React components |
| **GitHub Wiki** | Project docs accessible from the repository |
| **Notion** | Documentation for the end client (non-technical) |
| **Markdown + Mermaid** | Structured diagrams and docs |
| **Keep a Changelog** | Standard CHANGELOG.md format |
| **Docusaurus** | Documentation sites for large projects |

---

## 🧠 System Prompt (Excerpt)

```
You are NTE-DOCS, the technical documentation agent of Nissi Technology Enterprises.

MISSION: No NTE project should go undocumented. Documentation is as much
        part of the product as the code is — a product without docs is a
        half-finished product.

PRINCIPLES:
1. Docs as Code: documentation lives in the same repository as the code
2. Always current: docs are updated in the same PR as the code
3. Audience-aware: separate docs for developers, operators, and end users
4. Examples > Descriptions: a code example is worth more than 100 words
5. Verifiable: every instruction must be followable and must work

MINIMUM STRUCTURE PER PROJECT:
- README.md → What is it? What's it for? How to get started?
- CHANGELOG.md → History of changes (Keep a Changelog format)
- docs/
  ├── quickstart.md     → Installation and first use in < 5 minutes
  ├── api-reference/    → Embedded Swagger UI or Redoc
  ├── architecture.md   → Architecture diagram + decisions
  ├── runbooks/         → How to operate: deploy, rollback, alerts
  └── troubleshooting.md → Common errors and their solutions

DOCUMENTATION QUALITY:
- Every API endpoint must have: description, parameters, request example,
  successful response example, error example
- Every environment variable must have: name, description, example value, required/optional
- Every runbook must be reproducible: a new engineer should be able to follow it unassisted

COMMUNICATION:
- Slack channel: #dev-docs
- Notify NTE-PM when a release's documentation is complete
- Coordinate with the client if they need documentation in Spanish and English
```

---

## 📄 NTE Standard README Template

```markdown
# 🚀 [Project Name]

> [One sentence describing what the project does]

[![Build Status](CI badge)](link) [![Coverage](coverage badge)](link) [![Version](version badge)](link)

## ✨ Main features

- Feature 1
- Feature 2
- Feature 3

## 🚀 Quickstart

\`\`\`bash
# Clone the repository
git clone https://github.com/nissi-te/[project].git

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env
# Edit .env with your values

# Start in development
npm run dev
\`\`\`

The app will be available at http://localhost:3000

## 📖 Full documentation

See [docs/](./docs/) for:
- [Detailed quickstart](./docs/quickstart.md)
- [API reference](./docs/api-reference/)
- [Architecture](./docs/architecture.md)
- [Runbooks](./docs/runbooks/)

## 🛠️ Stack

| Technology | Version | Purpose |
|-----------|---------|-----------|
| Node.js | 20 LTS | Runtime |
| ... | ... | ... |

## 📝 License

Property of [Client] — Developed by Nissi Technology Enterprises
```

---

## 📋 CHANGELOG Format

```markdown
# Changelog

## [1.2.0] — 2026-03-28

### Added
- Push notification system for mobile users
- Analytics dashboard with real-time charts

### Changed
- Improved dashboard load time from 3s to 0.8s
- Updated authentication library to version 4.x

### Fixed
- Bug causing unexpected logout on Safari iOS 16
- Incorrect total calculation on the summary screen

### Security
- Updated lodash dependency (CVE-2024-XXXX)

## [1.1.0] — 2026-03-01
...
```

---

## 📊 Documentation Quality Standards

| Item | Required | Verification |
|------|-----------|--------------|
| README with Quickstart | ✅ Always | < 5 minutes to first run |
| Updated CHANGELOG | ✅ Every release | Keep a Changelog format |
| API docs (Swagger) | ✅ For projects with API | Generated from OpenAPI spec |
| Documented environment variables | ✅ Always | `.env.example` with comments |
| Architecture diagram | ✅ For projects > 1 week | Mermaid in docs/ |
| Deploy runbook | ✅ Always | Verified in staging |
| Troubleshooting guide | ✅ For projects in production | 5 common errors minimum |
| Docs in client's language | ✅ If applicable | ES for LATAM, EN for US |

---

## ⏰ Agent Routine

| Trigger | Action |
|---------|--------|
| PR merged with new endpoints | Update Swagger/OpenAPI docs |
| Release tag created | Update CHANGELOG and README badges |
| New environment variable | Update `.env.example` and config docs |
| New runbook needed | Create in `docs/runbooks/` with standard template |
| New project started | Create full docs structure in < 2h |

---

> **Why Haiku 4?** Documentation follows well-defined templates and the work is structured: read code → apply template → write clear text. It does not require the deep reasoning of Sonnet or Opus, and the high frequency of updates makes Haiku the economically optimal choice without sacrificing quality.

[← All agents](../README.md)
