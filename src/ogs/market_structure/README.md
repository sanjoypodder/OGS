# Market Structure Module

## Overview

The Market Structure module is the foundation of the OGS Smart Money AI
framework.

It converts raw candle data into validated swing points that can be
consumed by every Smart Money Concept module.

---

# Features

- Pivot High Detection
- Pivot Low Detection
- Higher High (HH)
- Higher Low (HL)
- Lower High (LH)
- Lower Low (LL)
- Swing Validation
- Swing Statistics
- Configurable Pivot Depth

---

# Architecture

```
Candles
    │
    ▼
MarketStructureAnalyzer
    │
    ▼
SwingSeries
    │
    ▼
Smart Money Modules
```

---

# Components

## enums.py

Defines

- SwingType
- SwingStrength
- TrendDirection

---

## domain.py

Immutable SwingPoint model.

---

## collection.py

Collection of SwingPoint objects.

---

## validator.py

Validates SwingPoint instances.

---

## factory.py

Creates validated SwingPoint objects.

---

## statistics.py

Provides statistics including

- Count
- Higher High Count
- Higher Low Count
- Lower High Count
- Lower Low Count
- Strong Swing Count

---

## analyzer.py

Detects market structure from Candle data.

---

# Usage

```python
from ogs.market_structure import (
    MarketStructureAnalyzer,
)

analyzer = MarketStructureAnalyzer(
    pivot_depth=2,
)

swings = analyzer.analyze(candles)
```

---

# Example Output

```
HIGH
LOW
HIGHER_HIGH
HIGHER_LOW
LOWER_HIGH
LOWER_LOW
```

---

# Used By

This module is the foundation for

- Break of Structure (BOS)
- Change of Character (CHOCH)
- Market Structure Shift (MSS)
- Liquidity Sweep
- Liquidity Pool
- Equal High
- Equal Low
- SMT Divergence
- Order Blocks
- Premium / Discount
- OTE
- AI Decision Engine

---

# Future Improvements

- ATR-based swing strength
- Volume confirmation
- Fractal detection
- ZigZag detection
- Multi-timeframe market structure
- Trend engine
- Swing clustering

---

# Version

OGS Smart Money AI

Version 0.0.1