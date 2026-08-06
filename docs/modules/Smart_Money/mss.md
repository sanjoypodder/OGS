# Market Structure Shift (MSS)

**Package Name:** Market Structure Shift (MSS)

**Package Path:** `src/ogs/smart_money/mss`

**Version:** 0.0.1

---

# Overview

The **Market Structure Shift (MSS)** package is responsible for detecting confirmed Market Structure Shift events within the OGS Smart Money Framework.

The current implementation analyzes previously detected **Change of Character (CHOCH)** events and identifies directional reversals that confirm a Market Structure Shift. Each detected MSS is represented as an immutable domain object and organized into reusable collections for subsequent Smart Money analysis.

The package follows the modular architecture of the OGS Smart Money Framework by separating analysis, domain modelling, collections, validation, statistics, interfaces, constants, exceptions, and supporting components. 

---

# Design Goals

The MSS package is designed to:

- Detect bullish and bearish Market Structure Shifts.
- Operate on confirmed CHOCH events.
- Produce immutable MSS domain objects.
- Validate detected MSS structures.
- Support future statistical analysis.
- Maintain consistency with other Smart Money packages.

---

# Package Structure

```text
smart_money/mss
│
├── __init__.py
├── analyzer.py
├── collection.py
├── constants.py
├── domain.py
├── dto.py
├── enums.py
├── exceptions.py
├── interfaces.py
├── statistics.py
└── validator.py
```

---

# Package Components

## MSS

`MSS` is the domain model representing a confirmed Market Structure Shift.

Each object stores:

- confirmation candle
- triggering CHOCH
- MSS direction

The implementation is an immutable dataclass (`frozen=True`) with `slots=True` and provides convenience properties for retrieving the event timestamp and price. :contentReference[oaicite:1]{index=1}

---

## MSSAnalyzer

`MSSAnalyzer` performs Market Structure Shift detection.

The analyzer accepts a `CHOCHSeries` and returns an `MSSSeries`.

The current implementation detects:

### Bullish MSS

A bullish MSS is created when:

```
Bearish CHOCH → Bullish CHOCH
```

---

### Bearish MSS

A bearish MSS is created when:

```
Bullish CHOCH → Bearish CHOCH
```

If the input is `None` or contains fewer than two CHOCH events, an empty collection is returned. :contentReference[oaicite:2]{index=2}

---

## MSSSeries

`MSSSeries` is the collection class for MSS objects.

It extends the Smart Money `BaseCollection` and provides:

- storage of MSS objects
- append operation
- retrieval of recent MSS events
- access to the underlying collection

:contentReference[oaicite:3]{index=3}

---

## MSSType

Defines the direction of a Market Structure Shift.

Current values are:

- `BULLISH`
- `BEARISH`

The implementation uses Python's `StrEnum`. :contentReference[oaicite:4]{index=4}

---

## MSSValidator

The package exports an `MSSValidator` as part of its public API. The validator implementation was not included in the uploaded files, so its internal validation rules cannot be documented from the available implementation. :contentReference[oaicite:5]{index=5}

---

## MSSStatistics

The package exports an `MSSStatistics` component as part of its public API. Its implementation was not included in the uploaded files, so its statistical calculations cannot be described from the current upload. :contentReference[oaicite:6]{index=6}

---

## MSSDTO

`MSSDTO` is currently a placeholder reserved for future serialization and data transfer responsibilities. :contentReference[oaicite:7]{index=7}

---

## Exception Hierarchy

The package defines a dedicated exception hierarchy:

```text
Exception
    │
    └── MSSError
            │
            └── InvalidMSSError
```

This enables MSS-specific error handling independent of other Smart Money modules. :contentReference[oaicite:8]{index=8}

---

## Interfaces

The package defines `MSSAnalyzerProtocol`, specifying that analyzer implementations accept a `CHOCHSeries` and return an `MSSSeries`. :contentReference[oaicite:9]{index=9}

---

## Constants

The package defines configurable detection options:

- `REQUIRE_CHOCH_CONFIRMATION`
- `REQUIRE_CONFIRMATION_BOS`

These constants centralize configuration for MSS confirmation requirements. :contentReference[oaicite:10]{index=10}

---

# Detection Workflow

```text
CHOCHSeries
      │
      ▼
MSSAnalyzer
      │
      ▼
Direction Change Detection
      │
      ▼
MSS
      │
      ▼
MSSSeries
```

The current implementation evaluates sequential CHOCH events and creates an MSS whenever the CHOCH direction reverses. :contentReference[oaicite:11]{index=11}

---

# Package Dependencies

```text
Market
   │
   ▼
CHOCH
   │
   ▼
MSS
```

Current implementation depends on:

- Market package
- Smart Money Base package
- CHOCH package

The analyzer consumes `CHOCHSeries` and produces `MSSSeries`. 

---

# Design Principles

The package demonstrates the following architectural principles:

- Immutable domain modelling.
- Separation of analysis and validation.
- Collection-oriented design.
- Protocol-based abstraction.
- Modular Smart Money architecture.
- Framework reuse through the Smart Money Base package.

---

# Current Implementation Status

| Component | Status |
|-----------|--------|
| Domain Model | Implemented |
| Analyzer | Implemented |
| Collection | Implemented |
| Enumeration | Implemented |
| Constants | Implemented |
| Interface | Implemented |
| Exceptions | Implemented |
| DTO | Placeholder |
| Validator | Exported (implementation not included) |
| Statistics | Exported (implementation not included) |

---

# Summary

The **Market Structure Shift (MSS)** package provides the implementation for detecting confirmed Market Structure Shift events within the OGS Smart Money Framework. It transforms confirmed Change of Character events into validated MSS domain objects while maintaining a clear separation between analysis, domain modelling, collections, interfaces, configuration, and supporting infrastructure. The current implementation builds directly upon the CHOCH package, forming the next stage of market structure analysis.