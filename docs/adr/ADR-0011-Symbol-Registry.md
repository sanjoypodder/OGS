# ADR-0011

## Title

Central Symbol Registry

## Status

Accepted

## Decision

All market metadata shall be stored in a centralized symbol registry.

The `Symbol` enum identifies the instrument.

`SymbolInfo` stores immutable metadata such as:

- Tick size
- Pip size
- Price precision
- Contract size
- Display name
- Quote currency

## Consequences

Advantages

- Single source of truth
- Easy broker integration
- Consistent validation
- Supports future exchanges and asset classes