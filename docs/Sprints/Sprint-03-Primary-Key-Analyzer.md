# Sprint 03 - Primary Key Analyzer

---

## Product

**InsightForge Sentinel**

---

## Sprint

Sprint 03

---

## Feature

Primary Key Analyzer

---

## Status

✅ Completed

---

# Objective

Develop an intelligent module capable of automatically identifying the most likely Primary Key(s) within a dataset without requiring any user configuration.

The analyzer evaluates every column and assigns a confidence score based on multiple characteristics that are commonly associated with primary keys.

This capability forms the foundation for future validation and business rule recommendations.

---

# Business Problem

Many datasets received from clients have little or no documentation.

Data analysts spend significant time trying to determine:

- Which column uniquely identifies a record
- Whether duplicate IDs exist
- Whether a column can be trusted for joins
- Which field should be used as a Primary Key

The Primary Key Analyzer automates this process.

---

# Scope

Current version evaluates every column based on:

- NULL values
- Duplicate values
- Uniqueness
- Column naming convention (contains "ID")

The analyzer produces a ranked list of candidate primary keys.

---

# Inputs

Input:

- Pandas DataFrame

Example

| Order_ID | Customer_ID | Invoice_Amount | Order_Date | Email |
|----------|-------------|---------------|------------|--------|

---

# Output

Returns a list of candidate primary keys.

Example

```python
[
    {
        "column": "Order_ID",
        "score": 40,
        "confidence": "40%",
        "nulls": 0,
        "duplicates": 1,
        "unique_values": 4,
        "reasons": [
            "No NULL values",
            "Column name contains 'ID'"
        ]
    }
]
```

---

# Current Scoring Algorithm

| Rule | Score |
|------|------:|
| No NULL values | +30 |
| No Duplicate values | +40 |
| High Uniqueness | +20 |
| Column name contains "ID" | +10 |

Maximum Score = 100

---

# Current Workflow

```text
Dataset

↓

Loop through every column

↓

Calculate

• NULL Count

• Duplicate Count

• Unique Count

↓

Apply Scoring Rules

↓

Generate Candidate List

↓

Sort by Score

↓

Return Results
```

---

# Example Output

```
Column

Order_ID

Confidence

40%

Reasons

✓ No NULL values

✓ Column contains ID
```

---

# Assumptions

Current implementation assumes:

- Primary keys should not contain NULL values.
- Primary keys should ideally be unique.
- Identifier columns often contain "ID" in their names.

---

# Current Limitations

Current version does not:

- Detect composite primary keys.
- Understand business semantics.
- Consider data types.
- Evaluate uniqueness percentage intelligently.
- Detect surrogate keys.
- Detect UUIDs.

---

# Future Enhancements

Version 2

- Confidence based on uniqueness percentage.
- Detect UUID columns.
- Detect composite keys.
- Weight duplicate ratio.
- Data type awareness.

Version 3

- AI-assisted recommendations.
- Business entity detection.
- Explainable confidence scoring.

---

# Architecture

```text
CSV / Excel

↓

File Connector

↓

Profiler

↓

Primary Key Analyzer

↓

Validation Engine (Future)

↓

Rule Engine (Future)

↓

Trust Score (Future)
```

---

# Engineering Notes

Design Principles:

- Single Responsibility Principle
- Modular Architecture
- Analyzer Pattern
- Explainable AI approach
- Extensible Scoring Model

---

# Lessons Learned

- Metadata alone is insufficient for identifying primary keys.
- Explainability is more valuable than simply returning a score.
- Business semantics will significantly improve detection accuracy.
- Modular analyzers simplify future enhancements.

---

# Sprint Outcome

Status

✅ Successfully implemented

Deliverables

- Primary Key Analyzer
- Confidence Scoring
- Reason Generation
- Ranked Candidate Detection

---

# Next Sprint

Business Type Analyzer

Objectives

- Detect Email columns
- Detect Date columns
- Detect Currency columns
- Detect Phone Numbers
- Detect Identifiers
- Detect Product Codes

This analyzer will enable Sentinel to automatically recommend business validation rules.