# OGS Smart Money AI

# Contract Module

The **Contract** module represents an exchange-traded or OTC financial contract.

A Contract is the final tradable entity derived from an Instrument.

Examples:

- NIFTY24AUG25000CE
- NIFTY24AUG25000PE
- BANKNIFTY FUT AUG24
- GOLD OCT FUT
- BTCUSDT PERPETUAL

---

## Hierarchy

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

---

## Features

- Contract Metadata
- Futures
- Options
- Perpetual Contracts
- Expiry Information
- Strike Price
- Settlement Type
- Exercise Style
- Tick Size
- Lot Size
- Validation
- Factory
- Collection
- Statistics
- Analyzer

---

The Contract module follows the same architecture and coding standards as every Market Data module in the OGS Smart Money AI framework.