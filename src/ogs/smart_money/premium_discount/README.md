# Premium / Discount Module

**OGS FinOS v0.0.2**

---

## Overview

The Premium / Discount module classifies price within an institutional dealing range. It determines whether the current market price is trading in the Premium, Equilibrium, or Discount region.

This module provides a reusable and immutable representation of institutional valuation zones and serves as a foundational component for Smart Money Concepts (SMC) analysis.

---

# Institutional Concept

Institutional traders commonly divide a completed dealing range into three valuation regions:

```
Range High
│
├──────── Premium
│
├──────── Equilibrium (50%)
│
├──────── Discount
│
Range Low
```

- **Premium** → Price trading above equilibrium.
- **Equilibrium** → Fair value (midpoint of the dealing range).
- **Discount** → Price trading below equilibrium.

These zones help identify favorable buying and selling opportunities.

---

# Package Structure

```text
premium_discount/
│
├── analyzer/
│   ├── __init__.py
│   └── analyzer.py
│
├── collection/
│   ├── __init__.py
│   └── premium_discount_collection.py
│
├── domain/
│   ├── __init__.py
│   └── premium_discount.py
│
├── enums/
│   ├── __init__.py
│   └── premium_discount_zone.py
│
├── factory/
│   ├── __init__.py
│   └── factory.py
│
├── statistics/
│   ├── __init__.py
│   └── premium_discount_statistics.py
│
├── validator/
│   ├── __init__.py
│   └── premium_discount_validator.py
│
├── __init__.py
└── README.md
```

---

# Components

## PremiumDiscount

Immutable domain model representing a single valuation zone.

Provides:

- Range High
- Range Low
- Equilibrium
- Current Price
- Zone
- Confidence
- Metadata

---

## PremiumDiscountCollection

Container for multiple PremiumDiscount objects.

Supports:

- add()
- extend()
- clear()
- filter_by_zone()
- iteration
- indexing

---

## PremiumDiscountValidator

Performs structural validation.

Checks:

- valid range
- equilibrium position
- current price
- confidence limits

---

## PremiumDiscountStatistics

Provides statistical summaries including:

- total objects
- premium count
- equilibrium count
- discount count
- average range size
- average confidence
- valuation ratios

---

## PremiumDiscountAnalyzer

Responsible for:

- computing equilibrium
- classifying valuation zone
- constructing immutable domain objects

The analyzer intentionally excludes:

- swing detection
- dealing range discovery
- Fibonacci calculations
- Optimal Trade Entry (OTE)
- market bias

These responsibilities belong to separate Smart Money modules.

---

## PremiumDiscountFactory

Factory responsible for constructing analyzers.

```python
analyzer = PremiumDiscountFactory.create_analyzer()
```

---

# Public API

```python
from ogs.smart_money.premium_discount import (
    PremiumDiscountFactory,
)

analyzer = PremiumDiscountFactory.create_analyzer()
```

---

# Example

```python
from decimal import Decimal

collection = analyzer.analyze(
    range_high=Decimal("200"),
    range_low=Decimal("100"),
    current_price=Decimal("175"),
)
```

---

# Unit Testing

```
pytest tests/smart_money/premium_discount -v
```

Current status:

```
8 Passed
0 Failed
```

---

# Design Principles

- Immutable domain objects
- Single Responsibility Principle
- Composition over inheritance
- Read-only statistics
- Factory-based construction
- Modular architecture
- Full type hints
- Python 3.14 compatible

---

# Dependencies

- Python 3.14+
- Decimal
- dataclasses
- pytest

---

# Future Enhancements

Future versions may integrate with:

- Dealing Range
- OTE
- Fibonacci
- Market Structure
- Liquidity
- Fair Value Gap
- Order Blocks

without modifying the existing public API.

---

# Version History

## v0.0.2

Initial implementation.

Includes:

- Enums
- Domain
- Collection
- Validator
- Statistics
- Analyzer
- Factory
- Unit Tests
- Documentation