# ADR-0009

## Title

Strongly Typed Market Symbols

## Status

Accepted

## Decision

All trading symbols inside OGS shall be represented by the Symbol enum.

Raw string symbols are prohibited within the application domain.

## Consequences

Advantages

- Type safety
- IDE autocomplete
- Easier testing
- Consistent APIs