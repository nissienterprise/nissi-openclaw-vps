<div align="center">

# ✍️ NTE-COPYWRITER
### Content Writer Agent

![Modelo](https://img.shields.io/badge/Modelo-Claude_Sonnet_4-cc7700?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)

</div>

## 🎯 Qué hace

Recibe el briefing de NTE-TREND-SCOUT y redacta 2 artículos de blog completos, SEO-optimizados, con la voz de NTE, y los sube directamente a WordPress como Drafts.

## 📄 Estructura de Cada Artículo

```
📝 Artículo Completo NTE
├── SEO Title (50-60 caracteres con keyword)
├── Meta Description (150-160 caracteres)
├── H1 — Título principal con keyword
├── Introducción (150 palabras · hook + promesa)
├── H2 — Sección 1
│   └── H3 — Sub-secciones con keywords LSI
├── H2 — Sección 2
├── H2 — Sección 3
├── H2 — Casos de uso / Ejemplos NTE
├── H2 — Conclusión
├── CTA → Contactar a NTE para [servicio relacionado]
├── Links internos (2-3 a otros artículos NTE)
└── Schema markup (FAQ o HowTo si aplica)
```

## 🖋️ Voz Editorial de NTE

Los artículos siempre deben:
- **Educar** antes de vender (80/20 regla)
- Usar ejemplos concretos del contexto empresarial (Miami · LATAM · PyMEs)
- Vincular naturalmente con servicios de NTE sin ser agresivo
- Mantener el tono: profesional pero accesible, con propósito

## 📤 Output — Lo que sube a WordPress

```json
{
  "title": "Título del artículo",
  "content": "HTML completo del artículo",
  "status": "draft",
  "categories": ["AI", "Software Development"],
  "tags": ["keyword1", "keyword2"],
  "meta": {
    "seo_title": "...",
    "meta_description": "...",
    "focus_keyword": "..."
  }
}
```

## 💬 Notificación a Michael vía Slack

```
📝 *2 artículos listos para revisión*

*Artículo 1:* "Cómo la IA está transformando el desarrollo de software en 2026"
🔗 Preview: wordpress.ntetech.com/wp-admin/post.php?post=123&action=edit
📊 Keyword: "AI software development" · Vol: 8,400/mes · Dificultad: 42

*Artículo 2:* "5 señales de que tu empresa necesita un CRM personalizado"
🔗 Preview: wordpress.ntetech.com/wp-admin/post.php?post=124&action=edit
📊 Keyword: "custom CRM development" · Vol: 2,900/mes · Dificultad: 38

✅ Reacciona con ✅ para publicar | 🔄 Responde con cambios | ❌ Para rechazar
```

[← NTE-TREND-SCOUT](./nte-trend-scout.md) | [NTE-PUBLISHER →](./nte-publisher.md)
