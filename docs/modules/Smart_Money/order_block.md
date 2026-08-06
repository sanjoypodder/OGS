# Order Block

**Package Name:** Order Block

**Package Path:** `src/ogs/smart_money/order_block`

**Version:** 0.0.1

---

# Overview

The **Order Block** package is responsible for identifying institutional Order Blocks within the OGS Smart Money Framework.

Unlike earlier Smart Money packages that directly produce confirmed structures, the Order Block package follows a **candidate-based detection pipeline**. Candidate Order Blocks are first generated from market analysis, validated against institutional rules, and are intended to be transformed into confirmed Order Block domain objects.

The package introduces a multi-stage workflow consisting of candidate generation, validation, and confirmation while integrating several previously detected Smart Money concepts.

---

# Design Goals

The Order Block package is designed to:

- Detect potential institutional Order Blocks.
- Build reusable candidate objects.
- Validate candidates using configurable rules.
- Produce confirmed Order Blocks.
- Support future institutional confirmation logic.
- Integrate multiple Smart Money concepts into one detection pipeline.

---

# Package Structure

```text
smart_money/order_block
│
├── __init__.py
├── analyzer.py
├── candidate.py
├── candidate_builder.py
├── candidate_collection.py
├── collection.py
├── constants.py
├── domain.py
├── dto.py
├── enums.py
├── exceptions.py
├── interfaces.py
├── statistics.py
├── validator.py
│
├── displacement/
└── validation/
```

---

# Package Components

## OrderBlock

Represents a confirmed institutional Order Block.

Each object stores:

- origin candle
- MSS confirmation
- Liquidity Sweep
- direction
- current status

The implementation is immutable (`frozen=True`) using `slots=True` and exposes convenient accessors for OHLC values through the origin candle.

---

## OrderBlockAnalyzer

`OrderBlockAnalyzer` coordinates the complete Order Block detection workflow.

The analyzer performs three sequential stages:

1. Build candidates
2. Validate candidates
3. Build confirmed Order Blocks

Current implementation:

```
Candles
      │
      ▼
Liquidity Sweep
      │
      ▼
MSS
      │
      ▼
Candidate Builder
      │
      ▼
Candidate Validation
      │
      ▼
Order Block
```

The confirmation stage is currently incomplete.

`_build_order_blocks()` presently returns an empty `OrderBlockSeries`, indicating that candidate confirmation is reserved for a future implementation.

---

## Candidate Builder

`OrderBlockCandidateBuilder` creates candidate Order Blocks.

Each candidate consists of:

- origin candle
- MSS
- Liquidity Sweep
- CandidateStatus

All new candidates begin with

```
CandidateStatus.DETECTED
```

---

## OrderBlockCandidate

Represents a potential Order Block before institutional validation.

Each candidate contains:

- origin candle
- MSS
- Liquidity Sweep
- candidate status

The candidate inherits from the shared Smart Money `BaseCandidate` class.

---

## OrderBlockSeries

Collection class for confirmed Order Blocks.

Provides:

- append()
- latest()
- access to underlying collection

---

## OrderBlockDirection

Current values:

- BULLISH
- BEARISH

---

## OrderBlockStatus

Represents lifecycle state.

Current values:

- ACTIVE
- MITIGATED
- INVALIDATED

---

## OrderBlockValidator

Validates confirmed Order Blocks.

Current implementation verifies:

- Order Block exists
- origin candle exists
- MSS exists
- Liquidity Sweep exists

---

## OrderBlockStatistics

Currently reserved for future metrics.

No statistical calculations are implemented.

---

## DTO

Placeholder for future serialization.

---

## Constants

Current configuration:

- MAX_ORDER_BLOCK_AGE

---

## Exceptions

```
Exception
    │
    └── OrderBlockError
            │
            └── InvalidOrderBlockError
```

---

## Interfaces

Defines `OrderBlockAnalyzerProtocol`.

---

# Candidate Detection Workflow

Current implementation:

```text
Candles
      │
      ▼
Liquidity Sweep
      │
      ▼
MSS
      │
      ▼
Find last bearish candle
      │
      ▼
OrderBlockCandidate
```

The analyzer searches for the most recent bearish candle preceding an MSS event and combines it with the corresponding Liquidity Sweep to create an Order Block candidate.

---

# Validation Package

The package includes a dedicated validation subsystem.

## OrderBlockCandidateValidator

Validates Order Block candidates before confirmation.

Current validation rules include:

- origin candle required
- Liquidity Sweep required
- MSS required

Validation returns a `ValidationResult` rather than raising exceptions.

---

## OrderBlockRules

Current configurable rules include:

- minimum displacement
- require liquidity sweep
- require fresh block
- require MSS

---

## Validation Statistics

Tracks:

- validated candidates
- rejected candidates
- total validations

---

# Displacement Package

The package contains a dedicated **Displacement** module.

## Purpose

Detect institutional displacement candles associated with Order Block formation.

## Components

- Displacement
- DisplacementAnalyzer
- DisplacementSeries
- DisplacementStatistics
- DisplacementValidator

Current implementation classifies bullish and bearish displacement using candle direction.

---

# Dependencies

Current implementation directly depends on:

```text
Market
      │
      ▼
Liquidity Sweep
      │
      ▼
CHOCH
      │
      ▼
MSS
      │
      ▼
Candidate
      │
      ▼
Order Block
```

Unlike previous Smart Money modules, Order Block integrates several previously detected market structures into a single workflow.

---

# Design Principles

The package demonstrates:

- Candidate-based architecture.
- Multi-stage validation.
- Immutable domain modelling.
- Separation of candidate and confirmed objects.
- Rule-driven validation.
- Modular Smart Money architecture.

---

# Current Implementation Status

| Component | Status |
|------------|--------|
| Domain | Implemented |
| Candidate | Implemented |
| Candidate Builder | Implemented |
| Candidate Collection | Implemented |
| Analyzer | Partially Implemented |
| Validator | Implemented |
| Validation Framework | Implemented |
| Displacement Module | Implemented |
| Statistics | Placeholder |
| DTO | Placeholder |
| Confirmation Stage | Not Yet Implemented |

---

# Summary

The **Order Block** package introduces the first multi-stage institutional detection workflow within the OGS Smart Money Framework. Rather than creating confirmed Order Blocks directly, it builds candidate objects from Liquidity Sweep and MSS events, validates them through a dedicated rule engine, and prepares them for confirmation. Although the final confirmation stage is not yet implemented, the package establishes the architectural foundation for institutional-grade Order Block detection by combining candidate modelling, validation, displacement analysis, and reusable Smart Money components.