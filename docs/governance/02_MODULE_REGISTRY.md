# OGS SMART MONEY AI
# Module Registry

---

## Purpose

The Module Registry is the authoritative catalogue of every module in OGS.

Every module must appear exactly once in this document.

A module is not considered part of the project until it has been registered here.

---

# Module Status

| Status | Meaning |
|---------|---------|
| PLANNED | Not started |
| DESIGN | Architecture phase |
| DEVELOPMENT | Coding in progress |
| TESTING | Under testing |
| REVIEW | Under review |
| COMPLETE | Production ready |
| DEPRECATED | Kept for compatibility |
| REMOVED | Removed from project |
| BLOCKED | Waiting on dependency |

---

# Definition of Complete

A module is COMPLETE only if every item below is finished.

- Domain
- DTO
- Enums
- Collection
- Analyzer
- Validator
- Statistics
- Interfaces
- Exceptions
- Package exports
- README
- Unit Tests
- Integration Tests
- Documentation
- ADR
- Manifest Updated

---

# MODULE REGISTRY

| ID | Module | Package | Category | Status | Version | Depends On | Used By | Tests | ADR | Owner |
|----|--------|---------|----------|--------|---------|------------|---------|-------|-----|-------|
| M001 | Configuration | core | Foundation | COMPLETE | 1.0 | - | All | ✔ | ADR-0001 | OGS |
| M002 | Constants | core | Foundation | COMPLETE | 1.0 | - | All | ✔ | ADR-0001 | OGS |
| M003 | Version | core | Foundation | COMPLETE | 1.0 | Configuration | All | ✔ | ADR-0001 | OGS |
| M004 | Logger | core | Foundation | COMPLETE | 1.0 | Configuration | All | ✔ | ADR-0002 | OGS |
| M005 | Environment | core | Foundation | COMPLETE | 1.0 | Configuration | All | ✔ | ADR-0003 | OGS |
| M006 | Application | core | Foundation | COMPLETE | 1.0 | Logger | All | ✔ | ADR-0008 | OGS |

---

## Market Layer

| ID | Module | Package | Status | Depends On | Used By |
|----|--------|---------|--------|------------|---------|
| M100 | Symbol | market | COMPLETE | - | Price, Candle |
| M101 | Symbol Registry | market | COMPLETE | Symbol | Price |
| M102 | Timeframe | market | COMPLETE | - | Candle |
| M103 | Trading Session | market | COMPLETE | Timeframe | Candle |
| M104 | Price | market | COMPLETE | Symbol | Candle |
| M105 | Candle | market | COMPLETE | Price | Swing |
| M106 | Candle Series | market | COMPLETE | Candle | All |

---

## Smart Money Layer

| ID | Module | Status | Depends On |
|----|--------|--------|------------|
| M200 | Swing | COMPLETE | Candle Series |
| M201 | BOS | COMPLETE | Swing |
| M202 | CHOCH | COMPLETE | BOS |
| M203 | Order Block | COMPLETE | CHOCH |
| M204 | Equal High | COMPLETE | Swing |
| M205 | Equal Low | COMPLETE | Swing |
| M206 | Buy Side Liquidity | COMPLETE | Equal High |
| M207 | Sell Side Liquidity | COMPLETE | Equal Low |
| M208 | Liquidity Sweep | COMPLETE | Liquidity |
| M209 | Liquidity Void | COMPLETE | Candle |
| M210 | Mitigation | COMPLETE | Order Block |
| M211 | Breaker Block | COMPLETE | Mitigation |
| M212 | Fair Value Gap | PLANNED | Breaker Block |
| M213 | Premium Discount | PLANNED | FVG |
| M214 | Dealing Range | PLANNED | Premium Discount |
| M215 | OTE | PLANNED | Dealing Range |
| M216 | Market Narrative | PLANNED | OTE |

---

## Engine Layer

| ID | Module | Status |
|----|--------|--------|
| M300 | Market Structure Engine | COMPLETE |
| M301 | Liquidity Engine | COMPLETE |
| M302 | Smart Money Engine | COMPLETE |
| M303 | Strategy Engine | PLANNED |
| M304 | Risk Engine | PLANNED |
| M305 | Execution Engine | PLANNED |
| M306 | AI Engine | PLANNED |

---

# Naming Rules

Module IDs are permanent.

Once assigned they are never reused.

Example

M001

will always mean Configuration.

---

# Future Modules

Reserve IDs

M400–M499

Indicators

M500–M599

Broker Integration

M600–M699

Backtesting

M700–M799

Artificial Intelligence

M800–M899

UI

M900–M999

Experimental

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | Initial Registry | Created |