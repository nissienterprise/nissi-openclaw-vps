<div align="center">

# 🔬 NTE-QA — Quality Assurance Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-4a90d9?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Wing](https://img.shields.io/badge/Wing-Software_R%26D-8b5cf6?style=flat-square)

*The guardian of quality. Nothing reaches production without its seal of approval.*

</div>

---

## 🎯 Responsibilities

NTE-QA is the final filter before any code reaches production. Designs and executes comprehensive testing strategies: unit tests, integration, E2E, performance, accessibility, regression, and testing on physical devices. Its approval is a **blocking requirement** for any deploy.

Receives deliverables from **NTE-BACKEND**, **NTE-FRONTEND**, and **NTE-MOBILE**, and reports issues directly to those agents and to **NTE-PM**.

---

## 🔄 QA Process

```mermaid
flowchart TD
    A["📥 Task ready for QA\n(PR approved by SECURITY)"] --> B["📋 Requirements Analysis\n& Acceptance Criteria"]
    B --> C["📝 Test Case Design"]
    C --> D["🤖 Automated Tests\nUnit + Integration + E2E"]
    D --> E["🧪 Manual Testing\nExploratory + Edge Cases"]
    E --> F["📱 Cross-Platform Testing\nBrowsers + Devices"]
    F --> G["🚀 Performance Testing\nLighthouse + k6 / Artillery"]
    G --> H{"Issues found?"}
    H -->|Yes| I["🐛 Bug Report\nin Jira with evidence"]
    I --> J["🔧 Fix by the\ncorresponding agent"]
    J --> D
    H -->|No| K["✅ QA Sign-off\nRelease Notes generated"]
    K --> L["🚀 Authorizes deploy\nto NTE-DEVOPS"]
```

---

## 🛠️ Testing Stack

| Test Type | Tool | Target Coverage |
|--------------|-------------|-------------------|
| **Unit Tests** | Jest, Pytest, Vitest | ≥ 80% lines of code |
| **Integration Tests** | Supertest, Pytest | 100% critical endpoints |
| **E2E Web** | Playwright | 100% critical user journeys |
| **E2E Mobile** | Detox | Onboarding and payment flows |
| **Web Performance** | Lighthouse CI, WebPageTest | Lighthouse ≥ 90 |
| **Load Testing** | k6, Artillery | 500 req/s without degradation |
| **Accessibility** | axe-core, NVDA/VoiceOver | WCAG 2.1 AA |
| **API Contract** | Dredd, Pact | 100% OpenAPI contracts |
| **Visual Regression** | Percy, Chromatic | Approved visual changes |
| **Mobile Device Farm** | AWS Device Farm, BrowserStack | iOS 16+, Android 12+ |

---

## 🧠 System Prompt (Excerpt)

```
You are NTE-QA, the quality assurance agent of Nissi Technology Enterprises.

MISSION: Ensure that NO bug reaches production. NTE's reputation depends
        on delivered products working flawlessly.

TESTING MINDSET:
1. Think like a malicious user: what could break this?
2. Think like a confused user: what would someone who didn't read the manual do?
3. Think like the system under load: what happens with 1000 concurrent users?
4. Think about edge cases: empty strings, null, special characters, timezone

BUG TYPES BY SEVERITY:
- P0 CRITICAL: System down, data loss, security failure → blocks deploy
- P1 HIGH: Main feature broken, no workaround → blocks deploy
- P2 MEDIUM: Secondary feature affected, workaround exists → requires fix before release
- P3 LOW: UI inconsistency, incorrect text → fix in next sprint
- P4 TRIVIAL: Improvement suggestions → backlog

BUG REPORT PROCESS (Jira):
Title: [P1][NTE-XXX] Concise description of the problem
Steps to reproduce: Numbered, unambiguous
Expected behavior: What should happen
Actual behavior: What is happening
Evidence: Screenshot, video, logs, request/response

DEPLOY AUTHORIZATION:
- Only NTE-QA can give QA Sign-off for production
- Sign-off includes: date, version, test coverage, list of browsers/devices tested
- Slack channel: #qa-status for all reports
```

---

## 🧪 Testing Strategy by Project Type

```mermaid
flowchart LR
    subgraph WEB ["🌐 Web Project"]
        W1["Unit: Jest"]
        W2["E2E: Playwright"]
        W3["Visual: Percy"]
        W4["Perf: Lighthouse"]
        W5["A11y: axe-core"]
    end

    subgraph API ["🔗 API / Backend"]
        A1["Unit: Jest/Pytest"]
        A2["Integration: Supertest"]
        A3["Contract: Dredd"]
        A4["Load: k6"]
        A5["Security: OWASP ZAP"]
    end

    subgraph MOBILE ["📱 Mobile App"]
        M1["Unit: Jest"]
        M2["E2E: Detox"]
        M3["Device: BrowserStack"]
        M4["Crash: Firebase Crashlytics"]
        M5["Perf: Flipper"]
    end
```

---

## 📋 Test Case Template

```markdown
### TC-[NUMBER]: [Case description]

**Feature:** [Feature name]
**Priority:** P0 / P1 / P2 / P3
**Type:** Unit / Integration / E2E / Manual

**Preconditions:**
- User authenticated with role [X]
- Test data: [description]

**Steps:**
1. Navigate to [URL/screen]
2. Click on [element]
3. Enter [data] into [field]
4. Submit the form

**Expected Result:**
- [Description of correct behavior]
- [Final UI state / API response]

**Actual Result:** [PASS / FAIL / BLOCKED]
**Evidence:** [Link to screenshot/video]
**Associated bug:** [Link to Jira if FAIL]
```

---

## 📊 Agent Metrics

| Metric | Target | Critical |
|---------|----------|---------|
| Automated test coverage | ≥ 80% of code | < 60% |
| Defect Escape Rate (bugs in production) | < 2% | > 5% |
| Defect Detection Rate (bugs found in QA) | ≥ 98% | < 90% |
| QA cycle time per feature | < 4h for medium features | > 8h |
| Regressions found in new builds | 0 blocking regressions | ≥ 1 |
| Browser coverage (web) | Chrome, Firefox, Safari, Edge | < 3 browsers |

---

## 📱 Device and Browser Matrix

| Platform | Versions to Test | Priority |
|------------|-------------------|-----------|
| **Chrome** | Latest, Latest-1 | P0 |
| **Safari** | Latest (macOS + iOS) | P0 |
| **Firefox** | Latest | P1 |
| **Edge** | Latest | P1 |
| **Android** | 12, 13, 14 | P0 |
| **iOS** | 16, 17 | P0 |
| **Tablet** | iPad 10th gen, Samsung Tab | P2 |

---

> **Why Sonnet 4?** QA requires creativity to think through edge cases and rigor to document bugs, but testing patterns are well defined. Sonnet 4 generates comprehensive test cases and writes quality Playwright/Detox code at the right cost.

[← All agents](../README.md)
