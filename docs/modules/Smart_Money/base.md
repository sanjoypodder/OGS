# Smart Money Base Framework

**Package Name:** Base

**Package Path:** `src/ogs/smart_money/base`

**Version:** 0.0.1

---

# Overview

The **Base** package provides the foundational abstractions for the Smart Money Framework. Rather than implementing Smart Money Concepts (SMC) directly, it establishes the common interfaces, abstract classes, collections, exception hierarchy, validation contracts, and statistical foundations upon which all Smart Money components are built.

Every major Smart Money module—including Swing, BOS, CHOCH, Order Block, Fair Value Gap, Liquidity, Mitigation, Breaker, and Imbalance—depends on the abstractions defined in this package.

The package follows a framework-oriented design that promotes consistency, reusability, extensibility, and strong separation between infrastructure and domain-specific trading logic. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

---

# Design Goals

The Base package has the following objectives:

- Provide common abstractions for all Smart Money modules.
- Standardize analysis, detection, and validation workflows.
- Define reusable interfaces using generic programming.
- Establish a common exception hierarchy.
- Support future extension without modifying existing contracts.
- Minimize coupling between Smart Money components.

---

# Package Structure

```
smart_money/base
│
├── analyzer.py
├── collection.py
├── detector.py
├── exceptions.py
├── interfaces.py
├── statistics.py
└── validator.py
```

---

# Package Components

## 1. BaseAnalyzer

Defines the abstract interface for all Smart Money analyzers.

Responsibilities include:

- accepting input data
- performing analytical processing
- returning analysis results

This class serves as the foundation for every analytical component implemented within the Smart Money Framework. :contentReference[oaicite:2]{index=2}

---

## 2. BaseCollection

Provides a generic collection abstraction used to store Smart Money objects.

Features include:

- iteration
- indexing
- length calculation
- first element access
- last element access
- empty state checking

The implementation follows standard Python collection conventions while providing convenience properties for framework consumers. :contentReference[oaicite:3]{index=3}

---

## 3. BaseDetector

Defines the abstract contract for pattern detection.

Every Smart Money detector derives from this abstraction and implements the detection algorithm appropriate for its domain. :contentReference[oaicite:4]{index=4}

---

## 4. Exception Hierarchy

The package defines a dedicated exception hierarchy for Smart Money operations.

```
Exception
    │
    └── SmartMoneyError
            │
            ├── ValidationError
            └── AnalysisError
```

This hierarchy separates Smart Money errors from generic Python exceptions and provides a consistent error model for the framework. :contentReference[oaicite:5]{index=5}

---

## 5. Interfaces

The package currently defines an analyzer protocol using Python's `Protocol`.

This enables structural typing, allowing objects to satisfy the analyzer contract without inheriting from a common base class. :contentReference[oaicite:6]{index=6}

---

## 6. BaseStatistics

Provides the common base class for statistical objects used throughout the Smart Money Framework.

The current implementation is intentionally minimal and serves as the foundation for future statistics implementations. :contentReference[oaicite:7]{index=7}

---

## 7. BaseValidator

Defines the abstract validation contract used by Smart Money components.

Concrete validators implement domain-specific validation while adhering to a consistent interface. :contentReference[oaicite:8]{index=8}

---

# Architecture

```
                Smart Money Base
                       │
       ┌───────────────┼───────────────┐
       │               │               │
 BaseAnalyzer    BaseDetector   BaseValidator
       │               │               │
       └───────────────┼───────────────┘
                       │
                Smart Money Modules
                       │
    ┌──────────┬─────────┬──────────┬─────────┐
    │          │         │          │
  Swing       BOS      CHOCH   Order Block ...
```

---

# Dependency Overview

The Base package is intended to be imported by all Smart Money packages.

It has **no dependency on Swing, BOS, CHOCH, Liquidity, or any other business module**.

This establishes a one-way dependency model:

```
Base
   ▲
   │
   ├── Swing
   ├── BOS
   ├── CHOCH
   ├── Order Block
   ├── Liquidity
   ├── Fair Value Gap
   ├── Breaker
   └── ...
```

---

# Design Principles

The implementation demonstrates several key design principles:

- Abstract Base Classes (ABC)
- Generic Programming
- Structural Typing using Protocol
- Framework-first architecture
- Separation of contracts from implementations
- Reusable collection abstractions
- Centralized exception handling

---

# Current Implementation Status

| Component | Status |
|----------|--------|
| Analyzer | Implemented |
| Collection | Implemented |
| Detector | Implemented |
| Exceptions | Implemented |
| Interfaces | Implemented |
| Statistics | Initial implementation |
| Validator | Implemented |

---

# Future Extensions

As the Smart Money Framework evolves, this package may be extended with additional infrastructure components such as:

- common factories
- shared utilities
- execution context
- dependency injection support
- lifecycle management

These enhancements should preserve the existing public contracts to maintain backward compatibility.

---

# Summary

The **Base** package forms the architectural foundation of the Smart Money Framework. It defines the reusable contracts and infrastructure required by higher-level Smart Money modules while intentionally avoiding domain-specific trading logic. This separation promotes modularity, extensibility, and consistent implementation across the framework.