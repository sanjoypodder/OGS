# Candle Module

## Overview

The Candle module is the foundation of the OGS Market Data Layer.

It provides immutable OHLCV candle objects, validation, creation,
collections, statistics, and analytical utilities that are shared across
the entire OGS Smart Money AI platform.

---

## Components

### Candle

Immutable OHLCV market data object.

### CandleFactory

Creates validated Candle instances.

### CandleValidator

Ensures every Candle satisfies OHLCV integrity rules.

### CandleSeries

Represents an ordered collection of Candle objects.

### CandleStatistics

Provides statistical summaries for CandleSeries.

### CandleAnalyzer

Provides generic candle analysis including:

- Bullish candles
- Bearish candles
- Doji candles
- Highest High
- Lowest Low
- Largest Range
- Average Close
- Direction Summary

---

## Design Principles

- Immutable domain model
- Broker independent
- Exchange independent
- Indicator independent
- Strategy independent
- Smart Money independent

The Candle module contains **only market data**.

Trading logic belongs to higher layers.

---

## Package Structure

```text
candle/

├── __init__.py
├── analyzer.py
├── collection.py
├── domain.py
├── enums.py
├── factory.py
├── README.md
├── statistics.py
└── validator.py
```

---

## Dependencies

- Python 3.12+
- Standard Library
- OGS Base Framework

---

## Author

Om Ganapati Solution

OGS Smart Money AI