# M001_CONFIGURATION.md

# ==========================================================
# MODULE CARD
# ==========================================================

## Module Information

| Field | Value |
|------|-------|
| Module ID | M001 |
| Module Name | Configuration |
| Package | ogs.core.config |
| Category | Foundation |
| Version | 1.0.0 |
| Status | COMPLETE |
| Owner | Om Ganapati Solution |

---

# Purpose

The Configuration module provides the centralized application configuration for OGS Smart Money AI. It defines the application's runtime settings and exposes a single configuration object that is accessible throughout the system.

---

# Responsibilities

- Store application metadata.
- Store runtime configuration.
- Provide default trading parameters.
- Provide default timezone.
- Provide logging configuration.
- Expose a single global configuration instance.

---

# Public API

## Class

```python
AppConfig
```

## Global Instance

```python
CONFIG
```

---

# Configuration Fields

| Field | Type | Default Source |
|------|------|----------------|
| app_name | str | APP_NAME |
| company | str | COMPANY |
| codename | str | CODENAME |
| version | str | VERSION.full |
| debug | bool | True |
| log_level | str | INFO |
| theme | str | Dark |
| timezone | str | DEFAULT_TIMEZONE |
| default_symbol | str | DEFAULT_SYMBOL |
| default_timeframe | str | DEFAULT_TIMEFRAME |

---

# Dependencies

## Depends On

- ogs.core.constants
- ogs.core.version
- dataclasses

## Used By

All application modules.

---

# Design Notes

- Implemented using a Python `@dataclass`.
- Uses `slots=True` to reduce memory usage and prevent dynamic attribute creation.
- Uses `default_factory` for the version field so the current project version is resolved during object creation.
- Exposes a singleton instance (`CONFIG`) for consistent access across the application.

---

# Configuration Defaults

| Property | Default |
|----------|---------|
| Debug | True |
| Log Level | INFO |
| Theme | Dark |

---

# Strengths

- Single source of configuration.
- Strongly typed configuration model.
- Lightweight implementation.
- Easy to extend.
- Centralized default values.

---

# Future Enhancements

- Load configuration from `.env`.
- Support YAML configuration files.
- Environment-specific profiles (Development, Testing, Production).
- Runtime configuration validation.
- Configuration serialization/deserialization.

---

# Test Checklist

- [ ] Default values are initialized correctly.
- [ ] Version is populated correctly.
- [ ] Singleton instance is available.
- [ ] Configuration object is immutable where required.
- [ ] Default symbol and timeframe load correctly.

---

# Definition of Complete

| Item | Status |
|------|:------:|
| Implementation | ✅ |
| Documentation | ✅ |
| Dependencies Identified | ✅ |
| Public API Documented | ✅ |
| Future Improvements Listed | ✅ |

---

# Source File

```
src/ogs/core/config.py
```

---
