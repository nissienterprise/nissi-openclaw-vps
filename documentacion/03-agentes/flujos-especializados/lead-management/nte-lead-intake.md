<div align="center">

# 📥 NTE-LEAD-INTAKE
### Lead Intake Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Frecuencia](https://img.shields.io/badge/Frecuencia-24/7_Continuo-4a90d9?style=flat-square)

*El primer filtro. Captura, clasifica y responde en menos de 5 minutos.*

</div>

## 🎯 Qué hace

Opera 24/7 escuchando todos los canales de entrada de NTE. Cuando detecta un lead potencial, lo normaliza en un perfil unificado, lo clasifica por temperatura, crea el registro en el CRM y envía una respuesta personalizada inmediata.

## 📋 Perfil Unificado del Lead

```json
{
  "lead_id": "NTE-LEAD-2026-001",
  "timestamp": "2026-03-28T14:32:00Z",
  "channel": "whatsapp",
  "contact": {
    "name": "Ana García",
    "phone": "+1-305-555-0123",
    "email": "ana@empresa.com",
    "company": "García Dental Group",
    "location": "Miami, FL"
  },
  "intent": {
    "service_interest": "website_development",
    "budget_range": "$2000-$5000",
    "timeline": "2 months",
    "urgency": "medium"
  },
  "classification": "WARM",
  "original_message": "Hola, busco información sobre páginas web para mi consultorio dental",
  "response_sent": true,
  "crm_id": "HS-12345",
  "assigned_to": "NTE-LEAD-NURTURE"
}
```

## 💬 Respuestas Inmediatas por Tipo

**Lead HOT:** Respuesta personalizada + "Un representante de NTE se comunicará contigo en los próximos 15 minutos" → Alerta inmediata a Michael

**Lead WARM:** Respuesta con 2-3 preguntas de calificación + mini-presentación de NTE relevante al servicio mencionado

**Lead COLD:** Respuesta con recursos educativos relevantes + invitación a conocer más sobre NTE

## 🛠️ Herramientas

- **Twilio API** — WhatsApp + SMS
- **Gmail API** — Email entrante
- **Meta Webhooks** — Facebook + Instagram
- **Crisp Webhooks** — Chat web
- **HubSpot CRM API** — Registro de leads

[← Lead Management](./README.md) | [NTE-LEAD-NURTURE →](./nte-lead-nurture.md)
