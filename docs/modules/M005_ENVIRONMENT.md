# M005_ENVIRONMENT.md

# ==========================================================
# MODULE CARD
# ==========================================================

## Module Information

| Field | Value |
|------|-------|
| Module ID | M005 |
| Module Name | Environment |
| Package | ogs.core.environment |
| Category | Foundation |
| Version | 1.0.0 |
| Status | COMPLETE |
| Owner | Om Ganapati Solution |

---

# Purpose

The Environment module validates the OGS runtime environment before the application starts. It ensures that the system meets all required prerequisites, preventing startup failures caused by missing dependencies, incorrect Python versions, invalid project structure, or insufficient permissions.

---

# Responsibilities

- Validate the Python runtime version.
- Verify the project root directory.
- Ensure required project directories exist.
- Validate required third-party packages.
- Check file system write permissions.
- Detect whether OGS is running inside a virtual environment.
- Report validation progress through the logging system.

---

# Public API

## Class

```python
EnvironmentManager
```

## Public Methods

| Method | Description |
|---------|-------------|
| `validate()` | Executes all environment validation checks before application startup. |

---

# Validation Pipeline

The `validate()` method executes the following checks in order:

1. Python Version
2. Project Root
3. Required Directories
4. Required Packages
5. Write Permissions
6. Virtual Environment

If any validation fails, an `EnvironmentError` is raised.

---

# Configuration

## Minimum Python Version

```text
3.14
```

## Required Packages

| Package |
|----------|
| loguru |

## Required Directories

- logs/
- database/
- config/
- docs/
- knowledge/
- tests/
- tools/
- releases/
- scripts/

---

# Dependencies

## Depends On

- `importlib`
- `platform`
- `sys`
- `ogs.core.constants`
- `ogs.core.logger`
- `ogs.core.exceptions`

## Used By

- Application Startup
- Bootstrap Process
- Initialization Pipeline

---

# Design Notes

- Centralizes all startup validation logic in a single manager.
- Creates missing project directories automatically.
- Uses dynamic package imports to verify installed dependencies.
- Performs a real write test by creating and removing a temporary file.
- Uses the logging system to provide detailed startup diagnostics.
- Stops initialization immediately if a critical validation fails.

---

# Validation Rules

| Validation | Result |
|------------|--------|
| Python Version | Must be ≥ 3.14 |
| Project Root | Must exist |
| Required Directories | Created if missing |
| Required Packages | Must be importable |
| Write Permission | Must succeed |
| Virtual Environment | Logged as Active/Not Active |

---

# Exceptions

| Exception | Condition |
|------------|-----------|
| `EnvironmentError` | Python version too low |
| `EnvironmentError` | Project root not found |
| `EnvironmentError` | Required package missing |
| `EnvironmentError` | Write permission test failed |

---

# Strengths

- Centralized startup validation.
- Self-healing directory creation.
- Clear startup diagnostics.
- Early failure detection.
- Easy to extend with additional validation steps.

---

# Future Enhancements

- Validate additional third-party packages.
- Check available disk space.
- Validate database connectivity.
- Validate configuration files.
- Verify network connectivity (optional).
- Support Development / Testing / Production profiles.

---

# Test Checklist

- [ ] Python version validation.
- [ ] Project root detection.
- [ ] Directory creation.
- [ ] Package validation.
- [ ] Permission check.
- [ ] Virtual environment detection.
- [ ] Error handling for failed validations.

---

# Definition of Complete

| Item | Status |
|------|:------:|
| Implementation | ✅ |
| Documentation | ✅ |
| Public API Documented | ✅ |
| Validation Pipeline Documented | ✅ |
| Dependencies Identified | ✅ |

---

# Source File

```text
src/ogs/core/environment.py
```

---