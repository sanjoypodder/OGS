# SMT Divergence

## Overview

The SMT (Smart Money Technique) Divergence module detects divergence between two correlated financial instruments.

It compares synchronized swing points from two markets and identifies situations where one market confirms a higher high or lower low while the other fails to do so.

This behavior is frequently used in Smart Money Concepts (SMC) trading to identify potential market reversals and liquidity shifts.

---

## Features

- Bullish SMT Divergence detection
- Bearish SMT Divergence detection
- Hidden Bullish SMT Divergence detection
- Hidden Bearish SMT Divergence detection
- Confidence classification
- Collection management
- Statistics generation
- Factory validation
- Immutable domain model
- Fully unit tested

---

## Package Structure

```
smt_divergence/
│
├── __init__.py
├── analyzer.py
├── collection.py
├── domain.py
├── enums.py
├── factory.py
├── statistics.py
├── validator.py
└── README.md
```

---

## Divergence Types

### Bullish SMT

The first market creates a Lower Low while the second market creates a Higher Low.

Expected outcome:

- Selling pressure weakening
- Possible bullish reversal

---

### Bearish SMT

The first market creates a Higher High while the second market creates a Lower High.

Expected outcome:

- Buying pressure weakening
- Possible bearish reversal

---

### Hidden Bullish SMT

The first market creates a Higher Low while the second market creates a Lower Low.

Expected outcome:

Continuation of bullish trend.

---

### Hidden Bearish SMT

The first market creates a Lower High while the second market creates a Higher High.

Expected outcome:

Continuation of bearish trend.

---

## Architecture

```
Swing Points
      │
      ▼
SMTDivergenceAnalyzer
      │
      ▼
SMTDivergence
      │
      ▼
SMTDivergenceSeries
      │
      ▼
SMTDivergenceStatistics
```

---

## Usage

```python
analyzer = SMTDivergenceAnalyzer()

result = analyzer.analyze(
    btc_swings,
    eth_swings,
)

print(len(result))
```

---

## Returned Object

Each detected divergence contains:

- first_symbol
- second_symbol
- first_price
- second_price
- comparison
- direction
- timestamp
- confidence

---

## Statistics

The statistics class provides:

- Total divergence count
- Bullish count
- Bearish count
- Hidden Bullish count
- Hidden Bearish count
- High confidence count
- Medium confidence count
- Low confidence count
- Latest divergence
- Oldest divergence

---

## Validation Rules

A divergence is considered valid when:

- symbols are present
- symbols are different
- prices are positive
- direction exists
- comparison exists
- timestamp exists
- confidence exists

---

## Unit Test Coverage

| Component | Tests |
|-----------|------:|
| Package | 2 |
| Domain | 14 |
| Validator | 13 |
| Factory | 13 |
| Collection | 11 |
| Statistics | 11 |
| Analyzer Basic | 6 |
| Analyzer Detection | 8 |
| Analyzer Edge Cases | 12 |
| Analyzer Performance | 5 |
| **Total** | **95** |

All tests are passing.

---

## Complexity

Analyzer

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

Statistics

- Time Complexity: **O(n)**

Validator

- Time Complexity: **O(1)**

---

## Version

Version: 1.0.0

Author: Om Ganapati Solution

Project: OGS Smart Money AI