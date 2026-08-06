# M101_SYMBOL_REGISTRY.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M101 |
| Module Name | Symbol Registry |
| Package | ogs.market.symbol_registry |
| Category | Market Foundation |
| Status | COMPLETE |

---

# Purpose

Provides the central registry of all supported trading instruments. It maps each trading symbol to its metadata, including asset class, tick size, pip size, price precision, contract size, display name, and settlement currency.

---

# Responsibilities

- Register supported market symbols.
- Store trading specifications.
- Provide symbol metadata.
- Serve as the single source of market definitions.

---

# Registry Contents

Each registered instrument includes:

- Trading Symbol
- Asset Class
- Tick Size
- Pip Size
- Price Precision
- Contract Size
- Display Name
- Currency

---

# Registered Symbols

| Symbol | Asset Class |
|---------|-------------|
| XAUUSD | Metal |
| BTCUSD | Crypto |
| EURUSD | Forex |

---

# Dependencies

- Symbol
- SymbolInfo
- Decimal

---

# Used By

- Price
- Candle
- Risk Engine
- Strategy Engine
- Execution Engine

---

# Strengths

- Centralized market metadata.
- Easy to extend with new instruments.
- Consistent precision across the platform.

---

# Future Enhancements

- Load symbols from YAML/JSON.
- Broker-specific symbol aliases.
- Trading session metadata.
- Margin and leverage information.
