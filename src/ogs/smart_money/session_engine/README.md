# Session Engine

## Overview

The Session Engine provides centralized management of trading sessions
for the OGS Smart Money AI framework.

It determines the active trading session, trading day, tradability,
and session state for a given timestamp.

---

# Supported Sessions

| Session | UTC |
|----------|-----|
| Asian | 00:00 - 03:00 |
| London | 07:00 - 10:00 |
| New York | 12:00 - 15:00 |
| London Close | 15:00 - 17:00 |

---

# Features

- Trading Day Detection
- Session Detection
- Session State Detection
- Active Session Detection
- Tradable Session Detection
- Weekend Detection
- Statistics
- Collection Support
- Factory Validation
- Immutable Domain Objects

---

# Package Structure

```
session_engine/
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

# Architecture

```
Timestamp
     │
     ▼
SessionAnalyzer
     │
     ▼
Session
     │
     ▼
SessionSeries
     │
     ▼
SessionStatistics
```

---

# Usage

```python
from datetime import datetime

from ogs.smart_money.session_engine import SessionAnalyzer

analyzer = SessionAnalyzer()

series = analyzer.analyze(
    symbol="XAUUSD",
    timestamp=datetime.utcnow(),
)

active = analyzer.active(
    symbol="XAUUSD",
    timestamp=datetime.utcnow(),
)
```

---

# Statistics

The statistics class provides:

- Total Sessions
- Active Sessions
- Tradable Sessions
- Closed Sessions
- Pre-open Sessions
- Session Counts
- Trading Day Counts
- Average Duration
- Latest Session
- Oldest Session
- Current Active Session

---

# Validation

Each Session must satisfy:

- Symbol exists
- Session exists
- State exists
- Trading Day exists
- Timezone exists
- Start Time exists
- End Time exists
- End Time > Start Time

---

# Complexity

Analyzer

- Time Complexity: **O(n)**

Statistics

- Time Complexity: **O(n)**

Validator

- Time Complexity: **O(1)**

---

# Version

Version **1.0.0**

Author **Om Ganapati Solution**

Project **OGS Smart Money AI**