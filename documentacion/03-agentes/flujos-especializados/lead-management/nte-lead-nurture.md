<div align="center">

# 🌱 NTE-LEAD-NURTURE
### Lead Nurturing Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Frecuencia](https://img.shields.io/badge/Frecuencia-24/7_Continuo-4a90d9?style=flat-square)

*Convierte el interés en conversación y la conversación en clientes.*

</div>

## 🎯 Qué hace

Recibe los leads clasificados de NTE-LEAD-INTAKE y los trabaja con secuencias de seguimiento personalizadas según su temperatura. Monitorea el engagement y re-clasifica automáticamente.

## 📧 Secuencias de Nurturing

### 🔴 HOT Lead — Alerta Inmediata

```
Slack → #nte-leads:

🔴 *HOT LEAD DETECTADO*

👤 *Nombre:* Ana García — García Dental Group
📱 *Canal:* WhatsApp
💬 *Mensaje:* "Necesito una página web profesional para mi clínica dental, tengo presupuesto de $3,000-$5,000 y lo necesito en 6 semanas"
🎯 *Servicio:* Web Development — Sitio Corporativo
💰 *Budget estimado:* $3,000-$5,000
⏰ *Timeline:* 6 semanas

*Próximo paso sugerido:* Llamada de discovery (30 min)
[Ver perfil completo en CRM →]
```

### 🟡 WARM Lead — Secuencia 5 Toques (14 días)

| Toque | Día | Canal | Contenido |
|---|---|---|---|
| 1 | Día 1 | Email | Bienvenida + caso de estudio relevante |
| 2 | Día 3 | WhatsApp | "¿Pudiste revisar la información?" + pregunta de calificación |
| 3 | Día 7 | Email | Artículo de blog relevante al servicio de interés |
| 4 | Día 10 | WhatsApp | Invitación a llamada de consulta gratuita (15 min) |
| 5 | Día 14 | Email | "Última oportunidad" + oferta especial o testimonio |

### 🔵 COLD Lead — Secuencia Educativa (30 días)

| Email | Día | Tema |
|---|---|---|
| 1 | Día 2 | "Bienvenido a NTE — La guía que necesitas para [tema]" |
| 2 | Día 10 | "5 errores que cometen las empresas en [área de interés]" |
| 3 | Día 25 | "¿Listo para el siguiente paso? Casos de éxito NTE" |

## ♻️ Re-clasificación Automática

NTE-LEAD-NURTURE monitorea:
- **Apertura de emails** → Si abre 3+ emails consecutivos: COLD → WARM
- **Respuesta a WhatsApp** → Si responde con preguntas específicas: WARM → HOT
- **Clic en "Agendar llamada"** → Inmediatamente HOT + alerta a Michael
- **Sin actividad 30 días** → Archivo con nota de reactivación futura

## 🛠️ Herramientas

- **SendGrid API** — Secuencias de email automatizadas
- **Twilio API** — Follow-up por WhatsApp
- **HubSpot CRM** — Tracking de todo el ciclo del lead
- **Google Calendar API** — Agendamiento automático de llamadas

[← NTE-LEAD-INTAKE](./nte-lead-intake.md) | [Volver al inicio](../../../../README.md)
