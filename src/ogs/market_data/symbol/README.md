# Symbol Module

## Overview

The **Symbol** module represents tradable financial instruments within the
OGS Smart Money AI platform.

It provides a standardized representation of instruments across multiple
asset classes including Forex, Cryptocurrency, Stocks, Indices,
Commodities, Futures, ETFs, and Options.

---

## Components

| File | Purpose |
|------|----------|
| domain.py | Immutable Symbol model |
| enums.py | Symbol enumerations |
| validator.py | Symbol validation |
| factory.py | Symbol creation |
| collection.py | Collection utilities |
| statistics.py | Collection statistics |
| analyzer.py | Collection analysis |
| __init__.py | Package exports |

---

## Supported Asset Classes

- Forex
- Cryptocurrency
- Stocks
- Indices
- Commodities
- Futures
- ETFs
- Options

---

## Example

```python
symbol = SymbolFactory.forex(
    "EURUSD",
    Currency.EUR,
    Currency.USD,
)
```

---

## Design Goals

- Immutable domain objects
- Strong validation
- Factory-based creation
- Collection filtering
- Statistical summaries
- Analyzer support
- Easy extension for brokers and exchanges

---

## Package Structure

```
symbol/
│
├── __init__.py
├── analyzer.py
├── collection.py
├── domain.py
├── enums.py
├── factory.py
├── statistics.py
├── validator.py
└── README.md
```

---

## Author

OGS Smart Money AI