# M103_PRICE.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M103 |
| Module Name | Price |
| Package | ogs.market.price |
| Category | Market Foundation |
| Status | COMPLETE |

---

# Purpose

Represents an immutable market price with symbol awareness. The module guarantees precision according to the trading instrument and prevents invalid arithmetic or comparisons across different symbols.

---

# Responsibilities

- Store immutable market prices.
- Enforce instrument-specific precision.
- Support arithmetic operations.
- Support comparisons.
- Expose tick size, pip size, and precision.

---

# Public API

## Class

```python
Price
```

---

# Supported Operations

- Addition
- Subtraction
- Less Than
- Less Than or Equal
- Greater Than
- Greater Than or Equal
- Float Conversion
- String Conversion

---

# Validation Rules

Prices belonging to different symbols cannot be:

- Added
- Subtracted
- Compared

Attempting to do so raises a `ValueError`.

---

# Dependencies

- Symbol
- Symbol Registry
- Decimal

---

# Design Notes

- Immutable (`frozen=True`)
- Memory optimized (`slots=True`)
- Automatic precision normalization using market metadata.
- Symbol-safe arithmetic.

---

# Strengths

- Prevents accidental cross-symbol calculations.
- Consistent decimal precision.
- Clean value-object implementation.

---

# Future Enhancements

- Multiplication/division operators.
- Percentage calculations.
- Pip distance calculations.
- Serialization helpers.
