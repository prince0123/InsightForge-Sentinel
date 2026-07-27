# ADR-002

# Base Engine

## Context

Every engine implemented its own lifecycle.

This resulted in inconsistent execution patterns.

---

## Decision

Introduce BaseEngine.

Every engine implements

run(context)

Only.

---

## Consequences

Advantages

Uniform architecture.

Simpler onboarding.

Consistent testing.

Future plugin support.