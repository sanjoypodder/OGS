# ADR-0005

## Title

Environment Validation

## Status

Accepted

## Decision

OGS must validate its runtime environment before starting.

Checks include:

- Python version
- Project structure
- Required packages
- Write permissions
- Virtual environment

## Consequences

Advantages

- Faster debugging
- Reliable startup
- Better diagnostics
- Consistent deployment
