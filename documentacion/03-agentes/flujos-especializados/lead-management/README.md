<div align="center">

# 🎯 Lead Management Pipeline
### De Extraño a Cliente — Completamente Automatizado

*2 agentes especializados · Operación 24/7 · 3 niveles de clasificación*

</div>

---

## Flujo Completo

```mermaid
flowchart TD
    subgraph CANALES["📥 Canales de Entrada"]
        WF["🌐 Website"] & WA["📱 WhatsApp"] & SM["📘 Social Media"] & CH["💬 Chatbot"] & EM["📧 Email"]
    end

    subgraph INTAKE["📥 NTE-LEAD-INTAKE · Sonnet 4"]
        I1["Normaliza el lead\nen perfil unificado"]
        I2["Respuesta inmediata\n< 5 minutos"]
        I3["Crea registro en CRM"]
    end

    HOT["🔴 HOT\nServicio específico\n+ presupuesto"]
    WARM["🟡 WARM\nInterés general\n+ preguntas"]
    COLD["🔵 COLD\nSolo info\nBrowsing"]

    subgraph NURTURE["🌱 NTE-LEAD-NURTURE · Sonnet 4"]
        N1["🚨 Alerta inmediata\na Michael · Slack"]
        N2["📧 Secuencia 5-touch\n14 días\nEmail + WhatsApp"]
        N3["📚 Secuencia educativa\n3 emails · 30 días\n+ Newsletter"]
        N4["♻️ Re-clasifica\nsegún engagement"]
    end

    MICHAEL["👤 Michael\nContacto directo"] --> CONVERT["💰 Proyecto NTE-PM"]

    CANALES --> I1
    I1 --> I2 & I3
    I1 -->|"Clasifica"| HOT & WARM & COLD
    HOT --> N1 --> MICHAEL --> CONVERT
    WARM --> N2
    COLD --> N3
    N2 & N3 --> N4
    N4 -->|"Lead calienta"| HOT

    style HOT fill:#8B0000,color:#fff
    style WARM fill:#7B6000,color:#fff
    style COLD fill:#003380,color:#fff
```

---

## Clasificación de Leads

### 🔴 HOT Lead — Acción Inmediata (< 15 min)
- Menciona un servicio específico ("necesito una app móvil")
- Tiene un presupuesto definido o timeline claro
- Ya tiene empresa establecida
- Fue referido por un cliente existente

### 🟡 WARM Lead — Nurturing 14 días
- Interés general en los servicios de NTE
- Hace preguntas pero no tiene claridad sobre lo que necesita
- Visitó el website varias veces (si se tiene tracking)
- Descargó un recurso o completó un formulario de contacto

### 🔵 COLD Lead — Educación 30 días
- Solo pidió información general
- No respondió preguntas de calificación
- Solo lee el blog o visita las redes sociales
- Muy temprano en su proceso de decisión

---

## Canales Monitoreados

| Canal | API | Tiempo de Respuesta |
|---|---|---|
| Website Forms | Webhook | < 2 min |
| WhatsApp Business | Twilio / Meta API | < 5 min |
| Facebook Messenger | Meta API | < 5 min |
| Instagram DMs | Meta API | < 5 min |
| Chat Web (Crisp) | Crisp Webhook | < 2 min |
| Email | Gmail API | < 10 min |

---

[← Todos los agentes](../../README.md) | [NTE-LEAD-INTAKE →](./nte-lead-intake.md)
