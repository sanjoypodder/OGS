# ADR-0008

## Title

Kernel Lifecycle

---

## Status

Accepted

---

## Context

OGS requires a deterministic application lifecycle.

---

## Decision

The application lifecycle shall always be:

STOPPED

↓

INITIALIZING

↓

RUNNING

↓

SHUTTING_DOWN

↓

STOPPED

---

## Consequences

Advantages

- Predictable startup
- Predictable shutdown
- Easy testing
- Future service orchestration