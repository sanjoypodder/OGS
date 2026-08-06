# Tick Module

The Tick module represents the smallest unit of market data received from an
exchange or broker.

A Tick contains real-time pricing information such as Bid, Ask, Last Traded
Price (LTP), traded Volume, Timestamp and Data Provider.

This module is the foundation of all market data processing inside the
OGS Smart Money AI platform.

## Features

- Immutable Tick domain object
- Strong validation support
- Factory methods
- Collection utilities
- Statistical analysis
- Market analysis helpers
- Provider awareness
- High-performance design

## Package Structure

```
tick/
│
├── __init__.py
├── analyzer.py
├── collection.py
├── domain.py
├── enums.py
├── factory.py
├── statistics.py
└── validator.py
```

## Dependencies

- Python 3.12+
- dataclasses
- datetime
- enum
- typing

## Author

OGS Smart Money AI