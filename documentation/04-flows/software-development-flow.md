<div align="center">

# ⚙️ Flow: Automated Software Development
### The 6 Phases — From Brief to Delivery

</div>

```mermaid
flowchart TD
    F1["📥 PHASE 1: INTAKE\nSamantha receives brief → EVA qualifies → David creates project\nAutomatic budget (QuickBooks draft) → Client + Michael approval"]
    F2["📋 PHASE 2: PLANNING\nDavid: Epics · Stories · Tasks in Jira (NTE-SW)\nTimeline · GitHub repository · Agent assignment\nMilestones in NTE-Calendar"]
    F3["🏗️ PHASE 3: ARCHITECTURE\nBishop + Sonny: Technical design · CASE: DB schema\nT-800: Initial security risk review"]
    F4["💻 PHASE 4: ITERATIVE DEVELOPMENT\nWeekly sprints · Bishop + Sonny + BB-8 in parallel\nAutomatic CI/CD (Optimus) · QA on every PR (AVA)\nClient report every Friday via David"]
    F5["🔍 PHASE 5: REVIEW & QA\nAVA: Complete post-sprint report in Jira\nT-800: Pre-release security scan\nBugs assigned back to the corresponding agent"]
    F6["🚀 PHASE 6: DEPLOYMENT & DELIVERY\nOptimus: Production deploy (with Michael's approval)\nMarvin: Final documentation in Confluence\nDavid: Project closeout in Jira + testimonial request"]

    F1 --> F2 --> F3 --> F4 --> F5
    F5 -->|"Critical bugs"| F4
    F5 -->|"QA ✅"| F6
    F6 -->|"New project"| F1

    style F1 fill:#1a1a2e,color:#fff
    style F2 fill:#1a2c1a,color:#fff
    style F3 fill:#2c1a1a,color:#fff
    style F4 fill:#1a1a2e,color:#fff
    style F5 fill:#2c1654,color:#fff
    style F6 fill:#1a3a1a,color:#fff
```

## Roles by Phase

| Phase | Active Agents | Output |
|---|---|---|
| 1. Intake | Samantha (NTE-CX) · EVA (NTE-LEAD-INTAKE) · David (NTE-PM) | Structured brief + approved QuickBooks estimate |
| 2. Planning | David (NTE-PM) | Jira board (NTE-SW) + GitHub repo + NTE-Calendar |
| 3. Architecture | David · Bishop · Sonny · T-800 | Technical architecture document |
| 4. Development | Bishop · Sonny · BB-8 · CASE · AVA · Optimus | Code + working CI/CD pipeline |
| 5. QA & Review | AVA (NTE-QA) · T-800 (NTE-SECURITY) | Bug report in Jira + security clearance |
| 6. Delivery | Optimus · Marvin · David | App in production + documentation in Confluence |

---

## SCRUM: Process Detail

Phase 4 (Iterative Development) operates under **weekly sprints** with Jira (project `NTE-SW`).

See the complete SCRUM process document:

**[→ Detailed SCRUM Workflow: Ceremonies · Jira · Branches · Definition of Done](./detailed-scrum-flow.md)**

Includes:
- Sprint Planning, Daily Standup, Sprint Review, Retrospective
- Jira board columns and ticket lifecycle
- Branch and commit conventions (Conventional Commits)
- Complete Definition of Done
- Production hotfix management
- Agile process KPIs

[← All flows](./README.md)
