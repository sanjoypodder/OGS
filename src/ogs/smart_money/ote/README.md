# OGS FinOS

# Optimal Trade Entry (OTE) Module

Version **0.0.2**

---

# Overview

The **Optimal Trade Entry (OTE)** module implements the Institutional Smart Money Concept (SMC) for identifying high-probability retracement zones within a confirmed dealing range.

An OTE represents the Fibonacci retracement zone between the **62%** and **79%** levels, with the **70.5%** level acting as the equilibrium of the entry zone.

Unlike standalone Fibonacci tools, the OTE module depends on an already confirmed **Dealing Range** and computes the institutional execution zone used by Smart Money traders.

The module is completely immutable, test-driven, and follows the layered architecture of OGS FinOS.

---

# Institutional Concept

After a confirmed impulse move, institutional traders typically wait for price to retrace into the OTE zone before considering trade execution.

```
Bullish Example

Swing High
     │
     │
 62%
     │
70.5%
     │
79%
     │
Swing Low
```

For bullish markets, price retraces downward into the OTE zone.

For bearish markets, price retraces upward into the OTE zone.

---

# Module Architecture

```
Market Structure
        │
        ▼
Confirmed Swings
        │
        ▼
Dealing Range
        │
        ▼
OTE Analyzer
        │
        ▼
OTE
        │
        ├────────► Execution Engine
        ├────────► Risk Management
        ├────────► Trade Planning
        ├────────► Strategy Engine
        └────────► Statistics
```

The OTE module does not detect swings or dealing ranges.

It consumes a completed `DealingRange`.

---

# Package Structure

```
ote/

├── analyzer/
├── collection/
├── domain/
├── enums/
├── factory/
├── statistics/
├── validator/

README.md
```

---

# Components

## Domain

Represents an immutable Optimal Trade Entry.

Properties include:

- UUID
- Range High
- Range Low
- 62% Level
- 70.5% Level
- 79% Level
- Zone Low
- Zone High
- Direction
- Metadata
- Timestamp

Computed properties:

- Zone Size
- Bullish
- Bearish

---

## Collection

Stores immutable OTE objects.

Supported operations:

- add()
- extend()
- latest()
- clear()
- get_by_id()
- iteration
- indexing
- containment

---

## Validator

Performs structural validation.

Validation includes:

- Positive prices
- High > Low
- Fibonacci levels inside dealing range
- Zone boundaries
- Positive zone size
- Direction validation

No market calculations are performed.

---

## Statistics

Provides read-only statistics.

Available metrics:

- Total OTEs
- Bullish Count
- Bearish Count
- Average Zone Size
- Maximum Zone Size
- Minimum Zone Size
- Average 62% Level
- Average 70.5% Level
- Average 79% Level

---

## Analyzer

Constructs immutable OTE objects from a confirmed DealingRange.

Responsibilities:

- Calculate 62% Fibonacci level
- Calculate 70.5% Fibonacci level
- Calculate 79% Fibonacci level
- Build OTE zone
- Create immutable domain object
- Return OTECollection

The analyzer does not detect swings or market structure.

---

## Factory

Provides standardized analyzer construction.

```
OTEFactory
      │
      ▼
OTEAnalyzer
```

---

# Public API

```python
from ogs.smart_money.ote import (
    OTEFactory,
)

from ogs.smart_money.dealing_range import (
    DealingRangeFactory,
)

dr_analyzer = (
    DealingRangeFactory.create_analyzer()
)

dealing_range = dr_analyzer.analyze(
    swing_high=2100,
    swing_low=2000,
    start_index=10,
    end_index=20,
    direction=DealingRangeDirection.BULLISH,
)

ote_analyzer = (
    OTEFactory.create_analyzer()
)

ote = ote_analyzer.analyze(
    dealing_range.latest()
)
```

---

# Design Principles

The module follows the OGS FinOS architecture.

- Immutable Domain Objects
- Single Responsibility Principle
- Layered Architecture
- Dependency Injection Friendly
- Strong Typing
- Test Driven Development
- Explicit Dependencies
- No Hidden State

---

# Dependencies

The module depends on:

- Python 3.14+
- Decimal
- UUID
- Dataclasses
- datetime
- Dealing Range Module

No third-party libraries are required.

---

# Unit Testing

Current status:

```
48 Passed
0 Failed
0 Skipped
```

Coverage includes:

- Domain
- Collection
- Validator
- Statistics
- Analyzer
- Factory

---

# Future Enhancements

Version 1.x may include:

- Configurable Fibonacci ratios
- Multi-timeframe OTE
- Session-aware OTE
- Liquidity-aware OTE
- Nested OTE zones
- Multiple active OTE tracking
- Confluence scoring
- Execution confidence metrics

These enhancements are intentionally deferred until after Version 1.0 to preserve architectural stability.

---

# Version History

## v0.0.2

Initial implementation.

Completed:

- Scaffold
- Enums
- Domain
- Collection
- Validator
- Statistics
- Analyzer
- Factory
- Unit Tests
- Documentation

Status:

Production Ready
