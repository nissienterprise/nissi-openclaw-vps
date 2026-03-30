<div align="center">

# 🎧 Flujo: Atención al Cliente Omnicanal
### Respuesta < 5 Minutos · 24/7 · En Todos los Canales

</div>

```mermaid
flowchart TD
    subgraph CANALES["📡 Canales Entrantes"]
        WA["📱 WhatsApp"] & EM["📧 Email"] & FB["📘 Facebook"] & IG["📸 Instagram"] & CH["💬 Chat Web"] & SMS["📟 SMS"]
    end

    CX["🎧 Samantha (NTE-CX) · Sonnet 4\n< 5 minutos · samantha@nissienterprise.com"]

    subgraph CLASIFICACION["🎯 Clasificación de Intención"]
        Q["💰 Cotización"]
        S["🔧 Soporte Técnico"]
        I["ℹ️ Info General"]
        C["😠 Queja"]
        SP["🗑️ Spam"]
    end

    subgraph ACCION["⚡ Acción Automática"]
        A1["Genera propuesta preliminar (QuickBooks estimado)\n→ pasa a EVA (NTE-LEAD-INTAKE)"]
        A2["Resuelve con base de conocimiento\n→ escala si es complejo"]
        A3["Responde con info de servicios NTE"]
        A4["Registra + alerta INMEDIATA a Michael\nvía #nte-cx"]
        A5["Archiva sin responder"]
    end

    CRM["📋 Registra ticket en Jira (NTE-OPS)\ny lead en CRM"]
    SLACK["💬 #nte-cx\nEscalada si necesaria"]

    CANALES --> CX
    CX --> CLASIFICACION
    Q --> A1
    S --> A2
    I --> A3
    C --> A4
    SP --> A5
    A1 & A2 & A3 & A4 --> CRM
    A4 --> SLACK
```

## Respuestas Tipo por Canal

**WhatsApp Business:**
> "¡Hola [Nombre]! 👋 Soy el asistente de Nissi Technology Enterprises. Recibí tu mensaje sobre [tema detectado]. Para darte la mejor atención, ¿puedes contarme un poco más sobre [pregunta de calificación]? Mientras tanto, aquí tienes información sobre nuestros servicios relacionados: [link]. ¡Un experto de nuestro equipo te contactará muy pronto!"

**Email (desde samantha@nissienterprise.com):**
> Asunto: Re: Tu consulta a Nissi Technology Enterprises
> "Hola [Nombre], gracias por contactarnos. He recibido tu mensaje y lo estoy procesando..."

[← Flujos](./README.md)
