# M003_VERSION.md

# ==========================================================
# MODULE CARD
# ==========================================================

## Module Information

| Field | Value |
|------|-------|
| Module ID | M003 |
| Module Name | Version |
| Package | ogs.core.version |
| Category | Foundation |
| Version | 1.0.0 |
| Status | COMPLETE |
| Owner | Om Ganapati Solution |

---

# Purpose

The Version module provides a centralized and immutable representation of the application's version information. It follows Semantic Versioning (SemVer) principles and exposes both short and detailed version formats for use throughout the OGS platform.

---

# Responsibilities

- Maintain application version information.
- Generate semantic version strings.
- Generate full release version strings.
- Prevent accidental modification of version data.
- Provide a single global version instance.

---

# Public API

## Class

```python
Version
```

## Global Instance

```python
VERSION
```

## Properties

| Property | Return Type | Description |
|----------|-------------|-------------|
| short | str | Semantic version (`major.minor.patch`) |
| full | str | Full version (`major.minor.patch-stage.build`) |

---

# Version Components

| Field | Type | Default |
|------|------|---------|
| major | int | 0 |
| minor | int | 1 |
| patch | int | 0 |
| stage | str | alpha |
| build | int | 1 |

---

# Generated Formats

### Short Version

```
0.1.0
```

### Full Version

```
0.1.0-alpha.1
```

---

# Dependencies

## Depends On

- dataclasses

## Used By

- Configuration Module
- Command Line Interface
- Logging
- About Dialog
- Documentation
- Release Management
- Build System

---

# Design Notes

- Implemented as a frozen dataclass to guarantee immutability.
- Uses `slots=True` for improved memory efficiency.
- Separates version components from presentation using computed properties.
- Exposes a singleton (`VERSION`) to ensure consistent version reporting throughout the application.

---

# Versioning Strategy

The module follows Semantic Versioning (SemVer):

```
MAJOR.MINOR.PATCH-STAGE.BUILD
```

Example:

```
0.1.0-alpha.1
```

Where:

- **Major** – Breaking changes
- **Minor** – New features
- **Patch** – Bug fixes
- **Stage** – Development stage (alpha, beta, rc, stable)
- **Build** – Build number

---

# Strengths

- Immutable design.
- Strongly typed.
- Centralized version management.
- Easy to extend.
- Consistent formatting through properties.

---

# Future Enhancements

- Add release date metadata.
- Add Git commit hash integration.
- Add branch name information.
- Support automatic build number generation.
- Include compatibility/version requirements for dependencies.

---

# Test Checklist

- [ ] Default version values initialize correctly.
- [ ] `short` returns semantic version format.
- [ ] `full` returns complete version string.
- [ ] Object is immutable (`frozen=True`).
- [ ] Singleton instance is available.

---

# Definition of Complete

| Item | Status |
|------|:------:|
| Implementation | ✅ |
| Documentation | ✅ |
| Public API Documented | ✅ |
| Dependencies Identified | ✅ |
| Version Strategy Defined | ✅ |

---

# Source File

```
src/ogs/core/version.py
```

---