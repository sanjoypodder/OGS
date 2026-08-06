"""
OGS Smart Money AI

Currency Enums
"""

from __future__ import annotations

from enum import Enum


class CurrencyType(Enum):
    """
    Currency classification.
    """

    UNKNOWN = "UNKNOWN"

    FIAT = "FIAT"

    CRYPTO = "CRYPTO"

    DIGITAL = "DIGITAL"

    COMMODITY = "COMMODITY"


class CurrencyStatus(Enum):
    """
    Currency status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    DELISTED = "DELISTED"