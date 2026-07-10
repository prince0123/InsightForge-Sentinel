# Sprint 04 - Business Type Analyzer

---

## Sprint ID

IF-004

---

## Release

v0.4.0

---

## Status

✅ Completed

---

# Objective

Develop a Business Type Analyzer capable of identifying the business meaning of dataset columns and recommending validation rules automatically.

---

# Business Problem

Most data quality tools require users to manually configure validation rules.

Sentinel aims to reduce this effort by understanding the business meaning of columns before validation.

Example

Order_ID → Identifier

Invoice_Amount → Currency

Email → Email Address

Order_Date → Date

---

# Features Implemented

- Business Type Detection
- Keyword-based Classification
- Recommended Validation Rules
- Structured Analyzer Output
- Console Reporting

---

# Supported Business Types

| Business Type | Example |
|---------------|---------|
| Identifier | Order_ID |
| Email Address | Email |
| Date | Order_Date |
| Currency | Invoice_Amount |
| Phone Number | Mobile |
| Quantity | Quantity |
| Percentage | Discount |
| Product SKU | SKU |

---

# Current Detection Strategy

Current Version

- Column Name Matching

Future Versions

- Value Pattern Detection
- Regex Detection
- Data Type Detection
- AI-assisted Classification

---

# Example Output

Business Type

Currency

Confidence

95%

Recommended Rules

- Cannot be Negative
- Detect Outliers

---

# Architecture

CSV

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

---

# Deliverables

- BusinessTypeAnalyzer
- ConsoleReporter
- Updated Main Application

---

# Known Limitations

- Detection based only on column names.
- Confidence is static.
- Does not inspect sample values.

---

# Future Improvements

- Value Pattern Detection
- Regex Engine
- Confidence Scoring
- AI Classification

---

# Sprint Outcome

Status

✅ Completed

Release

v0.4.0