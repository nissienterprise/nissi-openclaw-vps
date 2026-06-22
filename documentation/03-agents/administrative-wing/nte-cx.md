<div align="center">

# 🎧 NTE-CX
### Customer Experience Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Frecuencia](https://img.shields.io/badge/Frecuencia-24/7_Continuo-4a90d9?style=flat-square)

*El primer punto de contacto de NTE con el mundo. Nunca duerme.*

</div>

---

## 🎯 Responsabilidades

NTE-CX es el guardián de la experiencia del cliente. Responde en menos de **5 minutos** en todos los canales, mantiene la voz de NTE (Fe, Integridad, Excelencia) y sabe exactamente cuándo escalar.

---

## 📡 Canales Monitoreados

```mermaid
flowchart LR
    WA["📱 WhatsApp Business\n(Twilio API)"] --> CX
    EM["📧 Email\n(Gmail API)"] --> CX
    FB["📘 Facebook Messenger\n(Meta API)"] --> CX
    IG["📸 Instagram DMs\n(Meta API)"] --> CX
    CH["💬 Chat Web\n(Crisp API)"] --> CX
    FM["📝 Formularios Web\n(Webhook)"] --> CX
    SMS["📟 SMS\n(Twilio)"] --> CX

    CX["🎧 NTE-CX\nClasifica & Responde"]

    CX -->|"Proyecto detectado"| LI["📥 NTE-LEAD-INTAKE"]
    CX -->|"Soporte técnico complejo"| PM["🗂️ NTE-PM"]
    CX -->|"Escalada urgente"| SLACK["💬 #nte-cx"]
```

---

## 🔀 Flujo de Clasificación

| Intención detectada | Acción | Tiempo |
|---|---|---|
| Cotización de servicio | Genera propuesta preliminar + pasa a NTE-LEAD-INTAKE | < 5 min |
| Soporte técnico | Responde con pasos básicos; escala a NTE-PM si es complejo | < 5 min |
| Información general | Responde usando base de conocimiento de servicios NTE | < 2 min |
| Queja de cliente activo | Registra + alerta inmediata a Michael vía #nte-cx | Inmediato |
| Spam / irrelevante | Archiva y no responde | Automático |

---

## 🛠️ Herramientas & APIs

- **Twilio** — WhatsApp Business + SMS
- **Gmail API** — Email corporativo
- **Meta API** — Facebook + Instagram
- **Crisp** — Chat en vivo del website
- **CRM (HubSpot)** — Registro de todas las interacciones

---

[← NTE-MAIN](../nte-main.md) | [NTE-CONTENT →](./nte-content.md)
