# Breaker Block

**Package Name:** Breaker Block

**Package Path:** `src/ogs/smart_money/breaker`

**Version:** 0.0.1

---

# Overview

The **Breaker Block** package is responsible for identifying ICT Breaker Blocks from market price action.

A Breaker Block is created after a strong structural displacement where the final candle opposing the impulsive move becomes a potential support or resistance zone. The package analyzes market candles, detects bullish and bearish breaker formations, and represents them as immutable domain objects for further Smart Money analysis.

The package is organized into distinct components for analysis, domain modelling, collections, validation, statistics, and supporting enumerations, following the same architectural principles used throughout the OGS Smart Money Framework. 

---

# Design Goals

The Breaker Block package is designed to:

- Detect bullish and bearish Breaker Blocks.
- Produce immutable Breaker Block domain objects.
- Maintain reusable collections of detected breaker blocks.
- Validate detected structures.
- Provide statistical summaries of detected breaker blocks.
- Support future integration with higher-level Smart Money modules.

---

# Package Structure

```
smart_money/breaker
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

## BreakerBlock

The `BreakerBlock` domain model represents a detected ICT Breaker Block.

Each instance stores:

- originating candle
- breaker direction
- top price
- bottom price
- midpoint
- block size
- mitigation status
- mitigation timestamp

The implementation uses an immutable dataclass with `slots=True` for memory efficiency and provides convenience properties to determine whether the breaker is bullish or bearish. :contentReference[oaicite:2]{index=2}

---

## BreakerBlockAnalyzer

`BreakerBlockAnalyzer` performs the detection of Breaker Blocks.

The current implementation analyses consecutive candles and identifies two patterns:

- **Bullish Breaker**
  - Previous candle is bearish.
  - Current candle closes above the previous high.

- **Bearish Breaker**
  - Previous candle is bullish.
  - Current candle closes below the previous low.

For each confirmed pattern, a new `BreakerBlock` object is created and added to the result collection.

The implementation notes that future versions are intended to integrate directly with the BOS module, but the current version operates solely on candle data. :contentReference[oaicite:3]{index=3}

---

## BreakerBlockSeries

`BreakerBlockSeries` is the collection class for Breaker Block objects.

It extends the Smart Money `BaseCollection` and provides:

- storage of detected breaker blocks
- append operation
- retrieval of the latest breaker blocks
- direct access to the underlying collection

This encapsulates collection management within the package. :contentReference[oaicite:4]{index=4}

---

## BreakerBlockDirection

Defines the direction of a Breaker Block.

Current values are:

- `BULLISH`
- `BEARISH`

The enumeration identifies the directional bias associated with each detected breaker block. :contentReference[oaicite:5]{index=5}

---

## BreakerBlockValidator

Validates Breaker Block objects before they are used elsewhere in the framework.

The current implementation verifies:

- candle reference exists
- direction exists
- top price is greater than or equal to bottom price
- block size is not negative

Validation failures raise `ValueError`. :contentReference[oaicite:6]{index=6}

---

## BreakerBlockStatistics

Provides statistical information for a collection of Breaker Blocks.

Current statistics include:

- total breaker blocks
- bullish breaker blocks
- bearish breaker blocks
- mitigated breaker blocks
- unmitigated breaker blocks

The statistics are calculated dynamically from the associated collection. :contentReference[oaicite:7]{index=7}

---

# Detection Workflow

```
Candles
    │
    ▼
BreakerBlockAnalyzer
    │
    ▼
Pattern Detection
    │
    ▼
BreakerBlock
    │
    ▼
BreakerBlockSeries
```

The current implementation performs analysis directly on sequential candle data. :contentReference[oaicite:8]{index=8}

---

# Package Dependencies

```
Market
   │
   ▼
Smart Money Base
   │
   ▼
Breaker Block
```

Current implementation depends on:

- Market package
- Smart Money Base package

Although the analyzer comments mention future integration with BOS, no runtime dependency currently exists in the uploaded implementation. :contentReference[oaicite:9]{index=9}

---

# Design Principles

The package demonstrates the following architectural principles:

- Immutable domain modelling
- Separation of analysis and validation
- Collection-oriented design
- Dedicated domain statistics
- Modular Smart Money architecture
- Framework reuse through the Smart Money Base package

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

The **Breaker Block** package provides a complete implementation for detecting and representing ICT Breaker Blocks within the OGS Smart Money Framework. It transforms sequential candle data into validated Breaker Block objects while maintaining a clear separation between analysis, domain modelling, validation, collections, and statistical reporting. The package follows the common architectural conventions established across the Smart Money framework and is structured to support future enhancements without altering its existing public interfaces.