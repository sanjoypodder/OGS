# Break of Structure (BOS)

**Package Name:** BOS (Break of Structure)

**Package Path:** `src/ogs/smart_money/bos`

**Version:** 0.0.1

---

# Overview

The **Break of Structure (BOS)** package is responsible for detecting confirmed structural breaks within market price action. A Break of Structure represents the continuation of an existing market trend after price successfully closes beyond a previously identified swing level.

The package consumes market candles together with previously detected swing points and produces a collection of confirmed BOS events. These events become foundational inputs for higher-level Smart Money concepts such as Change of Character (CHOCH), Order Blocks, Mitigation, and Liquidity analysis. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

---

# Design Goals

The BOS package is designed to:

- Detect bullish and bearish Break of Structure events.
- Operate on confirmed swing structures.
- Produce immutable BOS domain objects.
- Provide reusable validation mechanisms.
- Support future expansion for additional BOS detection rules.
- Integrate cleanly with other Smart Money packages.

---

# Package Structure

```
smart_money/bos
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
├── validator.py
├── README.md
└── conftest.py
```

---

# Package Components

## BOS

The central domain model representing a confirmed Break of Structure.

A BOS object stores:

- confirmation candle
- broken swing
- BOS direction

The implementation is immutable (`frozen=True`) and uses `slots=True`, making it suitable as a lightweight domain object. It also exposes convenience properties for the event timestamp and broken swing price. :contentReference[oaicite:3]{index=3}

---

## BOSAnalyzer

`BOSAnalyzer` performs the core detection process.

It accepts:

- CandleSeries
- SwingSeries

and produces:

- BOSSeries

The implementation iterates over each detected swing and evaluates subsequent candles to determine whether a valid bullish or bearish structural break has occurred.

Current detection logic:

- Bullish BOS → candle closes above a Swing High.
- Bearish BOS → candle closes below a Swing Low.

The analyzer returns an empty collection if either input is missing or contains no data. :contentReference[oaicite:4]{index=4}

---

## BOSSeries

A specialized collection for BOS domain objects.

It extends the Smart Money `BaseCollection` and adds BOS-specific operations including:

- direct access to the underlying BOS structures
- append support
- retrieval of the most recent BOS events

This keeps collection management encapsulated within the BOS package. :contentReference[oaicite:5]{index=5}

---

## BOSType

Defines the direction of a Break of Structure.

Current values:

- `BULLISH`
- `BEARISH`

The implementation uses Python's `StrEnum`, providing readable string values while maintaining enumeration semantics. :contentReference[oaicite:6]{index=6}

---

## BOSValidator

Provides validation for BOS domain objects.

The current implementation verifies that:

- the BOS instance exists
- a confirmation candle is present
- the broken swing reference exists

Validation failures raise `ValueError`. :contentReference[oaicite:7]{index=7}

---

## BOSStatistics

Reserved for future statistical analysis of BOS events.

The class currently inherits from `BaseStatistics` without adding additional behavior. :contentReference[oaicite:8]{index=8}

---

## BOSDTO

Placeholder object reserved for serialization and data transfer responsibilities.

The current implementation contains no fields or logic. :contentReference[oaicite:9]{index=9}

---

## Exception Hierarchy

The package defines a dedicated exception hierarchy.

```
Exception
    │
    └── BOSError
            │
            └── InvalidBOSError
```

This hierarchy allows BOS-specific errors to be handled independently from other Smart Money modules. :contentReference[oaicite:10]{index=10}

---

## Interfaces

The package exposes a protocol describing the analyzer contract.

The protocol specifies that implementations analyze candle series and return a `BOSSeries`, providing a structural typing interface for BOS analyzers. :contentReference[oaicite:11]{index=11}

---

## Constants

The package defines configurable BOS detection options.

Current constants include:

- `REQUIRE_CLOSE_BREAK`
- `ALLOW_EQUAL_BREAK`

These values centralize behavioral configuration for BOS detection. :contentReference[oaicite:12]{index=12}

---

# Detection Workflow

```
CandleSeries
        │
        ▼
Swing Detection
        │
        ▼
SwingSeries
        │
        ▼
BOSAnalyzer
        │
        ▼
Break Detection
        │
        ▼
BOS Objects
        │
        ▼
BOSSeries
```

This reflects the implemented dependency where BOS analysis consumes both market candles and previously identified swings. :contentReference[oaicite:13]{index=13}

---

# Package Dependencies

```
Market
   │
   ▼
Swing
   │
   ▼
BOS
```

Current implementation dependencies:

- Market package
- Smart Money Base package
- Swing package

The BOS package does not currently depend on CHOCH, Order Block, Liquidity, or other higher-level Smart Money concepts. 

---

# Testing

The package includes pytest fixtures supporting BOS testing.

Current fixtures provide reusable objects for:

- Symbol
- Timeframe
- Swing High
- Swing Low
- SwingSeries
- CandleSeries

These fixtures establish a consistent testing foundation for analyzer and validator behavior. :contentReference[oaicite:15]{index=15}

---

# Current Implementation Status

| Component | Status |
|-----------|--------|
| Domain Model | Implemented |
| Analyzer | Implemented |
| Collection | Implemented |
| Enum | Implemented |
| Validator | Implemented |
| Constants | Implemented |
| Interface | Implemented |
| Exceptions | Implemented |
| Statistics | Initial implementation |
| DTO | Placeholder |
| Tests | Initial fixtures implemented |

---

# Summary

The **BOS** package provides the first complete Smart Money detection module within OGS. It transforms market candles and swing structures into confirmed Break of Structure events using a clear separation between domain models, analysis logic, validation, collections, and supporting infrastructure. This modular design makes the package reusable, extensible, and well positioned for integration with higher-level Smart Money concepts such as CHOCH and Order Blocks.