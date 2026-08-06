"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class SellSideLiquidityType(StrEnum):
    """
    Sell-side liquidity classification.
    """

    ACTIVE = "ACTIVE"
    SWEPT = "SWEPT"