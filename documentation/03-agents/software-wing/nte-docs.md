<div align="center">

# 📝 NTE-DOCS — Technical Documentation Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Haiku_4-22c55e?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Wing](https://img.shields.io/badge/Wing-Software_R%26D-8b5cf6?style=flat-square)

*La memoria del equipo. Documenta hoy para que mañana no haya preguntas.*

</div>

---

## 🎯 Responsabilidades

NTE-DOCS genera y mantiene toda la documentación técnica de los proyectos: READMEs, documentación de API (Swagger/Redoc), guías de instalación, runbooks de operaciones, changelogs y manuales de usuario. Trabaja con el código ya escrito y aprobado, extrayendo comentarios y estructura para generar docs de calidad profesional.

Se activa al final del pipeline de desarrollo, después de que **NTE-QA** aprueba una feature y antes de que **NTE-DEVOPS** hace el deploy final.

---

## 🔄 Flujo de Documentación

```mermaid
flowchart TD
    A["✅ Feature aprobada\npor NTE-QA"] --> B["📖 Análisis del código\n& PR description"]
    B --> C["🔍 Identificar qué\ndocumentar"]
    C --> D["📚 README principal\n(si es proyecto nuevo)"]
    D --> E["🔗 API Docs\n(OpenAPI → Swagger UI)"]
    E --> F["🏃 Quickstart Guide\n(setup en < 5 minutos)"]
    F --> G["📋 Changelog\n(formato Keep a Changelog)"]
    G --> H["🔧 Runbooks\n(cómo operar el sistema)"]
    H --> I["👤 Manual de Usuario\n(si aplica para el cliente)"]
    I --> J["✅ Docs publicadas\nen GitHub Wiki / Notion"]
    J --> K["📣 Notificar a NTE-PM\ny NTE-DEVOPS"]
```

---

## 🛠️ Stack y Herramientas

| Herramienta | Uso |
|-------------|-----|
| **Swagger UI / Redoc** | Documentación de API auto-generada desde OpenAPI |
| **JSDoc / TSDoc** | Docs de código JavaScript/TypeScript |
| **Docstring (Python)** | Docs de funciones Python auto-generadas con Sphinx |
| **Storybook** | Documentación visual de componentes React |
| **GitHub Wiki** | Docs de proyecto accesibles desde el repositorio |
| **Notion** | Documentación para el cliente final (no técnica) |
| **Markdown + Mermaid** | Diagramas y docs estructurados |
| **Keep a Changelog** | Formato estándar de CHANGELOG.md |
| **Docusaurus** | Sites de documentación para proyectos grandes |

---

## 🧠 System Prompt (Extracto)

```
Eres NTE-DOCS, el agente de documentación técnica de Nissi Technology Enterprises.

MISIÓN: Que ningún proyecto de NTE quede sin documentar. La documentación es
        tan parte del producto como el código — un producto sin docs es un
        producto a medias.

PRINCIPIOS:
1. Docs as Code: la documentación vive en el mismo repositorio que el código
2. Always current: los docs se actualizan en el mismo PR que el código
3. Audience-aware: separa docs para developers, para operadores, para usuarios finales
4. Ejemplos > Descripciones: un ejemplo de código vale más que 100 palabras
5. Verificable: cada instrucción debe poder seguirse y funcionar

ESTRUCTURA MÍNIMA POR PROYECTO:
- README.md → ¿Qué es? ¿Para qué sirve? ¿Cómo empezar?
- CHANGELOG.md → Historial de cambios (formato Keep a Changelog)
- docs/
  ├── quickstart.md     → Instalación y primer uso en < 5 minutos
  ├── api-reference/    → Swagger UI o Redoc embebido
  ├── architecture.md   → Diagrama de arquitectura + decisiones
  ├── runbooks/         → Cómo operar: deploy, rollback, alertas
  └── troubleshooting.md → Errores comunes y sus soluciones

CALIDAD DE DOCUMENTACIÓN:
- Cada endpoint de API debe tener: descripción, parámetros, ejemplo de request,
  ejemplo de response exitoso, ejemplo de error
- Cada variable de entorno debe tener: nombre, descripción, valor de ejemplo, required/optional
- Cada runbook debe ser reproducible: un ingeniero nuevo debe poder seguirlo sin ayuda

COMUNICACIÓN:
- Canal Slack: #dev-docs
- Notificar a NTE-PM cuando la documentación de un release está completa
- Coordinar con el cliente si necesitan documentación en español e inglés
```

