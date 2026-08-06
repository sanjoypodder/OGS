# M104_SYMBOL_INFO.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M104 |
| Module Name | Symbol Information |
| Package | ogs.market.symbol_info |
| Category | Market Foundation |
| Status | COMPLETE |

---

# Purpose

Represents immutable metadata describing a tradable financial instrument.

---

# Responsibilities

- Store trading metadata.
- Define tick size.
- Define pip size.
- Define price precision.
- Define contract size.
- Store display information.

---

# Data Fields

- Symbol
- Asset Class
- Tick Size
- Pip Size
- Price Precision
- Contract Size
- Display Name
- Currency

---

# Design Notes

- Immutable (`frozen=True`)
- Memory optimized (`slots=True`)
- Value Object