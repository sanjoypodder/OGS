# OGS Smart Money AI

# Feed Module

## Overview

The **Feed** module manages real-time and historical market data feeds used
throughout the OGS Smart Money AI framework.

A Feed represents a continuous source of market data from a provider for one
or more financial instruments.

The module provides standardized objects, validation, statistics, and analysis
for monitoring feed health and performance.

---

# Architecture

```
Feed
    │
    ├── Validator
    ├── Factory
    ├── Collection
    ├── Statistics
    └── Analyzer
```

---

# Package Structure

```
feed/

    __init__.py
    enums.py
    domain.py
    validator.py
    factory.py
    collection.py
    statistics.py
    analyzer.py
```

---

# Supported Feed Types

- Live
- Historical
- Simulated
- Paper

---

# Feed Information

Each feed stores:

- Feed Name
- Feed Type
- Feed Status
- Provider
- Symbol
- Timeframe
- Latency (ms)
- Update Count
- Last Price
- Last Updated

---

# Factory

- create()
- live()
- historical()
- simulated()
- clone()

---

# Collection

- connected()
- disconnected()
- by_type()
- by_provider()
- fastest()
- slowest()

---

# Statistics

- Feed Count
- Connected Count
- Average Latency
- Total Updates
- Feed Distribution
- Provider Distribution

---

# Analyzer

- Summary
- Latency Analysis
- Connection Analysis
- Performance Analysis
- Feed Analysis

---

Version

```
0.1.0
```

---

OGS Smart Money AI

Om Ganapati Solution