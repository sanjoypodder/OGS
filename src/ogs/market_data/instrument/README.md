# OGS Smart Money AI

## Instrument Module

The **Instrument** module represents a tradable financial instrument listed on a specific exchange.

An Instrument is the tradable representation of an Asset.

Examples:

- NASDAQ:AAPL
- NSE:RELIANCE
- BINANCE:BTCUSDT
- MCX:GOLD
- FOREX:EURUSD

The Instrument links together:

- Market
- Exchange
- Asset
- Trading Symbol
- Tick Size
- Lot Size
- Trading Status

---

## Features

- Instrument metadata
- Exchange specific symbol
- Trading configuration
- Validation
- Factory support
- Collection support
- Statistics
- Analyzer

---

## Module Hierarchy

```
Market
 └── Exchange
      └── Asset
            └── Instrument
                  └── Contract
```

---

## Typical Flow

```
Market
    ↓
Exchange
    ↓
Asset
    ↓
Instrument
    ↓
Contract
```

The Instrument module follows the same architecture and coding standards used throughout the OGS Smart Money AI framework.