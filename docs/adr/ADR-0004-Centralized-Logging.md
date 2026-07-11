# ADR-0004

## Title

Centralized Logging

## Status

Accepted

## Decision

Every module in OGS shall use the central logger.

No module shall directly call print() for operational logging.

## Consequences

- Consistent logging
- Easier debugging
- Rotating log files
- Centralized diagnostics
