# ADR-0015

## Title

Duplicate Candle Detection

## Status

Accepted

## Decision

Duplicate candles are identified by their timestamp.

The detector returns immutable `Duplicate` domain objects rather than raw indices.

## Rationale

Using domain objects makes the API extensible. Additional metadata such as broker, severity, or recovery status can be added without changing the detector interface.