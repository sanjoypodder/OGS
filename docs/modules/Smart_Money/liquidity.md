# Liquidity

**Package Name:** Liquidity

**Package Path:** `src/ogs/smart_money/liquidity`

**Version:** 0.0.1

---

# Overview

The **Liquidity** package provides the organizational structure for liquidity-related components within the OGS Smart Money Framework.

Rather than implementing a single liquidity detection algorithm, this package groups together the individual modules responsible for detecting, representing, and analyzing different forms of market liquidity.

The package serves as the common namespace for all liquidity-based Smart Money concepts while delegating implementation responsibilities to specialized subpackages.

---

# Design Goals

The Liquidity package is designed to:

- Organize all liquidity-related Smart Money modules.
- Provide a common namespace for liquidity concepts.
- Separate different liquidity models into independent packages.
- Maintain a modular and extensible architecture.
- Allow individual liquidity concepts to evolve independently.

---

# Package Structure

```
smart_money/liquidity
│
├── __init__.py
├── README.md
│
├── base/
├── buy_side/
├── equal_highs/
├── equal_lows/
├── sell_side/
└── sweep/
```

---

# Package Components

## Base

Provides shared infrastructure used by liquidity-related modules.

---

## Buy Side

Contains the implementation related to Buy-Side Liquidity.

---

## Sell Side

Contains the implementation related to Sell-Side Liquidity.

---

## Equal Highs

Contains the implementation responsible for detecting Equal High liquidity formations.

---

## Equal Lows

Contains the implementation responsible for detecting Equal Low liquidity formations.

---

## Sweep

Contains the implementation for liquidity sweep detection.

---

# Package Organization

```
Liquidity
│
├── Base
├── Buy Side
├── Sell Side
├── Equal Highs
├── Equal Lows
└── Sweep
```

Each subpackage is independently responsible for its own:

- domain models
- analysis or detection logic
- collections
- validation
- statistics
- supporting interfaces and exceptions

---

# Dependencies

The root Liquidity package acts as a namespace package.

Business logic resides inside the individual liquidity subpackages.

---

# Current Implementation Status

| Component | Status |
|-----------|--------|
| Root Package | Implemented |
| Package Organization | Implemented |
| README | Placeholder |
| Base | Separate package |
| Buy Side | Separate package |
| Sell Side | Separate package |
| Equal Highs | Separate package |
| Equal Lows | Separate package |
| Sweep | Separate package |

---

# Summary

The **Liquidity** package serves as the organizational foundation for all liquidity-related functionality within the OGS Smart Money Framework. It groups together multiple specialized liquidity modules under a common namespace while leaving implementation responsibilities to the individual subpackages. This modular organization supports maintainability, extensibility, and clear separation between different liquidity concepts.