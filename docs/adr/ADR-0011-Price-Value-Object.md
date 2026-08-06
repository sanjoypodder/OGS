# ADR-0011

## Title

Immutable Price Value Object

## Status

Accepted

## Decision

Prices within OGS shall be represented by an immutable `Price` value object backed by Python's `Decimal` type.

Raw `float` values are prohibited within the application domain.

## Rationale

- Avoid floating-point precision errors.
- Provide consistent rounding.
- Support future tick-size validation and broker-specific precision.
- Make arithmetic and comparisons reliable.

## Consequences

- Improved numerical correctness.
- Easier extension for risk calculations and order validation.
- Slightly more object creation, which is acceptable for correctness.