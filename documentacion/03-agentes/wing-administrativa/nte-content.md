<div align="center">

# ✍️ NTE-CONTENT
### Content & Marketing Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Frecuencia](https://img.shields.io/badge/Frecuencia-Diaria-4a90d9?style=flat-square)

*La voz digital de NTE. Genera, programa y distribuye contenido alineado con la marca.*

</div>

---

## 🎯 Responsabilidades

Ejecuta el **calendario editorial mensual** de NTE de forma autónoma. Coordina con NTE-TREND-SCOUT para los artículos del blog y gestiona el contenido evergreen de las redes sociales.

---

## 📅 Calendario Editorial

| Canal | Frecuencia | Tipo de contenido |
|---|---|---|
| Blog WordPress | 2 artículos/semana | SEO · Educativo · Casos de uso |
| LinkedIn | 5 posts/semana | Profesional · Thought leadership |
| Instagram | 1 post + 3 stories/día | Visual · Tips · Behind the scenes |
| Facebook | 3 posts/semana | Comunidad · Noticias · Testimonios |
| Twitter/X | 2 tweets/día | Rápido · Tips · Noticias tech |
| Newsletter | 1 email/mes | Resumen + novedades NTE |

---

## 🔧 Pipeline de Contenido

```mermaid
flowchart LR
    TS["🔍 NTE-TREND-SCOUT\nTemas trending"] --> CW["✍️ NTE-COPYWRITER\nArtículo completo"]
    CW --> PUB["🚀 NTE-PUBLISHER\nPublica en WP"]
    PUB --> PROP["📡 NTE-PROPAGATOR\nAdapta para RRSS"]
    
    CONTENT["✍️ NTE-CONTENT\nCoordina todo"] -.->|"Supervisa"| TS & CW & PUB & PROP
```

---

## 🛠️ Herramientas & APIs

- **WordPress REST API** — Publicación del blog
- **Buffer API** — Programación de redes sociales
- **SendGrid / Mailchimp** — Newsletter mensual
- **DALL-E / Stable Diffusion** — Imágenes para contenido
- **Semrush API** — Keywords y análisis SEO

---

[← NTE-CX](./nte-cx.md) | [NTE-ANALYTICS →](./nte-analytics.md)
