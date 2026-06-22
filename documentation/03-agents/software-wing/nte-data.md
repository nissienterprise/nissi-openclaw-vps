<div align="center">

# 📊 NTE-DATA — Data Engineering Agent

![Model](https://img.shields.io/badge/Model-Claude_Sonnet_4-4a90d9?style=flat-square)
![Sandbox](https://img.shields.io/badge/Sandbox-Docker_✓-5cb85c?style=flat-square)
![Wing](https://img.shields.io/badge/Wing-Software_R%26D-8b5cf6?style=flat-square)

*The guardian of data. Turns noise into actionable signal for NTE and its clients.*

</div>

---

## 🎯 Responsibilities

NTE-DATA designs and implements data pipelines (ETL/ELT), warehouses, business intelligence dashboards, and basic machine learning models for client projects. Ensures the quality, integrity, and availability of data across the entire NTE ecosystem.

Should not be confused with **NTE-ANALYTICS** (which generates internal NTE reports) — NTE-DATA builds the data infrastructure for *client products*.

---

## 🔄 Data Pipeline

```mermaid
flowchart LR
    subgraph SOURCES ["📥 Sources"]
        DB["🗄️ Databases"]
        API["🔗 External\nAPIs"]
        FILES["📁 CSV / Excel\n/ Sheets"]
        EVENTS["📡 Event\nStreams"]
    end

    subgraph PIPELINE ["⚙️ NTE-DATA Pipeline"]
        E["Extract\nConnectors"]
        T["Transform\ndbt / Pandas"]
        L["Load\nWarehouse"]
        Q["Quality\nChecks"]
    end

    subgraph OUTPUT ["📤 Destinations"]
        DW["🏛️ Data\nWarehouse"]
        DASH["📊 Dashboard\nMetabase / Looker"]
        ML["🤖 ML Model\nFeatures"]
        API2["🔗 Enriched\nAPI"]
    end

    SOURCES --> E
    E --> T
    T --> Q
    Q --> L
    L --> DW
    DW --> DASH
    DW --> ML
    DW --> API2
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| **ETL / ELT** | dbt, Apache Airflow, Prefect |
| **Processing** | Python + Pandas, PySpark (large volumes) |
| **Warehouse** | BigQuery, Snowflake, DuckDB (small projects) |
| **Streaming** | Apache Kafka, Redis Streams |
| **BI / Dashboards** | Metabase, Looker Studio, Grafana |
| **ML** | scikit-learn, XGBoost, HuggingFace Transformers |
| **Quality** | Great Expectations, dbt tests |
| **Orchestration** | Airflow DAGs, Prefect Flows, Cron |
| **Storage** | AWS S3, GCP Cloud Storage |

---

## 🧠 System Prompt (Excerpt)

```
You are NTE-DATA, the data engineering agent of Nissi Technology Enterprises.

MISSION: Build the data infrastructure that enables NTE clients to make
        evidence-based decisions, not gut-feel decisions.

CORE RESPONSIBILITIES:
1. Design ETL/ELT pipelines that are idempotent and re-runnable
2. Implement data quality checks before loading into the warehouse
3. Create documented dbt models with tests at every layer (staging/intermediate/mart)
4. Build dashboards that tell stories, not just display numbers
5. Model data for ML when the client needs predictions

DATA QUALITY PRINCIPLES:
- Never load data without prior validation (Great Expectations or dbt tests)
- Always implement SCD Type 2 for critical historical data
- Document data lineage in every dbt model
- Pipelines must be idempotent: running twice = same result

MODELING:
- Star schema for OLAP warehouses (facts + dimensions)
- 3NF normalization for OLTP (transactional databases)
- One Big Table for exploratory queries with DuckDB

COMMUNICATION:
- Slack channel: #dev-data
- Share data catalogs with NTE-DOCS for documentation
- Coordinate with NTE-BACKEND for enriched data endpoints
- Notify NTE-PM when a pipeline has data quality failures
```

---

## 📐 Data Warehouse Architecture (Medallion)

```mermaid
flowchart TD
    subgraph BRONZE ["🥉 Bronze Layer — Raw"]
        B1["Raw data\nuntransformed"]
        B2["Original schema\nfrom the source"]
        B3["Never modify\nafter loading"]
    end

    subgraph SILVER ["🥈 Silver Layer — Cleaned"]
        S1["Clean and\nnormalized data"]
        S2["Correct\ndata types"]
        S3["Duplicates\nremoved"]
        S4["dbt staging\nmodels"]
    end

    subgraph GOLD ["🥇 Gold Layer — Business"]
        G1["Business\nmetrics"]
        G2["Precomputed\naggregations"]
        G3["Ready for\ndashboards and APIs"]
        G4["dbt mart\nmodels"]
    end

    BRONZE --> SILVER
    SILVER --> GOLD
```

---

## 🔍 Data Quality Framework

```mermaid
flowchart LR
    A["📥 Incoming\ndata"] --> B["🔍 Schema\nValidation"]
    B --> C["📊 Statistical\nChecks"]
    C --> D["🔗 Referential\nIntegrity"]
    D --> E["⏰ Freshness\nCheck"]
    E --> F{"All OK?"}
    F -->|Yes| G["✅ Load to\nWarehouse"]
    F -->|No| H["🚨 Slack Alert\n#dev-data"]
    H --> I["🔒 Quarantine\nTable"]
    I --> J["🔧 NTE-PM\nreview and fix"]
```

### Mandatory Checks per Critical Column

| Check | Description | Severity |
|-------|-------------|----------|
| `not_null` | Field cannot be null | ERROR |
| `unique` | No duplicates in PK | ERROR |
| `accepted_values` | Enum within expected range | WARNING |
| `relationships` | FK exists in parent table | ERROR |
| `freshness` | Data not older than X hours | WARNING |
| `row_count` | Row count within expected range | WARNING |

---

## 📊 Deliverable Types

| Deliverable | Tool | Update |
|------------|-------------|---------------|
| Executive dashboard (KPIs) | Metabase | Real time |
| Weekly sales report | dbt + Looker Studio | Every Monday 7am |
| CRM sync pipeline | Airflow DAG | Hourly |
| Lead scoring model | scikit-learn | Weekly, re-training |
| Recommendations API | FastAPI + Redis cache | Real time |
| User cohort analysis | DuckDB + Jupyter | Ad-hoc |

---

## 📊 Agent Metrics

| Metric | Target | Critical |
|---------|----------|---------|
| Pipeline success rate | ≥ 99% | < 95% → alert |
| Data freshness (lag) | < 1 hour | > 4 hours → critical |
| Data quality score | ≥ 98% valid rows | < 95% → blocking |
| Query performance P95 | < 5s on warehouse | > 30s → optimize |
| dbt test coverage | 100% on Gold layer | < 80% → blocking |

---

> **Why Sonnet 4?** Data pipelines involve complex transformation logic and model design, but follow well-defined patterns (ELT, Star Schema, dbt). Sonnet 4 executes these tasks with high quality without the cost of Opus.

[← All agents](../README.md)
