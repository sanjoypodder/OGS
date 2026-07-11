# ADR-0003 – Application Orchestrator

## Status

Accepted

---

## Context

The application requires a single component responsible for coordinating startup, runtime, and shutdown.

---

## Decision

Introduce an `Application` class.

Responsibilities:

- Initialize subsystems
- Configure logging
- Load configuration
- Register engines
- Coordinate shutdown

The entry point (`app.py`) must remain minimal and contain no business logic.

---

## Consequences

Advantages

- Cleaner startup sequence
- Easier testing
- Better scalability
- Centralized lifecycle management
