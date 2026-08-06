# Mitigation Block

**Package Name:** Mitigation Block

**Package Path:** `src/ogs/smart_money/mitigation`

**Version:** 0.0.1

---

# Overview

The **Mitigation Block** package is responsible for detecting ICT Mitigation Blocks within market price action.

A Mitigation Block represents a price zone that is revisited after a strong impulsive movement, indicating that previously unfilled institutional orders may be mitigated. The current implementation identifies bullish and bearish mitigation patterns using a two-candle confirmation model and represents each detected mitigation as an immutable domain object.

The package follows the modular architecture of the OGS Smart Money Framework by separating analysis, domain modelling, collections, validation, statistics, and supporting enumerations. 

---

# Design Goals

The Mitigation Block package is designed to:

- Detect bullish and bearish ICT Mitigation Blocks.
- Produce immutable Mitigation Block domain objects.
- Maintain reusable collections of detected mitigation blocks.
- Validate mitigation structures.
- Provide statistical summaries of mitigation activity.
- Support future integration with other Smart Money concepts.

---

# Package Structure

```
smart_money/mitigation
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

## MitigationBlock

`MitigationBlock` is the domain model representing a detected ICT Mitigation Block.

Each object stores:

- mitigation candle
- mitigation direction
- top boundary
- bottom boundary
- midpoint
- block size
- mitigation status
- mitigation timestamp

The implementation uses an immutable dataclass (`frozen=True`) with `slots=True` and provides convenience properties for determining whether the mitigation block is bullish or bearish. :contentReference[oaicite:1]{index=1}

---

## MitigationBlockAnalyzer

`MitigationBlockAnalyzer` performs Mitigation Block detection.

The analyzer processes market candles in consecutive two-candle sequences.

### Bullish Mitigation

A bullish mitigation is detected when:

- the previous candle is bearish
- the current candle trades into the previous candle's range
- the current candle closes above the previous high

The resulting mitigation block uses the previous candle as the mitigation zone.

---

### Bearish Mitigation

A bearish mitigation is detected when:

- the previous candle is bullish
- the current candle trades into the previous candle's range
- the current candle closes below the previous low

The resulting mitigation block also uses the previous candle as the mitigation zone.

The analyzer marks each detected block as mitigated (`is_mitigated=True`).

The implementation documentation indicates that future versions are intended to integrate with:

- BOS
- CHOCH
- Order Block
- Fair Value Gap

The current implementation performs standalone detection based solely on candle relationships. :contentReference[oaicite:2]{index=2}

---

## MitigationBlockSeries

`MitigationBlockSeries` is the collection class for Mitigation Block objects.

It extends the Smart Money `BaseCollection` and provides:

- storage of mitigation blocks
- append operation
- retrieval of recent mitigation blocks
- direct access to the underlying collection

This encapsulates collection management within the package. :contentReference[oaicite:3]{index=3}

---

## MitigationBlockDirection

Defines the direction of a Mitigation Block.

Current values are:

- `BULLISH`
- `BEARISH`

The enumeration identifies the directional bias associated with each detected Mitigation Block. :contentReference[oaicite:4]{index=4}

---

## MitigationBlockValidator

Validates Mitigation Block objects.

The current implementation verifies:

- mitigation candle exists
- direction exists
- top boundary is greater than or equal to bottom boundary
- block size is not negative

Validation failures raise `ValueError`. :contentReference[oaicite:5]{index=5}

---

## MitigationBlockStatistics

Provides statistical information for a collection of Mitigation Blocks.

Current statistics include:

- total mitigation blocks
- bullish mitigation blocks
- bearish mitigation blocks
- mitigated blocks
- unmitigated blocks

Statistics are calculated dynamically from the associated collection. :contentReference[oaicite:6]{index=6}

---

# Detection Workflow

```
Candles
    │
    ▼
Two-Candle Analysis
    │
    ▼
Mitigation Detection
    │
    ▼
MitigationBlock
    │
    ▼
MitigationBlockSeries
```

The current implementation evaluates consecutive candle pairs and creates a Mitigation Block whenever the bullish or bearish mitigation conditions are satisfied. :contentReference[oaicite:7]{index=7}

---

# Package Dependencies

```
Market
   │
   ▼
Smart Money Base
   │
   ▼
Mitigation Block
```

Current implementation depends on:

- Market package
- Smart Money Base package

Although the analyzer comments reference future integration with BOS, CHOCH, Order Block, and Fair Value Gap modules, the current implementation does not depend on those packages and operates directly on market candle data. :contentReference[oaicite:8]{index=8}

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

The **Mitigation Block** package provides a complete implementation for detecting ICT Mitigation Blocks within the OGS Smart Money Framework. It analyzes consecutive market candles to identify bullish and bearish mitigation patterns, represents them as validated domain objects, and supports reusable collections and statistical reporting. The current implementation functions independently while providing a clear foundation for future integration with higher-level Smart Money concepts such as BOS, CHOCH, Order Blocks, and Fair Value Gaps.