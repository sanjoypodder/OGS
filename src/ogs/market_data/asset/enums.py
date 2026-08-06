"""
OGS Smart Money AI

Asset Enums
"""

from __future__ import annotations

from enum import Enum


class AssetType(Enum):
    """
    Financial asset type.
    """

    UNKNOWN = "UNKNOWN"

    EQUITY = "EQUITY"

    ETF = "ETF"

    INDEX = "INDEX"

    FOREX = "FOREX"

    CRYPTO = "CRYPTO"

    COMMODITY = "COMMODITY"

    FUTURE = "FUTURE"

    OPTION = "OPTION"

    BOND = "BOND"

    MUTUAL_FUND = "MUTUAL_FUND"

    OTHER = "OTHER"