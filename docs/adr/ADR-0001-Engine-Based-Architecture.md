# ADR-0001 - Engine-Based Modular Architecture

## Status

Accepted

---

## Date

11 July 2026

---

## Context

OGS Smart Money AI is designed as a long-term institutional trading platform.

The system will eventually contain multiple analysis engines including:

- Market Structure Engine
- Liquidity Engine
- Order Block Engine
- Fair Value Gap Engine
- Risk Engine
- AI Engine

A common architecture is required to ensure consistency, maintainability, and scalability.

---

## Decision

Every analysis component shall inherit from a common `BaseEngine` class.

Each engine must implement the following lifecycle:

- initialize()
- analyze()
- reset()
- shutdown()

No engine is allowed to call another engine directly.

Communication between engines will eventually occur through shared models and the Event Bus.

---

## Consequences

Advantages

- Consistent architecture
- Easier testing
- Plug-and-play engines
- Better scalability
- Cleaner code
- Easier debugging

Disadvantages

- Slightly more boilerplate code
- Requires careful interface design

---

## Approved By

Om Ganapati Solution (OGS)

Project GARUDA
