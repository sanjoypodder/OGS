# M002_CONSTANTS.md

# ==========================================================
# MODULE CARD
# ==========================================================

## Module Information

| Field | Value |
|------|-------|
| Module ID | M002 |
| Module Name | Constants |
| Package | ogs.core.constants |
| Category | Foundation |
| Version | 1.0.0 |
| Status | COMPLETE |
| Owner | Om Ganapati Solution |

---

# Purpose

The Constants module provides a centralized location for project-wide immutable values. It defines directory paths, application metadata, default trading parameters, and standard configuration values used throughout OGS.

---

# Responsibilities

- Define project root and standard directory paths.
- Define default application settings.
- Store project identity information.
- Provide reusable constants across all modules.
- Eliminate hard-coded values from the codebase.

---

# Public API

## Path Constants

| Constant | Description |
|----------|-------------|
| PROJECT_ROOT | Root directory of the project |
| SRC_DIR | Source code directory |
| DOCS_DIR | Documentation directory |
| LOG_DIR | Log storage directory |
| DATABASE_DIR | Database directory |
| CONFIG_DIR | Configuration directory |
| TESTS_DIR | Test directory |
| KNOWLEDGE_DIR | Knowledge base directory |
| ASSETS_DIR | Static assets directory |
| RELEASES_DIR | Release artifacts directory |
| TOOLS_DIR | Development tools directory |
| SCRIPTS_DIR | Utility scripts directory |

---

## File Constants

| Constant | Description |
|----------|-------------|
| LOG_FILE | Default application log file |
| DATABASE_FILE | Default SQLite database file |

---

## Application Constants

| Constant | Value |
|----------|-------|
| APP_NAME | OGS Smart Money AI |
| COMPANY | Om Ganapati Solution |
| CODENAME | GARUDA |

---

## Trading Defaults

| Constant | Value |
|----------|-------|
| DEFAULT_SYMBOL | XAUUSD |
| DEFAULT_TIMEFRAME | 5m |
| DEFAULT_TIMEZONE | Asia/Kolkata |

---

# Dependencies

## Depends On

- pathlib.Path

## Used By

- Configuration Module
- Logging
- Database
- Market Modules
- UI
- Testing
- Any module requiring project metadata or paths

---

# Design Notes

- Uses `pathlib.Path` for platform-independent path handling.
- Computes `PROJECT_ROOT` dynamically using the current file location.
- Derives all other directories from `PROJECT_ROOT` to avoid duplicated path logic.
- Separates path constants from business constants for clarity.

---

# Design Principles

- Single source of truth.
- No hard-coded paths outside this module.
- Immutable constant values.
- Cross-platform compatibility.

---

# Future Enhancements

- Add environment-specific path overrides.
- Support configurable default symbol and timeframe.
- Add versioned resource directories if required.
- Introduce grouped constant namespaces if the number of constants grows significantly.

---

# Test Checklist

- [ ] PROJECT_ROOT resolves correctly.
- [ ] All directory paths are valid `Path` objects.
- [ ] File paths are constructed correctly.
- [ ] Default trading constants are available.
- [ ] Application metadata is accessible.

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
src/ogs/core/constants.py
```

---