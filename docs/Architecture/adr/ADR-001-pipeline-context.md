# ADR-001

# Pipeline Context

## Status

Accepted

---

## Context

Sentinel engines were passing multiple objects between one another.

Examples included:

- profile
- validation_output
- health_score
- trust_assessment
- execution_plan
- knowledge

As Sentinel grows, parameter lists become difficult to maintain and error-prone.

---

## Decision

Introduce a shared PipelineContext object.

Every engine receives one object.

Every engine updates the same object.

Example

Health Engine

context.profile

↓

context.health_score

Validation Engine

context.validation_output

↓

Health Engine

No engine passes multiple parameters.

---

## Consequences

Advantages

• Cleaner APIs

• Easier testing

• Consistent engine lifecycle

• Simpler pipeline orchestration

Trade-offs

• Requires incremental migration

• Shared state must be managed carefully

Future

PipelineContext becomes the foundation for

- REST API
- Web UI
- Plugins
- HTML Reports