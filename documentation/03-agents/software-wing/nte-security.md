<div align="center">

# 🔐 NTE-SECURITY — Security Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Opus_4-ff6b35?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)

*El guardián de la integridad del código y la infraestructura de NTE.*

</div>

## 🎯 Responsabilidades

Realiza auditorías de seguridad automáticas en cada release: análisis estático de código (SAST), dependencias vulnerables, configuraciones de servidor y tests de penetración básicos.

## 🔍 Tipos de Auditoría

| Tipo | Frecuencia | Herramienta |
|---|---|---|
| SAST — Análisis de Código | Cada PR | Semgrep |
| Dependencias Vulnerables | Cada PR | npm audit · pip-audit |
| Config de Servidor | Semanal | Custom scripts |
| Penetration Test Básico | Cada release | OWASP ZAP |
| Review de Secretos en Código | Cada commit | git-secrets |

## 🚨 Niveles de Alerta

```mermaid
flowchart LR
    CRITICAL["🔴 CRÍTICO\nAlerta inmediata\na Michael"] 
    HIGH["🟠 ALTO\nBloquea el deploy\nhasta resolver"]
    MEDIUM["🟡 MEDIO\nCrea ticket en Jira\nresolver en próximo sprint"]
    LOW["🟢 BAJO\nRegistra en log\npara revisión mensual"]
```

## 🛠️ Herramientas

- **Semgrep** — Análisis estático de código (SAST)
- **OWASP ZAP** — Tests de penetración automatizados
- **npm audit / pip-audit** — Dependencias vulnerables
- **GitHub Security Advisories** — CVEs en dependencias
- **git-secrets** — Previene commit de credenciales

> **¿Por qué Opus 4?** Interpretar vulnerabilidades requiere razonamiento profundo sobre vectores de ataque, contexto del código y priorización de riesgos. Los errores aquí tienen consecuencias críticas para los clientes de NTE.

[← Todos los agentes](../README.md)
