# ADR-0006

## Title

Service Container

## Status

Accepted

## Decision

Introduce a lightweight Service Container responsible for registering
and resolving shared services.

The initial implementation is intentionally simple and does not provide
full dependency injection.

## Consequences

Advantages

- Centralized service management
- Simple API
- Easy future expansion

Disadvantages

- Runtime type checking
- No automatic dependency injection