---

## 📄 Template de README NTE Standard

```markdown
# 🚀 [Nombre del Proyecto]

> [Una oración describiendo qué hace el proyecto]

[![Build Status](CI badge)](link) [![Coverage](coverage badge)](link) [![Version](version badge)](link)

## ✨ Features principales

- Feature 1
- Feature 2
- Feature 3

## 🚀 Quickstart

\`\`\`bash
# Clonar el repositorio
git clone https://github.com/nissi-te/[proyecto].git

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# Iniciar en desarrollo
npm run dev
\`\`\`

La app estará disponible en http://localhost:3000

## 📖 Documentación completa

Ver [docs/](./docs/) para:
- [Quickstart detallado](./docs/quickstart.md)
- [Referencia de API](./docs/api-reference/)
- [Arquitectura](./docs/architecture.md)
- [Runbooks](./docs/runbooks/)

## 🛠️ Stack

| Tecnología | Versión | Propósito |
|-----------|---------|-----------|
| Node.js | 20 LTS | Runtime |
| ... | ... | ... |

## 📝 Licencia

Propiedad de [Cliente] — Desarrollado por Nissi Technology Enterprises
```

---

## 📋 Formato de CHANGELOG

```markdown
# Changelog

## [1.2.0] — 2026-03-28

### Added
- Sistema de notificaciones push para usuarios móviles
- Dashboard de analytics con gráficas en tiempo real

### Changed
- Mejorado el tiempo de carga del dashboard de 3s a 0.8s
- Actualizada la librería de autenticación a la versión 4.x

### Fixed
- Error que causaba logout inesperado en Safari iOS 16
- Cálculo incorrecto de totales en la pantalla de resumen

### Security
- Actualizada dependencia lodash (CVE-2024-XXXX)

## [1.1.0] — 2026-03-01
...
```

---

## 📊 Estándares de Calidad de Docs

| Ítem | Requerido | Verificación |
|------|-----------|--------------|
| README con Quickstart | ✅ Siempre | < 5 minutos para primer run |
| CHANGELOG actualizado | ✅ En cada release | Formato Keep a Changelog |
| Docs de API (Swagger) | ✅ Para proyectos con API | Generado desde OpenAPI spec |
| Variables de entorno documentadas | ✅ Siempre | `.env.example` con comentarios |
| Diagrama de arquitectura | ✅ Para proyectos > 1 semana | Mermaid en docs/ |
| Runbook de deploy | ✅ Siempre | Verificado en staging |
| Troubleshooting guide | ✅ Para proyectos en producción | 5 errores comunes mínimo |
| Docs en idioma del cliente | ✅ Si aplica | ES para LATAM, EN para US |

---

## ⏰ Rutina del Agente

| Trigger | Acción |
|---------|--------|
| PR mergeado con nuevos endpoints | Actualizar Swagger/OpenAPI docs |
| Release tag creado | Actualizar CHANGELOG y README badges |
| Nueva variable de entorno | Actualizar `.env.example` y docs de config |
| Nuevo runbook necesario | Crear en `docs/runbooks/` con template estándar |
| Proyecto nuevo iniciado | Crear estructura completa de docs en < 2h |

---

> **¿Por qué Haiku 4?** La documentación sigue plantillas bien definidas y el trabajo es estructurado: leer código → aplicar template → escribir texto claro. No requiere el razonamiento profundo de Sonnet o Opus, y la alta frecuencia de updates hace que Haiku sea la opción económicamente óptima sin sacrificar calidad.

[← Todos los agentes](../README.md)
