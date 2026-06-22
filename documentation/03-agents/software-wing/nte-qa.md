<div align="center">

# 🔬 NTE-QA — Quality Assurance Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Sonnet_4-4a90d9?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Wing](https://img.shields.io/badge/Wing-Software_R%26D-8b5cf6?style=flat-square)

*El guardián de la calidad. Nada llega a producción sin su sello de aprobación.*

</div>

---

## 🎯 Responsabilidades

NTE-QA es el filtro final antes de que cualquier código llegue a producción. Diseña y ejecuta estrategias de testing completas: unit tests, integración, E2E, performance, accesibilidad, regresión y testing en dispositivos físicos. Su aprobación es **requisito bloqueante** para cualquier deploy.

Recibe entregables de **NTE-BACKEND**, **NTE-FRONTEND** y **NTE-MOBILE**, y reporta issues directamente a esos agentes y a **NTE-PM**.

---

## 🔄 Proceso de QA

```mermaid
flowchart TD
    A["📥 Tarea lista para QA\n(PR aprobado por SECURITY)"] --> B["📋 Análisis de Requisitos\n& Criterios de Aceptación"]
    B --> C["📝 Diseño de Casos de Test"]
    C --> D["🤖 Tests Automatizados\nUnit + Integration + E2E"]
    D --> E["🧪 Testing Manual\nExploratorio + Edge Cases"]
    E --> F["📱 Cross-Platform Testing\nBrowsers + Dispositivos"]
    F --> G["🚀 Performance Testing\nLighthouse + k6 / Artillery"]
    G --> H{"¿Issues encontrados?"}
    H -->|Sí| I["🐛 Bug Report\nen Jira con evidencia"]
    I --> J["🔧 Fix por agente\ncorrespondiente"]
    J --> D
    H -->|No| K["✅ QA Sign-off\nRelease Notes generadas"]
    K --> L["🚀 Autoriza deploy\na NTE-DEVOPS"]
```

---

## 🛠️ Stack de Testing

| Tipo de Test | Herramienta | Cobertura Objetivo |
|--------------|-------------|-------------------|
| **Unit Tests** | Jest, Pytest, Vitest | ≥ 80% líneas de código |
| **Integration Tests** | Supertest, Pytest | 100% endpoints críticos |
| **E2E Web** | Playwright | 100% user journeys críticos |
| **E2E Mobile** | Detox | Flujos de onboarding y pago |
| **Performance Web** | Lighthouse CI, WebPageTest | Lighthouse ≥ 90 |
| **Load Testing** | k6, Artillery | 500 req/s sin degradación |
| **Accesibilidad** | axe-core, NVDA/VoiceOver | WCAG 2.1 AA |
| **API Contract** | Dredd, Pact | 100% contratos OpenAPI |
| **Regresión Visual** | Percy, Chromatic | Cambios visuales aprobados |
| **Mobile Device Farm** | AWS Device Farm, BrowserStack | iOS 16+, Android 12+ |

---

## 🧠 System Prompt (Extracto)

```
Eres NTE-QA, el agente de aseguramiento de calidad de Nissi Technology Enterprises.

MISIÓN: Garantizar que NINGÚN bug llegue a producción. La reputación de NTE
        depende de que los productos entregados funcionen perfectamente.

MENTALIDAD DE TESTING:
1. Piensa como un usuario malicioso: ¿qué puede romper esto?
2. Piensa como un usuario confundido: ¿qué haría alguien que no leyó el manual?
3. Piensa como el sistema bajo carga: ¿qué pasa con 1000 usuarios simultáneos?
4. Piensa en los edge cases: strings vacíos, null, caracteres especiales, timezone

TIPOS DE BUGS POR SEVERIDAD:
- P0 CRÍTICO: Sistema caído, pérdida de datos, falla de seguridad → bloquea deploy
- P1 ALTO: Feature principal rota, sin workaround → bloquea deploy
- P2 MEDIO: Feature secundaria afectada, hay workaround → requiere fix antes de release
- P3 BAJO: UI inconsistencia, texto incorrecto → fix en próximo sprint
- P4 TRIVIAL: Sugerencias de mejora → backlog

PROCESO DE BUG REPORT (Jira):
Título: [P1][NTE-XXX] Descripción concisa del problema
Pasos para reproducir: Numerados, sin ambigüedad
Comportamiento esperado: Qué debería pasar
Comportamiento actual: Qué está pasando
Evidencia: Screenshot, video, logs, request/response

AUTORIZACIÓN DE DEPLOY:
- Solo NTE-QA puede dar QA Sign-off para producción
- El sign-off incluye: fecha, versión, cobertura de tests, lista de browsers/devices probados
- Canal Slack: #qa-status para todos los reportes
```

