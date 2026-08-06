# Change of Character (CHOCH)

**Package Name:** CHOCH (Change of Character)

**Package Path:** `src/ogs/smart_money/choch`

**Version:** 0.0.1

---

# Overview

The **Change of Character (CHOCH)** package is responsible for identifying changes in market structure based on previously detected Break of Structure (BOS) events.

The package analyzes sequences of BOS events and identifies directional transitions that represent a confirmed Change of Character. Each detected CHOCH is represented as an immutable domain object and organized into reusable collections for subsequent Smart Money analysis.

The package follows the same modular architecture used throughout the Smart Money Framework by separating analysis, domain modelling, collections, validation, statistics, interfaces, and supporting components. 

---

# Design Goals

The CHOCH package is designed to:

- Detect bullish and bearish Change of Character events.
- Operate on confirmed Break of Structure events.
- Produce immutable CHOCH domain objects.
- Validate detected CHOCH structures.
- Support future statistical analysis.
- Maintain consistency with other Smart Money packages.

---

# Package Structure

```
smart_money/choch
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

## CHOCH

The `CHOCH` domain model represents a confirmed Change of Character.

Each object contains:

- confirmation candle
- broken BOS
- CHOCH direction

The implementation is an immutable dataclass (`frozen=True`) using `slots=True` and provides convenience properties for the event timestamp and price. :contentReference[oaicite:1]{index=1}

---

## CHOCHAnalyzer

`CHOCHAnalyzer` performs the detection of Change of Character events.

The analyzer accepts a `BOSSeries` as input and returns a `CHOCHSeries`.

The current implementation detects:

- Bearish BOS → Bullish BOS → Bullish CHOCH
- Bullish BOS → Bearish BOS → Bearish CHOCH

If the input is `None` or contains fewer than two BOS events, an empty result is returned. :contentReference[oaicite:2]{index=2}

---

## CHOCHSeries

`CHOCHSeries` is the collection class for CHOCH objects.

It extends the Smart Money `BaseCollection` and provides:

- storage of CHOCH objects
- append operation
- access to the underlying collection
- retrieval of the latest CHOCH events

:contentReference[oaicite:3]{index=3}

---

## CHOCHType

Defines the direction of a Change of Character.

Current values are:

- `BULLISH`
- `BEARISH`

The implementation uses Python's `StrEnum`. :contentReference[oaicite:4]{index=4}

---

## CHOCHValidator

Validates CHOCH objects.

The current implementation verifies:

- CHOCH object exists
- confirmation candle exists
- broken BOS reference exists

Validation failures raise `ValueError`. :contentReference[oaicite:5]{index=5}

---

## CHOCHStatistics

Provides the statistical foundation for CHOCH analysis.

The current implementation inherits from `BaseStatistics` and is reserved for future expansion. :contentReference[oaicite:6]{index=6}

---

## CHOCHDTO

Placeholder object reserved for serialization and data transfer responsibilities.

The current implementation contains no fields or behavior. :contentReference[oaicite:7]{index=7}

---

## Exception Hierarchy

The package defines its own exception hierarchy.

```
Exception
    │
    └── CHOCHError
            │
            └── InvalidCHOCHError
```

This allows CHOCH-specific errors to be handled independently from other Smart Money modules. :contentReference[oaicite:8]{index=8}

---

## Interfaces

The package exposes an analyzer protocol defining the expected analyzer contract.

The protocol specifies that implementations accept a `BOSSeries` and return a `CHOCHSeries`. :contentReference[oaicite:9]{index=9}

---

## Constants

The package defines configurable detection options.

Current constants include:

- `REQUIRE_BOS_CONFIRMATION`
- `ALLOW_EQUAL_BREAK`

These constants centralize configurable behavior for CHOCH detection. :contentReference[oaicite:10]{index=10}

---

# Detection Workflow

```
BOSSeries
     │
     ▼
CHOCHAnalyzer
     │
     ▼
Direction Change Detection
     │
     ▼
CHOCH
     │
     ▼
CHOCHSeries
```

The current implementation analyzes sequential BOS events and creates CHOCH objects whenever the BOS direction changes. :contentReference[oaicite:11]{index=11}

---

# Package Dependencies

```
Market
   │
   ▼
BOS
   │
   ▼
CHOCH
```

Current implementation depends on:

- Market package
- Smart Money Base package
- BOS package

The analyzer directly consumes `BOSSeries` and produces `CHOCHSeries`. 

---

# Design Principles

The package demonstrates the following architectural principles:

- Immutable domain modelling.
- Separation of analysis and validation.
- Collection-oriented design.
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
| Validator | Implemented |
| Constants | Implemented |
| Interface | Implemented |
| Exceptions | Implemented |
| Statistics | Initial implementation |
| DTO | Placeholder |

---

# Summary

The **CHOCH** package provides a complete implementation for detecting Change of Character events within the OGS Smart Money Framework. It transforms confirmed Break of Structure events into validated CHOCH domain objects while maintaining a clear separation between analysis, domain modelling, validation, collections, and supporting infrastructure. The package integrates naturally with the BOS package and establishes the next stage of market structure analysis.