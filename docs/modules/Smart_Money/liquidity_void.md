# Liquidity Void

**Package Name:** Liquidity Void

**Package Path:** `src/ogs/smart_money/liquidity_void`

**Version:** 0.0.1

---

# Overview

The **Liquidity Void** package is responsible for detecting institutional Liquidity Voids within market price action.

A Liquidity Void represents a rapidly traversed price region where little or no trading activity occurred, leaving an inefficient area between candles. The current implementation identifies Liquidity Voids using a three-candle imbalance model and represents each detected void as an immutable domain object.

The package follows the modular architecture of the OGS Smart Money Framework by separating analysis, domain modelling, collections, validation, statistics, and supporting enumerations. 

---

# Design Goals

The Liquidity Void package is designed to:

- Detect bullish and bearish Liquidity Voids.
- Produce immutable Liquidity Void domain objects.
- Maintain reusable collections of detected voids.
- Validate detected Liquidity Void structures.
- Provide statistical summaries of detected voids.
- Support future extensions while preserving the existing public interface.

---

# Package Structure

```
smart_money/liquidity_void
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

## LiquidityVoid

`LiquidityVoid` is the domain model representing a detected institutional Liquidity Void.

Each object stores:

- first candle
- last candle
- void direction
- top boundary
- bottom boundary
- midpoint
- void size
- candle count
- fill status
- fill timestamp

The implementation uses an immutable dataclass (`frozen=True`) with `slots=True` and provides convenience properties for determining whether the void is bullish or bearish. :contentReference[oaicite:1]{index=1}

---

## LiquidityVoidAnalyzer

`LiquidityVoidAnalyzer` performs Liquidity Void detection.

The analyzer processes market candles using a rolling three-candle window.

Current detection rules are:

### Bullish Liquidity Void

A bullish Liquidity Void is detected when:

```
Last Candle Low > First Candle High
```

The resulting void boundaries are calculated as:

- Top = Last Candle Low
- Bottom = First Candle High

---

### Bearish Liquidity Void

A bearish Liquidity Void is detected when:

```
Last Candle High < First Candle Low
```

The resulting void boundaries are calculated as:

- Top = First Candle Low
- Bottom = Last Candle High

Each detected void records a `candle_count` of three in the current implementation.

The analyzer documentation also notes that future versions may support multi-candle expansion detection, while the current implementation is limited to the three-candle model. :contentReference[oaicite:2]{index=2}

---

## LiquidityVoidSeries

`LiquidityVoidSeries` is the collection class for Liquidity Void objects.

It extends the Smart Money `BaseCollection` and provides:

- storage of detected Liquidity Voids
- append operation
- retrieval of recent Liquidity Voids
- direct access to the underlying collection

This encapsulates collection management within the package. :contentReference[oaicite:3]{index=3}

---

## LiquidityVoidDirection

Defines the direction of a Liquidity Void.

Current values are:

- `BULLISH`
- `BEARISH`

The enumeration identifies the directional bias associated with each detected Liquidity Void. :contentReference[oaicite:4]{index=4}

---

## LiquidityVoidValidator

Validates Liquidity Void objects.

The current implementation verifies:

- first candle exists
- last candle exists
- direction exists
- top boundary is greater than or equal to bottom boundary
- void size is not negative
- Liquidity Void contains at least two candles

Validation failures raise `ValueError`. :contentReference[oaicite:5]{index=5}

---

## LiquidityVoidStatistics

Provides statistical information for a collection of Liquidity Void objects.

Current statistics include:

- total Liquidity Voids
- bullish Liquidity Voids
- bearish Liquidity Voids
- filled Liquidity Voids
- unfilled Liquidity Voids

Statistics are calculated dynamically from the associated collection. :contentReference[oaicite:6]{index=6}

---

# Detection Workflow

```
Candles
    │
    ▼
Three-Candle Window
    │
    ▼
Liquidity Void Detection
    │
    ▼
LiquidityVoid
    │
    ▼
LiquidityVoidSeries
```

The current implementation evaluates each consecutive three-candle sequence and creates a Liquidity Void whenever the bullish or bearish detection conditions are satisfied. :contentReference[oaicite:7]{index=7}

---

# Package Dependencies

```
Market
   │
   ▼
Smart Money Base
   │
   ▼
Liquidity Void
```

Current implementation depends on:

- Market package
- Smart Money Base package

The analyzer currently operates directly on market candle data and returns a `LiquidityVoidSeries`. 

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

The **Liquidity Void** package provides a complete implementation for detecting institutional Liquidity Voids within the OGS Smart Money Framework. It analyzes sequential market candles using a three-candle detection model, identifies bullish and bearish Liquidity Voids, and represents them as validated domain objects supported by reusable collections and statistical reporting. The package follows the common architectural conventions established across the Smart Money framework while remaining focused on Liquidity Void detection and representation.