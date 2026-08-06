"""
OGS Smart Money AI

Instrument Enums
"""

from __future__ import annotations

from enum import Enum


class InstrumentType(Enum):
    """
    Instrument categories.
    """

    UNKNOWN = "UNKNOWN"

    EQUITY = "EQUITY"

    ETF = "ETF"

    INDEX = "INDEX"

    FOREX = "FOREX"

    CRYPTO = "CRYPTO"

    FUTURE = "FUTURE"

    OPTION = "OPTION"

    COMMODITY = "COMMODITY"

    BOND = "BOND"

    CFD = "CFD"

    OTHER = "OTHER"


class InstrumentStatus(Enum):
    """
    Trading status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    SUSPENDED = "SUSPENDED"

    HALTED = "HALTED"

    EXPIRED = "EXPIRED"

    DELISTED = "DELISTED"

    CLOSED = "CLOSED"