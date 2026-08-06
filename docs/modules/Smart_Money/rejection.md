# Rejection Block

**Package Name:** Rejection Block

**Package Path:** `src/ogs/smart_money/rejection`

**Version:** 0.0.1

---

# Overview

The **Rejection Block** package is responsible for detecting ICT Rejection Blocks within the OGS Smart Money Framework.

A Rejection Block represents a price rejection where a candle exhibits a significant wick and is subsequently confirmed by the following candle. The current implementation identifies bullish and bearish rejection patterns using a two-candle confirmation model and represents each confirmed rejection as an immutable domain object.

The package follows the modular Smart Money architecture by separating analysis, domain modelling, collections, validation, statistics, and supporting enumerations.

---

# Design Goals

The Rejection Block package is designed to:

- Detect bullish and bearish ICT Rejection Blocks.
- Identify rejection through wick analysis.
- Require confirmation before creating a Rejection Block.
- Produce immutable domain objects.
- Validate detected rejection structures.
- Provide statistical summaries of detected rejection events.
- Support future integration with additional Smart Money concepts.

---

# Package Structure

```text
smart_money/rejection
│
├── analyzer.py
├── collection.py
├── domain.py
├── enums.py
├── statistics.py
└── validator.py
```

---

# Package Components

## RejectionBlock

`RejectionBlock` is the domain model representing a confirmed ICT Rejection Block.

Each object stores:

- rejection candle
- rejection direction
- top boundary
- bottom boundary
- midpoint
- block size
- confirmation status
- confirmation timestamp

The implementation uses an immutable dataclass (`frozen=True`) with `slots=True` and provides convenience properties for determining whether the rejection is bullish or bearish.

---

## RejectionBlockAnalyzer

`RejectionBlockAnalyzer` performs Rejection Block detection.

The analyzer evaluates consecutive two-candle sequences.

For each pair:

- the first candle is treated as the potential rejection candle
- the second candle acts as the confirmation candle

The analyzer calculates:

- upper wick length
- lower wick length
- candle body size

To avoid division-by-zero issues, a candle with zero body size is assigned a minimum body value of `0.01` before wick comparisons.

### Bullish Rejection

A bullish Rejection Block is detected when:

- the lower wick is at least twice the candle body

```
Lower Wick ≥ 2 × Body
```

- the confirmation candle closes above the rejection candle's high

```
Confirmation Close > Rejection High
```

When both conditions are satisfied, a bullish Rejection Block is created.

---

### Bearish Rejection

A bearish Rejection Block is detected when:

- the upper wick is at least twice the candle body

```
Upper Wick ≥ 2 × Body
```

- the confirmation candle closes below the rejection candle's low

```
Confirmation Close < Rejection Low
```

When both conditions are satisfied, a bearish Rejection Block is created.

Each detected block is marked as confirmed (`is_confirmed=True`).

The analyzer documentation indicates that future versions are intended to integrate with:

- BOS
- CHOCH
- Order Block
- Liquidity

The current implementation performs standalone candle-based detection.

---

## RejectionBlockSeries

`RejectionBlockSeries` is the collection class for Rejection Block objects.

It extends the Smart Money `BaseCollection` and provides:

- storage of rejection blocks
- append operation
- retrieval of the latest rejection blocks
- direct access to the underlying collection

---

## RejectionBlockDirection

Defines the direction of a Rejection Block.

Current values are:

- `BULLISH`
- `BEARISH`

---

## RejectionBlockValidator

Validates Rejection Block objects.

The current implementation verifies:

- rejection candle exists
- direction exists
- top boundary is greater than or equal to bottom boundary
- block size is not negative

Validation failures raise `ValueError`.

---

## RejectionBlockStatistics

Provides statistical information for a collection of Rejection Blocks.

Current statistics include:

- total rejection blocks
- bullish rejection blocks
- bearish rejection blocks
- confirmed rejection blocks
- unconfirmed rejection blocks

Statistics are calculated dynamically from the associated collection.

---

# Detection Workflow

```text
Candles
      │
      ▼
Two-Candle Analysis
      │
      ▼
Calculate
• Upper Wick
• Lower Wick
• Body Size
      │
      ▼
Confirmation Check
      │
      ▼
RejectionBlock
      │
      ▼
RejectionBlockSeries
```

The analyzer evaluates each consecutive candle pair, measures wick-to-body relationships, and creates a confirmed Rejection Block only when both the rejection pattern and confirmation conditions are satisfied.

---

# Package Dependencies

```text
Market
   │
   ▼
Smart Money Base
   │
   ▼
Rejection Block
```

Current implementation depends on:

- Market package
- Smart Money Base package

Although future integration with BOS, CHOCH, Order Block, and Liquidity is planned, the present implementation operates directly on market candle data.

---

# Design Principles

The package demonstrates the following architectural principles:

- Immutable domain modelling.
- Confirmation-based pattern detection.
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

The **Rejection Block** package provides a complete implementation for detecting ICT Rejection Blocks within the OGS Smart Money Framework. It analyzes consecutive candle pairs, evaluates wick-to-body relationships, requires confirmation from the following candle, and represents confirmed rejection patterns as immutable domain objects. The package currently operates as an independent candle-pattern detector while providing a foundation for future integration with higher-level Smart Money concepts such as BOS, CHOCH, Order Blocks, and Liquidity.