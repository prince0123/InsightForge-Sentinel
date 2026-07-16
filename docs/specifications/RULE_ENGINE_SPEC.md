# Rule Engine Specification

Document ID: IF-SPEC-001

Product: InsightForge Sentinel

Component: Rule Engine

Version: 1.0

Status: Approved

Last Updated: July 2026

---

# Purpose

The Rule Engine is responsible for selecting, executing, and evaluating business validation rules against a dataset.

The Rule Engine does not understand datasets.

The Rule Engine does not infer business meaning.

It simply executes rules using the knowledge produced by previous engines.

---

# Position in Sentinel Architecture

                Data Ingestion
                        │
                        ▼
             Preprocessing Engine
                        │
                        ▼
              Profiling Engine
                        │
                        ▼
              Inference Engine
                        │
                        ▼
               Knowledge Model
                        │
                        ▼
                  Rule Engine
                        │
                        ▼
              Validation Engine
                        │
                        ▼
                 Trust Engine
                        │
                        ▼
           Recommendation Engine
                        │
                        ▼
                 Report Engine

---

# Responsibilities

The Rule Engine SHALL

- Load rule packs
- Select applicable rules
- Execute rule logic
- Return standardized validation results

The Rule Engine SHALL NOT

- Read files
- Infer business types
- Generate reports
- Calculate trust scores
- Recommend fixes

---

# Inputs

Required

Knowledge Model

Optional

Rule Pack

Execution Configuration

Industry Profile

---

# Outputs

Validation Results

Example

{
    "status": "SUCCESS",
    "rules_executed": 27,
    "passed": 24,
    "failed": 3,
    "results": [...]
}

---

# Rule Lifecycle

Rule Loaded

↓

Applicability Check

↓

Execute Validation

↓

Collect Result

↓

Determine Severity

↓

Store Result

↓

Return

---

# Rule Structure

Every rule must contain

Rule ID

Rule Name

Description

Applicable Business Type

Validation Type

Operator

Expected Value

Severity

Business Impact

Recommendation

Enabled

Version

Owner

---

# Example Rule

{
    "rule_id": "RET-001",

    "name": "Order ID must be unique",

    "business_type": "Identifier",

    "validation": "UNIQUE",

    "severity": "HIGH",

    "business_impact":
        "Duplicate orders may inflate revenue reporting.",

    "recommendation":
        "Remove duplicate Order_ID values.",

    "enabled": true,

    "version": "1.0"
}

---

# Rule Categories

Identifier Rules

Examples

Unique

Not NULL

Pattern

Length

---

Currency Rules

Examples

Positive Value

Range

Outlier

Decimal Precision

---

Date Rules

Examples

Not Future

Valid Date

Business Day

Minimum Date

Maximum Date

---

Email Rules

Examples

Valid Format

Corporate Domain

Not NULL

Maximum Length

---

Phone Rules

Examples

Country Code

Length

Numeric

---

Text Rules

Examples

Minimum Length

Maximum Length

Allowed Characters

Regex

---

Boolean Rules

Examples

Valid Boolean

Allowed Values

---

Custom Rules

Organization-specific validations.

---

# Supported Operators

EQUALS

NOT_EQUALS

GREATER_THAN

LESS_THAN

BETWEEN

REGEX

UNIQUE

NOT_NULL

IN_LIST

NOT_IN_LIST

FUTURE_DATE

PAST_DATE

CUSTOM

---

# Rule Execution Flow

For each column

↓

Read Business Type

↓

Find Matching Rules

↓

Execute Rules

↓

Collect Results

↓

Return Validation Results

---

# Rule Packs

Rule packs are grouped by industry.

rules/

retail/

banking/

healthcare/

human_resources/

customer_support/

common/

---

# Rule Pack Example

Retail

Order_ID

Unique

Invoice_Amount

Positive

Order_Date

Not Future Date

Email

Valid Email

---

# Severity Levels

LOW

Minor issue

---

MEDIUM

May affect reporting quality

---

HIGH

Likely to affect business processes

---

CRITICAL

Data should not be used until corrected

---

# Validation Result Standard

Every validation returns

Rule ID

Column

Status

Severity

Confidence

Message

Business Impact

Recommendation

Execution Time

---

# Performance Goals

Support datasets

100 Rows

< 1 second

10,000 Rows

< 3 seconds

100,000 Rows

< 10 seconds

Future optimization

Parallel execution

---

# Extensibility

New rules must be added without modifying Rule Engine source code.

Supported extension methods

JSON Rule Packs

YAML Rule Packs

Database Rule Repository (future)

REST API Rule Repository (future)

---

# Error Handling

Invalid rule format

Skip rule

Log warning

Continue execution

---

Missing column

Skip rule

Return informational message

---

Unsupported operator

Fail rule safely

Log diagnostic information

---

# Engineering Principles

The Rule Engine should

Be deterministic

Be explainable

Be configurable

Be testable

Be independent of industry

---

# Future Enhancements

Rule Dependencies

Conditional Rules

Cross-table Validation

Rule Priorities

Rule Versioning

Rule Marketplace

AI-generated Rules

---

# Definition of Done

The Rule Engine is complete when

- Rules load successfully
- Rules execute correctly
- Validation results are standardized
- Rule packs require no code changes
- Unit tests pass
- Documentation is updated