# 👋 Welcome to InsightForge Sentinel

**Product ID:** IF001

**Product Name:** Sentinel

**Version:** v0.4.0

---

# What is Sentinel?

Sentinel is an Enterprise Data Intelligence Platform that automatically understands datasets, detects data quality issues, recommends business validation rules, and measures data trust before data is consumed by downstream systems.

The vision is to reduce manual data validation by combining automation, business intelligence, and explainable analytics.

---

# Why Sentinel Exists

Most organizations still spend hours manually checking spreadsheets and CSV files before analysis.

Typical manual process:

CSV

↓

Excel

↓

Filter NULL values

↓

Find duplicates

↓

Check dates

↓

Validate IDs

↓

Build dashboard

↓

Repeat tomorrow

Sentinel automates this workflow.

---

# Current Capabilities

✅ File Connector

Read CSV and Excel datasets.

---

✅ Dataset Profiler

Understand dataset structure.

- Rows
- Columns
- Data Types
- Missing Values
- Memory Usage

---

✅ Primary Key Analyzer

Identify likely primary keys.

---

✅ Business Type Analyzer

Identify business meaning of columns.

Examples:

Order_ID → Identifier

Invoice_Amount → Currency

Email → Email Address

Order_Date → Date

---

✅ Console Reporter

Present findings in a structured format.

---

# Current Architecture

```

Raw Dataset

↓

File Connector

↓

Profiler

↓

Primary Key Analyzer

↓

Business Type Analyzer

↓

Console Reporter

```

---

# Repository Structure

```

IF001-Sentinel/

│

├── src/

│ ├── analyzers/

│ ├── connectors/

│ ├── preprocessing/

│ ├── profiling/

│ ├── reporting/

│ ├── validation/

│ ├── rules/

│ ├── utils/

│ └── main.py

│

├── data/

├── docs/

├── tests/

├── PROJECT_STATE.md

└── START_HERE.md

```

---

# How to Run Sentinel

## 1. Open Terminal

Navigate to the Sentinel project.

Example

```

cd Products/IF001-Sentinel

```

---

## 2. Activate Virtual Environment

Windows

```

.\.venv\Scripts\Activate.ps1

```

---

## 3. Install Dependencies

```

pip install -r requirements.txt

```

---

## 4. Run

```

python src/main.py

```

---

# Development Workflow

Every feature follows this process.

Backlog

↓

Product Requirement

↓

Architecture

↓

Implementation

↓

Testing

↓

Documentation

↓

Git Commit

↓

Release

---

# Documentation Guide

Read documents in this order.

1. START_HERE.md
2. PROJECT_STATE.md
3. docs/product/Product-Backlog.md
4. docs/releases/
5. docs/sprints/
6. Engineering-Handbook/

---

# Current Release

Version

v0.4.0

Completed

- File Connector
- Dataset Profiler
- Primary Key Analyzer
- Business Type Analyzer
- Console Reporter

---

# Next Release

v0.5.0

Theme

Data Quality Foundation

Planned Features

- Preprocessing Engine
- Null Analyzer
- Duplicate Analyzer
- Data Type Inference

---

# Engineering Principles

Every engineering decision follows these principles.

- Business First
- Explainability
- Modularity
- Reusability
- Automation by Design
- Simplicity
- Testability

---

# Current Status

See:

PROJECT_STATE.md

This file always contains the latest development status.

---

# Contributing

Every feature must include:

- Working Code
- Tests
- Documentation
- Sprint Notes
- Release Notes
- Git Commit

---

# Long-Term Vision

Sentinel will evolve into an Enterprise Data Intelligence Platform capable of:

- Intelligent data profiling
- Business rule validation
- Trust score calculation
- Automated reporting
- Power BI integration
- Power Automate integration
- REST API
- AI-powered dataset explanations
- Web application

---

# Welcome

You're looking at the early stages of InsightForge Sentinel.

Every release is designed to move the product one step closer to becoming a production-ready enterprise platform.