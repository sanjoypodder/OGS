"""
OGS Smart Money AI

Index Enums
"""

from __future__ import annotations

from enum import Enum


class IndexType(Enum):
    """
    Index classification.
    """

    UNKNOWN = "UNKNOWN"

    BROAD_MARKET = "BROAD_MARKET"

    SECTOR = "SECTOR"

    THEMATIC = "THEMATIC"

    STRATEGY = "STRATEGY"

    VOLATILITY = "VOLATILITY"

    BOND = "BOND"

    COMMODITY = "COMMODITY"

    CRYPTO = "CRYPTO"

    CUSTOM = "CUSTOM"


class IndexStatus(Enum):
    """
    Index status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    DELISTED = "DELISTED"