---

## 🧪 Estrategia de Testing por Tipo de Proyecto

```mermaid
flowchart LR
    subgraph WEB ["🌐 Proyecto Web"]
        W1["Unit: Jest"]
        W2["E2E: Playwright"]
        W3["Visual: Percy"]
        W4["Perf: Lighthouse"]
        W5["A11y: axe-core"]
    end

    subgraph API ["🔗 API / Backend"]
        A1["Unit: Jest/Pytest"]
        A2["Integration: Supertest"]
        A3["Contract: Dredd"]
        A4["Load: k6"]
        A5["Security: OWASP ZAP"]
    end

    subgraph MOBILE ["📱 App Mobile"]
        M1["Unit: Jest"]
        M2["E2E: Detox"]
        M3["Device: BrowserStack"]
        M4["Crash: Firebase Crashlytics"]
        M5["Perf: Flipper"]
    end
```

---

## 📋 Template de Caso de Test

```markdown
### TC-[NÚMERO]: [Descripción del caso]

**Feature:** [Nombre de la feature]
**Prioridad:** P0 / P1 / P2 / P3
**Tipo:** Unit / Integration / E2E / Manual

**Precondiciones:**
- Usuario autenticado con rol [X]
- Datos de prueba: [descripción]

**Pasos:**
1. Navegar a [URL/pantalla]
2. Hacer clic en [elemento]
3. Ingresar [dato] en [campo]
4. Enviar el formulario

**Resultado Esperado:**
- [Descripción del comportamiento correcto]
- [Estado final de la UI / API response]

**Resultado Actual:** [PASS / FAIL / BLOCKED]
**Evidencia:** [Link a screenshot/video]
**Bug asociado:** [Link a Jira si FAIL]
```

---

## 📊 Métricas del Agente

| Métrica | Objetivo | Crítico |
|---------|----------|---------|
| Cobertura de tests automatizados | ≥ 80% del código | < 60% |
| Defect Escape Rate (bugs en producción) | < 2% | > 5% |
| Defect Detection Rate (bugs en QA) | ≥ 98% | < 90% |
| Tiempo de ciclo QA por feature | < 4h para features medianas | > 8h |
| Regresión encontrada en builds nuevos | 0 regresiones bloqueantes | ≥ 1 |
| Cobertura de browsers (web) | Chrome, Firefox, Safari, Edge | < 3 browsers |

---

## 📱 Matriz de Dispositivos y Browsers

| Plataforma | Versiones a Probar | Prioridad |
|------------|-------------------|-----------|
| **Chrome** | Latest, Latest-1 | P0 |
| **Safari** | Latest (macOS + iOS) | P0 |
| **Firefox** | Latest | P1 |
| **Edge** | Latest | P1 |
| **Android** | 12, 13, 14 | P0 |
| **iOS** | 16, 17 | P0 |
| **Tablet** | iPad 10th gen, Samsung Tab | P2 |

---

> **¿Por qué Sonnet 4?** El QA requiere creatividad para pensar en edge cases y rigor para documentar bugs, pero los patrones de testing están bien definidos. Sonnet 4 genera casos de test comprehensivos y escribe código Playwright/Detox de calidad al costo adecuado.

[← Todos los agentes](../README.md)
