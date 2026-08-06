# M105_TRADING_SESSION.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M105 |
| Module Name | Trading Session |
| Package | ogs.market.session |
| Category | Market Foundation |
| Status | COMPLETE |

---

# Purpose

Defines institutional trading sessions and their operating hours. The module provides session timing, activity status, and user-friendly labels.

---

# Supported Sessions

- Sydney
- Asian
- London
- New York
- Overlap
- Closed

---

# Public Properties

- start
- end
- is_active
- label

---

# Design Notes

- Implemented as `StrEnum`.
- Encapsulates session start and end times.
- Supports session-aware trading logic.

---

# Future Enhancements

- Timezone-aware session calculation.
- Holiday calendars.
- Daylight Saving Time adjustments.