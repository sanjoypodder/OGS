# OGS Smart Money AI

## Market Module

The **Market** module represents a complete financial market within the OGS Smart Money AI framework.

A Market is the highest-level aggregation object in the Market Data package and owns one or more Exchanges.

Examples:

- Indian Equity Market
- US Equity Market
- Crypto Market
- Forex Market
- Commodity Market

### Features

- Market metadata
- Exchange management
- Market status
- Aggregated broker/account statistics
- Aggregated portfolio metrics
- Validation
- Factory creation
- Collection support
- Statistics
- Analyzer

### Module Structure

```
Market
 ├── Exchange
 │    ├── Broker
 │    │     ├── Account
 │    │     │     ├── Portfolio
 │    │     │     │      ├── Position
 │    │     │     │      │      └── Trade
```

The Market module follows the same architecture and coding standards as all other OGS Market Data modules.