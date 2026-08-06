"""
Liquidity Void Direction Enumeration
"""

from enum import Enum


class LiquidityVoidDirection(Enum):
    """
    Direction of a Liquidity Void.
    """

    BULLISH = "Bullish"
    BEARISH = "Bearish"