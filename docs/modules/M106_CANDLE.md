# M106_CANDLE.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M106 |
| Module Name | Candle |
| Package | ogs.market.candle |
| Category | Market Foundation |
| Status | COMPLETE |

---

# Purpose

Represents an immutable OHLCV market candle. The Candle module validates price consistency and guarantees that every candle satisfies fundamental market rules before it can be used by analytical components.

---

# Responsibilities

- Store OHLCV data.
- Validate price relationships.
- Validate symbol consistency.
- Validate volume.
- Provide immutable candle objects.

---

# Data Fields

- Symbol
- Timeframe
- Timestamp
- Open
- High
- Low
- Close
- Volume

---

# Validation Rules

- Open symbol must match candle symbol.
- High symbol must match candle symbol.
- Low symbol must match candle symbol.
- Close symbol must match candle symbol.
- High ≥ Open
- High ≥ Close
- High ≥ Low
- Low ≤ Open
- Low ≤ Close
- Volume ≥ 0

---

# Design Notes

- Immutable value object.
- Validation performed during construction.
- Suitable as the foundation for all Smart Money analysis.

---

# Used By

- Swing Detection
- BOS
- CHOCH
- Order Block
- Liquidity
- Mitigation
- Breaker Block