# InsightForge Sentinel

> **Enterprise Data Quality & Schema Intelligence Platform**

Transforming raw data into trusted business intelligence.

---

## Overview

InsightForge Sentinel is an enterprise-grade data quality platform designed to automatically profile datasets, infer business meaning, validate data quality, and generate actionable insights before data reaches downstream analytics or production systems.

Unlike traditional validation scripts, Sentinel combines profiling, schema intelligence, business rule execution, and modular validation into a single extensible framework.

The project is built with clean architecture principles, modular design, and extensibility in mind, making it suitable for enterprise-scale data quality initiatives.

---

## Key Features

### Dataset Profiling

- Dataset statistics
- Missing value analysis
- Duplicate detection
- Data type profiling
- Memory usage reporting

---

### Schema Intelligence

- Business type detection
- Logical type inference
- Physical type detection
- Confidence scoring
- Recommended validator generation

---

### Rule Engine

- Industry-specific rule packs
- Dynamic rule loading
- Execution plan generation
- Modular rule architecture

---

### Validation Framework

Current validators include:

- UNIQUE
- NOT_NULL
- POSITIVE
- VALID_EMAIL
- NOT_FUTURE_DATE

The validation framework is fully extensible using the Validator Registry pattern.

---

### Reporting

- Dataset Profile
- Primary Key Analysis
- Business Type Analysis
- Schema Intelligence
- Validation Results

---

## Architecture

```text
                    InsightForge Sentinel

                         CSV / Excel / SQL
                                 │
                                 ▼
                         File Connector Layer
                                 │
                                 ▼
                        Preprocessing Engine
                                 │
                                 ▼
                        Data Type Inference
                                 │
                                 ▼
                          Profiling Engine
                                 │
                                 ▼
                          Inference Engine
                                 │
                                 ▼
                     Schema Intelligence Engine
                                 │
                                 ▼
                           Knowledge Model
                                 │
                                 ▼
                            Rule Engine
                                 │
                                 ▼
                        Validator Registry
                                 │
         ┌──────────────┬──────────────┬──────────────┐
         ▼              ▼              ▼              ▼
      UNIQUE        NOT_NULL      POSITIVE     VALID_EMAIL
                                              NOT_FUTURE_DATE
                                 │
                                 ▼
                        Validation Engine
                                 │
                                 ▼
                         Console Reporter
```

---

## Project Structure

```
InsightForge-Sentinel/

├── src/
│   ├── connectors/
│   ├── preprocessing/
│   ├── profiling/
│   ├── inference/
│   ├── intelligence/
│   ├── rules/
│   ├── reporting/
│   └── models/
│
├── data/
├── docs/
├── tests/
│
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
├── LICENSE
└── requirements.txt
```

---

## Technology Stack

- Python
- Pandas
- Object-Oriented Programming
- Modular Architecture
- Rule Engine
- Data Validation
- Schema Intelligence
- Data Governance Concepts

---

## Current Capabilities

| Module | Status |
|----------|----------|
| File Connector | ✅ |
| Preprocessing Engine | ✅ |
| Data Type Inference | ✅ |
| Profiling Engine | ✅ |
| Inference Engine | ✅ |
| Schema Intelligence | ✅ |
| Rule Engine | ✅ |
| Validation Framework | ✅ |
| Console Reporter | ✅ |

---

## Roadmap

### Version 0.8.0

Architecture Stabilization

- Validator Registry
- Schema Intelligence
- Modular Validation Framework
- Console Reporting

---

### Version 0.9.0

Planned

- Dataset Health Engine
- Trust Score Engine
- Recommendation Engine
- HTML Executive Report

---

### Version 1.0.0

Enterprise Release

- REST API
- Excel Connector
- SQL Connector
- AI-powered Insights
- Multi-industry Rule Packs

---

## Why InsightForge Sentinel?

Organizations often discover data quality issues only after dashboards, reports, or machine learning models have already consumed the data.

InsightForge Sentinel shifts quality checks earlier in the pipeline by combining:

- Schema Intelligence
- Rule-based Validation
- Business-aware Recommendations
- Extensible Validation Architecture

This enables teams to build trust in their data before it reaches production systems.

---

## Getting Started

Clone the repository

```bash
git clone https://github.com/<your-github-username>/InsightForge-Sentinel.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Sentinel

```bash
python src/main.py
```

---

## Current Version

**v0.8.0**

Architecture Stabilization

---

## Author

**Prince Srivastava**

Data Analyst | Python | SQL | Power BI | Data Quality Engineering

---

## License

This project is licensed under the MIT License.