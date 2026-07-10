# InsightForge Sentinel

# System Architecture

Version: 0.1

---

# Vision

InsightForge Sentinel is an enterprise Data Intelligence Platform that helps organizations understand, validate, and improve data quality before the data is consumed by reporting, analytics, automation, or AI systems.

Instead of simply checking for errors, Sentinel analyzes datasets, identifies business entities, recommends validations, and produces an overall Data Trust Score.

---

# High-Level Architecture

```
                    CSV / Excel / SQL / API
                               │
                               ▼
                     File Connector Layer
                               │
                               ▼
                    Preprocessing Engine
                               │
                               ▼
                     Dataset Profiler
                               │
                               ▼
                    Business Analyzers
                               │
                               ▼
                    Validation Engine
                               │
                               ▼
                     Rule Evaluation Engine
                               │
                               ▼
                      Trust Score Engine
                               │
                               ▼
                   Reporting & Visualization
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
          JSON Report                    Power BI Dashboard
               │
               ▼
      Power Automate / APIs / AI
```

---

# Core Modules

## 1. File Connector

Responsibilities

- Read CSV
- Read Excel
- Read SQL
- Read SharePoint
- Read APIs

Output

- Pandas DataFrame

---

## 2. Preprocessing Engine

Responsibilities

- Normalize column names
- Remove extra spaces
- Convert blank values to NULL
- Detect malformed CSVs
- Standardize formats

Output

- Clean DataFrame

---

## 3. Dataset Profiler

Responsibilities

- Row count
- Column count
- Memory usage
- Missing values
- Duplicate rows
- Data types

Output

- Dataset Profile

---

## 4. Analyzer Engine

Responsibilities

Analyze business meaning.

Examples

- Primary Key Analyzer
- Data Type Analyzer
- Email Analyzer
- Date Analyzer
- Currency Analyzer
- Phone Analyzer
- Business Domain Analyzer

Output

- Intelligent Recommendations

---

## 5. Validation Engine

Responsibilities

Apply configurable business rules.

Examples

- NULL Validation
- Duplicate Validation
- Future Date Validation
- Negative Amount Validation
- Email Validation

---

## 6. Rule Engine

Responsibilities

Execute domain-specific business rules.

Examples

Retail

- Order ID must be unique
- Invoice Amount cannot be negative

Banking

- Account Number unique
- Balance cannot be negative

Healthcare

- DOB cannot be future

---

## 7. Trust Score Engine

Responsibilities

Calculate overall dataset quality.

Example

Overall Score

92%

Risk

Low

---

## 8. Reporting Engine

Responsibilities

Generate

- Console Report
- JSON
- HTML
- PDF (Future)

---

# Design Principles

- Modular Architecture
- Single Responsibility Principle
- Open/Closed Principle
- Explainable Intelligence
- Plug-in Architecture
- Business-first Design

---

# Technology Stack

Python

Pandas

OpenPyXL

Power BI

Power Automate

Git

GitHub

Future

FastAPI

Docker

Azure

OpenAI

---

# Future Roadmap

Version 1

CSV Validation

Version 2

Business Rules

Version 3

Automation

Version 4

AI Recommendations

Version 5

Enterprise SaaS