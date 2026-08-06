# OGS FinOS

# Dealing Range Module

Version **0.0.2**

---

## Overview

The **Dealing Range Module** is a foundational component of the OGS FinOS Smart Money architecture.

A dealing range represents the institutional trading range formed by a confirmed Swing High and Swing Low.

It provides the reference range used by multiple downstream Smart Money concepts including:

- Premium / Discount
- Fibonacci Retracement
- Optimal Trade Entry (OTE)
- Balanced Price Range (BPR)
- Liquidity Analysis
- Execution Engine

This module is intentionally responsible only for constructing and representing institutional dealing ranges. It does not detect market structure or swings.

---

# Institutional Concept

Institutional traders divide every confirmed dealing range into regions.

```
Swing High
    │
    │ Premium
    │
────┼──────── Equilibrium (50%)
    │
    │ Discount
    │
Swing Low
```

The midpoint (Equilibrium) separates Premium and Discount and acts as the primary reference for institutional execution models.

---

# Architecture

```
Market Structure
        │
        ▼
Confirmed Swing High
Confirmed Swing Low
        │
        ▼
DealingRangeAnalyzer
        │
        ▼
DealingRange
        │
        ├────────► Premium / Discount
        ├────────► Fibonacci
        ├────────► OTE
        ├────────► BPR
        ├────────► Liquidity
        └────────► Execution
```

The module assumes Swing High and Swing Low have already been confirmed by the Market Structure module.

---

# Package Structure

```
dealing_range/

├── analyzer/
├── collection/
├── domain/
├── enums/
├── factory/
├── statistics/
├── validator/

README.md
```

---

# Components

## Domain

Represents an immutable institutional dealing range.

Properties include:

- UUID
- Range High
- Range Low
- Equilibrium
- Direction
- Start Index
- End Index
- Metadata
- Timestamp

Computed properties:

- Range Size
- Bullish
- Bearish
- Sideways

---

## Collection

Stores multiple immutable DealingRange objects.

Supported operations:

- add()
- extend()
- latest()
- clear()
- get_by_id()
- iteration
- indexing
- containment

---

## Validator

Performs structural validation.

Validation rules include:

- Positive prices
- High > Low
- Equilibrium inside range
- Positive range size
- Valid index order
- Valid direction

No market logic is performed.

---

## Statistics

Provides read-only summaries.

Available statistics:

- Total Ranges
- Bullish Count
- Bearish Count
- Sideways Count
- Average Range Size
- Maximum Range
- Minimum Range

---

## Analyzer

Constructs immutable DealingRange objects from confirmed Swing High and Swing Low values.

Responsibilities:

- Calculate Equilibrium
- Build immutable domain object
- Return collection

The analyzer does not detect market structure.

---

## Factory

Provides standardized construction of analyzers.

```
DealingRangeFactory
        │
        ▼
DealingRangeAnalyzer
```

---

# Public API

```python
from ogs.smart_money.dealing_range import (
    DealingRangeFactory,
)

analyzer = (
    DealingRangeFactory.create_analyzer()
)

collection = analyzer.analyze(
    swing_high=2100,
    swing_low=2000,
    start_index=15,
    end_index=42,
    direction=DealingRangeDirection.BULLISH,
)
```

---

# Design Principles

This module follows the OGS FinOS architecture.

- Immutable Domain Objects
- Single Responsibility Principle
- Dependency Injection Friendly
- Layered Architecture
- Strong Typing
- Test Driven Development
- No Hidden State

---

# Dependencies

The module depends on:

- Python 3.14+
- Decimal
- UUID
- Dataclasses
- datetime
- OGS Smart Money Core

No third-party libraries are required.

---

# Unit Testing

Current status:

```
43 Passed
0 Failed
0 Skipped
```

Coverage includes:

- Domain
- Collection
- Validator
- Statistics
- Factory
- Analyzer

---

# Future Enhancements

Version 1.x may include:

- Automatic direction inference
- Multi-leg dealing ranges
- Nested dealing ranges
- Multi-timeframe dealing ranges
- Session-aware ranges
- Liquidity metadata
- Internal dealing ranges

These enhancements are intentionally deferred until after Version 1.0 to preserve architectural stability.

---

# Version History

## v0.0.2

Initial implementation.

Completed:

- Scaffold
- Enums
- Domain
- Collection
- Validator
- Statistics
- Analyzer
- Factory
- Unit Tests
- Documentation

Status:

Production Ready