# ADR-0014

## Title

Market Validation Layer

## Status

Accepted

## Decision

All broker market data must pass through the Market Validation Layer before being consumed by any analysis engine.

The validation layer is responsible for:

- Candle integrity
- Timestamp validation
- Duplicate removal
- Gap detection
- UTC normalization

## Rationale

Separating validation from analysis ensures that all downstream engines operate on trusted market data.

## Consequences

- Improved reliability of Smart Money algorithms.
- Cleaner separation of responsibilities.
- Easier testing and debugging.