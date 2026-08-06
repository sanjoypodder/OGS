# Imbalance

**Package Name:** Imbalance

**Package Path:** `src/ogs/smart_money/imbalance`

**Version:** 0.0.1

---

# Overview

The **Imbalance** package is responsible for detecting generic market imbalances within price action.

An imbalance occurs when a three-candle sequence leaves an inefficiently traded price region between the first and third candles. The package scans market candles, identifies bullish and bearish imbalance patterns, and represents each detected imbalance as an immutable domain object for subsequent Smart Money analysis.

The package follows the common modular architecture of the OGS Smart Money Framework by separating analysis, domain modelling, collections, validation, statistics, and supporting enumerations. 

---

# Design Goals

The Imbalance package is designed to:

- Detect bullish and bearish market imbalances.
- Produce immutable imbalance domain objects.
- Maintain reusable collections of detected imbalances.
- Validate imbalance structures.
- Provide statistical summaries of detected imbalances.
- Support future enhancements while preserving existing interfaces.

---

# Package Structure

```
smart_money/imbalance
│
├── __init__.py
├── analyzer.py
├── collection.py
├── domain.py
├── enums.py
├── README.md
├── statistics.py
└── validator.py
```

---

# Package Components

## Imbalance

`Imbalance` is the domain model representing a detected market imbalance.

Each object stores:

- first candle
- middle candle
- last candle
- imbalance direction

The implementation is an immutable dataclass and provides convenience properties for determining whether the imbalance is bullish or bearish. :contentReference[oaicite:1]{index=1}

---

## ImbalanceAnalyzer

`ImbalanceAnalyzer` performs imbalance detection.

The analyzer processes market candles using a rolling three-candle window.

Current detection rules are:

### Bullish Imbalance

A bullish imbalance is detected when:

```
Last Candle Low > First Candle High
```

---

### Bearish Imbalance

A bearish imbalance is detected when:

```
Last Candle High < First Candle Low
```

Whenever either condition is satisfied, a new `Imbalance` object is created and added to the result collection. :contentReference[oaicite:2]{index=2}

---

## ImbalanceSeries

`ImbalanceSeries` is the collection class for imbalance objects.

It extends the Smart Money `BaseCollection` and provides:

- storage of imbalance objects
- append operation
- retrieval of the latest imbalances
- direct access to the underlying collection

This encapsulates imbalance collection management within the package. :contentReference[oaicite:3]{index=3}

---

## ImbalanceDirection

Defines the direction of an imbalance.

Current values are:

- `BULLISH`
- `BEARISH`

The implementation uses Python's `Enum` with automatically assigned values. :contentReference[oaicite:4]{index=4}

---

## ImbalanceValidator

Validates imbalance objects.

The current implementation verifies:

- imbalance object exists
- first candle exists
- middle candle exists
- last candle exists
- direction exists

The validator returns a boolean value indicating whether the imbalance satisfies these requirements. :contentReference[oaicite:5]{index=5}

---

## ImbalanceStatistics

Provides statistical information for a collection of imbalance objects.

Current statistics include:

- total imbalances
- bullish imbalances
- bearish imbalances

Statistics are calculated dynamically from the associated collection. :contentReference[oaicite:6]{index=6}

---

## README

The package includes an initial README file containing placeholder sections for purpose, components, and future work. The content is currently marked as TODO and serves as a scaffold for future package documentation. :contentReference[oaicite:7]{index=7}

---

# Detection Workflow

```
Candles
    │
    ▼
Three-Candle Window
    │
    ▼
Imbalance Detection
    │
    ▼
Imbalance
    │
    ▼
ImbalanceSeries
```

The current implementation evaluates each consecutive three-candle sequence and records an imbalance whenever the bullish or bearish detection conditions are satisfied. :contentReference[oaicite:8]{index=8}

---

# Package Dependencies

```
Market
   │
   ▼
Smart Money Base
   │
   ▼
Imbalance
```

Current implementation depends on:

- Market package
- Smart Money Base package

The analyzer currently operates directly on market candle data and returns an `ImbalanceSeries`. 

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
| README | Initial placeholder |

---

# Summary

The **Imbalance** package provides a focused implementation for detecting generic market imbalances within the OGS Smart Money Framework. It analyzes sequential candle data, identifies bullish and bearish imbalance patterns, and represents them as validated domain objects supported by reusable collections and statistical reporting. The package follows the common architectural conventions established across the Smart Money framework while remaining dedicated to imbalance detection.