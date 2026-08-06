# ADR-0019

## Title

Swing Validation

## Status

Accepted

## Decision

Every Swing object must be validated before being consumed by higher-level market structure algorithms.

Current validation rules:

- Index must be non-negative.
- Swing must reference a valid Candle.

## Rationale

Separating validation from detection keeps the detector focused on identifying swing points while allowing business rules to evolve independently.

## Consequences

- Consistent validation across Smart Money modules.
- Easier extension for future rules (confirmation strength, minimum distance, etc.).