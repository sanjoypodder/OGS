# Candidate

**Package Name:** Candidate

**Package Path:** `src/ogs/smart_money/candidate`

**Version:** 0.0.1

---

# Overview

The **Candidate** package defines the common lifecycle model for institutional Smart Money candidates within the OGS framework.

Many Smart Money concepts initially exist as *candidates* before they become confirmed trading structures. Rather than allowing each package to implement its own lifecycle management, this package provides a reusable foundation consisting of a common candidate model and standardized status values.

The package is intentionally lightweight and serves as shared infrastructure for higher-level Smart Money modules. 

---

# Design Goals

The Candidate package is designed to:

- Standardize candidate lifecycle management.
- Provide a reusable base candidate model.
- Define common candidate states.
- Promote consistency across Smart Money modules.
- Reduce duplicated lifecycle implementations.

---

# Package Structure

```
smart_money/candidate
│
├── __init__.py
├── base_candidate.py
└── status.py
```

---

# Package Components

## BaseCandidate

`BaseCandidate` represents the common foundation for all Smart Money candidate objects.

The implementation is an immutable dataclass (`frozen=True`) with `slots=True` and currently stores a single attribute:

- candidate status

Future Smart Money candidates may extend this class while inheriting a common lifecycle representation. :contentReference[oaicite:1]{index=1}

---

## CandidateStatus

`CandidateStatus` defines the lifecycle of a Smart Money candidate.

Current lifecycle states are:

- `DETECTED`
- `VALIDATED`
- `REJECTED`

The implementation uses Python's `StrEnum`, providing readable string values while preserving enumeration semantics. :contentReference[oaicite:2]{index=2}

---

# Candidate Lifecycle

```
DETECTED
     │
     ▼
VALIDATED
```

or

```
DETECTED
     │
     ▼
REJECTED
```

The current implementation defines three lifecycle stages representing the progression of a candidate through the Smart Money detection process. :contentReference[oaicite:3]{index=3}

---

# Package Dependencies

```
Candidate
      │
      ▼
Smart Money Modules
```

The Candidate package has no dependency on BOS, Swing, CHOCH, Order Block, Liquidity, or other Smart Money implementations.

Instead, those packages may reuse the common candidate model and lifecycle definitions provided here. 

---

# Design Principles

The package follows several architectural principles:

- Immutable domain modelling.
- Shared lifecycle management.
- Framework reuse.
- Lightweight abstractions.
- Standardized state representation.

---

# Current Implementation Status

| Component | Status |
|-----------|--------|
| BaseCandidate | Implemented |
| CandidateStatus | Implemented |

---

# Summary

The **Candidate** package provides the common lifecycle infrastructure for institutional Smart Money candidates within OGS. By centralizing candidate representation and lifecycle states, it enables consistent processing across Smart Money modules while keeping business-specific detection logic separate from lifecycle management. Although intentionally small, it establishes a reusable foundation for future Smart Money components that progress from detection to validation or rejection.