"""
OGS Smart Money AI

Market Enums
"""

from __future__ import annotations

from enum import Enum


class MarketStatus(Enum):
    """
    Overall market status.
    """

    UNKNOWN = "UNKNOWN"
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    HALTED = "HALTED"


class MarketType(Enum):
    """
    Financial market type.
    """

    EQUITY = "EQUITY"
    FOREX = "FOREX"
    CRYPTO = "CRYPTO"
    COMMODITY = "COMMODITY"
    DERIVATIVES = "DERIVATIVES"
    MIXED = "MIXED"
    OTHER = "OTHER"