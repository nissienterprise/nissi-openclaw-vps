<div align="center">

# 🔐 NTE-SECURITY — Security Agent

![Model](https://img.shields.io/badge/Model-Claude_Opus_4-ff6b35?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)

*The guardian of NTE's code and infrastructure integrity.*

</div>

## 🎯 Responsibilities

Performs automatic security audits on every release: static code analysis (SAST), vulnerable dependencies, server configurations, and basic penetration tests.

## 🔍 Audit Types

| Type | Frequency | Tool |
|---|---|---|
| SAST — Code Analysis | Every PR | Semgrep |
| Vulnerable Dependencies | Every PR | npm audit · pip-audit |
| Server Configuration | Weekly | Custom scripts |
| Basic Penetration Test | Every release | OWASP ZAP |
| Secrets-in-Code Review | Every commit | git-secrets |

## 🚨 Alert Levels

```mermaid
flowchart LR
    CRITICAL["🔴 CRITICAL\nImmediate alert\nto Michael"] 
    HIGH["🟠 HIGH\nBlocks the deploy\nuntil resolved"]
    MEDIUM["🟡 MEDIUM\nCreates a Jira ticket\nresolve in next sprint"]
    LOW["🟢 LOW\nLogs for\nmonthly review"]
```

## 🛠️ Tools

- **Semgrep** — Static code analysis (SAST)
- **OWASP ZAP** — Automated penetration tests
- **npm audit / pip-audit** — Vulnerable dependencies
- **GitHub Security Advisories** — CVEs in dependencies
- **git-secrets** — Prevents committing credentials

> **Why Opus 4?** Interpreting vulnerabilities requires deep reasoning about attack vectors, code context, and risk prioritization. Mistakes here have critical consequences for NTE's clients.

[← All agents](../README.md)
