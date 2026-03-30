<div align="center">

# 🔄 Flujo: Blog Semanal Automatizado
### Del Trend al Tweet en 48 horas

</div>

## Diagrama Secuencial Completo

```mermaid
sequenceDiagram
    participant MAIN as 🧠 Jarvis (NTE-MAIN)
    participant TS as 🔍 Johnny 5 (TREND-SCOUT)
    participant CW as ✍️ C-3PO (COPYWRITER)
    participant M as 👤 Michael
    participant PUB as 🚀 R2-D2 (PUBLISHER)
    participant PROP as 📡 Baymax (PROPAGATOR)
    participant WP as 🌐 WordPress
    participant BUF as 📱 Buffer/RRSS

    Note over MAIN,TS: ⏰ LUNES 2:00 AM EST — INICIO AUTOMÁTICO

    MAIN->>TS: Activar análisis semanal
    TS->>TS: Analiza Google Trends, Semrush, Reddit
    TS->>TS: Filtra por servicios NTE
    TS->>TS: Selecciona Top 2 temas con scoring
    TS->>CW: Briefing: tema, keywords, audiencia, CTA

    Note over CW: Redacción de 2 artículos completos
    CW->>CW: Artículo 1: SEO full, 1200-1800 palabras
    CW->>CW: Artículo 2: SEO full, 1200-1800 palabras
    CW->>WP: POST /wp-json/wp/v2/posts (status: draft)
    CW->>M: 📨 Slack #nte-content con preview links

    Note over M: ⏳ Ventana de aprobación 24-48 horas

    alt ✅ Michael aprueba
        M->>PUB: Reacción ✅ o respuesta "publicar"
        PUB->>PUB: DALL-E genera imagen destacada
        PUB->>WP: PATCH post → status: published + imagen
        WP-->>PUB: URL del artículo publicado
        PUB->>M: ✅ "Artículo publicado: [URL]"
        PUB->>PROP: Trigger con URL + contenido

        Note over PROP: Adaptación para 5 plataformas
        PROP->>PROP: LinkedIn: 300 palabras profesional
        PROP->>PROP: Instagram: caption + 10 hashtags
        PROP->>PROP: Facebook: post comunidad + pregunta
        PROP->>PROP: Twitter/X: hilo 4-5 tweets
        PROP->>PROP: YouTube: guión 60 segundos
        PROP->>BUF: Programa posts escalonados (3-5 días)
        PROP->>M: 📊 Reporte con fechas de publicación

    else 🔄 Michael pide cambios
        M->>CW: "Cambios: [instrucciones]"
        CW->>WP: Actualiza draft con cambios
        CW->>M: 📨 "Draft actualizado — [preview link]"

    else ❌ Michael rechaza
        M->>PUB: "Rechazar artículo X"
        PUB->>WP: DELETE draft
        PUB->>M: "✓ Artículo descartado"

    else ⏰ Sin respuesta 72h
        MAIN->>M: 🔔 Recordatorio en #nte-alerts
        Note over M: Si sigue sin respuesta → archivado
    end
```

## Timeline Típico

| Hora | Evento |
|---|---|
| Lunes 2:00 AM | Johnny 5 (NTE-TREND-SCOUT) inicia análisis |
| Lunes 2:30 AM | Briefing enviado a C-3PO (NTE-COPYWRITER) |
| Lunes 5:00 AM | 2 artículos redactados y subidos como drafts |
| Lunes 7:00 AM | Michael recibe notificación en Slack |
| Lunes/Martes | Michael revisa y aprueba |
| +30 min | Artículo publicado + imagen generada |
| Semana | Posts en RRSS distribuidos escalonadamente |

[← Todos los flujos](./README.md)
