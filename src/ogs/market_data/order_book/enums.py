"""
OGS Smart Money AI

OrderBook Enumerations
"""

from __future__ import annotations

from enum import Enum


class OrderBookType(Enum):
    """
    Order book source type.
    """

    LIVE = "LIVE"
    HISTORICAL = "HISTORICAL"
    SIMULATED = "SIMULATED"
    PAPER = "PAPER"
    UNKNOWN = "UNKNOWN"


class OrderBookStatus(Enum):
    """
    Current order book status.
    """

    ACTIVE = "ACTIVE"
    STALE = "STALE"
    HALTED = "HALTED"
    CLOSED = "CLOSED"
    UNKNOWN = "UNKNOWN"