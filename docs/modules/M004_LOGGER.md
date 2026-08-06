# M004_LOGGER.md

# ==========================================================
# MODULE CARD
# ==========================================================

## Module Information

| Field | Value |
|------|-------|
| Module ID | M004 |
| Module Name | Logger |
| Package | ogs.core.logger |
| Category | Foundation |
| Version | 1.0.0 |
| Status | COMPLETE |
| Owner | Om Ganapati Solution |

---

# Purpose

The Logger module provides the centralized logging infrastructure for OGS Smart Money AI. It configures and manages the global application logger, ensuring consistent logging behaviour across every module.

---

# Responsibilities

- Configure application logging.
- Create the log directory automatically.
- Provide colored console output.
- Persist logs to rotating log files.
- Prevent duplicate logger initialization.
- Expose a single global logger instance.

---

# Public API

## Functions

| Function | Description |
|----------|-------------|
| `configure_logger()` | Initializes the global logging system. Safe to call multiple times. |
| `get_logger()` | Returns the configured global logger instance. |

---

# Logging Configuration

## Console Output

| Property | Value |
|----------|-------|
| Level | INFO |
| Colorized | Yes |
| Queue Enabled | Yes |
| Backtrace | Enabled |
| Diagnose | Enabled |

---

## File Output

| Property | Value |
|----------|-------|
| File | `logs/ogs.log` |
| Level | DEBUG |
| Rotation | 10 MB |
| Retention | 30 Days |
| Compression | ZIP |
| Queue Enabled | Yes |

---

# Dependencies

## Depends On

- `loguru`
- `sys`
- `ogs.core.constants`

## Used By

All application modules.

---

# Design Notes

- Uses **Loguru** as the logging backend.
- Creates the log directory automatically if it does not exist.
- Removes Loguru's default handlers before applying OGS configuration.
- Uses an internal `_CONFIGURED` flag to ensure initialization occurs only once.
- `get_logger()` lazily initializes the logger if required.

---

# Design Principles

- Single global logger.
- Idempotent configuration.
- Thread-safe queued logging.
- Human-readable console logs.
- Persistent rotating log files.

---

# Strengths

- No duplicate log handlers.
- Automatic log directory creation.
- Separate console and file logging levels.
- Log rotation prevents unlimited file growth.
- Compressed archived logs reduce storage usage.

---

# Future Enhancements

- Read logging configuration from `AppConfig`.
- Support JSON log output.
- Different logging profiles (Development / Production).
- Daily log rotation option.
- Correlation IDs for request tracing.
- Structured logging for external monitoring systems.

---

# Test Checklist

- [ ] Logger initializes successfully.
- [ ] Multiple calls do not duplicate handlers.
- [ ] Log directory is created automatically.
- [ ] Console logging works.
- [ ] File logging works.
- [ ] Log rotation functions correctly.
- [ ] Archived logs are compressed.

---

# Definition of Complete

| Item | Status |
|------|:------:|
| Implementation | ✅ |
| Documentation | ✅ |
| Public API Documented | ✅ |
| Dependencies Identified | ✅ |
| Configuration Documented | ✅ |

---

# Source File

```text
src/ogs/core/logger.py
```

---