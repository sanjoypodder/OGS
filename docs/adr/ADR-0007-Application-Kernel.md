# ADR-0007

## Title

Application Kernel

## Status

Accepted

## Decision

Introduce a dedicated Application class responsible for coordinating the lifecycle of OGS.

The Application owns:

- Service Container
- Startup Manager
- Shutdown Manager

It does not implement business logic.

## Consequences

Advantages

- Centralized lifecycle
- Easier testing
- Cleaner architecture
- Better scalability