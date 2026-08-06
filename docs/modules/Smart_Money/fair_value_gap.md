# Fair Value Gap (FVG)

**Package Name:** Fair Value Gap (FVG)

**Package Path:** `src/ogs/smart_money/fair_value_gap`

**Version:** 0.0.1

---

# Overview

The **Fair Value Gap (FVG)** package is responsible for detecting institutional Fair Value Gaps within market price action.

A Fair Value Gap represents a price imbalance created when a three-candle sequence leaves an untraded price region between the first and third candles. The package analyzes sequential market candles, identifies bullish and bearish Fair Value Gaps, and represents each detected imbalance as an immutable domain object.

The package follows the modular architecture of the OGS Smart Money Framework by separating analysis, domain modelling, collections, validation, statistics, and supporting components. 

---

# Design Goals

The Fair Value Gap package is designed to:

- Detect bullish and bearish Fair Value Gaps.
- Produce immutable Fair Value Gap domain objects.
- Maintain reusable collections of detected gaps.
- Validate detected gap structures.
- Provide statistical summaries of Fair Value Gaps.
- Support future extensions without changing existing public interfaces.

---

# Package Structure

```
smart_money/fair_value_gap
│
├── __init__.py
├── analyzer.py
├── collection.py
├── domain.py
├── enums.py
├── statistics.py
└── validator.py
```

---

# Package Components

## FairValueGap

`FairValueGap` is the domain model representing a detected Fair Value Gap.

Each object stores:

- first candle
- middle candle
- last candle
- gap direction
- top boundary
- bottom boundary
- midpoint
- gap size
- fill status
- fill timestamp

The implementation uses an immutable dataclass (`frozen=True`) with `slots=True` and provides convenience properties to determine whether the gap is bullish or bearish. :contentReference[oaicite:1]{index=1}

---

## FairValueGapAnalyzer

`FairValueGapAnalyzer` performs Fair Value Gap detection.

The analyzer processes sequential candle data and evaluates every three-candle window.

Current detection rules are:

### Bullish Fair Value Gap

A bullish gap is detected when:

```
Last Candle Low > First Candle High
```

The resulting gap boundaries are calculated from:

- Top = Last Candle Low
- Bottom = First Candle High

---

### Bearish Fair Value Gap

A bearish gap is detected when:

```
Last Candle High < First Candle Low
```

The resulting gap boundaries are calculated from:

- Top = First Candle Low
- Bottom = Last Candle High

Each detected imbalance is converted into a `FairValueGap` object and added to the resulting collection. :contentReference[oaicite:2]{index=2}

---

## FairValueGapSeries

`FairValueGapSeries` is the collection class for Fair Value Gap objects.

It extends the Smart Money `BaseCollection` and provides:

- storage of detected gaps
- append operation
- retrieval of recent gaps
- direct access to the underlying collection

This encapsulates collection management within the package. :contentReference[oaicite:3]{index=3}

---

## FairValueGapDirection

Defines the direction of a Fair Value Gap.

Current values are:

- `BULLISH`
- `BEARISH`

The enumeration identifies the directional bias associated with each detected Fair Value Gap. :contentReference[oaicite:4]{index=4}

---

## FairValueGapValidator

Validates Fair Value Gap objects.

The current implementation verifies:

- gap object exists
- first candle exists
- middle candle exists
- last candle exists
- direction exists
- top boundary is greater than or equal to bottom boundary
- gap size is not negative

The validator returns a boolean result indicating whether the gap satisfies these conditions. :contentReference[oaicite:5]{index=5}

---

## FairValueGapStatistics

Provides statistical information for a collection of Fair Value Gaps.

Current statistics include:

- total gaps
- bullish gaps
- bearish gaps
- filled gaps
- unfilled gaps

The statistics are calculated dynamically from the associated collection. :contentReference[oaicite:6]{index=6}

---

# Detection Workflow

```
Candles
    │
    ▼
Three-Candle Window
    │
    ▼
Gap Detection
    │
    ▼
FairValueGap
    │
    ▼
FairValueGapSeries
```

The current implementation evaluates each consecutive three-candle sequence and creates a Fair Value Gap whenever the required bullish or bearish conditions are satisfied. :contentReference[oaicite:7]{index=7}

---

# Package Dependencies

```
Market
   │
   ▼
Smart Money Base
   │
   ▼
Fair Value Gap
```

Current implementation depends on:

- Market package
- Smart Money Base package

The analyzer currently operates directly on market candle data and produces a `FairValueGapSeries`. 

---

# Design Principles

The package demonstrates the following architectural principles:

- Immutable domain modelling.
- Separation of analysis and validation.
- Collection-oriented design.
- Dedicated statistical reporting.
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
| Statistics | Implemented |

---

# Summary

The **Fair Value Gap** package provides a complete implementation for detecting institutional price imbalances within the OGS Smart Money Framework. It analyzes sequential candle data, identifies bullish and bearish Fair Value Gaps, and represents them as validated domain objects supported by reusable collections and statistical reporting. The package follows the common architectural conventions established across the Smart Money framework while remaining focused on Fair Value Gap detection and representation.