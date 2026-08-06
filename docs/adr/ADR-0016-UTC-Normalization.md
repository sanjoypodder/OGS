# ADR-0016

## Title

UTC Timestamp Normalization

## Status

Accepted

## Decision

All timestamps inside OGS are stored and processed in UTC.

Market data received from external sources must be normalized before analysis.

## Rationale

Using a single internal timezone eliminates ambiguity caused by broker-specific local times, daylight saving changes, and exchange timezones.

## Consequences

- Consistent analysis across brokers.
- Simpler backtesting.
- Reliable session calculations.