# M006_EXCEPTIONS.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M006 |
| Module Name | Exceptions |
| Package | ogs.core.exceptions |
| Category | Foundation |
| Status | COMPLETE |

---

# Purpose

Provides the unified exception hierarchy for OGS. All application-specific errors inherit from `OGSError`, enabling consistent exception handling across the platform.

---

# Exception Hierarchy

```
Exception
    │
    └── OGSError
          ├── ConfigurationError
          ├── EnvironmentError
          ├── EngineError
          ├── DataError
          ├── StrategyError
          └── DatabaseError
```

---

# Responsibilities

- Define application-specific exceptions.
- Provide a common base exception.
- Improve error categorization.
- Enable centralized exception handling.

---

# Public API

| Class | Purpose |
|--------|----------|
| OGSError | Base application exception |
| ConfigurationError | Configuration failures |
| EnvironmentError | Environment validation failures |
| EngineError | Engine execution failures |
| DataError | Market data errors |
| StrategyError | Strategy failures |
| DatabaseError | Database operations |

---

# Used By

All modules.

---

# Future Enhancements

- Error codes.
- Exception metadata.
- Automatic logging integration.
