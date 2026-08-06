# OGS Smart Money AI

# Provider Module

## Overview

The **Provider** module represents market data providers, brokers, exchanges,
data vendors, simulators, and historical data sources used throughout the
OGS Smart Money AI platform.

Every external data source is represented as a `Provider` object, making it
easy to manage connectivity, capabilities, latency, and provider-specific
features in a unified way.

The Provider module is a core component of the Market Data layer and is used
by multiple OGS modules including:

- Downloader
- Repository
- Cache
- WebSocket
- Live Feed
- Strategy Engine
- Market Engine
- Risk Engine

---

# Architecture

```
Provider
    │
    ├── Validator
    ├── Factory
    ├── Collection
    ├── Statistics
    └── Analyzer
```

The module follows the common OGS Framework architecture.

---

# Files

```
provider/

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

# Provider Types

The module supports multiple provider categories.

Examples include:

- Broker
- Stock Exchange
- Crypto Exchange
- Data Vendor
- Database
- CSV File
- Simulation
- Backtest

---

# Provider Information

Each Provider stores information such as:

- Provider Name
- Provider Type
- Connection Status
- Average Latency
- Live Market Support
- Historical Data Support
- WebSocket Support
- Order Execution Support
- Futures Support
- Options Support

---

# Example

```python
from ogs.market_data.provider import (
    Provider,
    ProviderType,
)

provider = Provider(
    name="FYERS",
    provider_type=ProviderType.BROKER,
    connected=True,
    latency_ms=18,
    supports_live=True,
    supports_historical=True,
    supports_websocket=True,
)
```

---

# Factory

Create Provider objects using:

- ProviderFactory.create()
- ProviderFactory.simulated()
- ProviderFactory.offline()
- ProviderFactory.clone()

---

# Collection

ProviderCollection offers utilities such as:

- connected()
- disconnected()
- fastest()
- slowest()
- by_type()
- average_latency()
- names()

---

# Statistics

ProviderStatistics computes:

- Provider Count
- Connected Providers
- Offline Providers
- Average Latency
- Provider Distribution
- Capability Statistics

---

# Analyzer

ProviderAnalyzer performs higher-level analysis including:

- Connection Analysis
- Capability Analysis
- Latency Analysis
- Provider Summary

---

# Design Principles

The Provider module follows the OGS Framework principles:

- Immutable domain objects
- Factory-based object creation
- Validation before creation
- Collection-oriented operations
- Statistical summaries
- Analyzer-driven insights
- Full type hints
- Python 3.14+
- Framework compliant

---

# Version

Current Version:

```
0.1.0
```

---

# Author

OGS Smart Money AI
Om Ganapati Solution