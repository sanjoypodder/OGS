# M007_SERVICE_CONTAINER.md

## Module Information

| Field | Value |
|------|-------|
| Module ID | M007 |
| Module Name | Service Container |
| Package | ogs.core.service_container |
| Category | Foundation |
| Status | COMPLETE |

---

# Purpose

Provides a lightweight dependency injection container for registering and resolving shared services during application execution.

---

# Responsibilities

- Register services.
- Resolve services.
- Check service existence.
- Remove services.
- Clear registry.
- Report service count.

---

# Public API

| Method | Description |
|--------|-------------|
| register() | Register service |
| resolve() | Resolve service |
| has() | Check registration |
| remove() | Remove service |
| clear() | Remove all services |
| count | Number of registered services |

---

# Design Notes

- Dictionary-backed registry.
- Prevents duplicate registration.
- Raises explicit `KeyError` for invalid operations.
- Lightweight implementation with no external dependencies.

---

# Future Enhancements

- Lazy service factories.
- Singleton and transient lifetimes.
- Automatic dependency injection.
- Interface-based registration.
