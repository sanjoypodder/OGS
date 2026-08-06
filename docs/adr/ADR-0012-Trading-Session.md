# ADR-0012

## Title

Trading Session Domain Model

## Status

Accepted

## Decision

Trading sessions shall be represented by the `TradingSession` enum.

Each session provides:

- Name
- Start time (UTC)
- End time (UTC)
- Active status

Future enhancements will include:

- Kill Zones
- Market holidays
- Daylight saving adjustments
- Exchange calendars