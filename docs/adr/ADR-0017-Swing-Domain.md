# ADR-0017

## Title

Swing Domain Object

## Status

Accepted

## Decision

A confirmed market turning point is represented by an immutable `Swing` domain object.

A Swing contains:

- Index within the candle series
- Source candle
- Swing type (HIGH or LOW)

Future versions may extend the object with metadata such as strength, confirmation status, and market structure annotations.

## Consequences

- Strongly typed market structure model.
- Simplifies downstream algorithms (BOS, CHoCH, MSS).
- Maintains immutability and clear domain boundaries.