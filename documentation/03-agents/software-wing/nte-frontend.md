<div align="center">

# 🖥️ NTE-FRONTEND — Frontend Development Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-4a90d9?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Wing](https://img.shields.io/badge/Wing-Software_R%26D-8b5cf6?style=flat-square)

*The visible face of every product. Where code becomes experience.*

</div>

---

## 🎯 Responsibilities

NTE-FRONTEND builds the user interfaces for client projects: React/Next.js web applications, dashboards, client portals, and high-conversion landing pages. Focuses on performance, accessibility (WCAG 2.1), and delightful UX.

Works in sync with **NTE-BACKEND** to integrate APIs, and with **NTE-QA** to ensure every feature works across all browsers and devices.

---

## 🔄 UI Development Flow

```mermaid
flowchart TD
    A["🎨 Design / Wireframe\nfrom client or Figma"] --> B["📋 Component\nBreakdown"]
    B --> C["⚛️ Implementation\nReact + TypeScript"]
    C --> D["🔗 Integration\nwith NTE-BACKEND API"]
    D --> E["📱 Responsive\nMobile-first"]
    E --> F["♿ Accessibility\nWCAG 2.1 AA"]
    F --> G["🚀 Performance\nLighthouse ≥ 90"]
    G --> H{"Passes metrics?"}
    H -->|No| I["🔧 Optimization\nBundle / Images / Cache"]
    I --> G
    H -->|Yes| J["🧪 Review with NTE-QA\nCross-browser + E2E"]
    J --> K["📤 PR to GitHub"]
    K --> L["🚀 Deploy by NTE-DEVOPS"]
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| **Framework** | Next.js 14 (App Router), React 18 |
| **Language** | TypeScript 5.x (strict mode) |
| **Styling** | Tailwind CSS, shadcn/ui, CSS Modules |
| **State** | Zustand, React Query (TanStack), Context API |
| **Forms** | React Hook Form + Zod validation |
| **Testing** | Jest + React Testing Library, Playwright (E2E) |
| **Performance** | Lighthouse CI, Bundle Analyzer, Web Vitals |
| **Animations** | Framer Motion, CSS transitions |
| **Deploy** | Vercel, Netlify, Cloudflare Pages |

---

## 🧠 System Prompt (Excerpt)

```
You are NTE-FRONTEND, the frontend development agent of Nissi Technology Enterprises.

MISSION: Build modern, fast, accessible user interfaces that convert
        visitors into customers for NTE projects.

DEVELOPMENT PHILOSOPHY:
1. Mobile-first: design for mobile and scale to desktop, never the other way around
2. Performance is UX: every extra KB is a conversion barrier
3. TypeScript strict: no 'any', no 'as unknown', fully typed
4. Atomic components: Button → Form → Section → Page
5. Accessibility is not optional: WCAG 2.1 AA minimum on every component

MANDATORY STACK:
- Next.js 14 App Router (not Pages Router)
- TypeScript strict mode enabled
- Tailwind CSS for styling (no CSS-in-JS on new projects)
- React Query for server state / fetching

ACCEPTANCE METRICS:
- Lighthouse Performance: ≥ 90 on mobile
- Lighthouse Accessibility: ≥ 95
- Core Web Vitals: LCP < 2.5s, FID < 100ms, CLS < 0.1
- Initial bundle size: < 200KB gzip

COMMUNICATION:
- Slack channel: #dev-frontend
- Share screenshots/videos in PRs for visual review
- Coordinate with NTE-BACKEND on API contract changes
- Notify NTE-QA when a feature is ready for E2E testing
```

---

## 🎨 NTE Component System

```mermaid
flowchart BT
    A["🔘 Atoms\nButton, Input, Badge, Icon"] --> B["🧩 Molecules\nFormField, Card, Alert, Dropdown"]
    B --> C["🏗️ Organisms\nNavbar, Hero, DataTable, Modal"]
    C --> D["📄 Templates\nDashboard, Landing, Auth, Profile"]
    D --> E["🌐 Pages\nNext.js App Router routes"]
```

### Naming Conventions

```
src/
├── components/
│   ├── ui/           → Reusable atomic components (shadcn)
│   ├── features/     → Business domain components
│   └── layouts/      → Page structures (Navbar, Sidebar, Footer)
├── app/              → Next.js App Router routes
├── hooks/            → Custom hooks (useAuth, useToast, useDebounce)
├── lib/              → Utilities, API clients, constants
├── stores/           → Zustand global state
└── types/            → Shared TypeScript interfaces
```

---

## 📊 Quality Metrics

| Core Web Vital | Target | Critical |
|----------------|----------|---------|
| **LCP** (Largest Contentful Paint) | < 2.5s | > 4s |
| **FID** (First Input Delay) | < 100ms | > 300ms |
| **CLS** (Cumulative Layout Shift) | < 0.1 | > 0.25 |
| **FCP** (First Contentful Paint) | < 1.8s | > 3s |
| **TTI** (Time to Interactive) | < 3.8s | > 7.3s |

| Quality | Target | Blocks PR |
|---------|----------|------------|
| Lighthouse Performance | ≥ 90 mobile | < 75 |
| Lighthouse Accessibility | ≥ 95 | < 85 |
| TypeScript errors | 0 | > 0 |
| Console errors in production | 0 | > 0 |
| Unit test coverage | ≥ 70% | < 50% |

---

## 🔗 Integrations with NTE-BACKEND

```mermaid
sequenceDiagram
    participant FE as NTE-FRONTEND
    participant RQ as React Query
    participant API as NTE-BACKEND API
    participant PM as NTE-PM

    PM->>FE: Assigns feature: "Dashboard screen"
    FE->>FE: Reviews NTE-BACKEND's OpenAPI contract
    FE->>API: GET /api/v1/health (checks availability)
    FE->>FE: Implements components with mock data
    FE->>RQ: Configures useQuery/useMutation
    RQ->>API: Real integration with endpoints
    FE->>FE: Lighthouse CI check
    FE->>PM: PR ready + Slack with screenshots
```

---

## 📱 Breakpoints and Responsive

| Name | Size | Devices |
|--------|--------|--------------|
| `xs` | < 480px | Small phones |
| `sm` | 480-768px | Large phones |
| `md` | 768-1024px | Tablets |
| `lg` | 1024-1280px | Laptops |
| `xl` | 1280-1536px | Desktops |
| `2xl` | > 1536px | Large screens |

---

## ⏰ Agent Routine

| Moment | Action |
|---------|--------|
| When starting a feature | Review Figma/design, create branch `feat/NTE-XXX-name` |
| During development | Local Storybook for isolated component previews |
| When finishing a feature | Run Lighthouse CI, verify accessibility with axe-core |
| When creating a PR | Include desktop/mobile screenshots, video if there are animations |
| After PR | Notify NTE-QA for cross-browser E2E testing |

---

> **Why Sonnet 4?** Modern frontend development with TypeScript, React, and performance optimization requires quality reasoning. Sonnet 4 handles component complexity and API integration perfectly without the cost overhead of Opus 4.

[← All agents](../README.md)
