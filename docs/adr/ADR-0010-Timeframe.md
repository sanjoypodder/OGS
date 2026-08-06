# ADR-0010

## Title

Strongly Typed Timeframes

## Status

Accepted

## Decision

All market timeframes shall be represented using the Timeframe enum.

The enum provides:

- Duration
- Seconds
- Human-readable labels
- Intraday classification
- Higher timeframe navigation

This replaces raw string usage throughout OGS.