# Swing

**Package Name:** Swing

**Package Path:** `src/ogs/smart_money/swing`

**Version:** 0.0.1

---

# Overview

The **Swing** package is responsible for detecting confirmed market swing highs and swing lows within the OGS Smart Money Framework.

The current implementation follows the classical **Bill Williams five-candle swing model**, where the center candle is evaluated against two preceding and two succeeding candles. Confirmed swings are represented as immutable domain objects and organized into reusable collections for downstream Smart Money analysis.

The package provides the structural foundation upon which higher-level market structure concepts such as BOS, CHOCH, MSS, Liquidity, and Order Blocks can be built.

---

# Design Goals

The Swing package is designed to:

- Detect confirmed Swing Highs.
- Detect confirmed Swing Lows.
- Produce immutable Swing objects.
- Maintain reusable Swing collections.
- Validate detected Swing structures.
- Provide a common structural foundation for market structure analysis.

---

# Package Structure

```text
smart_money/swing
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

## Swing

`Swing` represents a confirmed market swing.

Each object stores:

- candle index
- confirmation candle
- swing type

The implementation is an immutable dataclass (`frozen=True`) with `slots=True`.

Convenience properties provide:

- timestamp
- swing price

For a Swing High, the price corresponds to the candle high.

For a Swing Low, the price corresponds to the candle low.

---

## SwingAnalyzer

`SwingAnalyzer` implements the Bill Williams five-candle swing algorithm.

The analyzer evaluates every candle except the first two and last two candles.

### Swing High

A Swing High is detected when:

```
Center High >

Previous High (1)
Previous High (2)

Next High (1)
Next High (2)
```

---

### Swing Low

A Swing Low is detected when:

```
Center Low <

Previous Low (1)
Previous Low (2)

Next Low (1)
Next Low (2)
```

A minimum of five candles is required before swing detection begins.

---

## SwingSeries

Collection class for Swing objects.

Provides:

- append()
- latest()
- direct access to Swing collection

---

## SwingType

Current values:

- HIGH
- LOW

---

## SwingValidator

Current validation verifies:

- swing index is non-negative
- candle exists

---

## SwingStatistics

Reserved for future implementation.

No statistical calculations are currently implemented.

---

## SwingDTO

Placeholder reserved for future serialization.

---

## Constants

Current configuration:

- DEFAULT_LOOKBACK = 2
- MINIMUM_CANDLES = 5

---

## Exceptions

```text
Exception
    │
    └── SwingError
            │
            └── InvalidSwingError
```

---

## Interfaces

Defines `SwingAnalyzerProtocol`.

---

# Detection Workflow

```text
CandleSeries
      │
      ▼
Five-Candle Window
      │
      ▼
Swing High Detection
      │
      │
      └───────────────┐
                      ▼
              Swing Low Detection
                      │
                      ▼
                 Swing Objects
                      │
                      ▼
                 SwingSeries
```

The analyzer evaluates each rolling five-candle window independently and records every confirmed Swing High and Swing Low.

---

# Package Dependencies

```text
Market
   │
   ▼
Smart Money Base
   │
   ▼
Swing
```

Current implementation depends on:

- Market package
- Smart Money Base package

The Swing package acts as an upstream structural detector that can be consumed by higher-level Smart Money modules.

---

# Design Principles

The package demonstrates:

- Immutable domain modelling.
- Rule-based swing confirmation.
- Collection-oriented architecture.
- Separation of analysis and validation.
- Modular Smart Money architecture.
- Framework reuse through the Smart Money Base package.

---

# Current Implementation Status

| Component | Status |
|-----------|--------|
| Domain | Implemented |
| Analyzer | Implemented |
| Collection | Implemented |
| Constants | Implemented |
| Enumeration | Implemented |
| Validator | Implemented |
| Interface | Implemented |
| Exceptions | Implemented |
| DTO | Placeholder |
| Statistics | Placeholder |

---

# Summary

The **Swing** package provides a complete implementation of Bill Williams' five-candle Swing High and Swing Low detection algorithm. It establishes the foundational market turning points required by higher-level Smart Money concepts while maintaining a modular architecture through immutable domain models, reusable collections, validation, and extensible framework components.