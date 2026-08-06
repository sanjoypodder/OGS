"""
===========================================================

OGS Smart Money AI

Balanced Price Range Enums

===========================================================
"""

from __future__ import annotations

from enum import Enum


class BalancedPriceRangeDirection(str, Enum):
    """
    Balanced Price Range direction.
    """

    BULLISH = "Bullish"

    BEARISH = "Bearish"

    NEUTRAL = "Neutral"