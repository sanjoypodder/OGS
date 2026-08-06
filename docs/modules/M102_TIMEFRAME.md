# M102_TIMEFRAME.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M102 |
| Module Name | Timeframe |
| Package | ogs.market.timeframe |
| Category | Market Foundation |
| Status | COMPLETE |

---

# Purpose

Defines all supported trading timeframes and provides utility properties for duration, labeling, classification, and hierarchical navigation.

---

# Responsibilities

- Define trading timeframes.
- Convert timeframes to minutes and seconds.
- Provide user-friendly labels.
- Distinguish intraday and higher timeframes.
- Determine the next higher timeframe.

---

# Supported Timeframes

- M1
- M5
- M15
- M30
- H1
- H4
- D1
- W1
- MN1

---

# Public API

| Property | Description |
|----------|-------------|
| minutes | Duration in minutes |
| seconds | Duration in seconds |
| label | Human-readable label |
| is_intraday | Intraday classification |
| is_higher_timeframe | Higher timeframe classification |
| next_higher | Next higher timeframe |

---

# Design Notes

Implemented as a `StrEnum`, providing both type safety and direct string values such as `"5m"` or `"1h"`.

---

# Future Enhancements

- Previous timeframe lookup.
- Timeframe comparison helpers.
- Broker-supported timeframe validation.
