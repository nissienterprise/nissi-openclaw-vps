<div align="center">

# 🎧 Flow: Omnichannel Customer Service
### Response < 5 Minutes · 24/7 · Across All Channels

</div>

```mermaid
flowchart TD
    subgraph CANALES["📡 Incoming Channels"]
        WA["📱 WhatsApp"] & EM["📧 Email"] & FB["📘 Facebook"] & IG["📸 Instagram"] & CH["💬 Web Chat"] & SMS["📟 SMS"]
    end

    CX["🎧 Samantha (NTE-CX) · Sonnet 4\n< 5 minutes · samantha@nissienterprise.com"]

    subgraph CLASIFICACION["🎯 Intent Classification"]
        Q["💰 Quote"]
        S["🔧 Technical Support"]
        I["ℹ️ General Info"]
        C["😠 Complaint"]
        SP["🗑️ Spam"]
    end

    subgraph ACCION["⚡ Automatic Action"]
        A1["Generates preliminary proposal (QuickBooks estimate)\n→ passes to EVA (NTE-LEAD-INTAKE)"]
        A2["Resolves using knowledge base\n→ escalates if complex"]
        A3["Responds with NTE service info"]
        A4["Logs + IMMEDIATE alert to Michael\nvia #nte-cx"]
        A5["Archives without responding"]
    end

    CRM["📋 Logs ticket in Jira (NTE-OPS)\nand lead in CRM"]
    SLACK["💬 #nte-cx\nEscalation if needed"]

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

## Sample Responses by Channel

**WhatsApp Business:**
> "Hi [Name]! 👋 I'm the assistant for Nissi Technology Enterprises. I received your message about [detected topic]. To give you the best assistance, can you tell me a bit more about [qualifying question]? In the meantime, here's information about our related services: [link]. An expert from our team will contact you very soon!"

**Email (from samantha@nissienterprise.com):**
> Subject: Re: Your inquiry to Nissi Technology Enterprises
> "Hi [Name], thank you for reaching out. I've received your message and am processing it..."

[← Flows](./README.md)
