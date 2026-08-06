# Kill Zones

## Overview

The Kill Zones module detects ICT trading sessions and determines
whether a given timestamp belongs to an active, upcoming, or completed
Kill Zone.

The module is fully compatible with the OGS Smart Money AI framework.

---

# Supported Kill Zones

| Kill Zone | UTC |
|-----------|-----|
| Asian | 00:00 - 03:00 |
| London | 07:00 - 10:00 |
| New York | 12:00 - 15:00 |
| London Close | 15:00 - 17:00 |

---

# Features

- Asian Kill Zone
- London Kill Zone
- New York Kill Zone
- London Close
- Session Detection
- Active Zone Detection
- Upcoming Zone Detection
- Completed Zone Detection
- Statistics
- Collection Support
- Factory Validation
- Immutable Domain Objects

---

# Package Structure

```
kill_zones/
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
KillZoneAnalyzer
     │
     ▼
KillZone
     │
     ▼
KillZoneSeries
     │
     ▼
KillZoneStatistics
```

---

# Usage

```python
from datetime import datetime

from ogs.smart_money.kill_zones import KillZoneAnalyzer

analyzer = KillZoneAnalyzer()

zones = analyzer.analyze(
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

- Total Kill Zones
- Active Count
- Upcoming Count
- Completed Count
- Asian Count
- London Count
- New York Count
- London Close Count
- Average Duration
- Latest Zone
- Oldest Zone
- Current Active Zone

---

# Validation

Each Kill Zone must satisfy:

- Symbol exists
- Zone exists
- Session exists
- Status exists
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