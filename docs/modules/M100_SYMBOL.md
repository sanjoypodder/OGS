# M100_SYMBOL.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M100 |
| Module Name | Symbol |
| Package | ogs.market.symbol |
| Category | Market Foundation |
| Status | COMPLETE |

---

# Purpose

Defines all supported tradable instruments and their asset classes. The module provides a strongly typed representation of market symbols and helper properties for asset classification.

---

# Responsibilities

- Define supported trading symbols.
- Define asset classes.
- Map every symbol to its asset class.
- Provide classification helpers.

---

# Asset Classes

- FOREX
- METAL
- CRYPTO
- INDEX
- STOCK
- COMMODITY

---

# Supported Symbols

### Metals

- XAUUSD
- XAGUSD

### Crypto

- BTCUSD
- ETHUSD

### Forex

- EURUSD
- GBPUSD
- USDJPY
- USDCHF
- AUDUSD
- NZDUSD
- USDCAD

### Index

- US30
- NAS100
- SPX500

---

# Public Properties

- asset_class
- is_forex
- is_crypto
- is_metal
- is_index

---

# Design Notes

- Implemented as `StrEnum`.
- Strongly typed.
- Central source of supported instruments.