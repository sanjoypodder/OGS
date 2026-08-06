"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class BuySideLiquidityType(StrEnum):
    """
    Buy-side liquidity classification.
    """

    ACTIVE = "ACTIVE"
    SWEPT = "SWEPT"